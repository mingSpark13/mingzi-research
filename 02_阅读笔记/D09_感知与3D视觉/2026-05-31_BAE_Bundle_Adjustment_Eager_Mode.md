---
title: "Bundle Adjustment in the Eager Mode"
authors: Zitong Zhan, Huan Xu, Zihang Fang, Xinpeng Wei, Yaoyu Hu, Chen Wang
arxiv: "2409.12190"
date: 2026
institution: SAIR Lab (卡内基梅隆大学等)
conf: IEEE Transactions on Robotics (T-RO)
keywords: [Bundle Adjustment, PyTorch, GPU加速, 稀疏优化, SLAM, Levenberg-Marquardt, 微分优化]
tags: [3D视觉, 稀疏优化, 微分编程]
domain: 3D视觉
pdf_path: "../../01_论文库/3D视觉/2409_12190_BAE.pdf"
reading_date: 2026-05-31
reading_status: 在读
related_concepts: ["稀疏优化", "GPU加速", "非线性最小二乘", "SLAM后端", "微分编程"]
---

# 📖 花火格式笔记

## 🎯 题目

**Bundle Adjustment in the Eager Mode** — 让 BA 在 PyTorch 下提速 100x

## 📝 三句摘要

1. **问题背景**：传统 Bundle Adjustment (BA) 优化库（GTSAM、g2o、Ceres）基于 eager-mode 执行，难以与现代 PyTorch 生态的自动微分和 GPU 加速无缝结合，且无法利用稀疏 Jacobian/Hessian 结构进行高效二阶优化。

2. **核心方法**：提出 **BAE (Bundle Adjustment in the Eager Mode)** 库，实现稀疏感知自动微分设计 + GPU 加速稀疏张量算子，支持 exact 二阶优化（不近似），通过 `psjac` 装饰器追踪稀疏 Jacobian 结构，配合自定义 CUDA kernels 实现稀疏块运算。

3. **关键结果**：在大规模 BA 上，相比 GTSAM/g2o/Ceres 分别实现 **18.5x / 22x / 23x** 加速；在某些场景下端到端加速超过 **100x**；已集成进 PyPose v0.9.5 作为 LM 求解器的稀疏后端。

## 💎 价值评估

- **🔬 研究价值**：
  - 首个将稀疏 Jacobian 自动追踪与 PyTorch 原生自动微分深度融合的 BA 库
  - 证明了 exact second-order optimization 在大规模稀疏问题上可工程化落地
  - T-RO 2026 顶刊接收，学术认可度高

- **🚀 实践价值**：
  - 与 PyPose 无缝集成，可微分 BA 层可直接嵌入神经网络训练图
  - 支持 VGGT 等最新 SfM/MVS 工作流的 BA 精化步骤
  - Windows CUDA wheels 已发布，安装门槛低

- **📈 扩展潜力**：
  - Schur complement 加速（TODO）
  - CUDA graph 减少运行时开销（TODO）
  - DTensor 分布式支持（TODO）
  - NVIDIA AMGX 分布式求解器后端（TODO）

## 🎯 可落地实验点

**实验设计**：在无人机 SfM 重建流程中用 BAE 替换 Ceres 进行 BA 精化

- **对比基线**：原流程使用 Ceres Solver 的 BA 步骤
- **实现方案**：
  1. 使用 InstantSfM 或 COLMAP 快速重建作为初始化
  2. 提取共视特征点，构造 BA 问题
  3. 分别用 Ceres 和 BAE 求解，对比运行时间
  4. 对齐精度：用 GTSAM 或 OpenMVG 交叉验证重投影误差
- **度量指标**：
  - BA 步骤耗时（ms）
  - 最终 3D 点云重投影误差 (RMSE)
  - 内存占用峰值
- **预期结果**：BAE 在保证精度的前提下，显著加速 BA 步骤

## 🔗 知识图谱

- [[稀疏优化]] - 本文核心技术手段，稀疏 Jacobian/Hessian 的自动追踪与利用
- [[GPU加速]] - CUDA kernels 实现稀疏块矩阵运算，取代 CPU 库
- [[SLAM后端]] - BA 是 SLAM/SfM 后端的核心模块，本文改进其效率
- [[微分编程]] - 与 PyTorch 自动微分框架原生集成，支持端到端可微分

## 🔗 相关链接

- [PyPose/BAE GitHub](https://github.com/pypose/bae) - 官方开源实现
- [PyPose 库](https://github.com/pypose/pypose) - SE(3) 位姿表示与优化工具库
- [arXiv:2409.12190](https://arxiv.org/abs/2409.12190) - 原始论文

## 📌 待探索问题

1. **稀疏结构动态变化时 `psjac` 的开销**：当问题规模在优化过程中动态变化（如 BA 中加入新观测），稀疏 Jacobian 结构的重新追踪是否会成为瓶颈？
2. **与 Learning-based BA 的结合**：BAE 可微分特性是否适合作为 Neural BA 的可微 BA layer？当前 VGGT 集成只是后处理精化，能否 end-to-end gradient flowing？
3. **Schur complement 加速**：大规模 BA 的计算瓶颈通常在 Schur 消元，BAE TODO 列表中有此计划，实现后能否进一步 5-10x 加速？

---
**维护**: 花火 · 2026-05-31
**来源**: [B站视频: Bundle Adjustment in the Eager Mode, 让 BA 在 PyTorch 下提速100x](https://www.bilibili.com/video/BV1gaVj6YEM9)
