---
title: AR Forcing: Towards Long-Horizon Robot Navigation World Model
authors: Yifei Yang, Zehua Fan, Huan Li, Aoqi Wang, Lida Huang, Haibao Yu, Haiyan Liu, Xuanyao Mao
arxiv: 2605.31314
date: 2026-05-29
institution: Unknown
conf: arXiv
keywords: ["world model", "navigation", "autoregressive training"]
tags: ["世界模型", "语义导航", "长程任务规划"]
summary: "把 diffusion world model 的单步损失嵌入自回归训练循环，缓解长时域导航 world model 的训练-推理分布错位。"
domain: 世界模型
pdf_path: "../../01_论文库/数据飞轮/2605.31314_AR_Forcing.pdf"
reading_date: 2026-06-01
reading_status: 已读
related_concepts: ["世界模型", "语义导航", "长程任务规划"]
---

# 📖 花火格式笔记

## 🎯 题目

AR Forcing: Towards Long-Horizon Robot Navigation World Model

## 📝 三句摘要

1. **问题背景**：指出扩散式导航世界模型常用并行监督训练、却在规划时自回归推理，训练/推理分布错位会导致长时域漂移。
2. **核心方法**：提出 AR Forcing：把单步 diffusion loss 直接嵌入自回归训练循环，让模型在训练时就吃到自己的历史预测。
3. **关键结果**：在 RECON、SCAND、HuRoN、TartanDrive 多数据集上提升长时域图像一致性与轨迹预测精度，证明长程鲁棒性更强。

## 💎 价值评估

- **🔬 研究价值**：这篇对 D05/D01 都有价值：本质是在“如何让世界模型长时域不白跑”上补了训练机制。
- **🚀 实践价值**：对主人现有 world model / VLN 长链 rollout 很实用，可直接启发 teacher-forcing→AR-forcing 的训练改造。
- **📈 扩展潜力**：如果后续要做数据飞轮，可把长时域漂移率作为新一轮数据筛选和重采样信号。

## 🎯 可落地实验点

**实验设计**：在现有导航/轨迹预测模型上加入 AR Forcing 训练环，对比 teacher forcing、scheduled sampling、AR Forcing；指标看 rollout drift、轨迹终点误差、长时域成功率。
- 对比基线：teacher forcing / 单机VLA或现有规划基线
- 度量指标：成功率、长时域漂移、协同时延/轨迹误差
- 预期结果：在闭环长时域或跨载体协作任务中更稳

## 🔗 知识图谱

- [[世界模型]] - 长时域预测主问题
- [[语义导航]] - 导航任务落地场景
- [[扩散策略]] - diffusion world model 训练范式
- [[长时程规划]] - rollout 稳定性核心指标

## 🔗 相关链接

- [[2026-05-31_WorldVLN]] - 同样关心长时域动作/世界建模

## 📌 待探索问题

- 能否把共享状态提示替换成显式协同 latent / memory？
- 长时域 rollout 的漂移信号能否反过来驱动数据飞轮筛样？

---
**维护**: 花火 · 2026-06-01
