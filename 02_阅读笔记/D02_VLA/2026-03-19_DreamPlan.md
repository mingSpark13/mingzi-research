---
title: "DreamPlan: Vision-Language World Model Planning with Reinforcement Fine-Tuning"
authors: Multiple (from arXiv 2603.16860)
arxiv: 2603.16860
date: 2026-03-19
institution: 估计为VLM具身规划方向
conf: arXiv
keywords: World Model Planning, VLM Planner, RL Fine-tuning, Long-Horizon
tags: ["D02", "长程任务规划"]
domain: 具身智能
pdf_path: ../../01_论文库/世界模型/2603_DreamPlan.pdf
reading_date: 2026-03-26
reading_status: 已读
summary: "VLM planner在长时任务上容易出现任务连贯性丧失和短视问题，单纯靠监督学习无法让模型学会"为长期目标而规划"。"
related_concepts: ["长程任务规划"]
---

## 🎯 题目

DreamPlan: Vision-Language World Model Planning with Reinforcement Fine-Tuning

## 📝 三句摘要

1. **问题背景**：VLM planner在长时任务上容易出现任务连贯性丧失和短视问题，单纯靠监督学习无法让模型学会"为长期目标而规划"。
2. **核心方法**：DreamPlan将world model rollout与reinforcement fine-tuning结合，用长时任务连贯性作为reward信号，对VLM planner做RL式微调，使其学会考虑多步后果。
3. **关键结果**：在多种长时具身任务上，DreamPlan显著提升了VLM planner的任务完成率和多步连贯性。

## 💎 价值评估

- **🔬 研究价值**：是"路线D：滚动优化思想做强化微调"的典型代表，证明了RL fine-tuning可以让VLM planner学会"为长期目标生成"。
- **🚀 实践价值**：可用于无人机长时任务（巡检、搜索与救援）的VLM规划器微调。
- **📈 扩展潜力**：可与action-conditioned world model结合，构建"预测-评估-回滚-微调"的完整闭环。

## 🎯 可落地实验点

**实验设计**：将DreamPlan的RL fine-tuning思路用于无人机VLM导航规划器
- 对比基线：纯监督学习VLM planner、Dreamer-style latent world model
- 度量指标：长时任务成功率、多步连贯性、Sim2Real迁移效果
- 预期结果：RL fine-tuned planner应在长时任务上更优

## 🔗 知识图谱

- [[世界模型]] - World model rollout + RL fine-tuning是本文核心
- [[长程任务规划]] - 长时连贯性是核心优化目标
- [[VLA]] - VLM planner是VLA的一种形式

## 🔗 相关链接

- [[2025-01-08_LLMPC]] - LLMPC是语言/规划方向的MPC-style工作，DreamPlan是其具身版本
- [[2026-03-10_InteractiveWorldSimulator]] - Interactive World Sim提供world model rollout，DreamPlan在其上做RL fine-tuning
- [[2026-03-24_OmniVTA]] - OmniVTA同样做VLM+RL路线，可对比

## 📌 待探索问题

- RL fine-tuning的reward如何设计？长时任务的成功信号如何回传到每一步？
- DreamPlan是否会出现"学会在world model里作弊"（model exploitation）的问题？

---
**维护**: 花火 · 2026-04-12
