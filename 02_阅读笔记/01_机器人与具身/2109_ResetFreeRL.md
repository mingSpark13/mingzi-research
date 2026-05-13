---
title: "Reset-Free Reinforcement Learning via Multi-Task Learning"
authors: Multiple
arxiv: 2109.00001
date: 2021-09
institution: various
conf: arXiv / CoRL 2021
keywords: Reset-Free RL, Multi-Task Learning, Self-Reset, Continuous Learning
tags: ["D02"]
domain: 强化学习
pdf_path: ../../01_论文库/具身智能/2109_ResetFreeRL.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["强化学习"]
---

## 🎯 题目

Reset-Free Reinforcement Learning via Multi-Task Learning

## 📝 三句摘要

1. **问题背景**：传统 RL 需要人工 reset 来重置环境，效率低，真实世界无法频繁人工干预。
2. **核心方法**：将不同任务互相作为 reset，不同任务间形成自复位循环，减少人工 reset 依赖。
3. **关键结果**：在多任务环境中验证了 reset-free RL 的可行性，人工干预显著减少。

## 💎 价值评估

- **🔬 研究价值**：Reset-free RL 是 RoboClaw"EAP 自复位"思想的前身，证明"不同任务互为 reset"是可行路线。
- **🚀 实践价值**：为真实世界机器人持续学习提供了减少人工干预的思路。
- **📈 扩展潜力**：RoboClaw 在此基础上引入了 VLM-driven agent + EAP，是 reset-free 思想在 VLA 时代的进化。

## 🎯 可落地实验点

**实验设计**：以 reset-free 作为 RoboClaw/PMI 框架的底层机制
- 对比基线：固定 task 需要 reset、无 reset-free
- 度量指标：人工 reset 次数、连续任务完成数
- 预期结果：reset-free 应显著减少人工干预

## 🔗 知识图谱

- [[强化学习]] - reset-free RL 是 RL 的重要分支
- [[具身智能]] - 真实世界持续学习

## 📌 待探索问题

- reset-free 与主人的"意图-身体双状态框架"的结合点在哪里？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
