---
title: Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air
authors: Tianle Zeng, Yanci Wen, Xueang Yu, Hong Zhang
arxiv: 2605.31066
date: 2026-05-29
institution: University of Alberta
conf: arXiv
keywords: ["aerial VLA", "air-ground coordination", "closed-loop evaluation"]
tags: ["跨载体泛化", "空中操作", "语义导航"]
summary: "CARLA-Air 把 CARLA 与 AirSim 统一到同一运行时，用闭环任务量化 aerial VLA 在空地协同中的真实协作缺口。"
domain: 跨载体泛化
pdf_path: "../../01_论文库/空地迁移/2605.31066_CARLA_Air_Cooperation.pdf"
reading_date: 2026-06-01
reading_status: 已读
related_concepts: ["跨载体泛化", "空中操作", "语义导航"]
---

# 📖 花火格式笔记

## 🎯 题目

Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air

## 📝 三句摘要

1. **问题背景**：提出 CARLA-Air，把 CARLA 与 AirSim 放进同一 Unreal 运行时，专门测空地协同中的物理同步、时延和闭环配合。
2. **核心方法**：用移动平台降落与遮挡恢复护送两类诊断任务，评估现有 aerial VLA 与规划基线能否把单机能力迁移到 UAV-UGV 协作。
3. **关键结果**：结果显示现有 aerial VLA 虽能跟踪地面伙伴，但难以形成稳定协作，暴露了跨载体协同中的决策耦合缺口。

## 💎 价值评估

- **🔬 研究价值**：对 D03 很直接：它不是再做单机导航，而是把“空中模型能否迁到空地协同”单独做成闭环评测基准。
- **🚀 实践价值**：对主人后续 AirSpark/跨载体泛化路线有实用价值，可直接借鉴任务设计与 latency 指标。
- **📈 扩展潜力**：后续可作为空地协作 VLA benchmark，对接协同提示、共享状态和层级规划策略。

## 🎯 可落地实验点

**实验设计**：在 CARLA-Air 风格双载体环境里，对比单机 VLA、共享状态提示、显式协同规划三类策略；指标看协同成功率、恢复时延、轨迹同步误差。
- 对比基线：teacher forcing / 单机VLA或现有规划基线
- 度量指标：成功率、长时域漂移、协同时延/轨迹误差
- 预期结果：在闭环长时域或跨载体协作任务中更稳

## 🔗 知识图谱

- [[VLA架构]] - 空中 VLA 的协同外推场景
- [[跨载体泛化]] - UAV 到 UAV-UGV 协作迁移
- [[语义导航]] - 语言条件任务执行
- [[世界模型]] - 闭环协作中的状态预测

## 🔗 相关链接

- [[2026-05-31_WorldVLN]] - 同属空中语言导航/动作建模方向

## 📌 待探索问题

- 能否把共享状态提示替换成显式协同 latent / memory？
- 长时域 rollout 的漂移信号能否反过来驱动数据飞轮筛样？

---
**维护**: 花火 · 2026-06-01
