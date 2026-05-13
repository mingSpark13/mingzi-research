---
title: "Similarity-Guided Layer-Adaptive Vision Transformer for UAV Tracking"
authors: "待补充"
arxiv: "2503.06625"
date: "2025-03"
institution: "待补充"
conf: "arXiv"
keywords: "UAV跟踪, Vision Transformer, 动态层选择, 实时跟踪, 计算效率"
tags: ["目标跟踪", "Vision Transformer", "模型压缩", "空中视觉语言导航"]
summary: SGLATrack 通过相似性引导的动态层选择裁掉 ViT 冗余计算，在保持接近 SOTA 精度的同时显著提升 UAV 跟踪实时性。
domain: "UAV目标跟踪"
pdf_path: "../../01_论文库/UAV跟踪/SGLATrack_2503.06625.pdf"
reading_date: "2026-04-07"
reading_status: "已读"
related_concepts: ["目标跟踪", "Vision Transformer", "模型压缩"]
---

## 🎯 题目
Similarity-Guided Layer-Adaptive Vision Transformer for UAV Tracking

## 📝 三句摘要
1. **问题背景**：完整 ViT 架构在 UAV 跟踪中计算量过大，许多层学习了冗余重复的目标表征，限制了实时部署能力。
2. **核心方法**：提出相似性引导的层自适应方法，动态禁用表征相似的冗余层，仅保留最优层，实现精度与速度平衡。
3. **关键结果**：在 6 个跟踪基准上验证有效性，实现接近 SOTA 的精度同时显著提升实时速度，适合资源受限平台。

## 💎 价值评估
- **🔬 研究价值**：把动态层选择引入 UAV 跟踪，说明 ViT 内部存在可利用的层冗余，对轻量化 Transformer 跟踪器设计有参考意义。
- **🚀 实践价值**：计算效率高，适合板载部署，适合作为主人后续无人机目标跟踪系统的高性价比候选。
- **📈 扩展潜力**：动态层裁剪机制可迁移到检测、姿态估计和视频理解等其他 ViT 推理任务。

## 🎯 可落地实验点
**实验设计：UAV 跟踪器的板载轻量化部署对比**
- 对比基线：SGLATrack vs ORTrack vs 标准 ViT tracker
- 度量指标：FPS、成功率、精度、GPU/CPU 占用
- 预期结果：SGLATrack 在边缘设备上实现更高实时性，并保持可接受的跟踪精度

## 🔗 知识图谱
- [[目标跟踪]]
- [[Vision Transformer]]
- [[模型压缩]]
- [[空中视觉语言导航]]

## 🔗 相关链接
- [[2026-04-07_ORTrack]] - 与本文同属 UAV 跟踪方向，可用于对比遮挡与实时性表现
- [[2026-04-07_YOPOv2]] - 可作为跟踪后端控制框架的衔接对象
- arXiv: https://arxiv.org/abs/2503.06625
- GitHub: https://github.com/GXNU-ZhongLab/SGLATrack

## 📌 待探索问题
- 动态禁用层在快速视角变化场景下是否会导致目标重识别能力下降？
- 这种相似性引导策略能否与多模态特征或时序建模进一步结合？

---
**维护**: 花火 · 2026-04-12
