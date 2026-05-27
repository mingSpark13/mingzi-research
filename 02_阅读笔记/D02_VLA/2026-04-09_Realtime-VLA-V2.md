---
title: "Realtime-VLA V2: Learning to Run VLAs Fast, Smooth, and Accurate"
authors: "（待补充）"
arxiv: "2603.26360"
date: 2026-04-09
institution: "（待补充）"
conf: arXiv
keywords: [VLA, 实时控制, 平滑执行, 机器人部署]
tags: [VLA架构, 实时推理, 运动控制]
summary: "围绕 fast、smooth、accurate 三目标优化 VLA 部署链路，强调连续执行中的抖动与时序问题。"
domain: 具身智能
pdf_path: ""
reading_date: 2026-04-09
reading_status: 已读
related_concepts: [VLA架构, 实时推理, 运动控制]
---

# Realtime-VLA V2: Learning to Run VLAs Fast, Smooth, and Accurate

- **arXiv**: [2603.26360](https://arxiv.org/abs/2603.26360)
- **日期**: 2026-03
- **方向**: D02 VLA

## 一句话总结
这篇工作把 VLA 的重点继续从“会不会做”推进到“能不能像人一样顺滑地连续做”，核心不是再堆大模型，而是把整条部署链路里的校准、规划控制、执行时序一起优化。

## 核心贡献
1. 明确把 **end-to-end deployment speed** 当成核心目标，而不只看单次推理速度。
2. 在 Realtime-VLA 基础上补齐真实机器人连续执行中的抖动、时序错位和轨迹不顺问题。
3. 强调轻量机械臂也能达到接近日常人类操作的速度与精度，说明 VLA 的工程落地开始成熟。
4. 论文与项目页都把“fast + smooth + accurate”并列，说明动作连续性已成为和成功率同等级的指标。

## 与主人研究的相关度
⭐⭐⭐⭐ 这对主人很有价值，因为空中平台比机械臂更怕动作抖动和延迟抖动，Realtime-VLA V2 的关注点和主人“慢语义 + 快控制”的工程矛盾完全同频。

## 对 Paper A 的启发
- 低层执行器不能只追求正确，还要追求 **连续、平滑、少抖动**。
- 论文 A 后续验收指标应补上 **trajectory smoothness / control jitter / chunk stitching stability**。
- 它和 Xiaomi-Robotics-0 形成互补：前者更像部署链路系统优化，后者更像异步执行训练与 chunk 对齐。

## 可落地实验点
1. 在 AirSim 记录 action chunk 续接处的速度突变、姿态抖动和控制延迟。
2. 给主人现有空中 VLA 原型新增 3 个指标：轨迹平滑度、控制抖动率、chunk 拼接误差。
3. 做一版“VLM 慢规划 + 低层缓存轨迹滚动执行”的轻量原型，对比是否明显减抖。

## 局限 / 不足
- 当前信息主要来自摘要和项目页，method / experiments 细节还需后续补读。
- 重点仍在机械臂任务，对空中高动态平台的结论需要主人自己迁移验证。
- 它更偏工程调优，不直接解决高层语义意图与低层控制解耦问题。

---
🦊 花火 | 2026-04-09 heartbeat 深挖
