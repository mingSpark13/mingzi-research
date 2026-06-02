---
title: "UniGoal: Unified Goal-Oriented Navigation with Graph Matching"
authors: Hang Yin et al.
arxiv: ""
date: 2025
institution: ""
conf: CVPR 2025
keywords: unified navigation, object-goal, image-goal, text-goal, graph matching, zero-shot
tags: ["D06", "零样本泛化"]
summary: "UniGoal 用统一的图表示和图匹配机制把 object-goal、image-goal、text-goal 三类目标导航合到同一框架里，在多基准上取得零样本 SOTA。"
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["零样本泛化"]
---

## 🎯 题目

UniGoal: Unified Goal-Oriented Navigation（统一目标导航）

## 📝 三句摘要

1. **问题背景**：Object-goal、Image-goal、Text-goal 三类导航通常需要不同模型驱动，缺乏统一框架，泛化和部署成本高。
2. **核心方法**：将 goal 和 scene 都表示为 graph，通过 graph matching + 多阶段探索实现三类任务统一；单一模型在三类任务上取得 SOTA zero-shot 表现。
3. **关键结果**：在多个 benchmark 上实现三类 goal 统一导航的零样本 SOTA，泛化能力强。

## 💎 价值评估

- **🔬 研究价值**：首次实现三类 goal 导航的框架统一，为多模态目标搜索提供了通用架构。
- **🚀 实践价值**：未来可扩展到"文本找目标 + 图像找目标 + 实例级搜索"，一个模型搞定多种搜索范式。
- **📈 扩展潜力**：graph matching 机制可迁移到 3D 语义地图匹配，对无人机城市大尺度导航有潜在价值。

## 🎯 可落地实验点

**实验设计**：验证 UniGoal 在跨任务泛化上的能力：训练于 Image-goal + Text-goal，测试 Object-goal
- 对比基线：任务专用模型
- 度量指标：SR、SPL、跨任务迁移成功率
- 预期结果：UniGoal 在 unseen task 上的 SR 下降 <10%

## 🔗 知识图谱
- [[图匹配]]
- [[多任务统一]]
- [[零样本泛化]]
- [[目标表示学习]]
- [[层级探索]]

## 🔗 相关链接

- [[2024_SG-Nav_Scene_Graph_Navigation]] - SG-Nav 同作者，UniGoal 继承并扩展了 scene graph 思想
- [[2024_VLFM_Vision-Language_Frontier_Maps]] - VLFM 是零样本导航重要基线

## 📌 待探索问题

- graph matching 在大规模场景下的计算复杂度如何？是否需要层次化索引？
- 三类 goal 的统一表示如何设计才能最大限度保留各任务的独特信息？

---
**维护**: 花火 · 2026-04-12
