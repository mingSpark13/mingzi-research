---
type: "source"
tags: []
summary: "- **训练无关**: 不改变 VLA 权重，只用 KV 缓存实现历史注入"
origins: ["../../02_阅读笔记/D04_跨载体泛化/2026-04-05_TempoFit", "02_阅读笔记/D04_跨载体泛化/2026-04-05_TempoFit"]
updated: "2026-04-17"
---

# TempoFit_2603.07647

**核心要点**:
- **训练无关**: 不改变 VLA 权重，只用 KV 缓存实现历史注入
- **Layer-wise FIFO 记忆**: 在选定的中间层存储 prefix K/V，跨步复用
- **Frame-Gap Temporal Bias (FGTB)**: 固定 recency bias，保持决策当前主导

**原始资料**:
- [[../../02_阅读笔记/D04_跨载体泛化/2026-04-05_TempoFit]]
- [[02_阅读笔记/D04_跨载体泛化/2026-04-05_TempoFit]]
