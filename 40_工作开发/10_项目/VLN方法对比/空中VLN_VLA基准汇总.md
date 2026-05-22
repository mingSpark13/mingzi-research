# 空中 VLN / VLA 基准汇总

> 维护人：花火｜创建时间：2026-05-22｜状态：持续更新中
> 本文档汇总空中 VLN/VLA 领域主要评测基准，供方法选型、实验设计和论文对比参考。

---

## 一、速查总表

按任务类型排列，覆盖数据规模、动作空间、评测指标、可用性等关键维度。

| 基准                   | 任务类型                 | 场景         | 数据规模                              | 动作空间         | 核心指标                | 现实性         | 公开状态    | 来源               |
| -------------------- | -------------------- | ---------- | --------------------------------- | ------------ | ------------------- | ----------- | ------- | ---------------- |
| **AerialVLN**        | Route VLN            | 城市开放       | 8,446 条轨迹                         | 离散 4-DoF     | SR / SPL / NE       | Synthetic   | ✅ 公开    | ICCV 2023        |
| **TravelUAV**        | Route VLN            | 城市         | —                                 | 连续 3-DoF     | SR / SPL            | Synthetic   | ✅ 公开    | AAAI             |
| **AVDN**             | Dialog Nav           | 城市         | 6,269 条轨迹                         | 离散 3-DoF     | SR / SPL            | Synthetic   | ✅ 公开    | ACL 2023         |
| **CityNAV**          | Goal Nav             | 真实城市       | 32,637 条轨迹，4.65 km²               | 连续 4-DoF     | SR / SPL / NE       | Real Recon  | ✅ 公开    | arXiv 2024       |
| **OpenUAV**          | Object Search        | 22 场景      | 12,149 条 6-DoF 轨迹                 | 连续 6-DoF     | NE / SR / OSR / SPL | Synthetic   | ✅ 公开    | ICLR 2025        |
| **AirNav**           | Goal Nav             | 真实城市       | 137K navigation samples           | 连续 6-DoF     | SR / SPL / NE       | Real Data   | 🔄 部分公开 | arXiv 2601.03707 |
| **IndoorUAV**        | Indoor VLN           | 1000+ 室内场景 | 16K+ instruction-trajectory pairs | 连续 6-DoF     | SR / SPL / NE       | Synthetic   | ✅ 公开    | AAAI 2026        |
| **UAV-ON**           | ObjectNav            | 14 UE 环境   | 1,270 实例级目标                       | 连续           | SR / SPL            | Synthetic   | ✅ 公开    | ACM MM 2025      |
| **HUGE-Bench**       | High-level VLA       | 4 数字孪生场景   | 256 万米轨迹，8 类任务                    | 连续 6-DoF     | TCR / CR / CSPL     | Real Recon  | ✅ 公开    | arXiv 2603.19822 |
| **UAV-Flow**         | Fine-grained Control | 真实部署       | —                                 | 连续低层         | 轨迹模仿精度              | Real Deploy | ✅ 公开    | NeurIPS 2025     |
| **CosFly-Track**     | UAV Visual Tracking  | 城市         | 12,000 条轨迹，2.4M timesteps         | 连续 6-DoF     | 跟踪精度 / 可见性          | Synthetic   | 🔄 部分公开 | arXiv 2605.17776 |
| **UAV-Track VLA**    | Semantic Tracking    | —          | 890K+ 帧，176 任务                    | 连续 6-DoF     | 跟踪成功率               | Synthetic   | 🔄 部分公开 | arXiv 2604.02241 |
| **AIR-VLA**          | Nav + Manip          | 实验室        | 3,000 遥操作 demo                    | UAV 4D + 机械臂 | 任务成功率               | Syn+Real    | 🔄 部分公开 | arXiv 2601.21602 |
| **AeroVerse**        | 全栈评测                 | 多场景        | Ego10k + Ego500k                  | —            | 5 类任务               | Real+Syn    | ✅ 公开    | arXiv 2408.15511 |
| **MM-UAVBench**      | MLLM 评测              | 多场景        | —                                 | —            | 19 类任务              | Real+Syn    | ✅ 公开    | arXiv 2512.23219 |
| **UAVReason**        | 空中推理                 | —          | —                                 | —            | 22 类推理              | Synthetic   | ✅ 公开    | arXiv 2604.05377 |
| **CognitiveDrone-B** | 认知推理                 | —          | —                                 | 实时 4D        | 任务成功率               | Synthetic   | ✅ 公开    | arXiv 2503.01378 |

