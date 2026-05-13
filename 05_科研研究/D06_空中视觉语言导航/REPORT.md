# D06: 空中视觉语言导航 研究报告

> 最后更新：2026-04-20 | 成熟度：🟡中期（R843 引入 FineCog-Nav 后，D06 的增量主线从“verifier-first 恢复线还能否继续展开”进一步收束为：planner 内部是否值得显式拆成细粒度认知模块，以及这种模块化收益能否在不破坏 packet/verifier 主链的前提下，稳定转化为长航程 instruction adherence 与 memory-to-waypoint 净收益）
> 状态：🟡 推进中

## 一、研究背景与动机

视觉语言导航(VLN)让机器人根据自然语言指令在未知环境中导航到目标位置,是具身智能的核心能力。地面 VLN 已有大量工作(VLFM、NaVILA、ApexNav、SG-Nav 等),但**空中 VLN 研究极度匮乏**--现有方法假设 2D 平面运动、低速、稳定视角,无法处理无人机的 6-DoF 运动空间、高速飞行、俯仰视角剧变和动力学约束。

更重要的是,空中 VLN 天然可拓展为**导航+操作(Navigate-then-Manipulate)**,形成完整的空中具身智能闭环:先飞到语言描述的目标 → 再执行抓取/放置/检查等操作。这一路线在 Unified Aerial Grasping、AeroPlace-Flow 等工作中已初见端倪,但尚未与 VLN 框架系统结合。

## 二、相关工作梳理

### 2.1 地面视觉语言导航
- **VLFM (2024)**: Vision-Language Frontier Maps,用 VLM 语义相关性引导前沿探索,2D 地图
- **NaVILA (2025)**: 分层 VLA 导航,高层 VLM 推理 + 低层动作执行
- **ApexNav (2025)**: 自适应语义-几何探索,动态平衡探索vs利用
- **SG-Nav (2024)**: 场景图表示支持结构化导航推理
- **DRIVE-Nav (2026)**: 方向推理导航,空间推理能力增强
- **ABot-N0 (2026)**: 统一导航基础模型,多任务适配
- **局限**:全部假设 2D 平面运动,无动力学建模,无空中场景验证

## 最新扫描（R763）

- **arXiv:2604.13654** "Vision-and-Language Navigation for UAVs: Progress, Challenges, and a Research Roadmap" (April 9, 2026) — 系统综述空中VLN现状与LLM时代机遇，对标D06研究框架，直接指出3D空间表示和动力学感知是核心未解问题。
- **arXiv:2512.08639** "Aerial Vision-Language Navigation with a Unified..." — 统一框架空中VLN方法，已被引用2次，适合作为D06方法框架的baseline对比。

### 2.2 空中导航与VLA
- **OnFly (2026)**: 双 agent 无人机导航,感知/控制频次解耦,最接近空中 VLN
- **FineCog-Nav (2604.16298)**: 新增细粒度认知模块化 zero-shot UAV VLN 框架,把语言处理、感知、注意力、记忆、想象、推理、决策拆成 role-specific modules,并提供 AerialVLN-Fine 这种句级 instruction-trajectory 对齐 benchmark。它最值得保留的不是“再多几个模块”,而是把 **instruction adherence / memory usage / module I-O protocol** 直接抬成可诊断对象,非常适合作为 D06 后续比较 `planner 内部模块粒度` 是否真的值钱的强基线
- **UAV-Track VLA (2026)**: π0.5 架构空中追踪,temporal compression net
- **OpenFly (2502.18041)**: 不只是又一个 AVLN 数据集,而是把 **UE/GTA V/Google Earth/3DGS** 四类渲染源、自动轨迹生成、自动指令生成、以及 **OpenFly-Agent** 的关键帧感知 VLA 模型统一成完整平台。它对 D06 最重要的价值是补齐 **数据工厂 + benchmark + 轻量历史压缩基线** 这三层基础设施
- **See, Point, Fly**: 视觉指向飞行,简洁的指向-飞行范式
- **GoalSwarm**: 多无人机协同语义搜索
- **AirNav (2601.03707)**: 首个值得重点盯的**真实城市空中VLN benchmark**,不再依赖纯仿真场景,且给出 **AirVLN-R1 = SFT + RLFT** 的训练配方,能直接补上 D06 当前最缺的"真实数据评测闭环"
- **APEX (2602.00551)**: 提出 **Dynamic Spatio-Semantic Mapping + RL-based Action Decision + Target-guided Exploration** 的解耦式 explorer,把空中目标导航拆成可解释模块,明显比端到端黑盒更适合作为龙虾 GoalSearch 的工程参考
- **AutoFly (2602.09657)**: 面向开放世界 outdoor exploration 的 UAV VLA/VLN,核心不只是 pseudo-depth encoder,而是把任务切成 **目标驱动自主规划 + 连续避障 + 真实数据集成**。它很适合作为 end-to-end RGB(+pseudo-depth) 轻量基线,但对开放词汇目标搜索、显式地图记忆与重规划恢复的覆盖仍偏弱,因此更适合作为对照而非主骨架
- **2604.07705 / 2604.13654 Vision-Language Navigation for Aerial Robots: Towards the Era of LLMs** (April 9, 2026): 系统综述空中VLN现状与LLM时代机遇,直接指出3D空间表示和动力学感知是核心未解问题;arXiv:2604.13654为同期完整版roadmap,已作为D06框架直接对标
- **AerialVLA (2603.14363)**: 极简端到端 Vision-Language-Action 空中导航框架,直接从原始观测映射连续控制,适合作为我们"3D语义前沿图 + 动力学约束"方案的黑盒基线
- **Aerial VLN Unified (arXiv:2512.08639)**: 统一框架空中VLN方法,提供直接对照基准;验证了"语言引导+空中运动"联合学习的可行性
- **ViSA-Enhanced AVLN (2603.08007)**: 用 **structured visual prompting + image-plane spatial reasoning** 给 aerial VLN 补一层 training-free 前端推理增强。它最适合作为现有 explorer / frontier 主线的轻量插拔模块,帮助比较"只补视觉空间推理"到底能换来多少搜索稳定性提升
- **Fly0 (2602.15875)**: 将空中导航显式拆成 **MLLM语义 grounding → 深度投影到3D → 几何轨迹规划** 三阶段,强调 zero-shot、低延迟与视觉失联后的几何鲁棒性。它不是开放词汇搜索主骨架,但对 D06 很关键,因为它把“语义理解”和“几何执行”真正解耦,非常适合作为我们 C1/C2 的强对照基线。
- **Beyond Matching to Tiles (2603.22153)**: 把 D06 里常被忽略的 **global-local grounding / cross-view relocalization** 单独做强，联合回归绝对位置与航向角，适合作为长航程任务的全局重定位补件。
- **VLM-Nav (PLOS One 2026)**: 单目 RGB + DepthAnything-V2 + 通用 VLM 的低成本 mapless UAV 导航路线，适合作为 D06 的机载轻量 baseline，而不是主骨架。
- **局限**:OnFly 只做导航不做操作;UAV-Track 只做追踪不做目标搜索;AirNav 更偏 benchmark 与训练范式,方法创新有限;APEX 强在探索器拆分,但尚未自然延伸到导航后操作阶段;AutoFly/AerialVLA 虽更贴近端到端空中导航,但工程可解释性与约束显式性仍偏弱;Fly0 虽然把语义 grounding 与几何规划拆得很清楚,但更像“目标已可ground时的低延迟导航器”,对开放词汇长程搜索与显式3D前沿探索覆盖仍不足

### 2.3 空中操作(导航→操作拓展)
- **π-Make-It-Fly (2026)**: 发现视觉表征可迁移但控制动力学不可迁移,提出 Payload-Aware Guidance
- **Unified Aerial Grasping (2026)**: 语言指令+主动探索+6-DoF抓取端到端
- **AeroPlace-Flow (2026)**: 语言引导空中物体放置,Visual Foresight + Object Flow
- **局限**:操作类工作都假设已知目标大致位置,缺少系统的目标搜索/导航前端

### 2.4 现有工作的共同缺陷 / Gap
1. **没有完整的空中 VLN 框架**:地面方法无法迁移,空中方法零散不成体系
2. **2D 前沿地图无法处理 3D 空间探索**:空中场景需要 3D 体素/点云级前沿表示
3. **导航与操作割裂**:导航方法不考虑后续操作,操作方法不考虑前端搜索
4. **无动力学感知**:地面方法完全忽略运动约束,空中动力学是关键差异

## 三、我们的创新方向

### 3.1 核心创新点(Contribution)

1. **C1: 空中视觉语言前沿地图 (Aerial VL-Frontier Map)**
   - 将 VLFM 的 2D 前沿地图拓展为 3D 体素前沿图
   - 融合 VLM 语义相关性评分引导 3D 空间探索方向
   - 处理空中场景特有的垂直维度探索和视角变化
   - arXiv:2604.13654 roadmap **直接确认** 3D空间表示是核心未解问题，验证C1必要性

2. **C2: 动力学感知的导航策略 (Dynamics-Aware Navigation)**
   - 在前沿选择和路径规划中显式建模无人机能量/速度/安全约束
   - 将动力学约束作为探索代价函数的一部分,避免不可行路径
   - 参考 π-Make-It-Fly 的 Payload-Aware Guidance 思路
   - arXiv:2604.13654 roadmap **双重确认** 动力学感知是空中VLN的独立差异点

3. **C3: 导航-操作统一架构 (Navigate-then-Manipulate, NtM)**
   - 导航阶段积累的场景理解(3D 地图 + 目标位姿估计)直接传递给操作模块
   - 无缝模式切换机制:当目标进入操作范围,自动从导航模式转操作模式
   - 操作失败可回退重导航(闭环恢复)

### 3.2 拟定方法框架

```
输入:自然语言指令 "找到红色消防栓并拍照"
         │
    ┌────┴────┐
    │ VLM 语义  │  高层:理解目标语义 + 场景先验
    │ 目标解析  │  → 输出目标描述embedding + 探索优先级
    └────┬────┘
         │
    ┌────┴────────┐
    │ 3D VL-Frontier │  中层:维护3D体素前沿图
    │  Map + 探索策略 │  → VLM语义评分选择下一个前沿
    │  + 动力学约束   │  → 动力学代价过滤不可行前沿
    └────┬────────┘
         │
    ┌────┴────┐
    │ 飞行控制器 │  低层:轨迹生成 + PID/MPC 执行
    └────┬────┘
         │
    ┌────┴────┐  (拓展:目标进入操作范围时)
    │ 操作模块  │  → 精细接近 + 抓取/拍照/放置
    └─────────┘
```

#### 3.2.1 3D VL-Frontier Map 技术 instantiation

**体素地图构建**：
- 使用 Octomap 或 VoxelMap 维护 3D 体素占用网格（体素分辨率 0.1~0.2m）
- 每帧 RGB-D 或单目深度估计 → 3D 点云 → 体素融合
- 周期性从体素地图提取前沿（free 体素邻接 unknown 体素的面）

**VLM 语义评分**：
- 每年前沿 → 渲染该前沿对应的候选 view image
- VLM (Qwen-VL 或 GPT-4V) 输入: `[image, text: "Does this view contain '<target_description>'?"]`
- 取 VLM 输出 logits 或 binary response 作为语义相关性评分 $s_{sem}$

**动力学可行性评分** $s_{dyn}$：
- 对每个候选前沿，计算从当前位置飞往该点的：
  - 最大速度需求（怕 speed overshoot）
  - 最小转弯半径约束（怕 turning failure）
  - 高度变化率（怕 vertical jerk）
- $s_{dyn} = \text{sigmoid}(\frac{T_{flight} - T_{budget}}{T_{budget}})$，若超出时间预算则极低分

**前沿选择**：
- 综合评分: $S = \alpha \cdot s_{sem} + \beta \cdot s_{dyn}$，选 $S$ 最高的候选前沿
- $\alpha, \beta$ 通过 RL 或 Preference Learning 调整
- MotionScape (2604.07991) 提供 6-DoF 轨迹+语言标注数据，可用于训练 $s_{sem}$ 的 VLM scorer

### 3.2.2 planner-controller 接口契约（R812 新增）

> 来自本地回扫 **OnFly / HTNav / OpenFly / Ro-SLM** 的共同收束。D06 后续不能只写“高层 planner 输出一个子目标”，还要把 **输出的内容格式** 固定下来，否则 planner 收益、controller 收益、机载语言规划收益会继续混在一起。

**统一接口包 `Semantic Waypoint Packet`**：
- `goal_type`: `frontier / object-anchor / relocalize / manipulate-ready`
- `target_pose`: 目标 3D 位姿或局部航点（允许只有相对方位）
- `yaw_hint / altitude_band`: 朝向提示与允许高度带
- `semantic_confidence`: 语言-视觉接地置信度
- `progress_score`: 当前子目标完成度，供低频 monitoring agent 判断是否该重规划
- `safety_budget`: 允许最大速度、最小障碍距离、最大爬升/下降率
- `handoff_tag`: `search / approach / inspect / manipulate`，明确是否已进入 NtM 切换边界

**为什么它重要**：
1. **对齐 OnFly 的双频解耦**：高频 decision agent 与低频 monitoring agent 不再只共享自然语言，而是共享结构化子目标与进度状态。
2. **对齐 Ro-SLM 的机载规划器**：机载小模型不必直接输出底层动作，只需输出 `Semantic Waypoint Packet`，更容易蒸馏也更容易板载部署。
3. **对齐 E4 公平性实验**：固定 planner 输出包后，direct policy / safety shell / NMPC shell 才能真正做 shared-plan 公平对照。

**最小实现建议**：
- 第一版只保留 `goal_type + target_pose + semantic_confidence + safety_budget`
- 若第一版已能稳定支撑 E4，再逐步加入 `progress_score / handoff_tag`
- 所有 planner baseline（APEX / HTNav / Ro-SLM / SkyVLN-style）统一适配到这一接口，再进入 controller shell

### 3.2.3 planner 落地形态约束（R815 新增）

> 来自本轮本地回扫 **Ro-SLM / ORION / AerialVLN Survey** 的共同提醒。D06 不能只讨论“planner 放机载还是放云端”，还要明确 **planner 最终以什么形态落地**。当前至少存在两类实现：

1. **Packet-first**：planner 输出 `Semantic Waypoint Packet`，由 controller / safety shell 再翻译为低层执行。
2. **Code-first**：planner 直接输出可执行代码或动作脚本（Ro-SLM/ORION 风格），再由运行时执行。

**当前判断**：D06 主线应优先采用 **Packet-first**，把它作为 planner-controller 的统一中间层；**Code-first** 更适合作为 B9 工程型 baseline，而不是主叙事。

**原因**：
- Packet-first 更容易做 `shared-plan` 公平对照，便于隔离 planner 收益与 controller 收益。
- Packet-first 更适合 D06 的机载预算路由，云端和机载 planner 只需共享统一 packet schema。
- Code-first 的强项在于任务编排与 API 调用灵活性，但在空中连续控制里更容易把接口松散、执行时延和安全校验混在一起。

**因此**：后续 D06 的问题不该写成“机载小模型会不会写代码”，而应写成“在给定复杂度与预算下，planner 是不是至少能稳定输出可执行 packet；若不能，再考虑 code-generation 作为补充路径”。

### 3.2.4 verifier-first 准入门（R818 新增）

> 来自本轮本地回扫 **OnFly / Ro-SLM / ORION** 的共同收束。D06 现在不能只问“planner 输出了什么”，还要问 **这些输出在进入 controller 之前是否先过统一 verifier 准入门**。否则 `Packet-first`、`Code-first`、端到端 action generation 三类路线会在执行前混账，最后只剩一个总成功率，无法区分到底是规划错、接地错，还是执行链太松。

**统一准入门 `Verifier-Gated Execution`**：
1. **Semantic Validity Gate**：目标、方位、阶段标签是否与语言指令一致，避免 planner 在语义上已经跑偏。
2. **Geometric Executability Gate**：当前 packet / code 生成的子目标是否在局部地图、速度、转弯半径、爬升率约束下可飞。
3. **Budget Compliance Gate**：当前输出是否满足时延、显存、通信与机载能耗预算，超限则拒绝执行或升级路由。

**为什么它要单列**：
- **OnFly** 已证明 semantic-geometric verifier 不是附属技巧，而是零样本机载 VLN 能站住的关键层。
- **Ro-SLM** 说明机载小模型可以规划甚至生成代码，但不代表其输出天然适合直接执行，必须先做语义和可飞性验收。
- **ORION** 这类 end-to-end action generation 说明直接出动作在工程上很诱人，但若没有独立准入门，就很难判断失败来自语言理解、动作生成还是控制执行。

**D06 主线判断**：
- `planner -> verifier -> controller` 应作为默认执行链，而不是 `planner -> controller` 直通。
- `Code-first` 与 `end-to-end action generation` 可以作为 baseline，但都必须接入同一 verifier 准入门，才能做公平对照。
- 后续论文里真正要回答的不是“谁最会直接出动作”，而是“谁在统一准入门约束下，仍能稳定给出可执行且值得执行的子目标”。

### 3.2.6 verifier 触发后的恢复动作选择协议（R827 新增）

> 来自本轮本地回扫 **OnFly / HTNav / AutoFly / ORION** 的共同收束。D06 不该只停在 `Reject-and-Recover Ladder` 这个四级梯度，还要继续回答 **第一次 verifier 拒绝后到底该先修哪一层、何时必须停止本地硬顶**。否则系统虽然“有恢复机制”，但恢复动作选择仍然是拍脑袋。

**统一恢复动作选择器 `First-Reject Routing`**：
1. **语义错配（semantic mismatch）**：优先 `local retry`，仅重新采样 packet / 子目标，不先改 controller；若连续两次语义错配，则升级到 `shared-memory replan`。
2. **几何不可飞（geometric infeasibility）**：优先 `packet repair`，只修 `target_pose / yaw_hint / altitude_band / safety_budget`；若 repair 后仍 reject，再转 `shared-memory replan`。
3. **预算超限（budget violation）**：优先 `escalate` 到更低成本 planner 或云端路由，不重复同一重型规划链；这是资源约束问题，不应伪装成语义规划失败。
4. **连续拒绝（repeat reject）**：默认不再继续 `local retry`，直接进入 `shared-memory replan`；若重规划后仍 reject，则升级 `escalate`。

**为什么它重要**：
- **OnFly** 说明 semantic-geometric verifier 真正值钱的不是“能拒绝”，而是拒绝后还能快速回到可执行路径。
- **HTNav** 说明分层架构的优势在于能把失败精确定位到 `地图 / 航点 / 局部执行` 某一层，而不是所有失败都回退成整局重开。
- **AutoFly / ORION** 代表的端到端路线提醒我们，如果没有恢复动作选择协议，reject 之后系统通常只有两种极端：继续硬飞，或直接僵停。

**当前 D06 判断**：
- verifier 输出不应只包含 `pass / reject / route_action`，还应附带 `reject_reason` 与 `repeat_count`，否则恢复梯度无法稳定触发。
- 论文主结果不该只报“总成功率”或“reject 后恢复成功率”，还应单列 **Wrong-Escalation Rate / Repeat-Reject Rate / Recovery Cost Ratio**，判断系统是不是只是把失败更慢地重复了一遍。
- 若 `packet repair` 在几何 reject 场景下始终无增益，说明 D06 的 packet schema 仍不够承载几何约束，应优先修接口而不是继续调 planner。

### 3.2.8 verifier 触发后的阶段化首轮判线表（R830 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly / Ro-SLM / ORION** 的本地复核。D06 现在不只需要知道 `reject_reason` 和 `stage_tag`，还要把它们压成 **第一轮实验一出来就知道该收缩哪条线、何时停止本地硬顶** 的判线表。否则恢复协议虽然越来越完整，但依然缺少 go / no-go 依据。

