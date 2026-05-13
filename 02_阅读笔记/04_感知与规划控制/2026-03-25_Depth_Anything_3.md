---
title: "Depth Anything 3: Recovering the Visual Space from Any Views"
authors: Depth Anything Team
arxiv: 2511.10647
date: 2025-11-13
institution: ByteDance Seed Team
conf: arXiv
keywords: Depth Anything 3, Depth Estimation, Geometry Recovery, Visual Space
tags: ["深度估计"]
domain: 计算机视觉
pdf_path: ../../01_论文库/计算机视觉/2025_Depth_Anything_3.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["深度估计"]
---

## 🎯 题目
Depth Anything 3: Recovering the Visual Space from Any Views

## 📝 三句摘要
1. DA3 强调从任意视角输入中恢复具有空间一致性的几何结构，而不只是做孤立单帧深度估计。
2. 它用极简但可扩展的 depth-ray / transformer 设计，把深度恢复提升为更通用的视觉空间重建问题。
3. 在 InSpatio-World 中，DA3 被明确作为 Step 2，用于估深度并渲染点云，为生成模型提供几何锚点。

## 💎 价值评估
- **🔬 研究价值**：把几何恢复从“辅助任务”升级为世界建模中的显式前置步骤。
- **🚀 实践价值**：可以直接用于几何锚定、点云构建、相机控制视频重渲染等系统。
- **📈 扩展潜力**：适合作为视频世界模型中显式空间支撑模块。

## 🎯 可落地实验点
**实验设计**：在主人关注的视频世界模型链路中，用 DA3 替换普通深度估计器，比较点云稳定性与新视角视频质量。

## 🔗 知识图谱
- [[深度估计]] - DA3 的核心任务与能力边界
- [[3D重建]] - 深度是构建空间骨架的直接输入
- [[感知与3D视觉]] - 为空间一致的世界表示提供前置恢复能力

## 🔗 相关链接
- [[2026-03-19_InSpatio_WorldFM]] - InSpatio-World 的 Step 2 直接依赖 DA3
- [[2026-03-25_ReCamMaster]] - 需要几何支撑的相机控制重渲染路线
- [[2026-03-25_WorldScore]] - 几何一致性是世界生成评测的重要维度

## 📌 待探索问题
- DA3 提供的几何锚点对长时视频一致性的提升上限有多高？
- 在机器人场景中，DA3 与 LiDAR / 多视图 SfM 是否可以混合使用？

---
**维护**: 花火 · 2026-04-12
