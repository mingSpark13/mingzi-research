---
title: "DCCS-Det: Directional Context and Cross-Scale-Aware Detector for Infrared Small Target"
authors: Shuying Li, Q Ma, S Zhang, Chuang Yang
arxiv: "2601.16428"
date: 2025-01
institution: 未知（见 PDF）
conf: IEEE Transactions on Geoscience and Remote Sensing (TGRS)
keywords: [红外小目标检测, IRSTD, 方向上下文, 跨尺度感知, 注意力机制]
tags: [感知与3D视觉, UAV跟踪]
domain: UAV跟踪
pdf_path: "../../01_论文库/UAV跟踪/2601.16428_DCCS-Det_IRSTD.pdf"
reading_date: 2026-04-25
reading_status: 已读
summary: "DCCS-Det通过方向上下文建模与跨尺度语义聚合提升红外小目标检测，在复杂背景下兼顾检测精度与推理效率。"
---

# 📖 花火格式笔记

## 🎯 题目

DCCS-Det: Directional Context and Cross-Scale-Aware Detector for Infrared Small Target
（面向红外小目标的方向上下文与跨尺度感知检测器）

## 📝 三句摘要

1. **问题背景**：红外小目标检测（IRSTD）中，现有方法难以同时建模局部-全局特征，且多尺度融合存在特征冗余和语义稀释问题，导致小目标与复杂背景难以区分。
2. **核心方法**：提出 DCCS-Det，包含两个核心模块——DSE（双流显著性增强）块通过局部感知与方向感知上下文聚合捕获远程空间依赖和局部细节；LaSEA（潜在感知语义提取与聚合）模块通过跨尺度特征提取和随机池化采样策略缓解特征退化、增强判别特征并抑制噪声。
3. **关键结果**：在多个 IRSTD 基准数据集上达到 SOTA 检测精度，同时保持有竞争力的推理效率；消融实验验证了 DSE 和 LaSEA 在复杂场景下的贡献。

## 💎 价值评估

- **🔬 研究价值**：DSE 的方向感知上下文聚合机制对捕获小目标的远程依赖有创新性；LaSEA 的随机池化采样策略是缓解深层特征退化的新思路，对 IRSTD 领域有参考价值。
- **🚀 实践价值**：直接面向遥感和无人机监视应用，对无人机载红外传感器的目标检测任务有直接工程意义；模块化设计可嵌入现有检测框架。
- **📈 扩展潜力**：DSE 的方向感知机制可迁移到可见光小目标检测；LaSEA 的跨尺度随机池化思路可用于其他密集预测任务（如语义分割）。

## 🎯 可落地实验点

**实验设计**：将 DCCS-Det 部署在无人机载红外相机实时检测流水线中，测试在高速飞行（背景运动模糊）和强杂波（云层/地面热源）场景下的检测鲁棒性
- 对比基线：ACM、ALCNet、DNANet 等主流 IRSTD 方法
- 度量指标：IoU、Pd（检测概率）、Fa（虚警率）、推理帧率（FPS）
- 预期结果：DCCS-Det 在强杂波场景下 Fa 显著降低，Pd 保持高水平

## 🔗 知识图谱

- [[感知与3D视觉]] - 红外图像感知与目标检测核心方向
- [[UAV跟踪]] - 本文直接面向无人机遥感监视应用场景

## 🔗 相关链接

- 暂无已入库相关论文（IRSTD 方向尚未建立笔记库）

## 📌 待探索问题

- LaSEA 的随机池化采样策略在训练时引入随机性，推理时是否使用确定性池化？对检测稳定性有何影响？
- DSE 的方向感知上下文聚合具体如何编码方向信息（可学习方向核 vs 固定方向滤波器）？与可变形卷积相比优势在哪里？

---
**维护**: 花火 · 2026-04-25
