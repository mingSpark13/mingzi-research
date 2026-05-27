# 城市低空多模态数据采集与任务评测平台

# 城市低空多模态数据采集与任务评测平台
**平台总体架构设计 v0.6**
维护人：花火｜日期：2026-05-21
来源对照：`AirSpark架构文档_v0.5_2026-04-24.md`、`2026-05-21_AirManipBench_竞品调研与定位修正.md`
本版变更：基于 123.md 竞品更新与调研，全面升级项目定位、竞品矩阵、任务链路、数据飞轮、数据格式；新增 LiteVLA-H/AirVLA/Flying Hand/CosFly-Track 等 2026 年新工作；新增 4.5 架构原则（CARLA-Air 教训）；保留 v0.5 全部架构设计内容。
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
| CARLA-Air | 空地统一仿真 | 我们聚焦操作而非空地协同 |
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
| 自动化采集 | ✅ 6 类脚本 | ❌ | ❌ | ❌ | ✅ 导航 | ❌ | ✅ MuCO |
| Track/Approach 阶段 | ✅ | ❌ | 部分 | 部分 | ❌ | ❌ | ✅ |
| Recovery 数据 | ✅ | ❌ | 部分 | ❌ | ❌ | ❌ | ❌ |

### 1.4 论文卖点（v0.6 升级版）
论文标题方向：
**"AirManip-Bench: A Navigate-then-Manipulate Benchmark for Contact-Rich Aerial Tasks in Urban Environments"**

五个核心卖点：

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

## 三、Phase 1 边界（核心约束）
Phase 1 只做这些，禁止超范围。
### 3.1 场景约束
- 只做 1 个小城市场景（优先园区/校园模板），固定布局，不变体
### 3.2 载具约束
- 只做 1 个 UAV（不含机械臂，Phase 2 再接入）
- 不做 UGV，不做多智能体
### 3.3 传感器约束
Phase 1 实际做：
- 相机（RGB）+ 深度（Depth）+ 分割（Seg）+ 位姿（Pose）
- IMU / GPS 数据记录
- 统一时间戳协议（UE SimTime）
- 统一坐标系（ENU + UAV Body Frame）
- ROS2 topic 或 HDF5 回放
Phase 2 扩展：激光雷达、力/力矩传感器、末端执行器状态
### 3.4 任务约束
- 只做 PointNav + 简单 VLN
- 不做操作任务（Phase 2）、不做巡检（Phase 3）、不做空地协同（Phase 4）
### 3.5 评测约束
- 只做验证型 baseline（sanity check）
- 不追求指标数字漂亮，只验证平台接口通顺
### 3.6 Sim2Real 约束
- Month 3 新增：用龙虾真实数据跑 3-5 个 sim2real 对比 episode
- 记录 SRTD / SRSG 两个指标，验证基本可行性
---

## 四、总体架构原则
### 4.1 RPC 的定位
RPC 不应作为高带宽数据基础设施。
RPC 保留用途：
- 远程连接与调试
- 低频控制命令
- 实验脚本触发 episode 开始/停止
- 查询状态、切换模式、加载配置
- 少量标量观测或单帧调试图像
RPC 不承担：
- 大规模 RGB/Depth/Seg/LiDAR 流传输
- 批量 dataset 写入
- 高频建图输入
- 高频规划/控制闭环主数据面
### 4.2 数据面应在仿真内部构建
建议主数据面为：
```plaintext
UE/AirSim/MuJoCo Runtime
     ↓
SensorHub / StateHub
     ↓
ObservationBus（进程内 C++ 数据总线）
     ↓
Collectors / MapBuilder / Planner / Monitor / Optional IPC
     ↓
DatasetWriter / Evaluator / Visualizer
```

高带宽数据的首选路径：
1. **进程内 C++ 直接分发**：最快，服务 Collector、MapBuilder、Planner
2. **本地落盘**：训练数据与 benchmark 数据集主路径
3. **共享内存 / ZeroMQ / DDS/ROS2 可选桥接**：用于外部算法在线接入
4. **RPC**：仅保留控制面和调试面
### 4.3 所有重模块必须可选
模块必须可按需启停：
```json
{
  "AirSpark": {
    "EnableMuJoCo": false,
    "EnableSceneBuilder": true,
    "EnableTaskRuntime": true,
    "EnableCollector": false,
    "EnableMapping": false,
    "EnablePlanner": false,
    "EnableMonitor": true,
    "EnableRpc": true
  }
}
```

要求：
- 基础仿真可单独运行
- MuJoCo 可不开启，默认 kinematic/轻量模式仍可用于导航批采
- Collector 不开启时不产生额外 IO 压力
- Mapping/Planner 不开启时不占用 CPU/GPU
- Monitor/RPC 均可独立关闭
### 4.4 插件化优先级
短期不要为了插件化而过度拆仓。建议分两步：
1. **先在 **`**Source/zero_sim_up**`** 内做模块边界**，保证迭代速度
2. 模块稳定后迁出为插件，例如：
  - `AirSparkRuntime`
  - `AirSparkDataset`
  - `AirSparkMapping`
  - `AirSparkBenchmark`
