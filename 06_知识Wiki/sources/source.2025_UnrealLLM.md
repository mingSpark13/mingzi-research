---
type: "source"
id: "source.2025_UnrealLLM"
pageType: "source"
tags: ["程序化内容生成", "仿真平台", "具身智能", "多模态统一架构"]
summary: "UnrealLLM 多智能体框架用 LLM 操控 UE5 PCG 系统生成高度可控可交互 3D 场景，858K+ 资产库 + PCG 知识库实现自然语言到可执行 blueprint 的转译。"
origins: ["../02_阅读笔记/数据合成/2025_UnrealLLM.md"]
updated: "2026-05-28 14:20"
---

# UnrealLLM (ACL Findings 2025)

**核心要点**:
- **多智能体 PCG 架构**: SceneSpec Agent + PCG 执行 Agent + Validator Agent 分工，LLM 负责语义理解和任务分解，不直接操控坐标
- **UE5 PCG 集成**: 利用 UE5 原生 spline-based PCG 能力（道路/建筑/植被等），LLM 生成 SceneSpec JSON 而非硬编码坐标
- **大规模资产库**: 858K+ 多模态 3D 资产支持上下文感知检索，支撑场景生成质量和多样性

**与我们的关系**:
- 路线A（PCG主导+LLM参数化）完整工程范本，主人的 AirSpark/UE 平台最适合此路线
- 低空场景 PCG 扩展：道路网/建筑群/植被/车辆的规格化资产库建设

**原始资料**:
- [[02_阅读笔记/数据合成/2025_UnrealLLM]]
