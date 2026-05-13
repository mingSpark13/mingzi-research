---
title: "Dual Pose-Graph Semantic Localization for Vision-Based Autonomous Drone Racing"
authors: Multiple (from arXiv 2604.15168)
arxiv: 2604.15168
date: 2026-04-19
institution: UAV Localization / Drone Racing
conf: arXiv
keywords: [UAV, Localization, SLAM, Drone Racing, Visual-Inertial]
domain: 无人机感知定位
pdf_path: ../../01_论文库/2604.15168.pdf
reading_date: 2026-04-19
reading_status: 已读
tags: ["D04", "无人机定位", "SLAM", "视觉惯性里程计", "竞速无人机"]
summary: "无人机竞速需要在极端条件下（高速飞行、激进机动）实现鲁棒实时定位，单目视觉SLAM面临运动模糊和特征不稳定问题。"
related_concepts: ["无人机定位", "SLAM", "视觉惯性里程计", "竞速无人机"]
---

## 🎯 题目

Dual Pose-Graph Semantic Localization for Vision-Based Autonomous Drone Racing

## 📝 三句摘要

1. **问题背景**：无人机竞速需要在极端条件下（高速飞行、激进机动）实现鲁棒实时定位，单目视觉SLAM面临运动模糊和特征不稳定问题。
2. **核心方法**：提出双pose-graph架构，将里程计与语义检测融合；临时图累积多个门观测并在关键帧之间优化它们，再将优化结果提升到持久主图中，防止图增长影响实时性能。
3. **关键结果**：在TII-RATM数据集上相比独立VIO降低56%~74%的ATE，在A2RL竞赛中实现实时机载定位，每圈减少高达4.2m的漂移。

## 💎 价值评估

- **🔬 研究价值**：首次将语义SLAM与双图架构应用于无人机竞速场景，为高速无人机定位提供了新的方法论。
- **🚀 实践价值**：传感器无关设计，实际竞赛验证（A2RL），实时性好。
- **📈 扩展潜力**：双图架构可推广到其他需要长期运行的视觉定位系统。

## 🎯 可落地实验点

**实验设计**：将双pose-graph语义定位应用于自主无人机精准降落
- 对比基线：标准VIO、纯语义SLAM
- 度量指标：定位精度ATE、实时性（CPU占用）、长距离漂移
- 预期结果：双图架构应在长距离任务上显著减少漂移

## 🔗 知识图谱

- [[无人机定位]] - 竞速定位是本文的核心应用
- [[SLAM]] - 双pose-graph是SLAM的架构创新
- [[视觉惯性里程计]] - 单目VIO是基础传感器

## 🔗 相关链接

- [[2025-12-22_IndoorUAV]] - IndoorUAV的定位方法与本文可对比
