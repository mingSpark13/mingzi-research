---
title: Dynamic View Synthesis from Dynamic Monocular Video
authors: Edgar Tretschk, Ayush Tewari, Vladislav Golyanik, Michael Zollhöfer, Christoph
  Lassner, Christian Theobalt
arxiv: 2105.06468
date: 2021-05-13
institution: MPII, Facebook Reality Labs
conf: ICCV 2021
keywords: Dynamic View Synthesis, Monocular Video, Dynamic Scene, Novel View
tags:
- D01
domain: 世界模型
summary: Dynamic View Synthesis from Dynamic Monocular Video
pdf_path: ../../01_论文库/世界模型/2021_Dynamic_View_Synthesis_from_Dynamic_Monocular_Video.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts:
- 3D重建
- 视频生成
---

## 🎯 题目
Dynamic View Synthesis from Dynamic Monocular Video

## 📝 三句摘要
1. 该工作研究如何仅从单目动态视频恢复可随时间变化的新视角结果。
2. 它将动态场景建模与视图合成结合，迈出从静态 NeRF 走向 4D 视频世界表示的重要一步。
3. 对 InSpatio-World 谱系来说，它代表“视频本质是 4D 世界投影”的早期技术表达。

## 💎 价值评估
- **🔬 研究价值**：早期明确把动态视频场景与可渲染 4D 表示连接起来。
- **🚀 实践价值**：证明单目视频也可以承担动态新视角合成任务。
- **📈 扩展潜力**：后续 DynIBaR、GCD、ReCamMaster 都在更强生成模型下继续推进这条线。

## 🎯 可落地实验点
**实验设计**：以单目无人机巡检视频为输入，尝试构建小范围动态新视角系统，验证几何一致性与时间稳定性。

## 🔗 知识图谱
- [[3D重建]] - 将时变视频看作 4D 场景恢复问题
- [[视频生成]] - 动态场景下保持视角一致性是核心挑战
- [[3D重建]] - 属于从视频恢复时空场景结构的路线

## 🔗 相关链接
- [[2026-03-25_NeRF]] - 静态视图合成的起点
- [[2026-03-25_DynIBaR]] - 动态图像渲染路线的重要推进
- [[2026-03-25_GCD_Generative_Camera_Dolly]] - 单目动态新视角在生成模型时代的延伸

## 📌 待探索问题
- 单目输入对真实世界动态一致性的上限在哪里？
- 显式几何与隐式生成应如何分工来提升稳定性？

---
**维护**: 花火 · 2026-04-12
