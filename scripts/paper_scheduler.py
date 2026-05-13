#!/usr/bin/env python3
"""
论文调度管理器 - paper_scheduler.py
花火的智能论文调度系统

功能：
1. 目录监控：新 PDF/笔记文件自动注册入库
2. 调度队列：按 LRU + 价值等级计算优先级，返回待扫描论文
3. 扫描记录：花火每次扫描后 report 结果，程序自动更新 db
4. 升降级：水货论文标记 D 档归档
5. 进度报告：随时查看各方向研究覆盖度

用法：
    python paper_scheduler.py next --direction D01 --limit 2    # 获取待扫描论文
    python paper_scheduler.py report --arxiv 2603.13528 ...     # 花火汇报扫描结果
    python paper_scheduler.py demote --arxiv 2601.XXXXX --reason "水货"  # 归档
    python paper_scheduler.py status --direction D01            # 查看研究进度
    python paper_scheduler.py refresh                           # 刷新所有优先级
    python paper_scheduler.py watch                             # 启动目录监控（后台）
    python paper_scheduler.py import-dir --path 05_科研研究/D01_世界模型/README.md  # 批量导入
"""

import sqlite3
import json
import os
import sys
import argparse
import re
import glob
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# ========== 配置 ==========
WORKSPACE = Path("/home/muyin/.openclaw/workspace/Notebook/30_论文研究")
DB_PATH = WORKSPACE / "paper_research.db"
NOTE_BASE = WORKSPACE / "02_阅读笔记"
PDF_BASE = WORKSPACE / "01_论文库"
D0X_BASE = WORKSPACE / "05_科研研究"