### 4.5 统一进程设计的正确性（CARLA-Air 教训）
参考 CARLA-Air（arXiv 2603.28032）的经验：bridge-based co-simulation 存在同步开销和时空一致性问题。CARLA-Air 正是为了解决这个问题，将 CARLA 与 AirSim 放进同一个 UE 进程，共享 physics tick 和 rendering pipeline。

AirSpark 的 UE+AirSim+MuJoCo 统一进程设计是正确方向：
- 避免跨进程 bridge 的时间戳漂移
- 避免多进程同步开销影响仿真帧率
- 保证传感器数据与物理状态的时空一致性
- 为高带宽数据面（ObservationBus）提供基础
---

## 五、当前阶段判定
### 5.1 v0.4 原阶段与真实进度对照

| v0.4 阶段 | 原定义 | 当前真实状态 | 结论 |
|---|---|---|---|
| Phase 0 | 文档冻结 + Schema 定稿 | 已有多份设计文档，但代码推进已超过文档 | ✅ 已越过，需重新冻结 v0.5 |
| Phase 1 | MVP 导航闭环 | 仿真、传感器、控制、MuJoCo 已部分超出导航 MVP | 🔄 Phase 1 核心底座基本完成，缺程序化数据闭环 |
| Phase 2 | 空中操作 benchmark | MuJoCo/机械臂/夹爪资产已提前进入代码 | 🔄 物理基础提前完成，操作任务系统未完成 |
| Phase 3 | 巡检与接触观测 | 接触物理底座具备，任务和场景未做 | ⬜ 待 Phase 2 之后扩展 |
| Phase 4 | 空地协同 + 交互式学习 | 尚未开始 | ⬜ 暂缓 |

### 5.2 当前阶段命名
建议将当前阶段命名为：
> **Phase 1.5 — Infrastructure Pivot：从仿真内核转向程序化数据与自治基础设施。**
本阶段目标：
- 不再把 Python RPC 当作数据基础设施主通路
- 将 UE/AirSim/MuJoCo 内部能力收敛为可开关模块
- 先建立程序化场景、任务、采集、建图/规划/导航基础设施，再推进大规模 benchmark
---

## 六、当前代码架构快照
### 6.1 主线目录
```plaintext
AirSpark/
├── README.md
├── ROADMAP.md
├── configs/vehicles/       # MJCF/XML/mesh 资产
├── docs/                    # 控制、物理、Monitor、URLab 文档
├── PythonClient/            # RPC 客户端与测试脚本
└── Unreal/airworld/         # UE5.7 主工程
    ├── Source/zero_sim_up/  # 项目自有 C++ 模块
    └── Plugins/
        ├── AirSim/         # 主仿真插件与 AirLib
        └── URLab/          # UE + MuJoCo 子模块
```

### 6.2 AirSim 插件当前分层
```plaintext
Plugins/AirSim/Source/
├── AirLib/
│   ├── include/physics/
│   │   ├── IZeroPhysicsBackend.hpp
│   │   ├── KinematicBackend.hpp
│   │   └── MuJoCoBackend.hpp
│   └── include/vehicles/multirotor/firmwares/simple_flight/
│       ├── SimpleFlightApi.hpp
│       └── firmware/
│           ├── CommandManager.hpp
│           ├── MuJoCoController.hpp
│           ├── PidController.hpp
│           └── interfaces/
├── Camera/
├── Core/
├── Monitor/
├── Recording/
├── Sensors/Vision/
├── SimMode/
├── UnrealSensors/
├── Vehicles/Multirotor/
│   ├── MjFlyingPawn.*
│   ├── MultirotorPawnSimApi.*
│   ├── SimModeWorldMultiRotor.*
│   └── ZeroMuJoCoBridge.*
└── World/
```

### 6.3 已完成底座

| 能力 | 当前状态 | 代码/文档位置 |
|---|---|---|
| UE5.7 主工程 | 已稳定迁移 | `Unreal/airworld` |
| RPC 控制入口 | 可用 | `PythonClient/airsim`、AirLib RPC |
| 多模式控制器 | v8.0 已完成 | `docs/control_architecture.md` |
| PID 热重载 | 已完成 | `reloadCtrlParams()`、`ctrl_params.json` |
| 双物理后端 | 已完成核心抽象 | `IZeroPhysicsBackend.hpp` |
| Kinematic 后端 | 可用 | `KinematicBackend.hpp` |
| MuJoCo 后端 | 已接入 | `MuJoCoBackend.hpp`、`ZeroMuJoCoBridge.*` |
| MuJoCo 可选启动 | 已有基础 | `PhysicsEngineName=MuJoCoBackend` |
| AMjFlyingPawn | 已有 | `MjFlyingPawn.*` |
| 传感器基础 | 已有 | Camera、LiDAR、Detection、Seg 等 |
| Monitor | 已有 | `MonitorServer.*`、`monitor.html` |
| 人物行为/模型切换 | 已有 | `Source/zero_sim_up` |
| 统一 Recorder 雏形 | 已有 | `Recording/UnifiedRecorderManager.*` |

