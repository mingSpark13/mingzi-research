---
title: "CognitiveDrone: A VLA Model and Evaluation Benchmark for Real-Time Cognitive Task Solving and Reasoning in UAVs"
date: 2026-04-17
authors: Unknown
venue: arXiv 2503.01378
tags: ["D06", "长程任务规划", "跨载体泛化", "VLA"]
papertype: model+benchmark
pdf_path: ""
reviewer: 花火
related_concepts: ["长程任务规划", "跨载体泛化"]
---

## 三句话摘要

1. CognitiveDrone 是首个专注复杂认知任务的无人机 VLA 模型，数据涵盖人类识别、符号理解、推理三大类，共 8000+ 条仿真轨迹
2. 提出 CognitiveDrone-R1：额外增加 VLM 推理模块，在执行高频控制前先用 VLM 简化任务指令
3. 在 CognitiveDroneBench 评测中，基础版 59.6% 成功率，R1 版达 77.2%，比 RaceVLA 高 30%，证明推理模块显著提升认知任务表现

## 核心贡献

- **认知任务数据集**：8000+ 仿真轨迹，三大类别（Human Recognition / Symbol Understanding / Reasoning）
- **CognitiveDrone-R1**：VLM 推理模块 + VLA 执行模块两段式架构，推理结果作为指令压缩/改写送入低层控制
- **CognitiveDroneBench**：开源评测基准，覆盖多种认知难度场景

## 对 D06 的价值

- **推理-执行解耦**：CognitiveDrone-R1 的「先用 VLM 推理 → 再 VLA 执行」两段式与 D06 的分层架构思路一致
- **评测基准**：CognitiveDroneBench 可作为 D06 评测体系的补充
- **认知任务覆盖**：填补了空中 VLA 领域「认知推理能力评测」的空白

## 局限 / 不足

- 仅仿真测试，真实世界泛化性未验证
- VLM 推理模块增加延迟，不适合超实时场景
- 三阶段训练需要额外的 VLM 调用成本
