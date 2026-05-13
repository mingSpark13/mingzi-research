---
title: "DriveArena: A Closed-loop Generative Simulation Platform for Autonomous Driving"
authors: Xuemeng Yang, Licheng Wen, Yukai Ma, Jianbiao Mei, Xin Li, Tiantian Wei, Wenjie Lei, Daocheng Fu, Pinlong Cai, Min Dou, Botian Shi, Liang He, Yong Liu, Yu Qiao
arxiv: 2408.00415
date: 2024-08
institution: "上海人工智能实验室"
conf: arXiv
keywords: Closed-loop simulation, Generative model, Autonomous driving, World model
tags: ["仿真平台", "数据飞轮", "视频生成"]
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2408.00415_DriveArena.pdf"
reading_date: 2026-04-18
reading_status: 已读
summary: "驾驶智能体在真实场景中评测缺乏可控、可复现的闭环仿真平台，现有方法难以生成无限自动驾驶场景。 DriveArena 采用模块化架构，Traffic Manager 生成真实交通流，World Dreamer（条件生成模型）生成逼真图像，智能体输出轨迹后被 Traffic Manager 处理，生成新场景布局再传回 World Dreamer，实现闭环迭代。 任意能处理真实图像的驾驶智能体都能在 DriveArena 中导航；支持在不同城市街道图上生成多样化交通流，实现真实感交互。"
---

## 🎯 题目

DriveArena: A Closed-loop Generative Simulation Platform for Autonomous Driving

## 📝 三句摘要

1. **问题背景**：驾驶智能体在真实场景中评测缺乏可控、可复现的闭环仿真平台，现有方法难以生成无限自动驾驶场景。
2. **核心方法**：DriveArena 采用模块化架构，Traffic Manager 生成真实交通流，World Dreamer（条件生成模型）生成逼真图像，智能体输出轨迹后被 Traffic Manager 处理，生成新场景布局再传回 World Dreamer，实现闭环迭代。
3. **关键结果**：任意能处理真实图像的驾驶智能体都能在 DriveArena 中导航；支持在不同城市街道图上生成多样化交通流，实现真实感交互。

## 💎 价值评估

- **🔬 研究价值**：首个基于生成式图像的闭环驾驶仿真平台，World Dreamer 解决无限 autoregression 下的图像一致性。
- **🚀 实践价值**：对主人 UE 数据采集方案有参考意义——程序化场景生成 + 传感器仿真是核心链路。
- **📈 扩展潜力**：可与主人研究方向结合，探索生成式仿真替代传统渲染管线的可行性。

## 🎯 可落地实验点

**实验设计**：参考 DriveArena 的模块化仿真架构，设计 UE 中的程序化场景生成方案
- 核心组件：Traffic Manager（场景流生成）+ World Dreamer（图像生成）
- 对比基线：传统渲染仿真 vs 生成式仿真
- 预期结果：生成式仿真在场景多样性上优于传统渲染

## 🔗 知识图谱

- [[仿真平台]] - 模块化 Traffic Manager + World Dreamer 架构
- [[数据飞轮]] - 仿真数据支持驾驶策略持续改进
- [[视频生成]] - World Dreamer 实现逼真图像无限自回归生成

## 🔗 相关链接

- [[2026-04-18_GenieDrive]] - 同样关注生成式闭环驾驶仿真，可作方法对照
- [[2026-04-18_HUGSIM]] - 另一类高保真驾驶仿真平台，对比生成式与重建式路线

## 📌 待探索问题

- World Dreamer 的长时闭环一致性在极端交通交互下会不会迅速退化？
- 若迁移到无人机/空中机器人场景，Traffic Manager 应如何替换为可微或可规则约束的空域交互生成器？

---
**维护**: 花火 · 2026-04-18（批量入库）
