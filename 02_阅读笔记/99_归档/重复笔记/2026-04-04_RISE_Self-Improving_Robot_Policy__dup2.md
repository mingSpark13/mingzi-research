---
title: Self-Improving Robot Policy with Compositional World Model
authors: Jiazhi Yang, Kunyang Lin, Jinwei Li, Wencong Zhang, Tianwei Lin, Longyan Wu, Zhizhong Su, Hao Zhao, Ya-Qin Zhang, Li Chen, Ping Luo, Xiangyu Yue, Hongyang Li
arxiv: 2602.11075
date: 2026-02-11
institution: 待补充
conf: arXiv
keywords: World Model, Reinforcement Learning, VLA, Robotic Manipulation, Compositional World Model, Imaginary RL
tags: ["D02", "世界模型", "强化学习", "VLA", "灵巧操作"]
summary: 组合世界模型将未来预测与进度价值评估解耦，使机器人策略能在想象空间中自我改进，并在真实接触密集操作上显著提升成功率。
domain: 通用操作
pdf_path: ../../01_论文库/通用操作/RISE_2602.11075.pdf
reading_date: 2026-04-04
reading_status: 已读
related_concepts: ["强化学习", "灵巧操作"]
---

## 🎯 题目

Self-Improving Robot Policy with Compositional World Model

## 📝 三句摘要

1. **问题背景**：尽管 Vision-Language-Action (VLA) 模型在规模和训练数据上持续扩展，但在需要接触密集和动态操作的任务中仍然表现脆弱——微小的执行偏差会累积导致失败，而物理世界的强化学习受限于安全风险、硬件成本和环境重置。
2. **核心方法**：本文提出 RISE 框架，通过组合世界模型（Compositional World Model）在"想象空间"中进行机器人强化学习。该世界模型包含两部分：(i) 可控动力学模型预测多视角未来，(ii) 进度价值模型评估想象中的结果，生成用于策略改进的优势信号。
3. **关键结果**：RISE 在三个真实世界任务上显著超越 prior art：动态砖块分类 +35%、背包 packing +45%、盒子关闭 +35%。

## 💎 价值评估

- **🔬 研究价值**：首次提出组合世界模型解耦状态预测与价值评估两大功能，允许两者使用最适合的架构和目标独立优化，为世界模型在机器人 RL 中的应用提供了新范式。
- **🚀 实践价值**：完全在想象空间中进行策略更新，无需物理交互，大幅降低机器人技能训练的成本和风险，可直接部署到真实机器人。
- **📈 扩展潜力**：组合设计可推广到其他 VLA 框架；想象空间自我改进机制可与 Real2Sim2Real 结合；价值模型可独立作为机器人操作的成功检测器。

## 🎯 可落地实验点

**实验设计**：将 RISE 的组合世界模型思想迁移到空中操作场景
- 对比基线：原始 VLA 策略（无世界模型想象增强）、仅用动力学模型的想象增强
- 度量指标：任务成功率（5 次平均）、执行偏差累积曲线、策略更新收敛速度
- 预期结果：组合世界模型版本在动态抓取任务上比无增强基线提升 >25%，比单一模型版本提升 >10%

## 🔗 知识图谱

- [[VLA]] - 视觉-语言-动作统一模型，本文处理的核心任务类型
- [[世界模型]] - 组合世界模型是本文的核心方法，用于在想象中预测和评估
- [[强化学习]] - RISE 在想象空间中进行 RL 策略改进
- [[Sim2Real]] - 物理世界 RL 受限是本文解决的问题，RISE 通过想象空间规避
- [[机器人策略分类]] - 本文属于 Transformer 骨干 + RL 动作生成的范式

## 🔗 相关链接

- [[2024-10_pi0]] - π0: 物理世界 VLA+RL 的 prior art，RISE 在想象中做 RL 克服了其物理交互成本高的问题
- [[2023_RT-2]] - RT-2: VLA 领域奠基工作，本文问题背景和架构基础

## 📌 待探索问题

- RISE 的组合世界模型如何与空中操作的快速动力学特性兼容？价值模型在无人机高速运动场景下的预测精度是否会显著下降？
- 组合世界模型中动力学模型和价值模型各自的训练数据来源和规模要求是什么？能否从已有的操作数据集（如 Brinkhoff 数据）中迁移？

---
**维护**: 花火 · 2026-04-12
