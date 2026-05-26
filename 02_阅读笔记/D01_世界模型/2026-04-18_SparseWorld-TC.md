---
type: "paper"
title: "SparseWorld-TC: Trajectory-Conditioned Sparse Occupancy World Model"
authors: "Jiayuan Du, Yiming Zhao, Zhenglong Guo, Yong Pan, Wenbo Hou, Zhihui Hao, Kun Zhan, Qijun Chen"
arxiv: 2511.22039
date: 2025-11-28
institution: "Shanghai Jiao Tong University"
direction: "世界模型"
pdf_path: "../../01_论文库/世界模型/2511.22039_SparseWorld-TC.pdf"
tags: ["世界模型", "感知与3D视觉"]
summary: "SparseWorld-TC 用轨迹条件查询直接预测未来稀疏 3D occupancy，绕开 BEV 中间表征瓶颈，为世界模型与规划耦合提供更高效的场景动态建模方式。"
reading_date: 2026-04-18
reading_status: "已读"
related_concepts: ["世界模型", "感知与3D视觉"]
---

# 📖 花火格式笔记

## 🎯 题目

SparseWorld-TC: Trajectory-Conditioned Sparse Occupancy World Model

## 📝 三句摘要

1. **问题背景**：传统世界模型依赖 VAE 生成离散占用 token，表征能力受限；BEV 中间表征引入信息瓶颈，限制了动态场景预测精度。
2. **核心方法**：SparseWorld-TC 以稀疏占用表示为基础，输入历史多视角图像+未来轨迹查询，输出未来3D占用网格，支持长时序预测，无需 BEV 中间表征。
3. **关键结果**：首次将轨迹条件引入稀疏占用世界模型，实现从图像空间直接推理 occupancy，在动态场景预测一致性上显著优于 BEV-based 方法。

## 💎 价值评估

- **🔬 研究价值**：轨迹条件世界模型是自动驾驶/机器人规划的新兴方向；稀疏表示相比稠密 BEV 更高效，适合实时推理。
- **🚀 实践价值**：与主人 **UE 数据采集** 方向高度相关：程序化场景生成可结合 occupancy 预测做数据增强。
- **📈 扩展潜力**：SparseWorld-TC 的 occupancy 预测可作为龙虾项目的场景语义补充输入，探索"语言指令→占用预测→轨迹规划"端到端链路。

## 🎯 可落地实验点

将 SparseWorld-TC 的 occupancy 预测作为龙虾项目的场景语义补充输入，探索"语言指令→占用预测→轨迹规划"端到端链路。
- 对比基线：无 occupancy 辅助 / BEV-based occupancy
- 度量指标：动态场景预测一致性、规划成功率
- 预期结果：稀疏 occupancy 提升复杂动态场景的预测与规划性能

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[世界模型]] - 核心研究主线，轨迹条件稀疏占用世界模型
- [[感知与3D视觉]] - 3D occupancy 感知属于此方向

## 🔗 相关链接

- [[2026-04-18_SparseOccVLA]] - 稀疏 occupancy 与 VLA 融合的同方向工作
- [[2026-04-18_OmniNWM]] - 世界模型方向相关工作

## 📌 待探索问题

- 稀疏 occupancy 的稀疏度如何自适应场景复杂度？
- 轨迹条件查询能否泛化到非结构化室外无人机场景？

---
**维护**: 花火 · 2026-04-18
