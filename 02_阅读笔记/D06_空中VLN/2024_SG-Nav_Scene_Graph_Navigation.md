---
title: "SG-Nav: Scene Graph based Navigation with Hierarchical LLM Reasoning"
tags: ["D06", "语义导航", "长程任务规划"]
summary: "SG-Nav 通过在线 3D 场景图和层级 LLM 推理提升开放词汇目标导航的成功率与可解释性。"
authors: Hang Yin et al.
arxiv: ""
date: 2024
institution: ""
conf: NeurIPS 2024
keywords: scene graph, LLM reasoning, zero-shot object navigation, hierarchical planning, re-perception
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["语义导航", "长程任务规划"]
---

## 🎯 题目

SG-Nav: Scene Graph based Navigation with Hierarchical LLM Reasoning

## 📝 三句摘要

1. **问题背景**：开放词汇目标搜索依赖单帧 VLM 决策，缺乏场景级先验（如"垃圾桶在楼道口"），导致在复杂环境或目标稀疏时效率低下。
2. **核心方法**：将观测组织为在线 3D scene graph，让 LLM 在 graph 上做层级推理，并引入 re-perception 机制纠正误识别。
3. **关键结果**：在 MP3D、HM3D、RoboTHOR 上相比先前 zero-shot 方法成功率提升超 10%，可解释性强。

## 💎 价值评估

- **🔬 研究价值**：首次将 scene graph 结构化先验引入零样本语义导航，为"场景先验推理"提供了新范式。
- **🚀 实践价值**：校园找垃圾桶/找蓝色车等任务依赖场景先验，SG-Nav 的 graph 推理比单帧决策更会"猜目标大概在哪"。
- **📈 扩展潜力**：scene graph 可与 SLAM 地图、语义地图自然结合，适合扩展到无人机城市级大范围搜索。

## 🎯 可落地实验点

**实验设计**：在校园/园区场景验证"找特定位置目标"的场景先验推理能力
- 对比基线：VLFM、CLIP on Map
- 度量指标：SR、SPL、Path Efficiency
- 预期结果：SG-Nav 在目标稀疏分布场景下 SPL 提升 >20%

## 🔗 知识图谱
- [[语义导航]]
- [[长程任务规划]]
- [[层级推理]]
- [[零样本目标导航]]
- [[重新感知]]

## 🔗 相关链接

- [[2024_VLFM_Vision-Language_Frontier_Maps]] - VLFM 是主要对比基线，SG-Nav 超越其超10%
- [[2023-06_RTM-2]] - LLM 导航领域基础工作

## 📌 待探索问题

- scene graph 的在线构建如何保证实时性？在动态环境（如人群）中 graph 稳定性如何？
- 如何让 LLM 在 graph 上的推理兼顾效率和深度，避免过度思考导致行动迟缓？

---
**维护**: 花火 · 2026-04-12