### 6.4 仍缺的关键基础设施

| 缺口 | 为什么重要 | 建议落点 |
|---|---|---|
| Scene Builder | 批量生成场景、对象、语义标签 | `Source/zero_sim_up/SceneBuilder` 或新插件 |
| Episode Runtime | 任务加载、成功条件、重置、seed 管理 | `TaskRuntime` |
| Observation/DataBus | 高带宽数据不能走 RPC | UE 内部 C++ bus + ring buffer |
| SensorHub | 统一注册/启停/同步传感器 | `SimRuntime/SensorHub` |
| Collector | 程序化采集与批处理 | `Collector` |
| Dataset Writer | HDF5/Zarr/Arrow/图片+metadata 输出 | `DatasetBuilder` |
| MapBuilder | 从 Depth/LiDAR/Pose 建图 | `Mapping` |
| Planner/Nav Stack | 路径规划、局部避障、导航执行 | `Navigation` |
| Evaluator | SR/SPL/轨迹误差/碰撞/动力学指标 | `Evaluator` |
| Visualizer | 回放、失败归因、力曲线 | `Visualizer` |
| Module Manager | 所有能力按需启停 | `Core/RuntimeModuleManager` |

---

## 七、v0.5 目标模块设计
### 7.1 Core：配置、Schema、时间与坐标
职责：
- 加载全局配置
- 定义 Observation/Action/Episode Schema
- 管理 seed、episode id、run id
- 统一 FLU/NED/UE/MuJoCo 坐标转换
- 提供 RuntimeModule 生命周期接口
建议接口：
```cpp
class IAirSparkRuntimeModule
{
public:
  virtual void Initialize(const FAirSparkRuntimeContext& Context) = 0;
  virtual void StartEpisode(const FAirSparkEpisode& Episode) = 0;
  virtual void Tick(float DeltaSeconds) = 0;
  virtual void EndEpisode() = 0;
  virtual void Shutdown() = 0;
};
```

### 7.2 Sim Runtime：仿真运行时编排
职责：
- 选择物理后端：kinematic / MuJoCo
- 初始化车辆、人物、动态体、天气、时间
- 管理仿真 pause/play/reset
- 暴露统一状态源：pose、velocity、IMU、collision、contact
注意：Sim Runtime 不负责 dataset 格式，也不直接跑 baseline。
### 7.3 SensorHub：传感器统一注册与同步
职责：
- 注册 Camera、Depth、Seg、LiDAR、IMU、GPS、Detection、未来力/力矩传感器
- 统一 timestamp、frame id、坐标系
- 支持不同 sensor profile
- 支持按 episode 启停传感器
输出 ObservationFrame：
```plaintext
ObservationFrame
├── sim_time
├── frame_index
├── vehicle_state
├── camera_frames[]
├── lidar_frames[]
├── imu
├── gps
├── detection
└── contact/force_torque（Phase 2）
```

### 7.4 ObservationBus：高带宽数据总线
职责：
- 进程内发布/订阅
- 支持 ring buffer，避免阻塞仿真主线程
- 为 Collector、MapBuilder、Planner、Monitor 提供同一份数据
- 支持不同 QoS：latest-only、record-all、downsample
原则：
- 图像和点云不通过 RPC 作为主通道
- 不在 GameThread 做重 IO
- 高带宽数据采用异步 writer
### 7.5 Scene Builder：程序化场景系统
职责：
- 场景模板管理
- 语义对象注册
- 程序化放置目标、障碍物、动态体
- 天气、光照、风、时间随机化
- 输出 scene instance config
阶段目标：
1. 先做小型城市场景的 spawn/clear/reset
2. 再做道路、建筑、目标点、禁飞区、动态障碍
3. 最后做桥梁、电塔、管道、墙面等巡检/操作场景
### 7.6 Task Runtime / Episode Runtime
职责：
- 加载 episode
- 初始化 scene、vehicle、sensor、physics backend
- 执行 reset/start/stop
- 判断 success/failure/timeout/collision
- 记录 episode metadata
Episode 应包含：
```yaml
episode_id: nav_city_000001
seed: 12345
scene:
  template: city_block_small
  randomization_profile: train_light
physics:
  backend: kinematic  # kinematic | mujoco
sensors:
  profile: nav_rgbd_lidar
vehicle:
  profile: airspark_quad_gripper
task:
  type: point_nav  # point_nav | vln | inspect | manipulate | ntm
  start_pose: ...
  goal: ...
evaluation:
  metrics: [sr, spl, collision_rate, energy]
collector:
  enabled: true
  writer: local_dataset
```

### 7.7 Collector / Dataset Writer
职责：
- 接收 ObservationBus 数据
- 记录 action/state/observation/event
- 支持多 writer
- 支持 episode 完成后的质量检查
建议 writer 分层：
```plaintext
Collector
├── RawFrameWriter      # 图片/点云/状态原始输出
├── MetadataWriter      # episode.json/jsonl/parquet
├── Hdf5Writer          # 主训练格式，可后置转换
├── RldsExporter        # Phase 2
└── RosbagExporter     # Phase 2/Sim2Real 对齐
```

