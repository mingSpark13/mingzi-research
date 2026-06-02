---
title: Learning Dynamic Pick-and-Place for a Legged Manipulator
authors: Moonkyu Jung, Jiseong Lee, Zhengmao He, Donghoon Youm, Juhyeok Mun, HyeongJun Kim, Hyunsik Oh, Donghyuk Choi, Jungwoo Hur, Jie Song, Jemin Hwangbo
arxiv: ""
date: 2026-04-12
institution: KAIST + HKUST(GZ)
conf: IEEE Robotics and Automation Letters (RA-L) 2026
keywords: [Reinforcement Learning, Legged Robots, Mobile Manipulation, Whole-body Control, Hierarchical RL]
tags: [强化学习, 腿足机器人, 全身协调运动, 模仿学习]
summary: "该工作用分层强化学习、在线质量自适应与课程学习实现四足机械臂高速连续动态拾放。"
domain: 腿足机器人
pdf_path: "../../01_论文库/腿足机器人/Learning_Dynamic_Pick-and-Place.pdf"
reading_date: 2026-05-13
reading_status: 已读
related_concepts: ["强化学习", "腿足机器人", "全身协调运动", "模仿学习"]
---

# 📖 花火格式笔记

## 🎯 题目

Learning Dynamic Pick-and-Place for a Legged Manipulator

## 📝 三句摘要

1. **问题背景**：四足机械臂结合了灵活 locomotion 和多自由度机械臂，但现有 RL 方法只能处理轻物体、慢速分段动作，无法充分利用全身协调能力实现动态连续的拾放操作。

2. **核心方法**：提出分层强化学习框架——低层 locomotion 控制器提供稳定全身基础，高层统一策略负责完整拾放过程（含抓取、搬运、放置、收回）；引入在线质量自适应模块，通过物理交互估计物体质量，实现对不同重量物体的鲁棒操作；同时使用成功率驱动课程学习逐步扩展工作高度范围。

3. **关键结果**：仿真中 86.05% 成功率（最高 2.3kg），真实世界 6 类场景平均 73.3%（最高 1.3kg），平均执行时间 4.06s，相比之前准静态方法（43.8s）提速 10 倍，首次实现操作过程中保持高速 base velocity 的连续动态拾放。

## 💎 价值评估

- **🔬 研究价值**：首个实现四足机械臂快速连续动态拾放的工作，填补了"动态 loco-manipulation" 标准化连续任务流程的空白；分层控制结构为高维四足+臂系统提供了可复用的策略分解思路。

- **🚀 实践价值**：在 Unitree B1 + 6-DOF 机械臂上验证，质量自适应模块无需额外传感器，课程学习直接扩展工作高度至 2 倍基座高度，可迁移至其他四足平台。

- **📈 扩展潜力**：质量自适应 + 课程学习的组合可推广至其他重型/多形态物体操作；分层框架可与视觉-语言任务结合（如 "把桌上的可乐罐放到红色箱子"）。

## 🎯 可落地实验点

**实验设计**：在花火四足平台上复现分层 RL 拾放流程
- 平台：四足机器人（如 ANYmal/Unitree） + 6-DOF 协作臂
- 对比基线：单阶段统一 RL 策略（不分层）、纯 MPC 方法
- 度量指标：Success Rate、Execution Time、Payload Mass 容忍度
- 课程设计：L1 地面→L2 10cm→L3 30cm→L4 60cm→L5 1.1m，逐步增加
- 预期结果：分层策略在高度变化场景下成功率比单阶段高 >20%

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。
> 字典真源：`06_知识Wiki/_views/概念关键词字典.md`

- [[强化学习]] - 核心训练范式，低层+高层控制器均用 RL 训练
- [[腿足机器人]] - 验证平台，四足+6-DOF 机械臂
- [[全身协调运动]] - 核心问题，协调 locomotion 与 manipulation
- [[模仿学习]] - 课程学习中可能用到专家演示辅助
- [[灵巧操作]] - 末端机械臂的精确抓放控制

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作）

- [[2026-05-13_DQ-Net]] - DQ-Net: Whole-Body Coordination for Dynamic Object Grasping (KAIST, RA-L 2026)，同一团队同时期工作，DQ-Net 专注动态抓取，本文专注拾放
- [[2024-Visual Whole-Body Control]] - Visual Whole-Body Control for Legged Loco-Manipulation (UCSD, CoRL 2024)，高层策略代表对比基线

## 📌 待探索问题

- 在线质量自适应模块依赖力觉信号，在完全未知物体（无任何先验质量分布）时的估计误差有多大？是否有主动探测策略来减小误差？
- 分层框架中低层控制器是 frozen 再训练高层，两阶段训练的收敛性是否有理论保证？能否实现端到端一次性联合训练？

---
**维护**: 花火 · 2026-05-13
