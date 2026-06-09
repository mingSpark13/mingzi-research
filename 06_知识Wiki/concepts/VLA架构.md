---

type: "concept"
level: "secondary"
parent: "VLA"
tags: ["VLA架构"]
summary: "视觉 + 语言 + 动作统一端到端模型的核心架构（含微调策略）"
updated: "2026-05-20"
id: "concept.VLA架构"
pageType: "concept"
---


# 概念：VLA（Vision-Language-Action）

## 定义

VLA 是一种将**视觉感知（Vision）**、**语言理解（Language）**和**动作生成（Action）**统一到单一模型中的架构范式。给定机器人环境的图像/视频和自然语言指令，VLA 直接输出可执行的低层动作序列。

## 核心架构

```
图像/视频 + 语言指令 → VLM Backbone → Action Head → 7D 机器人动作
```

### 关键组件
- **Vision Encoder**：ViT/SigLIP 提取视觉特征
- **Language Backbone**：LLM 理解指令语义
- **Action Head**：MLP / Diffusion / Flow Matching 输出动作

## 主要方法流派

| 方法 | Action Head | 特点 | 代表 |
|------|------------|------|------|
| 离散 Token | Autoregressive | 直接复用 LLM 解码 | RT-2, OpenVLA |
| 连续回归 | MLP | 简单高效 | StarVLA-α |
| 扩散模型 | Diffusion | 多模态动作分布 | π₀, DAM-VLA |
| 流匹配 | Flow Matching | 训练稳定，推理快 | π₀-fast, LILAC |

## 现有局限

1. **VLM 推理延迟**：200-2000ms，无法满足毫秒级高频控制
2. **无层次化解耦**：缺乏「意图规划 ↔ 精细执行」的分层
3. **跨载体泛化难**：不同机器人的动作空间差异大
4. **缺乏物理理解**：纯视觉预测缺乏物理一致性

## 与其他概念的关系

- 上游：[[concepts/隐空间世界模型]] 可为 VLA 提供环境动力学预测
- 并行：[[concepts/ACT动作分块]] / [[concepts/扩散策略]] / [[concepts/流匹配]] 是 VLA 的 Action Head 候选
- 下游：[[concepts/跨载体泛化]] 解决 VLA 在不同机器人间的迁移

## 关键论文

- RT-2 (Google, 2023) — 首个大规模 VLA
- OpenVLA (Stanford, 2024) — 开源 VLA 基线
- π₀ (Physical Intelligence, 2025) — Flow Matching VLA
- StarVLA-α (HKUST, 2026) — 简化 VLA，MLP head 即可达到 SOTA
- [[sources/source.2605.18556_Key-Gram|Key-Gram (2605.18556)]] — 外置语言记忆经 key-gram 检索注入隐藏层，提供“不改 backbone 扩知识”的轻量路线

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [[concepts/跨载体泛化|概念：跨载体泛化（Cross-Embodyment Generalization）]]
- [[concepts/隐空间世界模型]]|概念：Latent 世界模型（Latent World Model）
- [[sources/source.2603.14363_AerialVLA|AerialVLA (2603.14363)]]
- [[sources/source.2509.23829_DexFlyWheel|DexFlyWheel (2509.23829)]]
- [[sources/source.2603.25406_MMaDA-VLA|MMaDA-VLA (2603.25406)]]
- [[sources/RDT2_2602.03310|RDT2 (2602.03310)]]
- [[sources/RoboInter_2602.09973|RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation]]
- [[sources/TIDAL_2601.14945|TIDAL: Temporally Interleaved Diffusion and Action Loop]]
- [[sources/ViSA-Enhanced_AVLN_2603.08007|ViSA-Enhanced Aerial Vision-Language Navigation (2603.08007)]]
- [[sources/Xiaomi-Robotics-0_2602.12684|Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution]]
- [[sources/deltaVLA_2603.08361|ΔVLA (2603.08361)]]
<!-- openclaw:wiki:related:end -->

## 旧知识图谱补充：代表模型与落地定位

### 代表模型补充
- **RT-1**：机器人 Transformer 开山之作，奠定 VLA/RT 系路线。
- **OpenVLA**：开源 7B VLA，适合做微调和系统验证。
- **GR00T / GO-1**：代表产业界大规模数据 + 基础模型路线。

### 与经典 Policy 层的关系
```
VLA（foundation model）
    ↓
ACT / Diffusion Policy（经典 policy）
    ↓
BC / 轨迹控制（底层执行）
```
VLA 更偏高层语义与通用能力，ACT / Diffusion Policy 更轻量，也更容易做任务化落地。


## 相关页面
- [[comparisons/端到端VLA_vs_层次化VLA]]
- [[overview/方向_VLA_技术路线图]]
