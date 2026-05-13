---
title: "Gated Memory Policy: Adaptive Memory for Robotic Manipulation"
authors: Yihuai Gao, Jinyun Liu et al.
arxiv: 2604.18933
date: 2026-04-21
institution: （待补充）
conf: arXiv
keywords: ["gated memory", "robot manipulation", "non-markovian", "memory mechanism"]
tags: [具身智能, 规划与控制, 长程任务规划, 强化学习]
domain: 具身智能
pdf_path: "../../01_论文库/具身智能/2604.18933_GatedMemoryPolicy.pdf"
reading_date: 2026-04-22
reading_status: 已读
related_concepts: ["规划与控制", "长程任务规划", "强化学习", "主动感知"]
---

# 📖 花火格式笔记

## 🎯 题目

Gated Memory Policy: Adaptive Memory for Robotic Manipulation

## 📝 三句摘要

1. **问题背景**：机器人操作任务对历史信息的依赖程度不同（Markovian vs 非马尔可夫），现有方法使用固定长度的记忆机制，导致记忆浪费或不足。
2. **核心方法**：本文提出门控记忆策略（Gated Memory Policy），通过可学习的门控机制自适应调节记忆长度，对需要长期历史的任务保留更多上下文，对简单任务则压缩记忆。
3. **关键结果**：在多种机器人操控任务中，门控记忆策略相比固定记忆基线在长程任务上成功率显著提升，同时计算效率更高。

## 💎 价值评估

- **🔬 研究价值**：对无人机时序建模（GRU/Transformer）有直接参考价值，可借鉴门控机制动态分配记忆资源。
- **🚀 实践价值**：可应用于无人机轨迹预测和飞行控制中的时序建模，自适应记忆长度能更好地处理突发障碍和动态目标。
- **📈 扩展潜力**：门控机制可与 Transformer 结合，用于多模态输入（视觉 + IMU + 激光雷达）的长程记忆建模。

## 🎯 可落地实验点

**实验设计**：门控记忆机制应用于无人机轨迹跟踪控制器
- 对比基线：固定长度历史窗口的 LSTM 控制器、无记忆的 MPC 基线
- 度量指标：轨迹跟踪误差、计算延迟、突发障碍处理成功率
- 预期结果：门控记忆控制器在 10Hz 控制频率下跟踪误差降低 15%，突发障碍处理成功率提升 25%

## 🔗 知识图谱

- [[规划与控制]] - 门控记忆用于机器人控制决策
- [[长程任务规划]] - 自适应记忆长度支撑长程任务执行
- [[强化学习]] - 门控机制通过强化学习训练
- [[主动感知]] - 记忆门控本质上是一种信息选择性感知

## 🔗 相关链接

- [[2026-04-22_Mask_World_Model]] - Mask World Model 的选择性预测与本文门控记忆有相似思想，可对比
- [[2026-04-22_Gated_Memory_Policy]] - TBD（本文自身引用）

## 📌 待探索问题

- 门控机制在高速无人机飞行场景下是否来得及在控制周期内完成门控计算？
- 如何将视觉记忆和状态记忆统一建模在同一门控框架下？

---
**维护**: 花火 · 2026-04-22
