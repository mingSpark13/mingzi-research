---
title: Integration of Robot and Scene Kinematics for Sequential Mobile Manipulation Planning
authors: Ziyuan Jiao, Yida Niu, Zeyu Zhang, Yangyang Wu, Yao Su, Yixin Zhu, Hangxin Liu, Song-Chun Zhu
arxiv: 2508.18627
date: 2025-08-26
institution: Beijing Institute for General Artificial Intelligence (BIGAI), Peking University, Tsinghua University
conf: T-RO 2025
keywords: Sequential mobile manipulation planning, kinematics, trajectory optimization, articulated objects, whole-body motion
tags: ["D02"]
domain: 通用操作
pdf_path: ../../01_论文库/通用操作/Integration_of_Robot_and_Scene_Kinematics.pdf
reading_date: 2026-03-18
reading_status: 在读
summary: "现有移动操作规划方法将导航和操作分离处理，难以处理长时域、多步骤的移动操作任务，尤其是与铰接物体交互的场景。"
related_concepts: ["运动控制", "全身协调运动", "任务与运动规划", "VLA架构", "空中操作"]
---

## 🎯 题目

Integration of Robot and Scene Kinematics for Sequential Mobile Manipulation Planning

## 📝 三句摘要

1. **问题背景**：现有移动操作规划方法将导航和操作分离处理，难以处理长时域、多步骤的移动操作任务，尤其是与铰接物体交互的场景。

2. **核心方法**：提出SMMP框架，通过将环境结构抽象为运动学模型并与机器人运动学整合，构建增广配置空间(A-Space)，统一导航和操作的任务约束，采用三层规划架构（任务规划→运动优化→规划精化）。

3. **关键结果**：仿真实验表明A-Space规划比基线方法任务成功率提高84.6%；真机验证涵盖7种刚体/铰接物体、17种场景、14步长时域任务。

## 💎 价值评估

- **🔬 研究价值**：
  - 首次将场景运动学纳入规划实体，而非编码特定任务约束
  - 统一了导航与操作的约束空间，为移动操作规划提供新范式
  
- **🚀 实践价值**：
  - 可应用于服务机器人、家庭助理、仓储物流等场景
  - 真机验证充分，具有较强的落地潜力
  
- **📈 扩展潜力**：
  - 可扩展到更复杂的铰接物体（如抽屉、门、多关节机械臂）
  - 可结合深度学习预测场景可达性

## 🎯 可落地实验点

**实验设计：在无人机/腿足机器人平台上验证A-Space方法**

- 对比基线：分离式导航+操作规划（TP+MP分开）
- 度量指标：任务成功率、规划时间、末端误差
- 预期结果：A-Space方法在复杂多步骤任务中成功率提升>50%

## 🔗 知识图谱
- [[运动控制]] - 场景与机器人整合的基础
- [[全身协调运动]] - 机器人base-arm协同的核心能力
- [[任务与运动规划]] - 三层规划架构
- [[VLA]]
- [[空中操作]]
- [[腿足机器人]]
## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- Kimera - 作者团队早期工作，IROS 2021版本
- [[2023-01_RT-2]] - VLA领域奠基工作
- π0 - π0: 遥操作基线对比

## 📌 待探索问题

- 问题1：A-Space的计算复杂度如何？实时性能否满足动态场景？
- 问题2：如何处理未知铰接物体的运动学建模？（当前需要预知模型）
- 问题3：能否结合视觉直接估计物体运动学参数？

---
**维护**: 花火 · 2026-04-12
