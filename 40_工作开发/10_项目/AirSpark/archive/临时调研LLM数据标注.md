> ⚠️ 本文档为临时调研记录，内容已整合至 [[2026-05-28_AirSpark_P3_AnnotationOps_设计规划]]，请以该文档为准。

---

可以，抛开 UAV-Flow 单篇，现在这条线已经很清晰了：

> **大模型不是直接替代仿真器，而是变成“场景/任务/语言/标注/评测”的自动化调度器。**
> 真正可靠的系统一般是：**LLM 负责语义规划和代码/参数生成，PCG/仿真器负责可执行生成，VLM/物理引擎/路径规划器负责验证与修正。**

这对你的低空 benchmark 很重要。你不应该只做“UE 里摆几个场景 + 采轨迹”，而应该做成：

```text
自然语言任务需求
    ↓
LLM 生成结构化场景规格 / 任务规格
    ↓
UE PCG / 资产库 / 程序化规则生成场景
    ↓
自动语义标注 / 3D scene graph / top-down map
    ↓
自动生成自然语言描述和任务指令
    ↓
自动建图、路径规划、轨迹采集
    ↓
VLA / VLN / Planner 统一评测
```

这才是现在比较像样的“主动数据工厂”范式。

---

## 1. 最新方向：从“视觉好看”转向“仿真可用”

2026 年的 embodied 3D generation survey 把这个领域分成三类：**Data Generator、Simulation Environments、Sim2Real Bridge**。它特别强调，现在评价 3D 生成不能只看视觉真实，而要看是否具备几何有效性、物理参数、关节/运动结构、仿真器兼容性和下游任务可执行性。这个判断非常关键，因为你的低空平台不能只生成漂亮 UE 场景，还要能碰撞、能规划、能标注、能采数据、能评测。([arXiv][1])

所以现在的核心转变是：

```text
旧范式：
文本 → 漂亮 3D 场景

新范式：
任务需求 → 可交互场景 → 自动标注 → 自动规划 → 自动采数据 → 自动评测
```

这也是 SAGE、SceneCode、UnrealLLM、HUGE-Bench、SimWorld Studio 这些工作的共同趋势。

---

## 2. 程序化场景生成：现在主流有四种路线

### 路线 A：规则 / PCG 主导，LLM 负责参数化

这是最适合你 AirSpark/UE 平台的路线。

典型代表是 **UnrealLLM** 和 **AutoUE**。UnrealLLM 把自然语言描述接到 Unreal Engine 5 的 PCG 系统里，通过知识库把文本转成可执行 PCG blueprint，并用 spline-based control 做几何布置。它的重点不是让 LLM 直接写一堆硬编码坐标，而是让 LLM 操控 UE 原生 PCG 能力。([ACL论文集][2])

AutoUE 更进一步，做成多智能体：模型检索 agent 从 858K 3D 模型库里找资产，场景生成 agent 用 UE PCG 生成可编辑 layout graph，代码 agent 生成玩法逻辑，最后还有自动 play-testing agent 运行测试命令检查结果。这个思路非常适合你，因为 UE 场景不是一次性 mesh，而是可编辑、可参数化、可复用的 PCG 图。([arXiv][3])

你可以对应到低空场景：

```text
LLM 输出：
{
  "scene_type": "urban_low_altitude",
  "roads": [...],
  "buildings": [...],
  "trees": [...],
  "targets": [...],
  "obstacles": [...],
  "task_zones": [...]
}

UE PCG 执行：
道路 spline
建筑 block grammar
树木 / 车辆 / 行人采样
目标区域 trigger volume
碰撞 mesh / navmesh / semantic ID 自动生成
```

这比“让大模型直接生成场景坐标”靠谱得多。LLM 负责高层语义，UE PCG 负责低层几何和批量生成，VLM/仿真器负责验证。

---

### 路线 B：Agentic scene generation：LLM/VLM + 工具 + critic 闭环

这类是目前最前沿的一支，代表是 **SAGE** 和 **SceneAssistant**。

SAGE 的核心是：给一个 embodied task，例如“pick up a bowl and place it on the table”，agent 自动生成可用于机器人训练的仿真场景。它通过 MCP 调用 floor plan、asset placer/mover/remover、physics simulator 等工具，并引入 **visual critic** 和 **physics critic** 进行迭代修正。visual critic 检查语义和空间合理性，physics critic 用 Isaac Sim 检查稳定性和碰撞。([arXiv][4])

