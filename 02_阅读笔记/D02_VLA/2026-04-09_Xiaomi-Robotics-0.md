---
title: "Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution"
authors: Xiaomi Robotics Team
arxiv: 2602.12684
date: 2026-03-25
institution: Xiaomi
conf: arXiv
keywords: [VLA, real-time execution, async execution, action chunking, cross-embodiment, flow matching]
tags: ["VLA架构", "ACT动作分块", "流匹配", "跨载体泛化"]
domain: D02_VLA
pdf_path: "../../01_论文库/D02_VLA/2602.12684_Xiaomi-Robotics-0.pdf"
reading_date: 2026-04-09
reading_status: 已读
related_concepts: ["VLA架构", "ACT动作分块", "流匹配", "跨载体泛化"]
---

# 📖 花火格式笔记

## 🎯 题目

Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution

## 📝 三句摘要

1. **问题背景**：现有 VLA 模型在真机部署时面临推理延迟导致控制抖动、action chunk 时序不对齐等工程瓶颈，"效果好但跑不起来"是主要矛盾。
2. **核心方法**：通过大规模跨载体轨迹+视觉语言数据预训练增强泛化，引入异步执行训练机制处理真机 rollout 中的推理延迟，并对连续 action chunk 做时间对齐实现平滑实时执行，支持在消费级 GPU 上运行。
3. **关键结果**：在仿真和双臂精细操作真机任务上取得强结果，实现消费级 GPU 上的实时连续执行，验证了"工程可行的 VLA"路线。

## 💎 价值评估

- **🔬 研究价值**：把 VLA 的重点从"只拼效果"拉回"真机实时可连续执行"，异步执行训练机制是解决 VLM 推理延迟的实用方案，对空中平台尤其重要（飞行控制不能等慢速 VLM）。
- **🚀 实践价值**：异步执行机制可直接迁移到 UAV 平台；action chunk 时间对齐策略适合用滚动式片段续接降低控制抖动；消费级 GPU 可运行意味着 Jetson/工控机部署可行。
- **📈 扩展潜力**：异步 chunk + PID/MPC 组合可在 AirSim 先验证，再决定是否接真机；跨载体预训练策略可扩展到空地联合预训练。

## 🎯 可落地实验点

**实验设计**：用 π0.5 / OpenVLA 做基座，单独复现异步执行机制，在 AirSim 中验证"异步 chunk + PID/MPC"组合对 UAV 控制延迟和抖动的改善效果。
- 对比基线：同步执行 VLA（每步等待完整推理）、标准 action chunking、本文异步执行
- 度量指标：Jetson/工控机上的 chunk latency、控制抖动（角速度方差）、轨迹连续性
- 预期结果：异步执行显著降低控制延迟，chunk 时间对齐减少抖动，整体轨迹更平滑

## 🔗 知识图谱

- [[concepts/VLA架构]] - 本文核心：面向真机实时部署的 VLA 工程化架构
- [[concepts/ACT动作分块]] - action chunk 时间对齐是本文关键工程贡献
- [[concepts/流匹配]] - 使用 flow matching 生成连续动作，支持精细操作
- [[concepts/跨载体泛化]] - 跨载体预训练是本文泛化能力的来源

## 🔗 相关链接

- [[2026-05-27_2601.02456_InternVLA-A1]] - InternVLA-A1 关注动态场景泛化，本文关注实时执行，两者互补
- [[ManualVLA_ChainOfThought_2512.02013]] - 同期 VLA 工作，关注推理链；本文关注执行效率

## 📌 待探索问题

- 异步执行训练中，如何处理"旧 chunk 还在执行、新推理已完成"时的动作切换平滑性问题？
- 跨载体预训练数据中，空中平台（UAV）的动力学特性与地面机械臂差异极大，直接混训是否会相互干扰？

---
**维护**: 花火 · 2026-05-27（规范化自 2026-04-09 旧笔记）
