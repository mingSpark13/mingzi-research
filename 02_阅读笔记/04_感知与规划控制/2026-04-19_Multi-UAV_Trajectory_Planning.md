---
title: "Trajectory Planning for a Multi-UAV Rigid-Payload Cascaded Transportation System Based on Enhanced Tube-RRT*"
authors: Multiple (from arXiv 2604.15074)
arxiv: 2604.15074
date: 2026-04-19
institution: Multi-UAV Trajectory Planning
conf: arXiv
keywords: [Multi-UAV, Trajectory Planning, Rigid-Payload, RRT*, Cable Oscillation]
domain: 无人机轨迹规划
pdf_path: ../../01_论文库/2604.15074.pdf
reading_date: 2026-04-19
reading_status: 已读
tags: ["D04", "多无人机", "轨迹规划", "刚体负载", "RRT*"]
summary: "多无人机刚体负载运输系统在密集障碍物环境中的轨迹规划问题，需要同时处理碰撞避免和缆绳振荡抑制。"
related_concepts: ["多无人机", "轨迹规划", "刚体负载", "RRT*", "缆绳振荡"]
---

## 🎯 题目

Trajectory Planning for a Multi-UAV Rigid-Payload Cascaded Transportation System Based on Enhanced Tube-RRT*

## 📝 三句摘要

1. **问题背景**：多无人机刚体负载运输系统在密集障碍物环境中的轨迹规划需要同时处理碰撞避免和缆绳振荡抑制，是个两阶段复杂问题。
2. **核心方法**：Stage I提出Enhanced Tube-RRT*算法，集成主动混合采样和自适应扩展策略；Stage II建立考虑负载平移旋转动力学、缆绳张力和碰撞安全约束的凸二次规划。
3. **关键结果**：Enhanced Tube-RRT*相比STube-RRT*和AETube-RRT*达到更高成功率和有效采样率，路径更短、转角更小。

## 💎 价值评估

- **🔬 研究价值**：首次解决多无人机刚体负载系统的两阶段规划问题，融合了采样规划与优化控制。
- **🚀 实践价值**：为物资投放、无人机编队运输提供了实用的规划框架。
- **📈 扩展潜力**：双阶段框架可推广到柔性负载或其他构型无人机的轨迹规划。

## 🎯 可落地实验点

**实验设计**：将Enhanced Tube-RRT*应用于多无人机物资精准投放
- 对比基线：标准RRT*、凸优化轨迹规划
- 度量指标：任务成功率、轨迹平滑度（累积转角）、缆绳振荡幅度
- 预期结果：Enhanced Tube-RRT*应在密集障碍场景显著优于基线

## 🔗 知识图谱

- [[无人机轨迹规划]] - 多机规划是本文的核心应用
- [[RRT*]] - Enhanced Tube-RRT*是对RRT*的改进
- [[多无人机协同]] - 多机编队控制是本文的场景

## 🔗 相关链接

- [[2025-12-22_IndoorUAV]] - IndoorUAV的规划方法与本文可对比