SceneAssistant 也类似，但更偏 open-vocabulary text-to-3D scene generation。它让 VLM 接收渲染反馈，然后通过 Scale、Rotate、FocusOn 等 action API 逐步修改场景，使空间关系更符合文本描述。它的关键点是 **visual feedback loop**，不是一次性生成。([arXiv][5])

这类方法对你的启发是：
你的场景生成器也应该有一个自检循环：

```text
生成初版场景
    ↓
VLM 检查：目标是否存在？空间关系是否正确？是否缺失关键物体？
    ↓
几何检查：是否重叠？是否悬空？是否越界？是否可通行？
    ↓
规划检查：是否存在可行航线？是否有足够 clearance？
    ↓
不合格则自动改场景
```

这就是“生成—验证—修复”闭环。没有这个闭环，LLM 场景生成很容易变成幻觉大舞台：看起来热闹，实际飞不了。

---

### 路线 C：程序化世界代码 / 可执行 world program

这个方向更像“让场景成为代码”，代表是 **SceneCode**。

SceneCode 把自然语言 prompt 编译成可执行的 indoor world program，而不是只输出不可编辑的 static mesh。它的对象是 part-wise Blender Python program，并导出 SDF 给物理仿真器使用；同时维护 scene-state registry，把 object request、可执行程序、渲染几何、仿真资产关联起来。([arXiv][6])

这对机器人很关键，因为机器人需要的不只是“椅子长得像椅子”，还需要知道：

```text
这个门能不能开？
抽屉的 joint 在哪里？
物体质量大概多少？
碰撞体是不是干净？
能不能被夹爪抓？
```

对你低空平台来说，也可以借鉴这个思想：
不要只保存 UE level，最好保存一份 **SceneSpec / TaskSpec / AnnotationSpec**，让场景可复现、可编辑、可批量变体生成。

建议你自己的中间格式这样设计：

```json
{
  "scene_id": "urban_block_003",
  "global_layout": {
    "roads": [],
    "buildings": [],
    "vegetation": [],
    "open_areas": []
  },
  "semantic_objects": [
    {
      "id": "building_12",
      "category": "office_building",
      "bbox_3d": [],
      "height": 18.2,
      "facade_type": "glass",
      "inspectable": true
    }
  ],
  "task_zones": [],
  "collision_layers": [],
  "spawn_points": [],
  "weather_lighting": {}
}
```

这个比纯 UE 工程资产更适合做 benchmark。

---

### 路线 D：真实场景重建 + 数字孪生 + LLM 标注

这个方向直接对标你想做的真实低空场景。代表是 **HUGE-Bench**。

HUGE-Bench 不是纯 PCG 造场景，而是用真实无人机采集数据，重建 **3DGS + Mesh 对齐数字孪生**。3DGS 用于高真实感渲染，mesh 用于碰撞、深度、物理查询和规划。它还用 top-down camera 渲染全局地图，让 LLM 在地图上定位 landmarks，人工审核后再利用深度反投影得到 3D landmark 位置。([arXiv][7])

这个流程非常值得你吸收：

```text
真实采集 / UE 场景
    ↓
3DGS 负责视觉真实感
Mesh / collision proxy 负责物理与规划
    ↓
top-down map 渲染
    ↓
LLM/VLM 辅助 landmark 定位
    ↓
人工轻量审核
    ↓
反投影到 3D 坐标
    ↓
生成任务轨迹和评测标签
```

注意重点：
**LLM 不是直接“知道 3D 坐标”，而是在渲染地图上做 2D/语义辅助，再用几何反投影得到 3D。**
这个很工程，也很靠谱。

---

## 3. LLM 辅助自然语言描述生成：不要只用模板句

目前生成自然语言指令有三条比较成熟的路。

### 第一类：scene tree + RAG 生成用户需求

**NavRAG** 自动构建 scene description tree，然后用 RAG-LLM 根据用户画像和场景上下文生成导航指令。它不是只描述轨迹，而是模拟不同用户在一天中会向导航 agent 提出的需求，生成更像真实用户的导航指令；它标注了 861 个 3D 场景上的 200 多万条导航指令。([arXiv][8])

你可以套到低空任务里：

