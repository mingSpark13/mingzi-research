# 城市低空多模态数据采集与任务评测平台

# 城市低空多模态数据采集与任务评测平台
**平台总体架构设计 v0.7**
维护人：花火｜日期：2026-05-21
来源对照：`AirSpark架构文档_v0.6_2026-05-21.md`、`D:\AirSpark` 实际仓库调研（ROADMAP v9.0，2026-05-15）
本版变更：基于实际仓库调研全面更新开发进度（P0/P1/P2 已完成，P3 SceneOps 启动）；更新代码架构快照（12 子模块实际状态与能力边界）；精简技术实现细节，强化顶层架构指引与方法论；更新开发路线图与近期执行清单；保留 v0.6 全部定位、竞品、任务体系、评测指标、架构原则内容。

---

## 一、项目定位与差异化
### 1.1 一句话定位
AirManip-Bench 是一个面向城市低空场景的多模态 Navigate-then-Manipulate benchmark，覆盖语言导航、目标搜索/跟踪、接近对齐、多类接触操作和负载扰动恢复，并提供动力学感知评测、自动化 episode 生成与 Sim2Real 配对验证。

### 1.2 竞品分析

| 竞品 | 核心特点 | 我们的差异 |
|---|---|---|
| OpenFly（ICLR 2026） | 4 引擎统一，100K 轨迹，自动生成 | ❌ 纯导航，无操作；我们不拼 VLN 规模，而是导航后接触操作与动力学评测 |
| OpenUAV（ICLR 2025） | UE4+AirSim，12K 条 6-DoF，三档助手 | ❌ 纯导航/目标搜索，无接触操作；我们补"搜索→接近→操作"闭环 |
| AirNav（arXiv 2601.03707） | 137K 真实城市 UAV VLN，AirVLN-R1（SFT+RFT） | 纯离散导航，无连续控制+操作；我们强调连续控制+接触操作 |
| IndoorUAV（AAAI 2026） | 室内连续 UAV VLN，Habitat，16K+ 轨迹 | 室内纯导航；我们聚焦城市低空+接触操作 |
| AerialVLA（AAAI 2026，在线对话版） | 在线对话导航，UNOD benchmark | 纯导航对话；我们聚焦操作链路 |
| HUGE-Bench | 3DGS 数字孪生，过程导向评测 | 偏高层过程与安全评测；我们偏接触操作和力/力矩 |
| AIR-VLA | 首个空中操作 benchmark，3000 遥操作 demo | 实验室场景，无城市；我们强调城市低空、多类接触、Sim2Real 配对、大规模自动采集 |
| AirVLA（arXiv 2603.25038） | π0 迁移到空中操作，3DGS 合成数据，PAG | 无城市低空、无多类接触、无系统性 Sim2Real 配对 |
| Flying Hand（RSS 2025） | end-effector-centric 全驱六旋翼+4-DoF arm | 无城市场景，无 benchmark，无大规模数据 |
| AERMANI-VLM（arXiv 2511.01472） | VLM reasoning + 离散安全技能库 | 无城市场景，无大规模数据集 |
| CosFly-Track（arXiv 2605.17776） | 城市 UAV 视觉跟踪，12K 轨迹，MuCO | 仅跟踪阶段，无操作；我们覆盖完整链路 |
| UAV-Track VLA（arXiv 2604.02241） | 890K+ 帧，176 任务，π0.5 架构 | 仅跟踪，无接触操作 |
| LiteVLA-H（arXiv 2605.00884） | 256M 参数机载 VLA，Jetson AGX Orin | 仅机载推理方法，无 benchmark |
| DroneVLA | 全链路抓取+交接 | 仅 1-DoF 夹爪，无多类操作 |
| UAV-Flow（NeurIPS 2025） | 细粒度飞行控制 | ❌ 无接触操作 |

### 1.3 核心差异化矩阵

