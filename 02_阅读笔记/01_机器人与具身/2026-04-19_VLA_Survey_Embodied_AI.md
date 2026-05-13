---
title: A Survey on Vision-Language-Action Models for Embodied AI
authors: Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, Irwin King
arxiv: 2405.14093
date: 2024-05-22
institution: The Chinese University of Hong Kong, Shenzhen; Shenzhen Research Institute of Big Data
conf: arXiv
keywords: [Embodied AI, Vision-Language-Action, Survey, Robot Learning, Foundation Model]
tags: ["VLA架构", "多模态统一架构", "模仿学习", "LLM驱动机器人", "具身智能"]
summary: "系统梳理 VLA 的定义、架构、训练范式与应用场景，是建立具身智能 VLA 全局地图的高价值综述入口。"
domain: 具身智能
pdf_path: "../../01_论文库/具身智能/2405.14093_VLA_Survey_Embodied_AI.pdf"
reading_date: 2026-04-19
reading_status: 待读
related_concepts: ["VLA架构", "多模态统一架构", "模仿学习", "LLM驱动机器人", "具身智能"]
---

## 🎯 题目

A Survey on Vision-Language-Action Models for Embodied AI

## 📝 三句摘要

1. **问题背景**：VLA 在 2023-2024 快速爆发，但不同工作分散在 manipulation、navigation、planning 等子方向，缺少一份系统综述帮助建立统一认知框架。
2. **核心方法**：这篇综述从 embodied AI 的整体视角梳理 VLA 的定义、核心架构、训练范式、代表模型与应用场景，并讨论数据、泛化、闭环控制与真实部署中的关键挑战。
3. **关键结果**：它给出了一条相对清晰的 VLA 演化脉络：从视觉语言模型扩展到动作生成，再走向多模态统一、长期规划和真实世界机器人落地，是很适合拿来补全主人整体地图的一篇基础综述。

## 💎 价值评估

- **🔬 研究价值**：这篇不是追单点 SOTA 的论文，而是“搭骨架”的综述，适合作为后续任何 VLA 阅读的总导航，尤其适合统一术语、梳理代表架构和识别空白点。
- **🚀 实践价值**：主人之后写 related work、开题背景、研究汇报时，这篇能直接当结构参考；尤其在讲“为什么需要 VLA、VLA 和传统模块化方法差在哪”时很好用。
- **📈 扩展潜力**：它本身不提供方法创新，但很适合作为索引入口，往 UAV VLA、world model、cross-embodiment、efficient VLA 这些更具体方向继续挖。

## 🎯 可落地实验点

**实验设计**：基于该综述整理一份“主人当前研究最相关的 VLA 子谱系图”
- 对比基线：manipulation VLA、navigation VLA、world-model-enhanced VLA、cross-embodiment policy 四类路线
- 度量指标：不是数值指标，而是比较输入模态、动作表示、训练数据、实时性、可迁移性
- 预期结果：形成一张适合主人长期维护的 related-work 地图，帮助后续论文选型和实验设计少走弯路

## 🔗 知识图谱

- [[concepts/VLA架构]] - 综述的核心主线
- [[concepts/多模态统一架构]] - 统一视觉、语言、动作的关键范式
- [[concepts/模仿学习]] - 许多 VLA 的基础训练范式
- [[concepts/LLM驱动机器人]] - 与高层推理/规划结合的重要方向
- [[concepts/具身智能]] - 论文整体所属的大框架

## 🔗 相关链接

- [[2026-03-27_RT-2]] - VLA 早期代表工作
- [[2026-03-27_OpenVLA]] - 开源 VLA 代表系统
- [[2026-03-27_pi0]] - 具代表性的现代机器人 foundation policy 路线

## 📌 待探索问题

- 这篇综述成文较早，面对 2025-2026 的 world model VLA、efficient VLA、cross-embodiment VLA，哪些分类需要主人自己补一层新框架？
- 如果以无人机 VLA 为中心重画 taxonomy，现有 manipulation-centered VLA 分类会在哪些地方失效？

---
**维护**: 花火 · 2026-04-19
