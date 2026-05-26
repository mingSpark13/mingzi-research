---
type: "entity"
subtype: "dataset"
id: "entity.数据集_InteriorGS"
pageType: "entity"
tags: ["3D高斯溅射", "语义导航", "仿真平台"]
summary: "1000个语义标注室内3DGS场景数据集，支持具身导航与空间智能研究，由 SpatialVerse Research Team 发布"
updated: "2026-05-15"
---

# InteriorGS 数据集

**发布方**: SpatialVerse Research Team (Manycore Tech Inc)
**发布时间**: 2025
**数据地址**: https://huggingface.co/datasets/spatialverse/InteriorGS
**GitHub**: https://github.com/manycore-research/InteriorGS
**关联论文**: [[02_阅读笔记/D09_感知与3D视觉/2026-04-18_SAGE-3D]] (arXiv 2510.21307)

## 核心内容

- **规模**: 1,000 个室内场景，80+ 种环境类型（住宅/便利店/婚宴厅/博物馆等）
- **表示**: 3D Gaussian Splatting (.ply)，5M+ 图像重建，支持实时渲染
- **语义标注**: 554,000+ 物体实例，755 类别，每个物体配 3D bounding box
- **占用图**: 每场景提供 occupancy map，支持导航与空间理解
- **轨迹**: 同时支持地面机器人（红色轨迹）和 UAV（黄色轨迹）视角

## 与主人研究的关系

- **D06 空中VLN**：InteriorGS 提供 UAV 视角渲染，是室内无人机导航训练/评测的高质量数据源
- **D01 世界模型**：语义标注 3DGS 场景可作为具身世界模型的训练环境
- **仿真平台参考**：物体级语义 + 占用图的设计思路可迁移到 UE 城市场景标注规范

## 相关概念

- [[concepts/3D高斯溅射]]
- [[concepts/语义导航]]
- [[concepts/仿真平台]]
