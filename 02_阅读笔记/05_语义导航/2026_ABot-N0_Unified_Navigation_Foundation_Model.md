---
title: "ABot-N0: Unified Navigation Foundation Model with LLM Brain and Flow Matching Action Expert"
authors: ""
arxiv: ""
date: 2026-02
institution: 阿里巴巴地图CV实验室
conf: ""
keywords: foundation model, unified navigation, point-goal, object-goal, instruction-following, LLM cognitive brain, flow matching
tags: ["D06", "流匹配"]
summary: "ABot-N0 用 LLM 认知脑 + Flow Matching 动作专家统一五类导航任务，在 7 个 benchmark 上达到接近 foundation model 路线的导航 SOTA。"
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["流匹配"]
---

## 🎯 题目

ABot-N0: 统一导航基础模型（LLM认知脑 + 流匹配动作专家）

## 📝 三句摘要

1. **问题背景**：现有导航方法多为单任务设计，Point-goal、Object-goal、Instruction-following、POI-goal、Person-following 各需不同模型，系统复杂难以统一部署。
2. **核心方法**：提出 LLM Cognitive Brain + Flow Matching Action Expert 架构，16.9M expert trajectories + 5.0M reasoning samples + 7802 scenes 训练，在 7 个 benchmark 上达新 SOTA。
3. **关键结果**：五类任务统一，在多个基准上实现 SOTA，是目前最接近 foundation model 路线的导航系统。

## 💎 价值评估

- **🔬 研究价值**：首次将 LLM cognitive brain 和 flow matching action 统一到单一 foundation model，是具身导航基础模型化的重要里程碑。
- **🚀 实践价值**：一个模型覆盖多种导航范式，降低多任务系统复杂度；Brain-Action 分层架构与主人"高层语义决策 + 低层控制器"设想高度一致。
- **📈 扩展潜力**：该架构可作为高层推理引擎，下接无人机/四足控制栈，实现多模态任务统一执行。

## 🎯 可落地实验点

**实验设计**：以 ABot-N0 作为高层语义决策头，接入四足/无人机低层 MPC，构建端到端语义导航系统
- 对比基线：VLFM + 底层控制器（拼接方案）
- 度量指标：Task Success Rate、End-to-End Latency、跨任务迁移能力
- 预期结果：统一模型在多任务场景下 SR 提升 >15%，系统复杂度降低 50%

## 🔗 知识图谱
- [[基础模型]]
- [[流匹配]]
- [[LLM认知架构]]
- [[多任务统一]]
- [[具身智能]]

## 🔗 相关链接

- [[2025_Nav-R2_RGB_Only_Navigation]] - Nav-R2 同年工作，同样关注高层语义决策
- [[2025_NaVILA_Two-Level_VLA_Navigation]] - NaVILA 的两层架构与 ABot-N0 的 Brain-Action 分层思想相似

## 📌 待探索问题

- 16.9M trajectories 训练成本极高，中小团队如何复现或迁移？是否有轻量化微调方案？
- flow matching action expert 在高频控制（>50Hz）场景下是否依然稳定？

---
**维护**: 花火 · 2026-04-12
