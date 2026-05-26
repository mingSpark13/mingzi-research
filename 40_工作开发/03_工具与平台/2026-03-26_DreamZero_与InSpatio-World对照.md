# DreamZero 与 InSpatio-World 对照

## 一句话
- **DreamZero** 想证明：世界动作模型本身就是零样本策略。
- **InSpatio-World** 想证明：参考视频可以被锚定成可交互的 4D 世界状态。

## 核心差异

| 维度 | DreamZero | InSpatio-World |
|---|---|---|
| 核心对象 | 动作 + 视频联合建模 | 参考视频 → 世界状态锚定 |
| 主要目标 | 零样本机器人策略 | 可交互新视角 / 世界观察生成 |
| 偏向 | policy / execution | observation / world state |
| 背后底座 | 视频模型 + 机器人动作建模 | Wan2.1 + Self-Forcing + DA3 + Florence-2 |
| 研究问题 | 世界动作模型能否直接成为 policy | 世界状态能否被几何锚定并实时交互生成 |

## 对主人的启发
最值得挖的点不是二选一，而是把两者拼起来：

> **能否先用 InSpatio-World 风格模型稳定维护 world state，再由 DreamZero 风格模型在该状态上输出 action / policy？**

这很可能就是“世界状态模型 + 世界动作模型”的耦合路线。
