---
title: "Primitive Prompt Learning: Lifelong Reusable and Extensible Skill Primitives"
authors: Yao et al.
arxiv: 2504.00420
date: 2025-04
institution: various
conf: CVPR 2025
keywords: Primitive Prompt Learning, Lifelong Learning, Skill Primitives, Manipulation, Reusable Skills
tags: ["D02", "灵巧操作"]
domain: 通用操作
pdf_path: ../../01_论文库/具身智能/2504_PrimitivePromptLearning.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["灵巧操作"]
---

## 🎯 题目

Think Small Act Big: Primitive Prompt Learning for Lifelong Robot Manipulation (CVPR 2025)

## 📝 三句摘要

1. **问题背景**：机器人需要持续学习新技能，但现有方法无法在 lifelong setting 中高效获取和复用技能 primitive。
2. **核心方法**：Primitive Prompt Learning 让机器人在 lifelong manipulation 中自动发现、提炼、重用可扩展的技能原语（skill primitives），新技能由已有 primitives 组合生成。
3. **关键结果**：在 lifelong manipulation 任务上显著优于从零学习方法，证明了 reusable primitives 的有效性。

## 💎 价值评估

- **🔬 研究价值**：Primitive Prompt Learning 与 RoboClaw 的"skill 编排"互补——前者关注"从已有 primitive 生长新 skill"，后者关注"用好已有 primitive"。两者结合形成完整的"skill 生命周期管理"。
- **🚀 实践价值**：为机器人 lifelong learning 提供了从"调用现有 primitive"升级到"自动生长新 primitive"的路线图。
- **📈 扩展潜力**：Primitive Prompt Learning 可以与主人的 Body-Usage Adapter 结合——Body-Usage Adapter 负责"如何用身体"，Primitive Prompt Learning 负责"如何长出新技能"。

## 🔗 知识图谱

- [[灵巧操作]] - lifelong manipulation 是精细操作的延伸
- [[强化学习]] - lifelong learning 是 RL 的扩展

## 📌 待探索问题

- Primitive Prompt Learning 的 skill primitive 粒度如何确定？与主人的"意图参数"如何对应？

---
**维护**: 花火 · 2026-04-12


## 🎯 可落地实验点

**实验设计**：待补充
- 对比基线：待补充
- 度量指标：待补充
- 预期结果：待补充


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
