---
type: "paper"
title: "SparseOccVLA: Bridging Occupancy and Vision-Language Models via Sparse Queries for Unified 4D Scene Understanding and Planning"
authors: "Y. Chen, Z. Wang, et al."
arxiv: 2601.06474
date: 2026-01-13
institution: "Momenta / Tsinghua University"
direction: "具身智能"
pdf_path: "../../01_论文库/具身智能/2601.06474_SparseOccVLA.pdf"
tags: ["VLA架构", "世界模型", "感知与3D视觉"]
reading_date: 2026-04-18
reading_status: "已读"
related_concepts: ["VLA架构", "世界模型", "感知与3D视觉"]
---

# 📖 花火格式笔记

## 🎯 题目

SparseOccVLA: Bridging Occupancy and Vision-Language Models via Sparse Queries for Unified 4D Scene Understanding and Planning

## 📝 三句摘要

1. **问题背景**：VLMs 擅长高层推理但受限于 token 爆炸和时空推理能力弱；语义 occupancy 表达精细但过于稠密难以与 VLM 高效融合。
2. **核心方法**：提出 SparseOccVLA，用稀疏 occupancy queries 作为视觉与语言的统一桥梁；引入 LLM-guided Anchor-Diffusion Planner，解耦锚点评分与去噪，支持跨模态轨迹条件融合。
3. **关键结果**：在 OmniDrive-nuScenes 上 CIDEr 相对提升 7%，Occ3D-nuScenes mIoU 提升 0.5，nuScenes 规划指标达到 SOTA。

## 💎 价值评估

- **🔬 研究价值**：首次有效融合 VLM 与稀疏 occupancy 范式，解决了 token 爆炸难题，为自动驾驶世界模型提供新思路。
- **🚀 实践价值**：端到端统一框架，兼顾感知、预测、规划三任务，对接下游控制直接可用。
- **📈 扩展潜力**：Anchor-Diffusion Planner 可迁移到无人机 VLA 动作生成；稀疏 query 机制适合多相机系统。

## 🎯 可落地实验点

**实验设计**：将 SparseOccVLA 的稀疏 occupancy encoder 引入无人机端到端规划
- 对比基线：原生 VLA（如 π0）+ BEV-based occupancy
- 度量指标：规划轨迹一致性（碰撞率 + 任务成功率）
- 预期结果：稀疏 query 降低计算量的同时保持场景理解精度

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[VLA架构]] - 视觉-语言-动作统一端到端模型核心架构
- [[世界模型]] - 仿真/驾驶场景的动态世界建模
- [[感知与3D视觉]] - 3D occupancy 感知属于此方向

## 🔗 相关链接

- [[2026-04-18_OmniNWM]] - 同为自动驾驶世界模型，本文 SparseOccVLA 侧重 VLA 融合 occupancy
- [[2026-04-18_SparseWorld-TC]] - 稀疏 occupancy 方向相关工作

## 📌 待探索问题

- Anchor-Diffusion Planner 的计算开销与实时性边界在哪里？
- 稀疏 query 数量如何自动适应不同场景复杂度？
- 能否迁移到非结构化室外无人机场景？

---
**维护**: 花火 · 2026-04-18
