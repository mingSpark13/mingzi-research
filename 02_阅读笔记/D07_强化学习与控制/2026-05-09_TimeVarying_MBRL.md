---
title: Model-Based Reinforcement Learning for Control under Time-Varying Dynamics
authors: Klemens Iten, Bruce Lee, Chenhao Li, Lenart Treven, Andreas Krause, Bhavya Sukhija
arxiv: 2604.0226
date: 2026-04-02
institution: ETH Zürich, ETH AI Center
conf: IEEE under review
keywords:
- model-based reinforcement learning
- non-stationary dynamics
- adaptive buffer
- continual control
tags:
- 强化学习
- 持续学习
- MPC
- 最优控制
- 运动控制
domain: 强化学习
pdf_path: ../../01_论文库/强化学习/2604.02260_TimeVarying_MBRL.pdf
reading_date: 2026-05-09
reading_status: 已读
related_concepts:
- 强化学习
- 持续学习
- MPC
- 最优控制
- 运动控制
summary: 该工作研究时变动力学下的模型式强化学习，重点解决控制器在环境参数持续漂移时的适应与稳定性问题。
---
# 📖 花火格式笔记

## 🎯 题目

Model-Based Reinforcement Learning for Control under Time-Varying Dynamics

## 📝 三句摘要

1. **问题背景**：现有学习控制和 MBRL 大多默认系统动力学平稳不变，但真实机器人会因磨损、载荷变化和环境漂移持续变动。
2. **核心方法**：论文提出面向时变动力学的 continual MBRL 设定，并用受限数据缓冲区的 optimistic MBRL 思路实现 R-OMBRL 与 SW-OMBRL，通过周期重置或滑动窗口抑制陈旧数据污染。
3. **关键结果**：作者给出了 variation-budget 下的 dynamic regret 理论分析，并在连续控制任务中证明自适应 buffer 比直接累积历史数据的 MBRL baseline 更稳。

## 💎 价值评估

- **🔬 研究价值**：这篇把“非平稳动力学下 MBRL 为什么会坏掉”讲得很清楚，还给了可落地的 regret 视角。
- **🚀 实践价值**：对长期运行机器人、飞行器、负载变化系统都很实用，尤其适合主人这边会遇到的硬件漂移和跨环境控制问题。
- **📈 扩展潜力**：可以直接嫁接到世界模型训练缓存、在线微调策略，甚至给无人机长期自适应控制做底层理论支撑。

## 🎯 可落地实验点

**实验设计**：在仿真无人机或机械臂中构造缓慢漂移动力学，验证滑动窗口 MBRL 的收益
- 对比基线：标准 MBRL（全历史数据）、固定窗口、周期重置窗口
- 度量指标：累计回报、漂移后恢复速度、模型校准误差、dynamic regret 近似指标
- 预期结果：滑动窗口或重置策略在动力学漂移后恢复更快，且模型不确定性更可信

## 🔗 知识图谱

- [[强化学习]] - 本文核心是非平稳环境下的 RL 控制
- [[持续学习]] - 需要在跨 episode 漂移中不断适应新动力学
- [[MPC]] - MBRL 规划与滚动控制思路与 MPC 强相关
- [[最优控制]] - dynamic regret 与最优策略跟踪构成本文理论主线
- [[运动控制]] - 论文落点就是现实控制系统在动态变化下的执行稳定性

## 🔗 相关链接

- [[2026-05-09_Dream_to_Fly]] - 同样是模型驱动控制/学习路线，可对比世界模型在飞行控制中的实际收益
- [[2026-04-19_2604.14678_Energy-MPC-Aerial]] - 都涉及学习与控制结合，适合对照非平稳场景下的 MPC/MBRL 边界
- [[2026-04-19_2604.13645_SimReal_CoTraining]] - 若把时变动力学视为分布漂移，可和 sim-real 共训机制联动思考

## 📌 待探索问题

- 当动力学漂移是突变而不是缓慢变化时，滑动窗口和周期重置是否还足够，还是需要显式变点检测？
- 这套 buffer 机制若接到高维神经世界模型上，会不会因为表示漂移带来新的不稳定项？

---
**维护**: 花火 · 2026-05-09
