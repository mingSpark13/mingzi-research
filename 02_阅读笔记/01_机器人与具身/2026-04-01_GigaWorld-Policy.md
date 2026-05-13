---
title: "GigaWorld-Policy: An Efficient Action-Centered World–Action Model"
authors: GigaAI (GigaWorld Team)
arxiv: "2603.17240"
date: "2026-03-24"
institution: GigaAI
conf: arXiv
keywords: World-Action Model, VLA, Flow Matching, Diffusion Transformer, Robot Manipulation, Imitation Learning
tags: ["D02", "VLA", "流匹配", "灵巧操作", "模仿学习"]
domain: 空中操作
pdf_path: ../../01_论文库/空中操作/GigaWorld-Policy_2603.17240.pdf
reading_date: "2026-04-01"
reading_status: 已读
summary: GigaWorld-Policy 用 action-centered world-action model 联合建模未来视觉动态与动作生成，以超低延迟实现高成功率机器人操作。
related_concepts: ["流匹配", "灵巧操作", "模仿学习"]
---

## 🎯 题目

GigaWorld-Policy: An Efficient Action-Centered World–Action Model

## 📝 三句摘要

1. **问题背景**：VLA 模型面临"监督稀疏性"困境——动作标签稀疏低维，而观测和语言指令高维语义丰富，导致模型过度依赖浅层上下文而非物理接地动作预测。
2. **核心方法**：提出 Action-Centered World–Action Model，使用因果注意力掩码将动作生成与未来视觉动态统一到扩散 Transformer 框架中，以未来视觉动态作为推理信号和密集监督源，而非依赖迭代式视频生成。
3. **关键结果**：在真实机械臂操作中，85% 任务成功率，A100 GPU 仅 0.5ms 推理延迟，超越 GigaBrain-0、Cosmos-Policy、Motus 等基线。

## 💎 价值评估

- **🔬 研究价值**：提出 WAM 范式（World-Action Model），填补了"动作中心"世界模型在机器人操作中的空白，证明了未来视觉动态可以作为动作学习的有效密集监督信号而非必须生成。
- **🚀 实践价值**：超低延迟（0.5ms）+ 高成功率使其具备实时控制潜力；5B 参数扩散 Transformer 架构路线清晰；预训练+后训练两阶段范式可迁移。
- **📈 扩展潜力**：可与空中机器人结合（边缘部署 5B 模型需量化压缩）；稀疏未来帧预测（固定步长 Δ）可迁移到无人机时序操作；多视角 composite 表示可借鉴到多相机无人机场景。

## 🎯 可落地实验点

**实验设计：空中机械臂操作场景下的 WAM 迁移实验**

- **对比基线**：原版 GigaWorld-Policy（机械臂）、无未来预测监督的动作模型（如 Diffusion Policy）、纯 VLA 方法（π0）
- **测试场景**：空中机械臂（如挂载在四旋翼上的 6DOF 机械臂）执行精细操作任务（物体抓取、开关操作）
- **迁移方法**：将 GigaWorld-Policy 的 action-centered 预训练权重迁移到空中机械臂操作场景，替换后训练阶段的 robot-specific 数据；关键改动：多视角 composite 输入适配机载多相机布局
- **度量指标**：任务成功率、操作平顺性（轨迹平滑度）、长时序任务完成率、Sim2Real 迁移性能
- **预期结果**：动作中心 WAM 相比纯 VLA 在长时序任务中提升 15-20% 成功率；稀疏未来预测机制可将监督密度提升 3-5 倍

## 🔗 知识图谱

- [[VLA]] - 视觉-语言-动作模型，本文提出 WAM（World-Action Model）作为 VLA 的新范式
- [[世界模型]] - 本文是 World-Action Model，在世界模型中显式融入动作生成，是具身世界模型的重要分支
- [[流匹配]] - Flow Matching 是本文的训练目标，同时优化动作预测和未来视觉动态
- [[扩散策略]] - Diffusion Policy 的进阶版，本文使用 5B 参数 Diffusion Transformer 作为动作生成骨干
- [[模仿学习]] - 后训练阶段使用专家轨迹数据进行行为克隆
- [[ACT动作分块]] - 一次预测一段动作序列（action chunk），减少误差累积
- [[具身智能]] - 预训练数据集包含 EgoDex、EGO4D 等具身数据，覆盖 10000 小时

## 🔗 相关链接

- [[2024-10_pi0]] - π0: 本文核心对比基线，VLA 领域奠基工作，GigaWorld-Policy 在长时序任务中显著超越
- [[2025_Cosmos-Policy]] - Cosmos-Policy: NVIDIA 的世界模型策略，GigaWorld-Policy 在延迟和成功率上均超越
- [[2025_DIAL]] - DIAL: 密集动作学习工作，本文方法与其共享"密集监督"思想但采用不同架构路径
- [[2025_RoboMind]] - RoboMind: 机器人数据预训练资源，本文预训练数据来源之一

## 📌 待探索问题

- GigaWorld-Policy 的 5B 参数规模如何压缩到无人机机载边缘设备（e.g., Jeton NX, Orin Nano）？量化+剪枝方案是什么？延迟能否控制在 10ms 以内？
- 稀疏未来帧预测步长 Δ 是手工设定还是学出来的？不同任务（快速飞行 vs. 精细操作）是否需要不同的 Δ？
- 预训练阶段包含大量 egocentric 人类视频（EgoDex、EGO4D），这种跨形态迁移是否会在空中机器人场景下出现 domain gap？如何缓解？

---
**维护**: 花火 · 2026-04-12
