---
title: "ParkGaussian: Surround-view 3D Gaussian Splatting for Autonomous Parking"
authors: "Wei, Ye, Gu, Zhu, Guo, Shen, Zhao, Sun, Wang, Chen, Lu, Ye"
arxiv: "2601.01386"
date: "2026-01-04"
institution: ""
conf: "arXiv"
summary: "ParkGaussian 将 surround-view 3DGS 用于自动泊车场景重建，并用 slot-aware 感知目标把重建质量与下游泊车任务对齐。"
tags:
  - "3D高斯溅射"
  - "感知与3D视觉"
  - "3D重建"
domain: "感知与3D视觉"
pdf_path: "../../01_论文库/3D视觉/2601.01386_ParkGaussian.pdf"
reading_date: "2026-04-18"
reading_status: "已读"
---

# 📖 花火格式笔记

## 🎯 题目

ParkGaussian: Surround-view 3D Gaussian Splatting for Autonomous Parking

## 📝 三句摘要

1. **问题背景**：自动泊车（ADS）在拥挤停车场和 GPS 拒止环境下面临独特挑战，现有 3D 重建方法难以满足泊车场景对高精度场景感知的需求。
2. **核心方法**：提出 ParkGaussian，首个将 3DGS 应用于自动泊车 surround-view 场景重建的框架，配套专用 benchmark ParkRecon3D（含四路鱼眼相机+标定外参+稠密泊车位标注）。
3. **关键结果**：在 ParkRecon3D 上实现 SOTA 重建质量，slot-aware reconstruction 使下游泊车位感知一致性优于基线，展示了"重建→感知"联合优化的工程价值。

## 💎 价值评估

- **🔬 研究价值**：首个泊车场景 3DGS benchmark，提出感知任务驱动的 3DGS 优化范式，替代传统纯视觉质量优化。
- **🚀 实践价值**：对 UE 数据采集主线的"程序化场景生成"有直接参考价值——合成数据的评价指标应与下游感知指标对齐，而非视觉逼真度。
- **📈 扩展潜力**：slot-aware 策略可迁移到无人机场景重建，以航迹规划/避障等下游任务指标作为重建质量锚点。

## 🎯 可落地实验点

**实验设计**：在 UE 程序化生成城市场景时，参考 ParkGaussian"感知驱动重建"的评价方式，以检测/分割等下游感知任务指标而非渲染质量作为场景合成质量标准。
- 对比基线：视觉质量（LPIPS/SSIM）与感知质量（mAP/mIoU）两种优化目标的差异
- 度量指标：下游感知任务精度 vs 渲染质量指标
- 预期结果：感知驱动的合成数据训练出的模型在真实场景泛化更优

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[concepts/3D高斯溅射]] - 核心技术，应用于泊车场景 3D 重建
- [[concepts/3D重建]] - 面向自动驾驶的稠密场景重建
- [[concepts/感知与3D视觉]] - 泊车位感知一致性作为优化目标
- [[concepts/数据合成]] - 仿真数据合成与场景重建用于训练

## 🔗 相关链接

> 链接本文核心引用的相关论文。

- [[2024-03-27_UniSplat]] - UniSplat：通用 3DGS 框架，本文方法基础
- [[2026-04-18_Street_Gaussians]] - Street Gaussians：驾驶场景 3DGS 相关工作

## 📌 待探索问题

- slot-aware reconstruction 的优化目标是泊车位感知，如何扩展到更通用的"任务感知重建"框架？
- ParkGaussian 使用鱼眼相机，针孔相机方案是否能在不显著降低重建质量的前提下简化标定流程？

---
**维护**: 花火 · 2026-04-18
