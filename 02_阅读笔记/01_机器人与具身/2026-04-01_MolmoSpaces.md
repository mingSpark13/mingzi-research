---
title: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation
authors: Yejin Kim, Wilbert Pumacay, Omar Rayyan, Max Argus, Winson Han, Eli VanderBilt,
  Jordi Salvador, Abhay Deshpande, Rose Hendrix, Snehal Jauhri, Shuo Liu, Nur Muhammad
  Mahi Shafiullah, Maya Guru, Ainaz Eftekhar, Karen Farley, Donovan Clay, Jiafei Duan,
  Arjun Guru, Piper Wolters, Alvaro Herrasti, Ying-Chun Lee, Georgia Chalvatzaki,
  Yuchen Cui, Ali Farhadi, Dieter Fox, Ranjay Krishna
arxiv: 2602.11337
date: 2026-02-11
institution: University of Washington, Allen Institute for AI, Stanford University,
  NVIDIA, TU Darmstadt 等
conf: arXiv
keywords: robot navigation, manipulation benchmark, simulator-agnostic, indoor environments,
  sim-to-real
tags:
- D02
- Sim2Real
domain: 通用操作
summary: 现有机器人 benchmark 很难覆盖真实世界里长尾的室内场景变化、物体几何差异和任务多样性，所以不足以测出策略真正的泛化能力。
pdf_path: ../../01_论文库/通用操作/2602.11337_MolmoSpaces.pdf
reading_date: 2026-04-01
reading_status: 已读
related_concepts:
- Sim2Real
---

## 🎯 题目

A Large-Scale Open Ecosystem for Robot Navigation and Manipulation

## 📝 三句摘要

1. **问题背景**：现有机器人 benchmark 很难覆盖真实世界里长尾的室内场景变化、物体几何差异和任务多样性，所以不足以测出策略真正的泛化能力。
2. **核心方法**：论文提出 **MolmoSpaces** 开放生态，包含 23 万+ 室内环境、13 万+ 带标注物体资产、4.8 万可操作物体和 4200 万稳定抓取，并设计了支持导航、静态/移动操作、多房间长时任务的 **MolmoSpaces-Bench**。
3. **关键结果**：MolmoSpaces-Bench 与真实世界评测呈现极强 sim-to-real 相关性（R=0.96，ρ=0.98），还能暴露提示词措辞、初始关节位姿和相机遮挡等对零样本策略性能的关键敏感因素。

## 💎 价值评估

- **🔬 研究价值**：这篇论文最强的点不是新 policy，而是把“开放、超大规模、跨模拟器、可同时做导航和操作”的 embodied benchmark 基础设施搭起来了，适合作为后续 VLA / 世界模型 / 长程任务规划工作的统一试验田。
- **🚀 实践价值**：对主人很有参考意义——如果以后要做空中操作或跨场景泛化，MolmoSpaces 这种“先把环境与资产标准化，再做大规模仿真筛选”的路线非常值得借鉴；尤其是它强调 prompt、视角遮挡、初始化这些真实部署里的脆弱点。
- **📈 扩展潜力**：可以继续往开放词汇任务生成、世界模型数据合成、跨 embodiment benchmark 扩展；如果迁移到无人机/空中机械臂场景，就是一套很强的数据生产与评测基础框架。

## 🎯 可落地实验点

**实验设计**：复现一个“开放词汇导航+操作”轻量 benchmark 原型，验证大模型策略对提示词和遮挡的敏感性。
- 对比基线：RT-2 / pi0 / 简单任务规划器 + 抓取策略
- 度量指标：任务成功率、跨场景泛化率、提示词扰动后的性能下降、不同视角遮挡下的鲁棒性
- 预期结果：和 MolmoSpaces 结论一致，强策略在标准条件下表现不错，但对 prompt phrasing 和相机 occlusion 仍然高度敏感

## 🔗 知识图谱
- [[具身智能]] - 统一导航与操作的 embodied benchmark 基础设施
- [[任务与运动规划]] - 多房间长程任务需要感知、规划、交互协同
- [[Sim2Real]] - benchmark 与真实部署强相关是论文核心卖点
- [[VLA]] - 零样本机器人策略的重要评测对象
- [[SLAM]] - 大规模室内导航场景与地图构建密切相关

## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- [[2023_RT-2]] - 零样本视觉语言动作策略代表工作，可作为 MolmoSpaces 中的 policy 评测对象
- [[2024-10_pi0]] - 新一代通用机器人策略基线，适合放到该 benchmark 中做统一比较
- [[2026-04-01_GigaWorld-Policy]] - 都在探索“大规模环境/世界建模”支撑真实机器人泛化，但 MolmoSpaces 偏 benchmark 基础设施，GigaWorld-Policy 偏统一 world-action model

## 📌 待探索问题

- MolmoSpaces 这种室内 benchmark 生态，怎么迁移到主人更关心的 **空中操作 / 空中机械臂** 场景？
- 如果把 MolmoSpaces 的开放环境生成能力和世界模型数据合成结合，能不能形成自动扩展任务难度的数据飞轮？
- 它测出了 prompt phrasing 和 occlusion 很敏感，那能否专门设计一个“鲁棒提示工程 + 主动视角调整”的策略层来补这个短板？

---
**维护**: 花火 · 2026-04-12