| 观察信号 | 若出现该结果，优先判断 | 推荐动作 |
|---|---|---|
| `VPR` 很低且 `FER` 不降 | verifier 本身没有形成有效准入门，拒绝/放行边界都不稳 | 先回查 verifier 阈值与 packet schema，暂停放大 recovery 线 |
| `RRS` 提升但 `RCR` 很高 | 系统只是靠高代价补救把成功率堆上去 | recovery 仅保留 recommendation 或 search 阶段使用 |
| `WER` 很高 | 恢复协议过度保守，本地能修的任务被过早升级 | 收紧 escalate 条件，优先补 retry / repair |
| `RRR` 很高 | 当前恢复动作只是把失败往后拖，没有真正修到根因 | 优先检查 `reject_reason` 判定与 `packet repair` 是否承载错误 |
| `search` 阶段收益明显，但 `approach / manipulate-ready` 阶段恢复收益差 | recovery 甜区主要在早期搜索，后期高风险阶段不适合继续本地硬顶 | 主叙事收束为 stage-bounded recovery，不宣传通用恢复器 |
| `CDR` 或 `RHD` 明显恶化 | 恢复在破坏阶段一致性，NtM handoff 边界不稳 | 先修 `handoff_tag / progress_score / stage_tag`，暂停扩大恢复动作集 |

**当前主张**：D06 后续不该再用“reject 后恢复成功率又涨了”做主结论，而应优先回答 **恢复值不值得保留在线闭环、值不值得进入 approach / inspect / manipulate-ready 阶段**。这会让 D06 从“有恢复梯度”继续收束成“恢复该在哪一段启用”。

### 3.2.9 恢复线部署边界与阶段化保留原则（R830 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly** 的本地复核。D06 现在不该再把 recovery 写成一个默认总开关，而要明确 **恢复该保留在哪些阶段、哪些阶段宁愿停住或只给建议**。因为本地材料已经足够说明：搜索期失败和接近/交接前失败不是同一种风险。

**阶段化保留原则**：
1. **`search` 阶段**：允许完整 `retry / repair / replan / escalate` 梯度，这是 recovery 的主甜区。
2. **`approach` 阶段**：只保留 `repair / replan`，默认收紧 `retry`，避免在局部高风险机动里靠重复采样硬碰。
3. **`inspect` 阶段**：保留轻量 `retry` 与 `replan`，但要求更低的恢复债务；若恢复代价高于重新定位收益，优先建议停住重看。
4. **`manipulate-ready` 阶段**：默认不宣传通用在线恢复器，只保留 `hard-stop / recommendation-only / escalate`，除非后续实验明确证明 handoff 前恢复不会显著恶化阶段一致性。

**为什么要这样收束**：
- **OnFly** 证明 verifier-first 值钱，但它最稳的仍是搜索与导航主段，而不是高风险末端交接。
- **HTNav** 说明分层系统的价值，在于不同阶段能精确定位失败属于地图、航点还是局部执行；既然阶段不同，恢复策略就不该一刀切。
- **AutoFly** 代表的端到端路线提醒我们：当系统越接近连续局部控制区，错误恢复往往更像“重新打方向盘”，风险高于搜索阶段的语义重试。

**当前 D06 判断**：
- 后续论文里，recovery 主结果应默认写成 **stage-bounded recovery**，先证明它在 `search` 阶段值钱，再决定是否扩到 `approach / inspect`。
- 若实验显示 `approach / manipulate-ready` 阶段的恢复主要带来高 `Recovery Cost Ratio`、高 `Repeat-Reject Rate` 或高 `Cross-Stage Drift`，则主线应明确降级为 `recommendation-only` 或 `hard-stop with replan suggestion`。
- 这会让 D06 从“有恢复机制”继续收束成“恢复在哪一段值得在线保留”。

## 3.2.13 late-stage recovery 的首轮收缩优先级（R866 新增）

> 来自本轮对 `D06/README.md`、`experiments.md`、近 30 天 D06 收束记录与 QMD 回流结果的再次压缩。既然前面已经基本确认 **late-stage recovery 坏掉时先看 packet schema insufficiency vs handoff interface instability**，那首轮实验结果出来后还需要更进一步回答：**两者若都看起来可疑，先收缩哪一条，按什么顺序停预算？** 否则 D06 仍会在 `packet repair / handoff 修补 / recovery 动作扩容` 三条线上同时烧算力。

**默认收缩顺序固定为三段**：
1. **先看 packet schema 是否已经不够表达晚期几何需求**：若 `Packet Repair Gain` 持续接近 0，且 reject 长期集中在 `target_pose / yaw_hint / altitude_band`，优先冻结 recovery 扩容，先修 `Semantic Waypoint Packet`。
2. **再看 handoff interface 是否让阶段信息漂移**：若 `search` 阶段 recover 仍有效，但 `approach / inspect` 开始稳定出现高 `Cross-Stage Drift Rate / Recovery-to-Handoff Delay / Late-Stage Penalty Inflation`，则默认优先修 `handoff_tag / progress_score / stage_tag`，而不是继续加 retry / replan。
3. **只有前两者都不过主导位时**，才允许继续把预算投给 late-stage recovery 动作扩容；否则 recovery 只保留为 `search-bounded` 或 `recommendation-only`。

**为什么要把顺序写死**：
- 过去几轮已经确认 recovery 的主甜区在 `search`，所以晚期失效大概率不是“动作还不够多”，而是接口根本没把晚期任务状态表达清楚；
- 若不先冻结顺序，D06 很容易把 `packet schema 不足 / handoff 接口漂移 / recovery 本身无效` 三件事混在一起，最后既解释不了增益来源，也很难形成论文主叙事。

**当前 D06 默认 go/no-go 规则**：
- `PRG≈0 + 几何 reject 主导` → 先修 packet schema
- `search recover 有效 + late-stage CSDR/RHD/LPI 恶化` → 先修 handoff interface
- 只有两类接口问题都未主导时，late-stage recovery 才继续保留在线扩容预算


## 3.2.16 late-stage recovery no-go 后的主叙事默认收束规则（R870 新增）

> 来自本轮对 `D06/README.md`、`REPORT.md`、`experiments.md` 与本地已入库 **FineCog-Nav / OnFly / HTNav / AutoFly** 的复核，以及一次 QMD 回流确认：当前新问题已经不再是“先砍哪条 late-stage 线”，而是 **砍完之后论文默认该讲哪条主叙事**。如果这一步不写死，D06 很容易在宣布某条路线 no-go 之后，仍把 `packet / handoff / recovery` 三条都保留在标题竞争位。

**默认收束规则固定为三段**：
1. **若 `Packet Repair Gain≈0`、几何 reject 主导且 `Recovery Budget Efficiency` 不显著为正**：默认先把 `late-stage recovery action expansion` 判为 no-go，主叙事直接收成 **packet-first interface under-specification**。也就是说，问题优先解释为 `Semantic Waypoint Packet` 对晚期几何需求表达不足，而不是恢复器还不够强。
2. **若 `search` 阶段 recover 仍有效，但 `approach / inspect` 稳定出现高 `Cross-Stage Drift Rate / Recovery-to-Handoff Delay / Late-Stage Penalty Inflation`**：默认先把 `handoff 后 online recovery` 判为 no-go，主叙事收成 **stage-bounded recovery + handoff-first repair**。也就是说，D06 当前最值钱的仍是搜索期在线恢复，而不是把 recovery 硬推进晚期阶段。
3. **只有当前两类接口问题都不主导，且 `Net Stage Benefit` 与 `Recovery Budget Efficiency` 仍显著为正时**：late-stage recovery 才继续保留在线预算，并允许主叙事暂时维持 **late-stage online recovery**；否则禁止继续与 packet / handoff 并列抢标题。

**为什么这一层必须写死**：
- 前几轮已经把 `packet schema insufficiency / handoff interface instability / late-stage recovery expansion` 的优先级压清了；若不继续把 no-go 后的叙事收束写死，首轮实验后仍会出现“明明某条线已判 no-go，却继续在摘要和主表里留坑位”的问题。
- **OnFly / HTNav / AutoFly** 的共同提醒很一致：晚期失效往往更像接口承载或阶段边界没站稳，而不是简单缺一个更强恢复器。
- 这能让 D06 从“知道先否掉哪条线”继续推进到“知道否掉之后默认该怎样诚实收束论文故事”。

**当前 D06 默认收束映射**：
- `PRG≈0 + geometry-dominant reject + RBE 不显著为正` → **主叙事收成 packet-first interface under-specification**
- `search recover 有效 + late-stage CSDR/RHD/LPI 恶化` → **主叙事收成 stage-bounded recovery + handoff-first repair**
- 只有接口问题都不主导时 → **late-stage online recovery** 才保留主标题竞争位

## 3.2.15 late-stage recovery 的 no-go 默认顺序（R869 新增）

> 来自本轮对 `D06/README.md`、`REPORT.md`、`experiments.md` 与近 30 天 D06 收束记录的再次压缩。既然前面已经把 **packet schema insufficiency**、**handoff interface instability**、**late-stage recovery 动作扩容** 的优先级固定下来，这一轮继续往前压一层：**首轮结果出来后，默认先宣布哪类路线 no-go，避免三条线都留着“再试一轮”**。

**默认 no-go 顺序固定为：**
1. **先判 `late-stage recovery action expansion` 是否直接 no-go**：若 `Packet Repair Gain≈0`，且几何 reject 长期集中在 `target_pose / yaw_hint / altitude_band`，同时 `Recovery Budget Efficiency` 不显著为正，则直接把“继续扩 late-stage recovery 动作集”判为首个 no-go，先回去修 `Semantic Waypoint Packet`。
2. **再判 `handoff 后 online recovery` 是否 no-go**：若 `search` 阶段 recover 仍有效，但 `approach / inspect` 稳定出现高 `Cross-Stage Drift Rate / Recovery-to-Handoff Delay / Late-Stage Penalty Inflation`，则默认把 `handoff 后 online recovery` 判为 no-go，优先修 `handoff_tag / progress_score / stage_tag`，并把 recovery 收缩成 `search-bounded` 或 `recommendation-only`。
3. **只有前两者都未触发时**，late-stage recovery 才继续保留在线预算；否则禁止再把 packet、handoff、recovery 三条一起并行烧算力。

**当前 D06 默认判线：**
- `PRG≈0 + geometry-dominant reject + RBE 不显著为正` → **先把 late-stage recovery 扩容判 no-go**
- `search recover 有效 + late-stage CSDR/RHD/LPI 恶化` → **先把 handoff 后 online recovery 判 no-go**
- 只有接口问题都不主导时，late-stage recovery 才继续保留在线预算


> 来自本轮对 `D06/README.md`、`REPORT.md`、`experiments.md` 与本地已入库 **OnFly / HTNav** 的复核，以及一次因 CPU-only QMD 扩展后 SIGKILL 的失败回扫。既然 D06 已经把 late-stage 失效先压到 **packet schema insufficiency** 与 **handoff interface instability** 两类根因，那下一步就不能再模糊地说“后续再看哪条更值得修”，而要把 **首轮预算默认先砍哪条线** 固定下来。

**默认预算收缩顺序固定为三段**：
1. **先砍 late-stage recovery 动作扩容预算**：若 `Packet Repair Gain≈0`，且 reject 长期集中在 `target_pose / yaw_hint / altitude_band`，则默认不是 recovery 动作还不够，而是 `Semantic Waypoint Packet` 已经表达不出晚期几何需求；此时先停扩 recovery，优先修 packet schema。
2. **再砍 handoff 之后的盲目 retry/replan 预算**：若 `search` 阶段 recover 仍有效，但一进入 `approach / inspect` 就稳定出现高 `Cross-Stage Drift Rate / Recovery-to-Handoff Delay / Late-Stage Penalty Inflation`，则默认先修 `handoff_tag / progress_score / stage_tag`，而不是继续在 handoff 后堆 retry / replan。
3. **只有前两类接口问题都不主导时**，late-stage recovery 才保留在线扩容预算；否则它最多保留为 `search-bounded` 或 `recommendation-only`。

**为什么要把顺序写死**：
- **OnFly** 反复说明 verifier-first 真正稳定的甜区在搜索与导航主段，而不是末端高风险交接；
- **HTNav** 说明分层系统值钱的地方在于能把失败明确归因到地图、航点、局部执行某一层，因此晚期恢复失效时更该先查接口承载而不是先扩动作；
- 若不先冻结预算顺序，D06 很容易同时烧在 `packet repair / handoff 修补 / recovery 扩容` 三条线上，最后既解释不了净收益来源，也难以形成一条干净论文主叙事。

**当前默认 go/no-go 规则**：
- `PRG≈0 + 几何 reject 主导` → **先修 packet schema，停 recovery 扩容**
- `search recover 有效 + late-stage CSDR/RHD/LPI 恶化` → **先修 handoff interface，收紧 handoff 后 retry/replan**
- 只有两类接口问题都未主导时 → **late-stage recovery 才继续保留在线扩容预算**

**当前 D06 主线不变**：
- 主执行链仍是 `packet-first + verifier-first + stage-bounded recovery`
- FineCog-Nav 只作为解释“planner 为什么会在前 verifier 阶段掉线”的辅助对照位
- 后续若没有统一执行链上的 waypoint 质量证据，就不再继续扩大“细粒度认知模块化”在论文主贡献中的篇幅

### 3.2.10 verifier-first 恢复线的阶段化部署判据（R831 新增）

> 来自本轮对 **OnFly / HTNav / Ro-SLM** 的本地回扫。前几轮已经把 D06 的恢复线收成 `reject_reason + stage_tag` 双条件协议，但还缺最后一步：**什么结果出现时，恢复器可以保留在线；什么结果出现时，必须降级成 recommendation-only 或 hover-bounded**。这一步不再增加新方法，而是把 R827/R830 的判断压成 go / no-go 标尺。

**阶段化部署判据**：
1. **search 阶段**：若 `Reject Recovery Success` 明显高于 `hard-stop`，且 `Wrong-Escalation Rate / Repeat-Reject Rate / Recovery Cost Ratio` 三项都未明显恶化，则保留完整在线恢复链。
2. **approach 阶段**：必须额外满足 `Cross-Stage Drift Rate` 与 `Recovery-to-Handoff Delay` 不明显恶化；否则 recovery 仅保留 `repair / replan`，不保留自由 retry。
3. **inspect 阶段**：若恢复收益主要来自轻量语义重试，而几何 repair 增益弱，则默认收缩成 `recommendation-only + bounded retry`，避免在目标确认窗口里反复抖动。
4. **manipulate-ready 阶段**：除非实验明确证明 `Recovery Cost Ratio` 可控且 `Cross-Stage Drift Rate` 不上升，否则默认不保留通用在线恢复，只保留 `hard-stop / escalate / recommendation-only`。

**为什么这一步关键**：
- **OnFly** 证明 verifier-first 值钱，但它最稳的是搜索与导航主段，而不是高风险末端交接。
- **HTNav** 说明分层系统的真实优势，是把失败定位到地图、航点、局部执行哪一层；既然失败层不同，部署边界也不该一刀切。
- **Ro-SLM** 提醒机载 planner 很可能让 `search` 阶段恢复足够便宜，但并不自动意味着接近/交接阶段也适合继续本地硬顶。

**当前 D06 判断**：
- 后续主结果优先写成 **stage-bounded online recovery**，先证明 `search` 值钱，再按证据决定要不要放宽到 `approach / inspect`。
- 若某阶段 recovery 的主要收益只是减少人工接管而不是提升净任务收益，必须同时检查它是否在偷偷增大 `Recovery Cost Ratio` 与 handoff 漂移。
- 这让 D06 从“恢复该在哪一段启用”继续收束到“恢复在哪一段真的值得上线”。

### 3.2.11 verifier-first 恢复线的首轮资源冻结与主叙事收束规则（R840 新增）

> 来自本轮对 **OnFly / UAV-VLN Survey / OnFly 笔记** 的本地回扫。D06 现在不再缺“恢复机制有没有”或“恢复在哪一段启用”，真正缺的是 **首轮实验一出来后，哪条恢复线值得继续吃算力，哪条必须冻结，论文主叙事该怎么收**。如果没有这层规则，后续很容易把 search 甜区、approach 高风险段和 manipulate-ready 的 recommendation-only 模式一起往前推，最后叙事发散。

**首轮资源冻结规则**：
1. **若 `search` 阶段的 `RRS` 提升明显，且 `RCR / WER / RRR` 都未恶化**：保留完整 `retry / repair / replan / escalate` 链，作为主线继续推进。
2. **若 `approach` 阶段只有 `repair / replan` 有边际收益，而自由 `retry` 明显拉高 `CDR / RHD`**：冻结 `approach` 阶段的 retry 线，只保留 bounded repair / replan。
3. **若 `inspect` 阶段收益主要来自语义重试，但净收益被恢复时延吃掉**：降级成 `recommendation-only + bounded retry`，不再继续投入 packet repair 扩展。
4. **若 `manipulate-ready` 阶段仍表现为高 `RCR`、高 `RRR` 或高 `CDR`**：默认冻结在线恢复线，主叙事明确收成 `hard-stop / recommendation-only before handoff`，不再宣传通用恢复器。

**主叙事收束规则**：
- **最好结果**：若 search 明显值钱、approach 有限值钱、inspect/manipulate-ready 需严格收缩，则主叙事写成 **stage-bounded verifier-first recovery for aerial VLN**。
- **中等结果**：若只有 search 阶段稳定获益，则主叙事收成 **search-phase online recovery + downstream conservative handoff**。
- **较弱结果**：若 recovery 总体收益主要来自 recommendation 而非在线修复，则主叙事降级为 **verifier-first gating + structured recovery recommendation**。

**为什么这一步值钱**：
- 它把 D06 从“恢复器越来越完整”推进到“知道哪一段配做主贡献、哪一段只能做安全壳层”。
- 它直接防止后续把高风险阶段的有限收益硬包装成通用在线恢复能力。
- 它也让 D06 与 D01/D07 的最新收束方式对齐：首轮结果出来后先冻结叙事边界，再决定要不要继续扩实验线。

### 3.2.11 verifier-first 恢复线的 packet-schema 失效判据与回修优先级（R843 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly / ORION** 的本地复核，以及 QMD 对 `aerial VLN packet verifier stage-bounded recovery handoff` 的回流结果。当前 D06 已经把 `verifier → reject_reason → stage_tag → recovery action` 链写得很全，真正还缺的是：**什么时候应承认不是 recovery 不够强，而是 `Semantic Waypoint Packet` 本身承载不了当前几何/阶段信息，必须先回修接口**。否则后续很容易把 packet 表达力不足误诊成 planner 退化或恢复器太弱。

**packet schema 失效判据**：
1. **几何 reject 长期集中在同一类 `target_pose / yaw_hint / altitude_band` 组合**，且 `packet repair` 多轮后仍高 `RRR`：优先判断为 packet 几何表达不足，而不是 planner 不会找路。
2. **`search` 阶段 recover 有效，但一进入 `approach / inspect` 就明显恶化 `CDR / RHD`**：优先判断 `handoff_tag / progress_score` 粒度不够，阶段边界没被 packet 稳定编码。
3. **verifier 的 semantic gate 能稳定工作，但 geometric gate 长期高 reject**：优先回修 `safety_budget / target_pose` 的约束字段，而不是继续调语义 scorer。
4. **D01 supervisor 对同一 packet 经常给出 `hover-bounded recovery / stop-and-escalate`，而本地 planner 仍倾向放行**：优先判断 packet 缺少足够的风险状态字段，应补 `failure_state` 或更细的 route hint，而不是再堆本地 retry。

**回修优先级**：
- **P1**：先修 `target_pose + yaw_hint + altitude_band`，确保 packet 对局部可飞性有最小表达力。
- **P2**：再修 `handoff_tag + progress_score`，确保 `search → approach → inspect → manipulate-ready` 的阶段切换不是隐式猜测。
- **P3**：最后才扩 `semantic_confidence / safety_budget` 的细粒度定义；若前两层没站住，继续堆置信度字段只会增加解释噪音。

**当前 D06 判断**：
- 后续实验里，若 `packet repair` 在几何 reject 上连续无增益，默认先回修 packet schema，而不是继续扩 planner baseline。
- 若 recovery 收益只在 `search` 阶段成立，而 `approach+` 阶段总被 handoff 边界卡死，主结论应优先写成 **packet-first interface still under-specified for late-stage execution**，这是比“恢复器还不够强”更诚实也更可行动的结论。
- 这一步把 D06 从“恢复该在哪一段启用”继续推进到“如果恢复在某段始终不起效，该先修接口还是先修策略”的更硬判线。

