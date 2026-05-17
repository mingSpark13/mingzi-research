---
type: "source"
tags: ["跨载体泛化", "流匹配", "动作分层", "动作分块", "少样本学习"]
summary: "MOTIF将跨载体动作时空模式抽象为motifs，条件化flow-matching策略实现少样本跨载体迁移，是功能对齐流派最新代表。"
origins: ["02_阅读笔记/01_机器人与具身/MOTIF_2602.13764", "05_科研研究/D04_跨载体泛化/papers/MOTIF_2602.13764"]
updated: "2026-05-09"
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
- [[02_阅读笔记/01_机器人与具身/MOTIF_2602.13764]]
- [[05_科研研究/D04_跨载体泛化/papers/MOTIF_2602.13764]]
