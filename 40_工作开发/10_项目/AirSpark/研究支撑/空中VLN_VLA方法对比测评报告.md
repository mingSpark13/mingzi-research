# 空中 VLN / VLA 方法对比测评报告

> 维护人：花火｜创建时间：2026-05-22｜状态：持续更新中
> 本文档用于系统性对比空中 VLN/VLA 各主流方法在统一基准上的表现，按方法逐步填充实验结果。

---

## 一、测评说明

### 1.1 测评目标
- 在统一基准（AirSpark / TravelUAV / OpenUAV 等）上横向对比各方法
- 覆盖导航、目标搜索、细粒度控制、导航→操作等多类任务
- 记录每个方法的复现状态、超参配置、实验结论

### 1.2 评测环境

| 项目        | 配置                                        |
| --------- | ----------------------------------------- |
| 仿真平台      | AirSpark（UE5.7 + AirSim fork + School 地图） |
| 物理后端      | Kinematic（导航任务）/ MuJoCo（操作任务）             |
| Python 环境 | Python 3.10，conda                         |
| GPU       | —                                         |
| 评测脚本      | `tools/airspark_dataset_tools`            |
| 基准版本      | AirSpark batch schema v2，FLU 坐标系          |
|           |                                           |

### 1.3 通用评测指标说明

| 指标   | 全称                              | 说明                 |
| ---- | ------------------------------- | ------------------ |
| SR   | Success Rate                    | 成功到达目标的 episode 比例 |
| SPL  | Success weighted by Path Length | 路径效率加权成功率          |
| NE   | Navigation Error                | 终点与目标的平均距离误差（米）    |
| OSR  | Oracle Success Rate             | 轨迹上任意点到达目标的比例      |
| TCR  | Task Completion Rate            | 多阶段任务子步骤完成比例       |
| CR   | Collision Rate                  | 碰撞次数 / 总步数         |
| CSPL | Collision-Safe SPL              | 碰撞惩罚加权 SPL         |
| EE   | Energy Efficiency               | 实际能量 / 理论最短路径能量    |
| TS   | Trajectory Smoothness           | 加速度变化率（jerk）均值     |

---

## 二、待测方法清单

下表列出计划纳入对比的方法，按任务类型分组。`复现状态` 随测评进展更新。

### 2.1 路线跟随型 VLN（Route-following VLN）

