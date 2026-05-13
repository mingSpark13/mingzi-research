---
title: "Diffusion Policy: Diffusion Models for Robotic Manipulation"
authors: Chi et al. (Columbia, TRI)
arxiv: 2303.04137
date: 2023-03
institution: Columbia University / Toyota Research Institute
conf: CoRL 2023
keywords: Diffusion Policy, Manipulation, Imitation Learning, Multi-modal Action
tags: ["扩散策略", "灵巧操作", "模仿学习"]
domain: 通用操作
pdf_path: ../../01_论文库/强化学习/2303_DiffusionPolicy.pdf
reading_date: 待补充
reading_status: 已读
related_concepts: ["扩散策略", "灵巧操作", "模仿学习"]
---

## 🎯 题目

Diffusion Policy: Diffusion Models for Robotic Manipulation

## 📝 三句摘要

1. **问题背景**：机器人操控需要建模多模态动作分布（多种合理解法如"从左边抓"vs"从右边抓"），传统方法（GPT/BC）在高维连续动作空间和多峰分布上建模困难。
2. **核心方法**：将策略表示为 conditional denoising diffusion process，把动作 chunk 加噪再逐步去噪恢复，配合 receding-horizon control 和 diffusion transformer 来缓解推理延迟问题。
3. **关键结果**：在 14 个任务上显著超越 prior imitation learning 方法，在复杂任务（餐饮、写字等）上展示了强大的多峰分布建模能力。

## 💎 价值评估

- **🔬 研究价值**：Diffusion Policy 是具身操控领域 diffusion-based policy 的奠基工作，证明了扩散模型对多模态动作分布的天然优势。
- **🚀 实践价值**：开源实现清晰，是 real robot manipulation 的强 baseline。
- **📈 扩展潜力**：可与 VLM 结合（如 GR00T N1 的 System 1），或与 world model 结合做 diffusion world model policy。

## 🎯 可落地实验点

**实验设计**：将 Diffusion Policy 作为具身操控 baseline，与主人的 world model 方向结合
- 对比基线：BC、RT-2、ACT
- 度量指标：任务成功率、多峰动作覆盖率、推理延迟（ms/step）
- 预期结果：Diffusion Policy 在多模态操作任务上应显著优于 autoregressive 方法

## 🔗 知识图谱

- [[扩散策略]] - Diffusion Policy 是扩散策略的奠基工作
- [[流匹配]] - FlowPolicy 是更快的替代方案，与 Diffusion Policy 同属生成式动作建模
- [[灵巧操作]] - 精细操控是本文核心应用场景

## 📌 待探索问题

- Diffusion Policy 的多步去噪推理延迟如何优化？是否能与 world model rollout 结合？
- 在高频控制（50Hz+）场景下，diffusion 是否仍然适用？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