### 3.2.11 verifier-first 恢复线的 packet-schema 失效判据与回修优先级（R843 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly / ORION** 的本地复核，以及 QMD 对 `aerial VLN packet verifier stage-bounded recovery handoff` 的回流结果。当前 D06 已经把 `verifier → reject_reason → stage_tag → recovery action` 链写得很全，真正还缺的是：**什么时候应承认不是 recovery 不够强，而是 `Semantic Waypoint Packet` 本身承载不了当前几何/阶段信息，必须先回修接口**。否则后续很容易把 packet 表达力不足误诊成 planner 退化或恢复器太弱。

**packet schema 失效判据**：
1. **几何 reject 长期集中在同一类 `target_pose / yaw_hint / altitude_band` 组合**，且 `packet repair` 多轮后仍高 `RRR`：优先判断为 packet 几何表达不足，而不是 planner 不会找路。
2. **`search` 阶段 recover 有效，但一进入 `approach / inspect` 就明显恶化 `CDR / RHD`**：优先判断 `handoff_tag / progress_score` 粒度不够，阶段边界没被 packet 稳定编码。
3. **verifier 的 semantic gate 能稳定工作，但 geometric gate 长期高 reject**：优先回修 `safety_budget / target_pose` 的约束字段，而不是继续调语义 scorer。
4. **D01 supervisor 对同一 packet 经常给出 `hover-bounded recovery / stop-and-escalate`，而本地 planner 仍倾向放行**：优先判断 packet 缺少足够的风险状态字段，应补 `failure_state` 或更细的 route hint，而不是再堆本地 retry。

**回修优先级**：
- **P1**：先修 `target_pose + yaw_hint + altitude_band`，确保 packet 对局部可飞性有最小表达力。
- **P2**：再修 `handoff_tag + progress_score`，确保 `search → approach → inspect → manipulate-ready` 的阶段切换不是隐式猜测。
- **P3**：最后才扩 `semantic_confidence / safety_budget` 的细粒度定义；若前两层没站住，继续堆置信度字段只会增加解释噪音。

**当前 D06 判断**：
- 后续实验里，若 `packet repair` 在几何 reject 上连续无增益，默认先回修 packet schema，而不是继续扩 planner baseline。
- 若 recovery 收益只在 `search` 阶段成立，而 `approach+` 阶段总被 handoff 边界卡死，主结论应优先写成 **packet-first interface still under-specified for late-stage execution**，这是比“恢复器还不够强”更诚实也更可行动的结论。
- 这一步把 D06 从“恢复该在哪一段启用”继续推进到“如果恢复在某段始终不起效，该先修接口还是先修策略”的更硬判线。

### 3.2.12 细粒度认知模块化 planner 的升级门槛（R850 新增）

> 来自本轮对 **FineCog-Nav / OnFly / GET / UAV-VLN Survey** 的本地回扫，以及 arXiv 对 `aerial VLN` 新结果的补检。当前 D06 已经确认 FineCog-Nav 值得保留，但还缺最后一步：**什么情况下它真的足以改写 D06 主叙事，什么情况下只能作为 supporting baseline**。否则后续很容易把“更多模块 + 更细 benchmark”误写成方法主链升级。

**升级门槛**：
1. **必须同时改善 `instruction adherence` 与 `memory-hit-to-waypoint conversion`**，不能只在句级 benchmark 或单一长程 SR 上占优。
2. **`Semantic Waypoint Packet` 兼容性不能明显恶化**，否则说明收益只是 planner 内部更花哨，而没有稳定转成 D06 可复用的 packet-first 输出。
3. **module latency budget 必须可控**，若时延主要靠堆模块换来，默认不允许升格为机载/在线主线。
4. **若收益主要来自更细 benchmark 标注或更强 prompt scaffolding**，而非真实改善 packet-compatible planning，则只记为 supporting baseline，不改写 `packet-first + verifier-first` 主链。

**当前 D06 判断**：
- FineCog-Nav 现在最适合做 **强对照的模块化 planner baseline**，而不是直接上升为 D06 主方法。
- 只有当它在统一 packet/verifier 协议下仍稳定带来净收益，才允许把“planner 内部模块粒度”升格为正式贡献点。
- 这会让 D06 从“知道 FineCog-Nav 值得盯”继续收束成“知道它什么时候真的值到足以改写主叙事”。

### 3.2.13 verifier-first 恢复线的最小可验证实验放行表（R840 新增）

| 实验位 | 目标 | 放行条件 | 不通过时动作 |
|---|---|---|---|
| **SC13 Search-stage recovery smoke test** | 验证 search 阶段 recovery 是否真实提升净收益 | `RRS` 提升且 `RCR / WER / RRR` 不恶化 | 冻结 recovery 主线，仅保留 verifier gating |
| **SC14 Approach-stage bounded repair** | 验证 approach 阶段是否只适合 bounded repair / replan | `repair` 有效且 `CDR / RHD` 可控 | approach 阶段降级为 hard-stop + replan suggestion |
| **SC15 Inspect-stage recommendation check** | 判断 inspect 阶段在线修复是否值得保留 | recommendation-only 不显著差于在线 repair | inspect 阶段不再继续扩恢复动作 |
| **SC16 Handoff-boundary safety check** | 检查 manipulate-ready 前 recovery 是否破坏 NtM handoff | `CDR` 与 `RHD` 不恶化 | handoff 前只保留 recommendation-only / hard-stop |

> 来自本轮对 **OnFly / HTNav / AutoFly / Ro-SLM** 与现有 `experiments.md` 的本地复核。D06 现在已经把 `verifier → reject_reason → stage_tag → recovery action` 这条线写得很全了，但还缺最后一步：**首轮结果出来后，哪些能力继续保留在线预算，哪些能力只保留成 supporting evidence**。这一步不是再加方法，而是避免 recovery 线无限膨胀。

| 首轮主要读数 | 优先结论 | 论文主叙事 | 资源动作 |
|---|---|---|---|
| `FER` 明显下降，且 `Gate Latency Overhead` 可控，但 recovery 额外增益弱 | verifier 已解释主要收益，恢复器不是主增益来源 | **verifier-first execution** | 冻结大部分 recovery 扩展，只保留基础 retry / replan |
| `WER / RRR` 显著下降，而 `FER` 改善有限 | 真正值钱的是 reject 后的 reason-aware routing | **reason-aware reject routing** | 保留 `reject_reason → action` 主线，压缩其他接口花样 |
| 收益主要集中在 `search` 阶段，`approach+` 阶段 `RCR / CSDR / RHD` 明显恶化 | recovery 甜区只在搜索期，后期不值得硬保留在线 | **stage-bounded online recovery** | 仅给 `search` 留在线预算，后期默认 recommendation-only / hard-stop |
| `D01 supervisor` 明显降低 `misroute / late stop`，而本地 verifier 收益趋于饱和 | 跨方向接口复用比继续细抠本地恢复更值钱 | **interface-first packet supervision** | 优先保留 D01→D06 接口，冻结部分本地恢复分支 |
| 各条子线都有一点收益，但指标重复记账严重 | 叙事过宽，首轮还没形成单主线 | **先收束不扩展** | 强制只留一条主叙事，其余降级为 supporting evidence |

**当前 D06 判断**：
1. 首轮后 **只允许保留一条主叙事**，其余一律降级为 supporting evidence，避免 D06 报告继续横向膨胀。
2. 若收益主要来自 verifier 准入门，就不要再把 packet repair / late-stage recovery 写成同级创新点。
3. 若收益主要来自 `search` 阶段恢复，就明确承认 D06 当前的 recovery 只是 **导航期在线恢复器**，不是通用 NtM 恢复框架。
4. 若 D01 接口复用收益最高，D06 后续应把主线从“本地 planner 怎么恢复”转向“packet 执行前如何做跨方向安全监督”。

### 3.2.12 首轮后 D06 统一叙事选择规则（R838 新增）

> 目的：把 D06 当前已经形成的四条候选主叙事压成一张选择规则表，避免首轮实验后继续同时保留 `verifier / routing / stage-bounded recovery / D01 supervisor` 四条并列贡献。

| 候选主叙事 | 何时选它 | 不该选它的信号 |
|---|---|---|
| **verifier-first execution** | `FER` 降得最稳，且时延开销小 | 主要收益其实来自 reject 后路由或 D01 supervisor |
| **reason-aware reject routing** | `WER / RRR` 改善最大，且恢复代价可控 | reject_reason 不稳定，repair 长期无效 |
| **stage-bounded online recovery** | search 阶段净收益最明显，晚期恢复风险高 | 各阶段收益分布平均，或 recommendation-only 几乎一样好 |
| **interface-first packet supervision** | D01 supervisor 明显降低危险放行、误路由或 late stop | packet schema 还不稳定，跨方向接口暂时只增加复杂度 |

**主规则**：
- 一轮实验后，优先保留 **解释力最高且最省预算** 的那条主叙事。
- 其余叙事只在第二节相关工作或第四节 supporting evidence 中出现，不再并列写成贡献点。
- 这样 D06 最终才能从“功能很多”收束成“论文讲得清楚”。

### 3.2.14 D01 执行前 supervisor 接口（R839 新增）

> 来自本轮对 D01 / D06 本地材料的联合回扫。D06 现在的 `planner→verifier→controller` 已经足够清楚，但还缺一个更保守、可复用的 **执行前 packet supervisor**：它不负责找路，只负责在 packet 即将进入执行链前，判断“该继续、该停悬、该回退还是该升级人工/云端”。这正好对应 D01 当前最现实的跨方向价值。

**最小接口绑定**：
- 输入：`Semantic Waypoint Packet`
- D01 输出：`rank_score + failure_state(F1/F2) + route_action + hover-bounded recovery`
- 执行位置：`planner → D01 supervisor → verifier/controller`

**为什么这一步关键**：
1. **隔离规划收益与执行安全收益**：D01 不接管 D06 planner，因此若收益出现，就能更清楚归因到执行前预筛与路由，而不是“又换了个更会找路的 planner”。
2. **与 D06 当前主线完全兼容**：`rank_score / F1-F2 / route_action` 正好补在 verifier-first 执行链前，不破坏现有 packet-first / code-first / end-to-end baseline 的公平比较。
3. **把 recovery 边界压实**：D01 的 recovery 只在 `hover / re-anchor` 窗口允许进入 D06，避免恢复器一上来就越界进入 `approach / manipulate-ready`。

**当前 D06 判断**：
- 若 D01 supervisor 能显著降低 `late stop / misroute / danger-action 漏放率`，则 D06 可把它正式吸收为 **execution supervisor baseline**。
- 若收益只出现在停悬窗口，则主叙事明确写成 **hover-bounded packet supervision**，不包装成通用导航恢复器。
- 若收益不明显，则 D06 保持本地 verifier-first 主线，不强行引入跨方向 supervisor。

### 3.2.14 细粒度认知模块化 planner 的首轮资源冻结与叙事降级规则（R854 新增）

> 来自本轮对 **FineCog-Nav / OnFly / HTNav / UAV-VLN Survey** 的本地回扫，以及 arXiv 对 `FineCog-Nav (2604.16298)` 的补检。D06 现在已经把 FineCog-Nav 的**升级门槛**写清了，但还缺最后一步：**首轮实验一出来后，什么时候它该升格为主线，什么时候应主动降级成 diagnostic baseline**。否则后续很容易把“模块更多、解释更细”误写成真正的方法主收益。

| 首轮主要读数 | 优先结论 | D06 主叙事 | 资源动作 |
|---|---|---|---|
| `instruction adherence / memory-hit-to-waypoint conversion / pre-verifier semantic mismatch rate` 三项都显著改善，且 packet 兼容与时延可控 | 模块化 planner 真正改善了 packet-compatible planning | **fine-grained cognitive planner as packet-compatible upgrade** | 允许保留为正式 planner 主对照，继续投入模块粒度实验 |
| adherence 提升明显，但 `semantic mismatch → reject` 没明显下降 | 收益主要是解释更细，不是执行前质量更强 | **diagnostic modular planner** | 降级为诊断型 baseline，不改写 packet-first 主链 |
| sentence-level benchmark 表现更好，但 `memory-hit-to-waypoint conversion` 与净 waypoint 质量无提升 | 更细 benchmark / prompt scaffolding 在抬分，而非真实改善长程规划 | **benchmark-sensitive supporting baseline** | 冻结额外模块扩展，保留作 supporting evidence |
| packet 兼容性差，或 module latency budget 明显超限 | planner 内部更复杂，但无法稳定接进现有执行链 | **packet-first still dominant** | 优先修 structured I/O protocol，不继续扩模块数 |
| 模块化收益只在 search 阶段成立，approach+ 不带来额外净收益 | 模块粒度更适合高层语义规划，不适合晚期连续执行区 | **search-phase cognitive planning only** | 只保留 search-stage 分析，不把它包装成全阶段主线 |

**冻结规则**：
1. FineCog-Nav 只有在 **统一 `Semantic Waypoint Packet + verifier-first` 协议下** 仍带来净收益，才允许升格为正式主线候选。
2. 若收益主要来自 `AerialVLN-Fine` 这类更细标注 benchmark，或来自 role-specific prompt scaffolding，而不是 packet-compatible 规划质量提升，则默认降级为 **diagnostic / supporting baseline**。
3. 若模块化收益与现有 verifier / reject routing 收益高度重叠，优先保留解释力更强、预算更省的那条叙事，不并列写成贡献点。
4. D06 后续对 FineCog-Nav 的默认态度应是：**先证明它能改进执行前 packet 质量，再讨论它值不值得改写 planner 主链。**

### 3.2.15 verifier-first 恢复线的首轮资源冻结表（R839 新增）

> 目的：D06 现在已经有 `packet schema / verifier / reject routing / stage-bounded recovery / D01 interface supervisor` 多条可写线，首轮实验后必须冻结主叙事，不能把每一条都塞进主摘要。

| 首轮主要读数 | 优先结论 | D06 主叙事 | 资源动作 |
|---|---|---|---|
| `planner→verifier→controller` 已显著降 FER，恢复增益弱 | verifier 准入门已足够解释收益 | **verifier-first execution** | recovery 冻结为 supporting evidence |
| `First-Reject Routing` 明显降 WER/RRR | 恢复动作选择协议最值钱 | **reason-aware recovery routing** | 继续投 packet schema 与 reject_reason |
| 恢复收益主要集中在 `search` 阶段 | 阶段边界比通用恢复更关键 | **stage-bounded online recovery** | approach+ 阶段恢复冻结 |
| `D01 supervisor` 显著降 misroute / late stop | 跨方向执行前接口成立 | **interface-first packet supervision** | 保留 D01 接口，压缩通用 recovery 叙事 |
| recommendation-only 与 online 差距很小 | 在线恢复不值预算 | **verifier + recommendation** | recovery 预算转回 verifier / packet / handoff 稳定性 |

**冻结规则**：
1. 首轮后只允许一条主叙事进入摘要和主表，其余全部降级为 supporting evidence。
2. 若收益主要来自 `search` 阶段，必须明确写成 **stage-bounded**，不再宣传“全阶段恢复器”。
3. 若 `D01 supervisor` 与 `local recovery` 同时有效，优先保留更可复用、边界更清楚的 **packet supervision**。
4. 任何明显提高 `Recovery Cost Ratio / Cross-Stage Drift / Wrong-Escalation Rate` 的子线，默认不占主贡献位。

### 3.2.13 verifier-first 恢复线的首轮资源冻结表（R836 新增）

> 目的：D06 现在已经把 `packet schema / verifier gate / reject routing / stage-bounded recovery` 都铺开了，再继续同时扩 planner、controller、recovery 很容易把首轮实验做散。这一节把 **阶段化部署判据** 进一步压成 **资源冻结 + 论文主叙事映射**，保证第一轮结果出来后就能立刻知道 recovery 线该不该继续烧预算。

| 首轮主要结果 | 优先结论 | 论文主叙事 | 资源动作 |
|---|---|---|---|
| `VPR` 提升最稳，而 recovery 额外收益弱 | verifier 准入门已解释主要收益 | **verifier-gated packet execution** | recovery 线降为 supporting evidence |
| recovery 仅在 `search` 阶段明显有效 | 恢复甜区只在搜索期 | **stage-bounded online recovery (search-only)** | 只保留 search 阶段预算，不扩 approach / manipulate-ready |
| `RRS↑`，但 `RCR`、`RRR` 偏高 | 系统在用高代价重复补救堆成功率 | **recommendation-only / bounded recovery** | 停止扩大在线恢复，优先修 reject routing |
| `WER` 高、`FER` 低 | 升级过度保守，很多本地可修问题被过早放弃 | **local retry/repair first** | 优先优化 packet repair 与 escalate 阈值 |
| recovery 扩到 `approach / manipulate-ready` 后 `CDR/RHD` 恶化 | 高风险阶段恢复在破坏 handoff 边界 | **hard-stop + replan suggestion** | 冻结后期阶段恢复，不再加动作种类 |
| `VPR`、`RRS` 都稳，且 `RCR/RRR/WER` 可控 | verifier 与恢复线都具备部署价值 | **verifier-first stage-bounded recovery** | 保留 recovery 主线，减少新增 planner baseline 扩张 |

**冻结原则**：
1. D06 后续不再接受“planner / controller / recovery 一起再加一轮”的并行推进；必须先按这张表决定 recovery 是否值得继续吃主预算。
2. 若 recovery 的主要收益只发生在 `search`，论文主叙事就明确写成 **search-bounded recovery**，而不是包装成通用在线恢复器。
3. 对 D06 而言，`CDR / RHD / WER` 的优先级高于“恢复成功率再涨一点”；只要跨阶段漂移或误升级明显，就不允许把 recovery 扩进高风险末端阶段。
4. 只有在 verifier 准入门稳定、reject routing 可解释、阶段边界不过度漂移时，恢复线才值得继续作为投稿主贡献推进。


> R827-R832 已经把 D06 的 verifier-first 恢复线压成 `reject_reason × stage_tag` 的阶段化协议；这一轮继续补上 **首轮实验一出来就能直接写进论文主叙事** 的结论表。目标不是再加一个指标，而是把“search 阶段值得保留、approach 以后要收紧”压成可复用的结论模板，避免每轮都靠口头解释。

| 首轮读数组合 | 优先判断 | 主叙事写法 | 部署结论 |
|---|---|---|---|
| `search` 阶段 `RRS↑`，且 `WER/RRR/RCR` 未恶化 | verifier-first recovery 在搜索主段真实有净收益 | **search-bounded online recovery** | 保留在线 `retry / repair / replan / escalate` |
| `search` 阶段有收益，但 `approach` 阶段 `RCR↑` 或 `RHD↑` | recovery 甜区仅在前期搜索，后段代价过高 | **early-stage recovery only** | `approach+` 收紧为 `repair / replan` |
| `approach` 阶段 `RRR` 高、`CDR` 恶化 | 恢复在破坏 handoff 边界，局部高风险区不适合硬顶 | **handoff-sensitive recovery** | `approach / inspect` 仅 recommendation 或 bounded repair |
| `manipulate-ready` 阶段收益弱，且 `WER` 或 `RHD` 高 | 末端阶段更适合停住或升级，而不是继续本地修补 | **recommendation-before-handoff** | `manipulate-ready` 默认 `hard-stop / escalate / recommendation-only` |
| 所有阶段 `VPR` 都低且 `FER` 不降 | verifier 本身未站住，恢复链没有讨论价值 | **verifier not ready** | 先修 verifier 阈值/packet schema，暂停恢复主线 |
| `search` 与 `approach` 都有收益，且 `CDR/RHD` 稳定 | 恢复可扩展到导航后半程，但仍未证明能进操作前阶段 | **navigation-phase recovery** | 保留到 `approach / inspect`，不默认进入 `manipulate-ready` |

**当前主张**：D06 论文主结果不该再写成“reject 后恢复率提升 X%”，而应直接落到这张表上——先回答 **恢复在哪一段真有净收益，在哪一段只是看起来更努力**。这会让 verifier-first 线从“系统设计很完整”继续收束成“部署边界被首轮数据证明”。

### 3.2.14 verifier-first 恢复线的阶段化资源收缩表（R838 新增）