三层数据格式（v0.6 新增）：
- **Raw logs**：传感器原始流（RGB/depth/segmentation/pose/IMU/force/torque/contact/event）
- **Episode format**：HDF5/Zarr 本地高吞吐训练格式
- **Release format**：LeRobot v3 / RLDS-compatible metadata（支持直接训 ACT、Diffusion Policy、OpenVLA-OFT、π0/π0.5）

每个 episode 的标准字段：
```text
observation:
  rgb_front / rgb_down / depth / segmentation
  drone_state: pose, velocity, angular velocity
  arm_state: q, dq, ee_pose
  force_torque / contact_state
  map_context / semantic_target

action:
  low_level_cmd
  waypoint / ee_delta_pose / gripper_cmd
  action_chunk

language:
  high_level_instruction
  subtask_instruction
  atomic_skill_label

metadata:
  scene_id
  task_id
  object_id
  weather/light/domain_randomization
  sim_or_real
  paired_real_episode_id
  success/failure_reason
```

短期可采用：
- 图像：PNG/JPEG/EXR 或 raw binary
- 点云：PLY/NPY/二进制 float buffer
- 状态：JSONL/Parquet
- Episode metadata：JSON/YAML
不要一开始被 HDF5 C++ 依赖拖住；可先落 raw + metadata，再由 Python Dataset Builder 离线转换。
### 7.8 Mapping：建图基础设施
职责：
- 从 Depth/LiDAR/Pose 构建局部/全局地图
- 支持 occupancy grid、height map、ESDF/TSDF 后续扩展
- 提供给 Planner 与 Visualizer
阶段目标：
1. 2.5D occupancy grid：用于低空导航
2. 3D voxel / TSDF：用于复杂避障与巡检
3. Semantic map：结合 Seg/Detection
4. Dynamic obstacle layer：行人/车辆动态体
### 7.9 Navigation / Planner
职责：
- 全局路径规划
- 局部避障
- 轨迹跟踪
- 与控制器解耦
短期推荐栈：
- Global：A* / Theta* / RRT*
- Local：DWA / MPC-lite / potential field fallback
- Controller interface：输出 waypoint / velocity / position target，交给现有控制器
不要一开始做大型学习式导航；先建立可解释、可评测的 rule-based baseline。
### 7.10 Manipulation / Contact Task Runtime
职责：
- 机械臂/夹爪任务定义
- 接触事件、力/力矩、抓取状态采集
- 操作成功条件判断
与 MuJoCo 的关系：
- 操作/接触任务默认需要 MuJoCo
- 纯导航任务默认不需要 MuJoCo
- Navigate-then-Manipulate episode 前半段可 kinematic，操作段切 MuJoCo；若切换成本高，则整条 episode 使用 MuJoCo
---

## 八、空中操作任务体系（Phase 2 核心）
### 8.0 完整任务链路（v0.6 新增）
Navigate-then-Manipulate 的完整链路：

> **Task instruction → Search/Locate → Track/Approach → Align/Stabilize → Contact-rich Manipulation → Post-contact Recovery/Transport → Evaluation**

四个关键中间环节说明：

**Track/Approach**
不只是找到目标，还要在接近过程中保持目标可见、保持合适视角、避免遮挡、控制相对速度。CosFly-Track 和 UAV-Track VLA 都说明这个方向正在升温。关键指标：目标可见性保持率、视角质量、相对速度控制精度。

**Align/Stabilize**
操作前需要机体-机械臂-末端的对齐，尤其是夹取、按钮、插入、拨动、开合这类任务。可引入末端中心控制（参考 Flying Hand 的 end-effector-centric 接口）、视觉伺服、MPC、action chunking。

**Contact/Load Transition**
接触瞬间、抓取后负载变化、推拉导致的反作用力，是比 VLN benchmark 更有价值的地方。AirVLA 的 Payload-Aware Guidance 已经明确把"负载变化导致高度下沉"作为关键问题，并通过在 flow-matching sampling 中注入负载约束来解决。

**Recovery**
失败不是只有撞不撞、到没到终点，还包括：抓取失败后重试、接触扰动后恢复悬停、目标丢失后重新搜索、负载晃动后稳定运输。这是 benchmark 很有辨识度的部分，几乎所有现有工作都忽略了这个阶段。

### 8.1 六类操作任务分类

| 类型 | 名称 | 接触特性 | 典型场景 | 难度 |
|---|---|---|---|---|
| A | 非接触近距操作 | 无接触力 | 高空裂缝检测、线路外观检查 | 低 |
| B | 瞬时接触操作 | 短暂接触后撤离 | 环境采样、按钮操控 | 中 |
| C | 持续接触操作 | 保持接触并移动 | 墙面清洗、管道涂覆、垃圾清理 | 高 |
| D | 抓取放置操作 | 抓取-运输-放置 | 垃圾回收、物资投递 | 高 |
| E | 推拉操作 | 施力改变物体状态 | 障碍清除、阀门操作 | 高 |
| F | 工具使用操作 | 持工具精确操作 | 无损检测、表面修补 | 极高 |

