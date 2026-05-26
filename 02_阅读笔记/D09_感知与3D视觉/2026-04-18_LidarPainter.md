---
title: "LidarPainter: One-Step Away From Any Lidar View To Novel Guidance"
authors: "TBD"
institution: "TBD"
arxiv: "2507.12114"
date: 2026-04-18
conf: "arXiv"
pdf_path: "../../01_论文库/3D视觉/2507.12114_LidarPainter.pdf"
reading_date: 2026-04-18
reading_status: "已读"
tags:
  - "3D高斯溅射"
  - "感知与3D视觉"
  - "深度估计"
  - "视频生成"
  - "数据合成"
domain: "3D视觉"
---

## 🎯 题目

LidarPainter: One-Step Away From Any Lidar View To Novel Guidance

## 📝 三句摘要

1. **问题背景**：现有方法在视图偏离输入轨迹时出现背景退化、车辆模型损坏等问题，难以生成高质量新视角驾驶场景。
2. **核心方法**：提出单步扩散模型，从稀疏 LiDAR 条件和受损图像中恢复一致的新视角驾驶场景视图，通过 LiDAR 几何条件引导扩散过程。
3. **关键结果**：实现高质量场景补全与新视角合成，解决了视图偏离时的背景退化与模型损坏问题。

## 💎 价值评估

- **研究价值**：将稀疏 LiDAR 与扩散模型结合是 3DGS 新视角合成的重要方向，对多传感器融合有参考意义。
- **实践价值**：稀疏 LiDAR → 高质量场景的思路可用于低密度传感器条件下的数据增强，支撑数据飞轮建设。
- **扩展潜力**：可应用于无人机多视角场景重建，减少采集硬件需求。

## 🎯 可落地实验点

将 LidarPainter 的 LiDAR 引导扩散思路应用于无人机多视角场景重建，探索用少量 LiDAR 数据补全 3DGS 场景，减少采集硬件需求。

## 🔗 知识图谱

- [[concepts/3D高斯溅射]] - 本文核心场景表征方法
- [[concepts/感知与3D视觉]] - 本文涉及多传感器感知融合
- [[concepts/深度估计]] - 场景几何恢复依赖深度估计
- [[concepts/视频生成]] - 新视角合成本质是时空维度的视频生成
- [[concepts/数据合成]] - 稀疏→高质量场景的弱标注数据合成思路

## 🔗 相关链接

- [[2026-04-18_Street_Gaussians]] - 动态驾驶场景 3DGS 重建
- [[2026-04-18_VolSplat]] - 3DGS 族工作

## 📌 待探索问题

1. LidarPainter 在动态前景物体（行人、车辆）存在时的视角合成质量如何？是否会出现运动模糊或物体变形？
2. 单步扩散 vs 多步扩散在视角合成质量与推理速度上的 trade-off 是什么？
