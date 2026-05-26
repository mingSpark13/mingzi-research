---
title: 'RoboGuard: Safety Guardrails for LLM Robots'
authors: UPenn Vijay Kumar Team
arxiv: '2503.07885'
date: 2025-03
institution: University of Pennsylvania
conf: '2025'
keywords: LLM Robot, Safety Guardrails, Jailbreak Attack, Temporal Logic, Embodied AI
tags:
- 任务与运动规划
- LLM驱动机器人
- 具身智能
domain: 通用操作
pdf_path: ../../01_论文库/通用操作/RoboGuard_Safety_Guardrails_for_LLM_Robots.pdf
reading_date: '2026-03-18'
reading_status: 在读
summary: RoboGuard 通过“可信根”LLM + 时序逻辑控制合成，把 LLM 机器人规划中的危险行为执行率从 92% 降到 3% 以下。
related_concepts:
- 任务与运动规划
- LLM驱动机器人
- 具身智能
---
## 🎯 题目

RoboGuard: Safety Guardrails for LLM Robots

## 📝 三句摘要

1. **问题背景**：大语言模型(LLM)成为机器人决策规划的重要组件，但存在幻觉、越狱攻击等安全问题，可能引发危险行为。

2. **核心方法**：提出两阶段安全护栏架构——①"可信根"LLM将安全规则与环境语义对齐，通过CoT生成时序逻辑约束；②时序逻辑控制合成验证修正机器人规划。

3. **关键结果**：模拟与真机实验中，危险行为执行率从92%降低到3%以下，同时保持任务性能，对自适应越狱攻击具有鲁棒性。

## 💎 价值评估

- **🔬 研究价值**：
  - 首个针对LLM机器人安全护栏的工程化解决方案
  - 将时序逻辑控制引入LLM安全领域
  
- **🚀 实践价值**：
  - 可直接部署到现有LLM机器人系统
  - 兼容真实机器人实验验证
  
- **📈 扩展潜力**：
  - 可扩展到多模态LLM机器人
  - 可结合其他安全机制（对抗训练、规则引擎）

## 🎯 可落地实验点

**实验设计：在无人机/机器人平台上验证RoboGuard安全护栏**

- 对比基线：无护栏的LLM规划器
- 度量指标：危险行为执行率、任务成功率
- 预期结果：危险行为降低>80%

## 🔗 知识图谱
- [[任务与运动规划]] - 本文核心贡献
- [[任务与运动规划]] - 本文使用的技术手段
- [[空中操作]]
- [[长程任务规划]]
## 🔗 相关链接

- [[2026-03-18_Integration_of_Robot_and_Scene_Kinematics]] - 同年T-RO工作，机器人规划领域

## 📌 待探索问题

- 问题1：如何平衡安全性与任务灵活性？过度限制是否会影响正常任务执行？
- 问题2：时序逻辑约束的自动生成如何应对未知场景？

---
**维护**: 花火 · 2026-04-12
