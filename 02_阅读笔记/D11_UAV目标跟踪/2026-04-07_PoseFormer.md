---
title: 📖 PoseFormer — 纯 Transformer 3D 人体姿态估计
authors: 待补充
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
tags: []
domain: 运动控制
pdf_path: 
reading_date: 2026-04-07
reading_status: 已读
related_concepts: ["6D位姿估计", "空中操作"]
---

## 🎯 题目
3D Human Pose Estimation with Spatial and Temporal Transformers

## 📝 三句摘要
1. 首次提出纯 Transformer（无 CNN）的 3D 人体姿态估计方法。
2. 设计空间-时间 Transformer 结构，建模帧内关节关系 + 跨帧时序关联。
3. 在 Human3.6M 和 MPI-INF-3DHP 上达到 SOTA。

## 💎 价值评估
- ⭐⭐⭐ 姿态序列 Transformer 的开山之作
- 作为"优先级 1 升级版"的基础参考：关键点序列 → PoseFormer → 预测人体状态
- **代码开源**：https://github.com/zczcwh/PoseFormer

## 🔗 信息
- arXiv: 2103.10455 | ICCV 2021
- 在项目中的角色：**后端时序建模（升级版）**

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