```text
scene tree:
  campus
    building A
      entrance
      windows
      roof
    road B
    parking lot C
    tree area D

user persona:
  security inspector
  delivery operator
  emergency responder
  maintenance engineer

生成指令：
  “巡检左侧玻璃楼的外立面”
  “沿主路搜索停在路边的白色车辆”
  “飞到施工区上方，绕障碍物完成低空穿越”
```

这样比模板句“go to building_12”自然很多。

---

### 第二类：把地图编码进 LLM 指令生成

**MAPInstructor** 指出，很多 LLM 指令生成方法只喂文本描述，忽略了全局空间地图。因此它把 egocentric observations 投影到 3D voxel，再结合 topological map 做 prompt tuning，让 LLM 生成更可靠的导航描述；它还加入 landmark uncertainty assessment 来减轻 landmark 幻觉。([CVF开放获取][9])

你这里可以做成：

```text
输入给语言生成器：
  top-down semantic map
  target object mask
  relative direction
  route keypoints
  obstacle distribution
  altitude / safety constraints

输出：
  high-level instruction
  low-level step instruction
  target referring expression
  success condition
```

例如：

```text
High-level:
“巡检主路右侧的办公楼外立面。”

Low-level:
“先沿道路向前飞至十字路口，在右侧玻璃楼前下降到 8 米高度，
保持约 5 米距离沿外立面飞行，完成一圈后返回起始高度。”
```

这可以同时支持 VLA 高层任务和 VLN step-by-step 任务。

---

### 第三类：dense 3D grounding 数据

**3D-GRAND** 是 CVPR 2025 的大规模 3D-text 数据集，包含 40,087 个 household scenes 和 620 万条 densely-grounded scene-language instructions，用来减少 3D-LLM 的 hallucination，并提出 3D-POPE 专门评估 3D-LLM 幻觉。([CVF开放获取][10])

这对你很重要：
低空场景语言标注不能只有一句任务指令，最好有多层 grounding：

```text
对象级：
“white car” → car_012 → 3D bbox / mask

区域级：
“parking lot near the building” → region_003 polygon

关系级：
“building on the left of the road” → relation(building_04, left_of, road_01)

任务级：
“inspect the left building” → target=building_04, behavior=orbit/inspect
```

如果你要训练 VLM/VLA，让模型真正理解场景，dense grounding 比单条 instruction 更有用。

---

## 4. 自动标注：最靠谱的是“生成即标注 + 渲染即标注 + VLM 校验”

你自己的平台里，不建议完全依赖后处理视觉模型去猜标签。最好的办法是三层结合。

### 4.1 生成即标注

PCG 生成每个对象时就记录 metadata：

```json
{
  "instance_id": "car_032",
  "category": "vehicle.car.white_sedan",
  "asset_id": "fab_car_white_01",
  "transform": [x, y, z, roll, pitch, yaw],
  "bbox_3d": [...],
  "semantic_tags": ["vehicle", "traffic", "obstacle", "inspection_target"]
}
```

这可以直接导出：

```text
2D segmentation
instance mask
3D bbox
semantic map
object graph
collision layer
task affordance
```

这个比 SAM/YOLO 后处理准确得多。

---

### 4.2 渲染即标注

UE / Isaac 都可以用 render pass 输出：

```text
RGB
Depth
Normal
Optical Flow
Semantic ID
Instance ID
Object mask
Camera pose
UAV pose
Collision signal
```

你需要把每个 frame 的视觉输入和几何真值绑定起来：

```text
frame_t:
  rgb.png
  depth.exr
  semantic.png
  instance.png
  camera_pose.json
  drone_state.json
  visible_objects.json
  target_relation.json
```

这一步是 benchmark 可信度的根基。

---

### 4.3 VLM / LLM 校验标注

VLM 不负责主标注，而负责检查：

```text
图中是否真的有白车？
目标是否在左侧？
建筑是否可见？
道路是否被遮挡？
语言描述是否和图像/地图一致？
```

SAGE 这类工作已经说明 visual critic + physics critic 能显著提升生成场景的语义、视觉和物理有效性。SAGE 的评测里还专门统计 Realism、Functionality、Layout、Completeness、Collision Ratio、Stability Ratio 等指标。([arXiv][4])

所以你可以把 VLM 当“质检员”，不是“唯一真值来源”。这个角色定位很重要。

---

## 5. 自动建图与路径规划：LLM 不应该直接规划低层轨迹

这里要非常明确：

> **LLM 适合生成任务规格、子目标、约束和候选策略，不适合直接输出连续安全航迹。**