| 维度 | 我们 | AIR-VLA | AirVLA | DroneVLA | OpenFly | HUGE-Bench | CosFly-Track |
|---|---|---|---|---|---|---|---|
| 导航→操作全链路 | ✅ 6 类操作 + 导航衔接 | ✅ 实验室 | ✅ pick-and-place | ✅ 1-DoF | ❌ | ❌ | ❌ 仅跟踪 |
| 接触操作多样性 | ✅ 6 类 | 部分 | 仅抓取 | 仅抓取 | ❌ | ❌ | ❌ |
| 城市实际场景 | ✅ | 实验室 | 室内 | 实验室 | 城市导航 | 数字孪生 | ✅ 城市跟踪 |
| 动力学感知 | ✅ 含负载变化 | 部分 | ✅ PAG | ❌ | ❌ | 仅碰撞 | 部分 |
| Sim2Real 配对 | ✅ | ❌ | 部分 | 无配对 | 3DGS | ❌ | ❌ |
| 力/力矩数据 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 自动化采集 | ✅ 批采集系统 | ❌ | ❌ | ❌ | ✅ 导航 | ❌ | ✅ MuCO |
| Track/Approach 阶段 | ✅ | ❌ | 部分 | 部分 | ❌ | ❌ | ✅ |
| Recovery 数据 | ✅ | ❌ | 部分 | ❌ | ❌ | ❌ | ❌ |

### 1.4 论文卖点（五个核心差异化）
论文标题方向：
**"AirManip-Bench: A Navigate-then-Manipulate Benchmark for Contact-Rich Aerial Tasks in Urban Environments"**

1. **Navigate-then-Manipulate Benchmark**
   城市低空任务不止"飞到目标"，而是覆盖搜索、跟踪、接近、对齐、接触操作、负载后恢复的完整链路（Search→Track→Approach→Align→Contact→Recovery）。

2. **Contact-Rich Aerial Operation Taxonomy**
   提供 6 类以上空中接触操作：抓取/放置、按钮/开关、推/拨/拉、插入/挂载、取样/贴近巡检、交接/运输等。

3. **Dynamics-Aware Evaluation**
   不只评 success rate，还评飞行稳定性、接触力、负载变化、姿态扰动、能耗、控制平滑性、碰撞、可见性、恢复能力。

4. **Hybrid Synthetic–Real Data Flywheel**
   UE 程序化场景 + 真实重建/3DGS-Mesh + 少量遥操作 seed + 自动轨迹优化（参考 CosFly-Track MuCO）+ Sim2Real paired validation。

5. **Modular Infrastructure for Scalable Collection**
   RPC 控制面、独立高带宽数据面、MuJoCo/UE/建图/规划/VLA 模块按需启停，支持 benchmark、baseline、主动采样和后续 world model 训练。

### 1.5 平台服务目标
平台同时服务于以下五类核心能力：
- **数据采集**：批量采集高质量多模态仿真数据（导航+操作）
- **任务生成**：自动生成可复用、可扩展的 episode / benchmark
- **baseline 验证**：统一接入主流与自定义算法进行验证
- **主动采样**：针对 hard cases 与薄弱分布补采数据
- **自主学习**：为后续 agent / world model / active learning 留出闭环接口

---

## 二、平台要解决的三层问题
### 2.1 数据层
- VLN / UAV 导航
- 空中接触操作（6 类）
- 巡检任务
- 搜索与定位
- 后续 VLA / agent 数据积累

### 2.2 算法层
- 主流 VLN baseline（APEX / OnFly / AutoFly / AerialVLA）
- 空中操作 baseline（AIR-VLA 风格）
- 项目自定义策略模型
- 后续主动探索 / 自主采样模型

### 2.3 平台层
- UE5.7 场景资产库
- episode benchmark（导航 + 操作 + 全链路）
- 自动评测
- 数据生成 pipeline
- 遥操作与自动采集闭环

---

## 三、总体架构原则
### 3.1 RPC 是控制面，不是数据面
RPC 保留用途：远程连接与调试、低频控制命令、episode 触发与状态查询、少量标量观测。
RPC 不承担：大规模 RGB/Depth/Seg 流传输、批量 dataset 写入、高频建图/规划/控制闭环主数据面。

高带宽数据的正确路径：
1. **进程内 C++ 直接分发**（ObservationBus）：最快，服务 Collector、MapBuilder、Planner
2. **本地落盘**：训练数据与 benchmark 数据集主路径
3. **共享内存 / ZeroMQ / DDS/ROS2 可选桥接**：用于外部算法在线接入
4. **RPC**：仅保留控制面和调试面

### 3.2 所有重模块必须可选
模块必须可按需启停。基础仿真可单独运行；MuJoCo 可不开启，默认 kinematic 模式仍可用于导航批采；Collector 不开启时不产生额外 IO 压力；Mapping/Planner 不开启时不占用 CPU/GPU。

