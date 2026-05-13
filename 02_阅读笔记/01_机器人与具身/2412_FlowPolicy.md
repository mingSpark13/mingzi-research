---
title: "FlowPolicy: Consistency Flow Matching for Fast Robot Manipulation"
authors: Multiple
arxiv: 2412.04987
date: 2024-12
institution: various
conf: arXiv
keywords: Flow Matching, Robot Manipulation, Fast Inference, Consistency Model
tags: ["D02", "流匹配", "灵巧操作"]
domain: 通用操作
pdf_path: ../../01_论文库/具身智能/2412_FlowPolicy.pdf
reading_date: 待补充
reading_status: 已读
summary: FlowPolicy 将 consistency flow matching 引入机器人操作策略学习，在保留生成式动作建模能力的同时显著加快推理。
related_concepts: ["流匹配", "灵巧操作"]
---

## 🎯 题目

FlowPolicy: Consistency Flow Matching for Fast Robot Manipulation

## 📝 三句摘要

1. **问题背景**：Diffusion Policy 多步去噪推理慢，难以满足实时控制需求；需要更快的生成式策略。
2. **核心方法**：将 consistency flow matching 引入机器人策略学习，实现单步或少数步推理即可输出动作序列，保持生成式策略的多峰动作建模能力。
3. **关键结果**：在多个 manipulation benchmark 上达到与 Diffusion Policy 相近的任务成功率，同时推理速度提升数倍。

## 💎 价值评估

- **🔬 研究价值**：明确了 flow matching 在具身操控中的定位——"保留 diffusion 优点的同时，大幅提升推理效率"。
- **🚀 实践价值**：单步推理能力使实时控制成为可能，适合高频精细操控。
- **📈 扩展潜力**：可与 VLA backbone 结合构建更快的 flow-matching VLA。

## 🎯 可落地实验点

**实验设计**：将 FlowPolicy 用于无人机精细操控，与 Diffusion Policy 和 MPC 做对比
- 对比基线：Diffusion Policy、MPPI、ReKep
- 度量指标：推理延迟（ms/step）、任务成功率、动作平滑性
- 预期结果：FlowPolicy 应在延迟上显著优于 diffusion，同时保持相近精度

## 🔗 知识图谱

- [[流匹配]] - FlowPolicy 是流匹配在具身操控的直接应用
- [[扩散策略]] - FlowPolicy 旨在替代 Diffusion Policy 的慢速多步去噪

## 📌 待探索问题

- Consistency model 的单步推理是否会影响多峰动作分布的建模能力？
- 在极复杂接触任务（如柔性体操作）上，flow matching 的表现与 diffusion 相比如何？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
