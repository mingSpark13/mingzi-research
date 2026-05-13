---
title: "Haptic Sensing for Robot Manipulation: Kinesthetic and Tactile Perception"
authors: Multiple
arxiv: 2508.11261
date: 2025-08
institution: various
conf: arXiv
keywords: Haptic Sensing, Kinesthetic Sensing, Tactile Perception, Body Schema, Proprioception, Embodied AI
tags: ["D02", "具身智能"]
domain: 具身智能
pdf_path: ../../01_论文库/具身智能/2508_HapticSensing.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["力-触融合"]
---

## 🎯 题目

Haptic Sensing for Robot Manipulation: A Comprehensive Survey

## 📝 三句摘要

1. **问题背景**：触觉感知在具身操控中常被忽视，机器人"知道自己身体怎么接触世界"需要的不只是视觉，还有触觉和本体感知。
2. **核心方法**：综述系统梳理了触觉感知的两个维度——接触面触觉（tactile）和本体感知（kinesthetic，即自身身体位置与受力状态的感知），强调二者共同构成机器人的"身体自我感知"。
3. **关键结果**：为具身智能研究提供了完整的触觉/本体感知知识体系，指出了 body schema 在线感知的重要方向。

## 💎 价值评估

- **🔬 研究价值**：为四层闭环框架的"世界感知层"提供了触觉+本体感知作为身体自感知的基础，是主人"身体自我闭环"理论的重要支撑。
- **🚀 实践价值**：触觉传感器选型和部署策略可直接用于实验系统设计。
- **📈 扩展潜力**：kinesthetic sensing 与主人的 body-schema online estimation 直接对应。

## 🎯 可落地实验点

**实验设计**：在 Body-Usage Adapter 中集成 kinesthetic sensing
- 对比基线：纯视觉 + 本体感知（无触觉）
- 度量指标：抓取稳定性、接触力估计误差、身体能力边界更新频率
- 预期结果：触觉 + kinesthetic 应显著提升身体使用参数的自适应调节能力

## 🔗 知识图谱

- [[力-触融合]] - 触觉和本体感知是力-触融合的核心组成部分
- [[具身智能]] - 身体自我感知是具身智能的四层闭环框架第一层

## 📌 待探索问题

- kinesthetic sensing 的精度如何校准？在动态接触中如何保持实时性？
- 触觉和本体感知如何与意图层/身体使用层的信息接口设计？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
