---
title: "DriveVGGT: Calibrated Visual Geometry Transformer for Multi-Camera Autonomous Driving"
authors: "Yulu Dai, Zeyu Li, Jiahui Wang et al."
arxiv: "2511.22264"
date: 2025-11-18
institution: "Tsinghua University / Multiple Institutions"
conf: "CVPR 2025"
keywords: ["VGGT", "Multi-Camera", "Autonomous Driving", "Depth Estimation", "Pose Estimation"]
tags:
  - 感知与3D视觉
  - 3D重建
  - SLAM
  - 深度估计
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2511.22264_DriveVGGT.pdf"
reading_date: 2026-04-18
reading_status: 已读
related_concepts: ["感知与3D视觉", "3D重建", "SLAM", "深度估计"]
summary: "DriveVGGT 把标定信息与多相机先验注入前馈几何 Transformer，在自动驾驶长序列上同时提升重建精度与推理效率。"
---

# 🎯 题目

DriveVGGT: Calibrated Visual Geometry Transformer for Multi-Camera Autonomous Driving

# 📝 三句摘要

1. **问题背景**：将通用前馈视觉几何重建模型 VGGT 直接迁移到自动驾驶多相机场景时，面临稀疏重叠（360°覆盖导致相机间重叠小）、标定信息未被利用、外参恒定先验未被建模三大挑战。
2. **核心方法**：DriveVGGT 提出三处针对性改进：TVA（Temporal Video Attention）独立处理各相机；MCA（Multi-camera Consistency Attention）+ scale head 利用标定信息实现绝对尺度重建；分解 pose head 和 ego motion head 建模外参恒定先验。
3. **关键结果**：在长序列场景下推理时间降低 49.3%，同时深度和位姿估计精度提升；对主人的无人机多传感器融合设计有直接参考价值。

# 💎 价值评估

- **🔬 研究价值**：证明自动驾驶领域特有先验（标定信息、外参恒定）可显著改善前馈重建效果，为领域适配几何重建提供了新思路。
- **🚀 实践价值**：TVA + MCA 架构可迁移到无人机多传感器融合；推理速度 -49.3% 对实时采集系统有工程价值。
- **📈 扩展潜力**：标定约束融合思路可推广到任意多相机机器人平台（如机械臂眼在手、无人机机巢等）。

# 🎯 可落地实验点

**实验设计**：参考 DriveVGGT 的"相机独立处理 + 标定约束融合"设计主人的多传感器数据采集系统
- 对比基线：直接使用 VGGT 前馈结果，不加标定约束
- 度量指标：深度估计误差（RMSE）、位姿估计精度（ATE）、推理延迟（ms/frame）
- 预期结果：在有标定信息的无人机多相机数据上，深度/位姿精度提升 10-20%，延迟降低 30-50%

# 🔗 知识图谱

- [[concepts/感知与3D视觉]] - DriveVGGT 的核心任务，即从多相机图像恢复三维结构
- [[concepts/3D重建]] - 基于 Transformer 的前馈 3D 重建方法，输入视频输出点云/深度/位姿
- [[concepts/SLAM]] - 与 SLAM 的关联：同样解决相机-几何-位姿的联合估计问题，但 DriveVGGT 是前馈而非优化
- [[concepts/深度估计]] - 深度估计是 DriveVGGT 的核心输出之一，scale head 实现绝对尺度恢复

# 🔗 相关链接

- [[2026-04-18_SimScale]] - SimScale 同样关注自动驾驶感知-规划 pipeline，可作数据合成视角对比
- [[2026-04-18_OmniVGGT]] - OmniVGGT 是 DriveVGGT 的基础模型，本文针对自动驾驶场景做领域适配

# 📌 待探索问题

- TVA 独立处理各相机虽然提高了效率，但损失了跨相机全局注意力，长基线场景下是否存在累积漂移？如何与全局 BA 结合？
- scale head 利用标定信息恢复绝对尺度，但当标定参数随时间漂移（如震动导致外参微变）时，系统如何鲁棒处理？

---
**维护**: 花火 · 2026-04-18
