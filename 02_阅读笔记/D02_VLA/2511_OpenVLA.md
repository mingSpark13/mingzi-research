---
title: "OpenVLA: Open-Source Vision-Language-Action Model for Robot Manipulation"
authors: Kim et al. (Stanford / TRI)
arxiv: 2511.10518
date: 2025-11
institution: Stanford / Toyota Research Institute
conf: arXiv / ICLR 2025
keywords: VLA, Open Source, Autoregressive, Language-Conditioned, Generalist Policy
tags: ["D02", "VLA"]
domain: 具身智能
pdf_path: ../../01_论文库/具身智能/2511_OpenVLA.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["VLA"]
---

## 🎯 题目

OpenVLA: Open-Source Vision-Language-Action Model for Robot Manipulation

## 📝 三句摘要

1. **问题背景**：RT-2 等 VLA 虽强但闭源；需要一个完全开源、可复现、适合研究社区的通用 manipulation VLA 基线。
2. **核心方法**：OpenVLA 是 7B 参数开源 VLA，训练在 970k real-world robot demonstrations 上，autoregressive 预测离散动作 token，支持语言指令。
3. **关键结果**：在 29 个任务、多 robot embodiment 上，绝对成功率比 RT-2-X 高 16.5%，在多任务语言泛化上比 Diffusion Policy 高 20.4%。

## 💎 价值评估

- **🔬 研究价值**：OpenVLA 是目前最强的开源通用 manipulation VLA 基线，完全可复现、微调方便，是研究起点的首选。
- **🚀 实践价值**：开源 7B 模型权重和训练代码，适合主人做具身方向研究的 baseline。
- **📈 扩展潜力**：可与主人的 world model 方向结合，构建"OpenVLA + world model"的具身 agent。

## 🎯 可落地实验点

**实验设计**：以 OpenVLA 作为主人研究方向的动作生成基线
- 对比基线：RT-2-X、DreamerV3
- 度量指标：语言泛化成功率、多任务成功率、finetune 数据效率
- 预期结果：OpenVLA 应在语言泛化和多任务上显著优于纯 model-based 方法

## 🔗 知识图谱

- [[VLA]] - OpenVLA 是 autoregressive token VLA 的最强开源代表
- [[具身智能]] - 通用 manipulation 是本文核心任务

## 📌 待探索问题

- OpenVLA 的 autoregressive tokenization 在高频精细操作上是否仍是瓶颈？
- OpenVLA 与主人的 world model 方向如何整合——VLA 作为 policy，world model 作为规划器？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
