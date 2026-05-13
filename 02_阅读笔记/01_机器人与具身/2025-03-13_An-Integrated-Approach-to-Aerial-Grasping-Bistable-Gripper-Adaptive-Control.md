---
title: "An Integrated Approach to Aerial Grasping: Combining a Bistable Gripper With Adaptive Control"
authors: Rishabh Dev Yadav, Brycen Jones, Saksham Gupta, Amitabh Sharma, Jiefeng Sun, Jianguo Zhao, Spandan Roy
arxiv: ""
date: 2026-02
institution: University of Denver, Purdue University
conf: IEEE/ASME Transactions on Mechatronics (TMECH), Vol.31 No.1
keywords: aerial grasping, bistable gripper, adaptive control, UAM, mechanical-control co-design
domain: 空中操作
pdf_path: ../../01_论文库/空中操作/2025_An_Integrated_Approach_to_Aerial_Grasping_Bistable_Gripper_Adaptive_Control.pdf
reading_date: 2025-03-13
reading_status: 已读
tags: ["D02", "空中操作", "运动控制"]
summary: "空中抓取面临精确位姿维持和接触力/负载不确定性两大挑战，现有电机驱动夹爪需精确对准且能耗高，传统控制器需要不确定性边界的先验知识。"
related_concepts: ["空中操作", "运动控制"]
---

## 🎯 题目

An Integrated Approach to Aerial Grasping: Combining a Bistable Gripper With Adaptive Control

## 📝 三句摘要

1. **问题背景**：空中抓取面临精确位姿维持和接触力/负载不确定性两大挑战，现有电机驱动夹爪需精确对准且能耗高，传统控制器需要不确定性边界的先验知识。
2. **核心方法**：提出"被动容错+主动补偿"协同设计——双稳态预紧带夹爪接触物体时被动触发抓取（80mm容差），配合无需先验不确定性边界的自适应控制器，通过 Lyapunov 方法保证闭环稳定性。
3. **关键结果**：实时实验验证了集成系统在多种不确定条件（负载变化±50%、接触力扰动）下的鲁棒抓取性能，相比固定增益PID显著提升稳定性。

## 💎 价值评估

- **🔬 研究价值 ⭐⭐⭐⭐⭐**：首次将双稳态机构与自适应控制深度集成用于空中抓取，提供"机械-passive + control-active"设计范式
- **🚀 实践价值 ⭐⭐⭐⭐⭐**：可应用于基础设施检测、精准农业、物流配送等空中操作场景，80mm大容差降低了部署精度要求
- **📈 扩展潜力 ⭐⭐⭐⭐⭐**：被动容错+主动补偿思路可迁移到其他空中操作平台，自适应律可扩展到多自由度操作

## 🎯 可落地实验点

**实验设计**：对比"被动容错+主动补偿" vs 纯主动控制的空中抓取性能

- 方案A：双稳态夹爪 + 自适应控制器（论文方案）
- 方案B：电机驱动夹爪 + 固定增益PID
- 方案C：电机驱动夹爪 + 自适应控制器（消融实验）

**度量指标**：
- 抓取成功率（不同初始偏差：20mm/40mm/60mm/80mm）
- 位置跟踪误差（mm）
- 接触力峰值（N）
- 能耗（Wh）

**预期结果**：方案A在大偏差下成功率显著高于B/C，验证机械容错的关键作用；方案C在小偏差下接近A，说明自适应控制是必要补充。


## 🔗 知识图谱

- [[空中操作]]
- [[无人机避障]]
- [[运动控制]]

## 🔗 相关链接

- [[2025-03-13_Flying-Hand]] - 同为空中操作，ee-centric框架+MPC控制
- [[2025-03-13_UMI-on-Air]] - 空中操作的策略学习，可搭配本文的底层控制
- [[2026-03-15_Drones_Review]] - 协作空中操作综述，覆盖本文所属类型
- [[空中操作]] - 核心概念
- [[运动控制]] - 本文控制方法

## 📌 待探索问题

- 双稳态夹爪在高速飞行中（>5m/s）能否可靠触发？
- 预紧带材料的疲劳寿命如何？长期使用后容差是否退化？
- 能否将双稳态机构扩展到多指灵巧操作（而非简单开合）？
- 自适应律在多旋翼协作场景（多机抬物）中如何扩展？

---
**维护**: 花火 · 2026-04-12