# ========== 数据库初始化 ==========
def init_db():
    """初始化数据库表"""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            arxiv_id        TEXT UNIQUE,
            title           TEXT NOT NULL,
            direction       TEXT DEFAULT 'unknown',
            value_tier      TEXT DEFAULT 'B',
            pdf_path        TEXT,
            note_path       TEXT,
            status          TEXT DEFAULT 'active',
            created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_scanned    TIMESTAMP,
            scan_count      INTEGER DEFAULT 0,
            priority_score  REAL DEFAULT 0,
            year            INTEGER,
            abstract        TEXT,
            tags            TEXT,
            source          TEXT DEFAULT 'unknown',
            last_promoted   TIMESTAMP,
            last_demoted    TIMESTAMP,
            demotion_reason TEXT
        )
    """)
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS scan_log (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            paper_id        INTEGER REFERENCES papers(id),
            scanned_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            direction       TEXT,
            round_id        TEXT,
            action          TEXT,
            findings        TEXT,
            new_insights    TEXT,
            is_new_paper    INTEGER DEFAULT 0
        )
    """)
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS dir_watch (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            watch_path      TEXT NOT NULL,
            last_check      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            files_tracked   TEXT
        )
    """)
    
    # 创建索引加速查询
    c.execute("CREATE INDEX IF NOT EXISTS idx_papers_direction ON papers(direction)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_papers_status ON papers(status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_papers_last_scanned ON papers(last_scanned)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_scan_log_paper ON scan_log(paper_id)")
    
    conn.commit()
    conn.close()
    print(f"[paper_scheduler] 数据库初始化完成: {DB_PATH}")

# ========== 工具函数 ==========
def get_conn():
    return sqlite3.connect(str(DB_PATH))

def parse_arxiv_from_filename(filename: str) -> Optional[str]:
    """从文件名解析 arXiv ID"""
    patterns = [
        r'(\d{4}\.\d{5})',       # 2603.13528
        r'(\d{2}\.\d{5})',       # 24.12345
        r'arXiv_(\d+)',           # arXiv_260313528
    ]
    for p in patterns:
        m = re.search(p, filename)
        if m:
            return m.group(1)
    return None

def extract_title_from_note(note_path: Path) -> Optional[str]:
    """从阅读笔记提取标题"""
    if not note_path.exists():
        return None
    try:
        content = note_path.read_text(encoding='utf-8')
        # 尝试从 YAML frontmatter 提取 title
        m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        if m:
            return m.group(1).strip()
        # 尝试从第一行 # 提取
        lines = content.split('\n')
        for line in lines[:5]:
            if line.startswith('# '):
                return line[2:].strip()
    except:
        pass
    return None

def guess_direction_from_path(path: str) -> str:
    """根据路径猜测方向"""
    path_lower = path.lower()
    if 'd01' in path_lower or '世界模型' in path:
        return 'D01'
    elif 'd02' in path_lower or 'vla' in path_lower:
        return 'D02'
    elif 'd03' in path_lower or '空地' in path:
        return 'D03'
    elif 'd04' in path_lower or '跨载体' in path:
        return 'D04'
    elif 'd05' in path_lower or '数据飞轮' in path:
        return 'D05'
    elif 'd06' in path_lower or '空中' in path or 'uav' in path_lower or 'vlp' in path_lower:
        return 'D06'
    elif 'd07' in path_lower or 'isaac' in path_lower or '强化学习' in path:
        return 'D07'
    elif '寒墨阁' in path or 'hanmo' in path_lower:
        return '寒墨阁'
    return 'unknown'

def days_since(dt: Optional[str]) -> float:
    """计算距离上次扫描的天数"""
    if dt is None:
        return 9999.0
    try:
        last = datetime.fromisoformat(dt.replace('Z', '+00:00'))
        now = datetime.now()
        return (now - last.replace(tzinfo=None)).total_seconds() / 86400
    except:
        return 9999.0

# ========== 优先级计算 ==========
def calculate_priority(row: tuple) -> float:
    """
    计算论文调度优先级
    row: (id, arxiv_id, title, direction, value_tier, scan_count, last_scanned, status)
    """
    id_, arxiv_id, title, direction, value_tier, scan_count, last_scanned, status = row
    
    # D档不参与正常调度
    if value_tier == 'D' or status == 'hidden':
        return -1.0
    
    value_coef = {'A': 3.0, 'B': 2.0, 'C': 1.0}.get(value_tier, 1.0)
    days = days_since(last_scanned)
    
    # 从未扫描 → 强制优先
    if last_scanned is None:
        return 9999.0
    
    # 刚扫过（<1天）→ 跳过
    if days < 1 and scan_count >= 1:
        return -1.0
    
    # LRU + 价值系数
    if days > 30:
        return days * value_coef * 2.5
    elif days > 14:
        return days * value_coef * 1.8
    elif days > 7:
        return days * value_coef * 1.2
    else:
        return days * value_coef

# ========== CLI 命令 ==========

def cmd_next(args):
    """返回待扫描论文队列"""
    conn = get_conn()
    c = conn.cursor()
    
    direction = args.direction.upper() if args.direction else None
    
    # 查所有 active 论文
    if direction:
        c.execute("""
            SELECT id, arxiv_id, title, direction, value_tier, 
                   scan_count, last_scanned, status,
                   pdf_path, note_path
            FROM papers 
            WHERE status='active' AND direction=?
            ORDER BY priority_score DESC
        """, (direction,))
    else:
        c.execute("""
            SELECT id, arxiv_id, title, direction, value_tier,
                   scan_count, last_scanned, status,
                   pdf_path, note_path
            FROM papers 
            WHERE status='active'
            ORDER BY priority_score DESC
        """)
    
    rows = c.fetchall()
    conn.close()
    
    # 重新计算优先级并排序
    scored = []
    for row in rows:
        # row: (id, arxiv_id, title, direction, value_tier, scan_count, last_scanned, status, pdf_path, note_path)
        # 取前8列传给 calculate_priority
        score = calculate_priority(row[:8])
        if score < 0:
            continue
        scored.append((score, row))
    
    # 输出
    limit = args.limit or 5
    print(f"\n=== 扫描队列 {'(' + direction + ')' if direction else '(全部)'} ===")
    print(f"{'优先级':>8} | {'方向':<6} | {'价值':<4} | {'未扫天':>6} | {'次数':>4} | 标题")
    print("-" * 100)
    
    for score, row in scored[:limit]:
        id_, arxiv_id, title, direction, value_tier, scan_count, last_scanned, status, pdf_path, note_path = row
        days = days_since(last_scanned)
        title_short = (title[:40] + '...') if title and len(title) > 40 else (title or '无标题')
        tier_icon = {'A': '⭐⭐⭐', 'B': '⭐⭐', 'C': '⭐', 'D': '🗑️'}.get(value_tier, '?')
        print(f"{score:>8.1f} | {direction:<6} | {tier_icon:<4} | {days:>6.1f} | {scan_count:>4} | {title_short}")
        
        # 额外信息
        if arxiv_id:
            print(f"         | arXiv: {arxiv_id}")
        if pdf_path:
            print(f"         | PDF: {pdf_path}")
        if note_path:
            print(f"         | 笔记: {note_path}")
        print()
    
    if not scored:
        print("无待扫描论文")
    return scored[:limit]

def cmd_report(args):
    """花火汇报扫描结果"""
    conn = get_conn()
    c = conn.cursor()
    
    # 查找论文
    arxiv_id = args.arxiv.replace('.pdf', '').strip()
    c.execute("SELECT id FROM papers WHERE arxiv_id=? OR title LIKE ?", 
              (arxiv_id, f"%{args.arxiv}%"))
    row = c.fetchone()
    
    if not row:
        print(f"[!] 未找到论文: {args.arxiv}")
        print("    请先用 import 命令注册论文")
        conn.close()
        return
    
    paper_id = row[0]
    
    # 更新论文记录
    now = datetime.now().isoformat()
    new_tier = args.new_tier.upper() if args.new_tier else None
    
    if new_tier:
        c.execute("UPDATE papers SET value_tier=? WHERE id=?", (new_tier, paper_id))
    
    c.execute("""
        UPDATE papers 
        SET last_scanned=?, scan_count=scan_count+1, priority_score=0
        WHERE id=?
    """, (now, paper_id))
    
    # 记录 scan_log
    c.execute("""
        INSERT INTO scan_log (paper_id, direction, round_id, action, findings, new_insights, is_new_paper)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (paper_id, args.direction, args.round_id, args.action, 
          args.findings, args.insights, 1 if args.is_new else 0))
    
    conn.commit()
    conn.close()
    print(f"[+] 扫描记录已更新: {args.arxiv}")
    print(f"    方向: {args.direction} | 操作: {args.action}")
    print(f"    发现: {args.findings[:60]}..." if args.findings else "")

