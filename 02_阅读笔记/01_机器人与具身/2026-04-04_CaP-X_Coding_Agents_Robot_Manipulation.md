---
title: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation
authors: Max Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi "Jim" Fan
arxiv: 2603.22435
date: 2026-03-23
institution: NVIDIA · UC Berkeley · Stanford University · Carnegie Mellon University
conf: arXiv
keywords: Code-as-Policy, Coding Agent, Robot Manipulation, LLM, VLM, Benchmark, RL, GRPO, CaP-Gym, CaP-Bench
tags: ["D02", "灵巧操作", "多模态统一架构", "跨载体泛化", "强化学习"]
domain: 通用操作
pdf_path: ../../01_论文库/通用操作/CaPX_2603.22435.pdf
reading_date: 2026-04-04
reading_status: 已读
summary: CaP-X 系统评测并后训练机器人操作 coding agents，结合 CaP-Gym、CaP-Bench 与可验证奖励优化，显著提升真实操作成功率。
related_concepts: ["灵巧操作", "多模态统一架构", "跨载体泛化", "强化学习"]
---

## 🎯 题目

A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation

## 📝 三句摘要

1. **问题背景**："Code-as-Policy"（代码即策略）探索可执行代码如何弥补数据密集型 VLA 方法的不足，但其在具身操作任务中作为自主控制器的有效性尚未被系统研究。
2. **核心方法**：本文提出 CaP-X 框架，包含交互环境 CaP-Gym、系统评测基准 CaP-Bench（覆盖8个难度层级）、无需训练的 CaP-Agent0（多轮交互+视觉差分+自动技能合成+集成推理）、以及基于可验证奖励后训练的 CaP-RL。
3. **关键结果**：前沿模型零样本机器人操作平均成功率约30%+，与人类仍有56个百分点差距；CaP-Agent0在扰动任务上超越部分VLA；CaP-RL让7B coding model从20%提升到72%，并在真实Franka机械臂上接近人类水平。

## 💎 价值评估

- **🔬 研究价值**：首次系统建立 Code-as-Policy 的评测基准，揭示了当前模型对"人类设计脚手架"的依赖问题，并提出无需训练即可提升鲁棒性的框架，为 coding agents 在机器人领域的应用奠定评估基础。
- **🚀 实践价值**：CaP-RL 的 sim-to-real 迁移gap极小，7B模型即可在真实机械臂上接近人类，提供了低成本、高可扩展的机器人技能训练路径；仓库已开源，支持多仿真器和多模型。
- **📈 扩展潜力**：CaP-Agent0 的多轮交互+视觉差分机制可独立迁移到其他 VLA/操纵框架；CaP-Gym 支持自定义 API 和环境扩展，适合作为机器人 Code-as-Policy 的实验平台。

## 🎯 可落地实验点

**实验设计**：将 CaP-X 的 Code-as-Policy 思想引入空中操作 Coding Agent
- 对比基线：原始 VLA 策略（无代码生成）、仅用单轮 code 生成
- 度量指标：任务成功率、执行稳定性、代码生成质量评分
- 预期结果：多轮交互+视觉差分的 Coding Agent 在空中抓取/放置任务上比纯 VLA 提升 >30%

## 🔗 知识图谱

- [[LLM驱动机器人]] - 本文用 LLM 直接生成 Python 代码操控机器人，是 code-as-policy 的核心
- [[具身智能]] - 具身操控是本文的任务场景
- [[VLA]] - 与 VLA 对比，Code-as-Policy 是替代/互补路径
- [[强化学习]] - CaP-RL 使用 GRPO 后训练，是本文的策略改进方法
- [[Sim2Real]] - CaP-RL 实现了 sim2real 最小 gap 迁移

## 🔗 相关链接

- [[2024-10_pi0]] - π0: VLA 领域 prior art，CaP-X 的 code-as-policy 路径与其形成对比/互补
- [[2023_RT-2]] - RT-2: VLA 奠基工作，本文揭示了 code-as-policy 与 VLA 的各自优劣势

## 📌 待探索问题

- Code-as-Policy 在空中机器人（无人机）上的可行性如何？高速运动和动态平衡任务是否对代码生成延迟有严格要求？
- CaP-Bench 揭示模型依赖"人类设计脚手架"，如何让 coding agent 自主发现和构建有用的抽象 API 层？

---
**维护**: 花火 · 2026-04-12
