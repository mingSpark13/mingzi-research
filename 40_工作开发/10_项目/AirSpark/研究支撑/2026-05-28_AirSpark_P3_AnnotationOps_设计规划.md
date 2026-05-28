---
title: AirSpark P3 AnnotationOps — 语义标注数据工厂设计规划
date: 2026-05-28
version: v1.0
status: 正式
tags: [AirSpark, P3, AnnotationOps, LLM标注, 数据工厂, 设计文档]
sources:
  - 初步讨论结果.md
  - 临时调研LLM数据标注.md
  - 临时方案讨论.md
  - AirSpark架构文档_v0.8_2026-05-28.md
---

# AirSpark P3 AnnotationOps — 语义标注数据工厂设计规划

> 本文档整合 2026-05-28 的完整讨论与调研，是 AirSpark P3 阶段的正式设计规划文档。
> 来源：[[初步讨论结果]]、[[临时调研LLM数据标注]]、[[临时方案讨论]]、[[AirSpark架构文档_v0.8_2026-05-28]]

---

## 一、项目定位与方向决策

### 1.1 平台定位

**AirManip-Bench** 是一个面向城市低空场景的多模态 Navigate-then-Manipulate benchmark，覆盖语言导航、目标搜索/跟踪、接近对齐、多类接触操作和负载扰动恢复，并提供动力学感知评测、自动化 episode 生成与 Sim2Real 配对验证。

论文标题方向：
> **"AirManip-Bench: A Navigate-then-Manipulate Benchmark for Contact-Rich Aerial Tasks in Urban Environments"**

五个核心差异化：
1. **Navigate-then-Manipulate 全链路**：Search → Track → Approach → Align → Contact → Recovery
2. **Contact-Rich 操作分类**：6 类空中接触操作（A-F 类）
3. **Dynamics-Aware 评测**：含接触力、负载变化、姿态扰动、恢复能力
4. **Hybrid Synthetic–Real 数据飞轮**：UE 仿真 + 3DGS 重建 + 遥操作 seed + 自动优化
5. **Modular 可扩展基础设施**：RPC 控制面 + 高带宽内部数据面 + 模块按需启停

### 1.2 P3 方向调整决策

**核心决策：不把 AirSpark 做成"大而全 UE 程序化场景生成器"。**

| 原定 | 调整后 |
|------|--------|
| P3 SceneOps — 程序化场景生成 | P3 AnnotationOps — 语义标注数据工厂 |
| SceneSpec 驱动 UE PCG 造世界 | SceneSpec 作为场景元数据治理 |
| 自研 mini-PCG 引擎 | 接入任何外部场景 + 自动深度标注 |
| 数据飞轮靠场景多样性 | 数据飞轮靠标注深度和语义丰富度 |

**理由：**
- PCG 场景生成已有大量商业方案全力推进（UnrealLLM、AutoUE、UE PCG Plugin、Fab 城市场景包），自研性价比极低
- 场景生成是供给侧，标注与任务构造才是差异化护城河
- 同一个 School 地图，通过深度语义标注 + 多样化语言指令 + 推理监督，数据价值可提升 10×

**一句话概括：**
> AirSpark 的重点不是造世界，而是把已有世界变成"可理解、可记忆、可推理、可训练"的低空任务数据。

### 1.3 SceneSpec 角色降级

```
原来：SceneSpec = 驱动 UE 程序化造世界的主抽象
调整：SceneSpec = 记录场景来源、资产版本、区域层级、任务配置、标注策略的统一元数据
```

SceneSpec 不负责"造场景"，负责"描述和治理场景"。后续接任何外部场景（School、Fab、PCG、3DGS 重建、真实回流）都统一接入 AnnotationOps 流水线。

---

## 二、平台架构现状（v0.8）

### 2.1 开发阶段

