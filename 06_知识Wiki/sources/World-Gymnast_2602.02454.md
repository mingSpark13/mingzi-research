---
type: "source"
id: "source.World-Gymnast_2602.02454"
pageType: "source"
tags: ["world model", "reinforcement learning", "VLM reward", "robot policy training", "隐空间世界模型", "强化学习"]
summary: "World-Gymnast 把动作条件世界模型直接当作 RL 训练环境，用 imagined rollout + VLM reward 优化机器人策略。"
origins: ["../../02_阅读笔记/99_归档/重复笔记/2026-04-09_World-Gymnast__dup2.md", "../../02_阅读笔记/99_归档/重复笔记/2026-04-09_World-Gymnast__dup2.md"]
updated: "2026-06-02"
---

# World-Gymnast_2602.02454

**核心价值**: World-Gymnast 把动作条件世界模型直接当作 RL 训练环境，用 imagined rollout + VLM reward 优化机器人策略。

**与我们的关系**:
- 这篇把 D01 从“世界模型做预测 / 做规划”进一步推进到“世界模型做训练器”。它直接回答了一个很关键的问题, 即 learned world model 能不能替代部分真实交互和传统 simulator 来优化策略。

**原始资料**:
- [[../../02_阅读笔记/99_归档/重复笔记/2026-04-09_World-Gymnast__dup2.md]]
- [[02_阅读笔记/99_归档/重复笔记/2026-04-09_World-Gymnast__dup2.md]]
