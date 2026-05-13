---
title: IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments
authors: Xu Liu, Yu Liu, Hanshuo Qiu, Yang Qirong
arxiv: 2512.19024
date: 2025-12-22
institution: 未知（待补）
conf: arXiv 2025
keywords: 室内UAV, VLN, 视觉语言导航, 基准测试, 连续3D环境
tags: ["空中视觉语言导航", "语义导航"]
domain: 语义导航
summary: "首个面向连续室内3D环境的UAV视觉语言导航基准，补齐室内空中VLN评测空白。"
pdf_path: ../../01_论文库/语义导航/2512.19024_IndoorUAV.pdf
reading_date: 2026-04-17
reading_status: 已读
related_concepts: ["空中视觉语言导航", "语义导航"]
---

# 📖 花火格式笔记

## 🎯 题目

IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments

## 📝 三句摘要

1. **问题背景**：现有 VLN 研究集中在地面机器人或室外无人机，室内 UAV 的视觉语言导航几乎空白，而室内检查/配送/搜救等场景有强烈需求。
2. **核心方法**：构建 IndoorUAV 基准，包含 1000+ 多样化室内场景，专为连续 3D 空中 VLN 设计，提供配套导航方法。
3. **关键结果**：填补了室内连续 3D 空中 VLN 基准的空白，为后续方法提供标准化评测平台。

## 💎 价值评估

- **🔬 研究价值**：首个专注室内连续 3D 空中 VLN 的基准，填补 D06 方向的评测空白；连续环境设定比离散 waypoint 更贴近真实部署。
- **🚀 实践价值**：室内检查/搜救场景直接对应工业需求；基准数据集可作为 D06 实验的标准评测集。
- **📈 扩展潜力**：可与 D04 的 physics adapter 结合，探索室内动力学约束下的语义导航；连续 3D 设定为 end-to-end 方法提供更真实的训练信号。

## 🎯 可落地实验点

**实验设计**：在 IndoorUAV 基准上验证 D06 的 L0-L3 实验路由表
- 对比基线：显式搜索方法 vs. 轻量端到端方法 vs. 几何重定位补件
- 度量指标：导航成功率（SR）、路径长度加权成功率（SPL）、碰撞率
- 预期结果：几何重定位补件在连续 3D 环境中显著提升 SR，尤其在遮挡场景

## 🔗 知识图谱

- [[视觉语言导航]] - 本文核心任务类型，VLN in continuous 3D indoor
- [[空中视觉语言导航]] - 本文专注的子领域，UAV-specific VLN
- [[基准测试]] - 本文主要贡献，室内 UAV VLN benchmark
- [[连续环境导航]] - 区别于离散 waypoint 的连续 3D 导航设定
- [[无人机]] - 本文平台类型

## 🔗 相关链接

- [[2023_R2R]] - R2R: VLN 领域奠基基准，本文在其框架基础上扩展到空中连续环境
- [[2024_NavGPT]] - NavGPT: LLM-based 导航方法，本文基准的对比方法之一

## 📌 待探索问题

- 室内连续 3D 环境中，UAV 的高度自由度如何影响 VLN 策略的探索效率？
- IndoorUAV 基准与室外 UAV VLN 基准（如 AerialVLN）的性能迁移性如何？

---
**维护**: 花火 · 2026-04-17
