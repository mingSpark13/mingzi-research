---
title: "CausalNav: A Long-term Embodied Navigation System for Autonomous Mobile Robots in Dynamic Outdoor Scenarios"
authors: Multiple (RAL'26)
arxiv: 2601.01872
date: 2026-01
institution: various
conf: RAL 2026
keywords: CausalNav, Embodied Navigation, Semantic Scene Graph, Embodied Graph, RAG, Long-Horizon Planning, Dynamic Outdoor
tags: ["D02"]
domain: 机器人与具身
pdf_path: ../../01_论文库/具身智能/2601_CausalNav.pdf
reading_date: 待补充
reading_status: 已读
summary: CausalNav 将语义场景图、RAG 与长程规划结合，解决动态户外场景中的长期 embodied navigation 问题。
related_concepts: ["任务与运动规划", "语义导航"]
---

## 🎯 题目

CausalNav: A Long-term Embodied Navigation System for Autonomous Mobile Robots in Dynamic Outdoor Scenarios

## 📝 三句摘要

1. **问题背景**：户外大尺度语言引导导航面临语义推理、动态条件和长程稳定性的三重挑战。
2. **核心方法**：CausalNav 构建多层级语义场景图（Embodied Graph），用 LLM 整合粗粒度地图和细粒度物体实体；通过 RAG 支持开放词汇查询语义导航和长程规划；实时感知与离线地图融合，支持动态目标处理。
3. **关键结果**：在仿真和真实户外环境中验证了优越的鲁棒性和效率。

## 💎 价值评估

- **🔬 研究价值**：CausalNav 是具身图（Embodied Graph）在导航中的首次应用，将场景图+RAG 引入动态户外导航。
- **🚀 实践价值**：为无人机/移动机器人的户外语义导航提供了新范式。
- **📈 扩展潜力**：Embodied Graph 可与主人的 PMI 框架结合——场景图作为世界感知层的结构化表征，RAG 作为长程规划的检索基础。

## 🔗 知识图谱

- [[具身智能]] - 具身导航是具身智能的重要分支
- [[任务与运动规划]] - 长程规划是核心能力

## 📌 待探索问题

- Embodied Graph 的构建成本如何？是否支持在线增量更新？
- 与主人的 PMI 框架中"意图层"如何结合？

---
**维护**: 花火 · 2026-04-12


## 🎯 可落地实验点

**实验设计**：待补充
- 对比基线：待补充
- 度量指标：待补充
- 预期结果：待补充


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
