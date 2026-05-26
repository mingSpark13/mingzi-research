---

title: "OccAny: Generalized Unconstrained Urban 3D Occupancy"
authors: Anh-Quan Cao, Tuan-Hung Vu (Valeo AI)
arxiv: 2603.23502
date: 2026-03-24
institution: Valeo AI
conf: CVPR 2026
keywords: 待补充
tags: []
domain: 自动驾驶感知
pdf_path: ""
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["3D重建", "视频生成"]
---

## 🎯 题目

OccAny: Generalized Unconstrained Urban 3D Occupancy

## 📝 三句摘要

1. 现有 3D occupancy 方法依赖域内标注和精确传感器先验，在跨场景泛化上存在严重瓶颈。
2. OccAny 首次提出无约束城市 3D occupancy 模型，利用视觉几何 foundation model 的强泛化能力，在 out-of-domain 未标定场景中实现 occupancy 预测与几何补全。
3. 核心贡献：Segmentation Forcing + Novel View Rendering 管道，支持单目/环视/序列多种输入设置。

## 💎 价值评估

⭐⭐⭐⭐ 极高价值。CVPR 2026 acceptance，3D occupancy 是自动驾驶/机器人感知核心任务，OccAny 解决了一个关键痛点（泛化能力），且 code 已开源。直接利好 3DGS/自动驾驶场景理解方向。

## 🎯 可落地实验点

在无人机城市巡检场景中，用 OccAny 做 zero-shot 3D occupancy 预测，无需重新训练即可泛化到新城区，大幅降低数据标注成本。

## 🔗 相关链接

- Paper: https://arxiv.org/abs/2603.23502
- Project: https://valeoai.github.io/OccAny/
- Code: https://github.com/valeoai/OccAny

## 🔗 知识图谱

- [[感知与3D视觉]]
- [[3D重建]]
- [[视频生成]]


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
