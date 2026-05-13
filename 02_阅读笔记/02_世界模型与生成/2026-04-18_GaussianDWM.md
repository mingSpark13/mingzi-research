---
title: "GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation"
authors: "Tianchen Deng et al."
arxiv: 2512.23180
date: 2025-12-30
institution: 科研机构
conf: arXiv
keywords: [driving world model, 3D Gaussian, scene understanding, multi-modal generation]
tags: [世界模型, 3D高斯溅射, 感知与3D视觉, 视频生成]
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2512.23180_GaussianDWM.pdf"
reading_date: 2026-04-18
reading_status: 已读
related_concepts: ["世界模型", "3D高斯溅射", "感知与3D视觉", "视频生成"]
---

# 📖 花火格式笔记

## 🎯 题目

GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation

## 📝 三句摘要

1. **问题背景**：现有驾驶世界模型缺乏 3D 场景理解能力，只能在输入数据条件下生成内容，无法对驾驶环境进行理解和推理；且用点云或 BEV 特征表示 3D 空间信息的方法存在信息损失和结构化不足的问题。
2. **核心方法**：提出 GaussianDWM，用 3D Gaussian 作为统一 3D 表示基础，同时支撑场景理解（3D perception）和多模态生成（视频/可控生成），实现"感知-生成"统一的世界模型。
3. **关键结果**：3DGS 的显式几何+外观表示天然支持多视角/多模态一致推理，避免了 BEV/点云的信息瓶颈；模型同时输出 3D 感知结果和未来视频生成，实现理解与生成的双向闭环。

## 💎 价值评估

- **🔬 研究价值**：首个 3DGS-based 驾驶世界模型，统一感知与生成，具有标杆意义
- **🚀 实践价值**：与 UE 数据采集有强协同：UE 场景 → 3DGS → GaussianDWM 风格统一世界模型
- **📈 扩展潜力**：可扩展到无人机、机器人等多模态驾驶场景的联合感知生成

## 🎯 可落地实验点

**实验设计**：构建 UE → 3DGS → GaussianDWM 完整数据管线
- 对比基线：BEV-based 驾驶世界模型
- 度量指标：3D 感知 mIoU / 视频生成 FVD
- 预期结果：3DGS 几何一致性优势在感知指标上超越 BEV 方法

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。

- [[concepts/世界模型]] - 本文核心研究对象，驾驶场景的世界模型
- [[concepts/3D高斯溅射]] - 本文统一 3D 表示基础，同时支撑感知与生成
- [[concepts/感知与3D视觉]] - 3D 场景理解是本文的核心任务之一
- [[concepts/视频生成]] - 多模态视频生成是本文的输出形式

## 🔗 相关链接

- [[2026-04-18_OmniNWM]] - OmniNWM：隐空间世界模型，本文方法论参照
- [[2026-04-18_WorldLens]] - WorldLens：世界模型 + 视频生成联合建模

## 📌 待探索问题

- 3DGS 表示在高速运动模糊场景下的重建质量如何保障？
- 感知与生成的联合训练是否存在任务干扰，如何设计解耦但协同的损失函数？

---
**维护**: 花火 · 2026-04-18
