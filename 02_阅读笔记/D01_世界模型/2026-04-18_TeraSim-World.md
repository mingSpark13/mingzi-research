---
type: paper
arXiv: 2509.13164
title: "TeraSim-World: Worldwide Safety-Critical Data Synthesis for End-to-End Autonomous Driving"
authors: Jiawei Wang, Haowei Sun, Xintao Yan, Shuo Feng, Jun Gao, Henry X. Liu
date: 2025-09
institution: University of Michigan / 多所机构
conf: arXiv
keywords: [数据合成, 仿真平台, 自动驾驶, 世界模型, Sim2Real]
tags:
  - 数据合成
  - 仿真平台
  - 视频生成
  - Sim2Real
  - 感知与3D视觉
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2509.13164.pdf"
reading_date: 2026-04-18
reading_status: 已读
related_concepts:
  - 数据合成
  - 仿真平台
  - 视频生成
  - Sim2Real
  - 感知与3D视觉
---

# TeraSim-World: Worldwide Safety-Critical Data Synthesis for End-to-End Autonomous Driving

## 🎯 题目

TeraSim-World: Worldwide Safety-Critical Data Synthesis for End-to-End Autonomous Driving

## 📝 三句摘要

1. **问题背景**：自动驾驶训练严重缺乏安全关键（corner case）数据，现有数据采集成本高、覆盖有限，无法覆盖全球地理多样性和极端场景。
2. **核心方法**：TeraSim-World 从任意地理位置自动获取真实地图和交通需求，用自然驾驶数据集模拟代理行为，通过对抗性编排生成极端场景；利用 Cosmos-Drive 视频生成模型实现照片级、地理锚定的传感器渲染（RGB/深度/LiDAR）。
3. **关键结果**：提供全球可扩展的安全关键数据合成方案，从任意地点自动生成多样化安全场景，弥合代理模拟与传感器模拟之间的鸿沟。

## 💎 价值评估

- **🔬 研究价值**：双层模拟分离设计（代理行为层 + 传感器渲染层）是数据合成的重要创新，全球地理多样性自动化生成解决了个性化场景覆盖难题。
- **🚀 实践价值**：与主人 UE 城市场景程序化生成方向高度契合；双层分离设计可直接应用于无人机 UE 数据采集的传感器模拟层。
- **📈 扩展潜力**：从自动驾驶迁移到无人机场景是自然扩展；对抗性场景编排方法可用于无人机安全关键数据增强。

## 🎯 可落地实验点

借鉴 TeraSim-World 双层模拟分离设计（代理行为层 + 传感器渲染层），为无人机 UE 数据采集设计：
- **代理行为层**：程序化场景生成（城市场景/障碍物/天气）的配置化框架
- **传感器模拟层**：RGB/深度/LiDAR 解耦配置，支持多传感器组合
- **对比基线**：现有单层仿真（场景即传感器）、TeraSim-World 风格双层分离
- **预期结果**：双层分离设计可实现场景配置与传感器配置的解耦，显著提升数据采集效率

## 🔗 知识图谱

- [[concepts/数据合成]] — 核心贡献：全球地理多样性的自动化安全关键数据合成，代理行为+传感器双层分离
- [[concepts/仿真平台]] — 从真实地图数据到 UE 仿真场景的自动化 pipeline，支撑可扩展数据生成
- [[concepts/视频生成]] — Cosmos-Drive 实现照片级传感器渲染，地理锚定的多模态视频生成
- [[concepts/Sim2Real]] — 街景驱动的地理锚定渲染降低 sim-to-real 差距，支撑策略零样本迁移
- [[concepts/感知与3D视觉]] — 多模态传感器模拟（RGB/深度/LiDAR）作为感知数据来源

## 🔗 相关链接

- [[2025-03_Cosmos-Drive]] - Cosmos-Drive：TeraSim-World 传感器渲染基础模型，实现照片级视频生成
- [[2024-12_SimWorld]] - SimWorld：具身智能仿真平台，可对比数据合成与仿真能力

## 📌 待探索问题

- TeraSim-World 的双层分离设计是否适用于无人机仿真？无人机视角下的传感器渲染质量（深度/LiDAR）与自动驾驶场景有何差异？
- 对抗性场景编排在无人机领域如何适配？空中障碍物（鸟类、无人机群）的行为建模是否已有成熟方案？

---
**维护**: 花火 · 2026-04-18
