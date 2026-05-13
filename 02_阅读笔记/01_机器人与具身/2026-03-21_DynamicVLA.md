---
title: "A Vision-Language-Action Model for Dynamic Object Manipulation"
authors: Haozhe Xie, Beichen Wen, Jiarui Zheng, Zhaoxi Chen, Fangzhou Hong, Haiwen Diao, Ziwei Liu
arxiv: "2601.22153"
date: "2026-01-29"
institution: "S-Lab, Nanyang Technological University"
conf: "arXiv 2601.22153 (cs.RO)"
keywords: "VLA, 动态物体操纵, LAAS, Continuous Inference, 闭环控制, DOM基准, 具身智能"
tags: ["D02"]
domain: "具身智能"
pdf_path: "../../01_论文库/具身智能/DynamicVLA_2601.22153.pdf"
reading_date: "2026-03-21"
reading_status: "已读"
related_concepts: ["VLA架构", "Sim2Real", "视频生成", "空中操作"]
---

## 🎯 题目

**DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation**

## 📝 三句摘要

1. **问题背景**：现有 VLA 模型在静态操纵任务上泛化能力强，但在动态场景（移动物体）下表现糟糕，原因在于感知-执行脱节（perception-execution gap）和推理延迟过高。

2. **核心方法**：DynamicVLA 通过三大设计解决动态操纵难题：① 0.4B 紧凑 VLA，采用卷积视觉编码器（替代 ViT）实现低延迟空间编码；② Continuous Inference，推理与执行重叠以降低延迟；③ Latent-aware Action Streaming (LAAS)，通过潜空间动作流对齐感知与执行窗口，弥合物理世界时空错位。

3. **关键结果**：在 DOM 基准（200K 合成 + 2K 真机场景）上，88Hz 推理速度，在未知运动模式泛化和实时闭环控制方面表现优异，跨实体泛化能力强。

## 💎 价值评估

- **🔬 研究价值**：首次系统解决 VLA 在动态场景的感知-执行脱节问题，LAAS 机制和 Continuous Inference 设计具有方法论创新价值。
- **🚀 实践价值**：0.4B 极简架构适合边缘部署，88Hz 推理满足实时要求，DOM 基准填补了动态操纵数据空白。
- **📈 扩展潜力**：可迁移至无人机/机械臂动态操作；LAAS 机制可与 RT-2/π0 等 VLA 结合；DOM 数据收集 pipeline 可扩展至其他动态任务。

## 🎯 可落地实验点

**实验设计**：在无人机动态目标跟踪任务中引入 LAAS 机制，解决机载视觉-动作延迟问题。

- **对比基线**：原生 VLA（无 LAAS）、纯开环轨迹规划
- **度量指标**：目标跟踪成功率、姿态误差、系统延迟（ms）
- **预期结果**：LAAS 闭环控制在动态轨迹跟踪场景下可显著降低跟踪误差（预计 Δ RMSE > 15%），同时保持 50Hz+ 控制频率

## 🔗 知识图谱
- [[VLA]] - 本文核心框架，视觉-语言-动作统一模型
- [[具身智能]] - 本文解决的问题域，动态物体操作
- [[Sim2Real]] - DOM 基准含 2K 真机场景，涉及仿真到真实迁移
- [[视频生成]] - 本文的视觉编码器设计（CNN 替代 ViT）
- [[空中操作]]
## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- π0 - π0: VLA 基线，DynamicVLA 继承其动作专家设计思路
- [[2023-01_RT-2]] - RT-2: VLA 领域奠基工作，DynamicVLA 对其动态场景局限性有深入分析

## 📌 待探索问题

- LAAS 的潜空间对齐机制是否依赖特定视觉编码器？对 CNN vs ViT 的选择是否敏感？
- 0.4B 模型在更复杂操作任务（如多指灵巧手）上的表现尚不清楚；模型容量与任务复杂度如何平衡？
- DOM 基准的 200K 合成数据如何生成？合成数据与真实数据的分布差异是否会影响 sim-to-real 泛化？

---
**维护**: 花火 · 2026-04-12
