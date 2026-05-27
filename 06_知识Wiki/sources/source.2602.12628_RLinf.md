---
type: "source"
tags: []
summary: ""
origins: ["../../02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628", "02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628"]
updated: "2026-04-17"
---

# RLinF / RL-Co (2602.12628)

**核心要点**:
<<<<<<< HEAD
- **Sim-Real Co-Training**: 在 Isaac Lab 仿真中用 RL 预训练 VLA 策略，同时保留真机 fine-tuning 通道。
- **域随机化 + 自适应**: 自动调整仿真参数以缩小 sim-to-real gap。
- **VLA + RL 联合**: 用 VLA 学高层意图理解，用 RL 学低层精细控制。

**与我们的关系**:
- 用 RL 补足 VLA 在低层连续控制上的细粒度修正能力。
- 用统一仿真平台积累安全可控的预训练数据，再把真机数据留给最后一跳对齐。
- 把 sim-to-real 当成训练协议而不是单次迁移技巧，适合后续扩成评测基线。
=======
- **Sim-Real Co-Training**: 在 Isaac Lab 仿真中用 RL 预训练 VLA 策略，同时保留真机 fine-tuning 通道
- **域随机化 + 自适应**: 自动调整仿真参数以缩小 sim-to-real gap
- **VLA + RL 联合**: 用 VLA 学高层意图理解 + RL 学低层精细控制
>>>>>>> 1080f76346ff43cff0d7fb71910b283cdc15be6a

**原始资料**:
- [[../../02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628]]
- [[02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628]]
