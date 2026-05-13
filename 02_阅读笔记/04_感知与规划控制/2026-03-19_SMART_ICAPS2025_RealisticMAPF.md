---
title: "Advancing MAPF towards the Real World: A Scalable Multi-Agent Realistic Testbed (SMART)"
authors: Jingtian Yan, Zhifei Li, William Kang, Kevin Zheng, Yulun Z hang, Zhe Chen, Yue Zhang, Daniel Harabor, Stephen F. Smith, Jiaoyang Li
arxiv: "2503.04798"
date: 2025-08-14
institution: Carnegie Mellon University / Monash University
conf: ICAPS 2025
keywords: 多智能体路径规划, MAPF, 多机器人仿真, 物理引擎, 执行监控, Action Dependency Graph, 仓储自动化, 规模化
tags: ["任务与运动规划"]
domain: 多机器人系统
pdf_path: ../../01_论文库/多机器人系统/SMART_ICAPS2025_arXiv2503.04798.pdf
reading_date: 2026-03-19
reading_status: 已读
summary: "SMART 将多智能体路径规划放进真实物理约束下的大规模仿真与执行监控闭环，弥补了 MAPF 研究与真实部署之间的验证断层。"
related_concepts: ["任务与运动规划"]
---

## 🎯 题目

 Advancing MAPF towards the Real World: A Scalable Multi-Agent Realistic Testbed (SMART)（推进MAPF走向真实世界：一个规模化多智能体真实仿真测试平台）

## 📝 三句摘要

1. **问题背景**：现有 MAPF（多智能体路径规划）算法能在秒级内为数百个机器人规划无碰撞路径，但依赖简化机器人模型，忽略了运动力学约束和执行不确定性，导致在真实环境中的表现未知。
2. **核心方法**：提出 SMART——基于物理引擎的规模化多智能体真实仿真测试平台，集成了 ARGoS3 / Isaac Sim 两个仿真器 + 执行监控服务器（基于 Action Dependency Graph）+ 机器人专用执行器，支持运动力学、碰撞动力学、通信延迟、执行不确定性等真实因素。
3. **关键结果**：SMART 可扩展至 **数千个机器人** 且保持一致可复现的结果（此前工具连100个机器人都无法处理）；提供在线可视化界面；已在真实移动机器人上验证鲁棒性；代码已开源。

## 💎 价值评估

- **🔬 研究价值**：
  - 填补了 MAPF 算法从理论到真实物理环境验证的空白
  - ADG（Action Dependency Graph）执行框架提供了将简化模型规划与真实执行桥接的理论基础
  - 开源代码 + 可直接导入 MovingAI benchmark MAPF 实例，降低研究门槛
- **🚀 实践价值**：
  - 仓储/物流机器人公司可直接使用 SMART 评估适合自己场景的 MAPF 算法
  - 支持 ARGoS3 和 Isaac Sim 两个主流仿真器，工程集成成本低
  - 真实物理验证过的执行监控框架，可直接迁移到实际机器人部署
- **📈 扩展潜力**：
  - 可与 RAPID-UAM 空中机械臂项目的多机协同规划模块结合
  - 可扩展到异构多机器人系统（空中+地面协同）
  - ADG 执行框架可作为多机器人执行监控的通用底层组件

## 🎯 可落地实验点

**实验设计**：使用 SMART 评估 RAPID-UAM 多机协同场景下的规划算法性能
- 对比基线：单臂独立规划 vs 多臂协调规划（使用 SMART 内置 MAPF 求解器）
- 度量指标：规划时间、碰撞率、执行成功率、总任务完成时间
- 预期结果：协调规划在多臂场景下显著优于独立规划，尤其是在窄通道/高密度障碍物环境
- 注意事项：需将 RAPID-UAM 的机器人模型（空中机械臂）适配到 SMART 的执行器接口

## 🔗 知识图谱
- [[任务与运动规划]] - Multi-Agent Path Finding，多智能体路径规划，本文核心研究问题
- [[多机器人协调]] - 仓储/物流自动化场景
- [[强化学习]]
- [[空中操作]]
## 🔗 相关链接

链接本文核心引用的论文：

- [[]] - MAPF 基础工作（待补充）
- [[]] - MovingAI benchmark（待补充）
- [[]] - ADG 执行框架原始论文（待补充）

## 📌 待探索问题

- 问题1：SMART 的 ADG 执行框架能否直接应用于空中机器人（相比地面轮式机器人，空中机器人的执行不确定性来源更多——气流、负载变化等）？
- 问题2：SMART 目前支持 ARGoS3 和 Isaac Sim，是否可以扩展到 ROS/Gazebo 生态，以复用现有的无人机仿真环境？
- 问题3：数千机器人的规模扩展中，计算瓶颈主要在规划阶段还是执行监控阶段？ADG 的计算复杂度是多少？

---
**维护**: 花火 · 2026-04-12