---

## 二、各基准详细介绍

### 2.1 AerialVLN
**定位**：首个空中 VLN 基准，城市级开放环境路线跟随。

| 属性 | 内容 |
|---|---|
| 论文 | AerialVLN: Towards Vision-and-Language Navigation for UAVs |
| 会议 | ICCV 2023 |
| 仿真平台 | AirSim |
| 场景 | 城市开放环境 |
| 数据规模 | 8,446 条轨迹 |
| 动作空间 | 离散 4-DoF 航点（前/后/左/右/上/下/停止） |
| 观测模态 | 单视角 RGB |
| 评测指标 | SR / SPL / NE |
| 现实性 | Synthetic |
| 代码/数据 | https://github.com/AirVLN/AirVLN |

**特点与局限**
- 首个空中 VLN 基准，奠定了领域基础评测协议
- 离散动作空间，与真实连续控制有差距
- 单视角 RGB，感知信息有限
- 城市场景，无室内/半室内支持

---

### 2.2 TravelUAV
**定位**：城市路线跟随 VLN，当前多个方法的主要对比基准。

| 属性 | 内容 |
|---|---|
| 会议 | AAAI |
| 场景 | 城市 |
| 动作空间 | 连续 3-DoF |
| 观测模态 | 双视角 RGB |
| 评测指标 | SR / SPL（Seen / Unseen 分开报告） |
| 现实性 | Synthetic |
| 代码/数据 | — |

**特点与局限**
- 当前 AerialVLA、AutoFly、OpenFly-Agent 等方法的主要对比基准
- Seen / Unseen 分开评测，考察泛化能力
- 连续动作空间，比 AerialVLN 更贴近真实控制
- 双视角 RGB，感知信息略丰富

---

### 2.3 AVDN
**定位**：首个空中多轮对话导航基准，人类指挥官 + 无人机专家交互采集。

| 属性 | 内容 |
|---|---|
| 论文 | Aerial Vision-and-Dialog Navigation |
| 会议 | ACL 2023 Findings |
| 场景 | 城市 |
| 数据规模 | 6,269 条轨迹 |
| 动作空间 | 离散 3-DoF |
| 观测模态 | RGB + 对话历史 |
| 评测指标 | SR / SPL |
| 现实性 | Synthetic |
| 代码/数据 | — |

**特点与局限**
- 验证「持续对话 > 单轮指令」的价值
- 人工采集，数据质量高但规模有限
- 离散动作空间

---

### 2.4 CityNAV
**定位**：首个大规模真实城市空中 VLN 数据集，Cambridge + Birmingham 真实航拍。

| 属性 | 内容 |
|---|---|
| 论文 | CityNav: Language-Goal Aerial Navigation Dataset with Geographic Information |
| arXiv | 2406.14240 |
| 场景 | 真实城市（Cambridge + Birmingham） |
| 数据规模 | 32,637 条轨迹，4.65 km² |
| 动作空间 | 连续 4-DoF |
| 观测模态 | 多视角 RGB + 地理信息 |
| 评测指标 | SR / SPL / NE |
| 现实性 | Real Reconstruction |
| 代码/数据 | — |

**特点与局限**
- 真实城市航拍，地标空间关系理解挑战
- 规模大，覆盖面广
- 无操作任务，纯导航

---