> 来自本轮继续对 **2604.13654 / 2604.07705 两篇 UAV-VLN survey、OnFly、HTNav、AutoFly** 的本地复核。D06 现在已经把 `reject_reason → route_action`、`stage_tag → deployment bound`、`SNU/VRC/LPI/RBE` 这些判线补齐了，但还缺一个最直接的执行件：**首轮实验一出来后，哪一段 recovery 继续吃主预算，哪一段立刻收缩到 recommendation-only 或 hard-stop**。这一节专门把“阶段化净收益”压成资源动作，避免 planner / controller / recovery 三条线继续一起扩。

| 阶段 | 若首轮结果满足 | 保留决策 | 资源动作 |
|---|---|---|---|
| **search** | `SNU > 0`，且 `VRC` 稳定、`RBE` 不低 | 保留为主线在线恢复 | 允许继续投入 `retry / repair / replan` 组合，作为论文主表保留 |
| **search** | `RRS` 有提升，但 `RBE` 偏低或 `RCR` 偏高 | 收缩为 budget-bounded online recovery | 只保留低成本恢复动作，不再加重型 planner 或 controller 分支 |
| **approach** | `SNU` 有限为正，但 `LPI / RHD` 开始上升 | 保留为 bounded recovery | 仅保留 `repair / replan`，冻结自由 retry 与新增恢复动作 |
| **approach** | `SNU <= 0` 或 `VRC` 低、`RRR` 高 | 退回 recommendation-first | 优先回查 packet schema / reject routing，不再给该阶段 recovery 新预算 |
| **inspect** | recommendation-only 与 online 差距很小 | 不保留通用在线恢复 | 把 recovery 降为辅助建议，主预算转回 verifier 与 planner 接口 |
| **manipulate-ready** | 任一 `LPI / CDR / RHD / RCR` 明显恶化 | 默认 hard-stop / escalate | 冻结该阶段在线恢复，不再宣传为主线能力 |

**收缩原则**：
1. D06 后续不再接受“每个阶段都继续补 recovery 动作”的推进方式；必须先看这张表决定预算保留边界。
2. 若只有 `search` 阶段的 `SNU` 明显为正，论文主叙事就明确写成 **search-bounded verifier-first recovery**，不把后期阶段包装成通用恢复器。
3. 对 D06 而言，`LPI / CDR / RHD` 的优先级高于“再多救回一点任务”；只要 handoff 边界开始漂，就应优先冻结后期 recovery。
4. 只有在 verifier 准入门稳定、`VRC` 可用、且恢复预算效率不过低时，recovery 才值得继续作为投稿主贡献保留。



> 来自本轮对 **OnFly / HTNav / AutoFly / Ro-SLM** 的本地回扫。R830-R831 已经把 D06 的恢复线收成“不同阶段采用不同部署边界”，但还缺一张更直接的**首轮实验后决策表**：第一轮结果出来后，到底是保留在线恢复、收缩成 bounded recovery，还是直接退回 recommendation-only。

| 阶段 | 若首轮结果满足 | 默认保留决策 | 默认收缩决策 |
|---|---|---|---|
| **search** | `RRS` 稳定提升，且 `WER / RRR / RCR` 不明显恶化 | 保留完整在线恢复链（retry / repair / replan / escalate） | 若 `RCR` 过高，仅保留 `retry + replan` |
| **approach** | `RRS` 有增益，且 `CDR / RHD` 不恶化 | 保留 `repair + replan`，禁自由 retry | 若 handoff 漂移明显，退回 `replan-only` |
| **inspect** | 恢复收益主要来自轻量语义修补，且 `WER` 低 | 保留 `bounded retry + recommendation` | 若几何 repair 不稳，退回 `recommendation-only` |
| **manipulate-ready** | 只有在 `RCR / CDR / RHD` 全都稳定时才考虑在线保留 | 最多保留 `hard-stop + escalate + recommendation` | 默认不保留通用在线恢复 |

**当前判断**：D06 的 recovery 主结果不该再写成“一个总恢复器”，而应写成 **按阶段裁剪的保留策略**。这会让 D06 从“有恢复机制”继续收束到“恢复到底在哪些任务阶段值得常驻”。

### 3.2.19 细粒度认知模块化 planner 的升级门槛（R850 新增）

> 来自本轮对 **OnFly / GET / UAV VLA review** 的本地回扫，以及 arXiv 新结果 **FineCog-Nav (2604.16298)** 的补扫。D06 当前已经把 `packet-first + verifier-first + stage-bounded recovery` 收得很紧，但还缺一个更前置的判断：**planner 内部是否值得显式拆成语言处理 / 感知 / 注意力 / 记忆 / 想象 / 推理 / 决策等细粒度认知模块**。FineCog-Nav 给出的真正新信号，不是“模块更多”，而是把 `instruction adherence / memory usage / module I-O protocol` 提升成了可单独诊断的对象。

**当前升级门槛**：
1. 只有当细粒度模块化 planner **同时** 提升 `sentence-level instruction adherence` 与 `memory-hit-to-waypoint conversion`，才允许它从 supporting baseline 升级为正式主线对照。
2. 若收益主要来自更细的 benchmark 标注、更多显式 prompt scaffolding，或 project page 式工程调参，而不是稳定改善 `long-horizon planning consistency`，则它只能作为 `planner 内部认知拆分` 的参考，不得抢走 D06 当前主叙事。
3. 若模块化 planner 与 `Semantic Waypoint Packet` 的 structured I/O 不兼容，或显著拉高 `module latency budget`，应优先回修模块间协议，而不是继续扩模块数量。
4. 因此 D06 后续真正要比较的不是“模块越多越像人”，而是：**模块化认知拆分是否在不破坏 packet-first / verifier-first 主链的前提下，带来真实的 instruction-following 与 memory-to-waypoint 净收益**。

**对当前主线的含义**：
- FineCog-Nav 适合作为 **B5/B8 交叉强基线**，专门检验 `planner 内部模块粒度` 是否值得单列。
- 但在首轮结果出来前，D06 主叙事仍应保持为 **packet-first + verifier-first + stage-bounded recovery**，而不是提前切成“认知模块化 planner”论文。
- 若后续 SC7.5 证明收益稳定、时延可控、结构化 packet 兼容，则可把 D06 从“planner 输出什么”继续推进到“planner 内部该如何组织认知链”；否则 FineCog-Nav 仅保留为重要 supporting evidence。

### 3.2.20 FineCog-Nav 的当前定位与冻结规则（R850 新增）

> 目的：防止 D06 因为 FineCog-Nav 这类新论文出现后，再次把 `memory planner / fine-grained cognition / packet planner / verifier-first execution` 同时拉进主摘要。

| 若首轮观察到 | FineCog-Nav 应被如何记账 | 不该怎么写 |
|---|---|---|
| instruction adherence 明显提升，但 packet compatibility 差或时延高 | 记为 **认知模块化强基线** | 不写成可直接部署主线 |
| instruction adherence 与 memory-hit-to-waypoint 都提升，且时延可控 | 升级为 **planner 粒度对照主基线** | 仍不能直接替代 verifier-first / packet-first 主叙事 |
| 收益主要来自 benchmark 更细、标注更强 | 降级为 **dataset/protocol advantage baseline** | 不写成 planner 结构优势 |
| 模块化收益只出现在 search 阶段 | 记为 **search-phase planner enhancement** | 不包装成通用 NtM planner 改进 |

**冻结规则**：
- 在没有跑通 `SC7.5 + packet compatibility` 之前，FineCog-Nav 只能挂在 D06 的 planner 侧对照位，不能提前改写主标题。
- 只有当它同时满足 `instruction adherence↑ + memory-hit-to-waypoint↑ + packet compatibility稳 + latency budget可控`，才允许进入 D06 主表主列。

### 3.2.21 R850 本轮推进结论

- 本轮本地回扫 **OnFly / GET / UAV VLA review** 后，D06 对“显式记忆 / 结构化推理 / 外部模块补偿”的已有理解继续稳定，没有出现需要改写 `packet-first + verifier-first` 主链的新冲突。
- arXiv 补扫命中 **FineCog-Nav (2604.16298)**，它与 D06 直接相关，但当前更适合作为 **planner 内部模块粒度** 的强对照，而非触发完整入库的新主线论文。
- 因此本轮不做论文入库，直接把 REPORT 与 experiments 推进到：**只有当模块化 planner 带来真实的 instruction-following 与 memory-to-waypoint 净收益，且不破坏 packet compatibility 时，才允许它升级为正式主对照。**

### 3.2.17 verifier-first 恢复线的高频连续执行边界（R844 新增）

> 来自本轮对 **UAV-Track VLA / OnFly / Ro-SLM / ORION** 的本地回扫，以及 QMD 对 `aerial VLN reject recovery verifier packet replan` 的回流结果。D06 现在的 recovery 主叙事已经基本收成 `search / approach / inspect / manipulate-ready` 四阶段，但还缺一个很现实的边界：**当任务进入 tracking-heavy / high-frequency continuous execution 区时，packet-first + verifier-first 还应不应该继续把恢复当默认主线？** 当前判断是，这类区间更像局部连续控制壳层的问题，而不是再多做一次 packet repair 就能解决。

**高频连续执行区定义**：
- 目标已进入近场视野，需要持续保持观测与小幅机动修正
- 局部控制频率显著高于高层 planner / verifier 的更新频率
- 典型对应 `approach` 后半段、`inspect` 的 tracking-heavy 片段，以及 `manipulate-ready` 前的最后对位窗口

**边界判断**：
1. 若 `UAV-Track VLA` 这类 temporal-compression 端到端路线主要在 **tracking continuity / low-latency local correction** 上占优，而 `packet-first` 主要在 **search / replan / safe gating** 上占优，则 D06 应明确承认：**高频连续执行区不是 packet recovery 的甜区**。
2. 若 verifier 在连续执行区频繁触发 reject，但 `packet repair` 只能带来高 `RCR / RRR`，则优先把该区段下沉给 controller shell 或 tracking-specific baseline，而不是继续扩 recovery 动作集。
3. 若 D01 supervisor 只在 `hover / re-anchor` 窗口有效，而一进入 tracking-heavy 区就收益变弱，也说明跨方向 execution supervisor 更适合作为 **低频执行前预筛**，不是高频连续控制器替代品。

**当前 D06 判断**：
- 后续主线应把 **search / global-local relocalization / packet-level safe routing** 与 **late-stage high-frequency tracking/execution** 分开验收。
- `UAV-Track VLA` 更适合作为 D06 的 **late-stage/high-frequency baseline**，专门检验我们是不是把不该由 packet recovery 解决的问题，误塞回了高层恢复链。
- 若 SC22 结果成立，D06 论文主叙事应明确写成：**packet-first + verifier-first 负责低频语义搜索与安全路由；tracking-heavy late stage 交给专门的连续执行壳层。**

### 3.2.18 verifier-first 恢复线的单主叙事优先级补丁（R844 新增）

> 目的：结合 **UAV-Track VLA** 这类高频连续执行基线，把 D06 当前的单主叙事冻结规则再压实一点，避免首轮实验后同时保留“search recovery 主线”和“late-stage tracking 也算恢复收益”这两种重叠表述。

| 若首轮现象出现 | 更应保留的主叙事 | 不该继续并列保留的叙事 |
|---|---|---|
| `search` 阶段 verifier/recovery 净收益明显，而 `approach+` 主要由 tracking baseline 占优 | **search-bounded verifier-first recovery** | 不再把 late-stage 连续跟踪收益写成 recovery 主贡献 |
| `FER` 改善最稳，但连续执行区主要靠 controller / tracking shell 稳住 | **verifier-first execution** | 不再并列宣传“通用 packet recovery + continuous control recovery” |
| `UAV-Track VLA` 仅在 inspect / manipulate-ready 前窗口显著占优 | **stage-split execution stack**（低频 packet + 高频 tracking shell） | 不把 tracking 优势误记成 planner/recovery 进步 |
| recommendation-only 与 online recovery 差距很小，而 tracking baseline 仍更稳 | **verifier + recommendation + tracking shell** | 不再为 late-stage online recovery 扩预算 |

**补充规则**：
1. 只要某段收益主要来自 **高频连续控制壳层**，就不计入 D06 的 packet recovery 主贡献。
2. D06 后续若保留 recovery 主线，默认只统计 **低频语义搜索 / packet 路由 / replan 边界** 带来的净收益。
3. 这一步的作用不是削弱 D06，而是让论文主结论更干净：哪些收益来自 verifier/recovery，哪些收益来自 tracking/controller，必须严格拆开。

### 3.2.16 verifier-first 恢复线的单主叙事冻结与终止条件（R841 新增）

> 来自本轮对 **2604.13654 / 2604.07705 / OnFly / HTNav / AutoFly / Ro-SLM** 的本地复核。D06 前面已经有多张“如何选主叙事”的表，但还缺一条更硬的执行规则：**什么时候必须停止继续并列讲 verifier / routing / recovery / D01 supervisor，直接冻结成单主线**。这一节不再扩方法，只负责给首轮结果一个明确止损边界。

| 首轮现象 | 立即判断 | 必做动作 | 禁止动作 |
|---|---|---|---|
| `FER` 改善最稳，且 `WER / RRR` 只带来边际小增益 | 主收益来自准入门，而非后续恢复 | 冻结为 **verifier-first execution** | 不再继续扩 late-stage recovery 叙事 |
| `WER / RRR` 明显优于 `FER` 改善，且 `reject_reason` 稳定 | 主收益来自 reason-aware routing | 冻结为 **reason-aware reject routing** | 不再并列宣传 verifier 和 recovery 都是主贡献 |
| 收益几乎全在 `search` 阶段，`approach+` 带来明显 `RCR / CSDR / RHD` 代价 | recovery 只是早期导航补件 | 冻结为 **search-bounded recovery** | 不再包装成通用 NtM 恢复器 |
| `D01 supervisor` 明显降低 `late stop / misroute / danger pass-through` | 跨方向接口复用价值最高 | 冻结为 **interface-first packet supervision** | 不再继续扩本地 local recovery 分支 |
| recommendation-only 与 online recovery 差距很小 | 在线恢复不值在线预算 | recovery 全部降级为 supporting evidence | 不再为 recovery 单独扩实验矩阵 |
| 多条子线各有小增益，但解释边界重叠严重 | 当前没有单一主叙事成立 | 先收束到 **最省预算且最可复用** 的那条 | 禁止把多条子线并列写进摘要 |

**终止条件**：
1. 首轮后若同一收益可被两条以上子线解释，默认只保留**更靠前、边界更清楚、成本更低**的那条。
2. 任一子线若主要收益建立在 `Recovery Cost Ratio / Cross-Stage Drift / Wrong-Escalation Rate` 明显恶化之上，直接取消主叙事资格。
3. D06 主摘要、主结果表、贡献点列表里**最多出现一条恢复相关主线**；其余只能下沉到 supporting evidence / appendix。
4. 若首轮仍无法形成单主线，下一轮默认不扩 recovery 动作，而是回头修 `packet schema / verifier threshold / reject_reason stability`。

### 3.2.12 verifier-first 恢复线的首轮结论模板（R834 新增）

> 来自本轮对 **OnFly / HTNav** 的本地复核。D06 现在已经有 `reject_reason → route_action`、`stage_tag → deployment bound`、`首轮判线表` 三层规则，但还缺一个最实用的收束件：**第一轮实验跑完后，论文里该怎样用一句话给出阶段化结论**。这一步不是新方法，而是把前面散开的判线、保留原则和部署边界压成可直接落在主表旁边的结论模板。

| 阶段 | 若首轮表现 | 标准结论句式 | 对论文主叙事的含义 |
|---|---|---|---|
| **search** | `RRS` 提升，且 `RCR / WER / RRR` 可控 | **在线恢复值得保留于 search 阶段** | recovery 是主线贡献的一部分 |
| **approach** | `RRS` 有限提升，但 `CDR` 或 `RHD` 开始恶化 | **恢复仅建议保留为 bounded repair / replan** | recovery 不是通用策略，而是阶段受限补件 |
| **inspect** | 轻量 retry 有收益，但几何 repair 波动大 | **恢复适合作为 recommendation-first 辅助机制** | 更适合写成 verifier 后的低风险补件 |
| **manipulate-ready** | 任一 `RCR / CDR / RHD` 明显恶化 | **默认不保留通用在线恢复，仅保留 hard-stop / escalate** | handoff 前后边界是论文的重要安全结论 |

**推荐统一写法**：
1. 若只有 `search` 明显成立：主结论写成 **stage-bounded online recovery with search-stage sweet spot**。
2. 若 `search + approach` 都成立、但 `inspect / manipulate-ready` 不成立：主结论写成 **navigation-phase recovery rather than handoff-phase recovery**。
3. 若只有 recommendation-first 有稳定收益：主结论写成 **verifier-guided recommendation is safer than closed-loop online recovery**。
4. 若 `manipulate-ready` 阶段 consistently 恶化：明确写成 **handoff boundary should prefer stop-and-escalate over local retry**。

**当前主张**：D06 后续不该再追“能不能把 recovery 再做大”，而应优先把**哪一段值得上线、哪一段只该给建议、哪一段必须停住升级**写成首轮结论模板。这样 REPORT 就能从“机制越来越全”真正进入“投稿级主结论越来越短、越来越硬”的状态。


> 来自本轮继续对 **OnFly / HTNav / AutoFly / ORION / Ro-SLM** 的本地回扫。D06 现在已经有了 `reject_reason + stage_tag + deployment criteria`，但还差最后一个更执行导向的问题：**当首轮结果出来后，哪一段 recovery 应该继续保留为主线，哪一段应立即冻结，只当附录或工程补件**。这一步的目标不是再发明新指标，而是把已有指标压成“资源该继续押哪一段”的决策表。

| 阶段 | 若观察到的首轮结果 | 结论 | 推荐动作 |
|---|---|---|---|
| **search** | `Net Stage Benefit` 为正，且 `WER / RRR / RCR` 未显著恶化 | recovery 值得保留为主线在线能力 | 继续扩大 `retry / repair / replan` 组合，并作为论文主表保留 |
| **search** | 收益主要来自降低人工接管，但 `RCR` 很高 | recovery 有用但代价偏大 | 降级为 budget-bounded online recovery，只在低风险场景开 |
| **approach** | `NSB` 微弱且 `CSDR / RHD` 上升 | recovery 在接近阶段破坏 handoff 稳定性 | 冻结自由 retry，只保留 `repair / replan` |
| **inspect** | `recommendation-only` 与 `online recovery` 差距很小 | 在线恢复贡献不足 | 从主线移除，只保留建议模式或离线分析 |
| **manipulate-ready** | 任一方案使 `RCR`、`CSDR` 或 `WER` 明显恶化 | 高风险末端不适合通用在线恢复 | 默认 hard-stop / escalate，不再宣传通用 recovery |
| **任意阶段** | `RRR` 持续偏高，且问题集中在同一 `reject_reason` | 当前恢复不是在修问题，而是在拖延问题 | 优先回查 `packet schema / reject_reason / verifier threshold`，暂停继续扩 recovery 动作集 |

**当前判断**：
1. D06 后续应把 recovery 写成 **按阶段竞争保留预算** 的组件，而不是默认每一段都保留。
2. 若只有 `search` 阶段稳定产生净收益，那主叙事就应明确写成 **search-bounded recovery**，不要把后期阶段一并包装成“通用恢复器”。
3. 这一步的价值，在于让 D06 从“知道恢复在哪一段可能值钱”继续推进到“首轮结果一出来就知道哪一段还能继续吃 GPU/篇幅预算”。

### 3.2.15 verifier-first 恢复线的主叙事冻结优先级（R840 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly** 与 D06 既有恢复协议的本地回扫。现在 D06 的问题已经不是“恢复线够不够完整”，而是 **首轮结果出来后，哪一条线有资格占主摘要、哪一条必须立刻降级为 supporting evidence**。这一节专门把 `verifier / packet repair / reject routing / stage-bounded recovery / D01 supervisor` 五条线排成固定优先级，避免首轮后继续把所有机制同时包装成主贡献。

