---
title: Explainable Deep Reinforcement Learning for UAV autonomous path planning
authors: Lei He, Nabil Aouf, Bifeng Song
arxiv: ""
date: 2021-11
institution: 待补（作者来自该论文署名机构）
conf: Aerospace Science and Technology, Volume 118, 107052 (2021)
keywords: UAV path planning, deep reinforcement learning, explainability, obstacle avoidance, AirSim
tags: []
domain: 空中操作
pdf_path: ""
reading_date: 2026-04-01
reading_status: 已读
related_concepts: ["强化学习", "空中操作", "无人机避障", "Sim2Real", "运动控制"]
---

## 🎯 题目

Explainable Deep Reinforcement Learning for UAV autonomous path planning

## 📝 三句摘要

1. **问题背景**：无人机自主路径规划通常要在复杂未知环境中兼顾避障、到达目标和控制稳定性，而传统 DRL 方法虽然有效，却常常是黑箱，难以解释策略为何这么飞。
2. **核心方法**：该工作提出一种 **可解释的深度强化学习无人机路径规划框架**，把 UAV 在复杂环境下的自主导航建模为 DRL 问题，并强调策略决策的可解释性与可分析性，从而提升方法的可信度与部署价值。
3. **关键结果**：这篇论文后来被 `UAV_Navigation_DRL_AirSim` 项目直接作为核心引用基础，说明它已经沉淀成可复现的 AirSim + SB3 无人机路径规划路线，对仿真训练到真实迁移具有较强工程参考意义。

## 💎 价值评估

- **🔬 研究价值**：这篇属于较早期、很扎实的无人机 DRL 路径规划工作，亮点不是“模型很大”，而是把 **可解释性** 带进无人机策略学习里，这对安全关键系统很重要。
- **🚀 实践价值**：如果主人要补无人机 DRL 基础路线，这篇很适合作为传统 baseline；尤其是 AirSim 项目已给出一条工程复现链，方便拿来做环境搭建、奖励设计和策略训练的起点。
- **📈 扩展潜力**：它可以作为 SPF 这类 learning-free 方法的对照组，也能与安全护栏、世界模型、语义感知模块结合，演化成“可解释 + 可控 + 可泛化”的空中智能体系统。

## 🎯 可落地实验点

**实验设计**：基于 AirSim 复现该论文/项目路线，建立一个经典 DRL 无人机自主路径规划 baseline。
- 对比基线：DQN/PPO/SAC 等常规 DRL 路线，与 learning-free 的 SPF 路线做横向比较
- 度量指标：到达成功率、碰撞率、路径长度、收敛速度、策略可解释性可视化质量
- 预期结果：传统 DRL 在特定训练分布内性能稳定，但跨环境泛化与开放词汇适应性会显著弱于 learning-free VLM 路线

## 🔗 知识图谱
- [[空中操作]] - 无人机自主路径规划是空中智能体核心任务
- [[强化学习]] - 论文主方法范式
- [[无人机避障]] - 在未知环境中规避障碍并到达目标
- [[Sim2Real]] - AirSim 训练路线天然关联仿真到真实迁移
- [[运动控制]] - 路径规划最终要转成稳定飞行控制执行

## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- [[2026-04-01_See_Point_Fly]] - learning-free VLM 导航路线，可与传统 DRL 路线形成强对照
- [[2026-04-01_MolmoSpaces]] - 都强调泛化评测的重要性，但该文更偏经典仿真训练路线
- [[2026-04-01_GigaWorld-Policy]] - 若未来把 DRL 路径规划嵌入 world-action model，可研究传统控制先验与生成式策略的融合

## 📌 待探索问题

- 这篇论文中的“可解释性”具体是通过注意力、显著图还是中间决策变量实现的？是否足够支撑安全部署？
- 在跨环境、跨天气、跨传感器设置下，这种传统 DRL 路线的泛化上限在哪里？
- 如果给主人当前的研究路线服务，是否应把它保留为 baseline，而把主要精力投向 SPF / 世界模型 / 开放词汇导航这类更新范式？

---
**维护**: 花火 · 2026-04-12