自动建图/规划建议分成三层：

```text
语义任务层：LLM
  “巡检左侧建筑”
  → target = building_04
  → behavior = facade_inspection
  → constraints = keep_distance, altitude_range, no_collision

几何规划层：A* / RRT* / PRM / frontier / coverage planner
  输入 ESDF / occupancy map / semantic map / no-fly zone
  输出 waypoints / reference trajectory

控制执行层：MPC / PID / low-level controller
  跟踪轨迹，处理动力学约束和安全距离
```

HUGE-Bench 就是这个思路：任务轨迹由 task-specific rules 生成，Traversal 任务用 RRT-based planner 做可行路径，并在 Isaac Sim 中采集 RGB、depth、pose、state 和 collision signals。([arXiv][7])

对你的低空平台，我建议建图结构用：

```text
Metric Layer:
  occupancy / ESDF / height map / collision mesh

Semantic Layer:
  object instances
  regions
  landmarks
  target affordances

Topological Layer:
  road graph
  corridor graph
  inspection graph
  viewpoint graph
  coverage cells

Language Layer:
  object aliases
  referring expressions
  task templates
  user demand descriptions
```

LLM 主要访问 Semantic + Topological + Language Layer，规划器访问 Metric + Semantic Layer。

---

## 6. 你可以建立的完整数据生成流水线

我建议你把系统叫成类似 **SceneOps / AirSceneOps / Low-altitude Data Factory**，结构如下：

```text
Step 1：任务本体定义
  landing / search / inspect / orbit / traverse / map / grasp / deliver

Step 2：LLM 生成 SceneSpec
  场景类型、道路、建筑、目标、障碍物、天气、任务区域

Step 3：PCG 生成 UE 场景
  spline road、建筑阵列、树木、车辆、标志物、动态障碍物

Step 4：自动语义标注
  instance ID、semantic ID、3D bbox、region polygon、scene graph

Step 5：VLM/physics critic 验证
  语义完整性、视觉合理性、碰撞、可通行、安全 clearance

Step 6：自动语言生成
  high-level command、step-by-step instruction、referring expression

Step 7：自动规划轨迹
  RRT/A*/coverage/orbit planner 生成 expert trajectories

Step 8：仿真执行采集
  RGB、depth、state、action、collision、visibility、target progress

Step 9：评测模型
  OpenVLA/π0/Diffusion/Planner/VLN 模型统一接口评测

Step 10：失败回流
  失败任务 → 生成 harder variants → 扩充训练集
```

这就是比较完整的“主动数据飞轮”。

---

# 7. 如何建立评估指标：建议分五层

你的评估不能只看最终模型 success rate。因为你要证明的是一个 **场景生成—标注—语言—规划—模型评测** 的平台，所以指标也要分层。

---

## 第一层：场景生成质量指标

评估“场景生成得对不对、能不能用”。

| 指标                        | 含义                        |
| ------------------------- | ------------------------- |
| Semantic Completeness     | prompt 要求的对象/区域/结构是否都出现   |
| Prompt-Scene Alignment    | 场景是否符合自然语言需求              |
| Object Placement Validity | 对象是否摆放合理，例如车在路上、树在绿化区     |
| Collision Ratio           | 物体之间是否重叠、穿模               |
| Stability Rate            | 物体经过物理仿真后是否稳定             |
| Navigable Area Ratio      | 可飞/可通行区域占比                |
| Path Existence Rate       | 随机任务点之间是否存在可行路径           |
| Diversity Score           | 不同 seed 生成的布局/对象/任务是否足够多样 |

SAGE 里就用了 Realism、Functionality、Layout、Completeness、collision ratio、stable object ratio 这一套。它还定义物体经过 120 个仿真 step 后，如果平移超过 0.2m 或旋转超过 8°，就算 unstable。([arXiv][4])

你可以把它改成低空版本：

```text
Building Placement Validity
Road Connectivity
Obstacle Density Validity
Flight Corridor Validity
No-fly Zone Respect
Takeoff/Landing Zone Validity
```

---

## 第二层：自动标注质量指标

评估“标签是不是准”。