| #    | 方法                          | 来源        | 骨干模型                 | 动作空间     | 代码/权重                                      | 复现状态  | 备注                    |
| ---- | --------------------------- | --------- | -------------------- | -------- | ------------------------------------------ | ----- | --------------------- |
| R-01 | AerialVLN Baseline          | ICCV 2023 | LSTM + Attention     | 离散 4-DoF | [GitHub](https://github.com/AirVLN/AirVLN) | ⬜ 待复现 | 首个空中 VLN baseline     |
| R-02 | AVDN                        | ACL 2023  | HAA-Transformer      | 离散 3-DoF | —                                          | ⬜ 待复现 | 多轮对话导航                |
| R-03 | AerialVLA（TravelUAV SOTA 版） | AAAI      | 端到端 VLA              | 连续 3-DoF | —                                          | ⬜ 待复现 | TravelUAV unseen SOTA |
| R-04 | AutoFly                     | ICLR 2026 | pseudo-depth encoder | 连续 6-DoF | —                                          | ⬜ 待复现 | TravelUAV seen +14.0% |
| R-05 | OpenFly-Agent               | ICLR 2026 | keyframe-aware       | 连续       | —                                          | ⬜ 待复现 | 100K 轨迹预训练            |
|      |                             |           |                      |          |                                            |       |                       |

### 2.2 目标搜索 / 连续导航（Goal Nav / Object Search）

| #    | 方法                | 来源               | 骨干模型          | 动作空间     | 代码/权重 | 复现状态  | 备注                      |
| ---- | ----------------- | ---------------- | ------------- | -------- | ----- | ----- | ----------------------- |
| G-01 | OpenUAV Baseline  | ICLR 2025        | Transformer   | 连续 6-DoF | —     | ⬜ 待复现 | 三档助手引导                  |
| G-02 | AirVLN-R1         | arXiv 2601.03707 | SFT + RFT     | 连续 6-DoF | —     | ⬜ 待复现 | 137K 真实城市数据             |
| G-03 | CognitiveDrone-R1 | arXiv 2503.01378 | VLM + VLA 两段式 | 实时 4D    | —     | ⬜ 待复现 | R1 版 SR 77.2%           |
| G-04 | OnFly             | arXiv 2603.10682 | 双 agent 频次解耦  | 连续 6-DoF | —     | ⬜ 待复现 | 零样本 SR 26.4%→67.8%      |
| G-05 | VLA-AN            | arXiv 2512.15258 | 3DGS 域适应      | 连续 6-DoF | —     | ⬜ 待复现 | 机载吞吐提升 8.3x             |
| G-06 | LiteVLA-H         | arXiv 2605.00884 | 256M 轻量 VLA   | 连续 6-DoF | —     | ⬜ 待复现 | Jetson AGX Orin 19.74Hz |

### 2.3 细粒度飞行控制（Fine-grained Control）

| # | 方法 | 来源 | 骨干模型 | 动作空间 | 代码/权重 | 复现状态 | 备注 |
|---|---|---|---|---|---|---|---|
| F-01 | UAV-Flow Baseline | NeurIPS 2025 | VLA | 连续低层 | — | ⬜ 待复现 | 首个真机 VLA 部署 |

### 2.4 导航 + 操作（Navigate-then-Manipulate）

| #    | 方法               | 来源               | 骨干模型            | 动作空间         | 代码/权重 | 复现状态  | 备注               |
| ---- | ---------------- | ---------------- | --------------- | ------------ | ----- | ----- | ---------------- |
| M-01 | AIR-VLA Baseline | arXiv 2601.21602 | —               | UAV 4D + 机械臂 | —     | ⬜ 待复现 | 首个空中操作 benchmark |
| M-02 | AirVLA（π0 迁移）    | arXiv 2603.25038 | π0 + PAG        | UAV + 机械臂    | —     | ⬜ 待复现 | 460 次真实实验        |
| M-03 | DroneVLA         | HRI 2026         | DINO + VLA + A* | A* + 视觉伺服    | —     | ⬜ 待复现 | 定位误差 0.070m      |
| M-04 | AERMANI-VLM      | arXiv 2511.01472 | VLM + 技能库       | 分层技能         | —     | ⬜ 待复现 | 分层安全策略           |
|      |                  |                  |                 |              |       |       |                  |

### 2.5 自研方法 / AirSpark Baseline

| # | 方法 | 版本 | 骨干模型 | 动作空间 | 状态 | 备注 |
|---|---|---|---|---|---|---|
| A-01 | AirSpark Rule-based Nav | v1.0 | A*/Theta* + DWA | 连续 6-DoF | ⬜ 待实现 | 可解释 baseline，P3 目标 |
| A-02 | AirSpark VLA（π0.5 微调） | v1.0 | π0.5 | 连续 6-DoF | ⬜ 待实现 | P4 目标 |

---

## 三、测评结果汇总表

> 说明：`—` 表示该基准未测试或不适用；`*` 表示引用原论文数据（非本地复现）；空白格待填充。

### 3.1 TravelUAV 基准（Route VLN，Seen / Unseen）

| 方法                              | Seen SR↑ | Seen SPL↑ | Unseen SR↑     | Unseen SPL↑   | 测试时间 | 备注        |
| ------------------------------- | -------- | --------- | -------------- | ------------- | ---- | --------- |
| AerialVLN Baseline（R-01）*       | —        | —         | —              | —             | —    | 原论文数据     |
| AerialVLA TravelUAV SOTA（R-03）* | —        | —         | —              | —             | —    | AAAI SOTA |
| AutoFly（R-04）*                  | —        | —         | +14.0% vs base | +7.9% vs base | —    | ICLR 2026 |
| OpenFly-Agent（R-05）*            | —        | —         | —              | —             | —    | —         |
| **AirSpark Rule-based（A-01）**   |          |           |                |               |      | 待测        |
| **AirSpark VLA（A-02）**          |          |           |                |               |      | 待测        |

### 3.2 OpenUAV 基准（Object Search，连续 6-DoF）

| 方法                            | NE↓（m） | SR↑ | OSR↑ | SPL↑ | 测试时间 | 备注    |
| ----------------------------- | ------ | --- | ---- | ---- | ---- | ----- |
| OpenUAV Baseline（G-01）*       | —      | —   | —    | —    | —    | 原论文数据 |
| CognitiveDrone-R1（G-03）*      | —      | —   | —    | —    | —    | —     |
| **AirSpark Rule-based（A-01）** |        |     |      |      |      | 待测    |
|                               |        |     |      |      |      |       |

### 3.3 AirSpark 内部基准（School 地图，PointNav）

| 方法 | SR↑ | SPL↑ | NE↓（m） | CR↓ | EE↑ | TS↑ | 测试 episode 数 | 测试时间 |
|---|---|---|---|---|---|---|---|---|
| AirSpark Rule-based（A-01） | | | | | | | | |
| OnFly（G-04） | | | | | | | | |
| VLA-AN（G-05） | | | | | | | | |
| LiteVLA-H（G-06） | | | | | | | | |
| AirSpark VLA π0.5（A-02） | | | | | | | | |

### 3.4 AirSpark 内部基准（School 地图，Navigate-then-Manipulate）

| 方法 | NM-SR↑ | NM-SPL↑ | GSR↑ | PCRT↓（s） | CR↓ | 测试 episode 数 | 测试时间 |
|---|---|---|---|---|---|---|---|
| AIR-VLA Baseline（M-01） | | | | | | | |
| AirVLA π0+PAG（M-02） | | | | | | | |
| AirSpark VLA（A-02） | | | | | | | |

---

## 四、各方法详细测评记录

> 每个方法独立一节，记录复现过程、超参、实验日志、结论。

---

### R-01 AerialVLN Baseline

**基本信息**

| 项目 | 内容 |
|---|---|
| 论文 | AerialVLN: Towards Vision-and-Language Navigation for UAVs（ICCV 2023） |
| arXiv | — |
| 代码 | https://github.com/AirVLN/AirVLN |
| 权重 | — |
| 复现状态 | ⬜ 待复现 |

**方法概述**

首个空中 VLN 基准方法。基于 AirSim 仿真，8,446 条轨迹，离散 4-DoF 航点动作空间。使用 LSTM + Attention 架构，输入单视角 RGB + 语言指令，输出离散导航动作。

**复现配置**

| 超参 | 值 |
|---|---|
| 基准 | TravelUAV |
| 动作空间 | 离散 4-DoF |
| 输入分辨率 | — |
| batch size | — |
| 推理设备 | — |

**实验日志**

```
# 待填充
```

**结论**

> 待填充

---

### G-04 OnFly

**基本信息**

| 项目 | 内容 |
|---|---|
| 论文 | OnFly: Online Adaptive VLA for Aerial Navigation（arXiv 2603.10682） |
| arXiv | 2603.10682 |
| 代码 | — |
| 权重 | — |
| 复现状态 | ⬜ 待复现 |

**方法概述**

双 agent 频次解耦架构：高频低层控制 agent + 低频高层语义 agent，配合语义-几何验证器。零样本 SR 从 26.4% 提升到 67.8%，Jetson Orin NX 推理延迟 0.81s。

**复现配置**

| 超参 | 值 |
|---|---|
| 基准 | AirSpark PointNav |
| 动作空间 | 连续 6-DoF |
| 推理设备 | — |
| 推理延迟目标 | <1s |

**实验日志**

```
# 待填充
```

**结论**

> 待填充

---

### G-06 LiteVLA-H

**基本信息**

| 项目 | 内容 |
|---|---|
| 论文 | LiteVLA-H: Lightweight VLA for Onboard Aerial Navigation（arXiv 2605.00884） |
| arXiv | 2605.00884 |
| 代码 | — |
| 权重 | — |
| 复现状态 | ⬜ 待复现 |

**方法概述**

256M 参数机载 VLA，双速率推理（动作分支 19.74Hz，语义输出 6.08-6.67Hz）。混合三类数据微调：反应式飞行 + 航空语义 + 通用字幕/VQA。Jetson AGX Orin 可部署。

**复现配置**

| 超参 | 值 |
|---|---|
| 基准 | AirSpark PointNav |
| 动作空间 | 连续 6-DoF |
| 推理设备 | Jetson AGX Orin / GPU |
| 动作推理频率目标 | ≥10Hz |

**实验日志**

```
# 待填充
```

**结论**

> 待填充

---

### A-01 AirSpark Rule-based Nav（自研）

**基本信息**

| 项目 | 内容 |
|---|---|
| 方法 | A*/Theta* 全局规划 + DWA 局部避障 + Waypoint Follower |
| 版本 | v1.0 |
| 状态 | ⬜ 待实现（P3 目标） |
| 代码位置 | `Plugins/AirSim/Source/AirSpark/Navigation/` |

**方法概述**

可解释 rule-based baseline。2.5D occupancy grid 建图，A*/Theta* 全局路径规划，DWA 局部避障，WaypointExecutor 执行。作为所有学习方法的对照基线，验证场景/传感器/评测是否正确。

**实验日志**

```
# 待填充
```

**结论**

> 待填充

---

## 五、消融实验记录

> 针对自研方法的消融实验，记录各组件贡献。

| 实验组 | 方法变体 | SR↑ | SPL↑ | NE↓ | 说明 |
|---|---|---|---|---|---|
| Ablation-01 | Full model | | | | 完整方法 |
| Ablation-02 | w/o depth | | | | 去掉深度输入 |
| Ablation-03 | w/o language | | | | 去掉语言指令 |
| Ablation-04 | discrete action | | | | 离散化动作空间 |

---

## 六、复现问题记录

> 记录复现过程中遇到的问题、解决方案和注意事项，供后续参考。

| 方法 | 问题描述 | 解决方案 | 状态 |
|---|---|---|---|
| — | — | — | — |

---

## 七、更新日志

| 日期 | 更新内容 |
|---|---|
| 2026-05-22 | 创建文档，设计框架，填充待测方法清单（R-01~05, G-01~06, F-01, M-01~04, A-01~02） |
