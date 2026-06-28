---
title: "Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think"
authors: "Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller et al."
arxiv: "2606.20246"
date: 2026-06-18
institution: "（待补充）"
conf: "arXiv 2026"
keywords: [VLA压缩, 层剪枝, Centered Kernel Alignment, 部署效率, 模型蒸馏]
tags: ["VLA架构", "实时推理", "多模态统一架构"]
domain: VLA架构
pdf_path: "../../01_论文库/D02_VLA/2606.20246_VLA-Layer-Compression.pdf"
reading_date: 2026-06-28
reading_status: 已读
related_concepts: ["VLA架构", "实时推理", "多模态统一架构"]
---

# VLA 微调只需要更少的层：你可能高估了 VLA 的深度需求

> **arXiv**: 2606.20246 | **方向**: D02_VLA | **入库时间**: 2026-06-28 R1268 | **状态**: ✅ 已入库（论文级深挖）

## 🎯 题目

Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think

## 📝 三句摘要

1. **问题背景**：π₀、GR00T-N1.5 等多 B 参数 VLA 在下游微调和实时推理上计算开销巨大，机载/边缘部署几乎不可能；现有 token reduction 和 dynamic layer selector 方法仍需加载全量模型才能工作。
2. **核心方法**：揭示 VLA 的层间表征严重冗余（通过 Centered Kernel Alignment 单次前向识别冗余层），提出 training-free structural compression 管线，把 VLM backbone 和 control policy head 一并剪除 twin layer，最多压缩 50% 深度。
3. **关键结果**：在 LIBERO/RoboCasa/SimplerEnv 三大仿真基准 + 10 个真机任务、4 种 embodiment 上，下游微调训练时间减 40-50%、实时推理加速最高 30%，同时匹配或超过原始全量模型性能。

## 💎 价值评估

- **🔬 研究价值**：揭示 VLA 层间冗余的"反直觉"事实——尽管训练轨迹多样、参数规模大，层间特征仍高度可压缩；为部署期 VLA 优化打开全新维度（无需重新训练的"结构剪枝"）。
- **🚀 实践价值**：直接对应主人 UAV/空中机械臂机载 VLA 部署的痛点（边缘算力受限），可用最小工程成本把现有 base VLA 部署到 Jetson Orin/RK3588 等平台。
- **📈 扩展潜力**：与 PolicyTrim（2606.22540, 已入库）形成"层剪枝"+"action chunk 剪枝"两条独立压缩路线，理论上可叠加；与 E-TTS（2606.27268, 已入库）正交（前者压缩模型本身，后者推理时计算 scaling）。

## 🎯 可落地实验点

**实验设计 1：主人现有 VLA base model 层剪枝落地**
- 用 CKA 算法对主人 base VLA（如基于 OpenVLA/π₀ 微调的版本）做单次前向分析，识别可剪除的 twin layer。
- 度量指标：剪除比例、动作预测 MSE 变化、真机任务成功率、机载延迟（Jetson Orin 测）。
- 预期结果：剪除 30-40% 深度后，真机成功率持平或略升（因层间冗余），机载延迟降 25%。

**实验设计 2：层剪枝 + PolicyTrim 组合压缩**
- 把层剪枝（结构侧）+ PolicyTrim（action chunk 优化侧）联合部署到同一 VLA pipeline。
- 度量指标：训练时间、推理延迟、单任务物理步数、SR 综合。
- 预期结果：训练时间减 60%+，推理减 50%+，动作执行效率提升 1.5×。

**实验设计 3：空中机械臂 edge 部署 PoC**
- 把剪枝后的 VLA 部署到 Jetson Orin Nano（8GB）+ 主人空中机械臂真机。
- 对比基线：原版 base VLA（FP16 推理）、DistillVLA（同等压缩方法）。
- 度量指标：端到端控制频率、真机任务成功率（5 个抓取/放置任务）、功耗。
- 预期结果：控制频率从 ~5Hz 提升到 ~10Hz，功耗减 40%，SR 持平。

## 🔗 知识图谱

- [[VLA架构]] - 核心对象是 VLA backbone 层间冗余
- [[多模态统一架构]] - VLM backbone + control head 的统一架构
- [[实时推理]] - 边缘部署实时性直接受深度影响
- [[ACT动作分块]] - 与 PolicyTrim 正交，action chunk 优化

## 🔗 相关链接

- [[2026-04_E-TTS]] - E-TTS 推理时计算 scaling，正交压缩路线
- [[PolicyTrim (2606.22540)]] - PolicyTrim action chunk 优化，与本文层剪枝叠加
- [[2603.23202_Gaze_Regularized_VLA]] - VLA 微调策略参考（微调阶段的层选择启发）
- [[2601.02456_InternVLA-A1]] - InternVLA-A1 大参数 VLA，可作层剪枝候选 base

## 📌 待探索问题

1. CKA 单次前向识别冗余层依赖 calibration 数据分布——若主人下游任务与 pretrain 分布差异大（如细粒度抓取 vs 大范围导航），剪除策略是否会失效？
2. 50% 深度压缩对长程任务（VLN、跨步操作）是否仍稳定？是否需要按层位（如 vision encoder vs policy head）差异化剪枝？
3. 本文方法 vs 蒸馏（如 DistillVLA）vs 量化（INT8/W4A16）三条部署优化路线如何选择？层剪枝可能与量化互补，蒸馏单独替代需评估。
4. 剪枝后 VLA 与 D01 world model verifier 组合时，verifier 是否需要同步压缩？还是 verifier 留在大模型只压缩 policy？

---
**维护**: 花火 · 2026-06-28 R1268
