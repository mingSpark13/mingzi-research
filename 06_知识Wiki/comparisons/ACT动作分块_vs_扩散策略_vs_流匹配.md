---
type: "comparison"
id: "comparison.ACT_vs_DiffusionPolicy_vs_FlowMatching"
pageType: "comparison"
tags: ["ACT动作分块", "扩散策略", "流匹配", "VLA架构", "模仿学习"]
summary: "三种动作生成范式在生成方式/分布/速度/场景上各有取舍，ACT适合低频精细操作，Diffusion适合多峰任务，Flow Matching平衡速度与多模态"
updated: "2026-05-16"
---

# ACT vs Diffusion Policy vs Flow Matching

三种主流动作生成范式的系统对比，为主人研究中的低层执行器选型提供参考。

## 一句话结论

| 范式 | 推荐场景 | 不推荐场景 |
|------|---------|-----------|
| **ACT** | 精细双臂操作 (~10Hz)，低层执行 baseline | 高频控制，多峰动作分布 |
| **Diffusion Policy** | 复杂多峰任务 (~3-5Hz)，生成多样性要求高 | 边缘实时部署，高频控制 |
| **Flow Matching** | 高频控制 (~50Hz+)，跨载体动作生成 | 极端多峰分布（ODE求解器不稳定） |

## 详细对比表

| 维度 | [[concepts/ACT动作分块]] | [[concepts/扩散策略]] | [[concepts/流匹配]] |
|------|--------------------------|------------------------|---------------------|
| **生成方式** | Transformer 自回归输出 chunk | 条件去噪扩散（DDPM） | 连续速度场 + ODE 积分 |
| **动作分布** | 单峰高斯 | 多峰（天然建模） | 可调（单峰→多峰） |
| **推理频率** | ~10Hz | ~3-5Hz | ~50Hz+ |
| **推理步数** | 1 次 forward | 10-100 步去噪 | 5-20 步 ODE |
| **实现复杂度** | 低 | 高 | 中 |
| **训练稳定性** | 高 | 中 | 中 |
| **参数量级** | 几十 M | 几十～百 M | 几十 M |
| **chunk 机制** | 固定长度（8-16步） | 可变 horizon | 可变 horizon |
| **多峰建模** | ❌ | ✅ | △（依赖 velocity 参数化） |
| **边缘部署** | ✅（易优化） | ❌（计算重） | ✅（比 diffusion 轻） |
| **代表工作** | ACT, OpenVLA action head | Diffusion Policy, π₀ | π₀-fast, RDT, RotVLA |

## 核心差异解析

### 1. 生成机制的本质差异

**ACT（Transformer 自回归）**
- 给定观测，直接从分布 $p(a_{t:t+H}|o_t)$ 采样一个动作序列
- 本质是条件回归，输出确定性（单峰）
- 推理最快，但无法建模"同任务多解法"

**Diffusion Policy（去噪扩散）**
- 学习逆过程 $\epsilon_\theta(a_t, t, c)$，从纯噪声逐步恢复动作
- 本质是学习能量函数，多步去噪探索多峰分布
- 推理最慢，但多峰建模最强

**Flow Matching（连续归一化流）**
- 学习速度场 $v_t(a_t, c)$，通过 ODE 积分从噪声到数据分布
- 本质是学习向量场，积分路径比扩散短
- 推理速度居中，多峰建模能力介于两者之间

### 2. 推理延迟的工程含义

```
ACT:     ~100ms/步（单次 forward）
Diffusion: ~200-300ms/步（10步 DDIM = 2-3s/chunk）
FlowMatch: ~20ms/步（5步 ODE = 100ms/chunk）
```

对主人研究中的**空中精细操作**场景：
- 飞行器控制频率 ~50Hz（20ms/步），只有 Flow Matching 能满足
- 机械臂精细操作 ~10Hz（100ms/步），ACT 刚好，Diffusion 勉强

### 3. 多峰动作的实战意义

多峰分布场景：
- 同一抓取任务可以从左侧/右侧/正上方抓
- 柔性物体形变导致不同运动路径
- 人机协作中人类意图的多样性

**Diffusion** 天然处理；**ACT** 只能输出均值（绕开多峰）；**Flow Matching** 可通过条件化velocity参数部分处理。

## 主人研究中的选型建议

### Paper A 三层架构中的定位

| 层级 | 推荐范式 | 理由 |
|------|---------|------|
| **高层（意图/规划）** | — | 不涉及动作生成 |
| **中层（世界模型/MPC）** | Flow Matching | 需要 ~20ms 推理满足实时规划 |
| **低层（精细执行）** | ACT（baseline）/ Diffusion（多峰场景） | 10Hz精细操作，ACT够用；复杂场景用Diffusion |

### 具体场景推荐

| 任务 | 推荐 | 备选 |
|------|------|------|
| 空中抓取（刚性物体） | ACT 或 Flow Matching | — |
| 空中抓取（柔性物体/衣物） | Diffusion Policy | Flow Matching + 多峰velocity |
| 精细装配（插针/插线） | ACT（误差累积低） | Diffusion（需要多峰探索） |
| 四足 locomotion | Flow Matching（50Hz+） | ACT（固定频率） |
| 跨载体动作生成 | Flow Matching（RDT/RotVLA） | — |

## 来源与文献

- ACT奠基: [[sources/source.2026-03-27_ACT]]
- Diffusion Policy: [[sources/source.2024-09-24_ReKep]]（ReKep≠Diffusion，但可对照）
- Flow Matching: [[concepts/流匹配]] → 来源页 [[sources/source.2603.03960_SAT]] / [[sources/RDT2_2602.03310]]

## Related

- [[concepts/ACT动作分块]]
- [[concepts/扩散策略]]
- [[concepts/流匹配]]
- [[overview/方向_VLA_技术路线图]]
