---
title: "dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought"
authors: ["Junjie Wen", "Minjie Zhu", "Jiaming Liu", "Zhiyuan Liu", "Yicun Yang", "Linfeng Zhang", "Shanghang Zhang", "Yichen Zhu", "Yi Xu"]
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
tags: ["D02"]
domain: 通用操作
pdf_path: "Notebook/30_论文研究/01_论文库/dVLA_Diffusion_VLA_CoT_2509.25681.pdf"
reading_date: 待补充
reading_status: 已读
related_concepts: ["VLA架构", "空中操作"]
---

## 🎯 题目

"dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought"

# dVLA: Diffusion VLA with Multimodal CoT

## 📝 三句摘要

1. **核心创新**：Diffusion-based VLA + Multimodal Chain-of-Thought，统一视觉感知、语言推理、机器人控制于单一扩散目标
2. **核心结果**：LIBERO 基准 96.4% 平均成功率，超越离散和连续 action policies；真实世界 Franka 机器人验证
3. **工程优化**：Prefix attention mask + KV caching，推理加速

## 核心创新

### 架构：Diffusion + VLA + Multimodal CoT

**dVLA 的核心设计**：
```
视觉观察 + 语言指令 → Multimodal CoT（视觉+语言+动作联合推理）→ Diffusion 生成动作
```

**关键机制**：
- **单一扩散目标**：联合优化感知、语言理解、动作生成
- **Multimodal CoT**：在推理时结合视觉和语言的 chain-of-thought
- **加速策略**：Prefix attention mask + KV caching，减少推理延迟

### 与 LaST0/ManualVLA 的关系

**同作者群（Shanghang Zhang, Jiaming Liu）**，但技术路线不同：

| 论文 | 核心机制 | CoT 类型 |
|------|---------|---------|
| LaST0 | 隐式时空 CoT + MoT | 连续隐空间 |
| ManualVLA | ManualCoT（多模态手册）| 显式多模态步骤 |
| dVLA | Multimodal CoT + Diffusion | 扩散+多模态联合 |

**三篇共同构成完整技术栈**：
- LaST0 = 隐式推理
- ManualVLA = 显式规划手册
- dVLA = 扩散生成 + 多模态 CoT

## 与 Paper A 的关系

**Paper A 高层 VLM 意图层的完整候选**：

| Paper A 分层 | dVLA 对应 |
|------------|---------|
| VLM 意图层 | Multimodal CoT（视觉+语言联合推理）|
| 中层意图解析 | 扩散目标隐含的意图分解 |
| 低层执行 | Diffusion 生成动作 |

**关键区别**：
- dVLA 是端到端，Paper A 是层次化解耦
- Paper A 的创新在于把「意图」显式建模为独立中层

## 待探索问题

1. dVLA 的 diffusion 推理延迟是否满足 Paper A 的实时性要求？
2. dVLA 与 SafeFlow 安全层的结合方案？
3. dVLA 在空中机械臂场景的适用性？


## 💎 价值评估

- **🔬 研究价值**：待补充
- **🚀 实践价值**：待补充
- **📈 扩展潜力**：待补充


## 🎯 可落地实验点

**实验设计**：待补充
- 对比基线：待补充
- 度量指标：待补充
- 预期结果：待补充


## 🔗 知识图谱
- [[VLA]]
- [[具身智能]]
- [[空中操作]]


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
