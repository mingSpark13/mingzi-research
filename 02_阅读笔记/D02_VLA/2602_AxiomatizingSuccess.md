---
title: "Axiomatizing Success: Semantic Digital Twins and Typed Predicates for Robot Manipulation"
authors: Multiple
arxiv: 2602.06572
date: 2026-02
institution: various
conf: arXiv
keywords: Axiomatic Success, Typed Predicates, Semantic Digital Twins, Capability Boundaries
tags: ["D02"]
domain: 通用操作
pdf_path: ../../01_论文库/具身智能/2602_AxiomatizingSuccess.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["任务与运动规划"]
---

## 🎯 题目

Axiomatizing Success of Robot Manipulation Actions

## 📝 三句摘要

1. **问题背景**：机器人操作任务缺乏 formal 的"成功标准"和"能力边界"表示，导致策略泛化和校验困难。
2. **核心方法**：用 typed predicates、physics/capability predicates 来表达身体与任务的能力边界，构建 semantic digital twins 来 formal 化任务成功条件。
3. **关键结果**：在多种 manipulation 任务上验证了 axiomatic success 表示的有效性，为可验证机器人操作提供了形式化基础。

## 💎 价值评估

- **🔬 研究价值**：Axiomatizing Success 为"意图的 formal 定义"提供了方法论，是 PMI 方向 B（意图表示学习 + feasibility checking）的最近邻工作。
- **🚀 实践价值**：typed predicates 可直接用于 PMI 的 capability validation 模块。
- **📈 扩展潜力**：可与主人的 PMI 接口结合，构建可验证的意图层。

## 🎯 可落地实验点

**实验设计**：将 axiomatic predicates 引入 PMI 的 capability validation
- 对比基线：无形式化验证的 PMI、纯学习的 feasibility 检查
- 度量指标：意图违规检测率、任务成功率、跨 embodiment 泛化
- 预期结果：形式化 predicates 应提升意图可验证性和安全性

## 🔗 知识图谱

- [[具身智能]] - 形式化验证是具身智能安全部署的基础
- [[任务与运动规划]] - 任务成功条件的 formal 表示

## 📌 待探索问题

- Typed predicates 的覆盖范围如何扩展到开放词汇和新型任务？
- Axiomatic success 与 learning-based intent 表示能否融合？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
