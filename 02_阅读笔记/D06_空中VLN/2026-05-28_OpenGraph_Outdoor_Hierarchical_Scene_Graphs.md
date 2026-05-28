---
title: "OpenGraph: Open-Vocabulary Hierarchical Scene Graphs for Large-Scale Outdoor Environments"
authors: 待补充
arxiv: 待补充
date: 2024
institution: 待补充
conf: RAL 2024
keywords: [outdoor hierarchical graph, LiDAR, scene graph, open-vocabulary, robot navigation]
tags: ["场景图", "语义导航", "开放词汇感知", "感知与3D视觉", "具身智能"]
domain: 语义导航
pdf_path: ""
reading_date: 2026-05-28
reading_status: 摘要级整理
summary: "OpenGraph 面向大尺度户外环境，把图像实例/caption 投影到 LiDAR 点云，构建 object-centric map，并基于道路/区域连通性组织成层级图，适合园区/道路/城市导航。"
related_concepts: ["场景图", "语义导航", "开放词汇感知", "感知与3D视觉", "具身智能"]
---

# 📖 花火格式笔记

## 🎯 题目

OpenGraph: Open-Vocabulary Hierarchical Scene Graphs for Large-Scale Outdoor Environments

## 📝 三句摘要

1. **问题背景**：室内层级图方法很难直接覆盖校园、道路、广场等大尺度户外环境，而低空导航与巡检又天然需要 outdoor region hierarchy。  
2. **核心方法**：OpenGraph 先从图像中提取实例与 caption，再把语义投影到 LiDAR / 点云上形成 object-centric map，并利用道路、车道、区域连通关系把环境组织成层级图。  
3. **关键结果**：它提供了从 object-centric perception 过渡到大尺度 outdoor hierarchical graph 的一条明确路线，适合机器人在开放世界做导航与语义查询。  

## 💎 价值评估

- **研究价值**：对主人低空/校园/园区导航任务很关键，因为它比 HOV-SG 更接近室外真实场景。  
- **实践价值**：如果 AirSpark 后续进入校园 outdoor 区域建模，OpenGraph 是比纯室内方法更直接的结构参考。  
- **扩展潜力**：可与 Clio 的 task-driven 压缩、NavRAG 的 scene tree 指令生成结合，形成面向任务的 outdoor semantic memory。  

## 🎯 可落地实验点

- 在校园/园区场景中，将“道路/楼栋/广场/操场/立面区域/设备区”做成 OpenGraph 风格层级。  
- 比较 LiDAR/点云支持的 outdoor region graph 与仅图像 landmark list 对导航推理的提升。  
- 尝试把 OpenGraph 的 outdoor hierarchy 接到 AirSpark 的 route planning + landmark reasoning 模块。  

## 🔗 知识图谱

- [[concepts/场景图]]  
- [[concepts/语义导航]]  
- [[concepts/开放词汇感知]]  
- [[concepts/感知与3D视觉]]  
- [[concepts/具身智能]]  

## 🔗 相关链接

- [[2026-05-28_HOV-SG_Hierarchical_OpenVocabulary_3D_Scene_Graphs]] - 室内层级图直接对照项  
- [[2026-05-28_ConceptGraphs_OpenVocabulary_3D_Scene_Graphs]] - object-centric graph 前置层  
- [[2502.11142_NavRAG]] - 层级场景树到任务指令生成的相关工作  

## 📌 待探索问题

- 低空无人机场景里，LiDAR 稀疏或缺失时如何退化成纯视觉版本的 OpenGraph？  
- 室外区域边界（道路/广场/楼体立面）怎样定义，才能既利于检索又利于规划？  
