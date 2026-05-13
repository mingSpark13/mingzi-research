---
title: Aerial Manipulation with Contact-Aware Onboard Perception and Hybrid Control
authors: Yuanzhu Zhan, Yufei Jiang
arxiv: 2602.08251
date: 2026-02-12
institution: 未知
conf: arXiv
keywords: [aerial manipulation, onboard perception, hybrid control, contact-rich manipulation]
tags: ["空中操作", "MPC", "运动控制", "主动感知"]
domain: 空中操作
pdf_path: "../../01_论文库/空中操作/2602.08251_Aerial_Manipulation_Contact_Aware_Onboard_Perception_Hybrid_Control.pdf"
reading_date: 2026-05-12
reading_status: 已读
related_concepts: ["空中操作", "MPC", "运动控制", "主动感知"]
---

# 📖 花火格式笔记

## 🎯 题目

Aerial Manipulation with Contact-Aware Onboard Perception and Hybrid Control

## 📝 三句摘要

1. **问题背景**：空中操作一旦进入接触阶段，外部定位缺失、接触扰动和感知漂移会一起放大，导致无人机难以稳定完成真实接触任务。
2. **核心方法**：论文提出全 onboard 的 contact-aware 感知-控制闭环，在 VIO 中加入接触一致性因子，并结合图像伺服与 hybrid force-motion control 做接触调节。
3. **关键结果**：实验显示其在接触时速度估计提升约 66.01%，且能在无 MoCap 条件下完成可靠接近、稳定贴靠与力调节，说明方案更接近真实部署。

## 💎 价值评估

- **🔬 研究价值**：它把“接触感知”真正并入空中操作状态估计和控制闭环，不再只做分离式轨迹跟踪，方向上很对。
- **🚀 实践价值**：对接触检测、表面巡检、擦拭、轻量操作这类 UAV 真实任务很有参考意义，尤其适合主人关注的空中操作线。
- **📈 扩展潜力**：后续可继续接 MPC、扰动观测器、力觉估计或更复杂末端执行器，走向更强的接触式 aerial manipulation。

## 🎯 可落地实验点

**实验设计**：在现有 UAV 接触控制仿真中对比普通 VIO 与 contact-aware VIO，评估接触阶段状态估计与力控稳定性。
- 对比基线：标准 VIO + 位置控制、无接触因子的视觉伺服方案
- 度量指标：接触阶段速度估计误差、法向力误差、稳定接触时长
- 预期结果：contact-aware 方案在接触瞬间与持续贴靠时显著更稳

## 🔗 知识图谱

- [[空中操作]] - 无人机执行接触式操作任务的核心设定
- [[运动控制]] - 接触期的姿态与运动调节是主问题之一
- [[主动感知]] - 利用接触一致性改善状态估计可视作任务相关主动感知
- [[MPC]] - 后续可直接嫁接到模型预测控制框架中增强部署性

## 🔗 相关链接

- [[2024-01_Flying_Calligrapher]] - 接触感知空中操作与力控的相关前作
- [[2022-01_Image_based_visual_impedance_force_control_for_contact_aerial_manipulation]] - 图像基础阻抗/力控路线的代表工作

## 📌 待探索问题

- 这套接触一致性 VIO 在更剧烈扰动或更长接触持续时间下，是否仍然稳定？
- 若换成更复杂工具端或抓取任务，hybrid force-motion control 是否需要任务级重构？

---
**维护**: 花火 · 2026-05-12
