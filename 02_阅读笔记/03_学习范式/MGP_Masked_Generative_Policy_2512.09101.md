---
title: "Masked Generative Policy for Robotic Control"
authors: ["Lipeng Zhuang", "Shiyu Fan", "Florent P. Audonnet", "Yingdong Ru", "Edmond S. L. Ho", "Gerardo Aragon Camarasa", "Paul Henderson"]
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
tags: []
domain: 强化学习
pdf_path: "Notebook/30_论文研究/01_论文库/MGP_Masked_Generative_Policy_2512.09101.pdf"
reading_date: 待补充
reading_status: 已读
related_concepts: ["强化学习", "模仿学习", "Sim2Real"]
---

## 🎯 题目

"Masked Generative Policy for Robotic Control"

# MGP: Masked Generative Policy

## 📝 三句摘要

1. **核心创新**：把 action 变成离散 token，用 masked transformer 并行生成，再对低置信度 token 选择性精炼
2. **核心结果**：150 个 Meta-World + LIBERO 任务，+9% 平均成功率，推理速度提升 35 倍
3. **关键特性**：全局一致性预测 + 鲁棒自适应执行，支持复杂非马尔可夫任务

## 核心创新

### 架构：Masked Transformer 替代 Diffusion

**传统 Diffusion Policy**：逐步去噪，串行，推理慢

**MGP（Masked Generative Policy）**：
```
动作离散化 → 并行生成所有token → 选择性精炼低置信度token
```

**两种采样范式**：
- **MGP-Short**：并行 masked 生成 + score-based 精炼（马尔可夫任务）
- **MGP-Long**：单次预测完整轨迹 + 基于新观察动态精炼低置信度 token（非马尔可夫任务）

### 关键设计

1. **动作离散化**：把连续动作变成离散 token，便于并行
2. **置信度选择**：只精炼低置信度 token，高置信度直接过
3. **全局一致性**：所有 token 同时预测，避免误差累积

## 与 Paper A 的关系

**Paper A 低层执行控制器的候选**：

| 维度 | MGP | Paper A 需求 |
|------|-----|------------|
| 并行生成 | ✅ 全部 token 并行 | ✅ 高频控制需求 |
| 长时域 | ✅ MGP-Long 单次预测完整轨迹 | ✅ 空中轨迹规划 |
| 自适应精炼 | ✅ 低置信度token选择性精炼 | ✅ 实时安全响应 |

**迁移价值**：MGP 的「并行生成 + 选择性精炼」机制可以直接用于 Paper A 的低层执行层，替代 ACT/Diffusion Policy。

## 待探索问题

1. MGP 的离散化动作空间是否适合空中机械臂的连续控制？
2. MGP-Short 的推理速度能否满足 50-100Hz 控制频率？
3. MGP 的置信度选择机制能否与 SafeFlow 安全层结合？


## 💎 价值评估

- **🔬 研究价值**：待补充
- **🚀 实践价值**：待补充
- **📈 扩展潜力**：待补充


## 🎯 可落地实验点

**实验设计**：待补充
- 对比基线：待补充
- 度量指标：待补充
- 预期结果：待补充


## 🔗 知识图谱
- [[强化学习]]
- [[模仿学习]]
- [[Sim2Real]]


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