| 若首轮主要收益来自 | 优先主叙事 | 必须降级的子线 | 为什么这样收 |
|---|---|---|---|
| `FER↓` 最稳，且无需 recovery 也能解释大部分收益 | **verifier-first execution gate** | 通用 online recovery / 复杂 planner 扩张 | 说明最值钱的是“哪些输出根本不该执行” |
| `WER↓ + RRR↓` 最稳，且收益集中在 reject 后动作选择 | **reason-aware reject routing** | 末端阶段 recovery 泛化叙事 | 说明系统赢在“拒绝后怎么修”，而不是“每段都能恢复” |
| `search` 阶段 `RRS↑` 最稳，其他阶段收益弱 | **search-bounded online recovery** | `approach / inspect / manipulate-ready` 在线恢复 | 说明 recovery 甜区明确存在，但不应冒充通用恢复器 |
| `D01 supervisor` 显著降低 misroute / late stop | **interface-first packet supervision** | D06 内部通用 recovery 夸张写法 | 说明跨方向执行前预筛比在 D06 内部继续堆恢复动作更可复用 |
| recommendation-only 与 online 差距很小 | **verifier + recommendation** | 在线恢复主贡献位 | 说明闭环在线修补不值实时预算 |

**冻结优先级规则**：
1. **可复用性优先于复杂度**：若 `D01 supervisor` 与本地 recovery 都有效，优先保留边界更清楚、迁移性更好的 packet supervision。
2. **执行前预筛优先于执行后补救**：若 verifier 已显著解释主要收益，recovery 默认不占主摘要。
3. **阶段甜区优先于通用叙事**：只要收益主要集中在 `search`，就必须明确写成 **search-bounded**，禁止再写“全阶段恢复”。
4. **低成本方案优先**：若 recommendation-only 与 online recovery 差距很小，默认保留 recommendation，回收在线恢复预算给 verifier / packet / handoff 稳定性。

### 3.2.16 verifier-first 恢复线的首轮资源冻结表（R840 新增）

> 目的：在已有 `R836/R839` 阶段化判线基础上，再补一张 **首轮实验后真正执行资源收缩** 的决策表。不是再加指标，而是把“谁继续吃篇幅/GPU/实验位，谁立即冻结”写死。

| 首轮读数组合 | 优先结论 | 保留线 | 冻结线 |
|---|---|---|---|
| `FER↓` 明显，`RRS` 边际收益弱 | verifier 已解释主要增益 | verifier / packet schema | online recovery 扩张 |
| `WER↓、RRR↓` 明显，且 `RCR` 可控 | reject routing 真正有净收益 | reject_reason + route_action | 新 planner baseline 扩张 |
| `search` 阶段 `RRS↑`，但 `approach+` 阶段 `RCR/CDR/RHD` 恶化 | recovery 只该保留在早期搜索 | search-stage recovery | approach / inspect / manipulate-ready recovery |
| `D01 supervisor` 让 `misroute/late stop` 明显下降 | 跨方向执行前接口成立 | packet supervision | D06 内部复杂 recovery 叙事 |
| recommendation-only 与 online 差距小，且 `RCR` 偏高 | 在线补救性价比低 | verifier + recommendation | online recovery 主线 |

**当前 D06 判断**：
- 首轮后只允许 **一条主线** 继续吃主预算，其余全部转 supporting evidence 或附录表。
- 若 `search` 阶段 recovery 有效、但后期阶段恶化，就把主结论固定为 **search-bounded verifier-first recovery**，不再扩后段在线恢复。
- 若 `D01 supervisor` 与 D06 本地 recovery 同时成立，优先保留 **execution-time packet supervision**，因为它更容易复用到 D07 或后续 NtM 接口。
- 这会让 D06 从“恢复线越来越完整”继续收束到“论文到底要押哪一条最硬的执行链结论”。

### 3.2.17 verifier-first 恢复线的主叙事冻结优先级（R840 新增）

> 来自本轮对 **2604.13654 / 2604.07705 两篇 UAV-VLN survey、OnFly、HTNav、AutoFly** 与现有 D06 恢复协议的联合回扫。现在 D06 真正缺的已经不是“再补一个恢复动作”，而是 **首轮结果一出来后，到底该把哪条执行链写成论文主叙事，哪条立刻降级成 supporting evidence**。这一步专门避免 `verifier / reject routing / search-bounded recovery / D01 packet supervision` 四条线继续并列膨胀。

| 若首轮主要收益来自 | 优先主叙事 | 必须降级的子线 | 为什么这样收 |
|---|---|---|---|
| `FER↓` 最稳，且无需 recovery 也能解释大部分收益 | **verifier-first execution gate** | 通用 online recovery / 复杂 planner 扩张 | 说明最值钱的是“哪些输出根本不该执行” |
| `WER↓ + RRR↓` 最稳，且收益集中在 reject 后动作选择 | **reason-aware reject routing** | 末端阶段 recovery 泛化叙事 | 说明系统赢在“拒绝后怎么修”，而不是“每段都能恢复” |
| `search` 阶段 `RRS↑` 最稳，其他阶段收益弱 | **search-bounded online recovery** | `approach / inspect / manipulate-ready` 在线恢复 | 说明 recovery 甜区明确存在，但不应冒充通用恢复器 |
| `D01 supervisor` 显著降低 misroute / late stop | **interface-first packet supervision** | D06 内部通用 recovery 夸张写法 | 说明跨方向执行前预筛比在 D06 内部继续堆恢复动作更可复用 |
| recommendation-only 与 online 差距很小 | **verifier + recommendation** | 在线恢复主贡献位 | 说明闭环在线修补不值实时预算 |

**冻结优先级规则**：
1. **可复用性优先于复杂度**：若 `D01 supervisor` 与本地 recovery 都有效，优先保留边界更清楚、迁移性更好的 packet supervision。
2. **执行前预筛优先于执行后补救**：若 verifier 已显著解释主要收益，recovery 默认不占主摘要。
3. **阶段甜区优先于通用叙事**：只要收益主要集中在 `search`，就必须明确写成 **search-bounded**，禁止再写“全阶段恢复”。
4. **低成本方案优先**：若 recommendation-only 与 online recovery 差距很小，默认保留 recommendation，回收在线恢复预算给 verifier / packet / handoff 稳定性。

### 3.2.18 verifier-first 恢复线的首轮资源冻结表（R840 新增）

> 目的：在已有 `R836 / R839` 阶段化判线基础上，再补一张 **首轮实验后真正执行资源收缩** 的决策表。不是再加指标，而是把“谁继续吃篇幅 / GPU / 实验位，谁立即冻结”写死。

| 首轮读数组合 | 优先结论 | 保留线 | 冻结线 |
|---|---|---|---|
| `FER↓` 明显，`RRS` 边际收益弱 | verifier 已解释主要增益 | verifier / packet schema | online recovery 扩张 |
| `WER↓、RRR↓` 明显，且 `RCR` 可控 | reject routing 真正有净收益 | reject_reason + route_action | 新 planner baseline 扩张 |
| `search` 阶段 `RRS↑`，但 `approach+` 阶段 `RCR/CDR/RHD` 恶化 | recovery 只该保留在早期搜索 | search-stage recovery | approach / inspect / manipulate-ready recovery |
| `D01 supervisor` 让 `misroute/late stop` 明显下降 | 跨方向执行前接口成立 | packet supervision | D06 内部复杂 recovery 叙事 |
| recommendation-only 与 online 差距小，且 `RCR` 偏高 | 在线补救性价比低 | verifier + recommendation | online recovery 主线 |

**当前 D06 判断**：
- 首轮后只允许 **一条主线** 继续吃主预算，其余全部转 supporting evidence 或附录表。
- 若 `search` 阶段 recovery 有效、但后期阶段恶化，就把主结论固定为 **search-bounded verifier-first recovery**，不再扩后段在线恢复。
- 若 `D01 supervisor` 与 D06 本地 recovery 同时成立，优先保留 **execution-time packet supervision**，因为它更容易复用到 D07 或后续 NtM 接口。
- 这会让 D06 从“恢复线越来越完整”继续收束到“论文到底要押哪一条最硬的执行链结论”。

### 3.2.19 R841 首轮最小执行包与默认冻结边界（本轮新增）

> 来自本轮对 **OnFly / AutoFly / Ro-SLM** 与现有 `experiments.md` 的本地复核。当前 D06 已不缺“还能再写什么机制”，缺的是 **下一轮先跑哪一组最小对照，跑完后默认冻结哪些边界**。这一节把首轮执行包压成最小集合，避免继续横向膨胀。

**首轮最小执行包**：
1. **主对照只保留三档**：`hard-stop` vs `verifier+recommendation` vs `verifier+stage-bounded online recovery(search-only)`。
2. **统一输入接口**：固定 `Semantic Waypoint Packet`，不再并行拉开 code-first / free-text / end-to-end action generation。
3. **统一观测分桶**：只按 `search / approach` 两阶段先记账；`inspect / manipulate-ready` 仅做风险观察，不进首轮主表。
4. **统一核心读数**：`FER / RRS / WER / RRR / RCR / CDR / RHD`，禁止再加新指标抢主叙事。

**默认冻结边界**：
- 若 `search` 阶段的 online recovery 没有稳定净收益，后续默认冻结通用 recovery，回到 `verifier + recommendation` 主线。
- 若 `approach` 阶段出现明显 `CDR / RHD` 恶化，默认冻结该阶段在线恢复，只保留 `repair / replan` 或 recommendation。
- 若 `AutoFly` 式端到端轻量基线已经覆盖大部分自恢复收益，则 D06 不再把 recovery 当独立贡献，而把 verifier-first 当主线。
- 若 `Ro-SLM` 路线只在低复杂度 search 任务上带来便宜恢复，则该收益记到 **onboard planner budget advantage**，不单独抬成通用恢复优势。

**当前主张**：
- 下轮最值得拿的不是更多论文，而是这一组 **三档主对照 + 两阶段记账** 的第一批硬结果。
- 只要首轮能回答“search-only online recovery 相比 recommendation 到底值不值”，D06 主叙事就足够继续收紧。

### 3.2.12 verifier-first 恢复线的首轮 deployment cutline（R840 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly / Ro-SLM / ORION** 与现有 D06 指标体系的本地复核。D06 现在已经有 `verifier-first / reason-aware routing / stage-bounded recovery / D01 supervisor` 四条候选主叙事，但还缺一张**真正用于决定“哪条能力能留在线，哪条只能留作 supporting evidence”** 的 deployment cutline。没有这一步，后续很容易把每条都写成贡献，最后主摘要失焦。

| 首轮观测模式 | 说明 | 推荐保留在线能力 | 应降级能力 |
|---|---|---|---|
| `FER` 稳定下降，`Gate Latency Overhead` 可控，但 `RRS` 增益有限 | 主要收益来自准入门本身，而不是 reject 后补救 | `verifier-first execution` | `late-stage recovery` 降为 supporting evidence |
| `WER / RRR` 明显下降，且 `RCR` 未显著恶化 | 真正值钱的是 reason-aware routing，而不是单纯多做恢复动作 | `reject_reason → action routing` | 复杂 packet 花样、额外 recovery 分支 |
| `search` 阶段净收益高，但 `approach+` 阶段 `CSDR / RHD / RCR` 变差 | recovery 甜区只在搜索前中段，越往后越不适合硬保留在线 | `search-stage online recovery` | `approach / inspect / manipulate-ready` 在线恢复 |
| `D01 supervisor` 显著降低 `late stop / misroute / danger-action pass-through` | 跨方向执行前监督比继续细抠本地恢复更稳更省预算 | `interface-first packet supervision` | 部分本地 escalation/retry 花样 |
| 所有子线都有一点收益，但读数高度耦合、重复记账 | 当前主叙事过宽，首轮尚未形成单一解释核 | **先冻结扩展，保留最省预算的一条主线** | 其余全部降级为 supporting evidence |

**当前主张**：
1. D06 首轮后只允许保留 **一条主叙事 + 一条 supporting mechanism**，禁止再把 `verifier / routing / stage-bounded recovery / D01 supervisor` 四条并列写成 contribution。
2. 若 `search` 是唯一稳定甜区，则论文明确写成 **search-bounded online recovery**，不包装成通用 NtM 在线恢复器。
3. 若 `D01 supervisor` 收益最稳，则 D06 后续应把主线从“本地 planner 怎么补救”转向“packet 执行前如何做外置安全监督”。
4. 这一步的目标不是再加功能，而是确保 D06 最终能从“机制很多”收束成“论文一句话讲得清楚”。

### 3.2.13 D06 首轮后单主叙事冻结规则（R840 新增）

> 目的：把前文已有的 `verifier-first / reason-aware routing / stage-bounded recovery / interface-first packet supervision` 正式压成单选规则，避免首轮实验后继续并列保留四条主摘要。

| 若首轮最强证据来自… | D06 主叙事固定为 | 其余线的处理 |
|---|---|---|
| 放行/拒绝边界本身最稳 | **verifier-first execution** | recovery / supervisor 降级为解释或补件 |
| reject 后路由显著优于硬停与盲重试 | **reason-aware reject routing** | verifier 作为前置条件，不再单列贡献 |
| 只有 `search` 阶段 recovery 净收益显著 | **search-bounded online recovery** | 晚期 recovery 明确降级为 recommendation-only |
| D01 supervisor 最明显降低危险放行与晚停 | **interface-first packet supervision** | 本地 recovery 仅保留 search 期基础版 |

**冻结原则**：
- 首轮后优先选 **解释力最高、预算最省、最容易复现** 的那条主叙事。
- 未被选中的线，一律只出现在 supporting evidence / appendix / ablation，不再并列写成 contribution。
- 这样 D06 最终能更接近一篇真正可投稿的论文，而不是功能说明书。

### 3.2.12 细粒度认知模块化 planner 是否值得单列（R843 新增）

> 来自本轮外部补扫 **FineCog-Nav (2604.16298)** 与本地已有 **HTNav / CityNavAgent / OnFly** 的对照。D06 之前已经把 planner 的外部接口逐步收束为 `Semantic Waypoint Packet`，但还没回答一个更细的问题：**planner 内部到底该保持单体式高层推理，还是值得显式拆成语言、感知、记忆、想象、推理、决策等细粒度认知模块**。这不是又加一层工程复杂度，而是在问“长航程 instruction adherence 的收益究竟来自更强大模型，还是来自模块边界本身更清楚”。

**FineCog-Nav 给 D06 的真正增量**：
1. **把 planner 内部模块粒度抬成显式变量**：不再只比较 `frontier / memory graph / hierarchical waypoint` 谁更强，而是比较“planner 是否需要把语言理解、长程记忆、局部想象与决策解耦”。
2. **把句级 instruction adherence 正式拉进主指标**：AerialVLN-Fine 这种 sentence-level alignment benchmark 说明 D06 后续不能只看总成功率，还应直接比较“每句子指令有没有被正确吸收到航点链里”。
3. **强调结构化 I/O 协议而不是自由文本协作**：FineCog-Nav 虽然是模块化 planner，但其价值不是多 agent 叙事，而是提醒 D06：若模块间协议不结构化，模块越多越容易把收益损耗在 handoff 上。因此它反而进一步支持 `packet-first + verifier-first` 主链，而不是推翻它。

**当前 D06 判断**：
- FineCog-Nav 不改写 D06 的主执行骨架；`planner → verifier → controller` 仍是默认主链。
- 它新增的是一个需要单独验证的 **planner-inside baseline family**：在同样走 packet/verifier/controller 的前提下，比较 `单体式 planner` 与 `细粒度认知模块化 planner`，看收益是否主要体现在 **instruction adherence / long-horizon memory use / multi-sentence decomposition**。
- 若后续实验显示模块化 planner 的优势主要来自 benchmark 标注更细，而不是实际 memory-to-waypoint 净收益提升，则 FineCog-Nav 只保留为分析型 baseline，不升主叙事。

**因此**：D06 后续不该把 FineCog-Nav 误记成“又一个空中 VLN SOTA”，而应把它放在 **planner 内部组织方式** 这个对照位上，专门回答：在 D06 已经有 packet schema 与 verifier gate 的前提下，planner 继续细分模块到底是不是净收益。

### 3.2.15 planner 内部模块化的升级门槛（R854 新增）

> 来自本轮对 **FineCog-Nav / OnFly / AutoFly / Ro-SLM / ORION** 的本地回扫与 arXiv 复核。D06 现在已经不缺“planner 可以拆成更多认知模块”的证据，真正缺的是：**这些模块化收益什么时候只是更会解释，什么时候真的能改写主方法主线**。因此需要把 FineCog-Nav 这类方法的升格条件写死，避免后续继续把 benchmark 漂亮和系统主收益混在一起。

**当前升级门槛**：细粒度认知模块化只有在统一 `Semantic Waypoint Packet + verifier-first` 主链下，同时满足以下条件，才允许升格为 D06 正式 planner 主线：
1. **前置质量提升**：显著降低 `semantic mismatch -> reject`，说明收益不只是后验解释更细，而是 planner 在进入 verifier 前就更少提交坏 packet。
2. **净 waypoint 收益成立**：`instruction adherence / memory usage / long-horizon reasoning` 的提升，必须真正转化为更高的 `memory-hit-to-waypoint conversion` 与更低的无效子目标率，而不只是句级 benchmark 更漂亮。
3. **packet 兼容性稳定**：模块化 planner 的 structured I/O protocol 必须稳定映射到 `Semantic Waypoint Packet`，不能靠额外 prompt glue 或人手规则临时对齐。
4. **时延预算不过度恶化**：若模块数增加主要带来更高的延迟、链路复杂度或更多 verifier 前修补成本，则默认不升格。

**默认降级规则**：若 FineCog-Nav 类方法的收益主要停留在以下任一层面，则默认只保留为 `diagnostic baseline`：
- 句级 instruction alignment benchmark 更强
- 解释性、可视化或 role-specific prompt 设计更漂亮
- 模块职责更清楚，但 waypoint 净质量没有同步提升
- 需要额外 glue code 才能对接 packet/verifier 主链

**这条规则的意义**：
- 防止 D06 被 planner 内部细拆牵着走，丢失 `packet-first + verifier-first + stage-bounded recovery` 的主收束。
- 让 FineCog-Nav 这类工作主要承担 **诊断与对照位**：帮助解释 planner 失败来自语言、记忆、推理还是决策，而不是默认拿走论文主标题。
- 把后续实验预算重新压回更关键的三处：`packet schema`、`verifier quality`、`stage-bounded recovery`。

### 3.2.12 FineCog-Nav 的默认定位：diagnostic baseline first（R856 新增）

> 来自本轮对 **FineCog-Nav / OnFly / HTNav** 的本地回扫，以及 QMD 对 `aerial VLN planner cognitive modules instruction adherence memory usage module protocol` 的回流结果。当前 D06 已经有足够多证据支持 `packet-first + verifier-first + stage-bounded recovery` 主链；因此新引入的 FineCog-Nav 不能再默认被问成“是不是更强的 planner”，而应先问 **它到底在提供真正的 planner 净收益，还是只是在把错误拆得更清楚**。

**当前最稳判断**：FineCog-Nav 的直接增量主要有两层：
1. **模块级错误可诊断性**：它把语言处理、注意力、记忆、推理、决策拆开，使 `instruction adherence`、`memory usage`、`reasoning slip` 更容易被单独定位；
2. **句级评测粒度提升**：AerialVLN-Fine 这类句级 instruction-trajectory 对齐 benchmark 让系统更容易在长指令与子句级偏差上显出优势。

但这两层增量**还不自动等价于**：
- 在统一 `Semantic Waypoint Packet` 接口下输出了更高质量的 waypoint；
- 在 `verifier-first` 执行链上实质降低了 `semantic mismatch → reject`；
- 在真实部署约束下带来了比现有 planner 更高的净任务收益。

**因此从 R856 起，FineCog-Nav 默认按 `diagnostic baseline first` 记账**：
- 若它只改善模块解释性、句级 adherence 或 benchmark 可诊断性 → 记作 **诊断收益**；
- 只有当它同时改善 `instruction adherence / memory-hit-to-waypoint conversion / pre-verifier semantic mismatch rate`，并最终转化为 **净 waypoint 质量提升**，才允许升格为正式 planner 主线候选。

**对主叙事的影响**：
- D06 当前主叙事继续维持 **packet-first + verifier-first + stage-bounded recovery**；
- FineCog-Nav 更适合作为一个“帮我们解释 planner 为什么失效、哪些失效值得继续拆模块”的探针，而不是自动改写主骨架的新主线。

