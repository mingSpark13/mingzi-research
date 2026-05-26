---
type: "concept"
id: "concept.Transformer"
pageType: "concept"
tags: ["Transformer", "序列建模", "注意力机制"]
summary: "Transformer 是以自注意力为核心的通用序列建模骨架，适合统一处理感知 token、动作 token 与语言推理过程。"
sources: ["sources/source.2605.15153_Pelican_Unified_1_0", "sources/source.2605.15187_Articraft", "sources/source.TripoSR_2403.02151"]
updated: "2026-05-18"
---

# Transformer

## 定义
以自注意力机制为核心的序列建模架构，可在统一 token 空间中处理语言、视觉、动作与时序上下文。

## 核心原理
- 通过 attention 在长程依赖之间建立动态关联，避免固定感受野对跨模态交互的限制。
- 用共享骨架承载编码、推理、生成与条件控制，适合 VLM/VLA/3D 重建等统一建模任务。

## 优缺点
- 优点：扩展性强，容易承接多模态预训练，并能统一表示高层语义与低层动作条件。
- 缺点：计算成本高，对数据规模敏感；直接用于机器人闭环时常需再配合结构先验、记忆机制或控制模块。

## 代表论文链接
- [[sources/source.2605.15153_Pelican_Unified_1_0]]
- [[sources/source.2605.15187_Articraft]]
- [[sources/source.TripoSR_2403.02151]]

## 相关概念
[[concepts/VLA架构]] [[concepts/多模态统一架构]] [[concepts/动作条件预测]]
