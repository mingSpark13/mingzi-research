---
title: Learning Adaptive Cross-Embodiment Visuomotor Policy with Contrastive Prompt Orchestration
authors: Yuhang Zhang, Chao Yan, Yu Jiaxi, Jiaping Xiao, Mir Feroskhan
arxiv: 2602.01040
date: 2026-02-01
institution: Nanyang Technological University, Nanjing University of Aeronautics and Astronautics
conf: arXiv
keywords: [cross-embodiment, visuomotor policy, contrastive learning, prompt orchestration]
tags: [跨载体泛化, 零样本泛化, 模仿学习]
domain: 跨载体泛化
pdf_path: "../../01_论文库/D03_空地迁移/2602.01040_Adaptive_Cross-Embodiment_Visuomotor_Policy.pdf"
reading_date: 2026-04-20
reading_status: 已读
related_concepts: ["跨载体泛化", "零样本泛化", "模仿学习"]
---

# 📖 花火格式笔记

## 🎯 题目

Learning Adaptive Cross-Embodiment Visuomotor Policy with Contrastive Prompt Orchestration

## 📝 三句摘要

1. **问题背景**：跨载体 visuomotor policy 容易把光照、FOV、旋转等 domain factor 和任务本身混在一起，导致在新 embodiment 或新环境下零样本失效。
2. **核心方法**：论文提出 CAPO，用视觉/时间动作/文本三重对比目标学习 prompt pool，再用自适应 orchestration 按当前观测动态聚合 prompt，构造更适合当前 embodiment 的状态表示。
3. **关键结果**：CAPO 在跨光照、跨视角和跨 embodiment 的 unseen target domain 上显著优于常规 end-to-end 与静态表征基线，同时提升 sample efficiency 和零样本适应能力。

## 💎 价值评估

- **🔬 研究价值**：这篇很贴 D03/D04 交界，核心不是单纯 domain randomization，而是把“domain factor 解耦 + 动态提示调度”系统化，值得跟主人现有跨载体泛化思路对照。
- **🚀 实践价值**：prompt orchestration 适合接到无人机/UGV 的视觉策略前端，先压制视场差异、光照差异，再把更干净的状态喂给 policy。
- **📈 扩展潜力**：若把 prompt 条件从视觉 domain factor 扩到动力学、几何状态、PMI packet 等，可形成更强的跨平台泛化接口。

## 🎯 可落地实验点

**实验设计**：在空地迁移或跨载体实验里加一个 domain-prompt 模块，对 FOV/illumination/rotation 做动态 prompt 选择。
- 对比基线：domain randomization、普通对比表征、静态 prompt encoder
- 度量指标：zero-shot success rate、样本效率、目标域收敛速度、跨平台性能跌幅
- 预期结果：动态 prompt orchestration 能比静态表征更稳地隔离 domain factor，在 unseen embodiment 上明显减小性能塌缩

## 🔗 知识图谱

- [[跨载体泛化]] - 论文核心任务就是跨 embodiment 适配
- [[零样本泛化]] - 强调 unseen target domain 的零样本表现
- [[模仿学习]] - 作为相关策略学习范式与可对比路线

## 🔗 相关链接

- [[2026-04-18_MiniUGV2]] - 同属跨平台/跨载体迁移相关工作，可对照其平台侧建模与 CAPO 的表征侧解法
- [[2026-04-19_X-Nav_Cross-Embodiment_Navigation]] - 已入库跨载体导航工作，可比较 navigation 与 visuomotor policy 的泛化接口差异
- [[2026-04-19_Abstract_Sim2Real]] - 与 Sim2Real 方向相邻，适合比较 domain gap 缓解手段是否可叠加

## 📌 待探索问题

- prompt pool 能否直接条件化机器人几何参数、动力学参数或 PMI packet，而不只依赖视觉线索？
- 如果把 CAPO 接到 VLA 或空中 VLN 上，动态 prompt 是否还能保持实时性并稳定提升 zero-shot 泛化？

---
**维护**: 花火 · 2026-04-20
