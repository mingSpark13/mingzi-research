---
title: "Autonomous Frontier-Based Exploration with VLM Guidance"
authors: Aarush Aitha, Avideh Zakhor
arxiv: 2605.23165
date: 2026-05-22
institution: UC Berkeley
conf: CVPR 2026 Workshop (2nd 3D-LLM/VLA Workshop)
keywords: [VLM引导探索, Frontier检测, 自主探索, 无人机]
tags: [空中VLN, SLAM, 长程任务规划, 语义导航, 主动感知]
domain: 空中操作
pdf_path: "../../01_论文库/空中操作/2605.23165_Frontier_Exploration.pdf"
reading_date: 2026-05-28
reading_status: 已读
---

# 📖 花火格式笔记

## 🎯 题目

Autonomous Frontier-Based Exploration with VLM Guidance

## 📝 三句摘要

1. **问题背景**：传统自主探索依赖几何驱动的算法（frontier-based exploration、Next-Best-View planning），缺乏语义层面的上下文推理能力。
2. **核心方法**：提出 VLM（Google Gemini 2.5 Pro）引导的探索管道，在决策点生成包含当前地图和候选路径视觉图像的多模态 prompt，让 VLM 选择最有前景的 frontier，替代简单的几何启发式。
3. **关键结果**：VLM 分析能替换简单几何启发式，实现基于上下文空间推理的探索策略选择。

## 💎 价值评估

- **🔬 研究价值**：首次系统验证 VLM 在自主探索中高层战略决策的可行性，为"VLM as规划器"提供新证据。
- **🚀 实践价值**：对无人机未知环境探索、灾害响应等场景有直接应用价值；方法可叠加到现有 frontier 探索系统上。
- **📈 扩展潜力**：可与 AirSpark 的程序化场景生成结合，构建 VLM 引导的主动探索数据集；也是 UAV 语义导航的重要技术储备。

## 🎯 可落地实验点

**实验设计**：将 Gemini 2.5 Pro 引导的 frontier 选择集成到 AirSpark 的仿真探索管道
- 对比基线：纯几何 frontier-based 探索策略
- 度量指标：探索覆盖率、目标发现速度、语义目标命中率
- 预期结果：VLM 引导应能显著提升语义目标（如"找到红色建筑"）的发现效率

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。

- [[空中VLN]] - 无人机自主探索本属此方向
- [[语义导航]] - VLM提供语义级推理能力
- [[长程任务规划]] - 高层战略决策由VLM完成
- [[主动感知]] - 机器人主动选择观察点
- [[SLAM]] - 底层建图支撑

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作）。

- [[2024-FrontierExploration]] - Frontier-based Exploration: 传统基线，本文替代对象
- [[2024-Gemini]] - Gemini 2.5 Pro: 本文使用的VLM后端

## 📌 待探索问题

- VLM 的推理延迟是否满足实时探索要求？如何在延迟和决策质量间平衡？
- 该方法在动态环境（人员走动、物体移动）中的鲁棒性如何？

---
**维护**: 花火 · 2026-05-28
