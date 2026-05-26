---
title: "LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels"
authors: Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero
arxiv: "2603.19312"
date: 2026-03
institution: Mila / NYU / Samsung SAIL / Brown University
conf: arXiv preprint
keywords: [JEPA, world model, representation collapse, SIGReg, embodied intelligence]
tags: [世界模型, 具身智能, 强化学习]
summary: "LeWorldModel 用预测损失 + SIGReg 稳定端到端 JEPA 世界模型训练，在保持物理结构表达的同时显著提升规划速度。"
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2603.19312_LeWorldModel.pdf"
reading_date: 2026-04-23
reading_status: 已读
---

# 📖 LeWorldModel: Stable End-to-End JEPA from Pixels

## 🎯 题目

LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

## 📝 三句摘要

1. **问题背景**：JEPA（联合嵌入预测架构）在潜在空间预测未来表示，理论上比生成式世界模型更高效，但长期受"表示坍塌"问题困扰，现有解法依赖 EMA、stop-gradient、预训练 encoder 或复杂多项损失函数，难以端到端训练。
2. **核心方法**：提出 LeWorldModel（LeWM），仅用两项损失（预测损失 + SIGReg 高斯正则化）实现稳定端到端训练；SIGReg 基于 Cramér-Wold 定理，用 1024 个随机投影方向以极低计算成本强制 latent space 服从高斯分布，从根本上杜绝坍塌。
3. **关键结果**：~15M 参数单卡数小时训练完成，规划速度比 DINO-WM 快 48×，在 Push-T 操作任务上超越唯一另一个端到端 JEPA（PLDM）18%，latent space 线性探针可近乎完美恢复物体位置，且能可靠检测物理上不可能的事件。

## 💎 价值评估

- **🔬 研究价值**：首次用有理论保证的极简机制（SIGReg）解决 JEPA 端到端训练的表示坍塌问题，将超参数从 6 个降至 1 个，是 JEPA 路线从理论走向实用的关键里程碑。
- **🚀 实践价值**：15M 参数可部署于嵌入式端侧设备，48× 规划加速使实时机器人控制成为可能；无需预训练 encoder，降低了工业离线 RL 的数据和算力门槛。
- **📈 扩展潜力**：SIGReg 作为通用反坍塌正则化器，可迁移至其他 JEPA 变体；latent space 的物理结构编码能力为具身智能感知-规划解耦提供新思路。

## 🎯 可落地实验点

**实验设计**：在 UAV 控制任务中验证 LeWM 作为轻量世界模型的可行性
- 用 LeWM 替换现有 UAV 仿真中的动力学模型，在 latent space 做 MPC 规划
- 对比基线：DINO-WM（基础模型世界模型）、传统 MPC（真实动力学）
- 度量指标：规划速度（ms/step）、轨迹跟踪误差、单卡训练时间
- 预期结果：规划速度大幅提升，轨迹误差与 DINO-WM 相当，训练成本显著降低

## 🔗 知识图谱

- [[世界模型]] - LeWM 是 JEPA 路线的世界模型实现
- [[强化学习]] - 世界模型用于 model-based RL 规划
- [[Sim2Real]] - 轻量世界模型降低 sim2real 迁移成本

## 🔗 相关链接

- [[2024_DINO-WM]] - DINO-WM: 基于 DINOv2 的基础模型世界模型，本文主要对比基线
- [[2024_PLDM]] - PLDM: 唯一另一个端到端 JEPA，本文在 Push-T 上超越其 18%
- [[2023_I-JEPA]] - I-JEPA: 杨立昆团队 JEPA 图像版，使用 EMA 避免坍塌

## 📌 待探索问题

- SIGReg 的 1024 个随机投影方向是否足够？在高维 latent space（>512 维）中是否需要更多投影？
- LeWM 的 latent space 物理结构编码能力能否扩展到 3D 场景（如 UAV 飞行空间），还是目前仅限于 2D 操作任务？
