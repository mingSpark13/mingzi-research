---
type: concept
id: concept.Loco-Manipulation
pageType: concept
updated: "2026-05-14"
---

# Loco-Manipulation

**别名**：运动操作、locomotion-manipulation、移动操作

## 定义

Loco-Manipulation 指机器人在运动（locomotion）过程中同时执行操作（manipulation）任务，要求全身协调控制——腿部/底盘负责移动，手臂/末端执行器负责操作，两者需要实时协同。

## 核心挑战

- **全身协调**：运动产生的扰动影响操作精度，操作负载影响运动稳定性
- **高维动作空间**：人形机器人 30+ DOF 的联合控制
- **接触丰富**：同时处理地面接触（足部）和操作接触（手部）
- **Sim-to-Real**：复杂接触动力学难以精确仿真

## 典型平台

- **人形机器人**：Unitree H1/G1、Figure 01、Boston Dynamics Atlas
- **四足+手臂**：Spot + arm、ANYmal + arm
- **轮式+手臂**：移动机械臂（Mobile Manipulation）

## 与相关概念的关系

## 相关概念
- [[concepts/全身协调运动]]
- [[concepts/腿足机器人]]
- [[concepts/灵巧操作]]

- [[全身协调运动]] - Loco-Manipulation 的核心控制问题
- [[灵巧操作]] - 操作侧的子任务
- [[强化学习]] - 主流训练范式
- [[Sim2Real]] - 核心工程挑战
- [[Isaac Lab]] - 主流仿真训练平台

## 代表论文

- [[2026-03-20_AGILE]] - AGILE: 人形 loco-manipulation 端到端工作流，Isaac Lab 标准化评测

---
**维护**: 花火 · 2026-04-17

## 相关概念
- [[concepts/全身协调运动]]
- [[concepts/腿足机器人]]
- [[concepts/灵巧操作]]
