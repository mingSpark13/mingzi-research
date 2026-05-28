---
title: "ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation"
authors: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang
U12.02013
date: 2025-12-01
institution: Peking University, CUHK
conf: arXiv preprint
keywords: VLA, Mixture-of-Transformers, Chain-of-Thought, 长程操作, 多模态规划
tags: ["D02", "VLA"]
domain: 通用操作
pdf_path: ../../01_论文库/世界模型/ManualVLA.pdf
reading_date: 2026-03-17
reading_status: 已读
summary: "现有VLA模型在需要明确目标终态的长程任务（乐高搭建、物体重排）中，难以协调高层规划与精细操控。"
related_concepts: ["VLA"]
---

## 🎯 题目

ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation

## 📝 三句摘要

1. **问题背景**：现有VLA模型在需要明确目标终态的长程任务（乐高搭建、物体重排）中，难以协调高层规划与精细操控。
2. **核心方法**：提出ManualVLA，基于Mixture-of-Transformers架构统一规划专家（生成图像+位置+文字的多模态操作手册）和动作专家（ManualCoT显隐结合推理），并用3DGS数字孪生自动生成训练数据。
3. **关键结果**：在RLBench 10个任务上平均成功率70%，超越π0和CoT-VLA分别7%和11%；真实场景比分层SOTA高32%。

## 💎 价值评估

- **🔬 研究价值**：首次实现"生成操作手册→指导动作"的端到端统一范式，解决了分层方法中规划与执行割裂的问题
- **🚀 实践价值**：3DGS数字孪生数据生成工具降低了数据收集成本，MoT多专家架构可扩展到其他长程任务
- **📈 扩展潜力**：ManualCoT的显隐结合推理机制可迁移到无人机复杂任务分解、人形机器人操作等领域

## 🎯 可落地实验点

**实验设计**：将ManualCoT思想应用到无人机长程任务规划
- 对比基线：传统分层规划（高层LLM规划 + 低层控制器）vs ManualVLA风格统一模型
- 度量指标：任务完成率、规划-执行一致性、总耗时
- 预期结果：统一模型在需要精确终态的任务（如精准降落、物资投递）上优于分层方案

## 🔗 知识图谱
- [[VLA]] - 视觉-语言-动作模型，本文核心架构类型
- MoE (Mixture-of-Experts) - MoT架构的基础思想
- [[长程任务规划]] - 本文要解决的核心问题
- [[世界模型]]
- [[强化学习]]
- [[空中操作]]
- [[3D高斯溅射]]
- [[长程任务规划]]
## 🔗 相关链接

- π0 - π0: Vision-Language-Action Flow Model，本文核心对比基线，ManualVLA在RLBench上超越其7%
- CoT-VLA - CoT-VLA: 结合自回归图像生成的VLA，另一核心对比方法，被超越11%
- [[2023-01_RT-2]] - RT-2: Vision-Language-Action Models，VLA领域奠基工作，本文方法论基础
- OpenVLA - OpenVLA: 开源VLA基线，本文实验中的对比方法之一

## 📌 待探索问题

- ManualCoT中显式条件（手册图文）和隐式引导（潜在表征）各自贡献多大？消融实验细节值得深挖
- 3DGS数字孪生生成的数据与真实数据的domain gap有多大？在更复杂场景（非桌面）是否仍有效？
- MoT架构的规划专家和动作专家之间的信息流是否可以做成双向的，让执行反馈也能修正规划？

---
**维护**: 花火 · 2026-04-12
