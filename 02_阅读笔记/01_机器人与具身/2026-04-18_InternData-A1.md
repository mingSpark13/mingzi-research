---
title: "InternData-A1: Vast and Diverse Simulation Data for Embodied Intelligence"
authors: "InternRobot Team"
arxiv: "2511.16651"
date: "2026-04-18"
institution: "InternRobot"
conf: ""
keywords: ["Simulation Data", "VLA", "Sim2Real", "Robotic Manipulation"]
tags: ["数据合成", "VLA架构", "Sim2Real", "具身智能", "仿真平台"]
domain: 具身智能
pdf_path: "../../01_论文库/具身智能/2511.16651_InternData-A1.pdf"
reading_date: 2026-04-18
reading_status: 已读
related_concepts: ["数据合成", "VLA架构", "Sim2Real", "具身智能", "仿真平台"]
summary: "具身智能 VLA 训练严重依赖真实机器人遥操作数据，成本高、规模小、无法覆盖多样化场景和机体，制约了 VLA 的泛化能力。"
---

# 📖 花火格式笔记

## 🎯 题目

InternData-A1: Vast and Diverse Simulation Data for Embodied Intelligence

## 📝 三句摘要

1. **问题背景**：具身智能 VLA 训练严重依赖真实机器人遥操作数据，成本高、规模小、无法覆盖多样化场景和机体，制约了 VLA 的泛化能力。
2. **核心方法**：InternData-A1 构建了 630k+ 条轨迹（7333 小时）的合成数据管线，覆盖 4 种机体、18 项技能、70 个任务、227 个场景；通过完全解耦的仿真流水线，实现灵活的任务组合与异构机体支持，最小化人工调参。
3. **关键结果**：使用与 π0 相同架构的模型在 InternData-A1 上预训练后，可在 49 个仿真任务、5 个真机任务和 4 个灵巧操作任务上匹配官方 π0 基线，并展现零样本 sim-to-real 迁移能力。

## 💎 价值评估

- **🔬 研究价值**：首次证明"纯合成数据可匹配真实机器人数据预训练 VLA 效果"，是具身数据合成领域的重要里程碑。
- **🚀 实践价值**：对主人的 UE 数据采集主线有直接参考价值——其"解耦仿真管线 + 组合任务生成"正是程序化数据采集管线可参考的架构范本。
- **📈 扩展潜力**：其技能空间分解（4emb×18skills×70tasks×227scenes）可迁移到无人机数据的多维任务空间建模。

## 🎯 可落地实验点

**实验设计**：参考 InternData-A1 的任务空间分解（4embodiments×18skills×70tasks×227scenes），主人可将 UE 无人机数据采集也做类似的多维任务空间建模
- 对比基线：无结构化任务空间的随机采集、固定场景的重复采集
- 度量指标：采集数据多样性（技能覆盖率）、下游任务迁移效果
- 预期结果：结构化任务空间采集的数据应显著提升 VLA 的零样本泛化能力

## 🔗 知识图谱

- [[concepts/数据合成]] - 核心贡献：630k+ 条合成轨迹的具身数据管线
- [[concepts/VLA架构]] - 使用与 π0 相同架构验证合成数据有效性
- [[concepts/Sim2Real]] - 零样本 sim-to-real 迁移能力是核心卖点
- [[concepts/具身智能]] - 覆盖多机体、多任务、多场景的具身数据平台
- [[concepts/仿真平台]] - 解耦仿真流水线是技术基础

## 🔗 相关链接

- [[2025-01_pi0]] - π0 架构，InternData-A1 使用相同架构验证
- [[2024-OpenVLA]] - OpenVLA 是另一个重要的开源 VLA 模型

## 📌 待探索问题

- InternData-A1 的零样本 sim-to-real 迁移在无人机场景（空中任务）是否同样有效？
- 其解耦仿真流水线的"完全解耦"具体指哪些模块？传感器仿真与场景生成的解耦程度如何？
- 与主人的 UE 数据采集方案相比，InternData-A1 的任务空间建模有何优劣？

---
**维护**: 花火 · 2026-04-18