### 3.3 统一进程设计的正确性（CARLA-Air 教训）
参考 CARLA-Air（arXiv 2603.28032）的经验：bridge-based co-simulation 存在同步开销和时空一致性问题。AirSpark 的 UE+AirSim+MuJoCo 统一进程设计是正确方向：
- 避免跨进程 bridge 的时间戳漂移
- 保证传感器数据与物理状态的时空一致性
- 为高带宽数据面（ObservationBus）提供基础

### 3.4 先 raw+metadata，再标准格式
不要一开始把所有采集都绑死到 HDF5/RLDS/ROS2 bag。推荐：先落 raw frames + episode metadata，Python 离线 Dataset Builder 转 HDF5/LeRobot v3/RLDS；C++ writer 保持轻量稳定。

### 3.5 先规则 baseline，再学习 baseline
建图规划导航先做可解释 baseline（A*/Theta*，DWA/MPC-lite），再接 VLA/RL baseline。可解释 baseline 能验证场景/传感器/评测是否正确，是后续学习方法的可靠对照。

### 3.6 模块化优先于插件化
短期不要为了插件化而过度拆仓。先在 `Source/AirSpark` 内做模块边界，保证迭代速度；模块稳定后再迁出为独立插件。

---

## 四、当前阶段判定（v0.7 更新）
### 4.1 实际开发进度（基于 ROADMAP v9.0，2026-05-15）

| 阶段 | 内容 | 状态 |
|---|---|---|
| P0 主线稳定化 | UE5.7 迁移、AirSim fork、MuJoCo 后端、控制器 v8.0、School 地图 | ✅ 已完成 |
| P1 随机化 VLA 采集闭环 | Schema v2 + FLU 坐标系、CollectorSubsystem 接入 WaypointExecutor、随机化采集循环 | ✅ 已完成（2026-05-13） |
| P2 UE 内部批采集系统 | BatchControllerSubsystem 状态机、MissionDirector、WaypointExecutor、JSONL writer、manifest、图像捕获队列、离线 validator/converter | ✅ 已完成（2026-05-15） |
| P3 SceneOps 平台化 | SceneSpec 版本化、资产版本化、任务 profile 版本化、QA Dashboard、Failure Mining、Regeneration Planner | 🔄 当前阶段 |
| P4 Real2Sim / Sim2Real | 真实重建回流、3DGS-Mesh 配对 episode、Sim2Real 验证 | ⬜ 待 P3 后启动 |
| P5 导航→操作 Benchmark | Navigate-then-Manipulate 完整链路、接触操作任务系统、动力学感知评测 | ⬜ 长期目标 |

### 4.2 P2 已交付能力清单

**批采集系统（已可用）**
- BatchControllerSubsystem：完整状态机（Idle→Configuring→Running→Paused→Completed/Failed）
- MissionDirector：episode 编排，支持 batch spec 驱动
- WaypointExecutor：航点执行，已接入 CollectorSubsystem
- JSONL writer + manifest：episode 数据落盘
- 图像捕获队列：5Hz 传感器捕获，异步 readback
- ObservationBus：进程内 C++ 数据总线（source × modality keys）

**Python 工具链（已可用）**
- `airspark_batch_runner`：thin client，生成 batch spec，触发批采集
- `airspark_dataset_tools`：离线 validator、LeRobot v3 converter、evaluator、randomization dry-run
- 离线验证通过：validate / eval-collection（success_rate=1.0）/ randomization-dry-run

**数据格式（已定稿）**
- Schema v2，FLU 坐标系（米）
- Episode 输出：`manifest.json`、`frames.jsonl`、`actions.jsonl`、`execution_events.jsonl`、`episode.json`、`scene_summary.json`、`_SUCCESS`
- LeRobot v3 兼容：Parquet + MP4(AV1) + meta/info.json + meta/stats.json（q01/q99）

### 4.3 P2 遗留缺口（进入 P3 前需收口）

| 缺口 | 影响 | 优先级 |
|---|---|---|
| `max_retries_per_episode` 只进 schema，BatchController 未消费 | 大批量采集自动恢复能力缺失 | 高 |
| URLab 子模块未初始化（空目录） | UE 主线无法可靠构建，MuJoCo 接触物理不可用 | 高 |
| ObserveSelector 采样通过率约 9% | 批采集效率低，大量 episode 被过滤 | 中 |
| 多 drone 并行未架构闭环 | RuntimeProfile 仍有全局 override 假设 | 中 |
| 导航规划器 occupancy grid 未实现 | 复杂场景路径规划不可用 | 中 |
| 无 CI / 自动化测试 | 回归风险高，协作成本上升 | 中 |
| 文档事实源不一致 | ROADMAP 说已完成，README/docs 仍写 stub | 低（但影响协作） |

