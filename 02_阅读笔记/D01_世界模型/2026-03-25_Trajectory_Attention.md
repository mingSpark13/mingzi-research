---
title: "Trajectory Attention for Fine-grained Video Motion Control"
authors: （待补充）
arxiv: 2411.19324
date: 2024-11-29
institution: StepFun 等
conf: arXiv
keywords: Trajectory Attention, Motion Control, Video Generation, Camera Control
tags: ["D01", "运动控制"]
summary: "以轨迹级时序建模强化长时动作理解与生成的序列建模方法。"
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2024_Trajectory_Attention.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["运动控制"]
---

## 🎯 题目
Trajectory Attention for Fine-grained Video Motion Control

## 📝 三句摘要
1. Trajectory Attention 试图把精细轨迹控制直接注入视频生成过程，让视频运动和相机控制更可控。
2. 它说明 controllable video generation 正从粗粒度条件走向轨迹级条件建模。
3. 在 InSpatio-World 谱系里，这代表“相机控制不再是附属能力，而是主任务”的重要阶段。

## 💎 价值评估
- **🔬 研究价值**：强调轨迹级注意力机制对视频控制质量的影响。
- **🚀 实践价值**：可为相机路径、物体运动和交互式视频控制提供更细粒度接口。
- **📈 扩展潜力**：可与显式几何和世界状态锚定结合，提升 controllable world model 的可用性。

## 🎯 可落地实验点
**实验设计**：将 trajectory attention 与传统 condition injection 对比，观察轨迹控制精度与时序漂移差异。

## 🔗 知识图谱
- [[视频生成]] - 属于视频生成控制路线的重要机制
- [[视频生成]] - 轨迹控制需要稳定视角变化
- [[实时推理]] - 轨迹条件的引入会直接影响在线控制代价

## 🔗 相关链接
- [[2026-03-25_GCD_Generative_Camera_Dolly]] - 更早的 camera-controlled video 合成路径
- [[2026-03-25_ReCamMaster]] - 参考视频重渲染的系统性实现
- [[2026-03-25_Diffusion_as_Shader]] - 与 3D-aware 控制形成互补

## 📌 待探索问题
- Trajectory Attention 是否足够替代显式几何控制？
- 轨迹控制和世界状态锚定之间怎样划分职责更合理？
 轨迹控制和世界状态锚定之间怎样划分职责更合理？

---
**维护**: 花火 · 2026-04-12
