---
type: "source"
tags: ["VLA架构", "强化学习", "Sim2Real", "仿真平台"]
summary: "在 Isaac Lab 中用 RL+VLA 联合训练并保留真机 fine-tuning 通道，是 D07 机械臂 sim-to-real 的直接参考。"
origins: ["../../02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628", "02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628"]
updated: "2026-04-17"
---

# RL-Based Sim-Real Co-Training for VLA (2602.12628)

**核心要点**:
- **Sim-Real Co-Training**: 在 Isaac Lab 仿真中用 RL 预训练 VLA 策略，同时保留真机 fine-tuning 通道
- **域随机化 + 自适应**: 自动调整仿真参数以缩小 sim-to-real gap
- **VLA + RL 联合**: 用 VLA 学高层意图理解 + RL 学低层精细控制

**原始资料**:
- [[../../02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628]]
- [[02_阅读笔记/D02_VLA/RL_SimReal_CoTraining_VLA_2602.12628]]
