---
title: "Global End-Effector Pose Control of an Underactuated Aerial Manipulator via Reinforcement Learning"
authors: "（待补充）"
arxiv: 待补充
date: 2026-03-28
institution: 待补充
conf: 待补充
keywords: 待补充
tags: ["D02"]
domain: 通用操作
pdf_path: ""
reading_date: 2026-03-28
reading_status: 已读
related_concepts: ["空中操作"]
---

## 🎯 题目

"Global End-Effector Pose Control of an Underactuated Aerial Manipulator via Reinforcement Learning"

## 📝 三句摘要

1. 空中机械臂（quadrotor + 2-DoF轻量机械臂）面临严格重量和复杂度约束，使用差分机构实现全6-DoF末端执行器姿态控制。
2. 在仿真中使用PPO训练，产生前馈加速度和机体角速率命令 + 关节角度目标，由INDI姿态控制器和PID关节控制器跟踪。
3. 实现了厘米级位置精度和degree级姿态精度，能处理重负载和推动等接触丰富的任务。

## 💎 价值评估

**为什么有价值**：直接展示了空中精细操作的工程可行性路线——RL + 经典控制器的组合。轻量化空中平台 + 学习-based控制 = 未来空中操作的主流范式。

**与Paper A的关系**：
- Paper A低层执行层可以参考：RL产生高层运动指令 → INDI/PID跟踪执行
- 仿真→真实迁移（sim-to-real）的训练范式对主人有参考价值
- contact-rich manipulation证明了空中操作可以处理物理交互任务

**核心创新**：针对欠驱动空中机械臂的端到端RL控制，证明学习-based方法在此类系统上的可行性。

## 🎯 可落地实验点

Paper A低层执行层可以参考本工作的"RL策略 + 经典控制器"组合：
1. 仿真中训练RL策略产生末端执行器运动指令
2. 低层用INDI/PID跟踪执行，保证稳定性和抗干扰
3. 适合主人的空中操作场景（需要飞行稳定性+操作精确性）

「可落地实验点」

## 🔗 知识图谱
- 父主题：[[03_空地迁移/README]]
- 相关论文：[[2026-03-28_GroundedPlanBench.md]]（空间规划层面）
- 前期论文：[[2026-03-27_OnFly.md]]（无人机导航的RL+控制组合）


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
