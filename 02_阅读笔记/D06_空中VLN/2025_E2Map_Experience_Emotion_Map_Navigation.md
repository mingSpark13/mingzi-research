---
title: "E2Map: Experience/Emotion Map with Reflexive Behavior Adjustment for Stochastic Navigation"
authors: ""
arxiv: ""
date: 2025
institution: ""
conf: ICRA 2025
keywords: experience map, emotion map, reflexive adjustment, language navigation, user preference
tags: ["D06"]
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["语义导航"]
---

## 🎯 题目

E2Map: 经验-情感地图与自反式行为调整的随机环境导航

## 📝 三句摘要

1. **问题背景**：传统语义导航假设环境静态、目标固定，无法处理用户的个性化偏好（如"走安全的路""避开嘈杂区"）和随机环境变化。
2. **核心方法**：将 experience/emotion map 引入语义导航，支持随机环境下的一次性行为调整和用户偏好引导，可运行 custom user instruction。
3. **关键结果**：在用户偏好引导的导航任务上显著优于基准，提供了更智能的个性化导航体验。

## 💎 价值评估

- **🔬 研究价值**：首次将"用户体验/偏好"显式引入语义导航地图表示，是人机交互导航的重要探索。
- **🚀 实践价值**：适合做"带偏好/风险规避/体验引导"的智能体，与主人"探索科技、追求体验"的调性契合。
- **📈 扩展潜力**：emotion map 可与无人机的能耗偏好、飞行安全偏好结合；experience map 可用于快速任务迁移和少样本泛化。

## 🎯 可落地实验点

**实验设计**：在园区导航中引入"安全性偏好"和"时间偏好"两个维度，对比 E2Map vs 普通语义导航
- 对比基线：普通语义导航（无偏好）
- 度量指标：用户满意度、路径安全性评分、任务成功率
- 预期结果：E2Map 用户满意度 >85%，偏好匹配率 >90%

## 🔗 知识图谱
- [[经验地图]]
- [[情感地图]]
- [[偏好学习]]
- [[人机交互导航]]
- [[自反式控制]]

## 🔗 相关链接

- [[2024_VLFM_Vision-Language_Frontier_Maps]] - VLFM 是纯语义导航基准，E2Map 在其基础上加了偏好层
- [[2024_SG-Nav_Scene_Graph_Navigation]] - SG-Nav 的 scene graph 与 E2Map 的 experience map 有概念联系

## 📌 待探索问题

- emotion map 的"情感"如何量化？用户的隐式偏好如何高效获取而不需要大量交互？
- 在偏好冲突（如"最快"vs"最安全"）时，E2Map 的优先级仲裁机制是什么？

---
**维护**: 花火 · 2026-04-12
