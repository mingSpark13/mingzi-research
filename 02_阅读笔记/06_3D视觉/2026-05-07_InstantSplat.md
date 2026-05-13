---
title: "InstantSplat: Sparse-view Gaussian Splatting in Seconds"
authors: Zhiwen Fan, Wenyan Cong, Kairun Wen, Kevin Wang, Jian Zhang, Xinghao Ding, Danfei Xu, Boris Ivanovic, Marco Pavone, Georgios Pavlakos, Zhangyang Wang, Yue Wang
arxiv: 2403.20309
date: 2024-03-28
institution: UT Austin · NVIDIA Research · Xiamen University · Georgia Tech · Stanford · USC
conf: arXiv preprint
keywords: ["sparse-view 3DGS", "SfM-free", "Gaussian Bundle Adjustment", "self-supervised", "fast reconstruction"]
tags: ["3D高斯溅射", "3D重建", "深度估计", "SLAM"]
domain: 3D视觉
pdf_path: "../../01_论文库/3D视觉/2403.20309_InstantSplat.pdf"
reading_date: 2026-05-07
reading_status: 已读
related_concepts: ["3D高斯溅射", "3D重建", "深度估计", "SLAM"]
---

# 📖 花火格式笔记

## 🎯 题目

InstantSplat: Sparse-view Gaussian Splatting in Seconds

## 📝 三句摘要

1. **问题背景**：3D Gaussian Splatting（3D-GS）的传统流程依赖 COLMAP 提供相机位姿，在少视角（2-3张图）或无初始位姿场景下 SfM 极易失败，导致重建无法进行。
2. **核心方法**：提出 Gaussian Bundle Adjustment（GauBA），借助 MASt3R 预训练深度先验进行端到端联合优化相机位姿与 3D Gaussians，实现 SfM-free 少视角重建；整个优化仅需少量步数（秒级）。
3. **关键结果**：在 Tanks and Temples 等数据集上比 COLMAP+3DGS 加速 20 倍以上，SSIM 从 0.375 提升至 0.762；同时兼容 3D-GS、2D-GS、Mip-Splatting 等多种表示。

## 💎 价值评估

- **🔬 研究价值**：首次实现纯端到端 SfM-free 的少视角 3DGS，将传统 pipeline 的多模块串联简化为单阶段联合优化，为后续"输入一张图即重建"提供了技术路径参考。
- **🚀 实践价值**：秒级重建速度 + 仅需 2-3 张图使该方法特别适合 UAV 空中采集后实时建图、机器人即时场景感知等资源受限的在线部署场景。
- **📈 扩展潜力**：可探索将 MASt3R 替换为更轻量的单目深度估计器以进一步提速；也可拓展到动态场景 4D-GS；或在 Sim2Real 框架中作为快速场景建模模块。

## 🎯 可落地实验点

**实验设计**：UAV 空中建图场景下的少视角 3DGS 在线建图实验
- **对比基线**：COLMAP+3DGS（传统流程）、pixelSplat（稀疏视图前馈 3DGS）
- **度量指标**：重建完整性（Completion）、重建精度（Accuracy）、端到端延迟（秒）、Novel-view PSNR/SSIM
- **预期结果**：InstantSplat 在 2-3 视角下以 <5 秒延迟达到与 COLMAP+3DGS 相当的重建精度，显著优于 pixelSplat 的视图合成质量

## 🔗 知识图谱

- [[3D高斯溅射]] - 本文核心 3D 场景表示方法
- [[3D重建]] - 本文解决的重建任务
- [[深度估计]] - 依赖 MASt3R 提供的像素对齐深度先验
- [[SLAM]] - 相机位姿估计作为联合优化的一部分（GauBA 承担 BA 功能）

## 🔗 相关链接

- [[2024-03_MVSplat]] - 同期 ECCV 2024 Oral，同样做稀疏多视角前馈 3DGS，是直接对比基线
- [[2024-06_MASt3R]] - 为 InstantSplat 提供深度与匹配先验，是技术依赖的核心工作

## 📌 待探索问题

- MASt3R 深度先验若替换为更轻量的单目深度网络（如 Marigold），是否仍能保持少视角下的收敛稳定性？
- InstantSplat 在 UAV 大尺度城市场景下的内存占用与长时间优化稳定性如何？秒级重建是否只是"粗略初始化"而需要后续 refinement？

---
**维护**: 花火 · 2026-05-07
