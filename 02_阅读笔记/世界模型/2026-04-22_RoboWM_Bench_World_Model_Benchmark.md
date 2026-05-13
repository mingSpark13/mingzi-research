---
title: "RoboWM-Bench: Benchmark for Evaluating World Models in Robotic Manipulation"
authors: Feng Jiang, Yang Chen, Kyle Xu et al.
arxiv: 2604.19092
date: 2026-04-21
institution: （待补充）
conf: arXiv
keywords: ["world model benchmark", "robotic manipulation", "evaluation", "simulation"]
tags: [世界模型, 仿真平台, 任务与运动规划, 物理一致性]
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2604.19092_RoboWM_Bench.pdf"
reading_date: 2026-04-22
reading_status: 已读
related_concepts: ["世界模型", "仿真平台", "任务与运动规划", "物理一致性"]
---

# 📖 花火格式笔记

## 🎯 题目

RoboWM-Bench: Benchmark for Evaluating World Models in Robotic Manipulation

## 📝 三句摘要

1. **问题背景**：世界模型在机器人领域的评估缺乏统一标准，现有评测要么只关注视频生成质量，要么只关注最终任务成功率，缺乏对世界模型"未来预测 fidelity"的系统性评估。
2. **核心方法**：RoboWM-Bench 提出系统化基准测试，从未来预测保真度（预测 vs 真实状态误差）和策略泛化能力（不同任务/场景）两个维度评估世界模型，涵盖多种操控任务和干扰场景。
3. **关键结果**：评测了主流世界模型（Mask World Model、GAIA-1 等），揭示了当前世界模型在长程预测和物理一致性上的主要瓶颈，为未来研究指明方向。

## 💎 价值评估

- **🔬 研究价值**：可作为主人"高保真仿真数据飞轮"评估标准参考，为世界模型选型提供客观依据。
- **🚀 实践价值**：在选定世界模型用于主人无人机仿真数据合成前，可用 RoboWM-Bench 做快速筛选，避免盲目投入训练资源。
- **📈 扩展潜力**：基准框架可扩展到无人机场景，建立空中世界模型评测子基准。

## 🎯 可落地实验点

**实验设计**：用 RoboWM-Bench 评估 Mask World Model vs GAIA-1 在主人无人机仿真任务上的适用性
- 对比基线：GAIA-1（自动驾驶世界模型）、无世界模型基线
- 度量指标：长程预测 MSE、策略成功率、物理一致性评分
- 预期结果：Mask World Model 在旋翼无人机快速机动场景下预测保真度更高，物理一致性评分提升 20%

## 🔗 知识图谱

- [[世界模型]] - 评测对象核心概念
- [[仿真平台]] - 基准测试的仿真环境基础设施
- [[任务与运动规划]] - 评测任务涉及的运动规划能力
- [[物理一致性]] - 评测维度之一，世界模型必须符合物理规律

## 🔗 相关链接

- [[2026-04-22_Mask_World_Model]] - Mask World Model 是被评测方法之一，本文评测结果可作为方法选择依据
- [[2026-04-22_VLA_Foundry]] - VLA Foundry 可接入 RoboWM-Bench 做标准化评测

## 📌 待探索问题

- RoboWM-Bench 的操控任务如何扩展到无人机飞行场景（高速度、大空间跨度）？
- 世界模型评测中"物理一致性"指标如何量化定义，是否适用于空中机器人物理特性？

---
**维护**: 花火 · 2026-04-22
