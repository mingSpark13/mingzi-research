# RL-Based Sim-Real Co-Training for VLA (2602.12628)

> **arXiv**: 2602.12628 | **方向**: D07_Isaac强化学习机械臂控制 | **深挖时间**: 2026-04-13 R684 | **状态**: 🆕 候选扫描

## 一句话与本方向关系
提出 RL+Sim2Real 联合训练 VLA 的框架，在 Isaac Lab 中训练，迁移到真机——与 D07 主线"Isaac Lab RL → sim-to-real"高度对齐，是机械臂 VLA 训练的新范式。

## 核心贡献
1. **Sim-Real Co-Training**：在 Isaac Lab 仿真中用 RL 预训练 VLA 策略，同时保留真机 fine-tuning 通道
2. **域随机化 + 自适应**：自动调整仿真参数以缩小 sim-to-real gap
3. **VLA + RL 联合**：用 VLA 学高层意图理解 + RL 学低层精细控制

## 与主人方向关联
- **龙虾机械臂控制**：可参考其"仿真 RL 训练 + 真机验证"协议
- **Isaac Lab 环境部署**：该论文直接用 Isaac Lab 作为训练平台，与 D07 基础设施选择一致
- **VLA+RL 双层**：龙虾项目的感知-决策链路可参考 VLA(高层)+RL(低层)分液控制架构
