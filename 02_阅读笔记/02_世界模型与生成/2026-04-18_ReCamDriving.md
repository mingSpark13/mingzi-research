---
title: "ReCamDriving: LiDAR-Free Camera-Controlled Novel Trajectory Video Generation"
authors: "Yaokun Li et al."
arxiv: "2512.03621"
date: "2025-12-05"
institution: ""
conf: "arXiv"
tags:
  - "视频生成"
  - "3D高斯溅射"
  - "物理一致性"
domain: "世界模型"
pdf_path: "../../01_论文库/世界模型/2512.03621_ReCamDriving.pdf"
reading_date: "2026-04-18"
reading_status: "已读"
---

# 📖 花火格式笔记

## 🎯 题目

ReCamDriving: LiDAR-Free Camera-Controlled Novel Trajectory Video Generation

## 📝 三句摘要

1. **问题背景**：现有 novel camera trajectory 可控生成方法依赖 LiDAR 提供稀疏深度线索，泛化受限；repair-based 方法难以处理复杂瑕疵，难以实现精确相机可控生成。
2. **核心方法**：提出 ReCamDriving，纯视觉（camera-only）控制的新轨迹视频生成框架。利用密集且场景完整的 3DGS 渲染作为显式几何引导，绕开 LiDAR 依赖，实现精确相机可控生成。
3. **关键结果**：通过两阶段方案（先 3DGS 完整重建，再新轨迹渲染+修复），在 Waymo 等数据集上实现了高质量 novel trajectory 生成，兼顾生成质量和可控性。

## 💎 价值评估

- **🔬 研究价值**：提出纯视觉 novel trajectory 视频生成方案，绕过 LiDAR 依赖，技术路线简洁但有工程价值。
- **🚀 实践价值**：对 UE 仿真平台的新视角/新轨迹数据扩增有直接参考价值，可用于仿真数据多样性增强。
- **📈 扩展潜力**：两阶段范式（先重建再渲染）可扩展到任意目标相机轨迹的数据扩增场景。

## 🎯 可落地实验点

**实验设计**：将 ReCamDriving 的两阶段范式引入 UE 城市场景数据扩增，在 UE 中先对程序化生成的场景做 3DGS 重建，再基于该重建生成多样化的 novel camera trajectory 视频。
- 对比基线：单一轨迹渲染 vs 多轨迹渲染数据扩增
- 度量指标：下游感知模型精度、数据多样性指标
- 预期结果：多轨迹扩增数据训练出的感知模型在真实场景泛化更优

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[concepts/视频生成]] - 核心任务，novel trajectory 驾驶视频生成
- [[concepts/3D高斯溅射]] - 密集场景重建为新轨迹渲染提供几何引导
- [[concepts/数据合成]] - 数据扩增范式，提升训练数据多样性
- [[concepts/物理一致性]] - 新轨迹渲染中保持物理合理性

## 🔗 相关链接

> 链接本文核心引用的相关论文。

- [[2026-04-18_Street_Gaussians]] - Street Gaussians：驾驶场景 3DGS 相关工作
- [[2026-04-18_PhyGenesis]] - PhyGenesis：物理一致性 driving world model 相关

## 📌 待探索问题

- ReCamDriving 需要高质量 3DGS 重建，计算成本较高，如何在推理速度和重建质量间做权衡？
- 纯视觉方案在没有 LiDAR 的情况下，对动态物体（行人、车辆）的建模效果如何？

---
**维护**: 花火 · 2026-04-18
