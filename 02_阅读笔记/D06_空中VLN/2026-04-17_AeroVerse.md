---
title: "AeroVerse: UAV-Agent Benchmark Suite for Simulating, Pre-training, Finetuning, and Evaluating Aerospace Embodied World Models"
date: 2026-04-17
authors: Unknown
venue: arXiv 2408.15511
summary: "AeroVerse 提供面向空中具身世界模型的全链路 benchmark 与数据飞轮框架，把仿真、预训练、微调和评测第一次统一到同一套 UAV-agent 基准里。"
tags: ["D06", "空中VLN", "世界模型", "数据飞轮"]
papertype: platform+benchmark
pdf_path: ""
reviewer: 花火
related_concepts: ["空中VLN"]
---

## 三句话摘要

1. AeroVerse 是首个面向 Aerospace Embodied World Model 的全链路基准套件，覆盖仿真平台 → 预训练 → 微调 → 评测，首次明确定义 5 类下游任务并构建对应评测
2. 构建了 AerialAgent-Ego10k（真实第一人称航拍图文预训练数据）和 CyberAgent-Ego500k（虚拟图-文-姿态对齐数据）两大数据集
3. 5 类下游任务：空中场景感知、空间推理、导航探索、任务规划、运动决策，首次统一评测空中具身智能全栈能力

## 核心贡献

- **AerialAgent-Ego10k**：首个大规模真实第一人称航拍图文预训练数据集（城市无人机视角）
- **CyberAgent-Ego500k**：虚拟图文姿态对齐数据，支撑世界模型预训练
- **5 类下游任务统一评测**：场景感知 / 空间推理 / 导航探索 / 任务规划 / 运动决策，覆盖空中具身智能全栈
- **全链路平台**：仿真 → 预训练 → 微调 → 评测，完整数据飞轮

## 对 D06 的价值

- **数据飞轮**思路与 D05 方向对齐，AeroVerse 可作为空中领域的数据工厂参考
- **全链路评测**是 D06 验收表设计的重要参照（5 类任务 vs D06 的 4+ 维度）
- **世界模型预训练**可作为 D06 高层语义推理能力的上游支撑

## 局限 / 不足

- 数据集偏向模拟/虚拟数据，真实世界泛化性未充分验证
- 世界模型评测指标尚不成熟，定义尚在早期
- 与 VLN 任务的对应关系未明确
