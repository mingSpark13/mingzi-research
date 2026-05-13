---
title: "HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents"
arxiv_id: "2604.07430"
authors: "Tencent Hunyuan Team, Robot-X Lab"
institution: "Tencent"
conf: "arXiv 2026"
date: "2026-04"
domain: "具身智能"
direction: "D02_VLA"
pdf_path: "Notebook/30_论文研究/01_论文库/具身智能/2604.07430_HY-Embodied-0.5.pdf"
source_url: "https://arxiv.org/abs/2604.07430"
github: "https://github.com/Tencent-Hunyuan/HY-Embodied"
reading_date: "2026-04-20"
reading_status: "已读"
tags: [VLA架构, 具身智能, 多模态统一架构]
summary: "以 MoT 架构、视觉隐层 token、迭代自进化训练与在线蒸馏构建可落地的具身基础模型闭环，小模型端侧部署与大模型云端推理两线并进。"
related_concepts: ["VLA架构", "具身智能", "多模态统一架构"]
---

# HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents

## 📌 三句话摘要

腾讯混元联合 Robot-X 实验室推出 HY-Embodied-0.5，以 MoT 架构 + 视觉隐层 token + 迭代自进化训练 + 大→小在线蒸馏四大设计，构建从 VLM 基座直训 VLA 的完整闭环方案。双版本设计：MoT-2B 面向端侧实时部署（22 个基准 16 项第一），MoE-A32B 面向云端复杂推理（平均分 67.0%，超越 Gemini 3.0 Pro）。在真实机器人控制任务上验证有效：精密插件装配 85%、餐具堆叠 80%、杯子悬挂 75% 成功率。

## 🎯 价值评估

**评分：⭐⭐⭐⭐⭐（5/5）**

- 全链路闭环方案，架构 + 数据 + 训练 + 蒸馏一体化，无短板
- MoT 架构视觉语言解耦，小模型也能拉满视觉能力
- 超 1 亿样本数据体系，专为具身需求设计（空间/几何/轨迹/可及性）
- 真实机器人验证，不只是 benchmark 刷分
- 对 D02 VLA 方向、D04 跨载体泛化、D07 机械臂 RL 均有直接参考价值

## 🔑 核心创新

### 1. MoT（Mixture-of-Transformers）架构
- 视觉 token 与文本 token 使用独立 FFN 与 QKV 参数
- 视觉分支：双向全注意力（适合图像建模）
- 语言分支：因果注意力（保证生成流畅性）
- 几乎不增加推理开销，训练收敛更快
- 配套 HY-ViT 2.0（400M 参数，原生任意分辨率，大模型蒸馏而来）

### 2. 视觉隐层 Token
- 每个视觉序列末尾加入可学习视觉隐层 token
- 用大 ViT 全局特征做监督
- 把细粒度视觉特征"翻译"成语言模型能理解的语义
- 注意力可视化：视觉精准聚焦物体关键区域，语言同步聚焦动作/空间关系

### 3. 迭代自进化后训练
- 冷启动 SFT：10 万级高质量 CoT 数据初始化推理链
- 强化学习 GRPO：任务感知奖励（空间 IoU、距离、轨迹相似度、LLM 裁判）
- 拒绝采样微调 RFT：只保留"部分答对、靠近能力边界"的样本
- 循环迭代：RL 探索边界 → RFT 固化优质推理链

### 4. 大→小在线策略蒸馏（OPD）
- 小模型先生成自己的回答
- 大模型在小模型每一步前缀上强制给出分布
- 最小化 KL 散度，让小模型在容易错的步骤上直接学大模型
- 2B 小模型继承 32B 大模型的推理逻辑与空间能力

## 📊 实验结果

### MoT-2B（端侧）
| 对比 | 结果 |
|------|------|
| 22 个基准 | 16 项第一，4 项第二 |
| 平均分 | 58.0% |
| vs Qwen3-VL-4B | +10.2% |
| vs RoboBrain2.5-4B | +8.6% |

### MoE-A32B（云端）
| 对比 | 结果 |
|------|------|
| 平均分 | 67.0% |
| vs Gemini 3.0 Pro | +3.4%（63.6%） |
| vs Seed 2.0 | +0.8%（66.2%） |
| vs Qwen3.5 A17B | +0.9%（66.1%） |

### 真实机器人控制
| 任务 | 成功率 |
|------|--------|
| 精密插件装配 | 85% |
| 餐具堆叠 | 80% |
| 杯子悬挂 | 75% |

## 💡 可落地实验点

1. **D02 VLA 方向**：MoT 架构的视觉语言解耦思路可借鉴，用于改进现有 VLA 小模型的视觉感知能力
2. **D04 跨载体泛化**：OPD 在线蒸馏策略可用于跨载体知识迁移，大模型教小模型适应新形态
3. **ZeroTracking 方向**：HY-ViT 2.0 的空间感知能力（深度估计/3D 定位）可作为 ZeroSeg 的视觉编码器候选

## ⚠️ 局限性

- 依赖高质量具身数据，标注成本高
- 动态环境、突发干扰鲁棒性仍需提升
- 未融入显式物理引擎，极端物理交互可能偏差
- MoE-A32B 总参数 407B，云端部署算力要求高

## 🔗 知识图谱

- [[concepts/VLA架构]]
- [[concepts/具身智能]]
- [[concepts/知识蒸馏]]
- [[concepts/空间推理]]
- [[concepts/扩散策略]]

## 📌 待探索问题

- MoT 架构与现有 ACT/π0 架构的对比实验？
- OPD 蒸馏在跨载体场景（UAV → 机械臂）的迁移效果？
- HY-ViT 2.0 能否直接替换 ZeroTracking 的视觉编码器？

## 🔗 相关链接

- arXiv: https://arxiv.org/abs/2604.07430
- GitHub: https://github.com/Tencent-Hunyuan/HY-Embodied
- 公众号解读: https://mp.weixin.qq.com/s/vkWuau9UN6Ra80RNSTo_oA
