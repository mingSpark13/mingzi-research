---
title: "Latent Action Diffusion for Cross-Embodiment Manipulation"
authors: Multiple
arxiv: 2506.14608
date: 2025-06
institution: various
conf: arXiv
keywords: Latent Action, Cross-Embodiment, Diffusion Model, Embodiment-Agnostic, Manipulation
tags: ["D02", "跨载体泛化", "灵巧操作"]
domain: 具身智能
pdf_path: ../../01_论文库/具身智能/2506_LatentActionDiffusion.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["跨载体泛化", "灵巧操作"]
---

## 🎯 题目

Latent Action Diffusion for Cross-Embodiment Manipulation

## 📝 三句摘要

1. **问题背景**：不同 robot embodiment 的动作空间差异大，无法直接迁移策略，需要在动作空间之上建立统一的抽象表示。
2. **核心方法**：提出 latent action space = embodiment-agnostic 的共享潜在动作表征，decoder 将 latent action 映射到各 embodiment 特定的执行动作，实现跨躯体迁移。
3. **关键结果**：在多种 robot embodiment 上验证了 latent action diffusion 的跨躯体策略迁移有效性。

## 💎 价值评估

- **🔬 研究价值**：Latent Action Diffusion 是"跨躯体潜在动作空间"的近邻工作，与主人的 body-state latent 方向（B2）直接对应。
- **🚀 实践价值**：为跨 embodiment 的身体使用状态统一表征提供了参考方法。
- **📈 扩展潜力**：本框架可在其基础上，把 latent 从"动作语义对齐"扩展到"身体使用状态对齐"。

## 🎯 可落地实验点

**实验设计**：以 latent action diffusion 为 baseline，将其扩展为"intent + body-state"双latent
- 对比基线：单 latent action diffusion（无身体使用状态）
- 度量指标：跨 embodiment 任务成功率、身体使用参数迁移率
- 预期结果：双 latent 应在身体状态变化时保持更高的意图一致性

## 🔗 知识图谱

- [[具身智能]] - 跨躯体迁移是具身智能的核心挑战
- [[扩散策略]] - latent action diffusion 基于 diffusion model

## 📌 待探索问题

- latent action 的语义粒度如何设计？太细则失去跨躯体泛化能力，太粗则无法表达精细操控差异？
- 本框架的"身体使用状态"latent 与"动作语义"latent 如何联合训练？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