def cmd_demote(args):
    """归档水货论文"""
    conn = get_conn()
    c = conn.cursor()
    
    arxiv_id = args.arxiv.replace('.pdf', '').strip()
    c.execute("SELECT id, title, pdf_path, note_path FROM papers WHERE arxiv_id=? OR title LIKE ?",
              (arxiv_id, f"%{args.arxiv}%"))
    row = c.fetchone()
    
    if not row:
        print(f"[!] 未找到论文: {args.arxiv}")
        conn.close()
        return
    
    paper_id, title, pdf_path, note_path = row
    now = datetime.now().isoformat()
    
    # 更新状态
    c.execute("""
        UPDATE papers 
        SET value_tier='D', status='archive', 
            last_demoted=?, demotion_reason=?
        WHERE id=?
    """, (now, args.reason, paper_id))
    
    # 移动文件到 archive
    if pdf_path and Path(pdf_path).exists():
        archive_pdf = Path(pdf_path).parent.parent / "papers" / "archive" / Path(pdf_path).name
        archive_pdf.parent.mkdir(parents=True, exist_ok=True)
        Path(pdf_path).rename(archive_pdf)
        c.execute("UPDATE papers SET pdf_path=? WHERE id=?", (str(archive_pdf), paper_id))
        print(f"[+] PDF 已归档: {archive_pdf}")
    
    if note_path and Path(note_path).exists():
        archive_note = Path(note_path).parent.parent / "papers" / "archive" / Path(note_path).name
        archive_note.parent.mkdir(parents=True, exist_ok=True)
        Path(note_path).rename(archive_note)
        c.execute("UPDATE papers SET note_path=? WHERE id=?", (str(archive_note), paper_id))
        print(f"[+] 笔记已归档: {archive_note}")
    
    conn.commit()
    conn.close()
    print(f"[+] 已归档: {title}")
    print(f"    原因: {args.reason}")

