---
type: "overview"
id: "overview.方向_VLA_技术路线图"
pageType: "overview"
tags: ["VLA架构", "模仿学习", "数据飞轮", "跨载体泛化", "空中VLN"]
summary: "VLA技术路线三条主线：端到端原生VLA（高通用性/低可控性）vs 模块化层次化VLA（低通用性/高可控性） vs 扩散式统一架构（平衡点），主人研究聚焦空中VLN+精细操作的层次化解耦"
updated: "2026-05-16"
---

# 方向：VLA 技术路线图

## 一句话结论

> **端到端 vs 模块化是VLA路线的根本张力**：端到端通用性强但可控性差；层次化模块化可控性强但迁移困难；扩散式统一架构是当前最有前景的折中方案。

## 技术格局

### 路线一：端到端原生 VLA

**代表工作**：RT-2, OpenVLA, VLA-GSE, PriorVLA

```
视觉语言感知 → Transformer → 动作输出
```

- **优点**：通用性强，zero-shot泛化能力最强
- **缺点**：黑盒不可控，长程任务漂移，数据效率低
- **适用**：通用机器人感知-动作统一建模，开放世界任务

### 路线二：层次化模块化 VLA

**代表工作**：[[sources/source.2605.12167_MoLA|MoLA]], [[sources/source.2605.10925_PriorVLA|PriorVLA]], [[sources/source.2605.07381_Anchor_Centric_Adaptation|Anchor-Centric Adaptation]], [[concepts/ACT动作分块]]

```
语言指令 → 高层规划器 → 低层执行器（ACT/Diffusion/FlowMatching）
```

- **优点**：可控性强，每层可独立替换/优化
- **缺点**：模块间接口设计复杂，跨载体迁移需要重新设计
- **适用**：精细操作任务（Paper A低层执行器）

### 路线三：扩散式统一架构

**代表工作**：π₀, dVLA, Diffusion VLA

```
视觉 + 语言 + 动作 统一token化 → Diffusion/flow action head → 动作输出
```

- **优点**：兼顾通用性与可控性，多峰动作建模能力强
- **缺点**：推理延迟高（Diffusion）或实现复杂（flow matching）
- **适用**：复杂多峰任务，通用操作+精细执行统一建模

## 关键 Gap

| Gap | 描述 | 当前最优解 |
|-----|------|-----------|
| **长程漂移** | 端到端VLA在长时任务中误差累积 | 层次化解耦（MoLA）+ 外部纠正（UniSteer） |
| **Sim2Real鸿沟** | 仿真训练vs真机部署的分布偏移 | VLA-GSE + 物理适配器（AirVLA PG Transfer） |
| **跨载体泛化** | 从机械臂迁移到无人机载体 | OPFA latent action + RotVLA SO(n)旋转建模 |
| **高频控制** | 空中50Hz+控制需求 | Flow Matching（50Hz+）vs Diffusion（3-5Hz） |
| **数据效率** | VLA需要海量多样化数据 | 数据飞轮（RoboEvolve/F-ACIL）+ 仿真生成 |

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
3. 探索 [[sources/source.2605.10925_PriorVLA|PriorVLA]] 的双专家适配防止灾难性遗忘

**长期（6-12个月）**：
1. 构建完整三层架构（意图层/世界模型层/执行层）
2. 结合数据飞轮实现自主数据采集与策略更新
3. 在真实无人机平台验证跨载体泛化能力

## 来源与文献

- 端到端VLA基线：[[sources/source.2605.06175_VLA_GSE|VLA-GSE]] / [[sources/source.2605.10925_PriorVLA|PriorVLA]]
- 层次化代表：[[sources/source.2605.12167_MoLA|MoLA]] / [[sources/source.2026-03-27_ACT|ACT]]
- 扩散统一架构：[[sources/source.2603.14363_AerialVLA|AerialVLA]] / [[sources/dVLA_2509.25681|dVLA]]
- 跨载体泛化：[[sources/source.2605.13403_RotVLA|RotVLA]] / [[sources/source.2603.14522_OPFA|OPFA]]

## Related

- [[concepts/VLA架构]]
- [[comparisons/ACT动作分块_vs_扩散策略_vs_流匹配]]
- [[overview/方向_空中VLN_技术路线图]]
- [[overview/方向_跨载体泛化_技术路线图]]
