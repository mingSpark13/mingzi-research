---

type: "concept"
level: "secondary"
parent: "VLA"
tags: ["ACT动作分块"]
summary: "通过 Transformer 对动作序列做 chunking，一次预测多步"
updated: "2026-04-17"
id: "concept.ACT动作分块"
pageType: "concept"
---


# 概念：ACT（Action Chunking with Transformers）

## 定义

ACT（Action Chunking with Transformers）是斯坦福团队提出的模仿学习方法，用 Transformer 对动作序列做 **chunking**，一次性预测并执行多个时间步的动作，从而提升长时任务执行稳定性与动作平滑性。

## 核心原理

```
观测 (图像 + 状态) → Encoder → Transformer → 动作序列 chunk → 控制器执行
```

### 关键机制

1. **动作序列 chunk**：不是单步预测，而是预测长度为 $k$ 的动作序列chunk，减少时序误差累积
2. **Transformer 建模时序依赖**：用 self-attention 建模长距离动作相关性，避免误差逐级传播
3. **闭环执行 + chunk 更新**：每执行完一个 chunk，用最新观测更新状态，再预测下一 chunk

### 数学形式

给定观测 $o_t$，ACT 输出动作 chunk：
$$\hat{a}_{t:t+H} = \text{Transformer}(o_t; \theta)$$

其中 $H$ 为 chunk 长度（通常 8-16 步），chunk 内动作顺序执行，chunk 边界重新观测更新。

## 优缺点

### ✅ 优势
- **误差累积降低**：chunk 内部动作顺序执行，避免单步预测的误差逐级传播
- **动作平滑**：一次性预测序列，比逐帧预测更连贯
- **实现简单**：Transformer 架构，训练/推理开销可控
- **广泛采用**：被 OpenVLA 等 VLA 方法引用为 action head

### ❌ 局限
- **chunk 长度固定**：不同任务可能需要不同 chunk 大小，固定长度难以自适应
- **开环 chunk 需要闭环校正**：长时间开环执行会累积漂移
- **推理延迟被 chunk 长度放大**：chunk 越长，VLM 延迟影响越大（VLA 场景下）
- **不适合高频底层控制**：毫秒级控制（如飞行器）需要 100Hz+，chunk 无法满足

## ACT vs. 其他动作生成范式

| 维度 | ACT | [[concepts/扩散策略]] | [[concepts/流匹配]] |
|------|-----|-----------------------------------|-------------------------------|
| **生成方式** | Transformer 自回归 | 去噪扩散过程 | 流匹配 |
| **动作分布** | 单峰高斯 | 多峰分布 | 单峰/多峰均可 |
| **推理速度** | 快（单次 forward） | 慢（多步去噪） | 中等（ODE 求解） |
| **适用场景** | 精细操作（~10Hz） | 复杂多峰任务（~3-5Hz） | 高频控制（~50Hz） |
| **chunk 长度** | 固定 8-16 步 | 可变 | 可变 |

## 在主人研究中的定位

ACT 是 Paper A 三层架构中**低层精细执行**候选之一（详见 [[overview/方向_世界模型_技术路线图]]）：

- **适用场景**：精细空中操作（抓取/放置），频率 ~10Hz
- **升级方向**：结合 [[concepts/扩散策略]] 的多峰建模能力，或引入 [[concepts/流匹配]] 的高速推理
- **当前判断**：ACT 的误差累积低、实现简单，是低层执行器首选 baseline

## 关键论文

- ACT (Stanford, CoRL 2023) — Action Chunking 奠基工作 [[02_阅读笔记/01_机器人与具身/2023-01_ACT.md]]
- OpenVLA — 将 ACT chunking 引入开源 VLA 系统 [[05_科研研究/D02_VLA/REPORT.md]]

## Related
<!-- openclaw:wiki:related:start -->
### Referenced By

- [[concepts/流匹配]]|概念：Flow Matching（流匹配）
- [[concepts/隐空间世界模型]]|概念：Latent 世界模型（Latent World Model）
- [[concepts/VLA架构|概念：VLA（Vision-Language-Action）]]
<!-- openclaw:wiki:related:end -->

## 旧知识图谱补充：多任务扩展

- **MT-ACT**：ACT 的多任务扩展版本，说明 action chunking 不只适用于单任务 imitation。
- 旧图谱中的关键对比仍保留：ACT 偏确定性 chunk 预测，Diffusion Policy 偏概率式动作生成，两者常作为模仿学习双核心 baseline 成对比较。


## 相关页面
- [[comparisons/ACT动作分块_vs_扩散策略_vs_流匹配]]
- [[overview/方向_VLA_技术路线图]]