| 阶段 | 内容 | 状态 |
|------|------|------|
| P0 主线稳定化 | UE5.7 迁移、AirSim fork、MuJoCo 后端、控制器 v8.0、School 地图 | ✅ 已完成 |
| P1 随机化 VLA 采集闭环 | Schema v2 + FLU 坐标系、CollectorSubsystem、随机化采集循环 | ✅ 已完成（2026-05-13） |
| P2 UE 内部批采集系统 | BatchControllerSubsystem 状态机、MissionDirector、JSONL writer、图像捕获队列 | ✅ 已完成（2026-05-15） |
| **P3 AnnotationOps** | **语义标注数据工厂（本文档）** | **🔄 当前阶段** |
| P4 Real2Sim / Sim2Real | 真实重建回流、3DGS-Mesh 配对 episode、Sim2Real 验证 | ⬜ 待 P3 后启动 |
| P5 Navigate-then-Manipulate | 完整操作链路、接触操作任务系统、动力学感知评测 | ⬜ 长期目标 |

### 2.2 P2 遗留缺口（P3.0 前必须收口）

| 缺口 | 影响 | 优先级 |
|------|------|--------|
| `max_retries_per_episode` 只进 schema，BatchController 未消费 | 大批量采集自动恢复能力缺失 | 高 |
| ObserveSelector 采样通过率约 9% | 批采集效率低，大量 episode 被过滤 | 中 |
| OccupancyGridPlanner 仍是 stub | 复杂场景路径规划不可用，Explore2Map 依赖此模块 | 中 |
| 无 CI / 自动化测试 | 回归风险高 | 中 |

### 2.3 代码架构快照（12 子模块）

| 子模块 | 职责 | 当前状态 |
|--------|------|----------|
| Batch | BatchControllerSubsystem 状态机，批采集编排 | ✅ P2 已完成 |
| Mission | MissionDirector，episode 编排与生命周期 | ✅ P2 已完成 |
| Navigation | WaypointExecutor + OccupancyGridPlanner | 🔄 Executor 可用，规划器 stub |
| Collection | CollectorSubsystem，数据采集接入 | ✅ P1/P2 已完成 |
| Episode | EpisodeCoordinator，episode 上下文管理 | ✅ P2 已完成 |
| Randomization | 场景/任务随机化，ObserveSelector | 🔄 基础可用，采样通过率待优化 |
| Runtime | AirSparkRuntimeProfile，全局配置与 backend 选择 | 🔄 可用，多 drone 全局 override 待拆 |
| Semantic | 语义标签与场景理解 | 🔄 基础可用 |
| Observation | ObservationBus，进程内数据总线 | ✅ P2 已完成 |
| Diagnostics | 诊断与健康检查 | 🔄 基础可用 |
| SceneDebug | 场景调试可视化（~974 行，待拆分） | 🔄 基础可用 |
| Physics | MuJoCo/Kinematic 后端抽象 | ✅ 已完成 |

### 2.4 数据流向

```
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

---

## 三、P3 AnnotationOps 核心设计

### 3.1 设计目标

把"能采集"升级为"能理解场景、能标注轨迹、能生成可训练数据"。

从：
```
instruction + trajectory
```
升级为：
```
instruction + trajectory + semantic map + region hierarchy + memory updates + subgoal reasoning labels
```

这才可能训练出具备 VLN 推理记忆能力的模型。

### 3.2 核心数据结构

P3 的核心是以下五张图：

```
RegionGraph     — 区域层级图（楼、楼层、教室、走廊、操场、篮球场）
ObjectGraph     — 对象实例图（门、窗、桌椅、篮球架、垃圾桶）
RelationGraph   — 空间关系图（包含、相邻、连接、可见、支撑、portal）
TaskTrace       — 轨迹过程推理图（子目标、记忆更新、候选目标、失败原因）
MapMemory       — 五层语义地图（Metric / Object / Region / Relation / Task Memory）
```

#### RegionGraph：区域层级图

区域不是扁平分类，必须做成**层级 + 关系**结构：

```json
{
  "region_id": "corridor_2f",
  "name": "二楼走廊",
  "type": "corridor",
  "parent": "floor_2",
  "children": ["classroom_201", "classroom_203"],
  "polygon_2d": [[...]],
  "height_range": [3.0, 6.0],
  "semantic_tags": ["indoor", "corridor", "navigable"],
  "aliases": ["教学楼二楼过道", "二层通道"],
  "description": "连接多个教室门的狭长室内通道，适合作为搜索教室门和楼梯的导航区域。"
}
```

**关键：边界对象（portal object）不是单区域归属**

```json
{
  "object_id": "SM_DoorClassroom2",
  "category": "door",
  "primary_region": "corridor_2f",
  "connected_regions": ["corridor_2f", "classroom_203"],
  "relation_type": "portal",
  "affordances": ["enter", "inspect", "observe"]
}
```

典型边界对象及其正确语义：

| 对象 | 正确语义 |
|------|----------|
| 门 | 连接走廊和教室 |
| 窗 | 属于建筑外立面，同时关联室内房间 |
| 楼梯 | 连接楼层 |
| 校门 | 连接校内和校外道路 |
| 篮筐 | 属于篮球场 |
| 垃圾桶 | 位于走廊/操场/楼门口 |

**区域生成方法**（不能只靠 SAM 切，要靠几何 + 语义 + 拓扑推断）：

```
Object Instances
    ↓
