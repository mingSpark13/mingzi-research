---
title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
authors: Fei, Senyu; Wang, Siyin; Shi, Junhao; et al.
arxiv: 2510.13626
date: 2025-10
conf: arXiv
keywords: VLA robustness, Perturbation analysis, LIBERO, Robot manipulation
tags: ["VLA架构", "仿真平台"]
domain: 具身智能
pdf_path: ../../01_论文库/具身智能/2510.13626_LIBERO-plus.pdf
reading_date: 2026-04-18
reading_status: 已读
related_concepts: ["VLA架构", "仿真平台", "跨载体泛化"]
summary: "VLA 模型在机器人操纵 benchmark 上报告高成功率，但这些结果可能掩盖了鲁棒性的根本弱点。"
---

## 🎯 题目

LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models

## 📝 三句摘要

1. **问题背景**：VLA 模型在机器人操纵 benchmark 上报告高成功率，但这些结果可能掩盖了鲁棒性的根本弱点。
2. **核心方法**：在七个维度引入受控扰动进行系统脆弱性分析：物体布局、相机视角、机器人初始状态、语言指令、光照条件、背景纹理、传感器噪声。
3. **关键发现**：模型对扰动因素极度敏感——相机视角和机器人初始状态的 modest perturbation 就让性能从 95% 跌到 30% 以下；但对语言变体却不敏感（模型倾向于完全忽略语言指令）。

## 💎 价值评估

- **🔬 研究价值**：首次系统揭示 VLA 的脆弱性分布，对 VLA 评测范式有重要警示意义。
- **🚀 实践价值**：直接指出当前 VLA 评测不能只看 benchmark 分数，需要在真实变体下评估可靠性。
- **📈 扩展潜力**：可启发主人做龙虾/UE 数据采集时的 perturbation 设计，以及"语义接地动作接口"的必要性论证。

## 🎯 可落地实验点

**实验设计**：参考 LIBERO-Plus 的 perturbation 维度，为龙虾项目仿真数据采集设计扰动扩展方案
- 对比基线：无扰动 baseline、单一扰动、复合扰动
- 扰动维度：视角、物体位姿、光照、背景纹理（参考七维度）
- 预期结果：复合扰动下策略泛化性应显著优于无扰动 baseline

## 🔗 知识图谱

- [[VLA架构]] - VLA 模型鲁棒性评估
- [[仿真平台]] - LIBERO 系列是具身智能标准仿真 benchmark
- [[具身智能]] - 机器人操纵是核心应用场景
- [[跨载体泛化]] - VLA 泛化能力是核心关注点

## 🔗 相关链接

- [[2025-10-01_LIBERO-Plus]] - 本文：LIBERO 系列鲁棒性深度分析
- [[2023-06-01_LIBERO]] - LIBERO：终身机器人学习知识迁移基准

## 📌 待探索问题

- VLA 对语言指令不敏感的根因是什么？是 VLM 表征问题还是 action head 训练方式问题？
- 七维度 perturbation 中哪个对策略泛化性影响最大？这对数据采集的 perturbation 设计有什么直接启示？

---
**维护**: 花火 · 2026-04-18（批量入库）