def cmd_status(args):
    """查看研究进度"""
    conn = get_conn()
    c = conn.cursor()
    
    direction = args.direction.upper() if args.direction else None
    
    if direction:
        # 指定方向的详情
        c.execute("""
            SELECT value_tier, COUNT(*) as cnt
            FROM papers
            WHERE direction=? AND status!='hidden'
            GROUP BY value_tier
        """, (direction,))
        tier_counts = dict(c.fetchall())
        
        c.execute("""
            SELECT COUNT(*) FROM papers
            WHERE direction=? AND status='active'
        """, (direction,))
        active = c.fetchone()[0]
        
        c.execute("""
            SELECT COUNT(*) FROM papers
            WHERE direction=? AND last_scanned IS NULL
        """, (direction,))
        never_scanned = c.fetchone()[0]
        
        c.execute("""
            SELECT COUNT(*) FROM papers
            WHERE direction=? AND status='archive'
        """, (direction,))
        archived = c.fetchone()[0]
        
        c.execute("""
            SELECT title, days_since_scan FROM (
                SELECT title, julianday('now') - julianday(last_scanned) as days_since_scan
                FROM papers WHERE direction=? AND last_scanned IS NOT NULL
                ORDER BY days_since_scan DESC
            ) LIMIT 5
        """, (direction,))
        oldest = c.fetchall()
        
        total = sum(tier_counts.values())
        print(f"\n=== {direction} 研究覆盖度 ===")
        print(f"论文总数: {total} | 活跃: {active} | 未扫描: {never_scanned} | 归档: {archived}")
        print(f"价值分布: A={tier_counts.get('A',0)} B={tier_counts.get('B',0)} C={tier_counts.get('C',0)} D={tier_counts.get('D',0)}")
        
        if oldest:
            print(f"\n最久未扫:")
            for title, days in oldest:
                print(f"  {days:.0f}天前: {title[:50]}")
    else:
        # 全局概览
        c.execute("""
            SELECT direction, COUNT(*) as total,
                   SUM(CASE WHEN status='active' THEN 1 ELSE 0 END) as active,
                   SUM(CASE WHEN value_tier='A' THEN 1 ELSE 0 END) as tier_a,
                   SUM(CASE WHEN value_tier='B' THEN 1 ELSE 0 END) as tier_b,
                   SUM(CASE WHEN value_tier='C' THEN 1 ELSE 0 END) as tier_c,
                   SUM(CASE WHEN value_tier='D' THEN 1 ELSE 0 END) as tier_d
            FROM papers
            GROUP BY direction
        """)
        rows = c.fetchall()
        
        print("\n=== 全局研究覆盖度 ===")
        print(f"{'方向':<8} | {'总数':>5} | {'活跃':>5} | {'A':>3} | {'B':>3} | {'C':>3} | {'D':>3}")
        print("-" * 50)
        for row in rows:
            direction, total, active, a, b, c_cnt, d = row
            print(f"{direction:<8} | {total:>5} | {active:>5} | {a or 0:>3} | {b or 0:>3} | {c_cnt or 0:>3} | {d or 0:>3}")
    
    conn.close()

def cmd_refresh(args):
    """刷新所有论文优先级"""
    conn = get_conn()
    c = conn.cursor()
    
    c.execute("""
        SELECT id, arxiv_id, title, direction, value_tier, scan_count, last_scanned, status
        FROM papers WHERE status='active'
    """)
    rows = c.fetchall()
    
    updated = 0
    for row in rows:
        score = calculate_priority(row)
        c.execute("UPDATE papers SET priority_score=? WHERE id=?", (score, row[0]))
        updated += 1
    
    conn.commit()
    conn.close()
    print(f"[+] 已刷新 {updated} 篇论文的优先级")