---

## 五、当前代码架构快照
### 5.1 主线目录结构
```plaintext
AirSpark/
├── ROADMAP.md                    # 开发路线图（v9.0，当前权威）
├── configs/vehicles/             # MJCF/XML/mesh 资产
├── docs/wiki/                    # 架构文档、模块边界、数据管线
├── PythonClient/                 # RPC 客户端与测试脚本
├── tools/
│   ├── airspark_batch_runner/    # 批采集 thin client
│   ├── airspark_dataset_tools/   # 离线 validator/converter/evaluator
│   └── airspark_packaged_runner/ # 打包版运行器
└── Unreal/airworld/              # UE5.7 主工程
    └── Plugins/
        ├── AirSim/               # 主仿真插件（深度 fork）
        │   └── Source/AirSpark/  # 业务主线（12 子模块）
        └── URLab/                # UE + MuJoCo 子模块（⚠️ 未初始化）
```

### 5.2 AirSpark 12 子模块（当前实际状态）

| 子模块 | 职责 | 当前状态 |
|---|---|---|
| Batch | BatchControllerSubsystem 状态机，批采集编排 | ✅ P2 已完成 |
| Mission | MissionDirector，episode 编排与生命周期 | ✅ P2 已完成 |
| Navigation | WaypointExecutor，航点执行，OccupancyGridPlanner | 🔄 WaypointExecutor 可用，规划器 stub |
| Collection | CollectorSubsystem，数据采集接入 | ✅ P1/P2 已完成 |
| Episode | EpisodeCoordinator，episode 上下文管理 | ✅ P2 已完成 |
| Randomization | 场景/任务随机化，ObserveSelector | 🔄 基础可用，采样通过率待优化 |
| Runtime | AirSparkRuntimeProfile，全局配置与 backend 选择 | 🔄 可用，多 drone 全局 override 待拆 |
| Semantic | 语义标签与场景理解 | 🔄 基础可用 |
| Observation | ObservationBus，进程内数据总线 | ✅ P2 已完成 |
| Diagnostics | 诊断与健康检查 | 🔄 基础可用 |
| SceneDebug | 场景调试可视化 | 🔄 基础可用（~974 行，待拆分） |
| Physics | MuJoCo/Kinematic 后端抽象 | ⚠️ URLab 子模块未初始化 |

### 5.3 数据流向（概念层）
```plaintext
Python RPC（控制面）
    ↓ 低频命令
BatchControllerSubsystem
    ↓ 状态机驱动
MissionDirector → WaypointExecutor
    ↓ 执行 episode
CollectorSubsystem ← ObservationBus（进程内高带宽）
    ↓ 异步写盘
Raw Episode（JSONL + 图像 + manifest）
    ↓ 离线转换
LeRobot v3 / HDF5 / RLDS（训练格式）
```

### 5.4 Python 工具链定位
Python 工具链是**离线处理层**，不是在线数据面：
- `airspark_batch_runner`：生成 batch spec，触发 UE 内部批采集，不拉图像
- `airspark_dataset_tools`：离线 validate、convert、evaluate，不依赖 UE 在线
- 原则：Python 不应成为高带宽数据通路，UE 内部采集是 source of truth

---

## 六、P3 SceneOps 平台化（当前阶段）
### 6.1 P3 核心目标
P3 的本质是把"能采集"升级为"能规模化、可复现、可迭代"。

三个关键能力：
1. **SceneSpec 版本化**：场景、资产、任务 profile 统一结构化描述，支持版本锁定与复现
2. **QA Dashboard**：采集质量可视化，覆盖率分析，失败分布统计
3. **Failure Mining + Regeneration Planner**：从失败 episode 中挖掘薄弱分布，驱动补采

### 6.2 SceneSpec 设计原则
SceneSpec 不是"一句话生成 UE 世界"，而是把外部输入统一转为结构化描述，再生成地图、任务、约束、评估指标。

```plaintext
外部输入（语言/配置/随机种子）
    ↓
SceneSpec（结构化场景描述）
    ├── 场景模板 + 资产版本
    ├── 任务 profile（类型/目标/约束）
    ├── 随机化 profile（天气/光照/目标位置）
    └── 评测 profile（指标/成功条件）
    ↓
UE 程序化生成（PCG + 资产库）
    ↓
Episode 执行 + 采集
```

