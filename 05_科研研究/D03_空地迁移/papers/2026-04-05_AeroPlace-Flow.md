# AeroPlace-Flow: Language-Grounded Object Placement for Aerial Manipulators via Visual Foresight and Object Flow

> **入库时间**: 2026-04-05 (R456)
> **方向**: 03_空地迁移
> **arXiv**: 2603.07744

## 核心贡献
- **问题**: 空中机械臂在杂乱环境中的语言引导物体放置
- **方法**: Visual Foresight + Object Flow
  - 给定场景和语言指令，识别目标物体并主动探索以获得更好的视角
  - 每个视角用 grasp generation network 预测多个6-DoF grasp候选
  - 用 collision-aware feasibility framework 评估每个候选，选最佳执行
- **关键创新**: Object Flow — 预测物体在操作过程中的运动轨迹，用于选择最优抓取时机

## 与主人主线的关系
- **直接相关**: 龙虾项目 "找到一辆单车" = 语言引导 + 视觉导航 + 物体操作
- AeroPlace-Flow 提供了**语言→视觉感知→抓取选择→执行**的完整 pipeline
- 可直接参考其 active exploration 策略（探索更好的视角）
- Object Flow 的思想可迁移到其他空中操作任务

## 可落地实验点
1. 将 Object Flow 思想引入龙虾导航 — 预测单车移动轨迹，选择最佳接近时机
2. 借鉴 collision-aware feasibility 评估框架，对每个候选动作评估碰撞风险
3. Active exploration 策略用于机臂协同场景

## 链接
- arXiv: https://arxiv.org/abs/2603.07744
