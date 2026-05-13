---
title: "LOVON: Legged Open-Vocabulary Object Navigator"
authors: ""
arxiv: ""
date: 2025
institution: ""
conf: ""
keywords: legged robot, open-vocabulary detection, semantic navigation, Unitree Go2, real-world deployment
tags: ["D06", "腿足机器人"]
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["腿足机器人"]
---

## 🎯 题目

LOVON: 四足开放词汇目标导航器

## 📝 三句摘要

1. **问题背景**：四足机器人开放词汇语义导航缺少完整系统方案，很多方法只在仿真验证，难以应对真实世界的 visual jitter、blind zone、target loss 等问题。
2. **核心方法**：围绕"自然语言 + 开放词汇目标检测 + 长程导航"构建完整系统，明确针对 Unitree Go2/H1-2/B2 部署，考虑了视觉抖动和盲区问题。
3. **关键结果**：在 Unitree 系列四足上完成真实世界部署验证，是目前最接近四足工程落地需求的开放词汇导航系统。

## 💎 价值评估

- **🔬 研究价值**：提供了四足开放词汇导航的完整系统方案，填补了实机部署的空白。
- **🚀 实践价值**：代码针对真实四足优化，能直接部署到 Unitree Go2；如果主人要做四足实机实验，这是最直接的参考。
- **📈 扩展潜力**：其目标检测 + 导航框架可迁移到无人机平台，特别是视觉感知部分可复用。

## 🎯 可落地实验点

**实验设计**：在 Unitree Go2 上部署 LOVON，验证"找垃圾桶/找风扇"等语义目标搜索能力
- 对比基线：SemExp、VLFM（部署版本）
- 度量指标：SR、SPL、Real-world Deployment Success Rate
- 预期结果：LOVON 在真实四足上的 SR > 60%，比仿真结果衰减 <15%

## 🔗 知识图谱
- [[抓取检测]]
- [[四足机器人]]
- [[实机部署]]
- [[语义导航]]
- [[传感器补偿]]

## 🔗 相关链接

- [[2025_NaVILA_Two-Level_VLA_Navigation]] - NaVILA 的两层架构与 LOVON 的系统设计思路相近
- [[2024_VLFM_Vision-Language_Frontier_Maps]] - VLFM 是核心算法基线

## 📌 待探索问题

- LOVON 在非 Unitree 平台（如自定义四足或轮式）上的迁移成本有多高？
- visual jitter 和 blind zone 的补偿机制是否足够应对快速运动中的目标丢失？

---
**维护**: 花火 · 2026-04-12
