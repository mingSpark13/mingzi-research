---
title: "R3D: Revisiting 3D Policy Learning"
authors: Multiple (from arXiv 2604.15281)
arxiv: 2604.15281
date: 2026-04-19
institution: 3D Policy Learning / Manipulation
conf: arXiv
keywords: [3D Policy Learning, Manipulation, Diffusion, Cross-Embodiment]
domain: 机器人灵巧操作
pdf_path: ../../01_论文库/2604.15281.pdf
reading_date: 2026-04-19
reading_status: 已读
tags: ["D02", "3D策略学习", "灵巧操作", "扩散策略"]
summary: "3D策略学习在跨实体迁移和泛化方面具有优势，但训练不稳定和严重过拟合阻碍了其发展。"
related_concepts: ["3D策略学习", "扩散策略", "灵巧操作", "Sim2Real"]
---

## 🎯 题目

R3D: Revisiting 3D Policy Learning

## 📝 三句摘要

1. **问题背景**：3D策略学习承诺更强的泛化能力和跨实体迁移能力，但训练不稳定和严重过拟合问题阻碍了其发展，阻止了强大3D感知模型的采用。
2. **核心方法**：R3D系统诊断发现Batch Normalization的负面影响和3D数据增强的缺失是主要原因；提出结合可扩展的Transformer 3D编码器和扩散解码器的架构，专为大规模稳定性设计。
3. **关键结果**：在多个挑战性操作基准上显著超越state-of-the-art的3D基线，为可扩展的3D模仿学习建立了新的稳健基础。

## 💎 价值评估

- **🔬 研究价值**：首次系统诊断3D策略学习的训练不稳定问题，提出BN和数据增强两个关键修复点，对领域有重要方法论贡献。
- **🚀 实践价值**：架构设计稳定可扩展，适合真实机器人的精细操作场景；项目主页已公开。
- **📈 扩展潜力**：可与无人机精准放置任务结合，用3D感知替代2D像素策略。

## 🎯 可落地实验点

**实验设计**：将R3D的3D encoder + diffusion decoder架构引入无人机精准操作任务
- 对比基线：2D CNN策略、纯diffusion policy无3D encoder
- 度量指标：任务成功率、操作精度、跨场景泛化率
- 预期结果：3D表示应在精准操作任务上显著优于2D像素策略

## 🔗 知识图谱

- [[灵巧操作]] - 3D策略学习是本文的核心应用场景
- [[扩散策略]] - diffusion decoder是策略输出的核心机制
- [[Sim2Real]] - 跨实体迁移是3D策略的核心承诺

## 🔗 相关链接

- [[2024-09-24_ReKep]] - ReKep探索了关系关键点约束，与3D表示学习互补
- [[2026-04-19_HiST-AT]] - HiST-AT探索了动作tokenizer层次化表示，与R3D的表示学习思想相关

## 📌 待探索问题

- R3D 对 Batch Normalization 的负面结论是否依赖具体数据规模与传感器模态，迁到空中平台后会不会变化？
- 3D encoder + diffusion decoder 的组合在低纹理、稀疏深度或强视角变化场景下，泛化收益是否仍显著？
