---
title: "Generative Camera Dolly: Extreme Monocular Dynamic Novel View Synthesis"
authors: Basile Van Hoorick, Rundi Wu, Ege Ozguroglu, Kyle Sargent, Ruoshi Liu, Pavel Tokmakov, Achal Dave, Changxi Zheng, Carl Vondrick
arxiv: ""
date: 2024-09-01
institution: Columbia University, Stanford University, Toyota Research Institute
conf: ECCV 2024 Oral
keywords: GCD, Camera Control, Novel View Synthesis, Dynamic Video
tags: ["视频生成", "3D重建"]
summary: "GCD 将 diffusion prior 引入单目动态新视角合成，用生成式 camera control 推进极端轨迹下的动态 novel-view synthesis。"
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2024_GCD_Generative_Camera_Dolly.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["视频生成", "3D重建"]
---

## 🎯 题目
Generative Camera Dolly: Extreme Monocular Dynamic Novel View Synthesis

## 📝 三句摘要
1. GCD 关注从单目动态视频出发，实现极端条件下的相机移动与新视角视频合成。
2. 它把 diffusion prior 引入动态新视角合成，代表从传统几何渲染向生成式 camera control 的过渡。
3. 在 InSpatio-World 技术谱系里，GCD 是 camera-controlled video-to-video / novel-view synthesis 重要前序之一。

## 💎 价值评估
- **🔬 研究价值**：把单目动态新视角推进到生成模型范式下的新阶段。
- **🚀 实践价值**：为“参考视频换机位重拍”提供强先验能力。
- **📈 扩展潜力**：为 ReCamMaster 和 InSpatio-World 这类系统提供任务定义与方法启发。

## 🎯 可落地实验点
**实验设计**：将 GCD 与 ReCamMaster / InSpatio-World 在相同视频和轨迹条件下比较，评价相机轨迹可控性与动态一致性。

## 🔗 知识图谱
- [[视频生成]] - 相机大幅变化时保持场景稳定是核心挑战
- [[3D重建]] - 动态时空场景的新视角建模问题
- [[视频生成]] - 通过生成先验完成动态视角扩展

## 🔗 相关链接
- [[2026-03-25_ReCamMaster]] - 更系统化的视频重渲染框架
- [[2026-03-25_Trajectory_Attention]] - 细粒度轨迹控制的重要后续工作
- [[2026-03-25_Diffusion_as_Shader]] - 更 3D-aware 的视频控制路线

## 📌 待探索问题
- GCD 对极端轨迹变化的稳定性来自几何还是来自生成先验？
- 如果显式加入深度/点云锚点，是否能进一步提升结果？

---
**维护**: 花火 · 2026-04-12
