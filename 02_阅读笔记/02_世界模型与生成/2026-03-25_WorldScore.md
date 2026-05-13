---
title: "WorldScore: A Unified Evaluation Benchmark for World Generation"
authors: （待补充）
arxiv: 2504.00983
date: 2025-04-01
institution: Stanford University 等
conf: arXiv
keywords: WorldScore, World Generation, Evaluation Benchmark, 4D World Model
tags: ["D01"]
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2025_WorldScore.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["视频生成"]
---

## 🎯 题目
WorldScore: A Unified Evaluation Benchmark for World Generation

## 📝 三句摘要
1. WorldScore 提出统一 benchmark，用于比较 3D、4D 与视频世界生成模型在 controllability、quality、dynamics 等维度的表现。
2. 它反映出社区评价目标已经从单纯“像视频”转向“像世界”。
3. 对 InSpatio-World 来说，WorldScore 是其“persistent world state”叙事背后的评价背景。

## 💎 价值评估
- **🔬 研究价值**：把 world generation 从视觉任务扩展为系统性评测对象。
- **🚀 实践价值**：为主人后续做 related work 和方法评价提供统一标准框架。
- **📈 扩展潜力**：可作为几何模型、视频模型和世界模型融合路线的公共评测基准。

## 🎯 可落地实验点
**实验设计**：对比 InSpatio-World、ReCamMaster、GCD 在 WorldScore 维度上的潜在差异，手工构建小型评估表。

## 🔗 知识图谱
- [[世界模型]] - 直接服务于世界生成与状态保持评价
- [[感知与3D视觉]] - 关注空间、时间与控制能力的统一评估
- [[视频生成]] - 世界一致性评价的重要组成部分

## 🔗 相关链接
- [[2026-03-19_InSpatio_WorldFM]] - 处在 world generation 叙事前沿的代表系统
- [[2026-03-25_ReCamMaster]] - 可作为 benchmark 中的 camera-controlled 参照系
- [[2026-03-25_Self_Forcing]] - 长时稳定与 rollout 能力可映射到 benchmark 维度

## 📌 待探索问题
- WorldScore 是否足以覆盖机器人/具身智能中的世界模型需求？
- 几何正确与视频真实感在 benchmark 中应如何平衡权重？
nchmark 中应如何平衡权重？

---
**维护**: 花火 · 2026-04-12
