# DreamZero 开源仓库笔记

- Repo: https://github.com/dreamzero0/dreamzero
- Project: https://dreamzero0.github.io/
- 论文：[[2026-03-26_DreamZero_World_Action_Models_are_Zero-shot_Policies]]
- 机构：NVIDIA GEAR Lab

## 定位
DreamZero 将机器人策略表达成 **World Action Model (WAM)**，即模型联合预测视频与动作，并把这种世界动作建模直接解释为零样本策略能力。

## 仓库关键信息
- Python 3.11
- PyTorch 2.8+
- CUDA 12.9+
- 至少 2 张 GPU 做分布式推理
- 官方测试硬件：GB200 / H100
- 提供 DROID / AgiBot checkpoint、LoRA / full finetune 脚本、WebSocket inference server

## 为什么重要
1. 这是主人正在看的 **World Model × RL** 路线里非常关键的当代节点。
2. 它把“视频模型当世界模拟器”推进到“视频模型直接当 policy”的阶段。
3. 与 InSpatio-World 相比，DreamZero 更偏 **动作执行 / 策略零样本迁移**，而 InSpatio-World 更偏 **几何锚定 + 世界状态建模 + 新视角可交互视频**。

## 和 InSpatio-World 的关系
- **DreamZero**：世界动作模型 → 零样本策略
- **InSpatio-World**：state-anchored 4D world → 可控新视角观察生成
- 一个更偏 **policy**，一个更偏 **world state / observation**
- 两者结合，正好构成主人可以重点追的研究机会：**世界状态模型 + 动作模型耦合**
