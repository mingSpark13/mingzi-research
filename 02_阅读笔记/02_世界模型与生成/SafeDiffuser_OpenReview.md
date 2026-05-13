---
title: 'SafeDiffuser: Control Barrier Functions for Safe Diffusion Planning'
authors: Multiple (from OpenReview)
arxiv: ''
date: ~2025
institution: 估计为安全控制/扩散模型方向
conf: OpenReview
keywords: Safe Diffusion Planning, Control Barrier Functions, Diffusion MPC, Safe
  Trajectory Generation
tags:
- D01
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/SafeDiffuser_OpenReview.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["物理一致性", "任务与运动规划", "MPC"]
- 物理一致性
- 任务与运动规划
---


## 🎯 题目

SafeDiffuser: Control Barrier Functions for Safe Diffusion Planning

## 📝 三句摘要

1. **问题背景**：diffusion model在轨迹/动作规划中无法保证安全性，需要在生成过程中引入安全约束机制。
2. **核心方法**：将control barrier functions (CBF) 直接集成进diffusion模型的采样过程，用CBF对每步采样方向做安全校正，保证生成的轨迹序列满足安全约束。
3. **关键结果**：在安全关键场景（机器人避障、无人机禁飞区）生成任务上，SafeDiffuser在保证安全性的同时保持了较高的轨迹质量。

## 💎 价值评估

- **🔬 研究价值**：将控制理论中的CBF与diffusion规划结合，是"采样时硬约束引导"的典型工程实现，与PCFM、SafeFlow同属第三层注入方法。
- **🚀 实践价值**：为需要安全保证的机器人轨迹生成提供了可证明安全的diffusion框架。
- **📈 扩展潜力**：CBF可扩展到多智能体避碰，diffusion可扩展到高维状态空间。

## 🎯 可落地实验点

**实验设计**：将SafeDiffuser的CBF引导用于多无人机协同编队安全轨迹生成
- 对比基线：标准diffusion planning、CBF-only控制
- 度量指标：碰撞率（安全）、编队一致性（任务）
- 预期结果：SafeDiffuser应在碰撞率上接近0

## 🔗 知识图谱

- [[世界模型]] - Safe diffusion planning是world model落地的重要支撑
- [[物理一致性]] - CBF引导提供安全性约束满足
- [[任务与运动规划]] - Control barrier function是安全护栏的核心技术

## 🔗 相关链接

- [[2025-04-23_SafeFlow]] - SafeFlow同样集成CBF，与SafeDiffuser同源
- [[2025-06-17_PCFM]] - PCFM是更通用的硬约束flow matching版本
- [[2026-03-25_MPCwithDiffWorldModel]] - MPC+可微世界模型与SafeDiffuser可结合

## 📌 待探索问题

- SafeDiffuser的CBF条件（class-K函数存在性）在复杂多约束场景下是否总是满足？
- SafeDiffuser与action-conditioned world model的结合方式是什么？

---
**维护**: 花火 · 2026-04-12