### 8.2 城市实际应用场景矩阵

| 应用场景 | 操作类型 | 目标物 | 典型指令 |
|---|---|---|---|
| 城市垃圾清理 | D 抓取放置 | 地面/屋顶垃圾 | "捡起那个塑料袋放到垃圾桶" |
| 高空墙面清洗 | C 持续接触 | 建筑外立面 | "清洁这面墙上的涂鸦" |
| 管道外壁检测 | B/F 瞬时/工具 | 暴露管道 | "检查这段管道的腐蚀程度" |
| 高空线路巡检 | A/F 近距/工具 | 电力线路 | "检测这段电缆的绝缘层厚度" |
| 建筑裂缝检测 | A 近距观察 | 墙面/桥墩 | "拍摄这面墙的裂缝细节" |
| 应急物资投递 | D 抓取放置 | 物资包裹 | "把这个急救包送到楼顶" |
| 障碍物清除 | E 推拉 | 遮挡物 | "把挡住通道的树枝推开" |
| 环境采样 | B 瞬时接触 | 空气/水/表面 | "在那个烟囱口采集空气样本" |
| 设备远程操控 | B 瞬时接触 | 开关/按钮 | "按下那个紧急停止按钮" |
| 表面修补 | C/F 持续/工具 | 裂缝/锈蚀 | "修补这段管道上的锈蚀点" |

### 8.3 数据采集范式：四层数据飞轮（v0.6 升级）
原"自动化数据采集 Pipeline"升级为四层数据飞轮：

**第一层：程序化场景 + 自动标签**
对应 OpenFly / AirNavigation / UEMM-Air 方向。重点保留 UE5.7 PCG、资产库、语义标签、可达区域、碰撞体、任务点位、操作目标状态。

**第二层：优化器生成 expert trajectory**
不只靠脚本随机飞。参考 CosFly-Track 的 MuCO（多约束轨迹优化器）：把 collision、visibility、viewpoint quality、smoothness、kinematic feasibility 一起放进连续 3D 优化。
可设计操作版优化器：
> Navigation optimizer + approach optimizer + manipulation pre-contact pose optimizer + post-contact recovery optimizer

**第三层：少量遥操作 seed → 批量变体生成**
MimicGen / DexMimicGen 思想迁移：少量高质量 demo，通过对象位置、目标姿态、场景布局、初始状态、扰动采样生成大量可用 episode。
- MimicGen：<200 条人工 demo 生成 50K+ demonstrations
- DexMimicGen：60 条 source demos 生成 20K+ 双臂/灵巧操作 demonstrations

**第四层：Real2Sim / 3DGS-Mesh 配对验证**
HUGE-Bench、AirVLA、UAVTwin 都说明 3DGS/3DGS-Mesh 已从"好看"变成 benchmark 与数据增强的一部分。
- UE 程序化场景负责规模化
- 3DGS/真实扫描场景负责真实纹理和 Sim2Real 配对
- MuJoCo/物理后端负责接触动力学

Phase 2 采集目标量：

| 操作类型 | 最小 episode 数 | 采集方式 |
|---|---|---|
| A 近距检查 | 500 | 全自动脚本 |
| B 瞬时接触 | 300 | 脚本 + 遥操作补采 |
| C 持续接触 | 200 | 遥操作为主 |
| D 抓取放置 | 500 | 脚本 + 遥操作 |
| E 推拉 | 200 | 遥操作为主 |
| F 工具使用 | 100 | 遥操作 |

### 8.4 UAV + 机械臂资产需求
**末端执行器资产库**
- 1-DoF 平行夹爪（抓取放置基础版）
- 3-DoF 灵巧夹爪（精细抓取）
- 吸盘（吸附轻物）
- 接触探头（检测/采样）
- 清洁刷头（表面清洁）
- 喷涂工具（涂覆）
**目标物资产库**
- 城市垃圾类：塑料袋、易拉罐、纸箱、树枝
- 基础设施类：管道段、电缆段、墙面块、阀门、开关
- 检测目标类：裂缝面板、锈蚀管道、绝缘层样本
**物理交互模型**
- 刚体抓取：质量/摩擦/碰撞体积
- 柔性体交互：塑料袋等柔性物体的简化模型
- 表面接触：法向力+摩擦力模型
- 负载效应：抓取物体后 UAV 重心偏移和动力学变化
---

