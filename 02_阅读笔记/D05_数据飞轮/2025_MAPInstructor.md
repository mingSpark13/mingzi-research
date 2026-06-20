---
title: "Scene Map-based Prompt Tuning for Navigation Instruction Generation"
authors: Sheng Fan, Rui Liu, Wenguan Wang, Yi Yang
arxiv: 待补充
date: 2025
institution: Zhejiang University
conf: CVPR 2025
keywords: [navigation instruction, map-based, prompt tuning, LLM, landmark hallucination]
tags: ["语义导航", "具身智能", "视觉语言导航", "提示学习"]
domain: 数据合成
pdf_path: "../../01_论文库/数据合成/2025_MAPInstructor.pdf"
reading_date: 2026-05-28
reading_status: 已读
related_concepts: ["语义导航", "具身智能", "视觉语言导航"]
---

# 📖 花火格式笔记

## 🎯 题目

Scene Map-based Prompt Tuning for Navigation Instruction Generation

## 📝 三句摘要

1. **问题背景**：现有导航指令生成方法只喂文本描述，忽略全局空间地图上下文，导致landmark hallucination（指令中提到场景不存在的地标）和指令不可靠问题。
2. **核心方法**：提出MAPINSTRUCTOR，将egocentric observations投影到3D voxel，结合topological map做prompt tuning；引入landmark uncertainty assessment，通过语义熵评估landmark可靠性，减少幻觉。
3. **关键结果**：在多个导航数据集上验证了地图上下文对指令生成可靠性的提升，landmark hallucination rate显著降低。

## 💎 价值评估

- **🔬 研究价值**：为路线A的语言生成提供了"把地图编码进LLM"的范式，与NavRAG互补——前者强调RAG+用户画像，本文强调地图空间感知。
- **🚀 实践价值**：主人可为低空指令生成设计输入格式：top-down semantic map + target object mask + relative direction + route keypoints + obstacle distribution + altitude constraints，输出high-level command、step-by-step instruction、target referring expression。
- **📈 扩展潜力**：可与主人的VLN评测结合——输入地图+任务描述，LLM生成的自然语言指令可用于评测VLA/VLN模型的指令跟随能力。

## 🎯 可落地实验点

**实验设计**：参考MAPINSTRUCTOR为低空指令生成构建地图编码输入：top-down semantic map（道路网/建筑/植被） + target object mask（巡检目标）+ relative direction + altitude constraints → LLM生成high-level和step-by-step指令。
- 对比基线：纯文本描述指令生成、无地图上下文的指令生成
- 度量指标：Instruction-Goal Consistency、Spatial Referring Accuracy、Hallucinated Landmark Rate、Route Faithfulness
- 预期结果：地图编码输入使landmark hallucination rate从~15%降低到~3%以下

## 🔗 知识图谱

- [[语义导航]] - 本文应用场景
- [[具身智能]] - 下游任务
- [[视觉语言导航]] - 指令驱动的导航

## 🔗 相关链接

- [[2502.11142_NavRAG]] - RAG增强的指令生成
- [[2025_3D_GRAND]] - 3D dense grounding
- [[2603.19822_HUGE_Bench]] - UAV任务基准

## 📌 待探索问题

- 低空场景的top-down semantic map粒度如何定义？需要区分道路边线/建筑轮廓/植被区块/停车场标线吗？
- MAPINSTRUCTOR的landmark uncertainty assessment如何迁移到低空场景的landmark（如"左侧玻璃楼"、"十字路口"）评估？

---
**维护**: 花火 · 2026-05-28
