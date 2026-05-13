---
title: "Training Large Language Models to Reason in a Continuous Latent Space"
authors: ["Shibo Hao", "et al."]
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
tags: []
domain: 强化学习
pdf_path: "Notebook/30_论文研究/01_论文库/Coconut_CoT_Continuous_Thought_2412.06769.pdf"
reading_date: 待补充
reading_status: 已读
related_concepts: ["强化学习", "模仿学习", "Sim2Real"]
---

## 🎯 题目

"Training Large Language Models to Reason in a Continuous Latent Space"

# Coconut: Chain of Continuous Thought

## 📝 三句摘要

1. **核心问题**：LLM 在语言空间中进行 CoT 推理并非最优，许多词 token 只保证文本连贯性而非推理本身，关键 token 反而需要复杂规划
2. **核心贡献**：提出 Coconut——把 LLM 最后一层隐状态作为「连续思维」，不解码成文字，而是直接反馈给模型作为下一步输入嵌入，在连续空间中进行推理
3. **核心发现**：连续思维可以编码多个可选的下一步路径，实现类似 BFS 的搜索而非 CoT 的确定性单一路径，在需要大规模搜索的逻辑推理任务上超越 CoT

## 核心创新

**传统 CoT**：
```
问题 → 语言 token → 语言 token → 语言 token → 答案
       (逐个生成，每个 token 是确定的)
```

**Coconut（连续思维）**：
```
问题 → 连续隐状态 h₁ → 连续隐状态 h₂ → ... → 解码输出答案
       (不解码成词，每个隐状态可编码多条备选路径)
```

**关键机制**：
- 用 LLM 最后一层 hidden state 作为"连续思维"
- 连续思维反馈给模型作为下一层输入 embedding
- 连续思维可以同时编码多个 alternative next steps → 实现 BFS 搜索

## 与主人研究方向的关系

- **Paper A 高层 VLM 意图层**：VLM 输出模糊意图而非直接 action
- Coconut 的思想类似——不在「语言空间」（等于 Paper A 的「动作空间」）逐个 token 生成，而是在「连续隐空间」进行高层规划
- 可迁移点：Paper A 的 VLM 意图层是否也可以借鉴 Coconut，在连续隐空间做多路径搜索而非直接解码成确定 action？

## 🔗 相关链接

- [arXiv 原文](https://arxiv.org/abs/2412.06769)
- [Coconut GitHub](https://github.com/)

## 待探索问题

1. Coconut 的连续思维和 Paper A 的「VLM 意图层」如何结合？
2. 连续思维的多路径 BFS 特性是否可以迁移到机械臂操作的层次化解码上？
3. 训练 cost 如何？在线推理时延是否可控？


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


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