### 2.5 OpenUAV / UAV-Need-Help
**定位**：基于 UE4 + AirSim 的仿真平台，连续 6-DoF 目标搜索，三档助手引导。

| 属性 | 内容 |
|---|---|
| 论文 | OpenUAV: A UAV Simulation Platform for Open-World Navigation |
| arXiv | 2410.07087 |
| 会议 | ICLR 2025 |
| 仿真平台 | UE4 + AirSim（含 CARLA 场景资源） |
| 场景 | 22 场景，89 类目标 |
| 数据规模 | 12,149 条连续 6-DoF 轨迹 |
| 动作空间 | 连续 6-DoF |
| 观测模态 | 五视角 RGB/Depth + UAV 状态 |
| 评测指标 | NE / SR / OSR / SPL |
| 现实性 | Synthetic |
| 代码/数据 | — |

**助手引导三档**
- L1：高频贴近 GT 连续指导
- L2：偏航时低频纠偏
- L3：仅危险场景安全兜底

**特点与局限**
- 连续 6-DoF 轨迹数据 + 多视角感知，是目前最完整的仿真 VLN 平台之一
- 无接触操作，纯导航/目标搜索

---

### 2.6 AirNav
**定位**：当前最大规模真实城市 UAV VLN 数据集，137K navigation samples。

| 属性 | 内容 |
|---|---|
| arXiv | 2601.03707 |
| 场景 | 真实城市 |
| 数据规模 | 137K navigation samples |
| 动作空间 | 连续 6-DoF |
| 观测模态 | 多视角 RGB |
| 评测指标 | SR / SPL / NE |
| 现实性 | Real Data |
| 方法 | AirVLN-R1（SFT + RFT 训练范式） |
| 代码/数据 | 部分公开 |

**特点与局限**
- 规模最大的真实城市 UAV VLN 数据集
- human-LLM collaborative pipeline，10 类 user personas 增强语言多样性
- 纯离散导航，无连续控制 + 操作

---

### 2.7 IndoorUAV
**定位**：连续室内 UAV VLN，基于 Habitat，1000+ 室内场景。

| 属性 | 内容 |
|---|---|
| 会议 | AAAI 2026 |
| 仿真平台 | Habitat |
| 场景 | 1000+ 室内场景 |
| 数据规模 | 16K+ instruction-trajectory pairs |
| 动作空间 | 连续 6-DoF |
| 观测模态 | RGB + Depth |
| 评测指标 | SR / SPL / NE |
| 现实性 | Synthetic |
| 代码/数据 | 公开 |

**特点与局限**
- 室内/半室内复杂结构导航，与城市低空互补
- 不构成城市低空操作方向的直接竞争

---

### 2.8 UAV-ON
**定位**：首个空中开放世界 ObjectNav 基准，不依赖细粒度路线指令。

| 属性 | 内容 |
|---|---|
| arXiv | 2508.00288 |
| 会议 | ACM MM 2025 |
| 仿真平台 | UE（高保真） |
| 场景 | 14 个高保真 UE 环境 |
| 数据规模 | 1,270 个实例级目标 |
| 动作空间 | 连续 |
| 观测模态 | RGB + 语义目标 |
| 评测指标 | SR / SPL |
| 现实性 | Synthetic |
| 代码/数据 | 公开 |

**特点与局限**
- 给高层语义目标，在开放世界里自主探索
- 补上「VLN 与 ObjectNav 的边界」
- 无操作任务

---

### 2.9 HUGE-Bench
**定位**：高层 VLA 过程执行基准，4 个真实数字孪生场景，过程导向 + 碰撞感知评测。

| 属性 | 内容 |
|---|---|
| arXiv | 2603.19822 |
| 场景 | 4 个真实数字孪生（3DGS-Mesh） |
| 数据规模 | 256 万米轨迹，8 类高层任务 |
| 动作空间 | 连续 6-DoF |
| 观测模态 | RGB（3DGS）+ 碰撞信息 |
| 评测指标 | TCR / CR / CSPL |
| 现实性 | Real Reconstruction |
| 代码/数据 | 公开 |

