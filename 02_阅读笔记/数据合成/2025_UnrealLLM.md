---
title: "UnrealLLM: Towards Highly Controllable and Interactable 3D Scene Generation by LLM-powered Procedural Content Generation"
authors: Song Tang, Kaiyong Zhao, Lei Wang, Yuliang Li, Xuebo Liu, Junyi Zou, Qiang Wang, Xiaowen Chu
arxiv: ""
date: 2025-07
institution: HKUST(GZ), XGRIDS, HIT(Shenzhen)
conf: ACL Findings 2025
keywords: [LLM, PCG, Unreal Engine 5, 3D scene generation, multi-agent]
tags: ["程序化内容生成", "具身智能", "多模态统一架构", "仿真平台"]
domain: 数据合成
pdf_path: "../../01_论文库/数据合成/2025_UnrealLLM.pdf"
reading_date: 2026-05-28
reading_status: 已读
related_concepts: ["程序化内容生成", "具身智能", "仿真平台", "多模态统一架构"]
---

# 📖 花火格式笔记

## 🎯 题目

UnrealLLM: Towards Highly Controllable and Interactable 3D Scene Generation by LLM-powered Procedural Content Generation

## 📝 三句摘要

1. **问题背景**：3D场景自动化生成对游戏和仿真应用至关重要，但现有方法难以在保留PCG优势的同时实现自然语言控制，核心挑战在于如何让LLM与专业PCG系统有效对接。
2. **核心方法**：提出UnrealLLM多智能体框架，通过构建丰富的多模态3D资产库（858K+资产）实现上下文感知检索，以及PCG知识库（节点操作/参数配置/生成策略）将文本转译为可执行PCG blueprint；使用spline-based control进行几何布置。
3. **关键结果**：在技术指标和美学质量上达到竞争性性能，在生成规模和交互性方面具有独特优势，证明LLM可有效操控UE5原生PCG能力而非直接硬编码坐标。

## 💎 价值评估

- **🔬 研究价值**：为路线A（规则/PCG主导，LLM负责参数化）提供了完整的多智能体工程实现范本，直接验证了"LLM+PCG分工"架构的可行性。
- **🚀 实践价值**：主人的AirSpark/UE平台最适合此路线——UE5 PCG系统已具备道路spline、建筑block grammar、植被采样等能力，LLM只需生成SceneSpec JSON而非直接操控坐标，工程上最稳。
- **📈 扩展潜力**：可扩展到低空场景的PCG图设计（道路网/建筑群/植被/车辆/目标区域），以及多智能体协作（场景生成agent+代码agent+playtesting agent）。

## 🎯 可落地实验点

**实验设计**：参考UnrealLLM的多智能体架构，为低空场景生成设计三Agent系统——SceneSpec生成Agent（GPT-4V接收任务描述）、PCG执行Agent（将Spec转为UE blueprint）、Validator Agent（检查几何有效性和可通行性）。
- 对比基线：直接让LLM输出UE坐标、规则化场景（无LLM语义理解）
- 度量指标：Semantic Completeness、Prompt-Scene Alignment、Path Existence Rate、生成速度
- 预期结果：多Agent系统在语义一致性和场景多样性上显著优于直接坐标输出

## 🔗 知识图谱

- [[程序化内容生成]] - 本文核心技术
- [[仿真平台]] - UE5平台的使用
- [[具身智能]] - 场景生成的最终目标应用
- [[多模态统一架构]] - LLM作为调度器

## 🔗 相关链接

- [[2603.07106_AutoUE]] - 多Agent系统进一步扩展
- [[2602.10116_SAGE]] - Agentic场景生成的另一种范式
- [[2312.09067_Holodeck]] - 早期语言驱动3D环境生成

## 📌 待探索问题

- UnrealLLM的资产库（858K+）如何迁移到低空场景？需要建立怎样的低空资产规范（建筑高度分类、植被密度、车辆类型、天气变体）？
- 多Agent架构中，Validator Agent的失败反馈如何高效引导SceneSpec Agent重新生成？是否需要引入视觉critic？

---
**维护**: 花火 · 2026-05-28
