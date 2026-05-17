---
type: "source"
tags: []
summary: "**原始资料**:"
origins: ["02_阅读笔记/01_机器人与具身/2026-04-09_Embedding_Morphology_into_Transformers"]
updated: "2026-04-17"
---

# ViSA-Enhanced AVLN (2603.08007)

**核心要点**:
- **Morphology token / attribute conditioning**: 将关节属性、运动学结构等形态信息作为条件输入策略模型。
- **Topology-aware attention bias**: 把机器人拓扑关系编码进注意力偏置，减轻模型从原始观测里硬猜本体结构的负担。
- **Single-policy cross-robot learning**: 目标是在多个 embodiment 上训练一套统一策略，而不是每个机器人各训一套。

**与我们的关系**:
- 1. **形态先验前置**：本体差异应尽早进入 backbone，而不是只留给 retargeting。
- 2. **结构偏置可解释**：相比纯黑盒隐式适配，topology-aware attention 更方便做误差归因。
- 3. **适合作为 D04 主线对照**：后续可与 CEI/SoftAct 的功能接口路线、DexFormer 的隐式本体推断路线做三线对照。

**原始资料**:
- [[02_阅读笔记/01_机器人与具身/2026-04-09_Embedding_Morphology_into_Transformers]]