## 九、评测指标体系
### 9.1 导航指标（Phase 1）
基础指标：Success Rate / SPL / Goal Error / Collision Rate / Timeout Rate
动力学感知指标（差异化）：
- **Energy Efficiency（EE）**：实际能量 / 理论最短路径能量
- **Dynamic Feasibility Rate（DFR）**：轨迹物理可执行比例
- **Wind Robustness（WR）**：无风 SR / 有风 SR
- **Trajectory Smoothness（TS）**：加速度变化率（jerk）均值
Sim2Real 对齐指标（差异化）：
- **Sim-Real Trajectory Divergence（SRTD）**：DTW 距离
- **Sim-Real Success Gap（SRSG）**：成功率差异
- **Sim-Real Perception Gap（SRPG）**：目标检测 mAP 差异
### 9.2 过程导向指标（对标 HUGE-Bench）
- **TCR（Task Completion Rate）**：多阶段子任务完成比例
- **CR（Collision Rate）**：碰撞次数/总步数
- **CSPL（Collision-Safe SPL）**
### 9.3 操作指标（Phase 2，差异化核心）
导航→操作全链路：
- **Navigate-then-Manipulate SR（NM-SR）**：联合成功率
- **Navigate-then-Manipulate SPL（NM-SPL）**：路径加权联合成功率
- **Phase Transition Time**：导航→操作切换耗时
操作专用：
- **Grasp Success Rate（GSR）**：抓取成功率（D 类）
- **Contact Stability（CS）**：接触力稳定性标准差（B/C/F 类）
- **Surface Coverage Rate（SCR）**：表面操作覆盖率（C 类）
- **Force Accuracy（FA）**：力偏差（B/C/E/F 类）
- **Object Placement Accuracy（OPA）**：放置精度（D 类）
- **Post-Contact Recovery Time（PCRT）**：操作后恢复稳定悬停时间
安全：
- **Manipulation Collision Rate（MCR）**
- **Force Overload Rate（FOR）**
- **Post-Manipulation Stability（PMS）**：负载变化后飞行稳定性
---

## 十、新阶段开发路线图
### Phase A：当前稳定化收口（1–2 周）
目标：确保已有仿真内核可信，避免在不稳定基础上堆数据管线。
交付：
- 控制器多模式端到端验证：MOTOR_DIRECT / ATTITUDE / POSITION
- reset 后 POSITION 悬停稳定验证
- kinematic 与 MuJoCo 后端启动/关闭路径验证
- MuJoCo 生命周期统一：reset/play/pause/stop
- Sensor profile 清单整理
- 当前 `ROADMAP.md`、`README.md`、`linshi.md` 状态同步
验收：
- 单 UAV 在默认场景可稳定起飞/悬停/移动
- 不开 MuJoCo 时基础 AirSim 仿真仍可运行
- 开 MuJoCo 时接触物理与电机 ctrl 映射可观测
- Monitor 与 Python smoke 脚本可正常用于调试
### Phase B：模块化运行时基础设施（2–3 周）
目标：搭建后续 Scene/Task/Collector/Mapping 的骨架。
交付：
- `AirSparkRuntimeContext`
- `RuntimeModuleManager`
- `EpisodeRuntime` 最小实现
- `SensorHub` 最小实现
- `ObservationBus` 最小实现
- `AirSpark` 配置段：模块启停、sensor profile、backend profile
验收：
- 能通过一个 episode config 启动/停止基础任务
- Collector/Mapping/Planner 关闭时不产生额外开销
- 观察数据可以被 Monitor 与 Collector 同时订阅
- 无需新增高带宽 RPC 接口即可采集本地数据
### Phase C：程序化场景与任务生成（3–4 周）
目标：从手工摆场景转向可重复、可扩展、可随机化的场景/任务系统。
交付：
- `SceneTemplate` 与 `SceneInstance` schema
- 对象注册表：目标物、障碍物、语义标签、可交互物
- PointNav episode generator
- 简单 VLN instruction generator
- 动态体/人物行为可控 seed
- 场景随机化：天气、光照、目标位置、障碍布局
验收：
- 同一 seed 可复现场景
- 可批量生成 100+ PointNav episode
- 每个 episode 有 start/goal/success condition/sensor profile
- 不需要人工打开 UE 调整蓝图即可生成一批任务
### Phase D：程序化数据采集管线（3–4 周）
目标：形成标准采集、落盘、回放、质检闭环。
交付：
- Collector module
- Async writer
- raw + metadata 数据格式
- Python Dataset Builder 离线转换
- Episode replay 工具
- 基础质量检查：帧率、丢帧、碰撞、深度异常、pose 连续性
验收：
- 可批量采集 1k 条导航 episode
- 数据采集不依赖 Python RPC 拉图
- 单 episode 可回放
- 采集失败可自动标记 failure reason
### Phase E：建图、规划、导航基础设施（4–6 周）
目标：建立 benchmark 与后续自主系统的中间能力，而不是只做端到端黑盒控制。
交付：
- 2.5D occupancy grid map
- LiDAR/Depth 到地图投影
- A*/Theta* 全局规划
- 局部避障 baseline
- Waypoint follower
- 导航 Evaluator：SR/SPL/Goal Error/Collision/Trajectory Smoothness/Energy
验收：
- 在程序化小城市场景完成 PointNav baseline
- 可输出地图、路径、执行轨迹
- 能区分规划失败、控制失败、感知失败
- 形成第一版导航 benchmark report
### Phase F：操作任务基础设施（4–6 周，可与 E 后段并行）
目标：把已经提前打通的 MuJoCo/机械臂/夹爪能力转化为 benchmark 任务系统。
交付：
- End-effector state schema
- Contact/force event schema
- 1-DoF 夹爪任务 API
- 三类最小操作任务：触碰/推拉/抓取放置
- Navigate-then-Manipulate episode runtime
- 操作 Evaluator：GSR/CS/contact force/hover stability
验收：
- 至少 3 类操作任务可自动 reset 与判定 success
- Collector 能记录接触事件与末端状态
- MuJoCo 后端可按 episode 选择开启
- 导航→操作闭环跑通
### Phase G：Benchmark 产品化与规模化（长期）
目标：形成可对外发布的数据集、评测协议和 baseline。
交付：
- Benchmark package
- Baseline Runner
- Visualizer Web/UE 回放
- Sim2Real paired dataset
- 论文级实验与报告
验收：
- 可复现 benchmark 生成流程
- 可一键评测 baseline
- 可导出标准数据格式
- 有清晰论文卖点：城市低空导航→操作、动力学感知、Sim2Real 配对
---

