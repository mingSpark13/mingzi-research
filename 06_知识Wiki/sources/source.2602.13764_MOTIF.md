---
type: "source"
tags: []
summary: ""
origins: ["../../02_阅读笔记/D02_VLA/MOTIF_2602.13764", "02_阅读笔记/D02_VLA/MOTIF_2602.13764"]
updated: "2026-04-17"
---

# MOTIF: Learning Action Motifs for Few-shot Cross-Embodiment Transfer

**核心要点**:
- **动作基元（Action Motifs）解耦**: 跨载体的技能共享"接近→对准→接触→施力→脱离"等时空模式，但关节执行各异；MOTIF 把这些模式显式建模为序列化的抽象基元
- **三层架构**: - Stage I：从多载体数据中学 embodiment-agnostic motifs
- **few-shot 迁移**: 新载体只需少量 demo 即可适配

**与我们的关系**:
- 1. **motif 作为中间抽象**：比纯语言动作（LAP）粒度更细，比纯几何轨迹（CEI）泛化更强
- 2. **flow-matching + 条件化生成**：避免直接回归，生成多样性更好
- 3. **少样本适配协议**：新载体仅需 5-10 条 demo 即可迁移

**原始资料**:
- [[../../02_阅读笔记/D02_VLA/MOTIF_2602.13764]]
- [[02_阅读笔记/D02_VLA/MOTIF_2602.13764]]
