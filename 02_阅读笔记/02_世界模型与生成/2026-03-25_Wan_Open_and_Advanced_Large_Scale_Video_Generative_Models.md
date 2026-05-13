---
title: "Wan: Open and Advanced Large-Scale Video Generative Models"
authors: Wan Team
arxiv: 2503.20314
date: 2025-03-26
institution: Alibaba / Wan Team
conf: arXiv
keywords: Wan, Video Foundation Model, T2V, I2V, Video Diffusion
tags: ["D01"]
domain: 世界模型
pdf_path: ../../01_论文库/世界模型/2025_Wan_Open_and_Advanced_Large_Scale_Video_Generative_Models.pdf
reading_date: 2026-03-25
reading_status: 已入库
related_concepts: ["视频生成", "多模态统一架构", "实时推理"]
---

## 🎯 题目
Wan: Open and Advanced Large-Scale Video Generative Models

## 📝 三句摘要
1. Wan 系列提供开放的大规模视频生成基础模型，覆盖 T2V、I2V、编辑等多任务形态。
2. 它把视频生成底座做成可复用基础设施，为后续系统类工作提供统一 backbone。
3. InSpatio-World 在 Step 3 中直接使用 Wan2.1 的 1.3B / 14B 模型，说明它是当前系统的生成骨干层。

## 💎 价值评估
- **🔬 研究价值**：开放视频基础模型的代表，降低视频生成研究进入门槛。
- **🚀 实践价值**：多尺寸模型适合系统集成，1.3B 版本尤其利于实验和快速迭代。
- **📈 扩展潜力**：可与几何恢复、相机控制、自回归训练法组合形成新型世界模型系统。

## 🎯 可落地实验点
**实验设计**：比较 Wan2.1 直接生成、相机条件控制、几何锚定后再生成三种路径的稳定性差异。

## 🔗 知识图谱
- [[视频生成]] - Wan 是典型视频生成基础模型
- [[多模态统一架构]] - 支持多任务、多条件的视频生成框架
- [[实时推理]] - 是 Self-Forcing 等实时化训练路线的重要底座

## 🔗 相关链接
- [[2026-03-25_Self_Forcing]] - 在 Wan 底模上推进实时自回归生成
- [[2026-03-19_InSpatio_WorldFM]] - InSpatio-WorldFM 也属于视频/空间智能系统路线
- [[2026-03-25_ReCamMaster]] - 在可控视频重渲染中可借用类似底模能力

## 📌 待探索问题
- Wan 的开放域能力与显式世界状态建模能力之间还有多大差距？
- 在机器人/世界模型场景下，视频基础模型是否需要额外状态记忆接口？

---
**维护**: 花火 · 2026-04-12