## 十一、推荐目录演进
短期目标结构：
```plaintext
Unreal/airworld/Source/zero_sim_up/
├── Core/                   # Schema、Config、RuntimeContext、ModuleManager
├── SceneBuilder/           # 场景模板、对象生成、语义标签
├── SimRuntime/             # backend 选择、状态源、时间同步
├── Sensors/                # SensorHub、ObservationFrame 适配
├── TaskRuntime/            # Episode 加载、执行、成功条件
├── Collector/              # ObservationBus 订阅、异步写盘
├── Mapping/                # Occupancy/TSDF/Semantic map
├── Navigation/             # Planner、Waypoint follower
├── Evaluation/             # SR/SPL/动力学/操作指标
├── Visualization/          # 回放、调试、失败归因
└── Character/              # 已有人物行为与模型切换逐步迁入
```

Python 侧：
```plaintext
PythonClient/
├── airsim/                 # 保持 RPC 客户端兼容，不作为高带宽数据面
├── multirotor/             # 当前测试脚本
└── zero_sim/               # 新 SDK：dataset/eval/tools，不强依赖在线 RPC
    ├── datasets/
    ├── evaluation/
    ├── replay/
    └── tools/
```

配置侧：
```plaintext
configs/
├── airspark_runtime.json
├── episode_schema.json
├── sensor_profiles.yaml
├── scene_templates/
├── task_profiles/
└── vehicles/
    ├── vehicle_profiles.yaml
    ├── profiles/
    └── *.xml
```

---

## 十二、关键技术决策
### 12.1 RPC 不是数据面
决策：RPC 保留为控制面，不作为高带宽采集/建图/规划主通路。
理由：
- 带宽不足
- Python 拉图/点云会影响仿真帧率
- 数据采集和建图应复用同一帧数据，避免重复拷贝
- 后续可用 shared memory / ZMQ / ROS2 作为可选桥，不影响基础仿真
### 12.2 MuJoCo 是可选后端
决策：MuJoCo 不是所有任务的默认成本。
建议默认：
- 纯导航批采：kinematic backend
- 接触/操作/动力学评测：MuJoCo backend
- 高保真验证集：MuJoCo backend
- 训练大规模视觉导航：kinematic 或简化动力学
### 12.3 模块按需启停
决策：SceneBuilder、Collector、Mapping、Planner、Monitor、MuJoCo 都必须是可配置模块。
收益：
- 日常调试轻量
- 采集时只开必要模块
- 建图规划实验不影响基础飞行仿真
- 后续 benchmark 可按 profile 组合
### 12.4 先 raw+metadata，再标准格式
决策：不要一开始把所有采集都绑死到 HDF5/RLDS/ROS2 bag。
推荐：
- Phase D 先落 raw frames + episode metadata
- Python 离线 Dataset Builder 转 HDF5/RLDS/ROS2 bag
- C++ writer 保持轻量稳定
### 12.5 先规则 baseline，再学习 baseline
决策：建图规划导航先做可解释 baseline。
理由：
- 能验证场景/传感器/评测是否正确
- 能做 sanity check
- 后续 VLA/RL baseline 才有可靠对照
---

## 十三、近期执行清单
### P0：本周必须收口
- [ ] 确认 README.md 中当前版本能力与源码一致
- [ ] 确认 ROADMAP.md 不再宣称 Phase 0 为当前阶段
- [ ] 确认 MuJoCo 可不开启时基础仿真正常
- [ ] 确认 MuJoCo 开启时 reset/play/pause/stop 行为稳定
- [ ] 确认 v8.0 控制器 POSITION 悬停可用
- [ ] 整理 sensor profile 初版
- [ ] 冻结 Episode Schema v0.5-draft
### P1：下一轮开发入口
- [ ] 建 Core/RuntimeModuleManager
- [ ] 建 TaskRuntime/EpisodeRuntime 最小骨架
- [ ] 建 Sensors/SensorHub 最小骨架
- [ ] 建 Collector/ObservationBus 最小骨架
- [ ] 建 configs/airspark_runtime.json
- [ ] 做一个 point_nav_smoke_episode.json
### P2：程序化场景与采集
- [ ] Scene template schema
- [ ] Scene Builder 支持 spawn/clear/reset
- [ ] PointNav generator
- [ ] Async writer
- [ ] Episode replay
- [ ] QC report
### P3：建图规划导航
- [ ] Depth/LiDAR 投影到 occupancy grid
- [ ] A*/Theta* 路径规划
- [ ] Waypoint follower
- [ ] 导航 evaluator
- [ ] 可视化地图+路径+轨迹
### P4：操作任务系统
- [ ] End-effector schema
- [ ] Contact event schema
- [ ] 最小 touch/push/grasp 三任务
- [ ] Navigate-then-Manipulate runtime
- [ ] 操作 evaluator
---

