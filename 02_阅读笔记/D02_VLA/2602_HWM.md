---
title: "H-WM: Hierarchical World Model for Embodied Agent Planning"
authors: Multiple
arxiv: 2602.11291
date: 2026-02
institution: various
conf: arXiv
keywords: Hierarchical World Model, Embodied Planning, Intent Representation, Cross-Body
tags: ["D02"]
domain: 世界模型
pdf_path: ../../01_论文库/具身智能/2602_HWM.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["PMI"]
---

## 🎯 题目

H-WM: Hierarchical World Model

## 📝 三句摘要

1. **问题背景**：现有 world model 通常是单层的，在跨躯体泛化和长时规划上能力不足。
2. **核心方法**：H-WM 提出 hierarchical world model，在高层维护抽象的 world state 用于规划和意图表示，在低层维护躯体相关的状态表示。
3. **关键结果**：验证了层级 world model 在长时任务规划和跨躯体迁移上的有效性。

## 💎 价值评估

- **🔬 研究价值**：H-WM 为主人的"意图层(world model)与执行层解耦"提供了层级 world model 的具体实现参考，是 PMI 高层设计的重要参照。
- **🚀 实践价值**：层级 WM 可直接作为 PMI 高层意图生成器的架构。
- **📈 扩展潜力**：H-WM 的高层表示 + PMI 的接口层 = 完整的层级意图 → 执行链路。

## 🎯 可落地实验点

**实验设计**：以 H-WM 为 PMI 高层意图生成器，在其下加入 PMI adapter
- 对比基线：单层 world model + PMI、端到端方法
- 度量指标：长时任务成功率、意图可迁移性、规划效率
- 预期结果：层级 WM + PMI 应优于单层方法

## 🔗 知识图谱

- [[世界模型]] - H-WM 是层级 world model 的代表
- [[具身智能]] - 跨躯体迁移是核心目标

## 📌 待探索问题

- H-WM 的高层表示是否有 formal 定义？与主人的 PMI Intention 定义如何对齐？
- 层级 WM 的高层和低层如何联合训练以保证一致性？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
