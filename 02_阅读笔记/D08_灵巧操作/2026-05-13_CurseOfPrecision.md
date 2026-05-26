---
title: "The Curse of Precision: A Data Scaling Law for High-Precision Robotic Manipulation"
authors: Cuijie Xu, Yuanfan Xu, Min Xue, Jianjie Lin, Jian Wang, Xudong Zhang, Yu Wang, Jincheng Yu
arxiv: ""
date: 2026
institution: 清华大学
conf: ICRA 2026
keywords: [data scaling law, high-precision manipulation, imitation learning, robotic assembly, limit precision]
tags: [灵巧操作, 模仿学习]
domain: 具身智能
pdf_path: "../../01_论文库/具身智能/2410_CurseOfPrecision.pdf"
reading_date: 2026-05-13
reading_status: 在读
summary: "本文揭示高精度机器人操作中达到目标精度所需示范数据会随精度要求呈超指数增长，并提出极限精度 c 是整个 agent 系统的涌现属性。"
related_concepts: ["灵巧操作", "模仿学习"]
---

# 📖 花火格式笔记

## 🎯 题目

The Curse of Precision: A Data Scaling Law for High-Precision Robotic Manipulation

## 📝 三句摘要

1. **问题背景**：模仿学习 Scaling Law 研究主要关注开放世界泛化，而封闭世界高精度任务（如机械装配）中数据量与精度的关系尚未被系统探索；本文填补了这一空白。
2. **核心方法**：在 ManiSkill3 高保真仿真环境中，对 Peg Insertion、Stack Cuboid、Roll Ball 三个高精度任务进行大规模实验（100+ 次独立训练、数万次 evaluation rollouts），系统建立数据-精度 scaling law。
3. **关键发现**：达到固定成功率所需的 demonstrations N 随目标精度 P 呈超指数增长，关系式为 log(N) ∝ 1/(P−c)；极限精度 c 不是任务的静态物理常数，而是整个 agent 系统的涌现属性（包括传感器和专家策略），改进系统组件（如添加腕部相机）可降低 c、扩展系统可达精度。

## 💎 价值评估

- **🔬 研究价值**：首次系统揭示高精度机器人操作中数据-精度的 scaling law，核心贡献是"极限精度 c 是系统涌现属性"这一反直觉发现，为机器人 precision 任务提供了新的理论框架。
- **🚀 实践价值**：提供了定量评估系统能力的指标（c 值），并给出"改进传感器/专家策略 → 降低 c → 扩展可达精度"的系统调试方法论；实验在 ManiSkill3 完成，可直接复现。
- **📈 扩展潜力**：c 的系统属性理论可扩展到 Sim2Real 领域（c 可以衡量 sim-to-real gap）；可指导数据采集策略（何时停止采集、如何分配标注资源）；对 Isaac 户外机械臂高精度任务有直接参考价值。

## 🎯 可落地实验点

**实验设计**：在 Isaac Lab 中复现本文 scaling law 验证框架，扩展到空中操作场景

- 对标任务：空中机械臂末端抓取精度 vs 数据量关系
- 基线对比：固定精度（0.5cm / 1cm / 2cm）下，不同数据量 N 的成功率曲线
- 核心验证：极限精度 c 是否随传感器质量（加入 IMU/视觉）而降低
- Isaac 扩展：在 UAV 扰动下测量末端抓取 c 值，验证 c 的系统属性在移动平台依然成立

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。
> 字典真源：`06_知识Wiki/_views/概念关键词字典.md`

- [[灵巧操作]] - 高精度机械装配任务的核心场景
- [[模仿学习]] - 数据 scaling law 的训练范式基础

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作），通常 2-5 篇。

- [[2024-10_pi0]] - π0: 本文使用的模仿学习基线策略之一
- [[2024_ManiSkill3]] - ManiSkill3: 本文实验所基于的高保真仿真环境

## 📌 待探索问题

- Isaac 空中操作场景中，c 的物理意义如何定义？基座扰动下极限精度 c 是否会显著提升？
- 如何在有限数据 budget 下通过优化 c 来最大化可达精度——这本质上是系统设计的优化问题还是数据量问题？

---
**维护**: 花火 · 2026-05-13
**备注**: ICRA 2026 论文，清华大学 nicsefc 实验室，PDF 直链下载
