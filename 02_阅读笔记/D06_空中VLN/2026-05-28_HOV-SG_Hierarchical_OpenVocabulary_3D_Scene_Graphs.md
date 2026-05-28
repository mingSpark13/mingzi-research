---
title: "HOV-SG: Hierarchical Open-Vocabulary 3D Scene Graphs for Language-Grounded Robot Navigation"
authors: 待补充
arxiv: 待补充
date: 2024
institution: 待补充
conf: RSS 2024
keywords: [hierarchical scene graph, open-vocabulary, language-grounded navigation, floor-room-object]
tags: ["场景图", "语义导航", "开放词汇感知", "长程任务规划", "具身智能"]
domain: 语义导航
pdf_path: ""
reading_date: 2026-05-28
reading_status: 摘要级整理
summary: "HOV-SG 构建 floor-room-object 层级开放词汇 3D scene graph，把对象语义进一步组织为区域层级，是 language-grounded robot navigation 的直接结构参考。"
related_concepts: ["场景图", "语义导航", "开放词汇感知", "长程任务规划", "具身智能"]
---

# 📖 花火格式笔记

## 🎯 题目

HOV-SG: Hierarchical Open-Vocabulary 3D Scene Graphs for Language-Grounded Robot Navigation

## 📝 三句摘要

1. **问题背景**：仅有对象级列表不足以支撑复杂语言导航，机器人需要 floor / room / object 层级结构来理解“二楼走廊尽头的 A101 教室门”这类多层级目标。  
2. **核心方法**：HOV-SG 先构建开放词汇 3D segment-level map，再将其组织成 **floor → room → object** 的层级 scene graph，使每一层都具备开放词汇语义特征与语言查询能力。  
3. **关键结果**：它证明层级 scene graph 比扁平 object list 更适合 large-scale multi-story environments 中的 language-grounded navigation。  

## 💎 价值评估

- **研究价值**：这是主人当前 AirSpark/MapMemory 设计里最关键的结构参考之一，直接回答“区域层级怎么建、为什么必须层级化”。  
- **实践价值**：对校园/教学楼/园区多层导航场景尤其重要，适合把 campus → building → floor → corridor/classroom 的层级做成统一 RegionGraph。  
- **扩展潜力**：可与 ConceptGraphs / OpenGraph / Clio 结合，形成 object detection → hierarchical region memory → task-driven retrieval 的完整栈。  

## 🎯 可落地实验点

- 在 AirSpark 的语义地图设计里直接尝试 HOV-SG 风格的层级结构：campus → building → floor → corridor/classroom → object。  
- 比较“扁平对象列表”与“层级区域图”对 LLM/VLM 导航推理效果的差异。  
- 针对低空导航任务扩展 room/floor 概念为 outdoor zone / facade / window band / balcony 等层级。  

## 🔗 知识图谱

- [[concepts/场景图]]  
- [[concepts/语义导航]]  
- [[concepts/开放词汇感知]]  
- [[concepts/长程任务规划]]  
- [[concepts/具身智能]]  

## 🔗 相关链接

- [[2026-05-28_ConceptGraphs_OpenVocabulary_3D_Scene_Graphs]] - object-centric graph 的前置层  
- [[2024_SG-Nav_Scene_Graph_Navigation]] - scene graph 直接 prompt LLM 做导航推理  
- [[2502.11142_NavRAG]] - scene tree 驱动用户需求导航指令生成  

## 📌 待探索问题

- 户外低空场景里“room/floor/object”如何改写为更适合无人机的区域层级？  
- 层级图更新时怎样兼顾增量建图效率与语言查询稳定性？  
