---
title: "Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning"
authors: Rohan Deb, Stephen J. Wright, Arindam Banerjee
arxiv: 2603.22430
date: 2026-03-25
institution: 估计为RL/控制方向
conf: arXiv
keywords: MPC, Differentiable World Model, Offline RL, Inference-Time Adaptation
tags: ["MPC"]
domain: 强化学习
pdf_path: ../../01_论文库/世界模型/2603_MPCDiffWorldModel.pdf
reading_date: 2026-03-26
reading_status: 已读
related_concepts: ["MPC"]
---

## 🎯 题目

Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning

## 📝 三句摘要

1. **问题背景**：传统离线RL在推理时不做进一步优化，学到的策略直接应用而无法适应；世界模型仅在训练阶段用于生成 imagined trajectories，推理时缺乏实时优化能力。
2. **核心方法**：提出推理时自适应框架，借鉴MPC思路：利用预训练策略+可微世界模型，在推理时结合MPC做在线优化，而不是只在训练时使用世界模型。
3. **关键结果**：在多个离线RL基准上，推理时MPC+可微世界模型的组合显著超越纯预训练策略，证明了"推理时优化"的重要性。

## 💎 价值评估

- **🔬 研究价值**：明确将MPC的推理时优化思想引入离线RL世界模型，是"生成式MPC"框架的典型实现——生成模型不再只是被动预测器，而是被放进在线优化环里。
- **🚀 实践价值**：适合需要实时适应的无人机场景，推理时可根据真实观测持续优化。
- **📈 扩展潜力**：可与action-conditioned world model结合，构建完整的MPC-style具身规划系统。

## 🎯 可落地实验点

**实验设计**：将MPC+可微世界模型用于无人机实时轨迹规划
- 对比基线：纯预训练策略、纯模型预测控制（基于物理模型）
- 度量指标：推理时任务成功率、实时适应能力、计算效率（FPS）
- 预期结果：MPC+learned world model应在适应性上优于纯预训练策略，在物理正确性上优于纯学习型方法

## 🔗 知识图谱

- [[世界模型]] - 可微世界模型是本文核心组件
- [[MPC]] - MPC是推理时优化的框架
- [[强化学习]] - 离线RL是本文的应用场景
- [[动作条件预测]] - 可与action-conditioned world model结合

## 🔗 相关链接

- [[2025-01-08_LLMPC]] - LLMPC是语言/规划方向的MPC-style工作，本文是其离线RL版本
- [[2026-03-10_InteractiveWorldSimulator]] - Interactive World Simulator提供action-conditioned world model，可作为本文的可微世界模型
- [[2025-06-17_PCFM]] - PCFM是约束采样方法，可与本文的MPC框架结合

## 📌 待探索问题

- 可微世界模型的sim-to-real gap如何在推理时MPC优化中被补偿？
- 推理时MPC的计算延迟与无人机实时控制频率如何匹配？

---
**维护**: 花火 · 2026-04-12
