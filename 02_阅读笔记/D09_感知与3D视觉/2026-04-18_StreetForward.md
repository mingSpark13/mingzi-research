---
type: "paper"
title: "StreetForward: Pose-Free Feed-Forward Framework for Dynamic Street Reconstruction"
authors: "M. Zhao, L. Wang, et al."
arxiv: 2603.19552
date: 2026-03-24
institution: "Tsinghua University / 清华大学"
direction: "感知与3D视觉"
pdf_path: "../../01_论文库/3D视觉/2603.19552_StreetForward.pdf"
tags: ["感知与3D视觉", "3D高斯溅射", "3D重建"]
summary: "StreetForward 直接用前馈网络做无位姿动态街景重建，绕开逐帧位姿优化，适合高吞吐在线 3D 场景建模。"
reading_date: 2026-04-18
reading_status: "已读"
related_concepts: ["感知与3D视觉", "3D高斯溅射", "3D重建"]
---

# 📖 花火格式笔记

## 🎯 题目

StreetForward: Pose-Free Feed-Forward Framework for Dynamic Street Reconstruction

## 📝 三句摘要

1. **问题背景**：传统动态街道 3D 重建依赖精确的姿态传感器或跟踪器，在无精确姿态的众包数据上难以部署；前馈方法虽有潜力但对动态场景保真度不足。
2. **核心方法**：StreetForward 是一个无姿态、无跟踪器的前馈动态街道重建框架，基于 VGGT 的交替注意力机制，提出 temporal mask attention 模块捕获动态运动信息；静态内容和动态实例统一用 3DGS 表示。
3. **关键结果**：在 Waymo Open Dataset 上验证，零样本泛化到 CARLA 等其他数据集，展示了优秀的泛化能力；无需姿态估计即可实现高保真动态街道重建。

## 💎 价值评估

- **🔬 研究价值**：无姿态依赖的前馈方案降低了动态街道 3D 重建的门槛，为大规模无标注街道数据利用提供了新思路。
- **🚀 实践价值**：对 UE 数据采集中多相机/无精确姿态的场景有直接参考价值；temporal mask attention 可用于动态物体重建。
- **📈 扩展潜力**：可扩展到无人机街道/园区场景的实时 3D 重建；与程序化场景生成结合可实现数据增强。

## 🎯 可落地实验点

在 UE 城市场景采集流程中引入 StreetForward 的 temporal mask attention 机制，验证对动态物体（如车辆、行人）重建质量的提升。
- 对比基线：纯静态 3DGS 重建 / 有姿态的动态重建
- 度量指标：动态物体渲染质量（LPIPS）、场景一致性
- 预期结果：temporal mask attention 提升动态物体保真度，同时降低姿态依赖

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[感知与3D视觉]] - 动态街道重建属于 3D 视觉方向
- [[3D高斯溅射]] - 核心场景表示方法，统一建模静态和动态内容
- [[3D重建]] - VGGT 驱动的 3D 重建是该工作的核心任务

## 🔗 相关链接

- [[2026-04-18_InfiniteVGGT]] - VGGT 系列工作，本文 StreetForward 基于 VGGT 的注意力机制
- [[2026-04-18_VGGT4D]] - 4D VGGT 方向相关工作

## 📌 待探索问题

- temporal mask attention 在无人机视角（非街道平视）上的泛化能力如何？
- 能否实现端到端"采集→实时重建→导航规划"一体化？

---
**维护**: 花火 · 2026-04-18