## 十四、风险与注意事项

| 风险 | 表现 | 对策 |
|---|---|---|
| 把基础设施继续堆在 RPC 上 | 采集慢、丢帧、难规模化 | 数据面进 UE 内部 ObservationBus |
| MuJoCo 默认常开 | 调试成本高、性能低 | backend profile，按 episode 开启 |
| Scene Builder 过早复杂化 | 做不出闭环 | 先支持单模板、少量对象、seed 复现 |
| Dataset 格式过早重型化 | 依赖和构建拖慢 | 先 raw+metadata，离线转格式 |
| 评测晚于采集 | 数据不可用才发现 | Evaluator 与 Collector 同步建设 |
| Plugin 化过早 | 工程拆分成本高 | 先模块化目录，稳定后迁插件 |
| 控制/规划耦合 | baseline 难替换 | Planner 输出 waypoint/velocity，不直接写电机 |
| 传感器时间戳不统一 | 建图/评测错位 | SensorHub 统一 sim_time/frame_index |

---

## 十五、对外定位更新
当前对外定位建议调整为：
> AirSpark 是一个面向城市低空无人机导航与空中操作的 UE5 + AirSim + MuJoCo 仿真与 benchmark 平台。平台已具备可选 MuJoCo 接触物理、多模式飞控和多模态传感器底座，下一阶段重点建设程序化场景、批量数据采集、建图规划导航与 Navigate-then-Manipulate 任务基础设施。
核心差异化仍保留：
1. 城市低空导航 → 空中操作全链路（Search→Track→Approach→Align→Contact→Recovery）
2. 可选 MuJoCo 接触物理与机械臂/夹爪
3. 动力学感知评测（含负载变化、接触力、恢复能力）
4. 程序化场景与任务生成（四层数据飞轮）
5. 高带宽内部采集管线，而不是依赖 RPC 拉数据
6. Sim2Real paired episode 预留
---

## 十六、与 ROADMAP/README 的同步建议
`README.md` 当前更接近真实代码状态，基本可作为 v8.0 用户入口。
`ROADMAP.md` 需要后续同步：
- 将"Phase 0 当前"改为已完成/已过期
- 将 v8.0 控制器重构写入已完成能力
- 将"多级控制器接口计划中"改为"v8.0 初版已完成，后续继续外部控制器/MPC/RL 接入"
- 将"下一阶段"改为程序化场景、采集、建图规划导航基础设施
- 明确 RPC 控制面 / 内部数据面分离
- 明确 MuJoCo 可选后端，不作为所有任务默认依赖
---

## 十七、总结
AirSpark 当前的关键转折点是：
> 已经完成"仿真内核能跑"的主要底座，下一步必须从工程架构上进入"程序化世界 + 高带宽数据基础设施 + 建图规划导航 + 操作任务 runtime"。
后续开发不要再围绕"加一个 RPC 接口"展开，而要围绕"模块是否可启停、数据是否在内部高效流动、episode 是否可复现、采集是否可规模化、评测是否能闭环"展开。
**优先级排序：**
1. 稳定现有控制/物理/传感器底座
2. RuntimeModuleManager + EpisodeRuntime + SensorHub + ObservationBus
3. Scene Builder + Task Generator
4. Collector + Dataset Writer + Replay/QC
5. Mapping + Planner + Navigation Evaluator
6. Manipulation Task Runtime + Contact Dataset
7. Benchmark 产品化与 Sim2Real
---

**v0.6 完整变更（2026-05-21）**：基于 123.md 竞品更新与调研，全面升级项目定位、竞品矩阵、任务链路、数据飞轮、数据格式；新增 AirNav/IndoorUAV/AerialVLA（AAAI 2026 在线对话版）/CosFly-Track/UAV-Track VLA/AirVLA/Flying Hand/AERMANI-VLM/LiteVLA-H 等 2026 年新工作；1.1 定位改为 AirManip-Bench 完整描述；1.4 论文卖点升级为五点；新增 4.5 统一进程设计原则（CARLA-Air 教训）；新增 8.0 完整任务链路（Track/Approach/Align/Contact/Recovery 四个中间环节）；8.3 数据采集范式升级为四层数据飞轮；7.7 数据格式补充三层结构与标准 episode 字段；保留 v0.5 全部十七章架构设计内容。

