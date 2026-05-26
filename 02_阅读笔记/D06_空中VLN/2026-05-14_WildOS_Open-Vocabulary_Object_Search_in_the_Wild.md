---
title: "WildOS: Open-Vocabulary Object Search in the Wild"
authors: Hardik Shah, Erica Tevere, Deegan Atha, Marcel Kaufmann, Shehryar Khattak, Manthan Patel, Marco Hutter, Jonas Frey, Patrick Spieler
arxiv: "2602.19308"
date: 2026-02-22
institution: "NASA JPL, ETH Zürich, Stanford University, UC Berkeley, FieldAI Inc."
conf: arXiv
keywords: ["开放词汇目标搜索", "语义导航", "视觉前沿检测", "稀疏导航图", "长距离机器人导航"]
tags: ["语义导航", "感知与3D视觉", "腿足机器人", "具身智能"]
domain: 语义导航
pdf_path: "../../01_论文库/语义导航/2602_19308_WildOS.pdf"
reading_date: 2026-05-14
reading_status: 已读
related_concepts: ["语义导航", "感知与3D视觉", "腿足机器人", "具身智能"]
---

# 📖 WildOS: Open-Vocabulary Object Search in the Wild

## 🎯 题目

**WildOS: Open-Vocabulary Object Search in the Wild**

## 📝 三句摘要

1. **问题背景**：复杂非结构化户外场景中，传统纯几何机器人导航依赖有限的深度传感器感知范围，无法进行语义推理，导致探索效率低下且缺乏对"该往哪走"的语义理解能力。

2. **核心方法**：提出统一导航系统 WildOS，融合几何安全探索与语义视觉推理。系统由稀疏导航图（存储空间记忆）+ ExploRFM 视觉基础模型（边界节点打分、通行性预测、目标相似度）+ 粒子滤波目标定位（超出深度传感器范围的远距离定位）三大模块组成。

3. **关键结果**：在 off-road 和 urban 多种地形进行闭环户外实验，WildOS 在导航效率和成功率上**显著优于纯几何基线和纯视觉基线（LRN）**，且展现出零样本泛化能力。

## 💎 价值评估

- **🔬 研究价值**：首次将 VFM（Vision Foundation Model）语义能力与稀疏图导航图结构深度融合，解决了长距离开放词汇目标搜索中"语义理解"与"几何安全"不可兼得的核心矛盾，为户外语义导航提供了新范式。

- **🚀 实践价值**：在 Boston Dynamics Spot 四足平台上完全机载运行（Jetson AGX Orin），验证了从研究到真实户外场景部署的可行性，对搜救、巡检等应用直接有意义。

- **📈 扩展潜力**：ExploRFM 的 VFM 特征可零样本泛化到新环境，与主人研究中 VLA 策略结合潜力大；稀疏图结构易于与现有 VLA 规划层集成；粒子滤波目标定位可扩展为多目标跟踪。

## 🎯 可落地实验点

**实验设计：将 ExploRFM 语义打分模块集成到现有 VLA 导航策略中**

- **实验平台**：ANYmal 或 Spot 四足机器人
- **对比基线**：
  1. 纯 VLA 视觉策略（无语义边界打分）
  2. WildOS 纯几何版（Vanilla GraphNav）
  3. 完整 WildOS（几何+视觉+粒子滤波）
- **核心改动**：将 ExploRFM 的 `Ttvis`（视觉通行性）和 `Ftvis`（视觉边界）输出作为 VLA 策略的高层奖励/代价输入，引导策略优先探索"视觉上可通行+有新的视觉信息"的区域
- **度量指标**：成功率、平均导航距离、导航时间、路径平滑度
- **预期结果**：融合语义打分后，机器人在复杂户外场景（如有障碍物的开放场地）的探索效率提升 30%+，减少无效往复运动

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。
> 字典真源：`06_知识Wiki/_views/概念关键词字典.md`

- [[语义导航]] - 本文核心任务场景，基于语义目标进行导航
- [[感知与3D视觉]] - ExploRFM 的视觉基础模型特征提取、粒子滤波三角化
- [[腿足机器人]] - Spot 四足平台为本文硬件验证载体
- [[具身智能]] - 户外非结构化场景的机载感知-规划-动作闭环

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作），通常 2-5 篇。

- [[2025-02_LRN]] - LRN: Long Range Navigation，本文核心对比基线，纯视觉边界导航方法
- [[2025-02_pi0]] - π0: 本文涉及 VLA 端到端策略的参考架构

## 📌 待探索问题

- ExploRFM 的视觉边界检测（Ftvis）与通行性预测（Ttvis）在动态场景（如风吹草动）下的鲁棒性如何？是否需要时序平滑？
- 粒子滤波目标定位在目标被长期遮挡（如穿越密林）时，粒子退化和重激活的策略是什么？
- 稀疏导航图随探索面积增长，边际效益如何？是否有规模上限需要工程优化（如剔除历史节点）？

---
**维护**: 花火 · 2026-05-14
