---
title: "World Action Models are Zero-shot Policies"
authors: Seonghyeon Ye, Yunhao Ge, Kaiyuan Zheng, Shenyuan Gao, Sihyun Yu, George Kurian, Suneel Indupuru, You Liang Tan, Chuning Zhu, Jiannan Xiang, Ayaan Malik, Kyungmin Lee, William Liang, Nadun Ranawaka, Jiasheng Gu, Yinzhen Xu, Guanzhi Wang, Fengyuan Hu, Avnish Narayan, Johan Bjorck
arxiv: 2602.15922
date: 2026-02-21
institution: NVIDIA GEAR Lab
conf: arXiv
keywords: DreamZero, World Action Model, Zero-shot Policy, Video Model, Robot Policy
tags: ["D01"]
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2026_DreamZero_World_Action_Models_are_Zero-shot_Policies.pdf
reading_date: 2026-03-26
reading_status: 已入库
related_concepts: ["VLA架构", "强化学习", "视频生成"]
summary: "DreamZero 把机器人策略学习重新表述为 **World Action Model (WAM)**：模型同时预测未来视频和动作，而不是只输出动作 token。 核心观点是：如果视频生成骨干已经学会了世界动态，那么在动作条件下它天然可以承担零样本策略的角色，从而在未见任务上直接执行。 论文与开源项目都强调 DreamZero 在 DROID 等基准上具有很强 zero-shot 表现，并说明视频模型骨干不只是“会生成视频”，而是可以转化为可执行机器人策略。"
---

## 🎯 题目
World Action Models are Zero-shot Policies

## 📝 三句摘要
1. DreamZero 把机器人策略学习重新表述为 **World Action Model (WAM)**：模型同时预测未来视频和动作，而不是只输出动作 token。
2. 核心观点是：如果视频生成骨干已经学会了世界动态，那么在动作条件下它天然可以承担零样本策略的角色，从而在未见任务上直接执行。
3. 论文与开源项目都强调 DreamZero 在 DROID 等基准上具有很强 zero-shot 表现，并说明视频模型骨干不只是“会生成视频”，而是可以转化为可执行机器人策略。

## 💎 价值评估
- **🔬 研究价值**：这是世界模型 / 视频模型 / 机器人策略三线汇合的重要节点，把“世界动作模型即零样本策略”明确提成方法论。
- **🚀 实践价值**：对于主人关注的 World Model × RL 路线很关键，因为它说明视频 backbone 不必只做想象器，还能直接充当 policy。
- **📈 扩展潜力**：可与 InSpatio-World、Self-Forcing、Wan 一起组成“视频基础模型 → 世界状态 → 机器人动作”的更完整路线图。

## 🎯 可落地实验点
**实验设计**：将 DreamZero 的 WAM 思想与主人现有 world model 学习路线结合，比较“只预测世界”与“世界+动作联合预测”两种方案在机器人零样本任务上的迁移差异。
- 对比基线：VLA policy、纯视频 world model、DreamZero-style WAM
- 度量指标：zero-shot success rate、任务泛化、动作时延、长时稳定性
- 预期结果：WAM 在未见任务上的策略迁移优于只做世界预测的模型

## 🔗 知识图谱
- [[世界模型]] - DreamZero 将世界建模直接推向策略执行层
- [[具身智能]] - 属于机器人可执行智能体路线的重要工作
- [[VLA]] - 可与传统 VLA policy 路线形成鲜明对比
- [[强化学习]] - 与 RL/策略学习问题直接相关
- AI智能体 - 模型不只预测，还承担可执行决策角色

## 🔗 相关链接
- [[2026-03-25_Wan_Open_and_Advanced_Large_Scale_Video_Generative_Models]] - DreamZero 背后的关键背景是视频基础模型能力的提升
- [[2026-03-25_Self_Forcing]] - 若要把视频模型做成实时可 rollout 的策略系统，训练-推理一致性问题很关键
- [[2026-03-19_InSpatio_WorldFM]] - 同样处在世界模型叙事前沿，但更偏视频世界状态而非直接策略
- [[2026-03-25_WorldScore]] - DreamZero 所在路线最终也需要“更像世界”而非“只像视频”的评价框架

## 📌 待探索问题
- DreamZero 的“动作+视频联合建模”与传统 WAM / VLA / policy model 的边界到底在哪里？
- 如果把 InSpatio-World 这类 state-anchored 4D world system 接到 DreamZero 式 WAM 上，是否能得到更强的交互式机器人策略？
- DreamZero 的 zero-shot 成功究竟更依赖视频骨干的世界知识，还是依赖数据规模与具身分布？

---
**维护**: 花火 · 2026-04-12
