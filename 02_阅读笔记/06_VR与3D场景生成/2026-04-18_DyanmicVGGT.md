---
title: "DynamicVGGT: Feed-Forward 4D Dynamic Scene Reconstruction for Autonomous Driving"
authors: "待补充"
arxiv: 2603.08254
date: 2026-03-12
institution: 待补充
conf: arXiv
domain: 感知与3D视觉
tags:
  - 3D高斯溅射
  - 深度估计
pdf_path: "../../01_论文库/3D视觉/2603.08254_DyanmicVGGT.pdf"
reading_date: 2026-04-18
reading_status: 已读
---

## 🎯 题目

DynamicVGGT: Feed-Forward 4D Dynamic Scene Reconstruction for Autonomous Driving

## 📝 三句摘要

1. **问题背景**：现有前馈 3D 重建方法（如 VGGT）只能处理静态场景，无法应对自动驾驶中常见的行人、车辆等动态物体，导致时间不一致和时间域外推困难。
2. **核心方法**：提出 DynamicVGGT，将 VGGT 扩展到 4D 动态场景重建；在共享参考坐标系中联合预测当前和未来时间点的点图；设计 Motion-aware Temporal Attention (MTA) 模块建模运动连续性；提出动态 3DGS Head，通过学习运动令牌预测高斯速度，在场景流监督下显式建模点运动。
3. **关键结果**：在自动驾驶数据集上显著优于现有方法，实现复杂行驶场景下鲁棒的前馈 4D 动态场景重建。

## 💎 价值评估

- **研究价值**：将前馈 3D 重建从静态推广到动态时空建模，是 VGGT 家族的重要扩展方向，对 4D 时空感知有基础贡献。
- **实践价值**：前馈推理适合批量数据生成，可直接用于自动驾驶数据集的后处理 4D 标注；对龙虾/UE 数据采集的动态场景重建有直接参考价值。
- **扩展潜力**：动态 3DGS + 运动速度建模可为机器人动态物体跟踪和意图预测提供感知基础。

## 🎯 可落地实验点

在 UniSplat 或 VGGT 基础上，引入 MTA 模块 + 动态 Gaussian velocity prediction，在实车/无人机采集数据中验证动态场景 4D 重建效果，对比静态重建基线的时序一致性提升。

## 🔗 知识图谱

- [[concepts/3D高斯溅射]] - 核心场景表示，动态 3DGS Head 基于此扩展
- [[concepts/深度估计]] - VGGT 系列方法的核心感知输出

## 🔗 相关链接

- [[2026-04-18_UniSplat]] - 前馈式 3DGS 重建，DynamicVGGT 在其基础上增加了动态场景处理
- [[2026-04-18_VGGT4D]] - 4D VGGT 方向相关

## 📌 待探索问题

- MTA 模块的运动连续性建模能否泛化到非道路场景（室内机器人、无人机）？
- 动态 Gaussian velocity prediction 在高速运动物体（>30km/h）下的估计精度如何？

---
**维护**: 花火 · 2026-04-18
