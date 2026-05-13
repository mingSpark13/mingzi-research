# 06_知识Wiki — L2 知识编译层

> 由 `knowledge-wiki` 技能维护，将 L1 原始笔记编译为结构化知识页面。
> 入口导航：[[index]]

## 架构版本

- **字典**: v1.1（2026-04-17）
- **一级概念**: 11 个（方向导航页）
- **二级概念**: 47 个（核心概念页）
- **别名映射**: ~200 条
- **黑名单**: ~80 条

## 目录结构

```
06_知识Wiki/
├── index.md           # 内容索引
├── log.md             # 操作日志
├── inbox.md           # 新概念候选（待审核）
├── _views/            # 字典 v1.1（唯一概念命名真源）
├── sources/           # 轻量索引页（≤25行，指回 L1）
├── concepts/          # 概念页（11 一级 + 47 二级 = 58 页）
├── comparisons/       # 方法对比
├── overview/          # 方向总览
├── entities/          # 人物/项目/工具
├── reports/           # REPORT 衍生分析
└── syntheses/         # 跨论文综合分析
```

## 核心规则

1. **字典是唯一真源**：`_views/概念关键词字典.md` 决定所有概念命名
2. **不得自行创建概念页**：字典外新概念 → 写 `inbox.md` → 知识库管理者审核
3. **sources/ ≤25 行**：轻量索引 + 增值摘要，不拷贝原始笔记
4. **origins 必须指向实际存在的 L1 文件**
5. **tags 和 related_concepts 只用字典规范名**

## 相关技能

- `skills/knowledge-wiki/SKILL.md` — 完整编译规范
- `skills/paper-manager/SKILL.md` — L1 入库规范
- `skills/paper-research/SKILL.md` — L1 研究主线规范

---
**最后更新**: 2026-04-18