### 3.2.12 FineCog-Nav 的判线优先级继续收缩到“前置语义收益是否真的转成净 waypoint 收益”（R858 新增）

> 来自本轮对 **FineCog-Nav / OnFly / HTNav** 的本地回扫与 QMD 回流复核。当前最需要回答的已经不是“FineCog-Nav 模块拆得细不细”，而是：**这些细粒度认知模块到底有没有在统一 `Semantic Waypoint Packet + verifier-first` 主链里，先减少前置语义错误，再稳定转化成更好的 waypoint 质量**。若做不到，这条线就不该继续占主叙事预算。

**本轮新的收束判断**：FineCog-Nav 暂时只保留为 **diagnostic-first baseline**，它最稳的价值是把三类 planner 前置问题单独暴露出来：
1. **instruction adherence 掉线**：语言子句理解正确，但在长航程执行中逐步失配；
2. **memory-hit-to-waypoint conversion 失配**：记忆模块命中了相关地标/线索，但没有稳定转成更好的下一个子目标；
3. **module I-O protocol 松散**：模块间中间状态说得清楚，却没有无损对接到 `Semantic Waypoint Packet`。

**因此主线资格继续冻结为三步判线**：
- **Step 1 前置语义收益**：先看它是否显著降低 `pre-verifier semantic mismatch rate`；
- **Step 2 记忆转化收益**：再看它是否显著提升 `memory-hit-to-waypoint conversion`；
- **Step 3 净航点收益**：只有前两步都成立，且最终换来 **净 waypoint quality 提升**（而不是只把解释做细），才允许升格为正式 planner 主线候选。

**当前最重要的负面判线**：
- 若收益只停留在 `instruction adherence` 更好看 → 记为 **语言诊断收益**；
- 若收益只停留在 `memory usage` 更可解释 → 记为 **memory debugging baseline**；
- 若收益主要来自更细 benchmark、role-specific prompts、或模块 prompt scaffolding → 统一记为 **supporting evidence**；
- 以上任一情况都**不改写** D06 当前的 `packet-first + verifier-first + stage-bounded recovery` 主叙事。

**这一收缩的直接意义**：后续 D06 不再把“planner 模块化程度”当作默认值得扩张的新故事，而是先把它压成一个很硬的问题——**模块化到底有没有把 verifier 之前的语义收益真正转成 controller 之前的可执行子目标收益**。只有这个问题回答成“有”，FineCog-Nav 才配升级。

### 3.3 与现有方法的关键差异

| 对比维度 | VLFM (地面) | OnFly (空中) | AutoFly (ICLR 2026) | Aerial VLN Unified (arXiv:2512.08639) | 我们的方法 |
|---------|-----------|-------------|-------------------|--------------------------|----------|
| 运动空间 | 2D 平面 | 3D 无系统前沿 | 3D端到端 | 3D统一框架 | 3D 体素前沿图 |
| 语言引导 | VLM评分前沿 | 无显式语言引导 | VLA端到端 | 语言+视觉统一 | VLM评分+3D前沿 |
| 动力学 | 无 | 无显式建模 | 无 | 无 | 动力学感知代价 |
| 操作拓展 | 无 | 无 | 无 | 无 | NtM统一架构 |
| 场景类型 | 室内 | 室外 | 室外开放世界 | 多场景 | 室内+室外 |
| 发表 | CVPR 2024 | IROS 2026 | ICLR 2026 | arXiv | 目标ICRA 2027 |

### 3.2.11 verifier-first 恢复线的首轮资源冻结与主叙事收束规则（R838 新增）

> 来自本轮对 **OnFly / GET / AirVLA / AerialVLA** 与既有 verifier-first 材料的本地回扫。D06 现在已经知道 recovery 该在哪些阶段启用，也有了 go / no-go 判据；但还缺最后一步：**首轮实验一出来后，哪条恢复线应该继续吃预算，哪条必须立刻冻结，并且论文主叙事到底写“通用恢复器”还是“阶段化恢复器”**。否则后续很容易继续在 `retry / repair / replan / escalate` 四条线上平均摊算力。

**资源冻结原则**：
1. **若 `search` 阶段收益稳定，但 `approach / inspect / manipulate-ready` 阶段的 `Recovery Cost Ratio / Repeat-Reject Rate / Cross-Stage Drift Rate` 明显恶化**：主叙事收束为 **stage-bounded recovery**，冻结后段在线恢复扩张，不再宣传“通用在线恢复器”。
2. **若 `packet repair` 在几何 reject 上长期无增益**：优先冻结 recovery 调参，把资源退回 `Semantic Waypoint Packet` 接口修订（`target_pose / yaw_hint / altitude_band / safety_budget`），而不是继续堆 repair heuristic。
3. **若 verifier 自身 `VPR` 低且 `FER` 不降**：冻结 recovery 线，先回查 verifier 阈值、`reject_reason` 判定和 packet schema；此时继续调 retry / replan 只会把 verifier 缺口包装成恢复能力。
4. **若 `Wrong-Escalation Rate` 高，但 `Repeat-Reject Rate` 低**：说明系统偏保守、仍有本地可修空间，优先保留 `retry / repair`，冻结 `escalate` 扩张。
5. **若 `Repeat-Reject Rate` 高，且 `shared-memory replan` 也无明显收益**：默认冻结 recovery 整条副线，回到 planner / grounding / controller 壳层排查，不再把失败归咎为恢复策略不够复杂。

**主叙事收束规则**：
- 只有当 recovery 在 `search` 阶段显著拉升净任务收益，且不明显放大 `Recovery Cost Ratio / Wrong-Escalation Rate / Cross-Stage Drift` 时，才允许把 D06 主结果写成 **verifier-first stage-bounded recovery**。
- 若 recovery 收益主要体现在“少数 case 被救回”，但成本和阶段漂移很高，则论文叙事应降级为 **verifier-first execution with bounded recovery recommendation**，把 recovery 写成部署补件而非核心贡献。
- 若 verifier 本身才是最大增益来源，则主叙事优先写 **planner → verifier → controller** 的准入门价值，恢复线只保留为附属分析，不与 C1/C2/C3 抢主贡献位。

**当前 D06 判断**：
- 后续首轮实验不该再只报“reject 后恢复成功率”，而应同步回答 **哪条恢复线值得继续投算力、哪条线该立刻停预算**。
- 这一步会让 D06 从“恢复该不该上线、该在哪段上线”继续收束到“恢复到底够不够资格进入论文主叙事”。

### 3.2.19 D06 首轮最小执行包与默认冻结规则（R842 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly / 2604.13654 UAV-VLN Survey** 的本地回扫。当前 D06 的 verifier / routing / recovery / supervisor 线已经足够丰富，下一步最重要的不是再补机制，而是把 **首轮到底先跑哪三个对照、跑完后默认冻结什么** 压成最小执行包，避免后续实验继续摊大饼。

**首轮最小执行包**：
1. **三档主对照**：`hard-stop` vs `verifier + recommendation-only` vs `verifier + search-only online recovery`
2. **统一接口**：固定 `Semantic Waypoint Packet`，禁止 planner / controller 走私有中间状态
3. **统一阶段记账**：首轮主表只记 `search / approach` 两阶段；`inspect / manipulate-ready` 仅保留风险观察，不进主表
4. **统一主指标**：`FER / RRS / WER / RRR / RCR / CDR / RHD`

**默认冻结规则**：
- 若 `search-only online recovery` 相比 `recommendation-only` 没有稳定净收益，则 **recovery 退出 D06 主叙事**，主线回收给 verifier / packet schema。
- 若 `approach` 阶段 `CDR / RHD` 明显恶化，则默认冻结该阶段在线恢复，只保留 `repair / replan` 或 recommendation。
- 若 `D01 supervisor` 后续收益主要体现在 `misroute / late-stop`，则 D06 主结论应优先收束到 **execution-time packet supervision**，而不是继续放大全阶段 recovery。
- 若 `AutoFly` 式轻量端到端基线已经覆盖大部分自稳收益，则 D06 主线优先收束为 **verifier-first execution gate**，不再把 recovery 单列成核心贡献。

**为什么要这样做**：
- **OnFly** 已足够说明 verifier-first 有价值，首轮应该先证明“拦住输出”本身值不值钱。
- **HTNav** 说明阶段边界必须单独记账，不然 search 与 approach 的收益会混淆。
- **AutoFly** 提醒我们部分“恢复收益”可能只是轻量端到端策略本身的自稳能力，不能误记成 recovery 机制贡献。

**当前 D06 判断**：
- 首轮实验后只允许 **一条主线** 继续吃主预算；其余全部降级为 supporting evidence 或 appendix。
- 如果 `recommendation-only` 已经解释大部分收益，就别再硬保在线 recovery。
- D06 近期最值钱的不是“恢复动作越来越多”，而是尽快回答：**search-only online recovery 到底值不值得留在线上。**

- 本轮方向继续选 **D06 空中视觉语言导航**，严格先本地回扫 `README / REPORT / experiments / FineCog-Nav 笔记`，并补做最小 arXiv 外查；外查结果显示 **FineCog-Nav (2604.16298)** 仍是本轮最有价值的新近相关工作，但它**已在本地入库**，因此本轮不新增 L1 入库。
- 当前更稳的判断不是“D06 要不要改成细粒度认知模块化主线”，而是：**FineCog-Nav 最适合作为强诊断型 planner baseline**，用来检验 `instruction adherence / memory-hit-to-waypoint conversion / pre-verifier semantic mismatch rate` 是否真的能在统一 `packet-first + verifier-first` 链上转化成净 waypoint 质量收益。
- 因此，D06 主叙事暂不改写，继续维持 **packet-first + verifier-first + stage-bounded recovery**；只有当模块化 planner 在不恶化 packet 兼容与时延预算的前提下，同时改善上述三项前置指标，才允许升格为正式 planner 主线候选。

## 3.2.15 late-stage recovery 的首轮默认停线规则（R868 新增）

> 来自本轮对 `D06/README.md`、`experiments.md`、近 30 天 D06 收束记录与本地已入库 **OnFly / HTNav / AutoFly / FineCog-Nav** 的再次压缩。既然前面已经把 **先修 packet schema / 先修 handoff interface / 再考虑继续扩 late-stage recovery** 的顺序基本写死，那本轮还需要把它再落成一个更适合首轮实验复盘的默认停线规则：**什么信号一出现，就先停哪条线，避免 packet、handoff、recovery 三条继续并行烧预算。**

**默认停线顺序固定如下**：
1. **几何 reject 主导 + `Packet Repair Gain` 持续接近 0**：先停 `late-stage recovery 动作扩容`，优先冻结到 `packet schema 修补` 线；此时继续加 retry / replan 只会重复把不可表达的几何需求塞回旧 packet。
2. **`search` 阶段 recover 仍有效，但 `approach / inspect` 稳定出现高 `Cross-Stage Drift Rate / Recovery-to-Handoff Delay / Late-Stage Penalty Inflation`**：先停 `handoff 后 recovery 扩容`，优先修 `handoff_tag / progress_score / stage_tag`；因为这类问题更像阶段接口漂移，而不是恢复动作还不够多。
3. **只有当 packet 与 handoff 两类接口问题都未主导**，且 `Recovery Budget Efficiency` 仍显著为正，才允许 late-stage recovery 继续保留在线扩容预算；否则默认降级为 `search-bounded` 或 `recommendation-only`。

**为什么要再写这一层**：
- 前几轮已经说明 recovery 的主甜区在 `search`，所以 late-stage 一旦失效，优先怀疑接口表达不足，比继续堆恢复动作更划算；
- 若首轮复盘时没有默认停线规则，D06 很容易重新回到“packet 修一点、handoff 修一点、recovery 再扩一点”三线并行，最后既解释不了收益来源，也难以形成论文主叙事。

**当前 D06 的默认复盘口径**：
- `PRG≈0 + 几何 reject 主导` → **先停 recovery 扩容，转修 packet schema**
- `search recover 有效 + late-stage CSDR/RHD/LPI 恶化` → **先停 handoff 后 recovery 扩容，转修 handoff interface**
- 只有两类接口问题都不主导且 `RBE>0` 时 → **late-stage recovery 才继续在线保留**

## 四、实验设计

### 3.2.21 FineCog-Nav 升格/降级的首轮冻结判据（R854 新增）

> 来自本轮对 **FineCog-Nav / OnFly / HTNav / UAV-VLN Survey** 的本地回扫，以及最小 arXiv 补检。D06 现在已经把 FineCog-Nav 的升级门槛写过一轮，但还缺最后一步：**首轮实验结果出来后，怎么一眼判断它该升格为主线 planner，还是主动降级回 diagnostic baseline**。不把这一步写死，后面很容易把“模块更多、解释更细、benchmark 更精”误写成真正的方法收益。

**首轮冻结判据**：
1. **升格为正式 planner 候选**：只有当 FineCog-Nav 在统一 `Semantic Waypoint Packet + verifier-first` 协议下，**同时** 改善 `instruction adherence`、`memory-hit-to-waypoint conversion` 与 `pre-verifier semantic mismatch rate`，并把收益转化为 **净 waypoint 质量提升**，才允许升格。
2. **保留为 diagnostic baseline**：若收益主要体现在 `module attribution clearer`、`sentence-level benchmark 更好看`、`error localization 更容易`，但没有明显改善执行前 packet 质量，则默认只记为诊断增益，不改写 D06 主叙事。
3. **直接降级为 supporting evidence**：若 `structured I/O protocol` 很难无损对接 `Semantic Waypoint Packet`，或模块时延明显侵蚀 verifier / controller 预算，则它只作为 supporting baseline 保留，不再占主实验篇幅。
4. **默认记账原则**：D06 后续对 FineCog-Nav 的默认态度应是：**先证明它提升执行前 planner 质量，再讨论它值不值得改写 planner 内部组织方式**；不能反过来先把模块化当成主结论。

**当前冻结结论**：
- FineCog-Nav 暂时默认归到 **diagnostic baseline**，不是自动升格的主线 planner。
- D06 主叙事继续维持 `packet-first + verifier-first + stage-bounded recovery`。
- 只有当 `SC7.5` 跑出真正的 **planner 质量净收益**，才允许它从诊断位进入摘要层。

### 4.1 数据集/环境
- **AirSim/UE5**: 主人已有 UE5.7 迁移经验(AirSpark 项目)
- **AirNav**: 真实城市空中VLN benchmark,可作为 D06 后续优先对照基准
- **Habitat-Air** (如有): 空中 VLN benchmark
- **MotionScape (2604.07991)**: 🆕 30h+ 4K UAV-view 视频，4.5M+ 帧，6-DoF 轨迹+语言标注，**专门用于训练 UAV 世界模型**，解决现有数据缺乏高动态 6-DoF 先验问题。GitHub: Thelegendzz/MotionScape
- **CARLA-Air (2603.28032)**: 🆕 统一空-地仿真基础设施，无人机+车辆在同一 UE5 进程，支持 18 种传感器模态，零修改复用 CARLA/AirSim API，**可替代 AirSim 作为主要仿真环境并直接对比地面 Agent**
- **真机验证**: 龙虾项目平台(D435i + 无人机)
- **自建场景**: 利用 3DGS 重建的真实环境（参考 MotionScape 的 3DGS 处理流程）

### 4.2 基线对比
- VLFM (直接应用到空中, 作为 ground truth 上界参考)
- OnFly
- Beyond Matching to Tiles（跨视角重定位补件基线）
- VLM-Nav（单目无地图轻量基线）
- 随机探索 / 贪心探索
- GPT-4V/Qwen-VL 直接推理导航指令

### 4.2+ baseline 家族与实验路由（R787 新增）

> 目的：不再按“论文一篇篇补”，而是把后续实验固定成几类可复用路由，方便直接排实验单。
>
> **R843 新补充：FineCog-Nav（2604.16298）定位**
> - 新扫描命中 **FineCog-Nav: Integrating Fine-grained Cognitive Modules for Zero-shot Multimodal UAV Navigation**（2604.16298，2026-04-17，CVPR 2026 Findings）。
> - 它最值得保留的不是“模块更多”，而是把 **language / perception / attention / memory / imagination / reasoning / decision-making** 压成一套 **fine-grained cognitive modularization**，并同步提供 **AerialVLN-Fine** 这种句级对齐评测切片。
> - 对 D06 的直接价值：它更像 **B5 长程记忆规划器** 与 **B8 结构化接口基线** 之间的桥梁——提醒我们后续不仅要比较 planner 是否有 memory，还要比较 **planner 内部模块化粒度** 与 **结构化 I/O 协议** 是否真的换来更稳的 instruction adherence 与 long-horizon consistency。
> - 当前判断：FineCog-Nav 暂不改写 `APEX / HTNav / OnFly` 主骨架，但应作为 **R843 候选 baseline** 写入 README，后续优先用它补 `instruction adherence / sentence-level alignment / modular planner cost` 三项对照位。

| baseline 家族 | 代表方法 | 主要承担层 | 最适合的任务类型 | 不该拿来证明什么 |
|---|---|---|---|---|
| **B1 显式搜索主线** | APEX / 我们的 3D VL-Frontier | L1 + L2 | 开放词汇目标搜索、长航程未知环境探索 | 不能单靠它证明机载部署便宜 |
| **B2 轻量端到端** | AutoFly / AerialVLA / VLM-Nav | L1 + L3 | 低成本机载闭环、短中程导航 | 不能单靠它证明搜索可解释或重定位可靠 |
| **B3 几何重定位补件** | Beyond Matching to Tiles / Fly0 / GeoNav | L0 + L2 | 已知目标附近精定位、跨视角回锚、几何规划 | 不能单靠它证明开放词汇搜索能力 |
| **B4 运行时补件** | QuadAgent / OpenFly keyframe compression / ViSA prompting | L0 或 L3 | 延迟压缩、前端推理增强、关键帧记忆 | 不能把补件当主导航骨架单独宣称优势 |
| **B5 长程记忆规划器** | CityNavAgent / HETT-style memory planner / FineCog-Nav-style modular planner | L1 + L2 | unseen 城市长航程任务、需要全局语义记忆的多阶段导航 | 不能单靠它证明局部控制或机载成本最优 |
| **B6 机载语言规划器** | Ro-SLM-style onboard SLM planner | L3 | 指令复杂、网络不稳定、需要本地闭环的机载任务 | 不能单靠它证明视觉 grounding 或全局搜索最优 |
| **B7 规划器-控制器解耦基线** | SkyVLN-style LLM planner + NMPC controller | L2 + L3 | 城市环境、约束较强、需要把高层语义子目标稳定变成可飞轨迹的任务 | 不能单靠它证明开放词汇搜索或全局记忆最优 |
| **B8 结构化机载接口基线** | OnFly / Ro-SLM-style planner + Semantic Waypoint Packet / FineCog-Nav-style structured module I/O | L2 + L3 | 需要比较“planner 输出格式”本身是否决定执行稳定性的任务 | 不能把接口收益误写成 backbone 收益 |
| **B9 代码生成式机载规划器** | Ro-SLM / ORION-style code-generation planner | L2 + L3 | 需要把任务规划、API 调用和局部执行脚本直接下沉到机载端的任务 | 不能把代码生成收益误记成 packet 设计或 controller shell 收益 |

**固定实验路由**：
1. **室内连续 3D 搜索**：IndoorUAV + B1/B2 对照，重点看 L0/L1。
2. **室外真实城市搜索**：AirNav + B1/B2/B4/B5 对照，重点看 L1/L3。
3. **跨视角回锚与长航程恢复**：Beyond Matching to Tiles + B3/B1/B5 对照，重点看 L0/L2。
4. **机载部署与压缩收益**：OpenFly/QuadAgent/VLM-Nav 路线，重点看 L3。
5. **长航程语义记忆规划**：CityNav/CityNavAgent 风格城市数据 + B1/B5 对照，重点看 long-range waypoint consistency、memory hit rate 与 replanning recovery。
6. **机载语言规划与压缩协同**：Ro-SLM/B6 + OpenFly/QuadAgent 路线联合对照，重点看 instruction complexity bucket、onboard replanning latency 与断网条件下的成功率。
7. **规划器-控制器接口验证**：SkyVLN/B7 + APEX/3D VL-Frontier 联合对照，重点看 high-level waypoint quality 相近时，NMPC 控制壳层是否显著降低轨迹抖动、急转向与局部恢复失败。
8. **细粒度认知模块化规划对照（R843 新增）**：FineCog-Nav/B5-B8 + APEX/HTNav 联合对照，重点看 sentence-level instruction adherence、module latency budget、memory-hit-to-waypoint conversion 与 structured packet compatibility。