def cmd_import(args):
    """从 README.md 批量导入论文（精确模式）"""
    conn = get_conn()
    c = conn.cursor()
    
    readme = WORKSPACE / args.path if not Path(args.path).is_absolute() else Path(args.path)
    if not readme.exists():
        print(f"[!] 文件不存在: {readme}")
        return
    
    content = readme.read_text(encoding='utf-8')
    direction = guess_direction_from_path(str(readme))
    
    # 收集已有的 arXiv ID
    c.execute("SELECT arxiv_id FROM papers WHERE direction=?", (direction,))
    seen_ids = {row[0] for row in c.fetchall() if row[0]}
    
    imported = 0
    skipped = 0
    
    # 策略1: 从 ### 2026-04-xx Rxxx:**标题** (arXiv_ID) 【新增入库/候选】 行提取
    # 这类行格式最规范
    strict_pattern = re.compile(
        r'###\s+[0-9-]+\s+R\d+:\s+\*\*(.+?)\*\*\s*\(([0-9]{4}\.[0-9]{5})\)\s*【(新增入库|候选入库|候选|入库)】'
    )
    
    # 策略2: 从正文日志行提取，但限制只有"入库/补抓/补记"等关键词才提取
    log_pattern = re.compile(
        r'(?:入库|补抓|补记|新增入库|新增候选|新增关注)\s+\*\*(.+?)\*\*\s*\(([0-9]{4}\.[0-9]{5})\)'
    )
    
    # 策略3: 直接匹配纯论文行 `**标题** (arXiv_ID)` 但排除日志正文里的上下文
    # 只取标题超过15个字符的（过滤掉短标题/代码片段）
    
    papers_to_add = []
    
    for m in strict_pattern.finditer(content):
        title = m.group(1).strip()
        arxiv_id = m.group(2).strip()
        tag = m.group(3)
        if len(title) > 10 and arxiv_id not in seen_ids:
            papers_to_add.append((arxiv_id, title, '入库'))
    
    for m in log_pattern.finditer(content):
        title = m.group(1).strip()
        arxiv_id = m.group(2).strip()
        # 过滤掉太短的标题（可能是日志里的其他内容）
        if len(title) > 15 and arxiv_id not in seen_ids:
            # 避免重复
            if not any(p[0] == arxiv_id for p in papers_to_add):
                papers_to_add.append((arxiv_id, title, '扫描'))
    
    for arxiv_id, title, source in papers_to_add:
        if arxiv_id in seen_ids:
            skipped += 1
            continue
        c.execute("""
            INSERT INTO papers (arxiv_id, title, direction, source)
            VALUES (?, ?, ?, ?)
        """, (arxiv_id, title, direction, f'readme_import_{source}'))
        seen_ids.add(arxiv_id)
        imported += 1
    
    conn.commit()
    conn.close()
    print(f"[+] 批量导入完成: 新增 {imported} 篇, 跳过 {skipped} 篇(已存在)")
    print(f"    方向: {direction}")

