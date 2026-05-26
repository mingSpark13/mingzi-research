---
title: "Seamless Transition Control in Spring-Legged Quadrotors: A Hybrid Dynamics Perspective with Guaranteed Feasibility"
tags: ["运动控制"]
summary: "提出弹簧腿四旋翼统一混合轨迹优化与 HNMPC 控制框架，提升空地模式切换可行性与跟踪性能。"
authors: Hongli Li, Botao Zhang, Rui Mao, Tao Wang, Hui Cheng
arxiv: ""
date: 2025
institution: Sun Yat-sen University (中山大学)
conf: IROS 2025
keywords: hybrid control, legged-UAV, trajectory optimization, differential flatness, NMPC
domain: 运动控制
pdf_path: ../../01_论文库/运动控制/2025_Seamless_Transition_Control_in_Spring-Legged_Quadrotors.pdf
reading_date: 2025-03-14
reading_status: 已读
related_concepts: ["运动控制"]
---

## 🎯 题目

Seamless Transition Control in Spring-Legged Quadrotors: A Hybrid Dynamics Perspective with Guaranteed Feasibility

## 📝 三句摘要

1. **问题背景**：弹簧腿四旋翼在空中-地面模式切换时仅支持单一步态，混合轨迹优化和控制器切换困难
2. **核心方法**：首次证明弹簧腿四旋翼在飞行相和支撑相均满足微分平坦性，提出统一混合轨迹优化框架 + HNMPC控制器
3. **关键结果**：混合运动跟踪误差减少27%，支持多样化步态，实物平台验证

## 💎 价值评估

- **🔬 研究价值**：首次将微分平坦性推广到弹簧腿混合系统，为混合动力学控制提供理论基础
- **🚀 实践价值**：代码开源(GitHub)，混合轨迹优化框架可迁移到aerial manipulation的接触-操作序列
- **📈 扩展潜力**：被动弹性元件+主动控制的设计哲学可借鉴到可变刚度末端执行器

## 🎯 可落地实验点

**实验设计**：将混合轨迹优化思路应用到aerial manipulation的飞行-接触-抓取序列
- 对比基线：分段独立控制器 vs 统一混合优化
- 度量指标：模式切换时的力/位跟踪误差、成功率
- 预期结果：统一框架应减少切换抖动


## 🔗 知识图谱

- [[空中操作]]
- [[腿足机器人]]
- [[运动控制]]

## 🔗 相关链接

- [[2025-03-13_An-Integrated-Approach-to-Aerial-Grasping-Bistable-Gripper-Adaptive-Control]] - TMECH双稳态夹爪，同为UAV混合控制
- [[2025-03-13_Flying-Hand]] - 空中操作端到端框架

## 📌 待探索问题

- 弹簧参数（刚度/阻尼）如何整定？论文未详细讨论
- HNMPC的实时求解频率和计算负担？
- 混合轨迹优化能否扩展到六自由度接触操作？

---
**维护**: 花火 · 2026-04-12
