---
title: "Human2Nav: Learning Crowd Navigation from Human Videos across Robots via Feasibility-Guided Flow Matching"
authors: Shenghong Zhang, Junjie Chen, Sichi Yan, Yutong Ban, Xiao Li
arxiv: ""
date: 2026-05-01
institution: 未知（待补）
conf: ICRA 2026
keywords: [人群导航, 流匹配, 跨机器人泛化, 人类视频模仿学习, 可行性引导]
tags: ["语义导航", "跨载体泛化", "流匹配"]
domain: 语义导航
summary: "通过人类视频学习跨机器人的人群导航策略，用流匹配建模人类运动模式，引入推理时可行性引导机制弥合机体差距。"
pdf_path: ""
video_source: "https://b23.tv/G4gpwzd"
reading_date: 2026-05-01
reading_status: 已看视频摘要
related_concepts: ["流匹配", "人群导航", "跨机器人迁移", "人类视频模仿学习"]
---

# 📖 花火格式笔记

## 🎯 题目

Human2Nav: Learning Crowd Navigation from Human Videos across Robots via Feasibility-Guided Flow Matching

## 📝 三句摘要

1. **问题背景**：机器人在动态人群中导航需要大规模演示数据，但物理平台采集成本高且不安全，人类视频是丰富且可扩展的替代来源，但存在机体差距（embodiment gap）挑战。
2. **核心方法**：提出 Human2Nav，用鸟瞰图（BEV）表示对齐视觉观察，训练条件流匹配模型捕捉人类导航细微模式；引入**推理时可行性引导机制**，无需重训练即可让生成的轨迹满足不同机器人的运动学和动力学约束。
3. **关键结果**：在仿真和真实异构机器人平台上验证，Human2Nav 在数据效率和导航性能上优于基于模型和学习的方法，同时保证跨人群场景的安全可执行轨迹。

## 💎 价值评估

- **🔬 研究价值**：流匹配用于人群导航是较新的结合点；推理时可行性引导无需重训练即可跨机器人迁移，对 D04 跨载体泛化和 D06 空中VLN 都有参考价值。
- **🚀 实践价值**：直接用人类视频训练，数据采集成本低；异构机器人验证说明泛化能力强，工业场景（无人机/地面机器人）均可应用。
- **📈 扩展潜力**：可探索将可行性引导与 D06 的 L0-L3 实验路由表结合；流匹配框架能否迁移到空中动态场景（如障碍物丰富的室内环境）是潜在创新点。

## 🎯 可落地实验点

**实验设计**：在 Human2Nav 仿真环境中复现，并尝试用 D06 的空中 VLN 设置替换地面导航
- 对比基线：原版 Human2Nav vs. 加入几何重定位补件 vs. 端到端方法
- 度量指标：导航成功率（SR）、路径效率、可执行轨迹比例
- 预期结果：可行性引导机制在异构 UAV 平台上可显著提升轨迹可执行率

## 🔗 知识图谱

- [[流匹配]] - 本文生成模型基础，conditional flow matching for trajectory generation
- [[人群导航]] - 本文核心任务，crowd navigation in dynamic environments
- [[跨机器人迁移]] - 本文解决的核心问题，embodiment gap across robot platforms
- [[人类视频模仿学习]] - 本文数据来源，learning from human videos
- [[可行性引导]] - 本文核心创新点，test-time feasibility guidance without retraining
- [[BEV表示]] - 本文观察空间对齐方式，bird's-eye-view representation

## 🏷️ 标签

#语义导航 #跨载体泛化 #流匹配 #人群导航
