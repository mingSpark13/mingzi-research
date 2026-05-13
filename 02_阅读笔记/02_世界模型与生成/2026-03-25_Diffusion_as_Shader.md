---
title: "Diffusion as Shader: 3D-aware Video Diffusion for Versatile Video Generation Control"
authors: （待补充）
arxiv: 2501.03847
date: 2025-01-07
institution: S-Lab, NTU 等
conf: arXiv
keywords: Diffusion as Shader, 3D-aware Video Diffusion, Video Control, Geometry-aware Generation
tags: ["D01"]
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2025_Diffusion_as_Shader.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["视频生成", "3D重建"]
---

## 🎯 题目
Diffusion as Shader: 3D-aware Video Diffusion for Versatile Video Generation Control

## 📝 三句摘要
1. DaS 的核心思想是把视频扩散控制做得更 3D-aware，而不是只在 2D 像素空间里做条件注入。
2. 它尝试利用更强的空间结构信号来改善视频控制的几何稳定性与可编辑性。
3. 对 InSpatio-World 这条路线来说，DaS 代表“视频控制必须吸收 3D 结构”这一范式转向。

## 💎 价值评估
- **🔬 研究价值**：把几何感知控制机制明确引入视频扩散系统。
- **🚀 实践价值**：为可控视频、动态新视角和重渲染提供更稳定的空间支撑。
- **📈 扩展潜力**：与 DA3 / 点云锚定 / 相机轨迹控制自然兼容。

## 🎯 可落地实验点
**实验设计**：比较 2D 条件视频控制与 DaS 式 3D-aware 控制在长时多视角任务中的漂移表现。

## 🔗 知识图谱
- [[视频生成]] - 以扩散视频模型为基础
- [[3D重建]] - 通过更强几何感知改善控制效果
- [[视频生成]] - 几何控制直接服务于一致性提升

## 🔗 相关链接
- [[2026-03-25_GCD_Generative_Camera_Dolly]] - 较早的视频相机控制方法
- [[2026-03-25_Trajectory_Attention]] - 轨迹控制与 3D-aware 控制相辅相成
- [[2026-03-25_ReCamMaster]] - 系统级 video rerendering 路线的关键代表

## 📌 待探索问题
- DaS 是否能作为几何锚定与视频生成之间的统一接口？
- 与显式点云渲染相比，3D-aware diffusion 的稳定性优势和劣势分别是什么？
的统一接口？
- 与显式点云渲染相比，3D-aware diffusion 的稳定性优势和劣势分别是什么？

---
**维护**: 花火 · 2026-04-12
