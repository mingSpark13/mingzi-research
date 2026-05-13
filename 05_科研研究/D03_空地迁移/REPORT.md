# D03: 空地迁移 研究报告

> 最后更新：2026-04-17 | 成熟度：🟡中期（R779 补齐最小迁移验收矩阵，开始把“能不能迁”收束成“哪些层能迁、哪些层必须加壳”）
> 状态：🟡 推进中

## 一、研究背景与动机

地面机械臂的前沿方法（ACT/Diffusion Policy/VLA/RL）积累了大量成果，但直接迁移到空中操作面临根本性挑战：(1) 振动和负载干扰导致末端精度下降；(2) 飞行动力学约束限制工作空间和运动速度；(3) 视野和传感器配置完全不同；(4) 空中数据采集成本远高于地面。

现阶段最关键的问题已经不是“地面方法能否一点都不改直接飞起来”，而是要把迁移对象拆开看：**视觉表征、任务语义、动作先验、低层控制壳、安全约束、sim-to-real 组件** 这些层到底谁能直接复用，谁必须为空中平台单独补齐。D03 的价值，就是把这条迁移链路从经验判断压成可复现实验协议。

## 二、相关工作梳理

### 2.1 空中 VLA 迁移
- **π-Make-It-Fly** — 发现视觉表征可迁移但控制动力学不可迁移，提出 Payload-Aware Guidance
- **AIR-VLA / AirVLA** — 给出当前最强的定量证据：视觉先验可以零样本迁移，但必须在推理时注入载荷/动力学约束，pick-and-place 从 23% 提升到 50%，Gaussian Splatting 合成导航数据可把 navigation 从 81% 提到 100%
- **Aerial VLN survey / roadmap (2604.07705 / 2604.13654)** — 进一步确认空中系统的 sim-to-real gap 不是单一问题，而是“感知保真 + 动力学执行 + 机载算力预算”三者耦合

### 2.2 空中操作系统
- **Unified Aerial Grasping** — 语言指令+主动探索+6-DoF抓取端到端（与龙虾项目最相关）
- **AeroPlace-Flow** — 语言引导空中物体放置，Visual Foresight + Object Flow
- **AkinoPDF** — 解析+微分平坦规划

### 2.3 空中机械臂控制
- **Aerial Manipulator RL** (2512.21085) — RL+经典控制组合，厘米级精度
- **Strain-Parameterized** (2603.23333) — 空中连续体机械臂
- **Precise Aggressive Aerial Maneuvers with Sensorimotor Policies (2604.05828)** — 虽不是操作迁移论文，但给 D03 一个很实用的部署结论：sim-to-real 成功不只靠更强 policy，本质上还依赖 **平滑动作约束、速度约束、感知蒸馏/正则化** 这些低层执行壳。对 D03 来说，这说明“地面策略迁到空中”大概率也需要类似的执行稳定壳，而不是只做高层表征适配。

### 2.4 Gap
1. π-Make-It-Fly / AirVLA 证明了视觉表征可迁移，但**怎么迁移控制动力学**仍未系统化
2. 缺少可复现的「地面→空中」迁移方法论，尤其缺少“表征层、策略层、控制壳层”分层验收
3. 空中操作+导航的联合框架缺失（→对接 D06）
4. 缺少部署导向的 sim-to-real 约束清单，现有工作常把“迁移成功”写成单个成功率，不足以指导主人后续实验

## 三、我们的创新方向

### 3.1 核心创新点
1. **C1: 动力学感知的策略迁移层**
   - 在 π-Make-It-Fly 基础上，显式建模飞行动力学约束作为策略适配层
   - 不追求“原策略裸迁移”，而是允许在 inference-time 注入 payload / jerk / acceleration / safety guidance

2. **C2: 地面数据→空中策略的分层迁移方法论**
   - 系统拆分哪些可迁移（视觉表征、任务语义、目标关系）
   - 哪些必须适配（控制频率、动作空间、稳定性壳层、安全约束）
   - 把“能迁移什么”从叙述压成验收矩阵

3. **C3: 导航-操作一体化迁移接口**
   - 与 D06 联动，从导航阶段输出的目标位姿/语义地图无缝切换到操作阶段
   - 把地面 manipulation policy 迁移为 NtM 中的操作子模块，而不是孤立空中抓取器

### 3.2 拟定方法框架

