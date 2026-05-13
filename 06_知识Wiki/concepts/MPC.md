---

type: "concept"
level: "secondary"
parent: "规划与控制"
tags: ["MPC"]
summary: "Model Predictive Control，滚动优化的经典控制框架"
updated: "2026-04-17"
id: "concept.MPC"
pageType: "concept"
---


# 概念：MPC (模型预测控制)

> Model Predictive Control，通过滚动优化和约束满足实现系统控制的经典控制理论框架。

## 说明

MPC 是将"未来预测"与"优化控制"结合的经典框架，核心公式：

$$\min_{u_{t:t+H-1}} \sum_{k=0}^{H-1} \ell(x_{t+k}, u_{t+k}) + V_f(x_{t+H})$$

subject to:
$$x_{t+k+1} = f(x_{t+k}, u_{t+k}), \quad g(x_{t+k}, u_{t+k}) \le 0$$

在具身 AI 语境下，MPC 是改造大模型生成的核心借鉴对象：
- **世界模型** ≈ 动力学模型 $f$
- **价值函数** ≈ $\ell + V_f$
- **约束函数** ≈ $g$
- **滚动优化** ≈ receding horizon replanning

## 核心思想

1. **滚动优化**：不一次性求解全时域最优，而是在每个时刻只执行第一步，到下一时刻重新求解
2. **约束满足**：将物理约束、安全约束显式编码进优化问题
3. **反馈校正**：基于真实观测不断修正预测和优化

## 与大模型结合的四种路线

| 路线 | 说明 | 代表工作 |
|------|------|---------|
| A：多步Rollout Loss | 训练时让模型对长时后果负责 | Self-Forcing |
| B：候选评估 | 推理时生成多个候选并打分 | LLMPC |
| C：价值引导 | 用价值函数引导生成分布 | SafeDiffuser |
| D：强化微调 | 用长时reward回传修正生成器 | DreamPlan |

## 与World Model的关系

MPC 的 hybrid 架构（Generator + Physics Prior + Value Critic + Receding-Horizon Replan）是具身 world model 的最有前景方向：

- **Generator**：大模型/扩散模型负责生成候选
- **Physics Prior / Constraint Projector**：保证物理可行性
- **Value Critic**：选择多步最优
- **Receding-Horizon Replan**：每步根据真实观测重规划

---
**通过 Obsidian Backlinks 自动建立双向链接，无需手动维护论文列表。**
