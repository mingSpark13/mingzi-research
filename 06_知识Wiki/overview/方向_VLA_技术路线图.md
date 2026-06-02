---
type: "overview"
id: "overview.方向_VLA_技术路线图"
pageType: "overview"
tags: ["VLA架构", "模仿学习", "数据飞轮", "跨载体泛化", "空中VLN"]
summary: "D02 已从抽象的三路线对比继续收束到 planner/verifier/executor 与 latency-accountable semantic packet：端到端 VLA 负责 baseline，统一生成式低层负责执行器候选，真正的增量集中在可审计中层接口。"
updated: "2026-05-27"
---

# 方向：VLA 技术路线图

## 一句话结论

> **D02 现在的主问题已不是“要不要层次化”，而是“中层接口能不能被审计、延迟能不能被记账”**：端到端 VLA 继续做强 baseline，统一生成式低层负责动作质量，而真正决定 Paper A 是否成立的是 planner/verifier/executor 之间那层 latency-accountable semantic packet。

## 技术格局

### 路线一：端到端原生 VLA

**代表工作**：RT-2, OpenVLA, VLA-GSE, PriorVLA, [[sources/source.2605.02881_MolmoAct2|MolmoAct2]]

```
视觉语言感知 → Transformer → 动作输出
```

- **优点**：通用性强，zero-shot泛化能力最强
- **缺点**：黑盒不可控，长程任务漂移，难以说明语义何时过时、控制何时该拒绝执行
- **适用**：通用机器人感知-动作统一建模，开放世界任务

### 路线二：层次化模块化 VLA

**代表工作**：[[sources/source.2605.12167_MoLA|MoLA]], [[sources/source.2605.10925_PriorVLA|PriorVLA]], [[sources/source.2605.07381_Anchor_Centric_Adaptation|Anchor-Centric Adaptation]], [[concepts/ACT动作分块]], TIDAL, TIC-VLA

```
语言指令 → 高层规划器 → 低层执行器（ACT/Diffusion/FlowMatching）
```

- **优点**：可控性强，每层可独立替换/优化
- **缺点**：模块间接口设计复杂，跨载体迁移需要重新设计
- **适用**：需要 verifier、latency metadata 与安全约束显式交接的精细操作任务（Paper A 主叙事）
 - **适用**：需要 verifier、latency metadata 与安全约束显式交接的精细操作任务（Paper A 主叙事）

### 路线三：扩散式统一架构

**代表工作**：π₀, dVLA, Diffusion VLA, [[sources/source.2026-04-28_2604.24447_VLA_XPU_Deployment|VLA XPU Deployment]], [[sources/source.2603.24941_TIES_VLA|TIES]]

```
视觉 + 语言 + 动作 统一token化 → Diffusion/flow action head → 动作输出
```

- **优点**：兼顾通用性与可控性，多峰动作建模能力强
- **缺点**：推理延迟高（Diffusion）或实现复杂（flow matching）
- **适用**：复杂多峰任务，通用操作+精细执行统一建模

## 关键 Gap

| Gap | 描述 | 当前最优解 |
|-----|------|-----------|
| **语义延迟** | 高层语义更新慢，低层执行已进入新状态 | latency-aware packet + verifier gating（TIC-VLA / TIDAL） |
| **部署瓶颈** | backbone 算得慢、action expert 吃内存，真机控制率被拖垮 | 两阶段 profile + token pruning + cache/fusion（TIES / VLA XPU） |
| **跨载体泛化** | 从机械臂迁移到无人机载体 | OPFA latent action + RotVLA SO(n)旋转建模 |
| **高频控制** | 空中50Hz+控制需求 | Flow Matching（50Hz+）vs Diffusion（3-5Hz） |
| **数据效率** | VLA需要海量多样化数据 | 数据飞轮（RoboEvolve/F-ACIL）+ 仿真生成 |

## 最新推进（2026-05-27）

1. **Paper A 的胜负手已明确压到中层接口**：D02/PAPER 不再只是“三层更优雅”，而是要求 semantic packet 至少携带 intent_age、latency_offset、controller routing、safety budget，否则无法证明层次化真的比强端到端 baseline 多出可审计增益。
2. **低层候选改成“执行器矩阵”而非单一路线**：ACT、Diffusion、MMaDA/flow、MolmoAct2-style continuous expert、以及部署优化路线（TIES / VLA XPU）应被视作同一执行器对照表，而不是互相替代整个系统。
3. **评测口径同步升级**：后续不只看成功率和平均时延，还要单列轨迹平滑度、chunk stitching stability、单位 episode 计算开销，以及 stale semantic state 下 verifier 的拒绝/放行质量。
## 主人研究的切入点

### 明子的核心方向
- **空中VLN**（D06）：UAV + 语义导航 + 开放词汇目标定位
- **精细空中操作**（D03）：UAV + 机械臂全向操作
- **跨载体泛化**（D04）：多形态机器人动作统一

### 推荐的技术路线

**短期（1-3个月）**：
1. 以层次化VLA为主线，用 [[concepts/ACT动作分块]] 作为低层执行器 baseline
2. 接入 [[sources/source.2605.14805_Cross_Coupled_Regime_Dependent_Aerial_Manipulation|Cross-Coupled Aerial Manipulation]] 的残差MPC架构
3. 调研 [[sources/source.2605.13665_Robot_Squid_Game|Robot Squid Game]] 的课程学习泛化方案

**中期（3-6个月）**：
1. 引入 [[concepts/流匹配]] 替换 ACT 应对更高控制频率
2. 结合 [[sources/source.2605.13403_RotVLA|RotVLA]] 的 SO(n) 旋转建模处理空中姿态
3. 参考 [[sources/source.2605.06481_OA-WAM|OA-WAM]] 的对象可寻址 world-action 表征，评估结构化对象槽位是否优于纯 token 堆叠
3. 探索 [[sources/source.2605.10925_PriorVLA|PriorVLA]] 的双专家适配防止灾难性遗忘

**长期（6-12个月）**：
1. 构建完整三层架构（意图层/世界模型层/执行层）
2. 结合数据飞轮实现自主数据采集与策略更新
3. 在真实无人机平台验证跨载体泛化能力

## 来源与文献

- 端到端VLA基线：[[sources/source.2605.06175_VLA_GSE|VLA-GSE]] / [[sources/source.2605.10925_PriorVLA|PriorVLA]]
- 层次化代表：[[sources/source.2605.12167_MoLA|MoLA]] / [[sources/source.2026-03-27_ACT|ACT]]
- 扩散统一架构：[[sources/source.2603.14363_AerialVLA|AerialVLA]] / [[sources/dVLA_2509.25681|dVLA]]
- 外置知识记忆：[[sources/source.2605.18556_Key-Gram|Key-Gram]]，验证“不改主干、外接语言知识”对组合泛化和真实操作的增益
- 跨载体泛化：[[sources/source.2605.13403_RotVLA|RotVLA]] / [[sources/source.2603.14522_OPFA|OPFA]]

## Related

- [[concepts/VLA架构]]
- [[concepts/机器人策略分类_总览]]
- [[concepts/生成式策略_概念笔记]]
- [[comparisons/ACT动作分块_vs_扩散策略_vs_流匹配]]
- [[overview/方向_空中VLN_技术路线图]]
- [[overview/方向_跨载体泛化_技术路线图]]
- [[sources/source.2026-04-29_M2-VLA|M2-VLA]]
- [[sources/source.2603.24941_TIES_VLA|TIES]]
- [[sources/source.2026-04-28_2604.24447_VLA_XPU_Deployment|VLA XPU Deployment]]