### 6.3 四层数据飞轮（P3→P4→P5 的数据策略）

**第一层：程序化场景 + 自动标签**
UE5.7 PCG、资产库、语义标签、可达区域、碰撞体、任务点位、操作目标状态。重点是 SceneSpec 驱动的可复现场景生成。

**第二层：优化器生成 expert trajectory**
不只靠脚本随机飞。参考 CosFly-Track 的 MuCO（多约束轨迹优化器）：把 collision、visibility、viewpoint quality、smoothness、kinematic feasibility 一起放进连续 3D 优化。
操作版优化器设计方向：
> Navigation optimizer → Approach optimizer → Pre-contact pose optimizer → Post-contact recovery optimizer

**第三层：少量遥操作 seed → 批量变体生成**
MimicGen / DexMimicGen 思想迁移：少量高质量 demo，通过对象位置、目标姿态、场景布局、初始状态、扰动采样生成大量可用 episode。
- MimicGen：<200 条人工 demo 生成 50K+ demonstrations
- DexMimicGen：60 条 source demos 生成 20K+ 双臂/灵巧操作 demonstrations

**第四层：Real2Sim / 3DGS-Mesh 配对验证**
- UE 程序化场景负责规模化
- 3DGS/真实扫描场景负责真实纹理和 Sim2Real 配对
- MuJoCo/物理后端负责接触动力学

### 6.4 P3 交付目标

| 交付物 | 说明 |
|---|---|
| SceneSpec schema v1 | 场景/资产/任务/随机化/评测的统一结构化描述 |
| 资产版本管理 | 场景资产与 SceneSpec 版本绑定，支持复现 |
| QA Dashboard | 采集质量可视化，覆盖率热图，失败分布 |
| Failure Mining | 从 episode 日志中自动识别失败模式 |
| Regeneration Planner | 基于失败分布驱动补采策略 |
| 3/10/100 episode 验收矩阵 | 端到端可重复的采集→验证→转换流程 |

---

## 七、空中操作任务体系（P5 核心）
### 7.1 完整任务链路
Navigate-then-Manipulate 的完整链路：

> **Task instruction → Search/Locate → Track/Approach → Align/Stabilize → Contact-rich Manipulation → Post-contact Recovery/Transport → Evaluation**

四个关键中间环节：

**Track/Approach**：不只是找到目标，还要在接近过程中保持目标可见、保持合适视角、避免遮挡、控制相对速度。关键指标：目标可见性保持率、视角质量、相对速度控制精度。

**Align/Stabilize**：操作前需要机体-机械臂-末端的对齐。可引入末端中心控制（参考 Flying Hand 的 end-effector-centric 接口）、视觉伺服、MPC、action chunking。

**Contact/Load Transition**：接触瞬间、抓取后负载变化、推拉导致的反作用力。AirVLA 的 Payload-Aware Guidance 已明确把"负载变化导致高度下沉"作为关键问题。

**Recovery**：失败不只是撞不撞、到没到终点，还包括：抓取失败后重试、接触扰动后恢复悬停、目标丢失后重新搜索、负载晃动后稳定运输。几乎所有现有工作都忽略了这个阶段。

### 7.2 六类操作任务分类

| 类型 | 名称 | 接触特性 | 典型场景 | 难度 |
|---|---|---|---|---|
| A | 非接触近距操作 | 无接触力 | 高空裂缝检测、线路外观检查 | 低 |
| B | 瞬时接触操作 | 短暂接触后撤离 | 环境采样、按钮操控 | 中 |
| C | 持续接触操作 | 保持接触并移动 | 墙面清洗、管道涂覆 | 高 |
| D | 抓取放置操作 | 抓取-运输-放置 | 垃圾回收、物资投递 | 高 |
| E | 推拉操作 | 施力改变物体状态 | 障碍清除、阀门操作 | 高 |
| F | 工具使用操作 | 持工具精确操作 | 无损检测、表面修补 | 极高 |

### 7.3 城市实际应用场景矩阵

