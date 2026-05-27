# 贡献指南 | Contributing Guide

> 维护者：花火 🦊 | 最后更新：2026-05-17

---

## 📋 仓库定位

本仓库是**明子论文研究知识库**的公开协作版本，包含：
- 论文阅读笔记（Markdown）
- 7 个研究方向的科研进展（D01-D07）
- 知识图谱与概念索引（06_知识Wiki）
- 工作开发笔记（40_工作开发）

**不包含**：PDF 原文（体积过大，通过其他渠道分发）

---

## 🗂️ 目录结构

```
mingzi-research/
├── 02_阅读笔记/          # 论文阅读笔记（按主题分类）
│   ├── 01_机器人与具身/
│   ├── 02_世界模型与生成/
│   ├── D01_世界模型/     # 研究方向专属笔记
│   ├── D02_VLA/
│   ├── D03_空地迁移/
│   ├── D04_跨载体泛化/
│   ├── D05_数据飞轮/
│   ├── D06_空中视觉语言导航/
│   └── D07_Isaac强化学习/
├── 05_科研研究/           # 7 个研究方向 PAPER.md 草稿
│   ├── D01_世界模型/
│   ├── D02_VLA/
│   └── ...
├── 06_知识Wiki/           # 知识图谱
│   ├── concepts/          # 概念页
│   ├── comparisons/       # 对比页
│   ├── entities/          # 实体页（数据集/框架/模型）
│   ├── overview/          # 方向综述
│   └── sources/           # 论文 source 页
├── 40_工作开发/           # 工程实践笔记
├── scripts/               # 辅助脚本
└── README.md
```

---

## ✍️ 贡献规范

### 论文笔记格式

每篇笔记必须包含 YAML frontmatter：

```yaml
---
title: "论文标题"
authors: ["作者1", "作者2"]
year: 2026
venue: "ICRA/RAL/CVPR/arXiv"
arxiv: "2605.XXXXX"
tags: ["VLA", "具身智能", "D02"]
value: "⭐⭐⭐"  # 1-5星
---
```

正文结构：
1. **三句摘要**：核心贡献 + 方法 + 结果
2. **价值评估**：对研究方向的意义
3. **可落地实验点**：具体可复现的实验想法
4. **知识图谱链接**：关联的 Wiki 概念/实体

### 文件命名规范

```
YYYY-MM-DD_arXiv编号_简短标题.md
# 例：2026-05-14_2605.12167_MoLA.md
```

### 知识 Wiki 规范

- `concepts/`：通用概念，跨论文复用
- `comparisons/`：两个或多个方法的对比分析
- `entities/`：具体数据集、框架、模型的详细介绍
- `sources/`：单篇论文的 source 页，供 concepts 引用

---

## 🔄 同步流程（花火维护规则）

### 定期同步（每周至少一次）

```bash
cd ~/.openclaw/workspace/repos/mingzi-research

# 1. 拉取远端最新
git pull --rebase origin master

# 2. 同步本地 Notebook
rsync -av --delete \
  --exclude='*.pdf' \
  --exclude='*.db' \
  --exclude='*.db-shm' \
  --exclude='*.db-wal' \
  --exclude='.obsidian/' \
  ~/.openclaw/workspace/Notebook/30_论文研究/ ./

# 3. 提交并推送
git add -A
git commit -m "sync: 同步本地 Notebook 最新变动 (YYYY-MM-DD)"
git push origin master
```

### 触发条件

花火应在以下情况主动同步：
- 主人新增论文笔记后
- 研究方向 PAPER.md 有重大更新后
- 知识 Wiki 有新概念/对比页后
- 主人明确要求同步时

### 冲突处理

如遇 merge conflict：
1. 优先保留**更新的内容**（时间戳更新的版本）
2. 对于 PAPER.md 等核心文件，保留**更完整的版本**
3. 冲突解决后通知主人确认

---

## 🤝 外部协作者规范

### 提交 PR 前

1. Fork 本仓库
2. 在 `02_阅读笔记/` 对应分类下新增笔记
3. 遵循上述笔记格式规范
4. PR 标题格式：`docs: 新增 [论文标题] 笔记`

### 请求 PDF

在 Issues 中提交请求，注明：
- 论文标题
- arXiv 编号（如有）
- 用途说明

花火会在 24 小时内响应。

---

## 📊 仓库统计（自动更新）

| 指标 | 数量 |
|------|------|
| 论文笔记 | ~175 篇 |
| 研究方向 | 7 个（D01-D07） |
| 知识 Wiki 页面 | ~100+ |
| arXiv 扫描轮次 | R1 → R781 |
| 最后同步 | 2026-05-17 |

---

## 📞 联系方式

- **花火**（维护者）：bigetua@gmail.com
- **明子**（研究者）：GitHub @zhangbt6
- **Issues**：在本仓库提 Issue
