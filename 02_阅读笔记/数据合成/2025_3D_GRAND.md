---
title: "3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination"
authors: Multiple Authors
arxiv: 待补充
date: 2025
institution: Multiple
conf: CVPR 2025
keywords: [3D-LLM, dense grounding, hallucination, dataset, scene-language]
tags: ["具身智能", "数据合成", "评测基准", "多模态学习"]
domain: 数据合成
pdf_path: "../../01_论文库/数据合成/2025_3D_GRAND.pdf"
reading_date: 2026-05-28
reading_status: 已读
related_concepts: ["具身智能", "数据合成", "评测基准", "多模态学习"]
---

# 📖 花火格式笔记

## 🎯 题目

3D-GRAND: A Million-Scale Dataset for 3D-LLMs with Better Grounding and Less Hallucination

## 📝 三句摘要

1. **问题背景**：3D-LLM存在严重的幻觉问题——模型生成的描述与真实3D场景不符，根源在于缺乏大规模dense 3D-text grounding训练数据。
2. **核心方法**：提出3D-GRAND数据集，包含40,087个室内场景和620万条densely-grounded scene-language指令；同时提出3D-POPE基准专门评估3D-LLM幻觉问题。
3. **关键结果**：使用3D-GRAND训练显著降低幻觉率并提升grounding准确率；scaling实验表明密集grounding数据量越大，3D-LLM性能越稳定提升；sim-to-real迁移显示合成数据可泛化到真实场景。

## 💎 价值评估

- **🔬 研究价值**：为dense 3D grounding提供了百万级数据集和评测基准，是主人"低空场景dense grounding"的核心参考——低空指令不能只有一句任务指令，需要对象级/区域级/关系级/任务级的多层grounding。
- **🚀 实践价值**：主人的benchmark可借鉴3D-POPE设计"低空语言-目标-区域"grounding评估，每1000个自动样本抽50个人工审核。
- **📈 扩展潜力**：可扩展到低空3D-language-action grounding——"white car"→car_012→3D bbox/mask，"parking lot near building"→region_003 polygon，"building on left of road"→relation。

## 🎯 可落地实验点

**实验设计**：参考3D-GRAND为低空场景构建dense grounding数据集：对象级（"white car"→3D bbox/mask）、区域级（"parking lot"→polygon）、关系级（"left of road"→relation）、任务级（"inspect left building"→target+behavior），建立低空3D-POPE幻觉评估基准。
- 对比基线：单条任务指令、模板化描述
- 度量指标：Grounding Accuracy、Landmark Localization Error、Relation Accuracy、Hallucination Rate
- 预期结果：dense grounding使target grounding accuracy从~80%提升到~95%以上

## 🔗 知识图谱

- [[具身智能]] - 3D-LLM应用
- [[数据合成]] - 大规模数据集
- [[评测基准]] - 3D-POPE基准
- [[多模态学习]] - 3D-text对齐

## 🔗 相关链接

- [[2502.11142_NavRAG]] - 导航语言生成
- [[2025_MAPInstructor]] - 地图编码指令生成
- [[2603.19822_HUGE_Bench]] - UAV任务基准

## 📌 待探索问题

- 3D-GRAND的dense grounding是针对室内场景设计的，低空场景的grounding粒度应如何调整？需要区分建筑外立面层次、飞行高度层、停机坪/施工区等功能区域吗？
- 主人如何建立低空场景的"3D landmark localization error"标准？哪些是低空特有的landmark（如"高压线塔"、"通信基站"、"屋顶停机坪"）？

---
**维护**: 花火 · 2026-05-28
