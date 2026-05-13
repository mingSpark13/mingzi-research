---
title: "WorldLens: Comprehensive Benchmarking of World Models in Autonomous Driving"
authors: "Jianhua Han, Yukai Ma, Yijun He et al."
arxiv: "2512.10958"
date: 2025-12-13
institution: "Tsinghua University / Multiple Institutions"
conf: "CVPR 2026"
keywords: ["World Model", "Autonomous Driving", "Benchmark", "Evaluation"]
tags:
  - 隐空间世界模型
  - 物理一致性
  - 视频生成
  - 感知与3D视觉
domain: 世界模型
pdf_path: "../../01_论文库/世界模型/2512.10958_WorldLens.pdf"
reading_date: 2026-04-18
reading_status: 已读
summary: "WorldLens构建自动驾驶世界模型五维评测体系与26K人类标注数据集，揭示纹理强但物理弱的核心矛盾。"
related_concepts: ["隐空间世界模型", "物理一致性", "视频生成", "感知与3D视觉"]
---

# 🎯 题目

WorldLens: Comprehensive Benchmarking of World Models in Autonomous Driving

# 📝 三句摘要

1. **问题背景**：现有世界模型评估体系零散，缺乏统一框架来全面衡量自动驾驶场景下"建（生成）—理（重建）—动（动作跟随）"的全链路能力。
2. **核心方法**：WorldLens 提出五维评估体系（生成质量、重建精度、动作跟随、下游任务、人类偏好），并构建 26K 人类标注视频数据集 WorldLens-26K，从中发现当前模型的"纹理强但物理弱"矛盾。
3. **关键结果**：WorldLens 揭示强纹理模型往往违反物理，几何稳定模型缺乏行为保真度；蒸馏出可扩展的 WorldLens-Agent 评估模型，可替代部分人工评估。

# 💎 价值评估

- **🔬 研究价值**：首个覆盖世界模型全链路（建/理/动）的评估基准，填补了自动驾驶世界模型系统性评测的空白，对后续研究有重要指引价值。
- **🚀 实践价值**：WorldLens-26K 人类标注数据集 + WorldLens-Agent 可为数据管线验收提供量化依据，直接服务于工程实践。
- **📈 扩展潜力**：五维框架可扩展到无人机、机器人等具身智能场景；"纹理-物理矛盾"发现为后续世界模型设计指明方向。

# 🎯 可落地实验点

**实验设计**：为无人机/自动驾驶数据采集管线设计 WorldLens 风格的多维验收标准
- 对比基线：无（可自建五维打分体系）
- 度量指标：几何一致性评分、物理合理性评分、语义正确性评分、动作跟随准确率
- 预期结果：建立一套可复用的仿真数据质量评估流水线，早期发现采集数据的物理不一致问题

# 🔗 知识图谱

- [[concepts/隐空间世界模型]] - WorldLens 评估的核心对象，即在隐空间建模环境动态的世界模型
- [[concepts/物理一致性]] - 本文揭示的核心矛盾：强纹理模型往往违反物理定律
- [[concepts/视频生成]] - WorldLens 五维中的"生成"维度，覆盖视频生成质量评估
- [[concepts/感知与3D视觉]] - "重建"维度的技术基础，涉及深度/几何/场景重建

# 🔗 相关链接

- [[2026-04-18_OmniNWM]] - OmniNWM 同属自动驾驶世界模型工作，WorldLens 将其纳入评测对比
- [[2026-04-18_HybridWorldSim]] - HybridWorldSim 同样关注真实物理一致性，可作横向对比

# 📌 待探索问题

- WorldLens 的五维评估中"人类偏好"维度如何客观化？人类标注成本高、可扩展性差，WorldLens-Agent 能否完全替代人工？
- "纹理强但物理弱"矛盾的根本原因是什么？是损失函数设计问题还是数据分布偏差？有无方法能同时提升两者？

---
**维护**: 花火 · 2026-04-18
