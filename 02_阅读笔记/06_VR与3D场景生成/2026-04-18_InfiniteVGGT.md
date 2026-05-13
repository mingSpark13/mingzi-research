---
title: "InfiniteVGGT: Visual Geometry Grounded Transformer for Endless Streams"
authors: "Shuai Yuan, Yantai Yang, Xiaotian Yang, Xupeng Zhang, Zhonghao Zhao, Lingming Zhang, Zhipeng Zhang"
arxiv: 2601.02281
date: 2026-01-03
institution: 科研机构
conf: arXiv
keywords: [VGGT, 3D reconstruction, long video, temporal modeling, feedforward]
tags: [3D重建, 感知与3D视觉, 深度估计]
domain: 3D视觉
pdf_path: "../../01_论文库/3D视觉/2601.02281_InfiniteVGGT.pdf"
reading_date: 2026-04-18
reading_status: 已读
related_concepts: ["3D重建", "感知与3D视觉", "深度估计"]
---

# 📖 花火格式笔记

## 🎯 题目

InfiniteVGGT: Visual Geometry Grounded Transformer for Endless Streams

## 📝 三句摘要

1. **问题背景**：VGGT 等离线前馈 3D 重建模型单次推理效果惊艳，但处理长视频时会因显存爆炸而失效，无法支撑自动驾驶、机器人等需要长时序 3D 理解的应用。
2. **核心方法**：InfiniteVGGT 提出基于滑动窗口的时序扩展策略，将 VGGT 扩展到无限长视频流，同时保持几何精度和长期稳定性。
3. **关键结果**：解决了"规模化 vs 长期稳定性"的根本矛盾，使大规模 3D 视觉基础模型真正可用于自动驾驶、机器人等长时序场景；为人体跟踪、UAV 目标跟踪等下游任务提供了更强的时间建模能力。

## 💎 价值评估

- **🔬 研究价值**：首个长视频前馈式 3D 重建方案，补全了 VGGT 族模型的时序扩展能力
- **🚀 实践价值**：滑动窗口策略可迁移到其他前馈 3D 模型，增强其处理长时序视频的能力
- **📈 扩展潜力**：与人体跟踪方向强相关，可借鉴其几何对齐策略构建长视频跟踪+重建联合框架

## 🎯 可落地实验点

**实验设计**：在人体跟踪项目中引入 InfiniteVGGT 的滑动窗口长视频几何建模
- 对比基线：无时序建模的单帧 VGGT 跟踪
- 度量指标：3D 重建精度（Luo et al.指标）/ 跟踪成功率 / 时序稳定性
- 预期结果：滑动窗口时序建模可显著提升长视频跟踪的几何一致性

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。

- [[concepts/3D重建]] - 本文核心任务，将视频流前馈式重建为 3D 几何
- [[concepts/感知与3D视觉]] - 本文属于 3D 视觉基础模型方向
- [[concepts/深度估计]] - 单目深度估计是 VGGT 的核心感知基础

## 🔗 相关链接

- [[2026-04-18_DriveVGGT]] - DriveVGGT：VGGT 在自动驾驶 3D 感知中的应用
- [[2026-04-18_OmniVGGT]] - OmniVGGT：VGGT 的全景感知扩展

## 📌 待探索问题

- 滑动窗口边界处的几何接缝问题如何处理？是否有跨窗口的特征传播机制？
- 前馈式 3D 重建与时序滤波（如卡尔曼滤波）结合能否进一步提升长期稳定性？

---
**维护**: 花火 · 2026-04-18