| 应用场景 | 操作类型 | 典型指令 |
|---|---|---|
| 城市垃圾清理 | D 抓取放置 | "捡起那个塑料袋放到垃圾桶" |
| 高空墙面清洗 | C 持续接触 | "清洁这面墙上的涂鸦" |
| 管道外壁检测 | B/F 瞬时/工具 | "检查这段管道的腐蚀程度" |
| 建筑裂缝检测 | A 近距观察 | "拍摄这面墙的裂缝细节" |
| 应急物资投递 | D 抓取放置 | "把这个急救包送到楼顶" |
| 障碍物清除 | E 推拉 | "把挡住通道的树枝推开" |
| 设备远程操控 | B 瞬时接触 | "按下那个紧急停止按钮" |

### 7.4 P5 数据采集目标量

| 操作类型 | 最小 episode 数 | 采集方式 |
|---|---|---|
| A 近距检查 | 500 | 全自动脚本 |
| B 瞬时接触 | 300 | 脚本 + 遥操作补采 |
| C 持续接触 | 200 | 遥操作为主 |
| D 抓取放置 | 500 | 脚本 + 遥操作 |
| E 推拉 | 200 | 遥操作为主 |
| F 工具使用 | 100 | 遥操作 |

---

## 八、数据格式与 VLA 训练接口
### 8.1 三层数据格式
- **Raw logs**：传感器原始流（RGB/depth/segmentation/pose/IMU/force/torque/contact/event），source of truth
- **Episode format**：HDF5/Zarr 本地高吞吐训练格式
- **Release format**：LeRobot v3 / RLDS-compatible（支持直接训 ACT、Diffusion Policy、OpenVLA-OFT、π0/π0.5）

### 8.2 标准 episode 字段

```text
observation:
  rgb_front / rgb_down / depth / segmentation
  drone_state: pose, velocity, angular velocity
  arm_state: q, dq, ee_pose（P5 操作阶段）
  force_torque / contact_state（P5 操作阶段）
  map_context / semantic_target

action:
  low_level_cmd / waypoint / ee_delta_pose / gripper_cmd
  action_chunk（VLA 训练用）

language:
  high_level_instruction
  subtask_instruction
  atomic_skill_label

metadata:
  scene_id / task_id / object_id
  weather / light / domain_randomization
  sim_or_real / paired_real_episode_id
  success / failure_reason
```

### 8.3 VLA 训练接口（P3 后期 / P4）
- 观测映射：`observation.state`（12 维）、`action`（4 维速度控制）、`observation.images.front/bottom`（256×256）
- π0.5 要求：q01/q99 stats，max_state_dim=32，max_action_dim=32
- Policy Server：gRPC/ZMQ，UE PolicyClient 接入，支持闭环评测
- 训练数据格式：LeRobot v3 Parquet + MP4(AV1) + meta/info.json + meta/stats.json

---

## 九、评测指标体系
### 9.1 导航指标
基础：Success Rate / SPL / Goal Error / Collision Rate / Timeout Rate

动力学感知（差异化）：
- **Energy Efficiency（EE）**：实际能量 / 理论最短路径能量
- **Dynamic Feasibility Rate（DFR）**：轨迹物理可执行比例
- **Trajectory Smoothness（TS）**：加速度变化率（jerk）均值

Sim2Real 对齐（差异化）：
- **Sim-Real Trajectory Divergence（SRTD）**：DTW 距离
- **Sim-Real Success Gap（SRSG）**：成功率差异

### 9.2 过程导向指标（对标 HUGE-Bench）
- **TCR（Task Completion Rate）**：多阶段子任务完成比例
- **CR（Collision Rate）**：碰撞次数/总步数
- **CSPL（Collision-Safe SPL）**

### 9.3 操作指标（P5 差异化核心）
导航→操作全链路：
- **NM-SR（Navigate-then-Manipulate SR）**：联合成功率
- **NM-SPL**：路径加权联合成功率

操作专用：
- **GSR（Grasp Success Rate）**：抓取成功率（D 类）
- **CS（Contact Stability）**：接触力稳定性标准差（B/C/F 类）
- **FA（Force Accuracy）**：力偏差（B/C/E/F 类）
- **OPA（Object Placement Accuracy）**：放置精度（D 类）
- **PCRT（Post-Contact Recovery Time）**：操作后恢复稳定悬停时间

安全：
- **MCR（Manipulation Collision Rate）**
- **FOR（Force Overload Rate）**
- **PMS（Post-Manipulation Stability）**：负载变化后飞行稳定性

---

## 十、开发路线图（P3→P4→P5）
### P3：SceneOps 平台化（当前，预计 4–6 周）
目标：从"能采集"升级为"能规模化、可复现、可迭代"。

