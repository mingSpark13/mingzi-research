---
title: "VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation"
authors: Arjun Majumdar, Gunjan Chug, Amit Singh, et al.
arxiv: ""
date: 2024
institution: MIT / BMW
conf: ICRA 2024
keywords: zero-shot semantic navigation, open-vocabulary, frontier exploration, vision-language model, object-goal navigation
tags: ["D06"]
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["Sim2Real"]
---

## 🎯 题目

VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation

## 📝 三句摘要

1. **问题背景**：开放词汇目标导航（Open-vocabulary ObjectNav）要求机器人在未知环境中根据自然语言指令找到任意类别目标，现有方法依赖大规模域内数据微调，泛化能力受限。
2. **核心方法**：提出 Vision-Language Frontier Maps（VLFM），将开放词汇视觉目标检测与 frontier exploration 结合，在无需任何域内微调的情况下实现零样本语义导航。
3. **关键结果**：在 HM3D、MP3D 等基准上相比先前零样本方法成功率提升显著，GitHub 社区活跃、开源代码成熟，适合作为工程基线。

## 💎 价值评估

- **🔬 研究价值**：证明了无需微调即可实现开放词汇语义导航的可行性，为零样本导航提供了简洁有效的骨架。
- **🚀 实践价值**：工程实现完整、代码成熟，易于接入自有控制 API，是最快搭建"语言指定目标搜索"系统的首选基线。
- **📈 扩展潜力**：可叠加 scene graph、LLM 推理、多层地图等模块；也适合作为高层语义决策头搭配底层 MPC/ locomotion policy 使用。

## 🎯 可落地实验点

**实验设计**：在室内走廊/校园楼层场景验证"找垃圾桶/找风扇"等语言目标搜索能力
- 对比基线：REASSEMBLE、CLIP on Map、Zero-shot PN
- 度量指标：Success Rate (SR)、SPL、Step Efficiency
- 预期结果：SR > 65%，相比纯几何探索方法有明显语义目标定位优势

## 🔗 知识图谱
- [[零样本语义导航]]
- [[Frontier Exploration]]
- [[开放词汇目标检测]]
- [[视觉语言模型]]
- [[Sim2Real]]

## 🔗 相关链接

- [[2024-03-01_REASSEMBLE]] - 语义导航基线方法，VLFM 在 HM3D 上显著超越
- [[2023-06_RTM-2]] - 视觉语言导航领域重要基础工作

## 📌 待探索问题

- 如何将 VLFM 的 frontier 选择策略与四足机器人的实时地形规避结合？
- 在目标物体被遮挡或未出现在训练分布中时，VLFM 的鲁棒性如何保障？

---
**维护**: 花火 · 2026-04-12