| 指标                          | 含义                                           |
| --------------------------- | -------------------------------------------- |
| 2D Mask IoU                 | 自动 instance/semantic mask 和人工抽检 mask 的 IoU   |
| 3D BBox Error               | 自动 3D bbox 和人工/几何真值的误差                       |
| Landmark Localization Error | landmark 3D 坐标误差                             |
| Category Accuracy           | 类别标签是否正确                                     |
| Relation Accuracy           | left/right/in front of/near/inside 等空间关系是否正确 |
| Visibility Accuracy         | 系统判断的目标可见性是否与渲染结果一致                          |
| Grounding Accuracy          | 语言短语是否能正确对应 object/region                    |

3D-GRAND 的思路是做 dense 3D grounding，并用 3D-POPE 评估 3D-LLM 幻觉；这很适合你借鉴到“低空语言—目标—区域”的 grounding 评估里。([CVF开放获取][10])

你可以设置人工抽检集，例如每 1000 个自动样本抽 50 个：

```text
mask IoU > 0.8
3D center error < 0.5m
relation accuracy > 90%
target grounding accuracy > 95%
```

这样论文里会非常有说服力。

---

## 第三层：自然语言描述质量指标

评估“生成的语言是不是自然、准确、有任务价值”。

| 指标                           | 含义                      |
| ---------------------------- | ----------------------- |
| Instruction-Goal Consistency | 指令目标和真实目标是否一致           |
| Spatial Referring Accuracy   | “左侧/右侧/前方/靠近”等描述是否正确    |
| Ambiguity Rate               | 指令是否存在多个可能目标            |
| Route Faithfulness           | step-by-step 指令是否符合真实路径 |
| Language Diversity           | 同一任务是否有多种自然表达           |
| Human Preference / VLM Judge | 人或 VLM 判断语言是否自然可用       |
| Hallucinated Landmark Rate   | 指令中是否提到了场景不存在的 landmark |

MAPInstructor 特别强调要把地图上下文引入指令生成，并用 landmark uncertainty assessment 减少 landmark 幻觉；NavRAG 则用 scene tree + RAG 生成更贴近用户需求的导航指令。([CVF开放获取][9])

你的语言数据最好分三种：

```text
1. High-level command
   “巡检左侧建筑”

2. Mid-level instruction
   “飞到左侧玻璃楼前，下降并沿外立面绕行”

3. Low-level step instruction
   “向前飞 20 米，在路口右转，下降到 8 米……”
```

这样可以评测模型在不同指令粒度下的能力。

---

## 第四层：自动规划与轨迹质量指标

评估“规划器生成的 expert trajectory 是否合理”。

| 指标                      | 含义               |
| ----------------------- | ---------------- |
| Planning Success Rate   | 是否成功生成无碰撞轨迹      |
| Path Length Ratio       | 规划路径长度 / 理论最短路径  |
| Clearance Margin        | 路径到障碍物的最小安全距离    |
| Smoothness / Jerk       | 轨迹是否平滑           |
| Energy / Control Effort | 速度、加速度、转向变化是否过大  |
| Coverage Rate           | 巡检/测绘任务覆盖了多少目标区域 |
| Viewpoint Quality       | 目标是否在合适距离、角度、视野内 |
| Feasibility Rate        | 轨迹是否满足 UAV 动力学限制 |

HUGE-Bench 的 process-oriented evaluation 很值得借鉴，它不只看终点，还用 TCR 衡量过程轨迹覆盖，用 SR 衡量终点成功，用 CR 衡量碰撞，用 CSPL 综合成功、路径效率和无碰撞安全。([arXiv][7])

对你的低空巡检/操作任务，可以定义：

```text
Inspection Coverage Rate:
  被有效观察的目标表面积 / 目标总表面积

Target Visibility Rate:
  目标在相机视野内的帧数 / 总帧数

Safe Flight Rate:
  无碰撞且 clearance > 阈值的时间比例

Trajectory Process Completion:
  完成的语义子阶段数 / 总子阶段数
```

---

## 第五层：下游模型评测指标

最终还是要看 benchmark 能不能区分不同模型。

| 任务类型   | 推荐指标                                                                     |
| ------ | ------------------------------------------------------------------------ |
| 目标导航   | SR、SPL、Navigation Error、Collision Rate                                   |
| 目标搜索   | Success Rate、Search Time、Exploration Efficiency、First Detection Distance |
| 巡检     | Coverage Rate、TCR、Target Visibility、Safe Distance Violation              |
| 绕飞     | Radius Error、Height Error、Orbit Completion、Smoothness                    |
| 穿越避障   | SR、CR、CSPL、Minimum Clearance                                             |
| 空中操作   | Grasp/Contact Success、End-effector Error、Base Drift、Interaction Safety   |
| VLA 控制 | Action Latency、Closed-loop Success、Trajectory Similarity、Recovery Rate   |

