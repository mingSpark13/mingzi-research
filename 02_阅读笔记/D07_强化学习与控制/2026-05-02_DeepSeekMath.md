---
title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
authors: "DeepSeek-AI Team"
arxiv: "2402.03300"
date: "2024-02-05"
institution: "DeepSeek-AI"
conf: "arXiv preprint"
keywords: [GRPO, reinforcement learning, mathematical reasoning, policy optimization]
tags: [强化学习, 策略优化, GRPO]
summary: "DeepSeekMath 用 GRPO 去掉独立 value model，在显著降低 RL 微调内存成本的同时保持数学推理性能。"
domain: 强化学习
pdf_path: "../../01_论文库/强化学习/2402.03300_DeepSeekMath.pdf"
reading_date: 2026-05-02
reading_status: 已读
related_concepts: ["GRPO", "强化学习", "策略优化"]
---

# 📖 花火格式笔记

## 🎯 题目

DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

## 📝 三句摘要

1. **问题背景**：传统 PPO 强化学习需要训练 value/critic model，内存开销大、训练不稳定，限制了大模型的 RL 微调规模
2. **核心方法**：提出 GRPO（Group Relative Policy Optimization），用组内相对 advantage 估计 baseline，无需独立 value model，显著降低内存和训练复杂度
3. **关键结果**：DeepSeekMath-7B 在 MATH 数据集上达到 51.7% 准确率（超越 GPT-4 的 42.5%），证明 GRPO 是高效、稳定的 RL 微调方法

## 💎 价值评估

- **🔬 研究价值**：GRPO 是 PPO 的轻量化变体，用组内归一化替代 value model，为大模型 RL 微调提供了更高效的路径，理论上适用于任何需要 reward 优化的场景
- **🚀 实践价值**：内存占用减少 ~50%，训练稳定性提升，已在 DeepSeekMath、DeepSeek-V2 等多个模型中验证，可直接用于 VLA、具身智能等领域的 RFT
- **📈 扩展潜力**：GRPO 不要求 reward 可微，可用于 UAV 跟拍、机器人操作等需要外部 reward（碰撞检测、构图评分、任务成功率）的场景，是 VLA-AN 三阶段训练的理论基础

## 🎯 可落地实验点

**实验设计**：GRPO-RFT for UAV shot-conditioned following
- **对比基线**：
  - SFT-only（只用监督微调）
  - PPO（传统 PPO with value model）
  - GRPO（本文方法）
- **度量指标**：
  - Framing reward（构图得分）
  - Distance reward（距离得分）
  - Collision penalty（碰撞惩罚）
  - Training memory usage（训练内存占用）
  - Training stability（训练稳定性，loss 方差）
  - Final success rate（最终任务成功率）
- **预期结果**：GRPO 在内存占用、训练稳定性上优于 PPO，在最终性能上与 PPO 相当或更好，证明 GRPO 是 UAV 跟拍 RFT 的可行方案

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。

- [[强化学习]] - 本文核心方法类别
- [[策略优化]] - GRPO 属于 policy optimization 范畴
- [[Reward建模]] - GRPO 的核心是 reward-guided optimization

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作），通常 2-5 篇。

- [[2026-04-17_VLA-AN]] - VLA-AN 三阶段训练的 Stage III 使用 GRPO-RFT
- [[2026-04-24_PPO-GRPO-DAPO-GSPO万字详解]] - GRPO 详细解析笔记

## 📌 待探索问题

- GRPO 的组内 advantage 归一化是否会导致 reward scale 敏感性问题（不同任务的 reward 范围差异大时如何处理）？
- 对于 UAV 跟拍这种连续控制任务，GRPO 的 group size 应该设多大（太小可能 baseline 不稳定，太大可能采样效率低）？
- GRPO 是否可以与 KL 散度约束结合，防止策略为了追 reward 偏离 SFT 模型太远（类似 RLHF 中的 KL penalty）？
- 如何设计 UAV 跟拍的 reward 函数，使其既能引导模型学到好的跟拍策略，又不会 reward hacking（例如为了避免碰撞永远停住）？

---
**维护**: 花火 · 2026-05-02
