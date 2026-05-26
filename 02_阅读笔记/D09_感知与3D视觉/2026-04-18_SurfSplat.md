---
title: "SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors"
authors: "Bing He, Jingnan Gao, Yunuo Chen, Ning Cao, Gang Chen, Zhengxue Cheng, Li Song, Wenjun Zhang"
arxiv: "2602.02000"
date: 2026-02-02
institution: "Shanghai Jiao Tong University"
conf: "arXiv"
keywords: ["2D Gaussian Splatting", "surface reconstruction", "sparse view", "3D reconstruction", "feedforward"]
tags:
  - 感知与3D视觉
  - 3D高斯溅射
  - 3D重建
domain: 感知与3D视觉
pdf_path: "../../01_论文库/感知与3D视觉/2602.02000_SurfSplat.pdf"
reading_date: 2026-04-18
reading_status: 已读
related_concepts:
  - 感知与3D视觉
  - 3D高斯溅射
  - 3D重建
---

# 📖 SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors

## 🎯 题目

SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors

## 📝 三句摘要

1. **问题背景**：从稀疏视角前馈式重建3D场景时，现有3DGS方法易产生离散的、不连续的点云，在近景视角下暴露严重伪影。
2. **核心方法**：SurfSplat基于2DGS基元（比3DGS各向异性更强、几何精度更高），引入表面连续性先验（Surface Continuity Prior）和强制alpha混合策略，重建连贯几何与忠实纹理，并提出HRRC高分辨率渲染一致性指标。
3. **关键结果**：在RealEstate10K、DL3DV、ScanNet上全面超越先前方法，标准指标和HRRC均达到最优。

## 💎 价值评估

- **🔬 研究价值**：前馈式2DGS重建的核心改进，为稀疏视角几何恢复提供新范式，与3DGS研究紧密相关。
- **🚀 实践价值**：近景视图质量提升对机器人操作场景的精细几何感知有直接价值，可用于仿真实物场景的快速三维重建。
- **📈 扩展潜力**：表面连续性先验可与视频生成/世界模型结合，用于提升生成式3D场景的几何一致性。

## 🎯 可落地实验点

**实验设计**：在UE仿真环境中引入SurfSplat的几何约束，提升程序化城市场景生成的表面连续性。
- 对比基线：标准3DGS前馈重建
- 度量指标：HRRC指标、Chamfer Distance、PSNR
- 预期结果：建筑物/地面等大面积表面几何质量显著提升

## 🔗 知识图谱

> 字典v1.1二级规范名

- [[感知与3D视觉]] - 本文所属领域
- [[3D高斯溅射]] - 核心表示方法（2DGS/3DGS对比）
- [[3D重建]] - 本文任务类型：稀疏视角3D重建
- [[深度估计]] - 几何恢复的隐含技术基础

## 🔗 相关链接

- [[2024-10_Scaffold-GS]] - Scaffold-GS: 本文对比的3DGS前馈基线之一
- [[2024-06_Instant-3DGS]] - Instant-3DGS: 稀疏视角3DGS前馈基线

## 📌 待探索问题

- 表面连续性先验能否与NeRF结合以进一步提升纹理质量？
- 在动态场景（机器人操作）中，SurfSplat的时序一致性如何保证？

---
**维护**: 花火 · 2026-04-18
