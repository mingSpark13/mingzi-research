---
title: See, Point, Fly: A Learning-Free VLM Framework for Universal Unmanned Aerial Navigation
authors: Chih Yao Hu, Yang-Sen Lin, Yuna Lee, Chih-Hai Su, Jie-Ying Lee, Shr-Ruei Tsai, Chin-Yang Lin, Kuan-Wen Chen, Tsung-Wei Ke, Yu-Lun Liu
arxiv: 2509.22653
date: 2025-09-26
institution: National Yang Ming Chiao Tung University, National Taiwan University 等
conf: CoRL 2025 (PMLR 305:4697-4708)
keywords: VLM, UAV navigation, learning-free, spatial grounding, aerial vision-language navigation
tags: ["D02", "多模态统一架构"]
domain: 空中操作
pdf_path: ../../01_论文库/空中操作/2509.22653_See_Point_Fly.pdf
reading_date: 2026-04-01
reading_status: 已读
related_concepts: ["多模态统一架构"]
---

## 🎯 题目

See, Point, Fly: A Learning-Free VLM Framework for Universal Unmanned Aerial Navigation

## 📝 三句摘要

1. **问题背景**：现有基于 VLM/VLA 的无人机导航方法往往需要训练或把动作预测当成文本生成，导致泛化差、闭环控制弱，而且很难直接适配开放环境中的自由语言指令。
2. **核心方法**：SPF 把空中视觉语言导航重新定义成 **2D 空间指认（spatial grounding）** 问题，让 VLM 在图像上迭代标注航点，再结合预测的行进距离将 2D 航点反投影成 3D 位移指令，形成“See → Point → Fly”的闭环控制框架。
3. **关键结果**：该方法完全无需训练，在 DRL 仿真基准上相对先前最佳方法取得 **63% 绝对成功率提升**，并在真实世界导航中显著优于强基线，还表现出对不同 VLM 的良好泛化性。

## 💎 价值评估

- **🔬 研究价值**：这篇论文很有意思，因为它没走“端到端学 action token”老路，而是把 VLM 的强项——视觉指认与语言理解——直接变成可执行导航信号，本质上是在给无人机搭一层轻量的感知-决策接口。
- **🚀 实践价值**：对主人特别有价值的点在于：**无需训练、单图像+自然语言就能导航**，这非常适合快速原型验证，也适合和传统控制栈、MPC、安全护栏组合，做低成本开放词汇空中导航。
- **📈 扩展潜力**：后续完全可以把 SPF 从纯导航扩展到“导航 + 感知 + 操作”的空中操作框架，比如把 point 从 waypoint 扩展到抓取点/交互点，再和世界模型、任务规划模块耦合。

## 🎯 可落地实验点

**实验设计**：做一个基于开源 VLM 的无人机开放词汇导航原型，复现 SPF 的 2D 航点 → 3D 位移闭环。
- 对比基线：传统 DRL 导航策略 / 文本生成式 VLM 导航 / 规则式 waypoint 选择
- 度量指标：任务成功率、路径长度、碰撞率、对指令改写的鲁棒性、对动态目标的跟随效果
- 预期结果：SPF 风格的空间指认路线在零训练条件下能明显优于纯文本动作生成方法，并且更容易和控制器解耦集成

## 🔗 知识图谱
- [[空中操作]] - 无人机平台上的开放词汇导航任务
- [[VLA]] - 用 VLM/VLA 能力直接驱动物理系统执行任务
- [[感知与3D视觉]] - 把语义理解映射为图像中的空间位置与位移决策
- [[主动感知]] - 动态环境中的闭环目标跟踪与持续观测
- [[运动控制]] - 2D 航点需转换为 UAV 可执行的 3D 控制指令

## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- [[2026-04-01_Explainable_DRL_UAV_Path_Planning]] - 传统 DRL 无人机路径规划代表路线，对比学习式与 learning-free 路线差异
- [[2026-04-01_MolmoSpaces]] - 都在强化真实世界泛化，但 MolmoSpaces 偏大规模评测生态，SPF 偏 learning-free 导航范式
- [[2026-04-01_GigaWorld-Policy]] - 如果后续把 SPF 的空间 grounding 接入世界模型，可形成更强的空中任务闭环

## 📌 待探索问题

- SPF 现在主要解决导航，如果扩展到 **空中操作**，point 能否直接指向交互目标、抓取位姿或接触点？
- 它依赖 VLM 的视觉 grounding 精度，在遮挡、弱纹理和小目标条件下是否会快速退化？
- 若把 SPF 与安全约束控制/MPC 融合，能否把“开放词汇导航”升级成“带安全护栏的可部署无人机智能体”？

---
**维护**: 花火 · 2026-04-12