如果你后面评测 OpenVLA、π0、Diffusion Policy、传统 planner、VLM+Planner，建议至少报：

```text
SR
Collision Rate
Trajectory Coverage Rate
Path Efficiency
Target Grounding Accuracy
Instruction Generalization
Unseen Scene Generalization
Latency
```

这样能说明你的平台不是只会“看谁飞到终点”，而是在评估语言理解、地图理解、过程执行、安全和泛化。

---

# 8. 我建议你自己的 benchmark 指标体系这样命名

可以做成一个总表，论文里很好看：

```text
Scene Generation Metrics
  SCS: Semantic Completion Score
  PVA: Physical Validity Accuracy
  NAR: Navigable Area Ratio
  PER: Path Existence Rate
  DIV: Scene Diversity

Annotation Metrics
  GA: Grounding Accuracy
  LE: Landmark Error
  RRA: Relation Reasoning Accuracy
  HLR: Hallucinated Landmark Rate

Language Metrics
  IGC: Instruction-Goal Consistency
  SRA: Spatial Reference Accuracy
  AR: Ambiguity Rate
  LD: Language Diversity

Trajectory Metrics
  PSR: Planning Success Rate
  CR: Collision Rate
  CLR: Clearance Rate
  SM: Smoothness
  TCR: Trajectory Coverage Rate

Policy Metrics
  SR: Success Rate
  SPL/CSPL
  OOD-SR: Unseen Scene/Object Success
  Latency
  Recovery Rate
```

其中最适合你低空平台拿来做“特色指标”的是：

```text
1. Semantic-Physical Consistency
   语言目标、语义地图、物理碰撞体是否一致

2. Viewpoint-aware Task Completion
   是否真的从合适视角观察/巡检目标

3. Collision-aware Process Completion
   是否完整执行任务过程且安全无碰撞

4. Active Data Utility
   用自动生成数据训练后，模型在 unseen 场景是否提升
```

最后这个 **Active Data Utility** 很关键。
你不只要证明“我能生成很多数据”，还要证明：

> 用我生成的数据训练，模型在未见场景、未见目标、未见语言上的性能真的提高。

SAGE 也做了类似思想：用生成场景和 action data 训练策略，并比较跨场景泛化能力。([arXiv][4])

---

## 9. 你项目里最推荐落地的技术路线

我建议你不要一上来追求“全自动、无限生成、完全无需人工”。更稳的是三阶段。

### Phase 1：PCG + metadata 自动标注

先做最稳的：

```text
UE PCG 生成道路/建筑/树/车/目标区域
每个对象自带 semantic id / instance id / bbox
自动导出 RGB/depth/mask/state/action
```

这一步可以快速形成可靠 benchmark 雏形。

---

### Phase 2：LLM 生成 SceneSpec + TaskSpec

把自然语言接进来：

```text
“生成一个城市街区，有两条交叉道路、五栋建筑、停车场和施工区域”
    ↓
LLM 输出 JSON SceneSpec
    ↓
UE PCG 执行
    ↓
Validator 检查
```

注意：**LLM 只输出结构化规格，不直接改 UE 工程。**

---

### Phase 3：critic 闭环 + 自动课程生成

最后再做高级版本：

```text
VLM critic 检查视觉/语义
Physics critic 检查碰撞/稳定性
Planner critic 检查路径可行性
Policy critic 检查模型失败样本
    ↓
自动生成更难但合理的新任务
```

这就是你真正可以包装成“主动数据飞轮”的地方。

---

## 10. 和现有工作的差异化怎么写

你可以这样对标：

