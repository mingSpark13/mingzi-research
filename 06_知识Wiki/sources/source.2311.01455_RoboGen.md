---
type: "source"
id: "source.2311.01455_RoboGen"
pageType: "source"
tags: ["数据合成", "具身智能", "强化学习", "世界模型"]
summary: "生成式仿真流水线覆盖任务提议→场景生成→策略训练→技能学习全过程，propose-generate-learn循环是主动数据飞轮雏形"
origins: ["../02_阅读笔记/数据合成/2311.01455_RoboGen.md"]
updated: "2026-05-28 14:44"
---

# RoboGen (2311.01455)

**核心要点**:
- **propose-generate-learn循环**: 自动生成所有仿真学习阶段所需信息——任务提议→场景→资产→策略→训练监督，端到端生成式仿真
- **任务级多样性**: 不仅关注场景多样性，更关注任务级多样性，显著提升技能学习泛化能力
- **CoRL 2024**: UC Berkeley/Stanford/MIT联合工作，生成式仿真（generative simulation）概念的里程碑

**与我们的关系**:
- D05数据合成方向，GenSim的扩展深化，生成式仿真概念提出者
- 主人低空数据飞轮可直接借鉴：Propose（SceneSpec+TaskSpec）→ Generate（PCG+Critic）→ Learn（轨迹+策略）→ Reflect（失败样本→变体）

**原始资料**:
- [[02_阅读笔记/数据合成/2311.01455_RoboGen]]
