---
title: Data Analogies Enable Efficient Cross-Embodiment Transfer
authors: Jonathan Yang, Chelsea Finn, Dorsa Sadigh
arxiv: 2603.06450
date: 2026-03-06
institution: Stanford University
conf: arXiv
keywords: [cross-embodiment transfer, paired demonstrations, data organization]
tags: ["跨载体泛化", "模仿学习", "数据合成"]
summary: "论文证明 paired demonstrations 比单纯扩大未配对异构数据更有效，直接支撑跨载体迁移中的数据组织优先级判断。"
domain: 跨载体泛化
pdf_path: "../../01_论文库/D04_跨载体泛化/2603.06450_Data_Analogies_Enable_Efficient_Cross_Embodiment_Transfer.pdf"
reading_date: 2026-05-10
reading_status: 已读
related_concepts: ["跨载体泛化", "模仿学习"]
---

# 📖 花火格式笔记

## 🎯 题目

Data Analogies Enable Efficient Cross-Embodiment Transfer

## 📝 三句摘要

1. **问题背景**：跨载体机器人策略常依赖海量异构示教，但究竟是“更多数据”还是“更成对、更可对齐的数据”更关键并不清楚。
2. **核心方法**：论文系统控制末端形态、机器人外观和相机视角三类变化，比较单纯扩充未配对示教与构造任务对应的 paired data 对跨载体迁移的影响。
3. **关键结果**：结果表明结构化 paired demonstrations 明显优于仅扩大未配对异构数据规模，说明跨载体迁移瓶颈不仅是表征能力，更是任务对应关系是否被显式暴露。

## 💎 价值评估

- **🔬 研究价值**：直接给 D04 的“数据策略”主线补上强实证，支持“paired 数据比海量未配对更值钱”的判断。
- **🚀 实践价值**：对明子后续做空地/异构平台迁移很实用，提示优先建设同任务跨载体配对数据，而不是盲目堆异构样本量。
- **📈 扩展潜力**：可进一步接到 D05 数据飞轮，用仿真自动生成 paired demo，再和 latent / morphology / dynamics 路线做正交消融。

## 🎯 可落地实验点

**实验设计**：在地面机械臂与空中操作平台之间构造同任务 paired demo，对比 paired/unpaired/mixed 三种训练组织方式。
- 对比基线：unpaired heterogeneous demos、paired demos、paired+latent retargeting
- 度量指标：Transfer Success、跨视角成功率、样本效率
- 预期结果：paired 数据在低样本 regime 下显著优于单纯扩规模，并能更清楚暴露 shared geometry 与 residual adaptation 的边界

## 🔗 知识图谱

- [[concepts/跨载体泛化]] - 本文核心问题
- [[concepts/模仿学习]] - 主要训练范式
- [[concepts/数据飞轮]] - 与 D05 可直接联动

## 🔗 相关链接

- [[2026-04-18_LAP]] - 语言-动作预训练的强零样本跨载体基线
- [[2026-04-18_Being-H0.5]] - 大规模统一动作空间跨载体路线
- [[2026-04-18_Unified_Latent_Space]] - 共享 latent 接口路线对照

## 📌 待探索问题

- paired demo 的收益主要来自几何对应、动作对应，还是视角对齐？
- paired 数据是否能减少 morphology-aware adapter 的必要性？

---
**维护**: 花火 · 2026-05-10
