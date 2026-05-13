---
title: "DA-Flow: Degradation-Aware Optical Flow Estimation with Diffusion Models"
authors: Jaewon Min, Seungryong Kim et al. (KAIST)
arxiv: 2603.23499
date: 2026-03-24
institution: KAIST
conf: arXiv (cs.CV)
keywords: 待补充
tags: []
domain: 计算机视觉
pdf_path: ""
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["深度估计", "视频生成", "3D重建"]
---

## 🎯 题目

"DA-Flow: Degradation-Aware Optical Flow Estimation with Diffusion Models"

## 📝 三句摘要

1. 现有光流模型在真实退化场景（blur/noise/compression）下性能严重下降，DA-Flow 首次提出 degradation-aware 光流估计任务。
2. 核心洞察：图像修复扩散模型的中间表征天然具有退化感知能力，但缺乏时序建模；DA-Flow 通过时空全注意力将其提升为时序感知。
3. Hybrid 架构（扩散特征+卷积特征融合）+ 迭代优化框架，在多种退化benchmark上大幅领先。

## 💎 价值评估

⭐⭐⭐⭐ 高价值。光流是视频理解/3D重建核心任务，DA-Flow 切入了一个被忽视的实用场景（抗退化），方法创新点清晰。KAIST 视觉组出品，质量有保障。

## 🎯 可落地实验点

在无人机飞行视频流中，用 DA-Flow 做抗退化光流估计，提升动态场景下的深度估计和运动分割精度。

## 🔗 相关链接

- Paper: https://arxiv.org/abs/2603.23499
- Project: https://cvlab-kaist.github.io/DA-Flow

## 🔗 知识图谱

- [[深度估计]]
- [[视频生成]]
- [[3D重建]]


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
