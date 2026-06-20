---
type: "source"
id: "source.2026-05-31_BAE_Bundle_Adjustment_Eager_Mode"
pageType: "source"
tags: ["Bundle Adjustment", "PyTorch", "GPU加速", "稀疏优化", "SLAM", "Levenberg-Marquardt"]
summary: "问题背景: 传统 Bundle Adjustment (BA) 优化库（GTSAM、g2o、Ceres）基于 eager-mode 执行，难以与现代 PyTorch 生态的自动微分和 GPU 加速无缝结合，且无法利用稀疏 Jacobian/Hessian 结构进行高效二阶优化。"
origins: ["../../02_阅读笔记/D09_感知与3D视觉/2026-05-31_BAE_Bundle_Adjustment_Eager_Mode.md"]
updated: "2026-06-02"
---

# Bundle Adjustment in the Eager Mode (BAE, 2409.12190)

**核心价值**: 问题背景: 传统 Bundle Adjustment (BA) 优化库（GTSAM、g2o、Ceres）基于 eager-mode 执行，难以与现代 PyTorch 生态的自动微分和 GPU 加速无缝结合，且无法利用稀疏 Jacobian/Hessian 结构进行高效二阶优化。

**原始资料**:
- [[../../02_阅读笔记/D09_感知与3D视觉/2026-05-31_BAE_Bundle_Adjustment_Eager_Mode.md]]