def cmd_auto_register(args):
    """自动注册单个文件（供 watch 模式调用）"""
    filepath = Path(args.path)
    if not filepath.exists():
        return
    
    conn = get_conn()
    c = conn.cursor()
    
    arxiv_id = parse_arxiv_from_filename(filepath.name)
    direction = guess_direction_from_path(str(filepath))
    
    # 确定文件类型和路径字段
    if '论文库' in str(filepath) or filepath.suffix == '.pdf':
        field = 'pdf_path'
        path_val = str(filepath.relative_to(WORKSPACE))
    elif '阅读笔记' in str(filepath):
        field = 'note_path'
        path_val = str(filepath.relative_to(WORKSPACE))
        # 尝试从笔记提取标题
        title = extract_title_from_note(filepath)
    else:
        conn.close()
        return
    
    if arxiv_id:
        # 检查是否已存在
        c.execute("SELECT id FROM papers WHERE arxiv_id=?", (arxiv_id,))
        row = c.fetchone()
        if row:
            # 已存在，更新路径
            c.execute(f"UPDATE papers SET {field}=? WHERE id=?", (path_val, row[0]))
            print(f"[~] 更新路径: {arxiv_id} -> {field}")
        else:
            # 新论文
            title = extract_title_from_note(filepath) if field == 'note_path' else f"arXiv {arxiv_id}"
            c.execute("""
                INSERT INTO papers (arxiv_id, title, direction, pdf_path, note_path, source)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (arxiv_id, title or f"arXiv {arxiv_id}", direction,
                  path_val if field == 'pdf_path' else None,
                  path_val if field == 'note_path' else None,
                  'auto_detect'))
            print(f"[+] 自动注册: {arxiv_id} ({title or '无标题'})")
    else:
        # 无 arXiv ID，当作新论文注册
        title = extract_title_from_note(filepath) if field == 'note_path' else filepath.stem
        if title:
            c.execute("SELECT id FROM papers WHERE title LIKE ?", (f"%{title[:30]}%",))
            if not c.fetchone():
                c.execute(f"""
                    INSERT INTO papers (title, direction, {field}, source)
                    VALUES (?, ?, ?, ?)
                """, (title, direction, path_val, 'auto_detect'))
                print(f"[+] 自动注册(无ID): {title}")
    
    conn.commit()
    conn.close()

def cmd_watch(args):
    """启动目录监控（需要 watchdog）"""
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print("[!] 需要安装 watchdog: pip install watchdog")
        return
    
    class PaperHandler(FileSystemEventHandler):
        def on_created(self, event):
            if event.is_directory:
                return
            path = Path(event.src_path)
            # 监听 PDF 和 Markdown 文件
            if path.suffix in ['.pdf', '.md'] and ('论文库' in str(path) or '阅读笔记' in str(path)):
                print(f"\n[watch] 检测到新文件: {path.name}")
                # 调用 auto_register
                import subprocess
                subprocess.run([
                    sys.executable, __file__, 'auto-register',
                    '--path', str(path)
                ])
        
        def on_modified(self, event):
            if event.is_directory:
                return
            path = Path(event.src_path)
            if path.suffix == '.md' and '阅读笔记' in str(path):
                print(f"\n[watch] 笔记更新: {path.name}")
                import subprocess
                subprocess.run([
                    sys.executable, __file__, 'auto-register',
                    '--path', str(path)
                ])
    
    watch_paths = [str(PDF_BASE), str(NOTE_BASE)]
    
    print(f"[watch] 启动目录监控...")
    print(f"       监控: {watch_paths}")
    print(f"       按 Ctrl+C 停止")
    
    observer = Observer()
    for p in watch_paths:
        if Path(p).exists():
            observer.schedule(PaperHandler(), p, recursive=True)
    
    observer.start()
    try:
        import time
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[watch] 监控已停止")
    observer.join()

# ========== 主入口 ==========
def main():
    parser = argparse.ArgumentParser(description='论文调度管理器')
    subparsers = parser.add_subparsers(dest='cmd', help='子命令')
    
    # next
    p = subparsers.add_parser('next', help='获取待扫描论文队列')
    p.add_argument('--direction', '-d', help='方向 (D01-D07)')
    p.add_argument('--limit', '-n', type=int, default=5, help='返回数量')
    
    # report
    p = subparsers.add_parser('report', help='花火汇报扫描结果')
    p.add_argument('--arxiv', required=True, help='arXiv ID 或标题')
    p.add_argument('--direction', '-d', default='unknown', help='方向')
    p.add_argument('--action', default='复核', help='操作类型')
    p.add_argument('--findings', '-f', default='', help='发现摘要')
    p.add_argument('--insights', '-i', default='', help='判断/洞察')
    p.add_argument('--new-tier', '-t', help='新的价值等级 (A/B/C)')
    p.add_argument('--round-id', '-r', help='轮次ID (R812)')
    p.add_argument('--is-new', action='store_true', help='是否新论文首次扫描')
    
    # demote
    p = subparsers.add_parser('demote', help='归档水货论文')
    p.add_argument('--arxiv', required=True, help='arXiv ID 或标题')
    p.add_argument('--reason', required=True, help='归档原因')
    
    # status
    p = subparsers.add_parser('status', help='查看研究进度')
    p.add_argument('--direction', '-d', help='方向 (D01-D07)')
    
    # refresh
    subparsers.add_parser('refresh', help='刷新所有优先级')
    
    # import
    p = subparsers.add_parser('import', help='从 README.md 批量导入')
    p.add_argument('--path', required=True, help='README.md 路径')
    
    # auto-register
    p = subparsers.add_parser('auto-register', help='自动注册文件（内部用）')
    p.add_argument('--path', required=True, help='文件路径')
    
    # watch
    subparsers.add_parser('watch', help='启动目录监控')
    
    args = parser.parse_args()
    
    # 初始化数据库
    init_db()
    
    if args.cmd == 'next':
        cmd_next(args)
    elif args.cmd == 'report':
        cmd_report(args)
    elif args.cmd == 'demote':
        cmd_demote(args)
    elif args.cmd == 'status':
        cmd_status(args)
    elif args.cmd == 'refresh':
        cmd_refresh(args)
    elif args.cmd == 'import':
        cmd_import(args)
    elif args.cmd == 'auto-register':
        cmd_auto_register(args)
    elif args.cmd == 'watch':
        cmd_watch(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
