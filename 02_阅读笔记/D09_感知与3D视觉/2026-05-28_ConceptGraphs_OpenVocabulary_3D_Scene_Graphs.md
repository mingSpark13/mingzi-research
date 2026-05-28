---
title: "ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning"
authors: 待补充
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: [open-vocabulary 3D scene graph, RGB-D, object graph, CLIP, SAM, planning]
tags: ["感知与3D视觉", "场景图", "开放词汇感知", "语义导航", "具身智能"]
domain: 感知与3D视觉
pdf_path: ""
reading_date: 2026-05-28
reading_status: 摘要级整理
summary: "ConceptGraphs 从 2D foundation model 的对象候选与特征出发，结合 RGB-D 和相机位姿投影融合到 3D，构建开放词汇 object-centric scene graph，服务感知与规划。"
related_concepts: ["感知与3D视觉", "场景图", "开放词汇感知", "语义导航", "具身智能"]
---

# 📖 花火格式笔记

## 🎯 题目

ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning

## 📝 三句摘要

1. **问题背景**：开放场景中的机器人不能只依赖封闭类别标签，需要把 2D foundation model 的感知结果稳定提升到 3D 对象图层，才能支持开放词汇查询与规划。  
2. **核心方法**：ConceptGraphs 使用 CLIP / DINO / SAM 等 2D foundation model 提取逐帧对象 proposal 与语义特征，再通过 RGB-D 与相机位姿投影到 3D，并在多视角间做实例关联融合，最终得到 object-centric scene graph。  
3. **关键结果**：它提供了一条从真实探索轨迹直接构造 open-vocabulary 3D object graph 的标准范式，可支持开放词汇查询、空间关系表达与后续规划。  

## 💎 价值评估

- **研究价值**：这是“2D foundation model → 3D object graph”路线的代表工作，正好回答主人场景语义标注方案里“真实/未知场景如何自动建对象图”的核心问题。  
- **实践价值**：如果 AirSpark 后续要接第三方场景、真实采集轨迹或无 actor 标签环境，ConceptGraphs 很适合作为 object-level 语义层前端。  
- **扩展潜力**：可与区域层级建模（HOV-SG / OpenGraph）结合，进一步从 object graph 提升到 region graph / hierarchical scene memory。  

## 🎯 可落地实验点

- 在 AirSpark 的真实/扫描场景数据上，验证“2D foundation model + 深度/位姿投影 + 3D 对象融合”是否能稳定构建开放词汇 object graph。  
- 用对象图作为中间层，比较“直接 object list”与“带空间关系的 scene graph”对 LLM 导航推理的差异。  
- 在后续区域层级建模前，先做 object-centric memory baseline，评估对目标搜索与 landmark grounding 的提升。  

## 🔗 知识图谱

- [[concepts/感知与3D视觉]]  
- [[concepts/场景图]]  
- [[concepts/开放词汇感知]]  
- [[concepts/语义导航]]  
- [[concepts/具身智能]]  

## 🔗 相关链接

- [[2024_SG-Nav_Scene_Graph_Navigation]] - 3D scene graph 直接服务 LLM 导航推理的相关工作  
- [[2025_3D_GRAND]] - 3D-language dense grounding 数据格式的参考  
- [[2025_UnrealLLM]] - 程序化场景生成与语义场景表达的另一条路线  

## 📌 待探索问题

- ConceptGraphs 在动态场景或长轨迹场景中，多视角实例关联的稳定性如何保证？  
- object-centric graph 往上提升成 floor / room / corridor 层级图时，哪些几何/拓扑规则最关键？  
