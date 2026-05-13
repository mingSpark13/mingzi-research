---
title: "Flow Matching: Conditional Generative Modeling via Continuous Normalizing Flows"
authors: Lipman et al.
arxiv: 2210.02747
date: 2022-10
institution: various
conf: NeurIPS 2022
keywords: Flow Matching, CNF, Continuous Normalizing Flows, Generative Model
tags: ["流匹配"]
domain: 学习范式
pdf_path: ../../01_论文库/具身智能/2210_FlowMatching.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["流匹配"]
---

## 🎯 题目

Flow Matching: Conditional Generative Modeling via Continuous Normalizing Flows

## 📝 三句摘要

1. **问题背景**：标准 diffusion models 需要复杂的中间扩散步骤，训练和采样效率受限；需要一个更直接的连续路径建模方法。
2. **核心方法**：Flow matching 直接学习从噪声分布到数据分布的连续速度场/向量场（CNF），不依赖仿真步数，允许用更简单甚至接近直线的概率路径。
3. **关键结果**：提出 simulation-free 训练范式，证明了 diffusion path 是 flow matching 的特例，同时 flow matching 可实现更高效率的采样。

## 💎 价值评估

- **🔬 研究价值**：Flow matching 是 diffusion 的理论扩展，提供了一个更统一的连续生成模型框架，是生成式机器人策略的新范式基础。
- **🚀 实践价值**：训练和采样效率优于标准 diffusion，适合需要快速推理的机器人控制。
- **📈 扩展潜力**：FlowPolicy (2412) 是其在机器人策略上的直接应用；π0 是 flow matching + VLA 的结合。

## 🎯 可落地实验点

**实验设计**：用 flow matching 替代 diffusion 作为动作生成器，构建更快的具身 policy
- 对比基线：Diffusion Policy (DDPM)、标准 autoregressive policy
- 度量指标：推理速度（steps）、任务成功率、动作平滑性
- 预期结果：flow matching 应在推理速度上显著优于 diffusion，同时保持相近的任务成功率

## 🔗 知识图谱

- [[流匹配]] - Flow matching 是流匹配方法的理论奠基
- [[扩散策略]] - diffusion 是 flow matching 的特例，flow matching 效率更高

## 📌 待探索问题

- Flow matching 在高度非线性动作空间（如多指灵巧手）上的收敛性如何？
- 与 world model 的 action-conditioned rollout 如何结合？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
