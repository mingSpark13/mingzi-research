---
title: "Embedding Robot Morphology into Transformer-Based Policies"
authors: Multiple
arxiv: 2603.00182
date: 2026-03
institution: various
conf: arXiv
keywords: Morphology Embedding, Body Schema, Transformer, Cross-Embodiment, Latent Representation
tags: ["D02", "VLA架构", "跨载体泛化"]
domain: 具身智能
pdf_path: ../../01_论文库/具身智能/2603_MorphologyEmbedding.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["VLA架构", "跨载体泛化"]
---

## 🎯 题目

Embedding Robot Morphology into Transformer-Based Policies

## 📝 三句摘要

1. **问题背景**：Transformer-based robot policies 难以显式感知 robot kinematic structure，换躯体时需要完整重训练或大量微调。
2. **核心方法**：将 robot morphology 显式嵌入 transformer 模型，让模型感知躯体结构，实现跨躯体迁移。
3. **关键结果**：在多种 robot embodiment 上验证了 morphology embedding 可显著提升跨躯体迁移能力，同时保持任务性能。

## 💎 价值评估

- **🔬 研究价值**：morphology embedding 是 PMI 框架中"body schema encoding"模块的重要技术基础，直接支持 PMI 的 cross-embodiment 目标。
- **🚀 实践价值**：为 PMI 的 body schema 表示提供了可参考的 embedding 方法。
- **📈 扩展潜力**：morphology embedding + PMI 接口 = 完整的躯体感知与迁移方案。

## 🎯 可落地实验点

**实验设计**：将 morphology embedding 集成到 PMI 的 body schema 模块
- 对比基线：无 morphology embedding 的 PMI、CEI
- 度量指标：跨 embodiment 任务成功率、躯体适配数据量
- 预期结果：morphology embedding 应显著减少新躯体的适配数据量

## 🔗 知识图谱

- [[具身智能]] - morphology 是跨躯体泛化的核心信息
- [[Sim2Real]] - morphology embedding 提升 Sim2Real 迁移

## 📌 待探索问题

- Morphology embedding 是学习的还是手工设计的？如果是学习的，如何保证新躯体的泛化？
- PMI 的 body schema encoding 与 morphology embedding 的关系是什么？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
