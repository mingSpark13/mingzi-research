---
type: "concept"
id: "concept.空中VLN"
pageType: "concept"
tags: ["空中视觉语言导航", "语义导航", "单目无地图导航"]
summary: "空中VLN是无人机在语言条件下进行三维视觉导航的核心任务设定，连接语义理解、在线决策与飞行控制。"
sources: ["sources/AerialVLA_2603.14363", "sources/UAV_VLN_Survey_2604.13654", "sources/source.2026-04-19_UAV_VLN_Survey"]
updated: "2026-04-19"
---

# 空中VLN

## 定义
空中VLN（Aerial Vision-Language Navigation）要求无人机依据自然语言指令和实时视觉观测，在三维空间中完成目标搜索、路径规划、避障与到达。

## 核心原理
- 以语言指令提供目标语义与约束
- 以视觉观测完成地标识别、空间定位与路径选择
- 以连续控制或分层规划将高层意图落到飞行动作

## 优势与挑战
- **优势**：天然适合开放词汇目标、弱地图甚至无地图场景
- **挑战**：3D连续动作空间、视角变化大、动力学约束强、导航与操作衔接困难

## 代表来源
- [[sources/AerialVLA_2603.14363]]
- [[sources/UAV_VLN_Survey_2604.13654]]
- [[sources/source.2026-04-19_UAV_VLN_Survey]]

## 相关概念
- [[concepts/空中视觉语言导航]]
- [[concepts/语义导航]]
- [[concepts/单目无地图导航]]
- [[concepts/无人机避障]]
- [[concepts/VLA架构]]
