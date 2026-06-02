---
title: "SAM 3: Segment Anything with Concepts"
authors: "Nicolas Carion, et al. (Meta AI)"
arxiv: "2511.16719"
date: "2025-11-20"
institution: Meta AI Research
conf: arXiv
keywords: ["SAM", "Segment Anything", "Promptable Concept Segmentation", "Video Tracking", "Unified Detection"]
tags: ["感知与3D视觉", "多模态统一架构"]
summary: "SAM 3 将 Segment Anything 扩展到概念级 promptable segmentation，在开放词汇图像/视频分割与跟踪上显著超过既有系统。"
domain: 感知与3D视觉
pdf_path: "../../01_论文库/感知与3D视觉/2511.16719_SAM3.pdf"
reading_date: "2026-05-12"
reading_status: 已读
related_concepts: ["感知与3D视觉", "多模态统一架构"]
---

# 📖 花火格式笔记

## 🎯 题目

SAM 3: Segment Anything with Concepts

## 📝 三句摘要

1. **问题背景**：SAM 2 在图像/视频分割跟踪上取得重要进展，但主要依赖几何prompt（点、框），对语义概念的开放词汇理解能力有限；现有方法难以用自然语言概念（"yellow school bus"）或图像示例灵活指定分割目标。
2. **核心方法**：提出 SAM 3，一个统一模型，通过概念prompt（短名词短语、图像示例或两者组合）实现图像/视频中物体的检测、分割和跟踪；引入 Promptable Concept Segmentation (PCS) 任务，通过 presence head 解耦识别与定位，并构建 4M 概念标签的大规模数据引擎。
3. **关键结果**：SAM 3 在图像和视频 PCS 上均比现有系统精度提升约 2 倍，同时在传统视觉分割任务上改进了 SAM 2 的能力；开源 SAM 3 及 SA-Co benchmark。

## 💎 价值评估

- **🔬 研究价值**：将 SAM 从几何prompt扩展到语义概念prompt，是 SAM 系列的重要演进；PCS 任务定义清晰，评测基准完整；解耦识别与定位的 presence head 有方法论创新。
- **🚀 实践价值**：可用于无人机航拍场景理解（如指定分割"建筑物"、"道路"、"车辆"）；视频跟踪与分割一体化对 UAV 动态目标跟踪有直接价值；开放词汇能力可替代部分检测器功能。
- **📈 扩展潜力**：可与 VLA 结合作为视觉感知层；可扩展到 4D（三维+时间）分割；其数据引擎构建方法对 UAV 场景数据采集有参考价值。

## 🎯 可落地实验点

**实验设计**：将 SAM 3 集成到 UAV 人体跟随系统，替代或增强现有检测/分割模块
- 对比基线：YOLO 检测 + SAM 2 分割 vs SAM 3 统一分割跟踪
- 度量指标：人体分割精度、跟踪 ID 一致性、遮挡恢复能力、帧率
- 预期结果：SAM 3 的概念级分割提升对"穿红衣的人"等语义指定目标的跟踪鲁棒性

## 🔗 知识图谱

- [[感知与3D视觉]] - 本文核心任务（图像/视频分割与跟踪）
- [[多模态统一架构]] - 概念prompt（文本+图像）统一建模方式

## 🔗 相关链接

- [[2023_SAM]] - SAM 2: 本文前身，SAM 系列基础
- [[2024_SAM2]] - SAM 2: 视频分割跟踪基础版本

## 📌 待探索问题

- SAM 3 的 presence head 解耦识别与定位，与传统检测-分割两阶段方法相比，在遮挡严重场景下的优势是否显著？
- 4M 概念标签的数据引擎如何构建？是否有适用于 UAV 场景的特定领域数据？如何避免语义歧义（如"bank"同时指银行和河岸）？

---
**维护**: 花火 · 2026-05-12
