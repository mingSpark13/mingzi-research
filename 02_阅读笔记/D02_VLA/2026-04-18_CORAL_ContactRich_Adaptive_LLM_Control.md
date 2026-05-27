---
title: "CORAL: Contact-Rich Adaptive LLM-Based Control for Robotic Manipulation"
authors: "Anonymous (ICLR 2026 double-blind review)"
arxiv: ""
date: "2026-01"
institution: "Anonymous"
conf: "ICLR 2026 (Under Review)"
keywords: ["LLM", "VLA", "MPPI", "Contact-Rich Manipulation", "Adaptive Control"]
tags: ["VLA架构", "MPC", "LLM驱动机器人", "灵巧操作", "强化学习"]
domain: 具身智能
pdf_path: ""  # OpenReview 需认证，PDF 无法直接下载，待补充
reading_date: 2026-04-18
reading_status: 在读
related_concepts: ["VLA架构", "MPC"]
summary: "VLA 系统依赖大量遥操作数据训练的固定动作集合，黑盒结构导致缺乏适应性和可解释性，在复杂动态接触场景中效果受限。"
---

# 📖 花火格式笔记

## 🎯 题目

CORAL: Contact-Rich Adaptive LLM-Based Control for Robotic Manipulation

## 📝 三句摘要

1. **问题背景**：VLA 系统依赖大量遥操作数据训练的固定动作集合，黑盒结构导致缺乏适应性和可解释性，在复杂动态接触场景中效果受限。
2. **核心方法**：CORAL 提出模块化框架，将 VLM 估计的物理参数（6-DoF 物体位姿）传入 MPPI（Model Predictive Path Integral）控制器；LLM 担任双重角色——任务初始化（Task Formulation）和在线自适应（Online Adaptation），分别输出初始 cost J₀/constraint C₀ 和更新版 Jₜ/Cₜ；Memory Unit 提供经验检索。
3. **关键结果**：模块化解耦了高层推理和低层控制，VLM 提供实时物理参数，MPPI 负责反应式执行。

## 💎 价值评估

- **🔬 研究价值**：明确了 LLM × MPC 的"LLM 定义 cost/constraint + MPPI 执行"接口分工，是目前最清晰的 MPC-as-executor 接口设计。
- **🚀 实践价值**：适合接触丰富的机械臂操作场景，VLM 实时估计物理参数让 MPC 能适应动态变化。
- **📈 扩展潜力**：LLM 的双重角色（初始化+在线自适应）可迁移到无人机场景；MPPI 可替换为其他 MPC 方法。

## 🎯 可落地实验点

**实验设计**：将 CORAL 框架迁移到无人机接触任务（如无人机精确抓取、空中充电插拔）
- 对比基线：纯 VLA policy、无自适应 MPC、LLM-only 规划
- 度量指标：任务成功率、LLM 在线自适应频率、对动态障碍的适应能力
- 预期结果：CORAL 应在动态场景显著优于纯 VLA，LLM 自适应开销 <50ms

## 🔗 知识图谱

- [[concepts/VLA架构]] - VLM 是物理参数估计器，不直接输出动作
- [[concepts/MPC]] - MPPI 是执行器，LLM 输出 cost/constraint 而非直接生成动作
- [[concepts/LLM驱动机器人]] - LLM 担任双重角色（初始化+在线自适应）
- [[concepts/灵巧操作]] - 接触丰富场景的机械臂操作是本文应用场景
- [[concepts/强化学习]] - Memory Unit 检索经验可类比 RL 中的经验回放

## 🔗 相关链接

- [[2025-01-08_LLMPC]] - LLMPC 是 LLM 生成候选 + 外部打分，CORAL 是 LLM 定义 cost + MPPI 执行
- [[2026-03-25_MPCwithDiffWorldModel]] - 同属推理时 MPC 优化方向

## 📌 待探索问题

- CORAL 的 LLM 在线自适应频率和计算开销如何？能否满足无人机实时控制？
- MPPI 的采样分布如何设计？LLM 能否引导 MPPI 的采样方向而非只输出 cost？
- Contact-VLA 与 CORAL 的关系：CORAL 是 Contact-VLA 的核心模块？

---
**维护**: 花火 · 2026-04-18
