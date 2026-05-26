---
type: "source"
tags: []
summary: "- **Sim-Real Co-Training**: 在 Isaac Lab 仿真中用 RL 预训练 VLA 策略，同时保留真机 fine-tuning 通道"
origins: ["../../02_阅读笔记/D04_跨载体泛化/2026-04-19_2604.13645_SimReal_CoTraining", "../../02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628", "02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628"]
updated: "2026-04-17"
---

# SimReal_CoTraining_2604.13645

**核心要点**:
- **Sim-Real Co-Training**: 在 Isaac Lab 仿真中用 RL 预训练 VLA 策略，同时保留真机 fine-tuning 通道
- **域随机化 + 自适应**: 自动调整仿真参数以缩小 sim-to-real gap
- **VLA + RL 联合**: 用 VLA 学高层意图理解 + RL 学低层精细控制

**原始资料**:
- [[../../02_阅读笔记/D04_跨载体泛化/2026-04-19_2604.13645_SimReal_CoTraining]]
- [[../../02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628]]
- [[02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628]]
