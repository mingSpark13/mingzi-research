---
title: "Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers"
authors: Zi-Xin Zou, Zhipeng Yu, Yuan-Chen Guo, Yangguang Li, Ding Liang, Yan-Pei Cao, Song-Hai Zhang
arxiv: 2312.09147
date: 2023-12-11
institution: Tsinghua University, VAST
conf: CVPR 2024
keywords: ["3D reconstruction", "triplane", "Gaussian splatting", "transformer", "feed-forward"]
tags: ["3D高斯溅射", "3D重建", "Transformer"]
summary: "TGS 用三平面与高斯混合表征连接 transformer 与显式几何，在单图输入下实现秒级 3D 重建并保持较强泛化性。"
domain: 3D视觉
pdf_path: "../../01_论文库/3D视觉/2312.09147_TGS.pdf"
reading_date: 2026-05-07
reading_status: 已读
related_concepts: ["3D高斯溅射", "3D重建"]
---

# 📖 花火格式笔记

## 🎯 题目

Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers

## 📝 三句摘要

1. **问题背景**：基于 SDS 的单图 3D 优化速度极慢（数十分钟），而纯前馈方法要么速度尚可但质量差（三平面 NeRF 分辨率受限），要么依赖 heavy transformer 架构导致计算代价高
2. **核心方法**：TGS 提出混合三平面-高斯表征，用 point decoder 从单图预测点云作为显式先验，再由 triplane decoder 查询高斯特征，最后 MLP 解码为 3D 高斯；两阶段 transformer 架构避免直接回归非结构化高斯属性
3. **关键结果**：CVPR 2024，GSO 数据集上几何重建和新视角合成均超越 LRM 等基线，推理速度达秒级，泛化到真实图像

## 💎 价值评估

- **🔬 研究价值**：首次将三平面表征与 3D 高斯溅射融合为混合表征，point decoder 生成显式点云作为 transformer 与非结构化高斯之间的桥梁，显著降低学习难度
- **🚀 实践价值**：秒级推理 + 优秀泛化性 + CVPR 认证，适合作为需要快速从真实图像重建 3D 资产的机器人感知 pipeline 前置模块
- **📈 扩展潜力**：混合表征设计为其他前馈 3D 方法提供通用框架；高斯渲染速度可进一步支持实时场景重建应用

## 🎯 可落地实验点

**实验设计**：TGS 混合三平面-高斯用于机器人实时 3D 感知
- **对比基线**：LRM（三平面 NeRF）、SDS 优化方法（DreamFusion）、纯 3DGS 重建
- **度量指标**：
  - 几何质量（Chamfer Distance、F-Score on GSO）
  - 新视角渲染质量（PSNR、SSIM、LPIPS）
  - 推理速度（秒/物体）
  - 真实图像泛化性（手机拍摄物体）
- **预期结果**：TGS 在真实图像上泛化性显著优于 LRM，速度比 SDS 快 2-3 数量级，适合作为机器人抓取规划的前置 3D 重建模块

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。
> 字典真源：`06_知识Wiki/_views/概念关键词字典.md`
> 不确定时查字典别名表；字典外新概念写入 `06_知识Wiki/inbox.md`，不自行创建。

- [[3D高斯溅射]] - 本文渲染框架：3D 高斯作为场景表征，通过 splatting 实现快速可微渲染
- [[3D重建]] - 核心任务：单图→三维几何+新视角合成

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作），通常 2-5 篇。

- [[2024-LRM]] - LRM: Large Reconstruction Model，本文直接基座架构对比基线，TGS 采用类似三平面设计但加入高斯混合表征
- [[2023-3DGS]] - 3D Gaussian Splatting: 高斯溅射渲染基础，本文用高斯替代三平面 NeRF 实现快速渲染
- [[2024-SyncDreamer]] - SyncDreamer: 多视角生成方法，与 TGS 同年工作，从不同角度解决单图 3D 问题

## 📌 待探索问题

- point decoder 生成的点云精度对最终高斯质量的影响有多大？能否用更精细的点云解码器进一步提升？
- 混合三平面-高斯表征与纯 LRM 三平面相比，在机器人操作场景（如遮挡、部分视图）中的鲁棒性如何？
- TGS 的 transformer 规模与推理速度 trade-off 在边缘设备（嵌入式 GPU）上的实际部署可行性？

---
**维护**: 花火 · 2026-05-07