核心交付：
- SceneSpec schema v1：场景/资产/任务/随机化/评测统一结构化描述
- 资产版本管理：SceneSpec 与资产版本绑定，支持复现
- QA Dashboard：采集质量可视化，覆盖率分析，失败分布
- Failure Mining：从 episode 日志自动识别失败模式
- Regeneration Planner：基于失败分布驱动补采策略
- 3/10/100 episode 端到端验收矩阵（含真实图像 payload）

P3 前置收口（优先级高）：
- 实现 `max_retries_per_episode`，BatchController 消费 schema 字段
- 初始化/锁定 URLab 子模块，修复 MuJoCo 构建路径
- 优化 ObserveSelector 采样通过率（当前约 9%）
- 清理文档事实源（以 ROADMAP.md 为准，删除旧 stub 描述）

### P4：Real2Sim / Sim2Real 配对（预计 P3 完成后启动）
目标：建立仿真与真实数据的配对验证能力，量化 sim2real gap。

核心交付：
- 真实场景 3DGS/NeRF 重建回流到 UE
- Sim2Real paired episode：同一任务在仿真与真实中各跑一遍
- SRTD / SRSG / SRPG 三个 sim2real 指标基线
- 真实数据采集协议（传感器标定、时间戳对齐、坐标系统一）

### P5：Navigate-then-Manipulate Benchmark（长期目标）
目标：形成可对外发布的城市低空导航→操作 benchmark。

核心交付：
- URLab Contact Bridge 完整接入（MuJoCo 接触物理）
- 6 类操作任务系统（A-F 类，含 reset/success/failure 判定）
- Navigate-then-Manipulate episode runtime
- 操作 Evaluator（GSR/CS/FA/OPA/PCRT/PMS）
- 遥操作 seed 采集 + MimicGen 风格批量变体生成
- Benchmark package + Baseline Runner + 论文级实验

---

## 十一、近期执行清单（P3 启动）
### 本周必须收口（P2 遗留）
- [ ] 实现 `max_retries_per_episode`，BatchController 消费该字段
- [ ] 初始化 URLab 子模块（`git submodule update --init URLab`），验证 MuJoCo 构建
- [ ] 跑一次 `scripts/airspark_ue.ps1 -Build` + 最小 School batch smoke
- [ ] 清理文档：以 ROADMAP.md 为准，删除 README/docs 中的 stub/placeholder 描述

### P3 第一轮（SceneSpec 基础）
- [ ] 起草 SceneSpec schema v1（YAML/JSON，含场景/资产/任务/随机化/评测字段）
- [ ] 资产版本注册表（场景资产与 SceneSpec 版本绑定）
- [ ] 端到端验收矩阵：3 episode → 10 episode → 100 episode（含真实图像 payload）
- [ ] validator strict 模式：rgb/depth/seg 不再标记为 deferred

### P3 第二轮（QA 与迭代）
- [ ] QA Dashboard 原型（采集质量可视化，覆盖率热图）
- [ ] Failure Mining：从 execution_events.jsonl 自动分类失败原因
- [ ] Regeneration Planner：基于失败分布生成补采 batch spec
- [ ] ObserveSelector 采样通过率优化（目标 >50%）

### P3 第三轮（导航规划补齐）
- [ ] 实现 OccupancyGridPlanner（A* 或 Theta*，3D clearance）
- [ ] 路径平滑与 sweep validation
- [ ] 导航 Evaluator：SR/SPL/Goal Error/Collision/Trajectory Smoothness

---

## 十二、关键技术决策
### 12.1 RPC 不是数据面
决策：RPC 保留为控制面，不作为高带宽采集/建图/规划主通路。
理由：带宽不足；Python 拉图/点云会影响仿真帧率；数据采集和建图应复用同一帧数据，避免重复拷贝。

### 12.2 MuJoCo 是可选后端
建议默认：
- 纯导航批采：kinematic backend（轻量，URLab 不需要初始化）
- 接触/操作/动力学评测：MuJoCo backend
- 高保真验证集：MuJoCo backend

### 12.3 SceneSpec 是 P3 的核心抽象
SceneSpec 不是"一句话生成 UE 世界"，而是把外部输入统一转为结构化描述，再生成地图、任务、约束、评估指标。这是从"手工摆场景"到"可复现规模化采集"的关键跨越。

