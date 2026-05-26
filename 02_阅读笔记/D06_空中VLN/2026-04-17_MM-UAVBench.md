---
title: "MM-UAVBench: How Well Do Multimodal Large Language Models See, Think, and Plan in Low-Altitude UAV Scenarios?"
date: 2026-04-17
authors: Unknown
venue: arXiv 2512.23219
tags: ["D06"]
summary: "MM-UAVBench 从感知、认知、规划三维度评估 MLLM 在低空无人机场景的能力，暴露小目标、俯视视角与动态环境下的系统短板。"
papertype: benchmark
pdf_path: ""
reviewer: 花火
related_concepts: ["空中操作", "VLA架构", "多模态统一架构"]
---

## 三句话摘要

1. MM-UAVBench 系统评估 MLLM 在低空无人机场景下的感知/认知/规划三大核心能力维度，覆盖 19 类任务
2. 认知维度包含多层级：物体/场景/事件；规划维度包含空中+地面 agent 双模式
3. 暴露了当前 MLLM 在 UAV 特有挑战（小目标、俯视视角、动态场景）下的系统性弱点

## 核心贡献

- **三维度 19 任务评测框架**：感知（物体检测/分割/计数）+ 认知（场景理解/事件推理）+ 规划（路径/任务分配）
- **UAV 特有考量**：多层级认知 + 空中+地面双 agent 规划
- **开源数据+代码**：HuggingFace 公开

## 对 D06 的价值

- 更上游的认知评测锚点：可用于检验 VLM 在空中场景下的基础能力是否「先站得住」
- 与 UAVReason 互补：UAVReason 偏空间/时序推理，MM-UAVBench 更全面覆盖感知-认知-规划
