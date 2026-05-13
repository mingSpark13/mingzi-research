---
title: "Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion"
authors: Xun Huang, Zhengqi Li, Guande He, Mingyuan Zhou, Eli Shechtman
arxiv: 2506.08009
date: 2025-06-10
institution: Adobe Research, UT Austin
conf: arXiv
keywords: Self-Forcing, Autoregressive Video Diffusion, KV Cache, Streaming Video
tags: ["D01"]
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2025_Self_Forcing.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["实时推理", "视频生成"]
---

## 🎯 题目
Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion

## 📝 三句摘要
1. Self-Forcing 关注自回归视频扩散模型在训练与推理之间的分布偏移问题。
2. 它通过训练时模拟推理阶段 rollout、使用 KV cache 与 video-level supervision，缩小 exposure bias。
3. 这使视频模型更接近实时、流式和长时稳定生成，是 InSpatio-World 能做“实时交互式 4D 世界模型”叙事的关键训练技术之一。

## 💎 价值评估
- **🔬 研究价值**：明确从“高质量生成”推进到“可持续 rollout 的生成系统”。
- **🚀 实践价值**：支持单卡接近实时的流式视频生成，适合系统集成。
- **📈 扩展潜力**：可作为未来世界模型、交互式视频智能体的训练范式基础。

## 🎯 可落地实验点
**实验设计**：在 Wan 基础模型上测试 Self-Forcing 式 rollout 训练是否能提升长时视频稳定性与交互延迟表现。

## 🔗 知识图谱
- [[实时推理]] - 实时流式生成是本文核心目标
- [[视频生成]] - 属于视频扩散模型训练范式改进
- FlashAttention - 与高效注意力和缓存机制有直接工程关联

## 🔗 相关链接
- [[2026-03-25_Wan_Open_and_Advanced_Large_Scale_Video_Generative_Models]] - Self-Forcing 直接构建在 Wan 类视频底模之上
- [[2026-03-19_InSpatio_WorldFM]] - InSpatio-World README 明确致谢并基于该工作
- [[2026-03-25_WorldScore]] - 长时一致性和世界性评价可用作后续评估标准

## 📌 待探索问题
- Self-Forcing 是否能从视频 rollout 推广到“世界状态 rollout”？
- KV cache 与状态锚定几何如何在同一系统中协同工作？

---
**维护**: 花火 · 2026-04-12
