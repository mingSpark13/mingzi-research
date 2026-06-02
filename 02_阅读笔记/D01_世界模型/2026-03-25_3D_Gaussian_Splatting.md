---
title: "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
arxiv: 2308.04079
date: 2023-08-08
institution: Inria
conf: SIGGRAPH 2023
keywords: 3DGS, Gaussian Splatting, Real-Time Rendering, View Synthesis
tags: ["D01", "3D高斯溅射"]
summary: "3DGS 用显式高斯原语实现高质量近实时辐射场渲染，证明高效几何表示是交互式世界建模的重要基础。"
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2023_3D_Gaussian_Splatting.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["3D高斯溅射"]
---

## 🎯 题目
3D Gaussian Splatting for Real-Time Radiance Field Rendering

## 📝 三句摘要
1. 3DGS 用显式高斯原语代替隐式神经场，实现高质量且接近实时的场景渲染。
2. 它通过可微 splatting、密度控制与优化机制，在质量和速度上都优于传统 NeRF 路线。
3. 对 InSpatio-World 这类系统而言，3DGS 代表“几何表示必须足够高效才能支持交互”的关键转折点。

## 💎 价值评估
- **🔬 研究价值**：证明了显式表示在新视角合成中可以同时兼顾质量与实时性。
- **🚀 实践价值**：大幅降低交互式三维场景渲染门槛，利于机器人/自动驾驶/数字孪生。
- **📈 扩展潜力**：语义占用、动态 4D 表示和世界模型都在吸收 3DGS 思路。

## 🎯 可落地实验点
**实验设计**：在主人关注的 3DGS 场景中，对比静态重建、动态占用预测和世界模型中的几何锚定作用。

## 🔗 知识图谱
- [[3D高斯溅射]] - 本文的核心方法与名称来源
- [[3D重建]] - 属于高效三维场景表示与重建路线
- [[实时推理]] - 实时渲染能力是其最大突破之一

## 🔗 相关链接
- [[2026-03-25_NeRF]] - 3DGS 对 NeRF 的实时性问题给出更优解
- [[2026-03-17_VG3S]] - 将 3DGS 引入语义占用预测
- [[2026-03-25_OccAny_Unconstrained_Urban_3D_Occupancy]] - 与空间几何泛化路线存在强关联

## 📌 待探索问题
- 在动态场景下，3DGS 与 4D 表示如何结合得更自然？
- 显式高斯表示与视频生成模型之间最佳接口形式是什么？

---
**维护**: 花火 · 2026-04-12
