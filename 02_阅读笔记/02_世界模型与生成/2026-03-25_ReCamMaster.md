---
title: "ReCamMaster: Camera-Controlled Generative Rendering from A Single Video"
authors: Jianhong Bai, Menghan Xia, Xiao Fu, Xintao Wang, Lianrui Mu, Jinwen Cao, Zuozhu Liu, Haoji Hu, Xiang Bai, Pengfei Wan, Di Zhang
arxiv: 2503.11647
date: 2025-03-14
institution: Kling AI Research 等
conf: arXiv
keywords: ReCamMaster, Camera-Controlled Rendering, Video Re-rendering, Single Video
tags: ["D01"]
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2025_ReCamMaster.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["视频生成", "3D重建"]
---

## 🎯 题目
ReCamMaster: Camera-Controlled Generative Rendering from A Single Video

## 📝 三句摘要
1. ReCamMaster 研究给定单个参考视频和新相机轨迹，生成可控重拍结果的问题。
2. 它把 camera-controlled generative rerendering 做成更系统化、产品化的完整框架。
3. InSpatio-World README 明确致谢 ReCamMaster，可视作其直接启发来源之一。

## 💎 价值评估
- **🔬 研究价值**：把“参考视频重拍 / 相机控制”正式定义成一类视频生成任务。
- **🚀 实践价值**：最接近 InSpatio-World 当前开源实现的表面任务形式。
- **📈 扩展潜力**：向世界模型叙事再走一步，就会变成 state-anchored 4D world 路线。

## 🎯 可落地实验点
**实验设计**：复现 ReCamMaster 与 InSpatio-World 在相同轨迹文件条件下的 novel-view video 输出，对比控制精度与时序稳定性。

## 🔗 知识图谱
- [[视频生成]] - 换机位重拍要求视角变化下结果稳定
- [[视频生成]] - 属于 controllable video rerendering 路线
- [[3D重建]] - 实际上逼近动态 4D 世界的观察生成问题

## 🔗 相关链接
- [[2026-03-25_GCD_Generative_Camera_Dolly]] - 更早的单目动态新视角生成路线
- [[2026-03-25_Trajectory_Attention]] - 轨迹控制机制层面的推进
- [[2026-03-19_InSpatio_WorldFM]] - InSpatio-World 对该路线进行系统整合与世界模型化叙事

## 📌 待探索问题
- ReCamMaster 与 InSpatio-World 的本质差异是在任务定义、几何锚定，还是训练范式？
- 单视频重渲染能否真正构成可持续世界状态，而不只是条件视频生成？

---
**维护**: 花火 · 2026-04-12
