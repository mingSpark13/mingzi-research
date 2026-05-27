---
title: "PhyWorldBench: A Physics Consistency Benchmark for World Models"
authors: Multiple (from arXiv 2507.13428)
arxiv: 2507.13428
date: 2025-07-28
institution: 估计为世界模型/具身智能评估方向
conf: arXiv
keywords: World Model Benchmark, Physics Consistency, Evaluation, Embodied AI
tags: ["D01", "具身智能"]
summary: "PhyWorldBench 以物理一致性而非纯视频质量为核心，系统评估世界模型是否真正遵守重力、接触与动力学规律。"
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2507_PhyWorldBench.pdf
reading_date: 2026-03-26
reading_status: 已读
related_concepts: ["物理一致性", "视频生成"]
---

## 🎯 题目

PhyWorldBench: A Physics Consistency Benchmark for World Models

## 📝 三句摘要

1. **问题背景**：现有视频质量指标（FVD、PSNR、LPIPS）和通用的 World Model 基准不足以评估"生成的视频是否符合物理定律"，导致大量视频生成模型被错误地当作 world model 评估。
2. **核心方法**：PhyWorldBench 以"物理规律遵守程度"为核心评估维度，构建了覆盖刚体动力学、关节运动、液体/柔性体、粒子系统等物理现象的测试集，并设计了专门的物理一致性评分（Physical Consistency Score）。
3. **关键结果**：主流视频生成模型在 PhyWorldBench 上暴露了大量物理违规（如物体悬空、违反重力），证明了"视频质量好 ≠ 世界建模能力强"，本文为 world model 评估提供了新标准。

## 💎 价值评估

- **🔬 研究价值**：首次以"物理一致性"为核心基准，直接点明了视频生成模型与真正的 world model 之间的本质差距，是该方向的里程碑评测工作。
- **🚀 实践价值**：为研究者提供了统一的物理一致性评测标准，可直接指导具身 world model 的发展方向。
- **📈 扩展潜力**：PhyWorldBench 的评估维度和指标设计可扩展到具身操控 world model 的专项评估。

## 🎯 可落地实验点

**实验设计**：使用 PhyWorldBench 评估主人研究方向的 world model 基线（DreamerV3、Phys4D）的物理一致性
- 对比基线：当前主流 world model 和视频生成模型
- 度量指标：Physical Consistency Score、重力违规率、接触违规率、时间连续性
- 预期结果：Action-conditioned world model 应在物理一致性上优于纯视频生成模型

## 🔗 知识图谱

- [[世界模型]] - 本文直接评估的对象
- [[物理一致性]] - 本文核心评估维度
- PhyWorldBench（本文） - PhyWorldBench 本身就是一个评估基准

## 🔗 相关链接

- [[2026-03-09_Phys4D]] - Phys4D 试图解决物理一致性问题，PhyWorldBench 是其评估标准
- [[2026-03-10_InteractiveWorldSimulator]] - Interactive World Simulator 的 action conditioning 是提高物理一致性的方法之一
- [[2025-02-25_InSpatioWorld]] - InSpatio-World 生成的视频应在 PhyWorldBench 上接受物理一致性检验

## 📌 待探索问题

- PhyWorldBench 的物理一致性指标是否可以与具身操控的任务成功率（如抓取成功率）建立关联？还是两者存在 trade-off？
- 物理违规的权重如何设计？不同应用场景（机器人操控 vs 电影制作）对物理违规的容忍度不同，benchmark 如何反映这个差异？

---
**维护**: 花火 · 2026-04-12
