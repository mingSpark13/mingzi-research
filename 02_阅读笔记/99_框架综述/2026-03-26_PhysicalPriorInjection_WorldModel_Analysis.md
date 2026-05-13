---
title: "物理先验注入大模型 & MPC风格世界模型优化 — 主人分析框架"
authors: 主人的技术分析
arxiv: ""
date: 2026-03-26
institution: 个人研究
conf: 研究框架综述
keywords: 物理先验, MPC, World Model, 约束生成, 滚动优化
tags: ["MPC", "世界模型"]
domain: 世界模型
pdf_path: ""
reading_date: 2026-03-26
reading_status: 已读
related_concepts: ["MPC"]
---

## 🎯 题目

物理先验注入大模型 & MPC风格世界模型优化 — 研究框架综述

## 📝 三句摘要

1. **问题背景**：大模型生成无法保证输出符合物理规律，且缺乏对长期后果的建模能力，需要借鉴MPC的控制理论框架改造生成式世界模型。
2. **核心方法**：提出四层物理先验注入体系（训练软先验→结构约束→采样硬约束→生成后投影）和四种MPC风格滚动优化路线（多步rollout loss→候选评估→价值引导→强化微调）。
3. **关键结果**：物理保证只有三种情况：输出空间参数化、每步硬投影/校正、仿真器作为世界演化内核；最有前景的架构是 Generator + Physics Prior/Constraint Projector + Value Critic + Receding-Horizon Replan。

## 💎 价值评估

- **🔬 研究价值**：系统梳理了"大模型+控制理论"的融合路径，是主人研究世界模型方向的核心理论框架。
- **🚀 实践价值**：为具身操作和无人机world model研究提供了从"会生成"到"会受约束地、为长期目标而生成"的完整路线图。
- **📈 扩展潜力**：该框架可指导Dreamer系列、Phys4D、Interactive World Simulator等具体工作的改进方向。

## 🎯 可落地实验点

**实验设计**：构建主人的"生成式MPC"无人机世界模型系统
- **架构**：Action-conditioned World Model (Generator) + Physics-constrained Projection (Physics Prior) + Task Critic (Value Model) + Receding-Horizon Replan
- **对比基线**：纯DreamerV3、无约束diffusion world model
- **度量指标**：长时rollout物理一致性(PhyWorldBench/EPiCS)、任务成功率、Sim2Real迁移效果
- **预期结果**：混合架构应在物理一致性和任务成功率上同时优于单一方法

## 🔗 知识图谱

- [[世界模型]] - 核心研究对象
- [[物理一致性]] - 核心优化目标之一
- [[MPC]] - 控制理论框架，本分析的核心借鉴对象
- [[动作条件预测]] - Action-conditioned prediction是具身world model的核心

## 🔗 相关链接

本文分析引用的核心论文（需入库）：

- [[2026-01-28_ConstrainedGeneration]] - 硬约束vs软约束保证能力区分，方法论基础
- [[2025-06-30_RoboScape]] - 第一层注入（训练时软先验）典型代表
- [[2025-12-10_EToT]] - 第三种保证（仿真器作为世界内核）典型代表
- [[2025-06-17_PCFM]] - 第三层注入（采样时硬约束）代表
- [[2025-04-23_SafeFlow]] - CBF引导采样，同属第三层
- [[2025-01-08_LLMPC]] - 路线B（推理时候选评估）代表
- [[2026-03-19_DreamPlan]] - 路线D（强化微调）代表
- [[2026-03-24_OmniVTA]] - Reflex correction承认纯预测不足，支撑框架核心判断

## 📌 待探索问题

- 如何在"生成式MPC"架构中平衡生成多样性与约束严格性？
- Value Critic的设计（任务成功 vs 安全 vs 能耗）如何自动学习而非手动设计？

---
**维护**: 花火 · 2026-04-12