| 工作                     | 主要贡献                                                               | 你的差异化空间                                              |
| ---------------------- | ------------------------------------------------------------------ | ---------------------------------------------------- |
| Holodeck               | 文本生成 embodied 3D 环境，GPT-4 生成空间约束并优化布局                              | 更强调低空 UAV、碰撞规划、轨迹采集和任务评测                             |
| UnrealLLM / AutoUE     | LLM + UE PCG 生成可编辑场景/游戏                                            | 更强调机器人数据闭环，而不是游戏内容生成                                 |
| SAGE                   | agentic scene generation + visual/physics critic + policy training | 扩展到户外低空、语义导航、巡检、操作任务                                 |
| SceneCode              | executable world programs + 可交互对象                                  | 你可以做低空 SceneSpec/TaskSpec，而非室内 articulated furniture |
| NavRAG / MAPInstructor | 自动生成导航语言指令                                                         | 你可以生成 UAV 高层任务语言 + 过程指令 + grounding 标签               |
| 3D-GRAND               | 大规模 3D-language dense grounding                                    | 你可以做 low-altitude 3D-language-action grounding       |
| HUGE-Bench             | 真实 3DGS-Mesh 数字孪生 + 高层 UAV 任务                                      | 你可以进一步加入程序化场景扩展、主动数据闭环和导航-操作一体化                      |

Holodeck 是较早的语言驱动 3D embodied environment 生成，利用 GPT-4 生成空间关系约束并从 Objaverse 放置资产；它证明了 LLM 可以把复杂 prompt 转成可用场景，但后续工作正在补它的物理验证、可交互性和仿真 ready 问题。([arXiv][11])

GenSim、RoboGen、GenSim2 这一支则说明，LLM 不只是能生成场景，还能生成任务、专家演示、reward/监督信号和多任务数据；GenSim 用 GPT-4 把 benchmark 扩展到 100+ 任务，RoboGen 形成 propose-generate-learn 循环，GenSim2 进一步用多模态/推理 LLM 生成 articulated 6-DoF 机器人任务和 demonstration data。([OpenReview][12])

所以你可以把自己的定位写成：

> 面向低空无人机导航—操作任务的 LLM-assisted procedural scene and task generation benchmark，统一支持场景程序化生成、语义标注、自然语言任务生成、路径规划、轨迹采集和闭环评测。

这个定位比“做一个无人机数据集”更强。

---

## 最后给你一个精炼版方案

你要做的不是单点工具，而是一条流水线：

```text
LLM：生成场景规格、任务规格、语言描述、子目标
UE PCG：生成道路、建筑、植被、车辆、障碍、目标区域
Asset Library：提供可控高质量资产
Renderer：输出 RGB/depth/semantic/instance/flow
Map Builder：生成 occupancy/ESDF/semantic map/scene graph
Planner：生成 expert trajectory 和 coverage/orbit/search path
Critic：检查语义、物理、路径、语言一致性
Benchmark：评测 VLA/VLN/planner 的成功率、安全性、过程完成度和泛化
```

一句话判断：

**现在最有价值的不是“让大模型自己造场景”，而是让大模型成为 PCG、资产库、语义地图、路径规划器和评测器之间的调度大脑。**
这条路线工程上最稳，也最适合你做低空主动数据平台。

[1]: https://arxiv.org/html/2604.26509v1 "3D Generation for Embodied AI and Robotic Simulation: A Survey"
[2]: https://aclanthology.org/2025.findings-acl.994/ "UnrealLLM: Towards Highly Controllable and Interactable 3D Scene Generation by LLM-powered Procedural Content Generation - ACL Anthology"
[3]: https://arxiv.org/html/2603.07106v1 "AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems"
[4]: https://arxiv.org/html/2602.10116v2 "SAGE: Scalable Agentic 3D Scene Generation for Embodied AI"
[5]: https://arxiv.org/html/2603.12238v1 "SceneAssistant: A Visual Feedback Agent for Open-Vocabulary 3D Scene Generation"
[6]: https://arxiv.org/html/2605.19587v1 "SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects"
[7]: https://arxiv.org/html/2603.19822v1 "HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks"
[8]: https://arxiv.org/html/2502.11142v1 "NavRAG: Generating User Demand Instructions for Embodied Navigation through Retrieval-Augmented LLM"
[9]: https://openaccess.thecvf.com/content/CVPR2025/html/Fan_Scene_Map-based_Prompt_Tuning_for_Navigation_Instruction_Generation_CVPR_2025_paper.html "CVPR 2025 Open Access Repository"
[10]: https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-GRAND_A_Million-Scale_Dataset_for_3D-LLMs_with_Better_Grounding_and_CVPR_2025_paper.html "CVPR 2025 Open Access Repository"
[11]: https://arxiv.org/abs/2312.09067 "[2312.09067] Holodeck: Language Guided Generation of 3D Embodied AI Environments"
[12]: https://openreview.net/forum?id=OI3RoHoWAN "GenSim: Generating Robotic Simulation Tasks via Large Language Models | OpenReview"
