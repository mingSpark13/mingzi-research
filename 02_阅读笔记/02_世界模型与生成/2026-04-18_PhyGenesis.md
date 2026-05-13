---
title: "Toward Physically Consistent Driving Video World Models under Challenging Trajectories"
authors: ""
arxiv: "2603.24506"
date: "2026-03-28"
institution: ""
conf: "arXiv"
tags:
  - "世界模型"
  - "物理一致性"
  - "视频生成"
  - "仿真平台"
domain: "世界模型"
pdf_path: "../../01_论文库/世界模型/2603.24506_PhyGenesis.pdf"
reading_date: "2026-04-18"
reading_status: "已读"
---

# 📖 花火格式笔记

## 🎯 题目

Toward Physically Consistent Driving Video World Models under Challenging Trajectories

## 📝 三句摘要

1. **问题背景**：现有驾驶世界模型在非完美轨迹（来自仿真器/规划系统生成）上存在物理不一致问题，直接输入无效轨迹会生成物理不合理视频。
2. **核心方法**：提出 PhyGenesis，引入 Physical Condition Generator 将任意轨迹条件转换为物理合理条件，再结合物理增强视频生成器，在 CARLA 仿真中训练。
3. **关键结果**：在多样化挑战性驾驶场景上显著优于 SOTA，物理一致性指标大幅提升，同时保持高视觉保真度。

## 💎 价值评估

- **🔬 研究价值**：首个针对"挑战性轨迹"提出物理一致性增强方案的驾驶世界模型，填补了仿真轨迹→真实视频生成中物理接地的空白。
- **🚀 实践价值**：与 UE 数据采集主线的"程序化场景生成"方向高度契合，PhyGenesis 的两阶段框架可直接迁移到 UE 数据合成流程。
- **📈 扩展潜力**：Physical Condition Generator 思想可泛化到无人机/机械臂等其他具身场景的 world model 训练。

## 🎯 可落地实验点

**实验设计**：借鉴 PhyGenesis 的两阶段框架（物理条件生成 + 视频生成），在 UE 中设计物理违规检测模块，对程序化生成的轨迹做物理合理性过滤，再进行世界模型数据增强。
- 对比基线：直接使用全部合成轨迹 vs 物理过滤后的轨迹
- 度量指标：生成视频的物理一致性评分、下游规划任务成功率
- 预期结果：物理过滤后的数据训练出的 world model 在真实场景中物理违规率更低

## 🔗 知识图谱

> 链接本文涉及的核心概念，必须使用字典 v1.1 二级规范名。

- [[concepts/世界模型]] - 驾驶世界模型核心，生成未来驾驶场景视频
- [[concepts/物理一致性]] - 核心贡献，确保生成视频符合物理定律
- [[concepts/视频生成]] - 面向具身任务的视频生成
- [[concepts/仿真平台]] - CARLA 仿真平台提供挑战性场景

## 🔗 相关链接

> 链接本文核心引用的相关论文。

- [[2026-04-18_GenieDrive]] - GenieDrive：驾驶世界模型相关工作
- [[2026-04-18_MAD]] - MAD：视频生成与 world model 结合的工作

## 📌 待探索问题

- Physical Condition Generator 能否扩展到非 CARLA 仿真环境（如 UE）生成的轨迹？
- 如何在物理一致性和视觉保真度之间做帕累托最优权衡？

---
**维护**: 花火 · 2026-04-18
