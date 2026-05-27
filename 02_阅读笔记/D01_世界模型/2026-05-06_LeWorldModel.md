---
title: "LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels"
authors: Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero
arxiv: 2603.19312
date: 2026-03
institution: Mila & Université de Montréal / NYU / Samsung SAIL / Brown University
conf: arXiv Preprint
keywords: [JEPA, 世界模型, 隐空间预测, SIGReg, 端到端训练]
tags: [隐空间世界模型, 物理一致性, 动作条件预测, MPC, 强化学习]
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2603.19312_LeWorldModel.pdf"
reading_date: 2026-05-06
reading_status: 已读
summary: "联合嵌入预测架构（JEPA）是学习世界模型的有效范式，但现有方法依赖复杂的损失项、预训练编码器或启发式技巧（如停止梯度、EMA）来防止表征崩溃，训练不稳定且调参困难。 提出 LeWorldModel (LeWM)，首个仅用**两个损失项**（下一嵌入预测损失 + SIGReg 正则化）即可从原始像素端到端稳定训练的 JEPA 方法，15M 参数单卡可训数小时。 LeWM 在多种 2D/3D 控制任务上达到或接近基础模型级世界模型性能，规划速度比 DINO-WM 快约 50 倍、比基于基础模型的方法快最多 48 倍，且其隐空间编码了可探测的物理结构。"
related_concepts: ["隐空间世界模型", "物理一致性", "动作条件预测", "MPC", "强化学习"]
---

# LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

## 🎯 题目

LeWorldModel (LeWM): 从像素出发的稳定端到端联合嵌入预测架构

## 📝 三句摘要

1. **问题背景**：联合嵌入预测架构（JEPA）是学习世界模型的有效范式，但现有方法依赖复杂的损失项、预训练编码器或启发式技巧（如停止梯度、EMA）来防止表征崩溃，训练不稳定且调参困难。
2. **核心方法**：提出 LeWorldModel (LeWM)，首个仅用**两个损失项**（下一嵌入预测损失 + SIGReg 正则化）即可从原始像素端到端稳定训练的 JEPA 方法，15M 参数单卡可训数小时。
3. **关键结果**：LeWM 在多种 2D/3D 控制任务上达到或接近基础模型级世界模型性能，规划速度比 DINO-WM 快约 50 倍、比基于基础模型的方法快最多 48 倍，且其隐空间编码了可探测的物理结构。

## 💎 价值评估

- **🔬 研究价值**：首次实现了真正"无技巧"（trick-free）的端到端 JEPA，证明了只需两层损失即可稳定训练，将可调超参数从 6 个减少到 1 个，为 JEPA 训练提供了原则性基础
- **🚀 实践价值**：单 GPU 可训（15M 参数），降低研究门槛；推理速度极快（48× 加速），适合实时控制场景；完全离线、无奖励信号要求，适配大规模无标注视频数据
- **📈 扩展潜力**：SIGReg 可与任意 JEPA 变体结合；隐空间物理探测结果表明该表示可迁移到物理推理任务；与扩散模型/视频生成模型的结合值得探索

## 🎯 可落地实验点

**实验设计：将 SIGReg 引入无人机世界模型训练**
- 对比基线：现有端到端隐空间世界模型（无 SIGReg）、基于预训练编码器的方法（DINO-WM 类）
- 度量指标：表征崩溃率（collapse rate）、下游控制任务成功率、规划效率（FPS）
- 实现方案：
  1. 在 AirSpark 仿真环境中采集无人机飞行数据（像素 + 动作），构建离线数据集
  2. 用 LeWM 训练隐空间世界模型，替换原有重构损失方案
  3. 用 latent MPC 进行轨迹规划，对比规划速度与控制精度
  4. 探针实验：验证隐空间是否编码速度/高度等物理量

## 🔗 知识图谱

> 字典 v1.1 二级规范名

- [[隐空间世界模型]] - 本文核心范式，在 compact latent space 中建模环境动力学
- [[物理一致性]] - LeWM 隐空间编码可探测的物理量，能检测物理不合理轨迹
- [[动作条件预测]] - 以 action 为条件输入，通过 autoregressive predictor 预测下一帧隐表示
- [[MPC]] - 测试时在隐空间进行 MPC 规划，迭代优化动作序列
- [[强化学习]] - 完全离线 reward-free 设置，与世界模型结合的 policy learning 框架

## 🔗 相关链接

- [[2023_DreamerV4]] - Dreamer 系列：基于重构的世界模型+imagination-based policy learning，LeWM 对比其规划效率
- [[2025_PLDM]] - PLDM：唯一现有端到端 JEPA 替代方案，但依赖多损失项和启发式，LeWM 以更简单目标超越之
- [[2025_DINO-WM]] - DINO-WM：基于冻结预训练编码器的世界模型，LeWM 以端到端学习在多项任务上超越之

## 📌 待探索问题

- SIGReg 的投影数 M 和正则化权重 λ 在不同环境/数据规模下的敏感性如何？是否有理论保证的最优范围？
- LeWM 的隐空间物理探测结果（速度/高度等）能否直接用于下游控制器的设计？能否实现"隐空间物理先验"的迁移？
- 当前方法仅预测下一帧嵌入，对于更长时域的规划是否仍然稳定？层次化 JEPA（如分层预测）与 LeWM 的结合是否值得探索？

---
**维护**: 花火 · 2026-05-06
