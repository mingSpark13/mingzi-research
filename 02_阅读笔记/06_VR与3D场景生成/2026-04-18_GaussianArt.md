---
title: "GaussianArt: Unified Modeling of Geometry and Motion for Articulated Objects"
authors: "Licheng Shen et al."
institution: "TBD"
arxiv: "2508.14891"
date: 2026-04-18
conf: "arXiv"
pdf_path: "../../01_论文库/3D视觉/2508.14891_GaussianArt.pdf"
reading_date: 2026-04-18
reading_status: "已读"
tags:
  - "3D高斯溅射"
  - "3D重建"
  - "视频生成"
  - "感知与3D视觉"
  - "具身智能"
domain: "3D视觉"
---

## 🎯 题目

GaussianArt: Unified Modeling of Geometry and Motion for Articulated Objects

## 📝 三句摘要

1. **问题背景**：传统方法将几何重建与关节运动解耦（先重建不同状态的几何，再后处理对齐），导致流程复杂且难以扩展。
2. **核心方法**：首次提出联合建模铰接物体几何与运动的统一框架，基于 3DGS 表示铰接物体几何，通过学习关节运动参数（轴向/位置）实现 motion-aware 的 3D 重建，支持未见姿态的零样本合成。
3. **关键结果**：在多个铰接物体数据集（关节门、抽屉、机械臂等）上实现高质量几何+运动联合建模，可直接输出用于仿真平台的运动学结构。

## 💎 价值评估

- **研究价值**：铰接物体几何与运动联合建模是 3DGS 领域的重要突破，为具身智能场景理解提供了新的数据基础。
- **实践价值**：可直接输出带运动学结构的动态物体资产，适用于仿真平台数据采集与程序化资产生成。
- **扩展潜力**：可与 VLA 世界模型结合，实现对动态操作场景的联合预测与规划。

## 🎯 可落地实验点

在 UE5 中导入 GaussianArt 重建的铰接物体资产（机械臂、门），验证关节运动在仿真环境中的物理一致性，评估对数据采集管线的影响。

## 🔗 知识图谱

- [[concepts/3D高斯溅射]] - 本文核心 3D 表征方法
- [[concepts/3D重建]] - 本文任务属于 3D 重建范畴
- [[concepts/视频生成]] - 关节运动合成本质是时空维度的视频生成
- [[concepts/感知与3D视觉]] - 本文涉及的场景理解能力
- [[concepts/仿真平台]] - 本文输出可直接用于仿真平台

## 🔗 相关链接

- [[2026-04-18_VolSplat]] - 3DGS 族工作，同为 VolSplat 系列
- [[2026-04-18_Street_Gaussians]] - 动态场景 3DGS 重建，场景覆盖更广

## 📌 待探索问题

1. GaussianArt 的关节参数学习方法是否泛化到未见过铰接类型？零样本能力边界在哪里？
2. 输出的运动学结构能否直接被 Isaac Sim / Genesis 等仿真平台解析和使用？
