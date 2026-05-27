---
title: "Robot Learning from Human Videos: A Survey"
authors: Junyi Ma, Yuxuan Tian, Zhenyang Huang, et al.
arxiv: 2604.27621
date: 2026-04-30
institution: Tsinghua University, Shanghai AI Lab
conf: arXiv preprint
keywords: ["robot learning", "human videos", "imitation learning", "data scaling"]
tags: ["数据生成", "模仿学习", "VLA"]
summary: 机器人学习需要大量高质量演示数据，但机器人数据采集成本高、效率低，限制了数据规模，而人类视频数据丰富且易获取
domain: VLA
pdf_path: ../../01_论文库/VLA/2604.27621_RobotLearning_HumanVideos_Survey.pdf
reading_date: 2026-05-02
reading_status: 已读
related_concepts: ["数据生成", "模仿学习", "VLA"]
---
# 📖 花火格式笔记

## 🎯 题目

Robot Learning from Human Videos: A Survey

## 📝 三句摘要

1. **问题背景**：机器人学习需要大量高质量演示数据，但机器人数据采集成本高、效率低，限制了数据规模，而人类视频数据丰富且易获取
2. **核心方法**：综述从人类视频学习机器人技能的 Scaling 路径，涵盖视频理解、动作映射、跨域迁移、VLA 训练等关键技术
3. **关键结果**：系统梳理了人类视频数据的利用方式、关键挑战（embodiment gap、视角差异、动作标注）和未来方向，为数据飞轮提供了理论基础

## 💎 价值评估

- **🔬 研究价值**：首次系统梳理人类视频数据在机器人学习中的应用，明确了从视频理解到动作映射的完整技术链路，为数据 Scaling 提供了新思路
- **🚀 实践价值**：为构建机器人数据飞轮提供了低成本数据源（人类视频），可显著降低数据采集成本，提升数据规模和多样性
- **📈 扩展潜力**：可指导 UAV 操作数据飞轮的设计（人类操作视频 → UAV 操作数据），或用于 VLA 预训练（大规模人类视频 → 机器人微调）

## 🎯 可落地实验点

**实验设计**：human video pretraining for UAV manipulation VLA
- **对比基线**：
  - 纯机器人数据训练（小规模）
  - 人类视频预训练 + 机器人微调（本文方法）
  - 混合数据训练（人类视频 + 机器人数据）
- **度量指标**：
  - Task success rate（任务成功率）
  - Data efficiency（数据效率，达到相同性能所需数据量）
  - Generalization（泛化能力，新任务/新场景）
  - Embodiment gap（具身差距，人类动作 → 机器人动作的映射误差）
- **预期结果**：人类视频预训练显著提升数据效率和泛化能力，证明人类视频数据对 UAV 操作 VLA 的价值

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。

- [[数据生成]] - 本文核心方法类别
- [[模仿学习]] - 核心技术范式
- [[VLA架构]] - 应用领域

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作），通常 2-5 篇。

- [[2026-04-01_GigaWorld-Policy]] - VLA 数据 Scaling 代表作
- [[2026-04-20_CAPO_Cross-Embodiment]] - 跨具身数据利用代表作

## 📌 待探索问题

- 如何将人类操作视频（如手工操作、工具使用）映射到 UAV 操作动作（飞行 + 机械臂）？
- 人类视频数据的 embodiment gap 如何量化和缩小（视角差异、动作空间差异、物理约束差异）？
- 如何用人类视频数据预训练 UAV 操作 VLA，再用少量机器人数据微调（few-shot transfer）？
- 人类视频数据的标注策略（自动标注 vs 人工标注 vs 无标注学习）如何选择和优化？

---
**维护**: 花火 · 2026-05-02
