---
title: 📖 MotionBERT — 统一人体运动表征学习
tags: []
summary: "MotionBERT 用统一时空表征预训练框架学习人体运动编码器，可迁移到 3D 姿态与跟踪等多任务。"
authors: 待补充
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
domain: 运动控制
pdf_path: 
reading_date: 2026-04-07
reading_status: 已读
related_concepts: ["6D位姿估计", "空中操作"]
---

## 🎯 题目
Learning Human Motion Representations: A Unified Perspective

## 📝 三句摘要
1. 提出统一的人体运动表征预训练框架，从大规模异质数据中学习运动编码器。
2. 预训练阶段从噪声 2D 观测恢复底层 3D 运动，融合几何/运动学/物理知识。
3. DSTformer 双流时空 Transformer 实现 SOTA 3D 姿态估计，简单微调即可迁移多任务。

## 💎 价值评估
- ⭐⭐⭐ 预训练运动编码器可直接微调用于人体跟随
- 统一表征 = 一套 backbone 做 3D pose + mesh recovery + action recognition
- ICCV 2023 | 代码：https://motionbert.github.io/

## 🔗 信息
- arXiv: 2210.06551 | ICCV 2023
- 在项目中的角色：**后端时序建模（与 PoseFormerV2 竞争选用）**

---
**维护**: 花火 · 2026-04-12


## 🎯 可落地实验点

**实验设计**：待补充
- 对比基线：待补充
- 度量指标：待补充
- 预期结果：待补充


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？


## 🔗 知识图谱
- [[6D位姿估计]]
- [[感知与3D视觉]]
- [[空中操作]]
