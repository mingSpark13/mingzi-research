---
title: "Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control"
authors: "（待补充）"
arxiv: 待补充
date: 2026-03-28
institution: 待补充
conf: 待补充
keywords: 待补充
tags: [VLA架构, ACT动作分块, 灵巧操作, 运动控制]
domain: 通用操作
pdf_path: ""
reading_date: 2026-03-28
reading_status: 已读
summary: "提出可转向的分层控制接口，在子任务、运动与像素坐标等多种抽象层次上增强 VLM→VLA 的可控性。"
related_concepts: ["VLA架构", "ACT动作分块", "灵巧操作", "运动控制"]
---

## 🎯 题目

"Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control"

## 📝 三句摘要

1. 当前层次化VLA（VLM做高层推理 → VLA做低层执行）以自然语言为接口，限制了VLM推理对低层行为的控制力。
2. 提出Steerable Policies：在多种抽象层次（子任务、运动、像素坐标）上训练合成命令，增强低层可控性，解锁VLM预训练知识。
3. 结合学习型高层推理器和in-context learning的VLM，在真实机器人Manipulation任务上优于现有hierarchical VLA baseline。

## 💎 价值评估

**为什么有价值**：直接回答了Paper A的核心问题——「VLM意图层→低层控制」的接口应该怎么设计？答案是：需要多层次抽象的可控命令，而非纯自然语言。

**与Paper A的关系**：
- Paper A主张三层架构：VLM意图层 → 中层意图解析器 → 低层执行
- Steerable VLA验证了：VLM → 多层次抽象命令（子任务/运动/像素坐标）→ VLA执行
- 多层次抽象 = Paper A「中层意图解析器」应该输出的东西

**核心创新**：显式建模VLM-VLA接口的多层次抽象，而不是用自然语言作为唯一接口。

## 🎯 可落地实验点

Paper A的中层「意图解析器」可以参考Steerable VLA的分层设计：
1. 第1层抽象：语义子任务（"拿起杯子"）
2. 第2层抽象：几何运动（"移动到(0.3, 0.2, 0.1)"）
3. 第3层抽象：像素坐标/末端执行器位置

不同抽象层次可以对应不同的执行频次和安全约束等级。

「可落地实验点」

## 🔗 知识图谱
- 父主题：[[02_VLA/README]]
- 相关论文：[[2026-03-28_ST-VLA.md]]（同期发现，层次化VLA的不同角度）
- 前期论文：[[2026-03-28_UniDex.md]]（UniDex是纯端到端，Steerable是层次化对比）


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