**与 OpenUAV 的本质区别**
- OpenUAV：逼真仿真里完成带辅助的目标搜索（realistic VLN/search）
- HUGE-Bench：理解一句高层命令并安全完成多阶段任务（high-level VLA/procedural execution）

**特点与局限**
- 过程导向评测（TCR/CR/CSPL），比 SR/SPL 更细粒度
- 3DGS-Mesh 真实纹理，Sim2Real 差距小
- 偏高层过程与安全评测，无接触操作和力/力矩

---

### 2.10 UAV-Flow
**定位**：首个真实世界语言条件细粒度 UAV 控制 benchmark，首次真机 VLA 部署。

| 属性 | 内容 |
|---|---|
| 论文 | UAV-Flow: Flying-on-a-Word Fine-grained UAV Control |
| arXiv | 2505.15725 |
| 会议 | NeurIPS 2025 |
| 场景 | 真实部署 |
| 动作空间 | 连续低层（速度控制） |
| 观测模态 | RGB + 原子指令 |
| 评测指标 | 轨迹模仿精度 |
| 现实性 | Real Deploy |
| 代码/数据 | 公开 |

**特点与局限**
- 定义 Flying-on-a-Word (Flow) 任务：语言→细粒度短程反应式飞行控制
- 首次真机 VLA 部署，无 sim-to-real gap
- VLA 范式优于 VLN 范式（论文结论）
- 仅覆盖细粒度控制，无接触操作

---

### 2.11 CosFly-Track
**定位**：城市 UAV 视觉跟踪基准，MuCO 多约束轨迹优化器。

| 属性 | 内容 |
|---|---|
| arXiv | 2605.17776 |
| 场景 | 城市 |
| 数据规模 | ~12,000 条轨迹，2.4M timesteps，334 小时 |
| 动作空间 | 连续 6-DoF |
| 观测模态 | RGB + metric depth + semantic seg + 6-DoF pose + target state/visibility |
| 评测指标 | 跟踪精度 / 可见性保持率 |
| 现实性 | Synthetic |
| 代码/数据 | 部分公开 |

**MuCO 优化器约束**：visibility、viewpoint quality、collision、smoothness、kinematic feasibility

**对 AirSpark 的启发**：可借鉴 MuCO 设计操作版轨迹优化器（approach optimizer + pre-contact pose optimizer）

---

### 2.12 AIR-VLA
**定位**：首个空中操作标准化数据集，UAV 4D pose + 机械臂关节，3000 条人工遥操作 demo。

| 属性 | 内容 |
|---|---|
| arXiv | 2601.21602 |
| 场景 | 实验室 |
| 数据规模 | 3,000 条人工遥操作 demonstrations |
| 动作空间 | UAV 4D pose + 机械臂关节 |
| 观测模态 | RGB + proprio |
| 评测指标 | 任务成功率 |
| 现实性 | Syn+Real |
| 代码/数据 | 部分公开 |

**覆盖任务**：base manipulation、object/spatial understanding、semantic reasoning、long-horizon planning

**局限**：实验室场景，无城市低空，无多类接触，无 Sim2Real 配对

---

### 2.13 AeroVerse
**定位**：全链路评测平台，仿真→预训练→微调→评测，5 类下游任务。

| 属性 | 内容 |
|---|---|
| arXiv | 2408.15511 |
| 场景 | 多场景（真实 + 仿真） |
| 数据 | AerialAgent-Ego10k + CyberAgent-Ego500k |
| 评测指标 | 5 类任务指标 |
| 现实性 | Real+Syn |
| 代码/数据 | 公开 |

---

### 2.14 MM-UAVBench
**定位**：MLLM 感知/认知/规划综合评测，19 类任务。

