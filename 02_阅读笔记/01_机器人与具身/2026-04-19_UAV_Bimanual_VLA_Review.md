---
title: Vision-Language-Action Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review
authors: Unknown
arxiv: ""
date: 2026-04
institution: Unknown
conf: Preprints.org
keywords: [UAV, Bimanual Manipulation, Vision-Language-Action, Review, Robotics]
tags: ["VLA架构", "空中操作", "多模态统一架构", "ACT动作分块", "扩散策略"]
domain: 空中操作
pdf_path: ""
reading_date: 2026-04-19
reading_status: 待读
related_concepts: ["VLA架构", "空中操作", "多模态统一架构", "ACT动作分块", "扩散策略"]
---

## 🎯 题目

Vision-Language-Action Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review

## 📝 三句摘要

1. **问题背景**：无人机与双手机器人都属于高自由度、强时空耦合平台，但现有 VLA 综述大多偏单臂 manipulation，缺少对 UAV 与 bimanual 这两类复杂 embodiment 的并行梳理。
2. **核心方法**：该综述聚焦 VLA 在无人机机器人与双手机器人上的代表架构、数据来源、动作表示与训练策略，对 AR、action chunking、diffusion、flow matching 等路线做横向对比。
3. **关键结果**：它的最大价值不是提出新算法，而是把“复杂 embodiment 下 VLA 为什么更难、难在哪里、现有解法如何取舍”整理出来，特别适合给主人做 UAV VLA related work 和选型参考。

## 💎 价值评估

- **🔬 研究价值**：这篇综述刚好踩中主人的两个高相关轴：UAV + 高维动作控制。它能帮主人快速看到 manipulation-centric VLA 之外，更贴近自身研究场景的共性难题。
- **🚀 实践价值**：如果主人要做 UAV instruction following、空中抓取、视觉语言导航或跟踪控制，这篇可以直接拿来当“架构与动作表示的选型表”。
- **📈 扩展潜力**：后续可以以它为入口，进一步拆成“无人机 VLA / 双臂 VLA / world-model-enhanced VLA / cross-embodiment policy”四条子线去补精读。

## 🎯 可落地实验点

**实验设计**：基于综述对主人场景做动作表示路线对比
- 对比基线：自回归动作生成 / ACT 动作分块 / diffusion policy / flow matching action model
- 度量指标：控制频率、任务成功率、长程误差累积、训练稳定性、推理时延
- 预期结果：对于无人机这类实时性更强的平台，ACT 或 flow matching 可能比纯自回归更适合作为落地起点

## 🔗 知识图谱

- [[concepts/VLA架构]] - 综述核心主线
- [[concepts/空中操作]] - 无人机相关 embodied 任务的重要分支
- [[concepts/多模态统一架构]] - 视觉、语言、动作统一建模
- [[concepts/ACT动作分块]] - 高频动作生成的重要范式
- [[concepts/扩散策略]] - 高维动作生成的主流路线之一

## 🔗 相关链接

- [[2026-03-27_RT-2]] - VLA 基础代表作
- [[2026-03-27_OpenVLA]] - 开源 VLA 架构参考
- [[2026-04-19_VLA_Survey_Embodied_AI]] - 更广义的 VLA 综述，可与本文形成总览 + 专题互补

## 📌 待探索问题

- UAV 场景的控制频率、安全约束、视角变化都强于桌面 manipulation，现有 manipulation-centric VLA 组件哪些能直接迁，哪些必须重做？
- 双臂与无人机虽然 embodiment 不同，但是否能共用统一动作接口或共享一部分策略 backbone？

---
**维护**: 花火 · 2026-04-19
