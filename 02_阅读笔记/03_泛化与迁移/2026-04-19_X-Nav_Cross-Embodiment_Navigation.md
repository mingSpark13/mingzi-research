---
title: X-Nav: Learning End-to-End Cross-Embodiment Navigation for Mobile Robots
authors: Haitong Wang, Aaron Hao Tan, Angus Fung, Goldie Nejat
arxiv: 2507.14731
date: 2025-07-19
institution: University of Toronto
conf: arXiv
keywords: [Cross-Embodiment, Navigation, Mobile Robots, Policy Learning, Generalization]
tags: ["跨载体泛化", "动作空间统一", "语义导航", "零样本泛化", "具身智能"]
domain: 跨载体泛化
pdf_path: "../../01_论文库/跨载体泛化/2507.14731_X-Nav_Cross-Embodiment_Navigation.pdf"
reading_date: 2026-04-19
reading_status: 待读
related_concepts: ["跨载体泛化", "动作空间统一", "语义导航", "零样本泛化", "具身智能"]
---

## 🎯 题目

X-Nav: Learning End-to-End Cross-Embodiment Navigation for Mobile Robots

## 📝 三句摘要

1. **问题背景**：导航策略通常强依赖特定机器人形态与传感器接口，换平台后往往需要重新训练，限制了移动机器人策略的复用与扩展。
2. **核心方法**：X-Nav 试图学习一个可跨多种 mobile robot embodiment 直接部署的统一导航策略，让不同机器人共享同一套 end-to-end 导航模型。
3. **关键结果**：论文表明跨 embodiment 统一策略在移动机器人导航上是可行的，价值不只在性能本身，更在于它把“策略从具体机体解耦”这件事往前推了一步。

## 💎 价值评估

- **🔬 研究价值**：这篇和主人做 UAV / 跟随 / 泛化控制的关系很近，因为它关注的不是单一导航性能，而是不同 embodiment 之间的迁移与共享，这正是更大一层的泛化问题。
- **🚀 实践价值**：如果主人后面要从地面移动机器人经验迁到无人机，或者想做统一感知接口 + 平台适配层，这篇会提供很好的 framing。
- **📈 扩展潜力**：它可以和 PMI、动作空间统一、跨载体泛化评测基准这些主题串起来，成为主人“跨平台机器人智能”路线的参考拼图。

## 🎯 可落地实验点

**实验设计**：做一个轻量版跨载体导航统一接口实验
- 对比基线：单平台独立训练策略 / 共享 backbone + 平台 adapter / 完全统一策略
- 度量指标：跨平台零样本成功率、微调样本效率、路径长度、碰撞率
- 预期结果：共享表征 + 小型平台适配头会比完全独立训练更高效，也比硬统一动作接口更稳

## 🔗 知识图谱

- [[concepts/跨载体泛化]] - 论文核心主题
- [[concepts/动作空间统一]] - 不同平台共享策略的关键接口问题
- [[concepts/语义导航]] - 导航任务的一种高层任务定义方式
- [[concepts/零样本泛化]] - 跨平台直接部署时关注的能力
- [[concepts/具身智能]] - 所属的大框架

## 🔗 相关链接

- [[2026-04-19_VLA_Survey_Embodied_AI]] - 从总览角度理解 embodied policy 的统一趋势
- [[2026-03-27_OpenVLA]] - 参考统一策略架构的开放实现思路
- [[2026-04-08_WowWoVal_EmbodiedWorldModel]] - 若后续想把 world model 融入 cross-embodiment 评测，可搭配阅读

## 📌 待探索问题

- 移动机器人之间的 cross-embodiment 方法，迁到无人机这类动力学差异更大的平台时，哪些表征还能保留？
- 统一策略到底该统一到 observation space、latent space，还是 action interface 这一层，哪层最适合作为主人后续研究切入口？

---
**维护**: 花火 · 2026-04-19
