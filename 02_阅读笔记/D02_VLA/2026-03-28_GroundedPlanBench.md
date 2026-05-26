---
title: "Spatially Grounded Long-Horizon Task Planning in the Wild"
authors: "（待补充）"
arxiv: 待补充
date: 2026-03-28
institution: 待补充
conf: 待补充
keywords: 待补充
tags: ["D02"]
domain: 通用操作
pdf_path: ""
reading_date: 2026-03-28
reading_status: 已读
summary: "评估 VLM 长程任务规划中空间接地能力的基准与自动数据生成框架"
related_concepts: ["长程任务规划", "空中操作", "强化学习", "VLA架构", "灵巧操作"]
---

## 🎯 题目

"Spatially Grounded Long-Horizon Task Planning in the Wild"

## 📝 三句摘要

1. 当前VLM做任务规划时，缺少对"精确空间位置"（在哪里操作）的评估，导致生成的规划在几何上不可执行。
2. 提出GroundedPlanBench基准，评估VLM的分层子动作规划和空间接地（spatial grounding）能力。
3. V2GP框架利用真实机器人视频演示自动生成空间接地规划数据，在基准和真实机器人实验上验证了效果。

## 💎 价值评估

**为什么有价值**：空中机械臂操作同样需要精确的空间接地（末端执行器应该去哪里）。VLM规划缺乏几何精确性是空中和地面操作的共同瓶颈。

**与Paper A的关系**：
- Paper A中层「意图解析器」的核心任务 = 将语义意图转换为几何可执行的操作
- GroundedPlanBench验证了这一需求是当前VLA的共同瓶颈
- V2GP的自动数据生成框架可用于创建Paper A所需的训练数据

**核心创新**：首次系统性地评估VLM的空间接地能力，并提出自动化数据生成方法。

## 🎯 可落地实验点

Paper A的「V2GP自动数据生成」可借鉴：
1. 利用主人已有的机器人视频演示，自动生成「VLM意图 + 空间接地」配对数据
2. 解决Paper A训练数据稀缺问题
3. 空间接地标注可以直接用于中层解析器的监督训练

「可落地实验点」

## 🔗 知识图谱
- 父主题：[[03_空地迁移/README]]
- 相关论文：[[2026-03-28_Aerial-Manipulator-RL.md]]（空中机械臂控制）
- 相关论文：[[2026-03-28_Steerable-VLA.md]]（VLM-VLA接口）
- 前期论文：[[2026-03-28_UniDex.md]]（UniDex的FAAS动作空间）


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
