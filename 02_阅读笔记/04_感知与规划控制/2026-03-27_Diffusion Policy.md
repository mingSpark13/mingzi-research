---
title: 'Diffusion Policy: Diffusion Models for Visuomotor Robot Control'
authors: Chenhao Li, etc.
arxiv: ''
date: 2024
institution: Columbia HCRL
conf: LeRobot Documentation / ACT++
keywords: diffusion model, imitation learning, visuomotor, action generation
tags:
- 模仿学习
domain: 通用操作
pdf_path: ../../01_论文库/强化学习/2303_DiffusionPolicy.pdf
reading_date: 2026-03-27
reading_status: 已读
related_concepts: ["扩散策略", "模仿学习", "ACT动作分块", "抓取检测"]
- 模仿学习
---


## 🎯 题目

Diffusion Policy — 扩散模型用于视觉运动机器人控制

## 📝 三句摘要

1. **问题背景**：传统模仿学习（如 BC）在处理多峰动作分布时容易丢失多样性，单点回归难以建模复杂动作分布。
2. **核心方法**：Diffusion Policy 用扩散过程（denoising diffusion）逐步生成动作序列，能够更自然地建模多模态动作分布，提升动作质量和鲁棒性。
3. **关键结果**：在多种操作任务上相比 BC 基线有显著提升，尤其在动作分布复杂场景；ACT++ 将其与 ACT 并列为双核心策略。

## 💎 价值评估

- **🔬 研究价值**：将扩散生成思想引入机器人动作控制，是近年来模仿学习方向的重要进展，启发了多个后续工作。
- **🚀 实践价值**：实现相对成熟，代码开源，适合作为「ACT vs DP」对比项目的另一极；比大模型路线更易本地部署。
- **📈 扩展潜力**：可与语言指令结合实现 open-vocabulary manipulation；也可与 6D pose、抓取检测等感知模块串联。

## 🎯 可落地实验点

**实验设计**：Diffusion Policy 与 ACT 在「抽屉开关」任务上的对比实验
- 对比基线：ACT (action chunking)
- 度量指标：任务成功率、动作序列多样性（entropy）、推理延迟
- 预期结果：DP 在「同一状态多种正确操作」场景下多样性更强，ACT 在执行速度上占优

## 🔗 知识图谱
- [[扩散策略]]
- [[模仿学习]]
- [[ACT动作分块]]
- [[多模态动作分布]]
- [[扩散策略]]

## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- [[2026-03-27_ACT]] - 动作分块 Transformer，ACT++ 将两者并列作为双核心策略对比

## 📌 待探索问题

- 扩散模型的推理延迟是否会影响实时控制场景的可行性？
- 在 few-shot 演示数据下，DP 和 ACT 的数据效率差异有多大？

---
**维护**: 花火 · 2026-04-12
