---
title: "ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment"
authors: Yuzhi Chen et al. (AMAP-CVLab)
arxiv: "https://arxiv.org/abs/2603.23376"
date: 2026-03-30
institution: 待补充
conf: 待补充
keywords: 待补充
tags: ["D02"]
domain: 通用操作
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["Sim2Real"]
---

## 🎯 题目

"ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment"

## 📝 三句摘要

1. ABot-PhysWorld 是一个 14B Diffusion Transformer 世界基础模型，生成物理合理、动作可控的机械臂操作视频。
2. 基于 300 万操作片段数据集，使用 DPO 后训练框架+解耦判别器抑制物理不合理行为（如物体穿透）。
3. 提出 EZSbench，首个训练无关的零样本 Embodied 基准，解耦评估物理合理性和动作对齐性。

## 💎 价值评估
**场景落地实验点**：ABot-PhysWorld 的物理对齐思路（DPO+判别器抑制物理违规）可用于训练无人机的世界模型，使其生成的未来状态满足空气动力学约束，而非只是视觉真实。对于 Sim2Real 无人机控制有直接价值。

**领域价值**：14B 规模的世界基础模型，物理对齐 + 跨载体控制，代表了世界模型在机械臂操作的最前沿进展。

## 🎯 可落地实验点
将 ABot-PhysWorld 的物理对齐训练范式迁移到无人机：用无人机飞控数据训练物理约束判别器，在世界模型训练中加入约束损失，使生成的四旋翼轨迹满足动力学约束。

## 🔗 知识图谱
- 关联：世界模型 / 扩散模型 / Sim2Real / 物理仿真


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
