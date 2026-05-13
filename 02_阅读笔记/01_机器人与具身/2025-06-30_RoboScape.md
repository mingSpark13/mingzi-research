---
title: "RoboScape: Physics-Informed Embodied World Model"
authors: Multiple (from arXiv 2506.23135)
arxiv: 2506.23135
date: 2025-06-30
institution: 估计为机器人具身方向
conf: arXiv
keywords: Physics-Informed, Embodied World Model, Contact Dynamics, Tactile
domain: 具身智能
pdf_path: ../../01_论文库/世界模型/2506_RoboScape.pdf
reading_date: 2026-03-26
reading_status: 已读
tags: ["D02", "物理一致性", "世界模型"]
summary: "传统视频重建型世界模型只学视觉统计相关性，缺乏对物理规律（接触力、摩擦、重力）的显式建模，导致长时rollout物理违规。"
related_concepts: ["物理一致性"]
---

## 🎯 题目

RoboScape: Physics-Informed Embodied World Model

## 📝 三句摘要

1. **问题背景**：传统视频重建型世界模型只学视觉统计相关性，缺乏对物理规律（接触力、摩擦、重力）的显式建模，导致长时rollout物理违规。
2. **核心方法**：RoboScape在world model内部加入物理辅助监督任务（动力学残差损失、接触一致性损失、几何/深度/速度/加速度一致性损失），同时引入触觉(visuo-tactile)信号作为物理grounding。
3. **关键结果**：在长时action-conditioned视频预测任务上，physics-informed world model显著优于纯重建型模型，物理违规率大幅降低。

## 💎 价值评估

- **🔬 研究价值**：是第一层（训练时软先验注入）的典型代表，证明了physics-informed loss确实能提升物理一致性，但作者也承认这只是"更倾向守法"而非"保证守法"。
- **🚀 实践价值**：可与机器人操控策略学习结合，提升Sim2Real迁移效果。
- **📈 扩展潜力**：可升级为第二层（结构约束注入），将物理辅助监督换成可微仿真器层。

## 🎯 可落地实验点

**实验设计**：将RoboScape的physics-informed监督思路用于无人机气流world model
- 对比基线：纯视频预测world model、无物理监督的latent dynamics model
- 度量指标：气流预测误差、物理违规率、Sim2Real成功率
- 预期结果：physics-informed版本应在气流预测上更符合物理规律

## 🔗 知识图谱

- [[世界模型]] - Physics-informed embodied world model是本文核心
- [[物理一致性]] - 软先验注入方式，只能"提升"不能"保证"物理一致性
- [[具身智能]] - 具身场景的action-conditioned视频预测

## 🔗 相关链接

- [[2026-01-28_ConstrainedGeneration]] - 本文属于第一层注入，ConstrainedGeneration区分了软/硬约束的不同保证能力
- [[2025-06-17_PCFM]] - PCFM是更强的硬约束注入，可与本文方法对比

## 📌 待探索问题

- Physics-informed loss的权重如何自动调整，避免物理损失与重建损失相互干扰？
- RoboScape的物理辅助任务是否需要针对不同机器人形态（无人机vs机械臂）重新设计？

---
**维护**: 花火 · 2026-04-12
