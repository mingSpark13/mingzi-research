---

title: "Three-Step Nav: A Hierarchical Global-Local Planner for Zero-Shot Vision-and-Language Navigation"
authors: Wanrong Zheng, Yunhao Ge, Laurent Itti
arxiv: 2604.26946
date: 2026-04-29
institution: University of Southern California
conf: AISTATS 2026
keywords: [vision-language navigation, zero-shot planning, multimodal large language models, hierarchical planner]
tags: [语义导航, 长程任务规划, 零样本泛化, LLM驱动机器人]
summary: "Three-Step Nav 用前看, 现看, 回看三阶段层次规划协议增强零样本 VLN，在几乎零训练开销下提升长程导航稳定性。"
domain: 语义导航
pdf_path: "../../01_论文库/语义导航/2604.26946_ThreeStepNav.pdf"
reading_date: 2026-05-03
reading_status: 已读
related_concepts: ["语义导航", "长程任务规划", "零样本泛化", "LLM驱动机器人"]
---

# 📖 花火格式笔记

## 🎯 题目

Three-Step Nav: A Hierarchical Global-Local Planner for Zero-Shot Vision-and-Language Navigation

## 📝 三句摘要

1. **问题背景**：零样本 VLN 虽然能借助多模态大模型直接导航，但常见问题是中途跑偏、过早停下、长程目标一致性差。
2. **核心方法**：论文提出“三步看”层次规划协议——先向前看提取全局地标与粗计划，再对齐当前视角与子目标，最后回看整段轨迹做纠偏。
3. **关键结果**：在 R2R-CE 和 RxR-CE 上，Three-Step Nav 以几乎零训练开销插入现有 VLN 流水线，取得 SOTA 的零样本性能。

## 💎 价值评估

- **🔬 研究价值**：它不是再训一个重模型，而是把 VLN 失败模式拆成“全局规划/局部对齐/终局审计”三段，结构很适合迁到空中导航任务里。
- **🚀 实践价值**：主人如果做无人机语言导航，这种低改造成本的 planner wrapper 很适合作为现有 VLM/VLA 系统上的增强层。
- **📈 扩展潜力**：可继续接入记忆、场景图谱、飞行安全约束，演化成更稳的长程 embodied planner。

## 🎯 可落地实验点

**实验设计**：把 Three-Step Nav 的“前看-现看-回看”协议移植到空中 VLN / UAV 路线跟随任务，验证是否能改善长程偏航与提前终止。
- 对比基线：单阶段 VLM 逐步决策、层次化导航基线 HTNav
- 度量指标：Success Rate、SPL、偏航恢复率、提前终止率
- 预期结果：分阶段审计机制能显著降低长程漂移，并提升零样本复杂指令成功率

## 🔗 知识图谱

- [[语义导航]] - 论文核心任务类型
- [[长程任务规划]] - 三阶段协议本质上是长程规划与纠偏框架
- [[零样本泛化]] - 不做额外训练直接提升导航表现
- [[LLM驱动机器人]] - 以 MLLM 作为高层感知-规划核心

## 🔗 相关链接

- [[2026-04-20_ReasoningSystemsSemanticNavigation]] - 同样关注语义导航，但前者偏显式知识推理，这篇偏 MLLM 零样本规划
- [[2026-04-16_HTNav]] - 可对比层次化导航思想在空中场景中的落地方式

## 📌 待探索问题

- 三步协议若迁到无人机平台，如何把动力学与避障安全约束显式注入“回看纠偏”阶段？
- 这种无训练增强方式在开放场景下是否会受 MLLM 视觉误识别与上下文长度限制拖累？

---
**维护**: 花火 · 2026-05-03
