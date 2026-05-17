---
type: "source"
tags: []
summary: "- **PWKE (Prior-Guided World-Knowledge Extractor)**: 从视觉输入提取可操控区域、空间关系、语义线索，由辅助头和先验伪标签引导，减少冗余。"
origins: ["02_阅读笔记/01_机器人与具身/2026-04-14_deltaVLA"]
updated: "2026-04-17"
---

# deltaVLA_2603.08361

**核心要点**:
- **PWKE (Prior-Guided World-Knowledge Extractor)**: 从视觉输入提取可操控区域、空间关系、语义线索，由辅助头和先验伪标签引导，减少冗余。
- **LWVQ (Latent World Variation Quantization)**: 将动作导致的world knowledge演变量化为离散表示。

**与我们的关系**:
- ΔVLA 的"变化量预测"思路与传统 VLA 的"绝对状态回归"正交。关键创新点：先用 prior extractor 建立当前状态表征，再预测该表征在action后的Δ变化。这与主人的「意图规划↔精细执行」三层解耦有一定呼应——高层建模世界变化量，而非直接输出动作。

**原始资料**:
- [[02_阅读笔记/01_机器人与具身/2026-04-14_deltaVLA]]