Spatial Clustering
    ↓
Boundary / Connectivity Analysis
    ↓
Region Candidate Generation
    ↓
LLM Region Naming + Hierarchy Inference
    ↓
Human Review / Rule Validation
```

**实现策略：**
- RegionGraph 在 C++ 侧（AirSparkSemanticWorldSubsystem）目前**不存在**对应数据结构
- P3 阶段先做 Python 侧 JSON 实现（方案 A），UE C++ Actor 实现（方案 B）留 P4
- 手工粗标大区域 polygon，再自动 object-to-region 分配

#### ObjectGraph：对象实例图

当前实际数据（episode.json）：

```json
{
  "instruction": "Navigate to observe 这是一个教室的门.",
  "target_semantic_name": "门",
  "target_object_id": "SM_DoorClassroom2"
}
```

LLM 补全后目标：

```json
{
  "object_id": "SM_DoorClassroom2",
  "canonical_name": "教室门",
  "category": "door",
  "nouns": ["门", "教室门", "入口"],
  "attributes": ["走廊侧", "室内入口", "矩形"],
  "affordances": ["接近观察", "进入教室", "检查门牌"],
  "observe_distance_m": 2.5,
  "task_roles": ["navigation_target", "inspection_target", "portal"],
  "language_aliases": ["走廊左侧的教室门", "二楼教室入口", "靠近墙边的那扇门"]
}
```

#### TaskTrace：轨迹过程推理图

每步结构化推理标签（非自由散文 CoT）：

```json
{
  "timestep": 42,
  "current_region": "corridor_2f",
  "visible_objects": ["door_201", "door_203", "window_02"],
  "target_candidates": [
    {"object_id": "door_203", "score": 0.82, "evidence": "left side, classroom sign visible"}
  ],
  "subgoal": "approach_target",
  "next_action_intent": "move_forward_and_yaw_left",
  "memory_update": ["door_203 observed", "corridor left wall explored"]
}
```

**TaskTrace 字段可靠性分级（重要）：**

| 字段 | 来源 | 可靠性 | 用途 |
|------|------|--------|------|
| current_region | 几何 polygon 判断 | 高（规则） | 直接作为训练监督 |
| visible_objects | UE seg render pass | 高（真值） | 直接作为训练监督 |
| subgoal_stage | 轨迹阶段规则切分 | 中（规则） | 训练监督 |
| target_candidates | 几何距离 + 可见性 | 中（规则） | 训练监督 |
| memory_update | LLM 推断 | 中（需验证） | 先数据增强，验证后升级 |
| failure_reason | LLM 推断 | 中（需验证） | 先数据增强，验证后升级 |
| next_action_intent | LLM 推断 | 低（参考） | 仅参考 |

#### 五层 MapMemory

```
AirSpark MapMemory
├── Metric Map        — occupancy grid / ESDF / height map / collision / no-fly zone
├── Object Map        — object instance / 3D bbox / affordance / observe pose
├── Region Map        — room / corridor / building / playground / court + 层级
├── Relation Graph    — left_of / near / inside / connected_to / visible_from / reachable_from
└── Task Memory       — discovered targets / candidate goals / visited regions / subgoal status / failure
```

训练两类模型：

**Map-conditioned VLN/VLA**：输入 RGB + state + instruction + MapMemory summary → 输出 next waypoint / action chunk

**Memory updater / reasoning model**：输入当前观察 + 上一时刻 MapMemory → 输出新增对象/区域、目标候选更新、下一步探索区域

### 3.3 两大子系统

**系统 A：场景自标注（Scene Auto-Annotation）**

在 UE 内自动完成场景语义理解，取代手动标注：

```
UE Scene → SceneScanner（多视角 RGB+Depth+Seg）
         → SegmentationBridge（Stencil 真值 / SAM）
         → SemanticEnricher（LLM 补全对象语义）
         → RegionBuilder（区域检测 + LLM 命名）
         → SemanticMap.json（ObjectGraph + RegionGraph + RelationGraph）
