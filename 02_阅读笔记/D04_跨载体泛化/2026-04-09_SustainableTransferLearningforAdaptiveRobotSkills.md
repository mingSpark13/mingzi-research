---
title: Sustainable Transfer Learning for Adaptive Robot Skills
authors: Benjamin N. Parks, Giovanna M. Bledsoe, Dylan A. Shell, Rafael Fierro
arxiv: 2604.06943
date: 2026-04-09
institution: University of New Mexico
conf: arXiv
keywords: [跨载体泛化, 通用操作, 迁移学习, 机械臂]
tags: []
domain: 跨载体泛化
pdf_path: "../../01_论文库/跨载体泛化/2604.06943_Sustainable_Transfer_Learning_for_Adaptive_Robot_Skills.pdf"
reading_date: 2026-05-03
reading_status: 已读
related_concepts: ["跨载体泛化", "模仿学习"]
---

# 📖 花火格式笔记

## 🎯 题目

Sustainable Transfer Learning for Adaptive Robot Skills

## 📝 三句摘要

1. **问题背景**：跨机器人技能迁移常在新平台上迅速遗忘旧技能，尤其在少样本微调时容易出现适应性与可持续性冲突。
2. **核心方法**：论文围绕 UR5e 与 Panda 机械臂上的 peg-in-hole 等操作任务，分析并设计更可持续的 transfer learning 流程，强调在目标平台适配时保住源平台技能。
3. **关键结果**：结果表明合理的迁移/微调策略能兼顾新平台适应与旧技能保留，适合作为跨载体泛化方向里“低成本目标平台锚点 + 可持续适配”证据。

## 💎 价值评估

- **🔬 研究价值**：直接命中 D04 跨载体泛化的核心痛点，不是只看一次 transfer 成功，而是看适配后是否还能持续保留跨平台能力。
- **🚀 实践价值**：对主人未来“地面机械臂经验迁到空中机械臂/其他机械臂”很有参考价值，尤其适合少量真机锚点场景。
- **📈 扩展潜力**：可与 D04 现有的 latent interface、paired demo、morphology-aware compensation 组合，变成“先统一接口，再可持续微调”的实验轴。

## 🎯 可落地实验点

**实验设计**：在主人现有跨载体实验中加入“迁移后旧技能保留率”指标，比较 full finetune、adapter、冻结 backbone+小头微调三种方案。
- 对比基线：full finetune / LoRA-adapter / frozen encoder + task head
- 度量指标：目标平台成功率、源平台保留成功率、双平台平均分
- 预期结果：小参数适配或结构化 adapter 能比全量微调更稳地平衡迁移增益与遗忘

## 🔗 知识图谱

- [[跨载体泛化]] - 核心问题定义
- [[通用操作]] - 任务落点
- [[模仿学习]] - 迁移学习常用前序范式

## 🔗 相关链接

- [[2026-04-15_Gupta2026_KinematicIntelligence]] - 都关注跨机器人技能迁移，但本篇更强调适配后的可持续保留

## 📌 待探索问题

- 少量目标载体数据下，adapter 是否优于 full finetune？
- 可持续迁移指标能否和 morphology-aware residual 一起建统一评测？

---
**维护**: 花火 · 2026-05-03
