# Real-to-Sim-to-Real Shared Autonomy (2603.17016)

> 深挖时间：R680 | 方向：D07_Isaac强化学习机械臂控制 | 状态：✅ 深挖入库

## 论文信息
- **标题**：Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy
- **作者**：Shuo Sha et al. | 2026-03-17
- **链接**：https://arxiv.org/abs/2603.17016
- **方向关系**：D07 sim-to-real 链路 + HITL refinement 协议直接参考

## 一、与本方向的关系（1句话）
kNN human surrogate 从 <5min 真实遥操作数据建模操作者行为，在 sim 中训练 residual copilot RL，为 D07 空中机械臂的 post-pretraining adaptation + HITL refinement 双层协议提供可直接落地的参考配方。

## 二、核心贡献
1. **kNN human surrogate**：用 <5min 真实遥操作数据拟合操作者行为模型，作为 sim 中 copilot RL 的训练信号，避免了"sim 中学到的策略与真实操作者行为不匹配"这一核心问题
2. **residual copilot RL**：在 sim 中训练一个加性修正策略，叠加在人类操作者的基础动作上，专门负责修正操作者未注意到的误差（接触力、位置偏差等）
3. **双通道验证**：仿真实验 + 16 人用户研究（nut threading、gear meshing、peg insertion），证明新手成功率提升、熟练者执行效率提升
4. **下游 IL 收益**：copilot-assisted 遥操作产生更高质量的示教数据，可用于后续 imitation learning

## 三、核心方法流程
```
真实遥操作(<5min) → kNN human surrogate (sim中建模操作者)
    → residual copilot RL (在sim中训练修正策略)
        → 真实部署: 人类操作 + copilot 修正 → 更高质量示教数据
```

关键工程细节：
- kNN surrogate：用历史状态-动作对预测"操作者此时会怎么做"
- residual 策略：输出 Δaction，而不是全新 action，保留人类操作者的原始意图
- sim 中训练：用 Isaac Gym / Isaac Lab 物理引擎

## 四、可借鉴的技术点（具体可用）

1. **kNN surrogate 作为操作者先验**：主人后续做空中机械臂遥操作时，可以先用 5 分钟收集操作者数据，拟合 kNN 先验，再在 sim 中训 residual copilot，避免"sim 策略与真实操作者不匹配"的问题

2. **residual copilot 双层协议**：
   - Layer 1（post-pretraining adaptation）：在 sim 中训好基础策略后，用 kNN surrogate 做行为对齐
   - Layer 2（HITL refinement）：真实部署时，人类操作者的实时修正作为在线强化信号，持续微调 residual 策略

3. **高质量示教数据生成**：copilot-assisted 数据比纯 human teleop 质量更高（更少抖动、更精确的接触力），可以直接用于后续 VLA 的 SFT 或 IL warm start

## 五、局限/不足（我们可以改进的点）

1. **kNN surrogate 的泛化性**：kNN 本质上是记忆型模型，对未见过的任务/物体泛化能力有限。主人后续若做空中机械臂的精细操作（如抓取未知物体），可能需要把 kNN 换成学习型策略（如轻量 LSTM）

2. **residual 策略的修正空间假设**：假设人类操作者的基础动作大部分正确，只做局部修正。如果操作者在陌生任务中大部分动作都是错的（如首次飞控空中机械臂），residual 策略可能无法弥补基础策略的错误

3. **接触力感知缺失**：当前方法主要基于位置/姿态修正，对接触力/力矩的感知和修正没有显式建模。主人后续若做空中机械臂的精确操作（如插拔、对准），需要把力觉反馈也加入 residual 层

## 六、对 D07 协议的补充

D07 原有协议：**训练器对照 + 奖励层 + post-pretraining adaptation + HITL refinement + deployment risk coverage**

本论文新增维度：
- **操作者先验建模**（kNN surrogate）：用少量数据建模"谁在操作"，降低 sim-to-real 行为差距
- **residual copilot 架构**：显式分离"人类意图"和"策略修正"，适合需要 HITL 介入的精细操作任务

后续 D07 实验设计应补充：
> **操作者先验层**：少量（<5min）人类遥操作数据 → kNN/LSTM surrogate → residual RL adaptation
> 对照：有无操作者先验对齐、有无 residual 修正、修正空间大小

## 七、归档状态
- ✅ 已深挖入库
- 关联 R674 候选-R674 入队
- R680 完成全文深挖
