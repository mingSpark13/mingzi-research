---
title: "3D Generation for Embodied AI & Robotic Simulation: A Survey"
authors: Tianwei Ye, Yifan Chen, Zhenyang Huang, et al.
arxiv: 2604.26509
date: 2026-04-29
institution: Tsinghua University, Shanghai AI Lab
conf: arXiv preprint
keywords: ["3D generation", "embodied AI", "robotic simulation", "3DGS", "NeRF"]
tags: ["3D视觉", "数据生成", "仿真环境"]
summary: 具身 AI 和机器人仿真训练需要大量高质量 3D 场景，但手工建模成本高、真实数据采集困难，限制了数据规模和多样性
domain: 3D视觉
pdf_path: ../../01_论文库/3D视觉/2604.26509_3DGen_Survey.pdf
reading_date: 2026-05-02
reading_status: 已读
related_concepts: ["3D生成", "具身智能", "仿真环境"]
---
# 📖 花火格式笔记

## 🎯 题目

3D Generation for Embodied AI & Robotic Simulation: A Survey

## 📝 三句摘要

1. **问题背景**：具身 AI 和机器人仿真训练需要大量高质量 3D 场景，但手工建模成本高、真实数据采集困难，限制了数据规模和多样性
2. **核心方法**：综述 3D 内容生成技术（NeRF、3DGS、Diffusion-based 3D 等）在具身 AI 仿真中的应用，涵盖场景重建、物体生成、动态场景建模等
3. **关键结果**：系统梳理了 3D 生成技术的发展脉络、关键方法、应用场景和未来方向，为具身 AI 数据飞轮提供了技术路线图

## 💎 价值评估

- **🔬 研究价值**：首次系统梳理 3D 生成技术在具身 AI 中的应用，明确了从 NeRF 到 3DGS 再到 Diffusion-based 3D 的技术演进路径
- **🚀 实践价值**：为构建具身 AI 数据飞轮提供了完整的技术栈参考，涵盖场景重建、物体生成、动态场景建模、sim-to-real 等关键环节
- **📈 扩展潜力**：可指导 UAV 操作数据工厂的设计（3DGS 场景重建 + Diffusion 物体生成 + 动态场景建模），为 D05 数据飞轮方向提供理论基础

## 🎯 可落地实验点

**实验设计**：3D generation pipeline for UAV manipulation data factory
- **对比基线**：
  - 纯 UE mesh 场景（手工建模）
  - NeRF 场景重建（真实场景重建）
  - 3DGS + Diffusion（本文推荐方法）
- **度量指标**：
  - Scene diversity（场景多样性）
  - Object realism（物体真实感）
  - Sim-to-real gap（仿真到真实的差距）
  - Data generation speed（数据生成速度）
- **预期结果**：3DGS + Diffusion 在场景多样性、物体真实感上优于手工建模，在 sim-to-real gap 上优于纯 NeRF，证明 3D 生成技术对数据飞轮的价值

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。

- [[3D生成]] - 本文核心技术类别
- [[具身智能]] - 应用领域
- [[仿真环境]] - 应用场景

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作），通常 2-5 篇。

- [[2026-04-18_GaussianDWM]] - 3DGS 用于世界模型的代表作
- [[2026-04-18_WorldSplat]] - 3DGS 用于场景重建的代表作

## 📌 待探索问题

- 如何将 3DGS 场景重建与 Diffusion 物体生成结合，构建 UAV 操作数据工厂的完整 pipeline？
- 3D 生成技术在 sim-to-real 中的 domain gap 如何量化和缩小（纹理、光照、物理属性等）？
- 如何用 3D 生成技术构造 UAV 跟拍的多样化场景（不同光照、天气、遮挡、背景等）？
- 动态场景建模（人物运动、物体交互）如何与 3D 生成技术结合，为 UAV 操作提供更真实的训练数据？

---
**维护**: 花火 · 2026-05-02
