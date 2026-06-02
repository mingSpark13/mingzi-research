---
title: "CLIER: Closed-Loop Interactive Embodied Reasoning"
authors: Multiple
arxiv: 2404.15194
date: 2024-04
institution: various
conf: arXiv
keywords: Closed-Loop, Interactive Reasoning, Embodied AI, Non-Visual Properties, Action Consequences
tags: ["D02", "具身智能"]
summary: "CLIER 通过执行中多模态反馈持续修正推理链，是闭环具身推理和触觉驱动策略更新的重要近邻工作。"
domain: 具身智能
pdf_path: ../../01_论文库/具身智能/2404_CLIER.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["力-触融合"]
---

## 🎯 题目

CLIER: Closed-Loop Interactive Embodied Reasoning

## 📝 三句摘要

1. **问题背景**：现有具身推理系统缺乏对动作不确定后果的在线交互式推理能力，非视觉属性（触觉、力反馈）和环境变化未充分纳入推理闭环。
2. **核心方法**：CLIER 提出 modular closed-loop embodied reasoning，明确考虑非视觉属性和外界扰动，生成可执行 primitive sequence，并在执行中持续根据多模态反馈更新推理。
3. **关键结果**：在多种具身任务上验证了闭环交互推理相对于开环规划的优势。

## 💎 价值评估

- **🔬 研究价值**：CLIER 是"闭环交互推理"的标志性近邻工作，证明了多模态反馈在线更新推理的重要性。
- **🚀 实践价值**：为主人的 Body-Usage Adapter 提供了"触觉/力反馈驱动意图修正"的参考架构。
- **📈 扩展潜力**：CLIER 还没做到"身体使用参数在线更新"，这是本框架相对于 CLIER 的增量所在。

## 🎯 可落地实验点

**实验设计**：以 CLIER 为 baseline，在其上加入 Body-Usage Adapter
- 对比基线：CLIER（无身体使用参数在线更新）
- 度量指标：意图修正频率、身体使用参数变化率、任务成功率
- 预期结果：Body-Usage Adapter 应在身体状态变化时更主动调节使用策略

## 🔗 知识图谱

- [[具身智能]] - 闭环推理是具身智能的核心能力
- [[力-触融合]] - CLIER 强调非视觉属性的闭环推理

## 📌 待探索问题

- CLIER 的"primitive sequence"与主人的意图层/身体使用层的对应关系是什么？
- CLIER 是否更新了对自身身体能力的估计，还是只更新了对任务的理解？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
