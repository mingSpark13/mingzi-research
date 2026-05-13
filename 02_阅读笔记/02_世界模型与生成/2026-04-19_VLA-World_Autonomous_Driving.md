---
title: Learning Vision-Language-Action World Models for Autonomous Driving
authors: Yuxi Li, Shangjie Li, Huan Ang, Tianfu Wang, Yuxiang Zhou, Xiangrui Kong, Yuanhan Zhang, Hanqing Lu, Hang Zhao
arxiv: 2604.09059
date: 2026-04-14
institution: Shanghai AI Laboratory; Tsinghua University; Zhejiang University; Horizon Robotics
conf: CVPR 2026 Findings
keywords:
- Autonomous Driving
- Vision-Language-Action
- World Model
- Trajectory Planning
- nuScenes
tags:
- 隐空间世界模型
- VLA架构
- 动作条件预测
- 多模态统一架构
- 实时推理
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2604.09059_VLA-World_Autonomous_Driving.pdf
reading_date: 2026-04-19
reading_status: 待读
related_concepts:
- 隐空间世界模型
- VLA架构
- 动作条件预测
- 多模态统一架构
- 实时推理
summary: VLA-World 将视觉、语言与动作统一进 latent world model，通过 action-conditioned rollout 同时建模未来世界演化与轨迹规划。
---
## 🎯 题目

Learning Vision-Language-Action World Models for Autonomous Driving

## 📝 三句摘要

1. **问题背景**：自动驾驶端到端规划模型往往只直接预测轨迹，缺少对环境演化的显式内部建模，导致安全性、可解释性和长时预测能力不足。
2. **核心方法**：论文提出 VLA-World，把视觉、语言导航指令与动作统一进世界模型框架，在 latent state 中做 action-conditioned future rollout，并联合优化轨迹规划与未来世界演化建模。
3. **关键结果**：在 nuScenes 相关规划评测上，VLA-World 在轨迹误差和碰撞率上优于既有 autoregressive / non-autoregressive 规划基线，说明把 VLA 与 world model 合起来对自动驾驶决策是有效的。

## 💎 价值评估

- **🔬 研究价值**：它不是单纯把 VLM 接到 driving policy 后面，而是把“语言条件 + 动作条件 + 世界演化”统一建模，属于比较干净的 VLA-world model 路线，对主人后续做 UAV VLA 世界模型很有参考意义。
- **🚀 实践价值**：自动驾驶和无人机虽然平台不同，但都面临部分可观测、强安全约束、长时规划的问题；其中 latent rollout、action-conditioned transition、trajectory fidelity 这几块都能直接迁移思路。
- **📈 扩展潜力**：很适合往“世界模型辅助控制而不是纯视频生成”方向延展，比如给主人做无人机导航/跟踪时引入 future latent imagination、collision-aware planning、语言条件任务切换。

## 🎯 可落地实验点

**实验设计**：在主人的无人机导航或跟随任务里复现一个轻量版 VLA-World
- 对比基线：纯 VLA policy / 无 world model 的端到端轨迹回归 / 带 latent rollout 的 action-conditioned VLA-world model
- 度量指标：轨迹 L2 误差、碰撞率、任务成功率、推理延迟
- 预期结果：加入 latent world rollout 后，在复杂动态场景下鲁棒性与安全性更好，尤其在被遮挡、目标临时消失、环境扰动时更稳

## 🔗 知识图谱

- [[concepts/隐空间世界模型]] - 在 latent space 中建模未来世界演化
- [[concepts/VLA架构]] - 视觉-语言-动作统一端到端建模
- [[concepts/动作条件预测]] - 以动作作为条件预测未来状态
- [[concepts/多模态统一架构]] - 联合处理视觉、语言与动作信号
- [[concepts/实时推理]] - 面向在线规划的低延迟决策

## 🔗 相关链接

- [[2026-03-27_RT-2]] - 早期 VLA 代表工作，提供视觉语言到动作统一建模范式
- [[2026-03-27_OpenVLA]] - 开源 VLA 路线代表，适合作为对照理解 action generation 设计
- [[2026-04-08_WowWoVal_EmbodiedWorldModel]] - 可搭配阅读其评测维度，理解 embodied world model 的好坏该怎么量

## 📌 待探索问题

- 这种 driving 场景中的 latent world rollout，如果迁移到无人机，面对更强三维运动和视角变化时是否仍稳定？
- 语言信号在自动驾驶里通常较弱，如果换成更强任务条件（如目标描述、追踪指令、空域规则），VLA 部分会不会带来更大收益？

---
**维护**: 花火 · 2026-04-19