```

**系统 B：轨迹语言标注（Trajectory Annotation）**

采集完成后，利用语义地图为轨迹生成训练监督：

```
采集轨迹 + SemanticMap
  → 实时标注：current_region / visible_objects / subgoal_stage（几何规则，UE 内）
  → 离线标注：instruction / memory_update / failure_reason（LLM 推断）
  → 输出：TaskTrace + Instructions + MapMemory supervision
```

### 3.4 系统分层架构

```
┌─────────────────────────────────────────────────┐
│  Layer 5: Dataset Export                         │
│    LeRobot / HDF5 / RLDS / VLN-Memory format    │
├─────────────────────────────────────────────────┤
│  Layer 4: LLM Annotation Engine（轨迹语言标注）    │
│    Instruction Gen · TaskTrace · Memory Labels   │
├─────────────────────────────────────────────────┤
│  Layer 3: Data Collection（已交付 P2）            │
│    BatchController · Planner · Collector · Sensor│
├─────────────────────────────────────────────────┤
│  Layer 2: Semantic Map（场景自标注）               │
│    SceneScanner · Segmentation · LLM · Region    │
├─────────────────────────────────────────────────┤
│  Layer 1: Scene Runtime（已交付 P1/P2）           │
│    SemanticWorld · SceneDebug · RuntimeProfile    │
└─────────────────────────────────────────────────┘
```

### 3.5 七个 LLM 模块

#### 模块 1：Semantic Patch Generator（优先级最高）

补全 UE 里已有 SemanticComponent 的空字段。

- 输入：actor_name、semantic_name、category、level_name、nearby_objects
- 输出：canonical_name、nouns、attributes、affordances、observe_distance、task_roles
- 实现：`tools/airspark_dataset_tools/semantic_patch_generator.py`
- 价值：直接提升现有 School 地图数据质量，不需要碰复杂 UE 逻辑

#### 模块 2：RegionGraph Builder

建立区域层级，短期手工粗标大区域，LLM 补自然语言别名和区域描述。

- 输入：手工 region polygon JSON + object list
- 输出：region_graph.json（含 aliases、description、typical_objects）
- 中期：自动分割/探索地图生成 region candidate

#### 模块 3：Object-to-Region Resolver

判断物体属于哪个区域、是否跨区域、是否是边界连接物。

- 规则优先：bbox center 在 region polygon 内 → belongs_to；与两个 region 边界相交且 category=door/window → connects
- LLM 处理模糊情况（portal 对象、外立面对象、跨层对象）
- 输出：object_region_assignments.json、region_object_index.json、relation_graph.json

#### 模块 4：Exploration-to-Map Annotator

UAV 探索完整地图后，自动生成语义地图。

- 仿真内优先用 UE 真值 segmentation（Stencil render pass）
- 真实/未知场景用 SAM3 / OpenMask3D / ConceptGraphs 路线（P4）
- 依赖：OccupancyGridPlanner（P3.0 需先完成）

#### 模块 5：Instruction & Referring Expression Generator

为同一目标生成不同粒度语言：

| 语言类型 | 示例 | 训练能力 |
|----------|------|----------|
| 高层指令 | "找到二楼走廊左侧的教室门并靠近观察" | 任务理解 |
| 区域引导 | "先进入教学楼二楼走廊，再寻找靠左侧墙面的教室入口" | 分层导航 |
| 目标指代 | "那扇位于走廊左侧、靠近窗户的教室门" | grounding |
| step-by-step | "从走廊入口起飞，沿走廊前进，在看到左侧门牌后调整朝向" | VLN 路径跟随 |
| 失败描述 | "目标门被墙遮挡，未能进入相机视野" | failure mining |

注意：**可 grounding 优先于语言自然**，一句漂亮但指错目标的指令是毒数据。

#### 模块 6：TaskTrace / Reasoning Label Generator

给轨迹补中间推理监督，输出结构化标签（非自由散文 CoT），更安全、更可控、更适合训练。

#### 模块 7：Failure Reasoner / Regeneration Planner

失败 episode 不只标注 `timeout`，而是解释失败原因并生成补采策略：

```json
{
  "failure_type": "target_not_visible",
  "failure_stage": "localize_target",
  "root_cause": "observe point was behind a wall, target door never entered camera frustum",
  "suggested_regeneration": {
    "change_spawn_region": "corridor_2f",
    "increase_observe_distance": 3.5,
    "require_visibility_check": true
  }
}
```

直接服务 AirSpark v0.7 已有的 Failure Mining + Regeneration Planner 主线。

### 3.6 完整 AnnotationOps 流水线（12 步）

```
1.  Scene Intake          — School / Fab / PCG / 3DGS / RealScan 场景接入
2.  Semantic Inventory    — 扫描 UE Actor / SemanticComponent / render pass → object_raw.json
3.  Region Seeding        — 手工或规则生成 building / floor / room / court / road 区域
4.  Exploration Sweep     — UAV 自动探索，采 RGB-D-Seg-Pose，生成可见性和候选对象
5.  Object & Region Fusion — 多帧融合 3D object map + object-to-region 归属 + region hierarchy
6.  LLM Semantic Enrichment — 补 nouns / attributes / affordances / aliases / referring expressions
7.  Task Generator        — 根据区域图和对象图生成高层任务、子任务、成功条件
8.  Expert Planner        — A*/Theta*/RRT/coverage/orbit planner 生成参考轨迹
9.  TaskTrace Annotator   — 给轨迹打 subgoal / memory update / target candidate / reasoning state
10. QA Validator          — 检查语义一致性、可见性、路径可达、语言歧义、标注置信度
11. Dataset Builder       — 输出 LeRobot / HDF5 / RLDS / 自定义 VLN-memory 格式
12. Failure Mining        — 模型训练/评测失败后，回流到任务生成器补采
```

**最核心的是第 5–9 步：把场景变成可查询、可推理、可训练的语义记忆。**

---

## 四、技术参考

### 4.1 指令生成方案

**NavRAG（场景树 + RAG）**：自动构建 scene description tree，用 RAG-LLM 根据用户画像和场景上下文生成导航指令，模拟不同用户（安全巡检员、配送员、应急响应员、维修工程师）的真实需求。可套用到低空任务：

```
scene tree: campus → building A → entrance / windows / roof
user persona: security inspector / delivery operator
生成指令: "巡检左侧玻璃楼的外立面" / "沿主路搜索停在路边的白色车辆"
```

**MAPInstructor（地图编码进指令生成）**：把 egocentric observations 投影到 3D voxel，结合 topological map 做 prompt tuning，加入 landmark uncertainty assessment 减少幻觉。输入给语言生成器：top-down semantic map + target object mask + relative direction + route keypoints + altitude constraints。

**3D-GRAND（dense 3D grounding）**：低空场景语言标注不能只有一句任务指令，最好有多层 grounding：

```
对象级：  "white car" → car_012 → 3D bbox / mask
区域级：  "parking lot near the building" → region_003 polygon
关系级：  "building on the left of the road" → relation(building_04, left_of, road_01)
任务级：  "inspect the left building" → target=building_04, behavior=orbit/inspect
```

### 4.2 自动标注三层方法

**生成即标注**：PCG 生成每个对象时就记录 metadata（instance_id、category、transform、bbox_3d、semantic_tags），直接导出 2D segmentation / instance mask / 3D bbox / object graph / task affordance。比 SAM/YOLO 后处理准确得多。

**渲染即标注**：UE render pass 输出 RGB / Depth / Normal / Semantic ID / Instance ID / Object mask / Camera pose / UAV pose，每帧视觉输入和几何真值绑定。这是 benchmark 可信度的根基。

**VLM/LLM 校验标注**：VLM 不负责主标注，而负责检查（图中是否真的有目标？目标是否在左侧？语言描述是否和图像/地图一致？）。VLM 是"质检员"，不是"唯一真值来源"。

### 4.3 规划三层架构

LLM 不应该直接输出连续安全航迹：

```
语义任务层：LLM
  "巡检左侧建筑" → target=building_04, behavior=facade_inspection
  constraints: keep_distance, altitude_range, no_collision

