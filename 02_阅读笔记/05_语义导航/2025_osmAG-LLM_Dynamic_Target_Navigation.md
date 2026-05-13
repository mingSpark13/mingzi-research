---
title: "osmAG-LLM: Object-Goal Navigation with Dynamic and Unmapped Target Query"
authors: ""
arxiv: "2507.12753"
date: 2025/2026
institution: ""
conf: arXiv
keywords: dynamic target, unmapped target, open-vocabulary, object-goal navigation, instance-level
tags: ["D06"]
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["语义导航", "6D位姿估计", "抓取检测", "持续学习"]
---

## 🎯 题目

osmAG-LLM: 动态目标与未建图目标查询的开放词汇目标导航

## 📝 三句摘要

1. **问题背景**：真实场景中目标可能被移动、可能根本不在已有地图里，现有方法依赖静态地图或已知目标位置，泛化能力受限。
2. **核心方法**：提出针对动态/未建图目标查询的语义导航方法，静态目标时路径更短、检索成功率更高；在动态目标查询上明显优于 prior methods。
3. **关键结果**：在动态/未建图目标场景下成功率显著提升，路径效率优于依赖预建图的方法。

## 💎 价值评估

- **🔬 研究价值**：首次明确针对"动态/未建图目标"这一真实场景优化，填补了开放词汇导航的空白。
- **🚀 实践价值**：非常适合"垃圾桶被人挪了""蓝色车换位置了"这类真实搜索任务，是实用性最强的语义导航扩展方向之一。
- **📈 扩展潜力**：动态目标追踪 + 重定位机制可与 SLAM 系统结合，实现"边建图边搜索动态目标"。

## 🎯 可落地实验点

**实验设计**：在目标位置动态变化的场景（目标每30秒随机移动）测试 osmAG-LLM vs VLFM
- 对比基线：VLFM、静态地图方法
- 度量指标：目标重发现成功率、平均搜索时间、路径效率
- 预期结果：osmAG-LLM 在动态场景下 SR 提升 >25%，平均搜索时间减少 >30%

## 🔗 知识图谱
- [[6D位姿估计]]
- [[抓取检测]]
- [[重定位]]
- [[持续学习]]
- [[语义导航]]

## 🔗 相关链接

- [[2024_VLFM_Vision-Language_Frontier_Maps]] - VLFM 是核心对比基线，osmAG-LLM 专注于动态场景扩展
- [[2025_ApexNav_Adaptive_Semantic-Geometric_Exploration]] - ApexNav 的自适应切换思想与 osmAG-LLM 的动态适应有协同潜力

## 📌 待探索问题

- 动态目标多次移动后，osmAG-LLM 是否会出现"目标遗忘"问题？如何保证实例级持续追踪？
- 在多目标动态场景（如多个物体同时移动）下，osmAG-LLM 的多目标协调策略是什么？

---
**维护**: 花火 · 2026-04-12
