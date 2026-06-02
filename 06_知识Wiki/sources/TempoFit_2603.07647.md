---
type: "source"
id: "source.TempoFit_2603.07647"
pageType: "source"
tags: ["VLA架构", "长程任务规划", "具身智能"]
summary: "TempoFit 通过对冻结 VLA 复用分层 temporal KV memory，无需训练即可为长时程操作注入状态级历史，在 LIBERO-LONG 上带来稳定增益。"
origins: ["../../02_阅读笔记/D04_跨载体泛化/2026-04-05_TempoFit.md", "02_阅读笔记/D04_跨载体泛化/2026-04-05_TempoFit.md"]
updated: "2026-06-02"
---

# TempoFit_2603.07647

**核心要点**:
- **训练无关**: 不改变 VLA 权重，只用 KV 缓存实现历史注入
- **Layer-wise FIFO 记忆**: 在选定的中间层存储 prefix K/V，跨步复用
- **Frame-Gap Temporal Bias (FGTB)**: 固定 recency bias，保持决策当前主导

**原始资料**:
- [[../../02_阅读笔记/D04_跨载体泛化/2026-04-05_TempoFit.md]]
- [[02_阅读笔记/D04_跨载体泛化/2026-04-05_TempoFit.md]]
