---
title: "WildWorld: Large-Scale Dataset for Dynamic World Modeling with Actions"
authors: Zhen Li, Zian Meng et al. (Shanda AI / 多校)
arxiv: 2603.23497
date: 2026-03-24
institution: Shanda AI 等
conf: arXiv (cs.CV)
keywords: 待补充
tags: ["D01"]
domain: 世界模型
pdf_path: ""
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["强化学习"]
---

## 🎯 题目

"WildWorld: Large-Scale Dataset for Dynamic World Modeling with Actions"

## 📝 三句摘要

1. WildWorld 是从 Monster Hunter: Wilds 自动采集的超大规模 action-conditioned world modeling 数据集，包含 1.08 亿帧、450+ 动作类型，带骨骼/状态/深度图等精细标注。
2. 解决了现有 world model 数据集动作语义匮乏、与视觉变化强耦合的问题，使模型能学习到解耦的结构化世界动态。
3. 配套 WildBench 基准，从 Action Following 和 State Alignment 两个维度评估模型。

## 💎 价值评估

⭐⭐⭐⭐⭐ 极高价值。数据规模罕见（108M 帧），动作空间丰富，标注完整（骨骼+状态+深度），是 world model + RL 联合训练的潜力数据集。对主人 world model 学习路线高度相关。

## 🎯 可落地实验点

使用 WildWorld 预训练一个 action-conditioned video prediction model，迁移到无人机仿真环境，验证物理动态一致性和动作响应性。

## 🔗 相关链接

- Paper: https://arxiv.org/abs/2603.23497
- Project: https://shandaai.github.io/wildworld-project/

## 🔗 知识图谱

- [[世界模型]]
- [[强化学习]]
- [[具身智能]]


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