### 4.3 评价指标
- **SR (Success Rate)**: 找到目标的成功率
- **SPL (Success weighted by Path Length)**: 路径效率
- **探索效率**: 找到目标所需的飞行距离/时间
- **能量效率**: 完成任务消耗的能量(空中特有)
- **NtM 成功率**: 导航到目标 + 操作成功的联合成功率(拓展实验)

### 4.3+ planner-controller 接口专用指标（R811 新增）

> 来自本地回扫 **HTNav / OpenFly / 2604.07705 survey** 的共同提醒。D06 之后不能只看“会不会找路”，还要固定回答“同样的高层子目标，控制接口到底有没有把它稳定飞出来”。

| 指标 | 定义 | 用途 |
|---|---|---|
| **WCES (Waypoint-Conditioned Execution Success)** | 在共享高层 planner / waypoint 序列下，成功飞完子目标段的比例 | 隔离 planner 收益，单测控制壳层是否真提高可飞性 |
| **Recovery Half-Life** | 偏航或局部碰撞预警后，轨迹误差恢复到 50% 所需时间 | 判断 controller shell 是否只是“更保守”，还是能更快回稳 |
| **Controller Regret@Shared Plan** | 相对同一 planner 下最优控制接口的额外碰撞/绕路/能耗损失 | 防止把控制层损失误记成搜索策略损失 |
| **Interface Overhead** | planner 输出到 controller 可执行轨迹之间新增的延迟、显存与同步成本 | 防止 NMPC / safety shell 因代价太高而板载不可用 |

### 4.3++++++ 恢复层主指标（R827 新增）

> 来自本轮本地回扫 **OnFly / HTNav / AutoFly / Ro-SLM / SkyVLN** 的共同收束。D06 既然已经写出 `Reject-and-Recover Ladder`，就不能再只报“最终有没有救回来”，而要把 **恢复成功、恢复代价、升级是否过度、是否陷入重复拒绝** 彻底拆开记账。

| 指标 | 定义 | 用途 |
|---|---|---|
| **Reject Recovery Success (RRS)** | 被 verifier 拒绝后，通过 `retry / repair / replan / escalate` 任一路由最终转为成功的比例 | 判断恢复梯度本身是否真有部署价值 |
| **Recovery Cost Ratio (RCR)** | 恢复成功任务相对首次直接成功任务新增的时间、路径、能耗成本比值 | 防止系统靠“反复补救”堆出表面成功率 |
| **Wrong-Escalation Rate (WER)** | 本可由本地 retry/repair 解决，却被过早升级到云端/人工接管的比例 | 防止恢复协议过度保守 |
| **Repeat-Reject Rate (RRR)** | 一次恢复后再次被 verifier 拒绝的比例 | 判断恢复动作是否只是把失败往后拖 |

**当前判断**：D06 的恢复层不该只追求 `RRS` 高，还必须同时压住 `RCR / WER / RRR`，否则所谓“可恢复”很容易只是高代价、爱升级、反复拒绝的假恢复。

### 4.3+++++++ 阶段感知恢复指标（R828 新增）

> 来自本轮本地回扫 **OnFly / HTNav / AutoFly / ORION / Ro-SLM / UAV-VLN Survey** 的进一步收束。D06 现在不能只按 `reject_reason` 选恢复动作，还要进一步判断 **失败发生在哪个执行阶段**：同样是语义错配，发生在 `search` 阶段和发生在 `approach / manipulate-ready` 阶段，容错策略完全不该一样。

| 指标 | 定义 | 用途 |
|---|---|---|
| **Stage Recovery Gain (SRG)** | 在固定阶段内，采用阶段感知恢复路由后，相比统一恢复策略新增的成功率或回稳收益 | 判断阶段判线是否真的值得保留 |
| **Stage Escalation Burden (SEB)** | 因阶段敏感风险而触发升级带来的额外时间、能耗与外部依赖成本 | 防止系统在高风险阶段过度升级 |
| **Cross-Stage Drift Rate (CDR)** | 恢复后系统误切到错误阶段标签（如 search 错切 approach）的比例 | 判断恢复协议是否破坏 NtM 阶段一致性 |
| **Recovery-to-Handoff Delay (RHD)** | 从触发恢复到重新回到正确 handoff_tag 所需时间 | 判断恢复是否只是把切换延后而没有真正修复 |

**当前判断**：D06 的恢复层不该只看 `Reject Recovery Success`，还必须同时回答 **恢复是否发生在正确阶段、是否把阶段边界搞乱、是否把升级成本压得过高**，否则 `search / approach / inspect / manipulate-ready` 四段最终仍会被一锅炖回总成功率。

### 4.24 首轮正文结果段优先级冻结规则（R889 新增）

> 目的：把 D06 从“标题与摘要该怎么诚实收束”再往前压一层，直接固定 **首轮实验主表与正文第一个结果段** 的解释顺序，避免后续又被局部 recovery 指标或单点 handoff 读数带偏。

| 首轮读数模式 | 默认解释顺序 | 正文第一个结果段默认结论 | 禁止的误读 |
|---|---|---|---|
| `Packet Repair Gain≈0`，且 `Geometry-Reject Share` 高、`Recovery Budget Efficiency` 不显著为正 | 先判 packet 表达不足 | **packet-first interface under-specification** | 不能把 recovery 动作不够多包装成主因 |
| `search` 阶段 recover 有效，但 `Cross-Stage Drift Rate / Recovery-to-Handoff Delay / Late-Stage Penalty Inflation` 持续恶化 | 先判 handoff 边界不稳 | **stage-bounded recovery + handoff-first repair** | 不能把 late-stage online recovery 继续写成默认主线 |
| 两类接口问题都不主导，且 `Net Stage Benefit` 与 `Recovery Budget Efficiency` 仍显著为正 | 才允许解释 recovery 在线收益 | **late-stage online recovery** 候选保留 | 不能跳过 packet/handoff 判线直接宣称末端恢复普遍有效 |
| `Packet Repair Gain` 有提升，但 `Net Stage Benefit` 仍不显著 | packet 有局部补益但不足以撑起主线 | **packet repair as supporting evidence** | 不能把局部补件增益升格为主标题 |
| `search` 恢复显著、late-stage 恢复不显著 | recovery 甜区仅在早期阶段 | **search-bounded recovery** | 不能混写成全阶段在线恢复器 |

**固定规则**：
1. D06 首轮主表默认按 `Packet Repair Gain / Geometry-Reject Share / Recovery Budget Efficiency → Cross-Stage Drift Rate / Recovery-to-Handoff Delay / Late-Stage Penalty Inflation → Net Stage Benefit` 的顺序解释，不接受局部 late-stage 恢复读数倒灌主结论。
2. 只要 packet 或 handoff 任一接口问题已主导，正文第一结果段就默认先证明接口承载问题，而不是先讲 recovery 动作集。
3. 只有当两类接口问题都不过主导位时，late-stage online recovery 才允许进入标题、摘要与主表竞争位。
4. 这张表的作用不是否定 recovery，而是强制 D06 先证明“当前该先修 packet 还是 handoff”，再讨论“是否值得继续扩末端恢复器”。

### 4.25 首轮预算投向冻结映射（R889 新增）

> 目的：把首轮结果直接映射成 **下一轮唯一优先动作**，防止 D06 在 `packet / handoff / recovery` 三条线上继续并行烧预算。

| 首轮信号组合 | D06 默认收束 | 下一轮唯一优先动作 |
|---|---|---|
| `PRG≈0 + geometry-dominant reject + RBE 不显著为正` | **packet-first interface under-specification** | 优先修 `target_pose / yaw_hint / altitude_band / safety_budget` schema |
| `search recover 有效 + late-stage CSDR/RHD/LPI 恶化` | **stage-bounded recovery + handoff-first repair** | 优先修 `handoff_tag / progress_score / stage_tag` |
| 两类接口问题都不主导，且 `NSB/RBE` 仍显著为正 | **late-stage online recovery** 候选保留 | 仅此时继续扩 late-stage recovery 动作集 |
| `PRG` 有局部收益但 `NSB` 不显著 | **supporting-only packet repair** | 停扩 recovery，先做 packet 轻量修补与 verifier 对齐 |

### 4.3++++++++ 恢复线首轮 go/no-go 指标（R830 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly / Ro-SLM / ORION** 的本地复核。D06 的恢复层现在不能只报 `RRS / RCR / WER / RRR`，还要进一步给出 **第一轮实验出来后是否继续保留在线恢复、是否限制在 search 阶段、还是直接降级为离线建议** 的 go/no-go 判据。

| 指标 | 判线含义 | 用途 |
|---|---|---|
| **Online Recovery Keep Rate (ORKR)** | 满足 `RRS` 提升且 `RCR / WER / RRR` 未明显恶化时，允许保留在线恢复的任务占比 | 判断恢复线是否值得继续放在线闭环 |
| **Stage-Bounded Recovery Ratio (SBRR)** | 恢复收益主要集中在 `search` 阶段的比例 | 判断 D06 是否应把恢复叙事收束成阶段受限，而非全程通用 |
| **Recovery Downgrade Trigger Rate (RDTR)** | 因高 `RCR`、高 `WER` 或高 `RRR` 被降级为 recommendation-only 的任务比例 | 防止系统把高代价假恢复继续留在主线 |
| **Late-Stage Hard-Stop Precision (LHSP)** | 在 `approach / inspect / manipulate-ready` 阶段选择 `replan / escalate / hard stop` 的正确性 | 判断后期保守恢复是否真的在压风险，而不是盲目停机 |

**当前判断**：D06 的恢复层后续不该只追求“能不能多救回来一点”，还应优先回答 **多少恢复值得继续在线保留、多少应限制在 search 阶段、多少应该直接降级为 recommendation-only**。

### 4.3+++++++++ 阶段化保留指标（R830 新增）

> 来自本轮对 **OnFly / HTNav / AutoFly** 的本地复核。D06 既然已经把恢复协议收束到 `stage-bounded recovery`，就还要继续回答 **哪些阶段值得保留完整恢复梯度，哪些阶段应该只保留建议或直接 hard-stop**。

| 指标 | 定义 | 用途 |
|---|---|---|
| **Stage Online Utility (SOU)** | 某阶段启用在线恢复后，相比关闭在线恢复带来的净成功率/净安全收益 | 判断该阶段是否值得保留在线恢复 |
| **Late-Stage Risk Inflation (LRI)** | 在 `approach / inspect / manipulate-ready` 阶段启用在线恢复后新增的碰撞、误接近、错误切换风险 | 判断后期恢复是否值得继续放在线上 |
| **Recommendation Conversion Rate (RCR-rec)** | 被降级为 recommendation-only 的恢复建议中，后续经重规划或人工确认转为有效动作的比例 | 判断“降级为建议”是不是合理兜底，而不是纯放弃 |
| **Hard-Stop Avoided Failure Rate (HAFR)** | 采用 hard-stop 替代强行恢复后避免的严重失败比例 | 判断后期保守停机是否真在压风险 |

**当前判断**：D06 主论文里的恢复线应默认先证明 `search` 阶段的 **SOU** 足够高，再决定是否扩展到 `approach / inspect`；若 `LRI` 明显升高，则 `manipulate-ready` 阶段默认只保留 recommendation-only 或 hard-stop。

### 4.3+++++++++++ 阶段化净收益收束指标（R838 新增）

> 来自本轮继续对 **2604.13654 / 2604.07705 两篇 UAV-VLN survey、OnFly、HTNav、AutoFly** 的本地复核。D06 当前关于 verifier-first recovery 的指标已经很多，但还差最后一个更适合首轮实验后直接写结论的收束：**到底是哪一段在创造“净任务收益”，哪一段只是把失败拖慢、把预算烧高、把 handoff 边界搅乱。** 因此本轮补一组“阶段化净收益”指标，专门把 recovery 从“机制完整”压到“可投稿主结论”。

| 指标 | 定义 | 用途 |
|---|---|---|
| **Stage Net Utility (SNU)** | 某阶段启用在线 recovery 相对 `recommendation-only / hard-stop` 带来的净成功收益，扣除额外时延、路径、能耗与升级代价后的综合增益 | 判断该阶段 recovery 是否真的值得上线 |
| **Verifier-to-Recovery Conversion (VRC)** | verifier 拒绝后，最终通过该阶段恢复链转成有效执行而非反复 reject/误升级的比例 | 判断 reject 是否真的被转化为可用动作，而不只是多绕一圈 |
| **Late-Stage Penalty Inflation (LPI)** | 在 `approach / inspect / manipulate-ready` 阶段启用 recovery 后新增的碰撞、漂移、错误 handoff 与安全代价 | 判断后期 recovery 是否在放大局部高风险 |
| **Recovery Budget Efficiency (RBE)** | 每单位新增计算/通信/能耗预算换回的额外成功任务比例 | 判断 recovery 是否适合继续留在板载常驻链路 |

**使用规则**：
1. 若某阶段 `SNU <= 0`，即使 `RRS` 看起来不错，也默认不保留该阶段通用在线 recovery。
2. 若 `VRC` 低而 `RRR` 高，说明恢复动作没有真正改变失败根因，优先回查 `reject_reason / packet repair / shared-memory replan`。
3. 若 `LPI` 在 `approach+` 阶段显著上升，论文主叙事就应明确收束为 **search-bounded** 或 **navigation-phase bounded** recovery，而不是继续包装成全阶段能力。
4. 若 `RBE` 持续偏低，recovery 更适合作为离线建议或云端增强，不适合作为机载常驻模块。

**当前判断**：D06 后续主结果不该再只回答“recover 了多少次”，而应直接回答 **recover 后哪一段净收益为正、哪一段预算效率仍可接受、哪一段已经开始放大风险**。这会让 verifier-first 线从“系统设计很全”继续收束到“部署边界由首轮数据直接证明”。

### 4.4 消融实验设计（细化版）

> 来自本轮本地回扫 **OnFly / Ro-SLM / ORION**。D06 后续必须把“planner 输出是否值得执行”单列成一组指标，否则很容易把 packet 设计、code 生成、动作生成和 controller 执行混成一个总成功率。

| 指标 | 定义 | 用途 |
|---|---|---|
| **VPR (Verified Packet Rate)** | planner 输出经 semantic + geometric + budget 三门验收后被放行的比例 | 判断 planner 产出中真正可执行的部分有多少 |
| **FER (False Execute Rate)** | 本应被 verifier 拒绝但仍被放行并导致失败的比例 | 防止 verifier 只是形式存在 |
| **URR (Useful Rejection Rate)** | 被 verifier 拒绝后经重规划/升级路由最终转为成功的比例 | 衡量“拒绝执行”是否真的有价值，而不是徒增保守性 |
| **Gate Latency Overhead** | verifier 引入的额外时延与显存开销 | 防止 verifier 本身把 L3 机载预算吃掉 |

### 4.3++ 统一实验记录模板（R787 新增）

每个实验都按同一行记录，避免后续又回到“只有结论没有证据”。

| Experiment ID | 任务类型 | baseline 家族 | L0 结果 | L1 结果 | L2 结果 | L3 结果 | 主失败模式 | 是否继续 |
|---|---|---|---|---|---|---|---|---|
| D06-E?? | indoor-search / outdoor-search / relocalization / onboard | B1/B2/B3/B4 | grounding / relocalization | SR / recovery | collision / energy | latency / fps | 感知掉线 / 搜索偏移 / 轨迹不可飞 / 板载超时 | yes / no |

**强制规则**：
- 先写失败模式，再写“是否有效”，防止把不同层失败混成一个总分。
- 只要 L0 没过，L1/L2 不得直接拿来做主结论。
- 只要 L3 没过，该方法默认不能进入龙虾机载候选。

### 4.3+ 四层统一验收矩阵（R783 新增）

> 目的：把近几轮反复收束出的 D06 主线真正压成可执行评测，而不是继续停留在“APEX + AirNav + 若干补件”的口头判断。

| 验收层 | 代表路线 | 核心问题 | 主指标 | 典型失败解释 |
|---|---|---|---|---|
| **L0 感知/接地前测** | UAVReason / VLM-Nav / Beyond Matching to Tiles | 目标到底有没有被看见、认对、对齐到全局 | tiny-object grounding、cross-view relocalization、orientation error | 目标根本没被正确ground，不该算导航器失败 |
| **L1 搜索/探索主线** | APEX / 3D VL-Frontier / AirNav-style policy | 开放词汇目标搜索能否稳定找到目标 | SR、SPL、探索步数、重规划恢复率 | 搜索策略无效、前沿选择偏移、历史记忆断裂 |
| **L2 执行/动力学约束** | Dynamics-aware scorer / Fly0 / AutoFly | 路径是否真的可飞、可恢复、能耗可接受 | 碰撞率、急转向次数、单位成功能耗、轨迹平滑度 | 目标找对了，但飞不过去或代价过高 |
| **L3 机载部署成本** | OpenFly keyframe/token merge / QuadAgent runtime / 轻量VLM | 方法能否在机载算力下闭环运行 | 平均延迟、峰值显存、机载帧率、掉帧恢复 | 方法离线分高，但板载根本跑不动 |

**使用规则**：
1. 任何主实验都先过 L0，再比较 L1/L2，不把感知失败误记成策略失败。
2. 若两条路线在 L1 接近，则优先看 L2/L3，避免“找得到但飞不稳/跑不动”的伪优势。
3. D06 主论文的最小对照应固定为三类：**显式 frontier 主线**、**轻量端到端基线**、**运行时补件方案**。

### 4.3+++, 三段诊断协议（R797 新增）

> 来自 **HTNav (2604.08883)** 的直接启发，不再只把分层框架当成“又一个 baseline”，而是把 D06 的失败拆成三段单独记账。

| 诊断层 | 对应模块 | 核心问题 | 主指标 | 典型失败 |
|---|---|---|---|---|
| **D1 地图构建质量** | 动态增量地图 / 3D VL-Frontier | 地图是否稳定保留目标相关结构与可通行区域 | map IoU、frontier recall、目标候选召回率 | 地图断裂、障碍漏建、目标区域被抹掉 |
| **D2 航点选择质量** | 全局 planner / frontier scorer | 被选中的 waypoint 是否真的缩短到目标的搜索路径 | waypoint hit rate、无效绕路率、单位成功步数 | waypoint 总是偏向高语义噪声区域 |
| **D3 局部执行回稳能力** | reactive controller / dynamics-aware scorer | 局部执行偏航后能否快速回到可行航线 | replanning latency、回稳时间、局部碰撞率 | 已找到大方向，但局部控制把优势耗光 |

**使用方式**：
- 对任何分层方法，必须同时给出 D1-D3，避免只报总成功率。
- 若 D1 差，优先修地图或前沿抽取；若 D2 差，优先修语义评分/全局策略；若 D3 差，优先修动力学约束与局部控制。
- 这组协议特别适合比较 **HTNav / APEX / 我们的 3D VL-Frontier**，因为三者都显式包含“地图-决策-执行”三段。

### 4.4 消融实验设计（细化版）

