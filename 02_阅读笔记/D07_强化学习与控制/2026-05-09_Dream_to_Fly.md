---
title: 'Dream to Fly: Model-Based Reinforcement Learning for Vision-Based Drone Flight'
authors: Angel Romero, Ashwin Shenai, Ismail Geles, Elie Aljalbout, Davide Scaramuzza
arxiv: 2501.14377
date: 2026-01-01
institution: University of Zurich (UZH) Robotics and Perception Group
conf: IEEE ICRA 2026
keywords:
- model-based RL
- vision-based drone
- dreamerv3
- autonomous drone racing
- pixel-to-control
tags:
- 强化学习
- 无人机避障
- 单目无地图导航
domain: 空中操作
pdf_path: ../../01_论文库/空中操作/2501_14377_Dream_to_Fly.pdf
reading_date: 2026-05-09
reading_status: 已读
related_concepts:
- 强化学习
- 无人机避障
- 单目无地图导航
summary: Dream to Fly 使用 DreamerV3 式模型式强化学习，让无人机仅凭单目视觉学会高速自主飞行，最高可达 9 m/s。
---
# 📖 花火格式笔记

## 🎯 题目

Dream to Fly: Model-Based Reinforcement Learning for Vision-Based Drone Flight

## 📝 三句摘要

1. **问题背景**：无人机竞速已成为测试机器人学习能力的前沿基准，人类飞行员能直接从单目相机像素映射到控制指令，但现有端到端方法依赖中间表征简化或模仿学习（IL）大量预训练，在纯像素条件下训练困难、无模型RL（如PPO/SAC）样本效率低下。
2. **核心方法**：利用 DreamerV3（基于世界模型的MBRL框架）从零开始，仅用单目相机像素作为观测训练视觉运动策略，无需中间表征或IL预训练；在仿真和硬件在环（HITL）环境中验证，最终部署到真实四旋翼实现最高 9 m/s 飞行速度。
3. **关键结果**：MBRL方法可在纯像素输入下实现敏捷飞行，DreamerV3提供了从仿真到真实机器人研究的有前景路径；展示了MBRL在样本效率和零样本泛化上的优势。

## 💎 价值评估

- **🔬 研究价值**：首次将DreamerV3应用于无人机竞速视觉飞行控制，证明了MBRL世界模型在高频视觉运动控制任务中的可行性；为高样本效率的端到端无人机控制提供了新范式。
- **🚀 实践价值**：HITL硬件在环验证流程可直接迁移到其他旋翼无人机研究；最高9m/s的飞行速度接近入门级无人机竞速水平，具有实用价值。
- **📈 扩展潜力**：可结合更先进的世界模型（DreamerV4等）进一步提升性能；可扩展到室外非结构化环境；其框架可作为通用无人机视觉控制MBRL基准。

## 🎯 可落地实验点

**实验设计：基于DreamerV3的空中无人机目标追踪MBRL策略**

- 对比基线：本文DreamerV3方法 vs PPO（无模型基线） vs 纯IL预训练+RL微调
- 度量指标：
  - 任务成功率（穿过所有检查点）
  - 平均飞行速度（m/s）
  - 样本效率（达到相同性能所需的训练步数）
  - Sim2Real迁移后的性能保持率
- 预期结果：DreamerV3应显著优于PPO（样本效率），与IL基线成功率相当但样本效率更高
- 实验平台：IsaacGym仿真 + 真实四旋翼（HITL验证）

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。
> 字典真源：`06_知识Wiki/_views/概念关键词字典.md`
> 不确定时查字典别名表；字典外新概念写入 `06_知识Wiki/inbox.md`，不自行创建。

- [[强化学习]] - 本文核心训练框架：DreamerV3属于基于模型的RL方法
- [[空中视觉语言导航]] - 本文任务设定：视觉导航的无人机版本（无语言指令，但同属视觉导航范畴）

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作），通常 2-5 篇。

- [[2024-03_DreamerV3]] - DreamerV3: 本文使用的MBRL基础框架，基于世界模型的强化学习
- [[2022_Swift]] - Swift: 无人机竞速SOTA工作，本文主要对比的基线之一

## 📌 待探索问题

- **问题1**：DreamerV3训练的世界模型在遇到训练分布外的障碍物（如突然出现的气流、动态障碍物）时泛化能力如何？是否需要引入安全盾或备用安全策略？
- **问题2**：本文8页篇幅限制了消融实验的深度——DreamerV3的哪个组件（world model / policy / reward）对其成功贡献最大？世界模型和policy之间的更新频率如何调参？
- **问题3**：HITL设置使用渲染图像而非真实相机图像，这是否仍存在Sim2Real差距？该方法能否直接泛化到真实室内/室外非结构化环境？

---
**维护**: 花火 · 2026-05-09