| 属性 | 内容 |
|---|---|
| arXiv | 2512.23219 |
| 评测对象 | 多模态大语言模型（MLLM） |
| 任务类型 | 感知 / 认知 / 规划，19 类 |
| 观测模态 | 多模态 UAV 图像 |
| 现实性 | Real+Syn |
| 代码/数据 | 公开 |

**用途**：上游认知能力评测锚点，可用于筛选适合空中任务的 VLM 骨干

---

### 2.15 UAVReason
**定位**：22 类空间/时序 aerial reasoning，暴露通用 VLM 在俯视场景下的脆弱性。

| 属性    | 内容                |
| ----- | ----------------- |
| arXiv | 2604.05377        |
| 任务类型  | 22 类空间/时序推理       |
| 观测模态  | RGB / Depth / Seg |
| 现实性   | Synthetic         |
| 代码/数据 | 公开                |

**核心发现**：通用 VLM 在俯视视角、小目标、重复纹理场景下表现脆弱

---

## 三、基准选型建议

### 3.1 按研究目标选基准

| 研究目标 | 推荐基准 | 理由 |
|---|---|---|
| 路线跟随 VLN 方法对比 | TravelUAV + AerialVLN | 当前主流对比基准，方法覆盖最广 |
| 连续 6-DoF 目标搜索 | OpenUAV | 连续动作 + 多视角 + 三档助手，最完整 |
| 真实城市导航 | AirNav + CityNAV | 真实数据，泛化性验证 |
| 高层 VLA 过程执行 | HUGE-Bench | 过程导向评测，3DGS 真实纹理 |
| 细粒度飞行控制 | UAV-Flow | 唯一真机部署基准 |
| 空中操作 | AIR-VLA | 唯一空中操作标准化数据集 |
| 认知能力压测 | MM-UAVBench + UAVReason | 上游 VLM 能力评测 |
| AirSpark 内部验证 | AirSpark PointNav（自建） | 与平台深度集成，可控性最强 |

### 3.2 AirSpark 推荐评测组合

**训练数据**：OpenFly（100K 自动生成）+ AeroVerse（预训练资源）+ CosFly-Track（跟踪阶段）

**评测-导航**：AirNav（真实城市）+ UAV-ON（开放世界）+ OpenUAV（6-DoF 搜索）

**评测-VLA**：HUGE-Bench（高层 VLA）+ UAV-Flow（细粒度控制）

**评测-操作**：AIR-VLA（空中操作基准）

**认知压测**：MM-UAVBench + UAVReason

---

## 四、评测指标对照表

| 指标    | 全称                              | 适用基准                         | 计算方式                   |
| ----- | ------------------------------- | ---------------------------- | ---------------------- |
| SR    | Success Rate                    | 全部                           | 成功 episode / 总 episode |
| SPL   | Success weighted by Path Length | 全部                           | SR × (最短路径 / 实际路径)     |
| NE    | Navigation Error                | AerialVLN / OpenUAV / AirNav | 终点与目标的欧氏距离（米）          |
| OSR   | Oracle Success Rate             | OpenUAV                      | 轨迹上任意点到达目标的比例          |
| TCR   | Task Completion Rate            | HUGE-Bench                   | 多阶段子任务完成比例             |
| CR    | Collision Rate                  | HUGE-Bench / AirSpark        | 碰撞次数 / 总步数             |
| CSPL  | Collision-Safe SPL              | HUGE-Bench                   | 碰撞惩罚加权 SPL             |
| NM-SR | Navigate-then-Manipulate SR     | AIR-VLA / AirSpark           | 导航 + 操作联合成功率           |
| GSR   | Grasp Success Rate              | AIR-VLA / AirSpark           | 抓取成功率                  |
| PCRT  | Post-Contact Recovery Time      | AirSpark                     | 操作后恢复稳定悬停时间（秒）         |

---

## 五、更新日志

| 日期 | 更新内容 |
|---|---|
| 2026-05-22 | 创建文档，汇总 17 个主要基准，完成速查总表、详细介绍、选型建议、指标对照 |
