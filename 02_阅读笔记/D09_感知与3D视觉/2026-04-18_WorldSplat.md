---
title: "WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving"
authors: "Xiaofeng Du, Zeqi Xiao, et al."
date: 2025-09-30
institution: "Tsinghua University & Huawei"
conf: "arXiv 2509.23402"
keywords: ["4D Scene Generation", "Gaussian Splatting", "Autonomous Driving", "World Model"]
tags:
  - 世界模型
  - 3D高斯溅射
  - 视频生成
domain: "世界模型"
pdf_path: "../../01_论文库/世界模型/2509.23402_WorldSplat.pdf"
reading_date: 2026-04-18
reading_status: "已读"
related_concepts: ["世界模型", "视频生成", "3D高斯溅射"]
summary: "WorldSplat 用 Gaussian-centric 前馈 4D 场景生成统一重建与生成，提升自动驾驶多视角时空一致性与远轨迹质量。"
---

# 📖 WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving

## 🎯 题目

WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving

## 📝 三句摘要

1. **问题背景**：传统4D场景生成方法在自动驾驶中场景重建与生成割裂，无法高效合成时空一致的多视角视频。
2. **核心方法**：提出Gaussian-centric前馈框架，用高斯中心化建模替代像素级建模，实现时空一致的多轨道视频生成。
3. **关键结果**：在新轨迹视角下显著改善背景和车辆模型的质量退化，提升4D场景重建的鲁棒性。

## 💎 价值评估

- **🔬 研究价值**：首个Gaussian-centric 4D前馈框架，弥合场景重建与生成之间的鸿沟
- **🚀 实践价值**：直接支撑D01世界模型研究，可为UE5城市场景生成管线提供新方向
- **📈 扩展潜力**：可扩展到无人机视角4D场景、空中数据采集的实时场景生成

## 🎯 可落地实验点

**实验设计**：将WorldSplat的Gaussian-centric生成能力集成到UE5城市场景批量采集流程
- 对比基线：传统像素级4DGS重建
- 度量指标：FID、CS-FID（场景保真度）、视图一致性（LPIPS）
- 预期结果：Gaussian-centric在长距离轨迹下视图一致性显著优于像素级方法

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[concepts/世界模型]] - 本文核心目标，构建4D驾驶场景的世界模型
- [[concepts/视频生成]] - 多视角时空一致性视频生成
- [[concepts/3D高斯溅射]] - Gaussian-centric场景表示基础

## 🔗 相关链接

> 链接本文核心引用的相关论文。

- [[2024-01_HUGSIM]] - HUGSIM：3DGS仿真平台，同属场景生成族
- [[2026-04-18_TeraSim-World]] - TeraSim-World：4D世界模型对比基线
- [[2026-04-18_VolSplat]] - VolSplat：本文技术基础，前馈3DGS新范式

## 📌 待探索问题

- WorldSplat在复杂城市场景（多移动物体、动态光照）下的生成质量如何保证？
- 能否将其扩展到无人机垂直起降、大角度俯仰等非标准驾驶视角？

---
**维护**: 花火 · 2026-04-18
