---
title: "Preference Aligned Visuomotor Diffusion Policies for Deformable Object Manipulation"
authors: Multiple
arxiv: 2602.09583
date: 2026-02-13
institution: various
conf: arXiv
keywords: [deformable object manipulation, diffusion policy, preference alignment, visuomotor control]
tags: ["扩散策略", "模仿学习", "VLA架构"]
domain: 具身智能
pdf_path: "../../01_论文库/具身智能/2602.09583_Preference_Aligned_Visuomotor_Diffusion_Policies.pdf"
reading_date: 2026-04-22
reading_status: 已读
related_concepts: ["扩散策略", "模仿学习", "VLA架构"]
---

# 📖 花火格式笔记

## 🎯 题目

Preference Aligned Visuomotor Diffusion Policies for Deformable Object Manipulation

## 📝 三句摘要

1. **问题背景**：可变形物体操作存在多解和偏好差异，普通 diffusion policy 往往只学到平均化动作，难把“人更想要的操作轨迹”稳定学进去。
2. **核心方法**：这篇工作把 preference alignment 引入 visuomotor diffusion policy，让策略不仅拟合示范，还显式偏向更符合人类偏好的操作结果。
3. **关键结果**：论文报告该方法在 deformable manipulation 上优于常规扩散策略，说明“偏好对齐+扩散策略”对复杂接触任务有直接增益。

## 💎 价值评估

- **🔬 研究价值**：把 RLHF/偏好学习思路往机器人扩散策略迁移，是 D02 里很值得跟的训练范式分支。
- **🚀 实践价值**：对布料、线缆、软体物体这类“成功不只看终态、还看过程质量”的任务很有用。
- **📈 扩展潜力**：后续可和语言反馈、自动偏好标注、主人的空中操作/灵巧操作数据闭环结合。

## 🎯 可落地实验点

**实验设计**：在现有 manipulation 数据上加入成对偏好标签，比较 vanilla diffusion policy 与 preference-aligned diffusion policy 的轨迹质量。
- 对比基线：Diffusion Policy、ACT 类 chunking policy
- 度量指标：任务成功率、末态误差、轨迹平滑度、人工偏好胜率
- 预期结果：偏好对齐版在相近成功率下给出更稳定、更符合人类习惯的操作轨迹

## 🔗 知识图谱

- [[扩散策略]] - 核心策略建模范式
- [[模仿学习]] - 从示范与偏好信号联合学习
- [[VLA架构]] - 视觉到动作闭环控制骨架

## 🔗 相关链接

- [[2026-04-19_HiST-AT]] - 同属具身时序动作建模，可作结构化动作对比
- [[2026-04-19_Abstract_Sim2Real]] - 同期具身泛化工作，可比较数据效率与迁移能力

## 📌 待探索问题

- 偏好标签能否由 VLM 自动生成，减少人工成对标注成本？
- 该方法对刚体操作是否同样有效，还是主要受益于可变形任务的多模态性？

---
**维护**: 花火 · 2026-04-22