几何规划层：A* / RRT* / PRM / frontier / coverage planner
  输入 ESDF / occupancy map / semantic map / no-fly zone
  输出 waypoints / reference trajectory

控制执行层：MPC / PID / low-level controller
  跟踪轨迹，处理动力学约束和安全距离
```

LLM 主要访问 Semantic + Topological + Language Layer，规划器访问 Metric + Semantic Layer。

### 4.4 真实场景路线（P4）

仿真内优先用 UE 真值，真实/未知场景用以下路线：

```
UAV 探索轨迹（RGB / Depth / Pose / IMU）
    ↓
SAM3 / Grounded-SAM / YOLO-seg → 多帧 2D mask
    ↓
深度 + 相机位姿投影到 3D
    ↓
多视角关联，聚合成 3D object instance
    ↓
CLIP/SigLIP/DINO 特征聚合 → open-vocabulary object embedding
    ↓
LLM/VLM 语义命名与区域关系推断
```

参考：ConceptGraphs（2D foundation model → open-vocabulary 3D scene graph）、OpenMask3D（class-agnostic 3D mask + 多视角 CLIP 特征聚合）。

注意：SAM3 给的是 2D/视频 object mask，不会自动给可靠的 3D 区域层级。区域生成要靠几何边界 + 拓扑关系 + 语义对象集合 + LLM 归纳。

---

## 五、P3 执行计划

### P3.0：收口现有采集系统（地基，不可跳过）

- [ ] 实现 `max_retries_per_episode`（BatchController 消费该字段）
- [ ] Semantic Inventory 导出路由 `/debug/semantic_inventory`
- [ ] 验证 ObserveSelector 通过率 >50%（需启动 UE 实测）
- [x] ObserveSelector 候选采样优化（近距离环 + clearance 统一到 cell size）
- [x] 起点连通性重试（PreviewPaths 最多 5 次不同 seed）
- [x] MissionDirector 参数源统一（从 RuntimeProfile 读 clearance）

### P3.1：LLMClient + Semantic Patch

最低成本，最高收益。

- [ ] `Source/AirSpark/LLM/AirSparkLLMClient.h/.cpp`：OpenAI-compatible HTTP 客户端，支持多模态
- [ ] `Source/AirSpark/Annotation/AirSparkSemanticEnricher.h/.cpp`：对象语义补全
- [ ] School 地图 Semantic Patch：补全所有 SemanticComponent 的 canonical_name / affordances / aliases
- [ ] 输出 `semantic_inventory.json` + `semantic_patch.json`

> ⚠️ 待确认：scene_summary.json 是否包含完整 SemanticComponent 列表？School 地图中有多少 Actor 已挂载 SemanticComponent？

### P3.2：RegionBuilder + RegionSubsystem

不要一上来自动识别区域。先手工定义 building / floor / corridor / classroom / playground / court 的 polygon，再自动把对象分配进去。

- [ ] `Source/AirSpark/Annotation/AirSparkRegionBuilder.h/.cpp`：区域自动检测
- [ ] `Source/AirSpark/SemanticMap/AirSparkRegionSubsystem.h/.cpp`：运行时区域查询
- [ ] School 地图 RegionGraph v1（走廊/教室/操场/楼梯间）
- [ ] Object-to-Region 归属分配

输出：region_graph.json（Python 侧 JSON，方案 A）

### P3.3：SceneScanner + 分割融合 + SceneSpec v1 + QA Dashboard

- [ ] `Source/AirSpark/Annotation/AirSparkSceneScannerSubsystem.h/.cpp`：扫描路径规划 + 多视角采集
- [ ] `Source/AirSpark/Annotation/AirSparkSegmentationBridge.h/.cpp`：Stencil 真值 + SAM 双路线
- [ ] 多视角实例融合 → 3D BBox
- [ ] 完整场景自标注 pipeline 端到端验证
- [ ] SceneSpec schema v1（轻量元数据角色）
- [ ] QA Dashboard：标注质量可视化，覆盖率分析

### P3.4：TrajectoryAnnotator

- [ ] `Source/AirSpark/Annotation/AirSparkTrajectoryAnnotator.h/.cpp`
- [ ] 实时标注：current_region / visible_objects / subgoal_stage（写入 frames.jsonl 扩展字段）
- [ ] 离线 LLM 标注：instruction / memory_update / failure_reason（输出 task_trace.json）
- [ ] Prompt 模板设计与验证

为每个 episode 生成：high_level_instruction / subtask_instruction / target_referring_expression / region_hint / subgoal sequence / memory_update labels / failure_reason

### P3.5：Dataset Export + QA + Failure Mining

- [ ] Dataset Builder：输出 LeRobot / VLN-Memory 格式
- [ ] QA Validator：语义一致性、可见性、路径可达、语言歧义检查
- [ ] Failure Mining：从失败 episode 自动定位错误区域/目标/路径
- [ ] Regeneration Planner：驱动补采策略

---

## 六、评估指标体系

### 6.1 语义地图质量

| 指标 | 含义 |
|------|------|
| Object Detection Recall | 探索后地图里找到了多少真实对象 |
| Object Duplicate Rate | 同一对象是否被重复建成多个实例 |
| 3D Localization Error | 对象 3D 中心 / bbox 误差 |
| Region Assignment Accuracy | 物体归属区域是否正确（篮球架→篮球场，不能只到操场） |
| Region Hierarchy Accuracy | 层级关系是否正确（篮球场→操场→校园） |
| Relation Accuracy | left_of / inside / connected_to 等关系是否正确 |
| Map Coverage | 已探索区域 / 总可探索区域 |
| Visibility Coverage | 目标对象被有效观察的角度/距离覆盖率 |

### 6.2 语言标注质量

| 指标 | 含义 |
|------|------|
| Grounding Accuracy | 指令中的目标是否能唯一对应正确 object/region |
| Ambiguity Rate | 一句话是否可能指向多个目标 |
| Spatial Reference Accuracy | 空间词（左/右/前/后/附近）是否正确 |
| Hallucinated Landmark Rate | 指令中是否提到了场景不存在的 landmark |
| Instruction Diversity | 同一任务的语言表达多样性 |
| Planner Feasibility | 按该指令是否存在可行轨迹 |

### 6.3 TaskTrace / 记忆监督质量

| 指标 | 含义 |
|------|------|
| Subgoal Alignment | 轨迹阶段标签是否和实际位置/动作一致 |
| Memory Update Precision/Recall | 新发现对象/区域是否在正确时间写入记忆 |
| Candidate Target Accuracy | 每步候选目标排序是否合理 |
| Failure Explanation Accuracy | 失败原因是否和真实日志一致 |

### 6.4 下游模型收益（核心对比实验）

| 实验组 | 输入/监督 |
|--------|-----------|
| Baseline A | RGB + instruction → action |
| Baseline B | RGB + instruction + semantic target → action |
| Ours-Map | RGB + instruction + MapMemory → action |
| Ours-Trace | RGB + instruction + MapMemory + TaskTrace supervision |
| Ours-Active | 加入 failure mining 回流补采 |

**重点报三个新指标：**

1. **Wrong-Region Rate** — 模型是否跑到了错误区域（体现区域推理能力）
   ```
   目标：二楼教室门
   错误：飞到一楼门 / 操场门 / 另一个教室门
   ```

2. **Memory Utility Gain（MUG）** = SR_with_MapMemory − SR_without_MapMemory（证明标注不是摆设）

3. **Exploration Efficiency** — 首次看到目标所需时间/路径长度/无关区域访问次数

### 6.5 导航与操作指标（P5 差异化核心）

**导航指标**：SR / SPL / Goal Error / Collision Rate / Energy Efficiency / Dynamic Feasibility Rate / Trajectory Smoothness

**操作指标**：
- NM-SR（Navigate-then-Manipulate SR）：联合成功率
- GSR（Grasp Success Rate）：抓取成功率
- CS（Contact Stability）：接触力稳定性标准差
- PCRT（Post-Contact Recovery Time）：操作后恢复稳定悬停时间
- PMS（Post-Manipulation Stability）：负载变化后飞行稳定性

---

## 七、论文叙事

### 7.1 定位

**不写成：**
> 我们提出了一个 UE 程序化场景生成平台。

**写成：**
> 我们提出一个面向低空导航—操作任务的 **LLM-assisted Semantic Annotation and Map-Memory Data Factory**。它能从仿真或真实探索轨迹中构建层级区域图、对象图、关系图和任务过程轨迹标注，并生成可训练 VLN/VLA 推理记忆能力的数据。

### 7.2 核心贡献（五条）

1. **Hierarchical Low-altitude Semantic Map**
   面向 UAV 的区域—对象—关系层级图，支持建筑、楼层、教室、操场、篮球场、道路、外立面等多尺度区域建模。

2. **LLM-assisted AnnotationOps**
   利用 LLM/VLM 自动补全对象语义、区域归属、空间关系、自然语言指令和任务过程标签。

3. **Map-memory Supervision for VLN/VLA**
   不只提供轨迹 imitation 标签，还提供探索记忆、候选目标、子目标阶段、失败原因等中间监督。

4. **Active Failure-driven Data Flywheel**
   从模型失败中自动定位错误区域/目标/路径/观察点，驱动补采。

5. **Navigate-then-Manipulate Extension**
   后续接入接触操作，语义地图同时服务导航和操作（P5）。

---

## 八、风险与注意事项

| 风险 | 表现 | 对策 |
|------|------|------|
| max_retries 未消费 | 大批量采集自动恢复能力缺失 | P3.0 前置收口 |
| ObserveSelector 通过率低 | 批采集效率低，大量 episode 被过滤 | P3.0 第二轮优化采样策略 |
| 规划器 stub | 复杂场景路径规划不可用 | P3.3 实现 OccupancyGridPlanner |
| RegionGraph 工作量被低估 | C++ 侧无对应数据结构，需从 Python 侧 JSON 开始 | P3.2 先做 Python 侧方案 A |
| TaskTrace LLM 字段可靠性 | LLM 推断字段直接作为监督信号可能引入噪声 | 按可靠性分级，几何/规则字段优先 |
| 模块继续膨胀 | 线程/状态/日志互相缠绕 | 严格遵守 Module-Boundaries.md |
| 无 CI | 回归风险高 | P3 期间建立基础 pytest + smoke test |
| 跳过 Sim2Real 直接做 benchmark | sim2real gap 无法量化 | P4 先建配对验证能力 |

---

## 九、待确认问题

1. **scene_summary.json 完整性**：是否包含完整 SemanticComponent 列表？还是需要单独从 UE 导出 Actor 列表？这决定 P3.1 Semantic Inventory 的实现路径。

2. **School 地图 SemanticComponent 覆盖率**：有多少 Actor 已挂载 SemanticComponent？这决定 P3.1 Semantic Patch 的实际工作量。

---

## 十、参考文献

| 论文 | 来源 | 关联模块 |
|------|------|----------|
| MapNav | arXiv 2502.13451 | MapMemory 设计参考 |
| VLMaps | ICRA 2023 | 视觉语言特征融合进 3D 地图 |
| HOV-SG | RSS 2024 | Hierarchical Open-Vocabulary 3D Scene Graphs |
| ConceptGraphs | arXiv 2309.16650 | 真实场景 open-vocabulary 3D scene graph |
| OpenMask3D | NeurIPS 2023 | Open-Vocabulary 3D Instance Segmentation |
| SAM3 / SAM3.1 | Meta AI | 真实场景分割（P4） |
| NavRAG | — | 指令生成：scene tree + RAG |
| MAPInstructor | CVF | 指令生成：地图编码 |
| 3D-GRAND | CVPR 2025 | Dense 3D grounding 数据 |
| HUGE-Bench | arXiv | 3DGS 数字孪生 + 过程导向评测 |
| SAGE | arXiv | Agentic 场景生成 + visual/physics critic |
| UnrealLLM | ACL 2024 | 自然语言 → UE5 PCG blueprint |
| AutoUE | arXiv | 多智能体 UE 场景生成 |
| CARLA-Air | arXiv 2603.28032 | bridge-based co-simulation 教训 |
| AirNav | arXiv 2601.03707 | 竞品：137K 真实城市 UAV VLN |
| AIR-VLA | — | 竞品：首个空中操作 benchmark |
| AirVLA | arXiv 2603.25038 | 竞品：π0 迁移到空中操作 |
| CosFly-Track | arXiv 2605.17776 | 竞品：城市 UAV 视觉跟踪 |


