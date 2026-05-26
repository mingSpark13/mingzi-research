---
title: "UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation"
authors: Jie Liu, Wanli Ouyang et al.
arxiv: 2603.23500
date: 2026-03-24
institution: 未知
conf: arXiv (cs.CV)
keywords: 待补充
tags: []
domain: 多模态生成
pdf_path: ""
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["视频生成", "多模态统一架构", "流匹配"]
---

## 🎯 题目

"UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation"

## 📝 三句摘要

1. UniGRPO 提出统一 RL 框架，联合优化 interleaved 生成（文本推理+图像合成）两个策略，通过 GRPO + FlowGRPO 双驱动实现。
2. 关键改进：去掉 classifier-free guidance（保证线性 unbranched rollouts）+ 用 MSE 替代 latent KL penalty（更稳健的反奖励hack）。
3. 在 reasoning-driven image generation 任务上验证，显著提升生成质量。

## 💎 价值评估

⭐⭐⭐⭐ 高价值。多模态生成+推理是当前热点方向，UniGRPO 的统一框架思路清晰，两处关键改动有工程价值。值得关注后续在真实 interleaved 生成任务上的扩展。

## 🎯 可落地实验点

将 UniGRPO 的 dual-GRPO 框架迁移到"视觉推理+动作生成"场景，用 RL 联合优化 VLA 模型的推理链和执行动作质量。

## 🔗 相关链接

- Paper: https://arxiv.org/abs/2603.23500

## 🔗 知识图谱

- [[视频生成]]
- [[多模态统一架构]]
- [[流匹配]]


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
