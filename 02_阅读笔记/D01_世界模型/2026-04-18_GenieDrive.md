---
title: "GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation"
authors: "Yang, Liu, Lu, Hou, Miao, Peng, Feng, Bai, Zhao"
arxiv: 2512.12751
date: 2025-12-14
institution: 科研机构
conf: arXiv
keywords: [driving world model, 4D occupancy, video generation, physics-aware]
tags: [隐空间世界模型, 视频生成, 物理一致性]
summary: "GenieDrive 用 4D 占用作为中间物理表征，再条件生成驾驶视频，提升了世界模型的物理一致性与效率。"
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2512.12751_GenieDrive.pdf"
reading_date: 2026-04-18
reading_status: 已读
related_concepts: ["隐空间世界模型", "视频生成", "物理一致性"]
---

# 📖 花火格式笔记

## 🎯 题目

GenieDrive: Towards Physics-Aware Driving World Model with 4D Occupancy Guided Video Generation

## 📝 三句摘要

1. **问题背景**：现有驾驶世界模型直接从动作/控制信号预测视频，存在物理不一致（物体穿墙、违反重力等）问题；且纯扩散方法难以精确建模 3D 空间结构的动态演化。
2. **核心方法**：提出两段式架构——先预测 4D 占用（含 3D 结构+时间维度的动态演化），再以占用为条件生成视频，实现物理感知的世界建模。
3. **关键结果**：latent 尺寸降至前人方法的 58%（VAE 三平面编码），推理速度 41 FPS，预测 mIoU 提升 7.2%，视频生成 FVD 降低 20.7%，显著提升物理一致性。

## 💎 价值评估

- **🔬 研究价值**：首创 4D 占用作为物理载体，解决视频生成物理一致性问题，架构有示范意义
- **🚀 实践价值**：两段式架构（占用→视频）可用于 UE 数据采集后的仿真数据飞轮构建
- **📈 扩展潜力**：占用预测可扩展到无人机、机器人等需要空间推理的场景

## 🎯 可落地实验点

**实验设计**：UE 仿真器输出中间占用表征 → GenieDrive 式两段式方法生成多视角视频
- 对比基线：单阶段视频扩散（无占用中间层）
- 度量指标：视频生成 FVD / 占用预测 mIoU / 物理违规率
- 预期结果：两段式方法在物理一致性指标上显著超越单阶段基线

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。

- [[concepts/隐空间世界模型]] - 本文在隐空间建模 4D 占用动态
- [[concepts/视频生成]] - 视频生成是最终输出形式
- [[concepts/物理一致性]] - 本文核心要解决的问题，提升视频生成的物理合理性
- [[concepts/动作条件预测]] - 占用演化以控制信号为条件

## 🔗 相关链接

- [[2026-04-18_GaussianDWM]] - GaussianDWM：3DGS 统一感知与生成的世界模型
- [[2026-04-18_OmniNWM]] - OmniNWM：隐空间世界模型先驱

## 📌 待探索问题

- 4D 占用预测的计算开销如何？实时性是否能在嵌入式平台达到？
- 两段式训练是否存在错误累积问题，占用预测误差如何反向传播到视频生成模块？

---
**维护**: 花火 · 2026-04-18
