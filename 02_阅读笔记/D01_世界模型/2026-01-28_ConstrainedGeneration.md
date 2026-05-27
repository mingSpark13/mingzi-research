---
title: 'Constrained Generation: From Language Models to Hard-Constraint Satisfaction'
authors: Multiple (from arXiv 2601.07525)
arxiv: 2601.07525
date: 2026-01-28
institution: 估计为大模型/控制理论方向
conf: arXiv
keywords: Constrained Decoding, Control Barrier, Hard Constraints, LLM Generation
tags:
- 物理一致性
- 动作条件预测
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2601_ConstrainedGeneration.pdf
reading_date: 2026-03-26
reading_status: 已读
related_concepts:
- 物理一致性
- 动作条件预测
summary: 这篇综述把 constrained decoding、barrier guidance 与投影采样统一到“硬约束生成”框架下，强调只有把约束嵌入生成过程才能真正保证可行性。
---
## 🎯 题目

Constrained Generation: From Language Models to Hard-Constraint Satisfaction

## 📝 三句摘要

1. **问题背景**：大模型生成中，软约束（loss penalty、physics-informed bias）只能"更像"约束，无法保证输出落在约束集合内，实际系统需要硬约束保证时，现有方法不足。
2. **核心方法**：综述+提出多种约束生成方法：constrained decoding（解码时mask非法token）、control barrier guidance（采样时用barrier引导）、hard-constrained flow sampling（流匹配中嵌入硬约束）、projection-based constrained sampling（生成后投影到可行集）。
3. **关键结果**：明确区分了"软约束近似"与"硬约束保证"的本质差异，指出只有将约束直接嵌入生成参数化/采样/投影过程，才能谈"保证约束满足"。

## 💎 价值评估

- **🔬 研究价值**：是约束生成领域的系统性综述，明确了"尽力逼近"与"严格保证"的边界，是具身world model物理一致性研究的方法论基础。
- **🚀 实践价值**：为需要硬约束保证的机器人控制提供了将约束嵌入生成的完整路线图。
- **📈 扩展潜力**：可与diffusion/flow matching结合，构建physics-constrained机器人世界模型生成器。

## 🎯 可落地实验点

**实验设计**：将constrained decoding思路引入无人机控制生成，将安全区域约束直接嵌入生成token空间
- 对比基线：physics-informed loss、unconstrained generation
- 度量指标：约束满足率、任务成功率、生成质量（FVD）
- 预期结果：硬约束方法应在约束满足率上显著优于软约束方法

## 🔗 知识图谱

- [[世界模型]] - 约束生成是world model物理保证的核心技术
- [[物理一致性]] - 硬约束vs软约束的区分直接影响物理一致性保证能力
- [[动作条件预测]] - 约束生成可与action-conditioned结合

## 🔗 相关链接

- [[2025-06-17_PCFM]] - PCFM将硬约束注入flow matching采样过程
- [[2025-04-23_SafeFlow]] - SafeFlow用control barrier引导采样，保证安全约束
- [[2026-03-10_InteractiveWorldSimulator]] - 具身world model可受益于本文的约束注入框架

## 📌 待探索问题

- 硬约束方法在复杂非线性约束（如多体接触约束）上的可扩展性如何？
- 约束越硬，生成质量下降的trade-off如何在具身场景中平衡？

---
**维护**: 花火 · 2026-04-12
