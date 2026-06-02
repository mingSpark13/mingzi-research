---
type: "source"
id: "source.MOTIF_2602.13764"
pageType: "source"
tags: ["cross-embodiment transfer", "action motifs", "flow matching", "few-shot transfer", "跨载体泛化", "流匹配"]
summary: "MOTIF 将跨载体共享的动作时空模式抽象为 motifs，再条件化 flow-matching 策略，实现少样本跨载体迁移。"
origins: ["../../02_阅读笔记/D02_VLA/MOTIF_2602.13764.md", "02_阅读笔记/D02_VLA/MOTIF_2602.13764.md"]
updated: "2026-06-02"
---

# MOTIF: Learning Action Motifs for Few-shot Cross-Embodiment Transfer (2602.13764)

**核心要点**:
- **动作基元（Action Motifs）解耦**: 跨载体的技能共享"接近→对准→接触→施力→脱离"等时空模式，但关节执行各异；MOTIF 把这些模式显式建模为序列化的抽象基元
- **三层架构**: - Stage I：从多载体数据中学 embodiment-agnostic motifs
- **few-shot 迁移**: 新载体只需少量 demo 即可适配

**与我们的关系**:
- 1. **motif 作为中间抽象**：比纯语言动作（LAP）粒度更细，比纯几何轨迹（CEI）泛化更强
- 2. **flow-matching + 条件化生成**：避免直接回归，生成多样性更好
- 3. **少样本适配协议**：新载体仅需 5-10 条 demo 即可迁移

**原始资料**:
- [[../../02_阅读笔记/D02_VLA/MOTIF_2602.13764.md]]
- [[02_阅读笔记/D02_VLA/MOTIF_2602.13764.md]]
