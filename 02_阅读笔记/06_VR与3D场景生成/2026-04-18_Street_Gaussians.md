---
title: "Street Gaussians: Modeling Dynamic Urban Scenes with Gaussian Splatting"
authors: "Yan, Lin, Zhou, Wang, Sun, Zhan, Lang, Zhou, Peng"
institution: "TBD"
arxiv: "2401.01339"
date: 2024-01-02
conf: "arXiv"
pdf_path: "../../01_论文库/3D视觉/2401.01339_Street_Gaussians.pdf"
reading_date: 2026-04-18
reading_status: "已读"
tags:
  - "3D高斯溅射"
  - "3D重建"
  - "视频生成"
  - "感知与3D视觉"
  - "世界模型"
domain: "3D视觉"
---

## 🎯 题目

Street Gaussians: Modeling Dynamic Urban Scenes with Gaussian Splatting

## 📝 三句摘要

1. **问题背景**：传统 NeRF 类方法渲染速度慢（数分钟/帧），难以满足自动驾驶仿真平台的实时性需求。
2. **核心方法**：提出用带语义 logit 和 3D 高斯的点云表示动态城市场景，将前景车辆与背景分离建模，通过可优化追踪姿态和 4D 球谐模型表达动态外观。
3. **关键结果**：在 KITTI 和 Waymo 数据集上以 135 FPS（1066×1600）渲染，半小时完成训练，全面超越 SOTA NeRF 类方法。

## 💎 价值评估

- **研究价值**：Street Gaussians 是 3DGS 在自动驾驶场景重建的开创性工作，将动态场景解耦为静态背景和动态前景，兼顾效率与质量。
- **实践价值**：显式表示使场景编辑和物体合成操作极为自然，适合作为自动驾驶仿真平台的场景基础。
- **扩展潜力**：可与 GaussianWorld/GaussWorld 类世界模型结合，构建可预测的未来帧仿真环境。

## 🎯 可落地实验点

将 Street Gaussians 重建的动态场景用于自动驾驶 VLA 策略的仿真训练，验证 sim-to-real 差距。

## 🔗 知识图谱

- [[concepts/3D高斯溅射]] - 本文核心表征方法
- [[concepts/3D重建]] - 本文任务属于动态场景 3D 重建
- [[concepts/视频生成]] - 动态场景合成本质是时空视频生成
- [[concepts/感知与3D视觉]] - 本文涉及多视角几何融合
- [[concepts/世界模型]] - 可作为世界模型的场景表示基础

## 🔗 相关链接

- [[2026-04-18_GaussianArt]] - 铰接物体 3DGS 扩展
- [[2026-04-18_UniSplat]] - 动态驾驶场景时空融合的更新工作

## 📌 待探索问题

1. Street Gaussians 的动态前景建模能否泛化到未见过的新类别物体（如特种车辆、非机动车）？
2. 4D 球谐模型对快速运动物体的表征是否存在速度上限？高速运动场景下的渲染质量如何？
