---
title: "RL Token: Bootstrapping Online RL with Vision-Language-Action Models"
authors: Physical Intelligence (π) Team
arxiv: ""
date: 2025
institution: Physical Intelligence (π)
conf: pi.website technical report
keywords: [VLA, online RL, RL token, fine-tuning, manipulation, actor-critic, action chunking]
tags: [具身智能, 强化学习, VLA架构]
domain: 具身智能
pdf_path: "../../01_论文库/具身智能/RLT_RLToken_pi.pdf"
reading_date: 2026-04-24
reading_status: 已读
---

# 📖 RL Token (RLT)：冻结大模型，用小 RL 头精调 VLA

## 🎯 题目

RL Token: Bootstrapping Online RL with Vision-Language-Action Models

## 📝 三句摘要

1. **问题背景**：预训练 VLA 模型在任务的"粗粒度"阶段表现良好，但在需要高精度的关键阶段（如螺丝插入、以太网接口对准）成功率低，而对整个大模型做在线 RL 微调计算代价极高且不实用。
2. **核心方法**：在冻结 VLA 的基础上，通过少量 demo 数据训练 VLA 暴露一个紧凑的"RL Token"（在 Transformer 最终层 embedding 后附加一个特殊 `<rl>` token），再用这个 token 训练一个轻量 actor-critic 头做在线 RL，actor 同时接收 RL Token 和 VLA 的参考动作 chunk（Pass-Through），用 BC 正则化锚定策略不偏离 VLA 太远。
3. **关键结果**：仅需 5 分钟真实机器人数据即可在关键精度阶段超越 base VLA，15 分钟内完成整体任务提升；在以太网插入等高精度任务上成功率匹配 base policy 同时步数减少 2×，不修改 VLA 任何参数。

## 💎 价值评估

- **🔬 研究价值**：提出了"冻结大模型 + 轻量 RL 接口"的精调范式，将 VLA 的在线 RL 微调从"全模型更新"降级为"小头更新"，解决了大模型在线 RL 的计算瓶颈；RL Token 作为 VLA 内部表示的压缩接口，是一种通用的 VLA-RL 桥接设计。
- **🚀 实践价值**：可在机器人本体上实时运行（无需离线训练集群），15 分钟数据即可显著提升精度，对工业精密操作（插接件、螺丝、精密装配）有直接落地价值。
- **📈 扩展潜力**：RL Token 机制可推广到任意 Transformer-based VLA；与 RLHF/RLAIF 结合可实现人类反馈驱动的精度提升；可探索多任务 RL Token 共享以提升泛化。

## 🎯 可落地实验点

**实验设计**：在 UAV 精密对接任务中验证 RL Token 范式
- 用预训练 VLA（如 π0）作为 base policy 处理粗粒度导航，RL Token 头专注对接最后 10cm 的精密控制
- 对比基线：base VLA 直接推理 / 全模型 RL 微调 / RLT（本文方法）
- 度量指标：对接成功率、对接精度（mm）、所需真实数据量（分钟）
- 预期结果：RLT 用 <30 分钟数据达到全模型微调的精度，计算开销降低 10× 以上

## 🔗 知识图谱

- [[VLA架构]] - RLT 以 VLA 为 base policy，RL Token 是 VLA 的 RL 接口
- [[强化学习]] - 核心训练范式，在线 actor-critic RL
- [[模仿学习]] - BC 正则化锚定策略，防止 RL 偏离 VLA 先验

## 🔗 相关链接

- [[2024_pi0]] - π0: Physical Intelligence 的基础 VLA，RLT 的 base policy
- [[2024_DSRL]] - DSRL: 强约束 VLA 的 RL 方法，本文对比基线之一
- [[2024_DAgger]] - DAgger: 模仿学习对比基线，受限于人类演示速度

## 📌 待探索问题

- RL Token 的维度选择（压缩比）如何影响 RL 学习效率？过度压缩是否会丢失精度相关的关键信息？
- 当任务切换时（如从螺丝插入换到以太网插入），RL Token 是否需要重新训练，还是可以跨任务迁移？
