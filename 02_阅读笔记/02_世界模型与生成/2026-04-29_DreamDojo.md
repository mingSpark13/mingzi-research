---
title: "DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos"
authors: Shenyuan Gao, William Liang, Kaiyuan Zheng, Ayaan Malik, Seonghyeon Ye, Sihyun Yu, Wei-Cheng Tseng, Yuzhu Dong, Kaichun Mo, Chen-Hsuan Lin, Qianli Ma, Seungjun Nah, et al.
arxiv: 2602.06949
date: 2026-02-06
institution: NVIDIA, Carnegie Mellon University, UC Berkeley, Stanford等
conf: arXiv
keywords: [world model, human videos, latent actions, robot manipulation, video prediction]
tags: ["隐空间世界模型", "动作条件预测", "视频生成", "零样本泛化", "具身智能"]
summary: "DreamDojo 用大规模第一视角人类视频预训练 latent-action 世界模型，再用少量机器人数据后训练适配开放场景机器人任务。"
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2602.06949_DreamDojo.pdf"
reading_date: 2026-04-29
reading_status: 已读
related_concepts: ["隐空间世界模型", "动作条件预测", "视频生成", "零样本泛化", "具身智能"]
---

# 📖 花火格式笔记

## 🎯 题目

DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

## 📝 三句摘要

1. **问题背景**：机器人世界模型在灵巧操作和开放环境里常被数据覆盖不足、动作标签稀缺卡住，难以学到能泛化的动力学。
2. **核心方法**：DreamDojo 用 4.4 万小时第一视角人类视频做预训练，引入连续 latent action 作为统一代理动作，再用少量目标机器人数据后训练适配，并蒸馏到 10.81 FPS 实时版本。
3. **关键结果**：方法在多项 OOD benchmark 上验证了更强的物理理解、动作可控性与开放场景生成能力，可直接支持遥操作、策略评估和基于模型的规划。

## 💎 价值评估

- **🔬 研究价值**：把“大规模人类视频 + latent action world model”真正拉到 foundation model 级别，是 D01 世界模型主线里很关键的一步。
- **🚀 实践价值**：对主人后续想做的开放环境预测、低成本预训练、世界模型辅助规划都很有参考价值，尤其适合数据稀缺机器人任务。
- **📈 扩展潜力**：可继续追问 latent action 是否能迁移到 UAV / aerial manipulation，以及蒸馏后实时模型能否嵌入闭环控制链路。

## 🎯 可落地实验点

**实验设计**：复现“人类视频预训练 + 机器人小样本后训练”的两阶段路线，验证对特定机器人任务的 sample efficiency 提升。
- 对比基线：纯机器人数据训练的 video world model、无 latent action 版本
- 度量指标：OOD rollout 一致性、任务成功率、视频预测误差、规划成功率
- 预期结果：大规模人类视频预训练应在低数据 regime 下显著提升泛化与可控性

## 🔗 知识图谱

- [[concepts/隐空间世界模型]] - 用 latent action 与统一隐空间承载动力学学习
- [[concepts/动作条件预测]] - 以代理动作条件驱动未来状态/视频预测
- [[concepts/视频生成]] - 世界模型输出具备开放场景生成与多任务预测能力
- [[concepts/零样本泛化]] - 强调对未见物体与环境的泛化
- [[concepts/具身智能]] - 服务真实机器人交互与规划闭环

## 🔗 相关链接

- [[2026-04-20_AdaWorld]] - 同属机器人 world model / latent action 路线，可作对照
- [[2026-04-20_Cosmos_Predict2.5]] - 文中用于评测生成质量与开放场景预测能力的重要参照
- [[2026-04-20_VAP]] - 将统一代理动作引入异构 embodied data 的相关基础工作

## 📌 待探索问题

- latent action 这套统一代理动作，迁到无人机轨迹/控制 token 上还能保持可控性吗？
- 10.81 FPS 的蒸馏版本能否直接进 MPC / replanning 闭环，而不是只做离线评估？

---
**维护**: 花火 · 2026-04-29