```text
地面策略先验（ACT / Diffusion Policy / VLA / RL）
        │
        ├─ 可直接复用层：视觉表征 / 任务语义 / 目标关系表示
        │
        ├─ 迁移适配层：动作接口映射 + payload-aware guidance + dynamics-aware cost
        │
        ├─ 低层执行壳：smoothness / speed / safety constraint / recovery policy
        │
        └─ 空中平台执行：导航后操作 / 近距接触 / 失败回退重规划
```

核心判断：D03 最可能成立的路线不是“端到端从 ground policy 直接飞”，而是**ground prior + inference-time dynamics guidance + lightweight execution shell**。

### 3.3 与现有方法的关键差异

| 对比维度 | 现有空中迁移工作 | 我们的方法 |
|---------|----------------|----------|
| 迁移对象 | 通常只说视觉/策略整体迁移 | 拆成表征层、动作层、控制壳层分别验收 |
| 动力学处理 | 多为后验补丁或任务内技巧 | 显式作为迁移适配层核心变量 |
| 评测方式 | 单一成功率为主 | ground→air gap、执行平滑度、部署成本联合验收 |
| 与导航关系 | 多数只看操作本身 | 与 D06 的 NtM 接口统一设计 |
| 部署导向 | sim-to-real 细节零散 | 把执行稳定壳和安全约束写进主协议 |

## 四、实验设计

### 4.1 迁移验证主线
1. **Ground policy prior 复用**：先验证地面表征/任务语义能否直接迁到空中任务输入
2. **Dynamics guidance 注入**：在不重训或少量微调前提下，加入 payload-aware / dynamics-aware guidance
3. **Execution shell 补强**：增加 smoothness、speed constraint、recovery 壳层，验证是否进一步提升部署稳定性
4. **NtM 对接**：把 D06 导航输出接入操作阶段，评估“导航→操作”接口是否会放大迁移误差

### 4.2 最小迁移验收矩阵（R779 新增）

> 目标：先验证 D03 的核心判断是否成立，即“视觉先验可迁，动力学与执行壳必须补”。

| 实验 | 对比设置 | 关键指标 | 通过门槛 |
|------|---------|---------|---------|
| **T1 表征迁移** | ground visual prior 冻结迁移 vs 从头训练 | 成功率、收敛步数、样本效率 | 冻结迁移在样本效率上显著更优 |
| **T2 动力学适配收益** | 无 guidance vs payload/dynamics guidance | 成功率、碰撞率、轨迹可行率 | 成功率提升且碰撞率下降 |
| **T3 执行壳收益** | guidance-only vs guidance+execution shell | jerk、速度超限率、末端稳定误差 | 平滑度显著改善且成功率不降 |
| **T4 导航-操作接口** | 直接给定目标位姿 vs 接 D06 导航输出 | 联合成功率、重规划恢复率 | 接入导航后性能退化可控 |

### 4.3 建议首轮 baseline
- **Base-1**: 地面策略直接迁移（裸迁移）
- **Base-2**: 裸迁移 + dynamics guidance（对标 AirVLA 思路）
- **Base-3**: 裸迁移 + dynamics guidance + execution shell（D03 主推路线）
- **Upper-bound**: 空中平台专门训练策略

### 4.4 评价指标
- **任务成功率**：pick / place / contact inspection
- **轨迹可行率**：是否满足速度、姿态、碰撞约束
- **末端稳定误差**：目标接触或抓取前的最终误差
- **平滑度**：速度/加速度/jerk
- **部署成本**：是否需要重训、微调轮数、额外数据量
- **联合成功率**：D06 导航 + D03 操作串联后整体成功率

### 4.5 当前阶段判断
- 最有希望直接迁移的是 **视觉表征、目标语义、关系表示**
- 最不该幻想“零改动复用”的是 **连续控制策略本体**
- 真正该优先验证的是 **inference-time dynamics guidance + execution shell** 是否足够把地面策略拉到可用区间

## 五、后续 TODO
- [ ] π-Make-It-Fly / AirVLA 源码与实验设置复核，量化 ground→air gap
- [ ] 把 AirVLA 的 payload-aware guidance 具体化为 D03 可复用的适配接口
- [ ] 设计 T1-T4 最小迁移实验，对齐主人当前 UE/AirSpark 资产
- [ ] 与 D06 的 Navigate-then-Manipulate 接口对齐
- [ ] 补一张“可迁移层 / 必适配层 / 必重训层”三分图，供后续论文直接使用
