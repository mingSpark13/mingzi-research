---
title: "DriveDreamer-Policy"
tags: ["世界模型", "感知与3D视觉", "动作生成", "自动驾驶"]
summary: "DriveDreamer-Policy 把深度生成、未来视频生成和动作生成统一到 geometry-grounded world-action model 中，为几何锚定的世界模型提供模块化路线。"
---

# DriveDreamer-Policy (2604.01765) 【候选入库】

> 日期：2026-04-14 | 方向：D01_世界模型 | 轮次：R701

## 核心贡献

**Geometry-Grounded World-Action Model**，把深度图生成 + 未来视频生成 + 运动规划统一在一个模块化架构里：
- **LLM 处理层**：语言指令 + 多视角图像 + 动作输入
- **三个轻量生成器**：depth 生成器 + 未来视频生成器 + 动作生成器
- **几何感知世界表示**：用深度信息显式锚定 3D 几何，而非只用 2D latent

## 与本方向的关系

- 直接对应 D01 识别的「纯 latent 缺几何锚定」gap
- 与 ABot-PhysWorld 的 physics alignment 形成互补（ABot 补物理，DriveDreamer 补几何）
- 对主人无人机场景极有价值：深度感知是空中导航 world model 的关键输入

## 可借鉴的技术点

1. **depth + video + action 三联生成**：可拆解用于无人机 world model，depth 提供 3D 一致性锚定
2. **模块化架构**：三个生成器并行，解耦了各模态生成，可独立替换/升级
3. **geometry-aware latent**：解决了 world model 在空中场景缺几何 grounding 的根本问题

## 局限/不足

- 针对自动驾驶场景（Navsim），向无人机场景迁移需做感知模态适配
- 未涉及安全验证层（verifier / safety gate），需后续补齐

## 归档

方向 D01，新增候选（摘要级），待后续轮次补充全文深挖。
