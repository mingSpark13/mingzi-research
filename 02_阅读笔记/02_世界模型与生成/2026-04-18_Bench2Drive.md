---
title: "Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving"
authors: Xiaosong Jia, Zhenjie Yang, Qifeng Li, Zhiyuan Zhang, Junchi Yan
arxiv: 2406.03877
date: 2024-06
conf: NeurIPS 2024 Datasets and Benchmarks Track
institution: 上海交通大学
keywords: [E2E autonomous driving, closed-loop benchmark, CARLA, multi-ability evaluation]
tags: [世界模型, VLA架构, 仿真平台, 跨载体泛化, 模仿学习]
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2406.03877.pdf
reading_date: 2026-04-18
reading_status: 已读
summary: "Bench2Drive 构建了 CARLA 闭环多能力自动驾驶评测基准，可用结构化场景与路线拆解模型能力短板。"
related_concepts: [世界模型, VLA架构, 仿真平台, 跨载体泛化, 模仿学习]
---

## 🎯 题目

Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving

## 📝 三句摘要

1. **问题背景**：此前 E2E 自动驾驶评测缺乏统一的闭环多能力评估体系，开环评测和单一长路线评测指标方差大，无法公平对比不同算法。
2. **核心方法**：Bench2Drive 是首个在 CARLA v2 中实现闭环、多能力综合评估的 E2E-AD 基准，覆盖 13638 个短场景片段、44 种交互场景、23 种天气、12 个城镇，提供 200 万帧全标注帧官方训练集和 220 条结构化评测路线。
3. **关键结果**：UniAD、VAD 等 SOTA E2E-AD 模型在 Bench2Drive 上全面评测，揭示了当前方法在交互场景下的核心瓶颈，为社区提供了透明的基线对比。

## 💎 价值评估

- **🔬 研究价值**：首个专门针对 E2E-AD 闭环多能力评测的基准，填补了仿真平台缺乏公平算法级对比的空白，对世界模型下游评测体系设计有重要参考意义。
- **🚀 实践价值**：多能力拆解评测框架（交互场景 × 天气 × 城镇）可直接迁移到无人机城市场景数据采集的评测体系设计中。
- **📈 扩展潜力**：主人 UE 数据采集可借鉴其结构化评测路线设计思路；Benchmark 的开闭环对比结论对仿真数据有效性评估有直接参考价值。

## 🎯 可落地实验点

**实验设计**：迁移 Bench2Drive 多能力拆解评测框架到无人机城市场景采集
- 评测维度：交互场景（人群/障碍物/多无人机）× 天气（晴/雨/雾/夜）× 城镇（高楼/街道/开阔地）× 任务类型（跟踪/导航/避障）
- 对比指标：感知精度、决策成功率、端到端延迟、跨场景泛化系数
- 预期结果：形成可量化的无人机感知-决策模型综合能力评测基准

## 🔗 知识图谱

- [[世界模型]] — Benchmark 的核心价值在于为世界模型提供可量化的下游评测标准
- [[VLA架构]] — E2E-AD 本质是一种 VLA 架构，端到端直接从感知预测控制输出
- [[仿真平台]] — CARLA v2 作为仿真平台，Bench2Drive 为其扩展了结构化评测框架
- [[跨载体泛化]] — 多城镇/多天气设定隐含跨载体泛化的场景多样性需求
- [[模仿学习]] — 训练数据来源于人类驾驶的模仿学习轨迹

## 🔗 相关链接

- [[2025-11_Alpamayo-R1]] - Alpamayo-R1：Chain of Causation 推理驾驶（本文同源对比方法）
- [[2025-10-01_LIBERO-Plus]] - LIBERO-Plus：VLA 鲁棒性分析（跨领域 benchmark 设计参考）

## 📌 待探索问题

- Bench2Drive 的短场景片段设计相比长路线评测有什么优势？如何确定最短有效场景长度以平衡评测效率与指标方差？
- 开环评测和闭环评测的 gap 有多大？这个 gap 对无人机仿真数据采集的策略有什么启示？

---
**维护**: 花火 · 2026-04-18（批量入库）
