---
title: "ReconDrive: Feed-Forward 4D Gaussian Splatting for Scalable Autonomous Driving Scene Reconstruction"
authors: "Haibao Yu, Kuntao Xiao, Jiahang Wang, Ruiyang Hao, Yuxin Huang, Guoran Hu, Haifang Qin, Bowen Jing, Yuntian Bo, Ping Luo"
arxiv: "2603.07552"
date: "2026-03-11"
institution: "Tuojing Intelligence, The University of Hong Kong, King's College London, The University of Sydney, MBZ University of AI"
conf: "arXiv"
tags:
  - "3D高斯溅射"
  - "3D重建"
  - "视频生成"
  - "物理一致性"
domain: "3D视觉"
pdf_path: "../../01_论文库/世界模型/2603.07552v1_ReconDrive.pdf"
reading_date: "2026-04-18"
reading_status: "已读"
---

# 📖 花火格式笔记

## 🎯 题目

ReconDrive: Feed-Forward 4D Gaussian Splatting for Scalable Autonomous Driving Scene Reconstruction

## 📝 三句摘要

1. **问题背景**：现有 4DGS 方法依赖逐场景优化，计算开销巨大，无法扩展到大规模城市场景；前馈方法虽快但视觉质量下降。
2. **核心方法**：提出 ReconDrive，扩展 VGGT 3D 基础模型用于前馈 4DGS 生成。设计 Hybrid Gaussian Prediction Heads（解耦空间坐标与外观属性回归）和 Static-Dynamic 4D Composition 策略（速度建模捕获动态运动）。
3. **关键结果**：在 nuScenes 上显著优于前馈基线，8/9 指标超越逐场景优化方法，同时速度提升数个数量级。

## 💎 价值评估

- **🔬 研究价值**：首个将 3D 基础模型（VGGT）扩展到前馈 4DGS 的工作，解决逐场景优化不可扩展的核心痛点。
- **🚀 实践价值**：对 UE 数据采集主线的直接参考——前馈 4DGS 可作为程序化场景生成的质量验证器，或为仿真器提供真实感 4D prior。
- **📈 扩展潜力**：Seg-wise temporal fusion 可用于长距离无人机轨迹的新视角合成；Static-Dynamic Composition 可迁移到无人机场景的动态物体建模。

## 🎯 可落地实验点

**实验设计**：借鉴 ReconDrive 的 Hybrid Gaussian Prediction Head 思想，在 UE 场景采集流程中加入前馈深度/新视角质量评估模块，验证程序化生成场景的视觉质量。
- 对比基线：纯 UE 渲染 vs ReconDrive 风格前馈质量增强
- 度量指标：新视角 PSNR/SSIM、几何精度（若 UE 场景有 GT）
- 预期结果：前馈质量评估模块可快速发现程序化场景的视觉缺陷

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[concepts/3D高斯溅射]] - 核心表示方法，4DGS 扩展到时间维度
- [[concepts/3D重建]] - 动态城市场景的时空重建任务
- [[concepts/视频生成]] - 新视角合成能力，多视角一致性
- [[concepts/物理一致性]] - Static-Dynamic Composition 显式建模物体运动

## 🔗 相关链接

> 链接本文核心引用的相关论文。

- [[2025_VGGT]] - VGGT: 3D 基础模型，本文 backbone，直接扩展到 4D
- [[2024_Street_Gaussians]] - Street Gaussian: 逐场景优化 4DGS 基线，本文对比对象
- [[2024_SAM2]] - SAM2: 用于动态物体 mask 提取的 foundation model

## 📌 待探索问题

- Hybrid Gaussian Prediction Heads 的 appearance attribute regression 在无人机非结构化场景中是否同样有效？
- Static-Dynamic Composition 的速度建模能否扩展到非刚体（如柔性物体）？
- 前馈 4DGS 与程序化 UE 场景生成的结合方式：是用作质量验证还是生成 prior？

---
**维护**: 花火 · 2026-04-18
