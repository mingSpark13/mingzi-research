---
type: "source"
id: "source.DexFormer_2602.08278"
pageType: "source"
tags: ["cross-embodiment", "dexterous manipulation", "history-conditioned transformer", "zero-shot transfer", "跨载体泛化", "灵巧操作"]
summary: "利用历史条件 Transformer 隐式推断不同手型与动力学差异，实现零样本跨灵巧手泛化。"
origins: ["../../02_阅读笔记/D02_VLA/2026-04-09_DexFormer.md", "02_阅读笔记/D02_VLA/2026-04-09_DexFormer.md"]
updated: "2026-06-02"
---

# DexFormer_2602.08278

**核心要点**:
- **History-conditioned transformer**: 利用历史观测而非单帧输入，在线推断 embodiment 差异
- **Dynamics-aware cross-embodiment policy**: 同时适配不同灵巧手的运动学与动力学，不依赖每个本体单独 decoder head
- **Procedural dexterous-hand assets**: 在多种程序化手型资产上训练，获得可迁移的 manipulation prior

**与我们的关系**:
- 1. **隐式本体识别**：不一定要显式输入 morphology token，可把“识别当前本体”交给时序模型自己完成
- 2. **history as embodiment signal**：跨载体差异不只在结构参数，也体现在同一动作下的动态响应轨迹中
- 3. **适合作为对照基线**：后续主人做异构末端执行器/空中机械臂共享策略时，可把它作为“implicit inference”路线，对照 CEI/SoftAct/Embedding Morphology 这类显式结构先验路线

**原始资料**:
- [[../../02_阅读笔记/D02_VLA/2026-04-09_DexFormer.md]]
- [[02_阅读笔记/D02_VLA/2026-04-09_DexFormer.md]]
