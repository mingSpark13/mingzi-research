---
title: "NaVILA: Two-Level Vision-Language-Action Framework for Legged Robot Navigation"
authors: ""
arxiv: ""
date: 2025
institution: ""
conf: RSS 2025 (arXiv 2024)
keywords: two-level framework, VLA, locomotion policy, legged robot, real-world deployment
tags: ["D06", "VLA", "腿足机器人"]
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["腿足机器人"]
---

## 🎯 题目

NaVILA: 两层视觉-语言-动作框架（四足机器人导航）

## 📝 三句摘要

1. **问题背景**：很多 VLA 方法直接输出离散动作 token，在真实四足/轮式机器人上部署时缺乏实时障碍规避能力，动作执行不够平滑。
2. **核心方法**：提出两层架构：上层 VLA 输出带空间信息的语言式中层指令（如"向前 75cm"）；下层实时 locomotion policy 负责障碍规避和执行。
3. **关键结果**：在四足机器人上实现真实世界部署验证，两层分离架构被验证能兼顾高层语义正确性和低层运动稳定性。

## 💎 价值评估

- **🔬 研究价值**：明确了 VLA 系统的层次化部署范式，为"语言决策 + 运动控制"的系统架构提供了设计参考。
- **🚀 实践价值**：与主人"龙虾/大模型只做'往哪、为什么' + 低层控制器负责'怎么稳地走/飞过去'"的设想完全吻合，是四足/飞行器导航系统的设计蓝图。
- **📈 扩展潜力**：上层 VLA 可替换为 Nav-R2/DRIVE-Nav，下层 locomotion policy 可复用现有四足/无人机控制器。

## 🎯 可落地实验点

**实验设计**：以 DRIVE-Nav 或 Nav-R2 作为上层语义决策，以 Unitree Go2 原始 locomotion policy 作为下层，构建完整四足语义导航系统
- 对比基线：端到端 VLA 方法（如 RT-2）
- 度量指标：Navigation Success Rate、Obstacle Avoidance Rate、End-to-End Latency
- 预期结果：两层架构在障碍密集场景下成功率提升 >20%，实时性更好

## 🔗 知识图谱
- [[两层架构]]
- [[视觉语言动作模型]]
- [[实时运动控制]]
- [[四足机器人]]
- [[具身智能]]

## 🔗 相关链接

- [[2025_Nav-R2_RGB_Only_Navigation]] - Nav-R2 可作为 NaVILA 上层 VLA 候选
- [[2026_DRIVE-Nav_Directional_Reasoning_Navigation]] - DRIVE-Nav 可作为 NaVILA 上层语义决策头

## 📌 待探索问题

- 两层之间指令频率如何匹配？VLA 输出"向前75cm"后，locomotion policy 如何处理指令执行的中断和重新规划？
- 在空中机器人场景下，locomotion policy 替换为飞行控制时，两层架构是否依然有效？

---
**维护**: 花火 · 2026-04-12
