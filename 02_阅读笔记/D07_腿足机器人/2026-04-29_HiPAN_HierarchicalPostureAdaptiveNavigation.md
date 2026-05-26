---

title: "HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments"
authors: Jeil Jeong, Minsung Yoon, Seokryun Choi, Heechan Shin, Taegeun Yang, Sung-eui Yoon
arxiv: 2604.26504
date: 2026-04-29
institution: KAIST
conf: RA-L 2026
keywords: [腿足机器人, 语义导航, 运动控制, 3D视觉]
tags: []
domain: 腿足机器人
pdf_path: "../../01_论文库/腿足机器人/2604.26504_HiPAN_Hierarchical_Posture_Adaptive_Navigation_for_Quadruped_Robots.pdf"
reading_date: 2026-05-03
reading_status: 已读
related_concepts: ["语义导航", "运动控制"]
---

# 📖 花火格式笔记

## 🎯 题目

HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments

## 📝 三句摘要

1. **问题背景**：四足机器人在狭窄、低矮和复杂 3D 地形中导航时，不仅要避障，还要动态调整身体姿态，传统 mapping-planning 管线误差累积且算力开销高。
2. **核心方法**：HiPAN 用层次化架构直接基于 onboard depth image 输出高层导航指令与 body posture，再由低层姿态自适应 locomotion controller 执行，并用 Path-Guided Curriculum Learning 拉长导航时域。
3. **关键结果**：论文在仿真和真实世界都展示了比经典 reactive planner 与端到端基线更好的导航成功率与路径效率，且已被 RA-L 2026 接收。

## 💎 价值评估

- **🔬 研究价值**：为 D03/D06 相关的空地迁移与复杂环境导航提供了“高层导航 + 低层姿态控制”分层范式证据。
- **🚀 实践价值**：对主人未来做 UAV/UGV/四足跨平台导航时很有启发，尤其是姿态约束与狭窄空间通行问题。
- **📈 扩展潜力**：可作为 D03 空地迁移里的地面腿足导航锚点，也能和 D06 的 3D VLN 做“语义指令→姿态/速度子目标”的接口对照。

## 🎯 可落地实验点

**实验设计**：把“高层规划输出 body posture / velocity command，低层 controller 跟踪”的两层结构迁到主人后续 UAV/地面平台导航对比实验中。
- 对比基线：传统 map-planner + controller / end-to-end policy / hierarchical posture-aware policy
- 度量指标：成功率、路径效率、狭窄通道通过率、姿态调整次数
- 预期结果：层次化 posture-aware 路线在非结构化 3D 环境里更稳，且更容易跨平台复用高层语义策略

## 🔗 知识图谱

- [[语义导航]] - 导航问题主轴
- [[运动控制]] - 低层执行控制
- [[3D视觉]] - 深度图感知输入

## 🔗 相关链接

- [[2026-04-15_Gupta2026_KinematicIntelligence]] - 都涉及跨本体结构约束，但 HiPAN 聚焦导航姿态适配

## 📌 待探索问题

- 这类 posture token 能否直接接到空中 VLN 的高层子目标接口？
- 深度图直出高层命令的范式，能否迁到 UAV 狭窄空间穿越？

---
**维护**: 花火 · 2026-05-03