### 12.4 数据飞轮的正确顺序
不要跳步：先程序化场景（P3）→ 再 Sim2Real 配对（P4）→ 再操作任务（P5）。每一层都依赖上一层的基础设施。

### 12.5 模块边界是长期健康的保障
当前 WaypointExecutorComponent（~1651 行）、SceneDebugSubsystem（~974 行）已偏大。继续堆功能会让线程生命周期、采集状态、飞控命令和 QA 日志互相缠绕。P3 期间应按 Module-Boundaries.md 的要求，避免 MissionDirector、BatchController、Collector 继续膨胀。

---

## 十三、风险与注意事项

| 风险 | 表现 | 对策 |
|---|---|---|
| URLab 子模块未初始化 | UE 主线无法可靠构建，MuJoCo 不可用 | P3 前置收口，优先初始化并锁定版本 |
| 文档事实源不一致 | 团队被旧 stub 文档误导 | 以 ROADMAP.md 为准，清理旧描述 |
| max_retries 未消费 | 大批量采集自动恢复能力缺失 | P3 前置收口，BatchController 消费该字段 |
| ObserveSelector 通过率低 | 批采集效率低，大量 episode 被过滤 | P3 第二轮优化采样策略 |
| 模块继续膨胀 | 线程/状态/日志互相缠绕 | 严格遵守 Module-Boundaries.md |
| 规划器 stub | 复杂场景路径规划不可用 | P3 第三轮实现 OccupancyGridPlanner |
| 无 CI | 回归风险高 | P3 期间建立基础 pytest + smoke test |
| 多 drone 全局 override | 后续并行采集会踩到边界 | P5 前拆 per-vehicle context |
| 跳过 Sim2Real 直接做 benchmark | sim2real gap 无法量化 | P4 先建配对验证能力 |

---

## 十四、对外定位
> AirSpark 是一个面向城市低空无人机导航与空中操作的 UE5.7 + AirSim + MuJoCo 仿真与 benchmark 平台。平台已完成仿真内核（P0）、随机化 VLA 采集闭环（P1）和 UE 内部批采集系统（P2），当前进入 SceneOps 平台化阶段（P3），目标是建立可复现、可规模化、可迭代的场景-任务-采集-评测闭环，为后续 Navigate-then-Manipulate Benchmark（P5）奠定基础。

核心差异化：
1. 城市低空导航 → 空中操作全链路（Search→Track→Approach→Align→Contact→Recovery）
2. 可选 MuJoCo 接触物理与机械臂/夹爪
3. 动力学感知评测（含负载变化、接触力、恢复能力）
4. 程序化场景与任务生成（四层数据飞轮）
5. 高带宽内部采集管线（ObservationBus），不依赖 RPC 拉数据
6. Sim2Real paired episode 预留（P4）

---

## 十五、总结
AirSpark 已经完成了从"飞行仿真 demo"到"VLA 数据工厂雏形"的演进。P0/P1/P2 三个阶段交付了可用的仿真内核、随机化采集闭环和批采集系统，方向是清楚的。

当前最大问题不是缺想法，而是：
1. **复现基线**：URLab 子模块未初始化，UE 主线无法可靠构建
2. **文档一致性**：ROADMAP 与 README/docs 事实源不一致
3. **批采集鲁棒性**：max_retries 未消费，ObserveSelector 通过率低
4. **规划器真实能力**：OccupancyGridPlanner 仍是 stub

P3 的核心任务是收口这些问题，同时建立 SceneSpec 平台化能力，为 P4 Sim2Real 和 P5 操作 Benchmark 打好基础。

**优先级排序：**
1. 修复复现基线（URLab + max_retries + 文档清理）
2. SceneSpec 平台化（P3 主线）
3. 导航规划器补齐（OccupancyGridPlanner）
4. Sim2Real 配对验证（P4）
5. 操作任务系统（P5，依赖 URLab Contact Bridge）
6. Benchmark 产品化与论文

---

**v0.7 完整变更（2026-05-21）**：基于 D:\AirSpark 实际仓库调研（ROADMAP v9.0，2026-05-15），全面更新开发进度（P0/P1/P2 已完成，P3 SceneOps 启动）；更新代码架构快照（12 子模块实际状态）；精简技术实现细节，强化顶层架构指引；将 Phase A-G 路线图替换为 P3/P4/P5 实际路线图；更新近期执行清单（P3 任务）；新增 P2 遗留缺口表；保留 v0.6 全部定位、竞品矩阵、任务体系、评测指标、架构原则内容。

