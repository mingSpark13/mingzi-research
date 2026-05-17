---
title: "AirCopBench: A Benchmark for Multi-drone Collaborative Embodied Perception and Reasoning"
authors: Jirong Zha, Yuxuan Fan, Tianyu Zhang, Geng Chen, Y. Chen, C. Gao, X. Chen
arxiv: 2511.11025
date: 2025-11
institution: Tsinghua University / Shanghai Jiao Tong University
conf: AAAI 2026
keywords: [multi-drone, collaborative perception, embodied perception, benchmark, MLLM]
tags: [多机器人协调, 跨载体泛化, 多模态统一架构]
summary: "AirCopBench 构建多无人机协同具身感知退化基准，系统揭示现有 MLLM 在遮挡、模糊与协同决策上的明显短板。"
domain: UAV跟踪
pdf_path: "../../01_论文库/UAV跟踪/2511.11025_AirCopBench.pdf"
reading_date: 2026-05-16
reading_status: 已读
related_concepts: ["多机器人协调", "跨载体泛化", "多模态统一架构"]
---

# 📖 花火格式笔记

## 🎯 题目

AirCopBench: A Benchmark for Multi-drone Collaborative Embodied Perception and Reasoning

## 📝 三句摘要

1. **问题背景**：现有VQA基准主要针对单智能体高质量图像，缺少对多无人机协同具身感知场景的退化感知评估，无法全面评估MLLMs在真实世界退化条件下的协同感知与推理能力。
2. **核心方法**：提出AirCopBench，首个系统性评估MLLMs在具身空中协同感知下退化鲁棒性的综合基准，包含14.6k+问答对，涵盖场景理解、物体理解、感知评估、协同决策四大任务维度，14种任务类型，覆盖遮挡、阴影、运动模糊、噪声、数据丢失、远距离检测等真实退化条件。
3. **关键结果**：对40个MLLMs评估显示，协同感知任务存在显著性能差距，最佳模型仍落后人类平均24.38%，且不同任务间表现不一致；微调实验验证了空中协同感知从仿真到真实的可行性。

## 💎 价值评估

- **🔬 研究价值**：首个针对多无人机协同具身感知与退化条件下的MLLM评测基准，填补了该领域空白，为未来研究提供了标准化评测框架和数据集。
- **🚀 实践价值**：支持RGB图像、文本、点云多模态，覆盖无人机、行人、车辆、自行车等多类目标，可直接用于评估实际部署的MLLMs在无人机集群系统中的协同感知能力。
- **📈 扩展潜力**：可扩展至地面多机器人协同、其他退化场景（如雨雪雾天气）、以及与LLM-based规划控制系统的联合评测。

## 🎯 可落地实验点

**实验设计**：基于AirCopBench评估国产MLLMs（如Qwen-VL、CogVLM）在多无人机协同感知任务上的退化鲁棒性

- **对比基线**：GPT-4V、Gemini Pro、Claude 3等商用闭源模型；LLaVA、Qwen-VL-Chat、InternVL等开源模型
- **度量指标**：准确率（scene understanding、object understanding）、协同决策正确率、感知评估一致性
- **预期结果**：发现国产模型在运动模糊和遮挡条件下的具体短板，为后续针对退化感知的模型优化提供方向

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。
> 字典真源：`06_知识Wiki/_views/概念关键词字典.md`
> 不确定时查字典别名表；字典外新概念写入 `06_知识Wiki/inbox.md`，不自行创建。

- [[多机器人协调]] - 本文核心任务场景，多无人机协同感知与决策
- [[跨载体泛化]] - AirCopBench作为评测基准，评估模型在不同退化条件下的泛化能力
- [[多模态统一架构]] - 本文评估对象MLLMs的核心架构类型

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作），通常 2-5 篇。

- [[2025-05_SwarmBench]] - SwarmBench: Benchmarking LLMs' Swarm Intelligence，本文同领域benchmark，但侧重去中心化协同而非具身感知
- [[2024-10_pi0]] - π0: VLA领域基线模型，本文对比的SOTA端到端VLA方法

## 📌 待探索问题

- **退化感知推理**：AirCopBench仅评估MLLMs的感知与推理能力，未来可探索如何让模型在退化条件下主动调度协同资源（如请求其他无人机视角），需要何种协同推理机制？
- **Sim-to-Real迁移**：微调实验证明可行，但不同MLLM架构的迁移效率差异显著（如LLaVA vs GPT-4V），其根本原因是什么？是表征学习差异还是推理链路的结构差异？

---

**维护**: 花火 · 2026-05-16
