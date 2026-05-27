---
title: "FoundationPose: Unified 6D Pose Estimation and Tracking"
authors: NVIDIA Team
arxiv: ""
date: 2024
institution: NVIDIA
conf: ""
keywords: 6D pose estimation, pose tracking, foundation model, manipulation
tags: ["灵巧操作"]
domain: 视觉感知
pdf_path: ""
reading_date: 2026-03-27
reading_status: 已读
related_concepts: ["灵巧操作"]
---

## 🎯 题目

FoundationPose — 统一 6D 位姿估计与跟踪的基础模型

## 📝 三句摘要

1. **问题背景**：6D 位姿估计是机器人操作的关键感知能力，但传统方法依赖 CAD 模型，对新物体泛化能力差。
2. **核心方法**：FoundationPose 定义为 unified 6D pose estimation and tracking foundation model，支持 model-based 和 model-free 两种模式，新物体可在测试时直接用 CAD 或少量参考图启动。
3. **关键结果**：在未知物体 6D 跟踪和位姿估计上展示了较强的泛化能力，是当前最值得关注的 6D pose 开源方案之一。

## 💎 价值评估

- **🔬 研究价值**：将 6D pose 估计推向 foundation model 范式，解决了「依赖特定物体模型」的传统限制。
- **🚀 实践价值**：代码开源，适合作为「机器人操作感知模块」的即插即用组件；与 GraspNet 等抓取检测模块高度互补。
- **📈 扩展潜力**：可与 Diffusion Policy/ACT 等 policy 结合形成「感知-规划-执行」闭环；也是面试机器人感知方向的重要话题。

## 🎯 可落地实验点

**实验设计**：FoundationPose + GraspNet 在「已知/未知物体抓取」任务上的集成实验
- 对比基线：只用 RGBD 几何方法（ICP）、只用 GraspNet 抓取候选
- 度量指标：抓取成功率、位姿估计误差、推理延迟
- 预期结果：FoundationPose 提供精确 6D pose 能显著提升抓取准确性

## 🔗 知识图谱
- [[6D Pose Estimation]]
- [[位姿跟踪]]
- [[VLA架构]]
- [[机器人感知]]
- [[抓取检测]]

## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- [[2026-03-27_GraspNet]] - FoundationPose 可与 GraspNet 串联形成完整抓取 pipeline
- [[2026-03-27_BundleSDF]] - BundleSDF 是另一个 6D 跟踪方案，可做技术对比

## 📌 待探索问题

- FoundationPose 在遮挡严重场景下的鲁棒性如何？
- model-free 模式需要的「少量参考图」具体需要多少张？

---
**维护**: 花火 · 2026-04-12