| 编号 | 消融变量 | 对比设置 | 验证假设 | 预期差异 |
|------|---------|---------|---------|---------|
| **A1** | 3D体素前沿 vs 2D平面前沿 | VLFM 2D baseline 直接迁移到空中 | C1: 3D体素对空中探索是必需的 | SR↑ / SPL↑（尤其垂直维度丰富场景） |
| **A2** | 有/无动力学约束 | Frontier选择代价 = 纯距离 vs 距离+动力学安全性评分 | C2: 动力学感知提升飞行安全性 | 碰撞率↓ / 能量效率↑ / 路径可行性↑ |
| **A3** | NtM统一架构 vs 两阶段独立 | 先纯导航后接操作 vs 联合end-to-end | C3: 统一架构避免模式切换碎片化 | 联合成功率↑ / 切换延迟↓ |
| **A4** | VLM语义评分 vs 纯几何贪心 | Frontier评分 = VLM(text,图像) vs 最近前沿 | 无VLM时探索方向随机性更高 | 有VLM时SR↑ / 探索步数↓ |
| **A5** | 解耦 explorer vs 端到端 | APEX式分层 vs 直接pixel→action | 模块拆分提升长时序稳定性 | 长距离任务 SPL↑ / 遮挡恢复↑ |
| **A6** | 有/无关键帧选择+token merging | OpenFly式压缩历史 vs 全帧输入 | 轻量压缩对机载部署至关重要 | 推理延迟↓ / 内存↓ / 精度损失最小化 |
| **A7** | RGB-only vs RGB+pseudo-depth | AutoFly路线 | 轻量深度先验增强空间推理 | 避障成功率↑ / 连续帧位姿一致性↑ |
| **A8** | 轻量端到端 vs 显式frontier | AutoFly伪深度基线 vs 我们方案 | 验证"前端压缩+后端显式"路线优势 | 开放词汇目标搜索SR↑ / 显式地图可解释性↑ |
| **A9** | 原始VLM打分 vs ViSA structured prompting | ViSA式structured visual prompting增强 | 结构化视觉提示增强空间推理 | 复杂场景SR↑ / 目标误识别率↓ |
| **A10** | Frontier主线 vs Fly0三段解耦 | 我们的3D frontier+动力学约束 vs MLLM grounding+几何投影+几何规划 | 验证“显式搜索”与“先ground再规划”谁更适合开放词汇空中任务 | 已知目标场景延迟↓，开放搜索场景我们方案SR↑ |
| **A11** | 同为分层框架时谁真正更稳 | HTNav / APEX / 我们的 3D VL-Frontier | 验证分层方法的优势到底来自地图、航点还是局部控制 | 用 D1-D3 三段诊断协议拆开比较，而不是只看最终 SR |
| **A12** | frontier 搜索 vs 语义记忆规划 | APEX / 3D VL-Frontier vs CityNavAgent-style planner | 验证长航程城市任务里，全局语义记忆是否比显式前沿探索更稳 | 看 long-range waypoint consistency、memory hit rate、恢复后额外绕路率 |
| **A13** | 云端强模型 vs 机载小模型规划 | 云端 VLM/VLM+planner vs Ro-SLM-style onboard SLM planner | 验证 L3 阶段真正的瓶颈是视觉前端还是语言规划链路 | 看复杂指令 SR、onboard replanning latency、断网条件成功率 |
| **A14** | 子目标规划固定时,控制接口是否决定可飞性 | 同一高层语义/waypoint 规划器下, 直接动作执行 vs SkyVLN-style NMPC tracking | 验证 D06 的 L2 不该只看“找没找到路”,还要单列“能不能稳定把子目标飞出来” | 看轨迹平滑度、急转向次数、局部碰撞率、replanning 后回稳时间 |
| **A15** | 共享 planner 的公平接口对照 | 固定同一地图、同一 waypoint 生成器,只替换 controller shell（direct policy / safety shell / NMPC shell） | 防止把高层搜索器优势误写成低层控制优势 | 看 WCES、Recovery Half-Life、Controller Regret@Shared Plan、Interface Overhead |
| **A16** | planner 输出格式是否决定执行稳定性 | 同一 planner backbone 下比较 `自由文本子目标` vs `pose-only waypoint` vs `Semantic Waypoint Packet` | 验证 D06 的瓶颈是否部分来自 planner-controller 接口过松 | 看 WCES、接口解析失败率、重规划次数、机载时延 |
| **A17** | 固定机载/固定云端 vs 预算感知路由 | `always-onboard` vs `always-cloud` vs `budget-aware router` | 验证 B6 的真实价值是不是“低复杂任务留机载,高复杂任务按需升级” | 看 LPC、Escalation Precision、Budget Violation Rate、Degraded-Mode Survival |
| **A18** | Packet-first vs Code-first planner realization | 同一机载小模型容量下比较 `Semantic Waypoint Packet` 输出 vs `代码/动作脚本生成` 输出 | 验证 D06 主线是否该优先把机载 planner 固定为结构化 packet，而不是直接生成执行脚本 | 看 WCES、接口解析失败率、平均规划时延、Safety Violation、Degraded-Mode Survival |
| **A19** | 直接执行 vs verifier-gated execution | 在同一 planner backbone 下比较 `planner→controller` 与 `planner→verifier→controller`，并统一覆盖 packet / code / action generation 三类输出 | 验证 D06 是否必须把 verifier 准入门写成默认执行协议，而不是附属补件 | 看 VPR、FER、URR、Gate Latency Overhead，以及总任务成功率 |
| **A20** | verifier 拒绝后的恢复梯度是否真的救任务 | 在统一 verifier 下比较 `reject→直接停机`、`reject→local retry`、`reject→packet repair`、`reject→replan/escalate` 四类策略 | 验证 D06 的关键不只是“拦住坏输出”，而是“拦住后能否高质量恢复” | 看 Reject Recovery Success、平均恢复步数、Escalation Precision、额外时延与安全违例 |

**关键验收指标（A1-A9通用）**：
- SR@1/3/5（1/3/5次尝试内成功率）
- SPL（路径效率）
- 探索步数/飞行距离
- 能量消耗（空中特有）
- 碰撞率（安全指标）

### 4.5 硬件需求矩阵

| 组件 | 最低配置 | 推荐配置 | 用途 |
|------|---------|---------|------|
| 仿真训练 | RTX 3060 12G / Mac M1 Pro | RTX 4090 × 2 | UE5.7 + AirSim 并行环境 |
| VLM 推理 | Qwen-VL-7B (API或本地) | InternVL-3B 本地或 API | Frontier 语义评分、目标解析 |
| 真机控制 | 机载 Jeston Orin / Raspberry Pi 5 | 机载 Jetson Orin NX | 低层飞行控制、视觉采集 |
| 数据存储 | 500GB SSD | 2TB NVMe | 仿真回放数据、点云地图 |

**分布式仿真方案**（加速数据采集）：
- AirSim 多实例并行（同一机器开 4-8 并行环境）
- 或使用 AirSpark UE5.7 多实例集群（主人已有部署经验）

### 4.6 最小可验证实验路径（R776 起，R811 扩到接口公平性）

> 目标：先用最小代价验证 C1/C2/C3 不是空想，再决定是否扩成完整论文主线。

#### P0：一周内先跑通的 4 组实验
1. **E1, 3D frontier 必要性验证**
   - 对比：2D VLFM 迁移版 vs 3D voxel frontier
   - 场景：室内楼梯/夹层、室外桥下/高低差街区各 2 个
   - 验收：若 3D frontier 在高低差场景 `SR@3` 提升 ≥10%，则 C1 站住
2. **E2, 动力学约束是否真有用**
   - 对比：纯语义前沿打分 vs 语义+动力学联合打分
   - 指标：碰撞率、急转向次数、单位成功能耗
   - 验收：若碰撞率下降 ≥20% 且成功率不降，则 C2 站住
3. **E3, 显式 frontier vs 轻量端到端**
   - 对比：我们的 3D frontier 路线 vs AutoFly/AerialVLA 风格 RGB-only 轻量基线
   - 指标：开放词汇目标搜索 SR、重规划恢复率、推理延迟
   - 验收：若我们方案在 SR 或恢复率显著更优，且延迟仍可控，则主线继续保留
4. **E4, 共享 planner 的 controller shell 公平性验证**
   - 对比：固定同一全局地图与 waypoint planner，只替换 `直接动作执行 / safety shell / NMPC shell`
   - 指标：WCES、Recovery Half-Life、Controller Regret@Shared Plan、Interface Overhead
   - 验收：若 controller shell 能在不显著拉高 L3 成本的前提下稳定提升 WCES 或缩短 Recovery Half-Life，则 B7/A14/A15 继续保留；否则 D06 论文主叙事不把控制壳层写成核心贡献
   - 附加约束：E4 统一使用 `Semantic Waypoint Packet`，禁止某一控制器额外读取 planner 私有中间状态，保证 shared-plan 公平性

#### 数据与实现优先级
- **优先环境**：先 AirSpark/UE5 复用主人现有资产，再补 CARLA-Air 做空地统一对照
- **优先目标类型**：单车、消防栓、行人、路牌 4 类，覆盖静态/细长/易混淆目标
- **优先观测**：RGB + 深度/伪深度二选一，不首轮就上多模态堆料

#### 决策门槛
- 若 E1/E2 都成立，继续写完整 Method + Experiment 主线
- 若 E1 成立但 E2 不成立，主线收缩为“3D frontier + 轻量安全壳”
- 若 E1/E2 成立但 E4 不成立，主论文只把 controller shell 作为工程补件，不写成核心方法贡献
- 若 E1 也不成立，D06 暂不做主论文，转为服务龙虾工程 baseline

## 五、论文写作计划

### 5.1 会议路由与投递判据

| 路线 | 目标 venue | 适用条件 | 当前判断 |
|---|---|---|---|
| **主投路线** | **ICRA 2027** | E1/E2 成立，且 B1 相比 B2/B3 在开放词汇搜索或恢复率上有明确优势 | **当前首选** |
| **备投路线A** | **IROS 2027** | 方法有效但真机或机载部署完成度略弱，仍有系统性实验闭环 | 可保留 |
| **备投路线B** | **RAL + ICRA Option** | 若形成较完整系统实现与可复现实验，但时间线压缩 | 作为保险 |

**当前投稿判断**：D06 更适合冲 ICRA 2027，因为它的方法贡献是 `3D frontier + dynamics-aware scorer + NtM接口` 的系统组合，不只是工程报告。只要 4.6 的 E1/E2 站住，论文主轴就足够清晰。

### 5.2 章节落稿顺序（按最小成稿链路）

1. **Method 先行**：先写清 `3D VL-Frontier / dynamics-aware scoring / NtM handoff`，避免后续实验做完却没有统一叙述。
2. **Experiment 第二**：固定按 `L0 → L1 → L2 → L3` 写，先报告失败类型，再报告总分。
3. **Introduction 最后收束**：等 E1/E2/E3 跑完，再把“为什么空中VLN不能直接照搬地面VLN”压成最终故事线。

### 5.3 时间线与交付物

| 阶段 | 时间 | 最低交付物 | 放行条件 |
|---|---|---|---|
| **Phase A 方法冻结** | 4月下旬 | Method 图 + 4.6 三组最小实验脚本清单 | 不再继续扩主骨架 |
| **Phase B 最小证伪** | 5月上旬 | E1/E2/E3 首轮结果表 + 主失败模式 | 至少确认 C1/C2 是否成立 |
| **Phase C 主实验** | 5月中下旬-6月 | 室内/室外/回锚三条实验路由结果 + baseline 总表 | B1/B2/B3 至少形成一张完整对照表 |
| **Phase D 机载与真机补证** | 7月 | 龙虾或等价机载闭环演示 + L3 成本表 | 至少一条路线可机载闭环 |
| **Phase E 论文成稿** | 7月下旬-8月 | 6页主文 + 图表 + Appendix 提纲 | 进入投稿打磨 |
| **投稿窗口** | 8月底-9月初 | ICRA 2027 主投包 | DDL 前两周冻结结果 |

### 5.4 写作时必须守住的论文叙事

- **主问题**：空中 VLN 的核心不是“再换一个更大的 VLM”，而是 `3D 搜索表示 + 可飞行执行约束 + 机载闭环成本` 同时成立。
- **新增提醒**：L3 机载层不能只写成“视觉 token 压缩后能跑起来”，还要回答 **语言规划本身是否能下沉到机载小模型**，否则方法很可能在断网或高时延链路下失效。
- **R815 新提醒**：即使机载 planner 能跑，也不能默认“全任务都留本地”，而要把 **复杂度分桶 + 预算感知路由** 写成正式协议，明确哪些任务该本地完成、哪些任务该升级云端/强模型、断网时如何 fallback。
- **R823 新提醒**：D06 也不能只写“verifier 把不安全输出拦下来”，还必须写清 **Reject-and-Recover Ladder**，即被拒绝后到底是 `local retry / packet repair / replan / escalate` 哪一种。否则 verifier 只是把撞墙改成卡死，并没有提升可部署性。
- **补充提醒**：L2 也不能只写“有动力学约束项”，还要回答 **同样的高层子目标送给不同控制接口时，谁更能稳定执行**，否则很容易把控制壳层收益误记成搜索策略收益。
- **主对照**：必须固定比较 **显式 frontier 主线**、**轻量端到端基线**、**几何/运行时补件** 三家族，不能只挑对自己友好的基线。
- **主证据**：至少给出一组“找得到但飞不稳”和一组“飞得稳但找不到”的失败案例，证明四层验收矩阵不是形式主义。

## 七、进展日志
- 2026-04-20 R842: 本轮按轮换主推进 **D06**，严格先看本地方向文档、近 30 天 L1 笔记与 QMD 结果，重点复核了 **OnFly / HTNav / AutoFly / AerialVLA / VLM-Nav** 等本地锚点；QMD 检索 `aerial VLN verifier recovery packet stage handoff` 仍主要回流现有 D06 文档与知识Wiki source 页，没有形成需要立即完整入库的新高价值论文，因此本轮未触发 arXiv / Tavily 外扩，也无新论文入库。Phase 2 的核心推进不是再补 recovery 动作，而是把 **首轮最小执行包** 正式写死：已在 `REPORT.md` 新增 `hard-stop vs verifier+recommendation vs verifier+search-only recovery` 三档主对照、统一 `Semantic Waypoint Packet`、以及只记 `search / approach` 两阶段的默认执行规则。核心价值是把 D06 从“知道首轮后该保留哪条主叙事”继续推进到“知道首轮到底先跑哪三个对照、跑完默认冻结什么”，避免 verifier / routing / recovery / supervisor 继续并行摊大饼。

## 六、后续 TODO

- [x] 按 L0-L3 四层统一验收矩阵补一张实验记录模板，后续所有 D06 baseline 统一走同一张表
- [x] 新增一组 `shared planner vs planner+NMPC controller shell` 对照,验证 B7/A14 是否真的降低局部执行失败
- [x] **R811**: 新增 planner-controller 接口专用指标（WCES / Recovery Half-Life / Controller Regret@Shared Plan / Interface Overhead），并把最小实验路径扩成 E1-E4 四组，正式把“planner 收益”和“controller shell 收益”拆开记账
- [x] **R812**: 基于 OnFly / HTNav / OpenFly / Ro-SLM 的本地回扫，补出 `Semantic Waypoint Packet` 接口契约，新增 B8 / A16，并要求 E4 统一走 shared packet 公平对照
- [x] **R815**: 基于本地 `Ro-SLM / AerialVLN Survey / ORION` 回扫，把 D06 的机载层从“能否本地规划”推进到“何时本地规划、何时升级云端”的 **复杂度分桶 + 预算感知路由** 协议，新增 `LPC / Escalation Precision / Budget Violation Rate / Degraded-Mode Survival` 与 A17
- [x] **R815**: 明确 `Packet-first > Code-first` 的 D06 主线判断，把 `Semantic Waypoint Packet` 固定为 planner-controller 统一中间层，并新增 B9 / A18 用于单独比较代码生成式机载规划器的真实边界
- [x] **R818**: 基于本地 `OnFly / Ro-SLM / ORION` 回扫，把 D06 的执行链从“planner 输出后直接交 controller”推进为默认 `planner → verifier → controller`，新增 `VPR / FER / URR / Gate Latency Overhead` 与 A19，用统一准入门公平比较 packet / code / action generation 三类路线
- [x] **R823**: 基于本地 `OnFly / HTNav / AutoFly / ORION` 回扫，把 D06 从“verifier 是否存在”继续推进到“verifier 拒绝后系统如何恢复”的 `Reject-and-Recover Ladder`，新增 `A20`，要求统一比较 `retry / repair / replan / escalate` 四类恢复策略，避免 verifier 只会把失败从撞墙改成卡死
- [x] **R830**: 基于本地 `OnFly / HTNav / AutoFly` 回扫，把 recovery 主叙事进一步收束为 **stage-bounded recovery**，新增“恢复线部署边界与阶段化保留原则”，并要求用 `SC15` 比较 `统一在线恢复 / 仅 search 在线恢复 / recommendation-only` 三种部署策略，优先回答 recovery 该保留在哪一段而不是继续追总恢复率
- [x] **R843**: 外部补扫新增 **FineCog-Nav (2604.16298)**。已将 D06 的新增问题从“恢复线还能否继续展开”进一步收束为 **planner 内部是否值得显式拆成细粒度认知模块**。在 `REPORT.md` 新增 3.2.12，明确它不改写 `packet-first + verifier-first` 主骨架，而是作为 `planner-inside baseline family`，专门比较 `instruction adherence / memory-to-waypoint conversion / structured module I-O` 的净收益；同时在 `experiments.md` 新增 **SC7.5**，要求统一比较 HTNav / APEX / CityNavAgent 与 FineCog-Nav-style 模块化 planner，避免把“模块更多”直接误写成方法更优。
- [x] **R842**: 将 README 中 `UAV-Track VLA (2604.02241)` 状态由候选更新为已入库，并在 `experiments.md` 新增 **SC21 阶段净收益冻结** 与 **SC22 tracking-heavy end-to-end baseline 边界比较**，把 D06 进一步收束为“先判断 recovery 在哪一阶段真有净收益，再判断 UAV-Track VLA 这类连续跟踪路线更适合放在哪个执行层”
- [ ] 深挖 VLFM/NaVILA 源码,分析空中迁移可行性
- [ ] 深挖 OnFly/UAV-Track VLA 架构,分析与我们框架的差异
- [x] **R763**: 新增 arXiv:2604.13654 系统综述 + 2604.07705 合并更新；新增 Aerial VLN Unified (arXiv:2512.08639)；对比表扩展至5路；C1/C2创新必要性获roadmap直接确认
- [x] **R772**: 新增 MotionScape (2604.07991) 世界模型训练数据集；新增 CARLA-Air (2603.28032) 统一仿真环境；3.2.1节给出3D VL-Frontier Map 技术 instantiation（体素地图+VLM语义评分+动力学可行性评分）
- [x] **R778（本轮）**: 扫描发现2个未入库新论文候选：①VLM-Nav (PLOS One 2026-04-03, DepthAnything-V2+VLM无地图UAV导航，零样本障碍回避) ②Beyond Matching to Tiles (2026-04-11, 无人机+卫星视角对齐，vision-only UAV导航)；引用追踪确认 AIR-VLA(2603.25038) 在机器人论文日报高频出现，引用热度上升；arXiv API 今日网络不通，改用 Tavily 搜索，工具链降级正常
- [x] **R780**: 新增 Fly0 (2602.15875) 作为“语义 grounding 与几何规划解耦”强基线。已把它补入相关工作，并新增 A10 对照实验，用来直接比较“显式3D frontier搜索”与“先ground再几何规划”在开放词汇空中任务里的边界。
- [x] **R782**: 入库 **VLM-Nav** 与 **Beyond Matching to Tiles**；前者补齐 D06 的单目无地图机载 baseline，后者补齐 cross-view global-local grounding / 长航程重定位支线；并完成本轮工具链体检（arXiv/Tavily/PDF 正常，web_fetch 受限，QMD 退化，memory_search 偏弱）。
- [x] **R797**: 结合 **HTNav (2604.08883)** 把分层方法比较从“总成功率”推进到 **D1地图构建 / D2航点选择 / D3局部回稳** 三段诊断协议，并新增 A11 对照实验。
- [ ] 复用 OpenFly 的关键帧选择 + visual token merging 思路,验证是否适合作为龙虾当前 VLM 前端压缩层
- [ ] 龙虾项目 GoalSearch 实验数据整理,作为 baseline
- [x] 3D VL-Frontier Map 的技术方案设计 → 见 3.2.1 节
- [ ] 确定 UE5 仿真场景方案(CARLA-Air 优先 or AirSpark 复用)
- [ ] 与主人讨论实验服务器资源安排
- [x] **R776**: 新增 4.6「最小可验证实验路径」，把 D06 收束成 E1/E2/E3 三组最小实验与继续/收缩/转baseline 的决策门槛
