---
title: "SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes"
authors: "Nicholas Pfaff, Thomas Cohn, Sergey Zakharov, Rick Cory, Russ Tedrake"
arxiv: "2602.09153"
date: "2026-02-09"
institution: "Massachusetts Institute of Technology, Toyota Research Institute"
conf: "arXiv"
tags:
  - "具身智能"
  - "仿真平台"
  - "数据合成"
  - "感知与3D视觉"
summary: "Agentic 室内场景生成框架，打通文字到可仿真物理场景的自动构建链路。"
domain: "具身智能"
pdf_path: "../../01_论文库/具身智能/2602.09153_SceneSmith.pdf"
reading_date: "2026-04-18"
reading_status: "已读"
---

# 📖 花火格式笔记

## 🎯 题目

SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes

## 📝 三句摘要

1. **问题背景**：现有仿真环境场景稀疏、缺乏密集杂物和铰接式家具，物理属性缺失，无法支撑家庭机器人的真实训练需求。
2. **核心方法**：提出 SceneSmith，一个层次化 Agentic 框架，从自然语言生成仿真就绪室内场景。场景通过建筑布局→家具摆放→小物体填充的层级构建，每步由 Designer/Critic/Orchestrator 三种 VLM Agent 协作完成。资产生成通过 text-to-3D 合成（静态物体）+ 数据集检索（铰接家具）+ 物理属性估计联合实现。
3. **关键结果**：相比基线多生成 3-6x 物体（71.1 vs 11-23 个/房间），碰撞率<2%，物理稳定性 96%；用户研究显示 92% 真实感、91% prompt 遵从性。

## 💎 价值评估

- **🔬 研究价值**：首个实现"生成资产+组装场景+物理属性"全链路自动化的室内场景生成工作，填补了仿真环境缺乏密集物理可交互场景的空白。
- **🚀 实践价值**：与 SAGE 同源但聚焦室内场景，与 UAV 关联度一般。其 Designer-Critic-Orchestrator Agent 架构是具身智能仿真场景生成的通用范式参考。
- **📈 扩展潜力**：Dense object population 策略可启发无人机室外场景的密集物体场景生成；物理属性估计方法可迁移到 UAV 场景的碰撞属性建模。

## 🎯 可落地实验点

**实验设计**：借鉴 SceneSmith 的物理属性估计方法，探索面向 UAV 城市场景的物体碰撞属性自动标注方案。
- 对比基线：无碰撞属性 UE 场景 vs 碰撞属性自动标注场景
- 度量指标：导航碰撞率、穿模率
- 预期结果：自动碰撞属性标注可提升仿真数据的物理真实性

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[concepts/具身智能]] - 应用领域，家庭机器人场景生成
- [[concepts/仿真平台]] - 场景部署目标，支持物理仿真
- [[concepts/数据合成]] - 大规模室内场景自动生成
- [[concepts/感知与3D视觉]] - 场景理解与资产生成基础

## 🔗 相关链接

> 链接本文核心引用的相关论文。

- [[2024_ProcTHOR]] - ProcTHOR: 规则驱动室内场景生成基线
- [[2026_SAGE]] - SAGE: 同源工作，具身 AI 场景生成，本文姐妹篇

## 📌 待探索问题

- SceneSmith 的铰接家具检索策略在 UAV 室外场景中是否有对应资产来源（如 3D 资产库）？
- Dense object population 的碰撞率控制方法能否泛化到非室内场景？
- 端到端 pipeline（自然语言→场景→策略执行→验证）的完整闭环是否可迁移到 UAV 城市场景？

---
**维护**: 花火 · 2026-04-18
