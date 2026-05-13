---
summary: "ManiDreams 是一个开源的模块化操作规划框架，通过**不确定性感知的任务特定直觉物理模型**，无需重训练即可自适应应对环境各类不确定性（物体属性、初始状态、外部扰动）。核心范式为 **sample-predict-constrain**：用 DRIS 表示分布式状态、TSIP 预测前向动力学、caging 约束限制不确定性边界，最终通过求解器选择鲁棒动作。在真实机器人高不确定性任务上验证有效，面对逐步升级的扰动显著优于 RL 基线。"
title: "ManiDreams: An Open-Source Library for Robust Object Manipulation via Uncertainty-aware Task-specific Intuitive Physics"
arxiv_id: "2603.18336"
authors: "G Wang, K Ren, AS Morgan, K Hang"
institution: "Rice University (RobotPI Lab)"
conf: "arXiv 2025"
date: "2025-03"
domain: "机器人操作"
direction: "D04_跨载体泛化"
pdf_path: "Notebook/30_论文研究/01_论文库/通用操作/2603.18336_ManiDreams.pdf"
source_url: "https://arxiv.org/abs/2603.18336"
github: "https://rice-robotpi-lab.github.io/ManiDreams/"
reading_date: "2026-04-20"
reading_status: "已读"
tags: ["操作鲁棒性", "不确定性感知", "直觉物理", "无需重训练", "模块化框架", "约束优化"]
---

# ManiDreams: Robust Object Manipulation via Uncertainty-aware Task-specific Intuitive Physics

## 📌 三句话摘要

ManiDreams 是一个开源的模块化操作规划框架，通过**不确定性感知的任务特定直觉物理模型**，无需重训练即可自适应应对环境各类不确定性（物体属性、初始状态、外部扰动）。核心范式为 **sample-predict-constrain**：用 DRIS 表示分布式状态、TSIP 预测前向动力学、caging 约束限制不确定性边界，最终通过求解器选择鲁棒动作。在真实机器人高不确定性任务上验证有效，面对逐步升级的扰动显著优于 RL 基线。

## 🎯 价值评估

**评分：⭐⭐⭐⭐（4/5）**

- **无需重训练**是最大亮点，直接在推理时适应新环境，工程价值极高
- 模块化设计（DRIS + TSIP + caging + solver）可插拔，易于集成到现有系统
- 对 D04 跨载体泛化方向有直接参考：不确定性感知 + 约束优化思路可迁移到跨形态操作
- 开源，可直接复用

## 🔑 核心创新

### 四大可组合抽象（sample-predict-constrain 范式）

```
环境状态（不确定）
      │
      ▼
[1] DRIS（Domain-Randomized Instance Set）
    - 分布式状态表示
    - 对物体属性/初始状态进行域随机化采样
    - 输出：一组可能的状态实例
      │
      ▼
[2] TSIP（Task-Specific Intuitive Physics）
    - 任务特定的前向动力学预测
    - 后端无关（可接物理引擎/神经网络/解析模型）
    - 输出：每个状态实例的动力学预测
      │
      ▼
[3] Caging Constraints（笼形约束）
    - 限制不确定性边界
    - 确保动作在最坏情况下仍然可行
    - 输出：可行动作空间
      │
      ▼
[4] Solver（求解器）
    - 在约束空间内选择最优动作
    - 输出：鲁棒动作
```

### 为什么叫"直觉物理"（Intuitive Physics）

- 不是精确物理仿真，而是任务特定的轻量动力学模型
- 只建模"完成任务所需"的物理关系，忽略无关细节
- 计算成本低，可在线实时运行

### 无需重训练的关键

- 不确定性通过 DRIS 的分布采样显式建模，不依赖训练数据覆盖
- Caging 约束在推理时动态计算，适应新的不确定性分布
- TSIP 是任务特定的，可以快速换新任务而不重训

## 📊 实验结果

| 实验 | 结果 |
|------|------|
| 真实机器人高不确定性任务 | 成功部署，鲁棒性显著 |
| vs RL 基线（逐步升级扰动） | ManiDreams 显著更优 |
| 模块化可组合性 | 5 类任务 × 多种 TSIP 后端均可运行 |
| 运行时开销 | 轻量，可实时 |

## 💡 可落地实验点

1. **D04 跨载体泛化**：DRIS 的域随机化状态表示思路可用于跨形态操作，对不同机器人形态的不确定性显式建模
2. **ZeroTracking**：Caging 约束思路可用于 UAV 跟踪中的鲁棒性保证——在目标位置不确定时，约束飞行动作在安全边界内
3. **AirSpark 操作任务**：TSIP 的轻量任务特定物理模型可作为空中操作的动力学预测模块

## ⚠️ 局限性

- TSIP 需要针对每类任务手动设计，泛化性有限
- Caging 约束的设计依赖任务先验知识
- 对高度动态、快速变化的场景（如高速飞行操作）效果待验证

## 🔗 知识图谱

- [[concepts/跨载体泛化]]
- [[concepts/具身智能]]
- [[concepts/规划与控制]]
- [[concepts/Sim2Real]]

## 📌 待探索问题

- TSIP 能否用神经网络自动学习，减少手工设计？
- Caging 约束与 CBF（Control Barrier Function）有何关联？
- 能否迁移到 UAV 空中抓取场景？

## 🔗 相关链接

- arXiv: https://arxiv.org/abs/2603.18336
- 项目主页: https://rice-robotpi-lab.github.io/ManiDreams/
- B站视频: https://b23.tv/VFEcrTf
