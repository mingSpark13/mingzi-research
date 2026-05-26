---
title: "DISCOVERSE: Efficient Robot Simulation in Complex High-Fidelity Environments"
authors: "Y. Jia et al."
arxiv: "2507.21981"
date: "2026-04-18"
institution: ""
conf: "arXiv"
keywords: ["3DGS", "Robot Simulation", "Real2Sim2Real"]
tags: ["仿真平台", "3D高斯溅射", "具身智能", "Sim2Real"]
summary: "现有机器人仿真器在复杂真实场景的高保真建模方面存在显著差距，导致 sim-to-real 迁移效果不佳。"
domain: "具身智能"
pdf_path: "../../01_论文库/具身智能/2507.21981_DISCOVERSE.pdf"
reading_date: "2026-04-18"
reading_status: "已读"
---

# 📖 花火格式笔记

## 🎯 题目

DISCOVERSE: Efficient Robot Simulation in Complex High-Fidelity Environments

## 📝 三句摘要

1. **问题背景**：现有机器人仿真器在复杂真实场景的高保真建模方面存在显著差距，导致 sim-to-real 迁移效果不佳。
2. **核心方法**：DISCOVERSE 提出首个统一模块化的开源 3DGS 仿真框架，专注于 Real2Sim2Real 机器人学习流程，将真实世界与仿真环境闭环连接。
3. **关键结果**：基于 3D Gaussian Splatting 实现高保真物理建模，支持复杂场景的实时渲染与机器人策略迁移验证，在多个机器人任务上验证了有效性。

## 💎 价值评估

- **🔬 研究价值**：提供了 Real2Sim2Real 闭环的系统化框架，对世界模型方向的数据采集和仿真验证有重要参考价值。
- **🚀 实践价值**：DISCOVERSE 的模块化设计理念可用于构建高保真仿真-采集-训练闭环，与 UE5 数据采集管线高度契合。
- **📈 扩展潜力**：可与 3DGS 实时重建技术结合，实现开放场景的持续仿真更新。

## 🎯 可落地实验点

- 借鉴 DISCOVERSE 的模块化架构，设计 UE5 中的 3DGS 仿真层，实现与 AirSim/AirDroneSim 的数据接口标准化
- 探索将 3DGS 重建能力接入城市场景程序化生成流程，实现真实场景的自动仿真化

## 🔗 知识图谱

- [[concepts/仿真平台]] - DISCOVERSE 核心定位是新型仿真基础设施
- [[concepts/3D高斯溅射]] - 实现高保真场景渲染的核心表示方法
- [[concepts/具身智能]] - 论文服务的核心研究领域
- [[concepts/Sim2Real]] - 核心任务是弥合仿真到真实的迁移鸿沟

## 🔗 相关链接

- [[2026-04-18_HUGSIM]] - 同属仿真平台族，相关工作
- [[2026-04-18_Bench2Drive]] - 驾驶仿真相关，同属仿真平台族

## 📌 待探索问题

- DISCOVERSE 的 3DGS 场景重建速度如何？在实时性要求高的场景下是否需要降级处理？
- 模块化设计是否支持多智能体协同仿真场景？
