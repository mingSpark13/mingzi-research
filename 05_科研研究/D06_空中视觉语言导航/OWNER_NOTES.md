# D06 空中VLN — 主人批注 (Owner Notes)

> 📌 **花火必读**：每次推进 D06 研究前，先读此文件，按最新批注调整 PAPER.md 方向。
> 主人可随时在此添加批注，花火下次 Heartbeat 时自动生效。

---

## 📋 批注格式说明

每条批注请按以下格式添加（花火会按时间倒序读取，最新的优先级最高）：

```
### [YYYY-MM-DD] 批注标题
**类型**: 方向调整 / 创新点 / 实验要求 / 写作风格 / 其他
**优先级**: 🔴 立即执行 / 🟡 下轮执行 / 🟢 长期参考

内容...
```

---

## 📝 主人批注区

### [2026-05-26] 拆分为两篇论文：数据集论文 + 方法论文
**类型**: 方向调整  
**优先级**: 🔴 立即执行

当前 PAPER.md 的四个贡献点（C1 地图创新 + C2 策略创新 + C3 框架创新 + C4 数据集）范围太广，一篇论文撑不住。应拆成两篇独立论文，各自聚焦：

**论文一：AirManip-Bench（数据集与 benchmark 工作）**
依托 AirSpark 平台，核心贡献是：城市低空 Navigate-then-Manipulate benchmark，覆盖 Search→Track→Approach→Contact→Recovery 完整链路，提供多类接触操作、动力学感知评测、Sim2Real 配对验证、自动化 episode 生成。这篇不需要提出新的导航算法，重点是"我们建了什么、评测了什么、现有方法在哪里失败"。

**论文二：方法论文（D06 核心方法）**
聚焦导航策略本身，贡献收窄为：3D 语义前沿图（C1）+ Semantic Waypoint Packet 接口（原 C3 的 planner→controller 部分）。动力学感知（C2）作为方法的一个组件而非独立贡献。NtM 框架作为应用场景，不作为独立贡献。用论文一的 benchmark 作为评测平台。

**对 PAPER.md 的引导**：
- 把 C4（数据集）从当前 PAPER.md 中剥离，归入 AirManip-Bench 论文
- 把 C3（NtM 架构）降级为方法论文的"应用场景"，不作为独立贡献
- 方法论文的核心主张收窄为：**Semantic Waypoint Packet + 3D VL-Frontier Map 的组合，是让 aerial VLN 从"能导航"变成"能交付给控制器执行"的关键接口**
- 两篇论文共享 AirSpark 平台，数据集论文先出，方法论文用其 benchmark 评测

---

### [2026-05-26] D06 与 AirSpark 工程平台的结合方向
**类型**: 方向调整 + 实验要求  
**优先级**: 🔴 立即执行

**核心判断**：D06 不应该继续在纸面上堆路由规则。AirSpark 已经是一个真实可用的仿真平台（P0-P2 已完成，UE5.7 + AirSim + MuJoCo + 批采集系统），它就是 D06 缺少的实验基础设施。两者应该合流，而不是平行推进。

**三者分工**：
- **AirSpark** = 平台与 benchmark 基础设施（数据采集、episode 生成、评测）
- **D06** = 导航层研究（VLN → 3D 语义前沿图 → Semantic Waypoint Packet → 控制器）
- **D07** = 操作层研究（机械臂高频稳定器 → 接触操作 → 负载扰动恢复）

AirSpark 的 P5 目标（Navigate-then-Manipulate 完整链路）正是 D06 的 C3 贡献（NtM 架构）+ D07 的核心能力（高频臂控）的自然落地场景。

**对 D06 PAPER.md 的引导**：

1. **实验平台明确化**：D06 的实验应在 AirSpark（UE5.7 城市场景）上跑，而不是假设一个抽象仿真环境。AirSpark 的 BatchControllerSubsystem + WaypointExecutor 已经可以驱动 episode，D06 的 Semantic Waypoint Packet 应该直接对应 AirSpark 的 WaypointExecutor 接口格式。

2. **Semantic Waypoint Packet 的工程锚点**：D06 的 `goal_type / target_pose / yaw_hint / altitude_band / semantic_confidence / progress_score / safety_budget` 这些字段，应该和 AirSpark 的 episode schema（`manifest.json / frames.jsonl / actions.jsonl`）对齐，而不是停留在论文里的抽象定义。

3. **NtM 的实验路径**：AirSpark P5 的"导航→操作全链路"就是 D06 C3 的实验场。D06 不需要另起炉灶建仿真环境，直接在 AirSpark 的城市场景里跑 Search→Track→Approach→Contact 链路即可。

4. **停止堆路由规则**：当前 PAPER.md 的 Section 4.2 已有 50+ 子节全是"subtraction 规则"，在没有实验数据之前继续添加没有价值。下一轮应把精力放在：把 AirSpark 的 WaypointExecutor 接入 D06 的 planner 输出，跑出第一批真实 episode 数据。

**与 D07 的接口**：D06 负责把无人机导航到目标附近（输出 Semantic Waypoint Packet），D07 负责在无人机漂移情况下保持末端高精度跟踪（接管 Contact 阶段）。两者的接口边界是"目标进入操作范围"这一时刻，对应 AirSpark 任务链路里的 Approach→Align→Contact 切换点。

---

---

## 📊 花火执行记录

> 花火每次读取此文件后，在此记录已响应的批注（避免重复执行）。

| 日期 | 响应的批注 | 执行动作 |
|------|-----------|---------|
| 2026-06-10 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：先做本地优先扫描，近 30 天 L1 命中 **WorldFly / AirDreamer / FLIGHT VLA**，QMD 仍主要回流 D06 README/REPORT 与既有 AerialVLA source；未发现需要新增完整入库的 executor-facing 新论文，但确认 **FLIGHT VLA (2606.06836)** 适合作为“长时程异步推理-控制”邻近基线。Phase 2 直接推进 PAPER.md：在 **2.2** 补入 FLIGHT VLA 的 baseline family 定位，在 **2.21 Limitations** 新增两条缺口，明确现有异步长程 UAV 系统仍未证明中间对象是 WaypointExecutor-consumable packet，并在 **3.8** 增加 `Q^{async}_{lh}` 审计项，把 long-horizon progress discipline 与 AirSpark-schema-aligned packet accountability 显式拆开，继续把方法主张锁定为可序列化、可消费、可追责、可重建的 Semantic Waypoint Packet 接口。 |
| 2026-06-08 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：先做本地优先扫描，QMD 仍主要回流 D06 README/REPORT 与既有 OpenFly / AerialVLA / AirNav 锚点，未发现值得完整入库的新 executor-facing 论文，因此正式新增入库 0 篇。Phase 2 直接推进 PAPER.md：在 **2.21 Limitations** 追加两条 executor-facing 缺口，明确现有工作仍混淆 *controller-consumable command compactness* 与 *cross-log replay equivalence*，且几乎不报告 packet 是否能从 `manifest.json / frames.jsonl / actions.jsonl` 三面日志中事后重建；同时重写 **3.4 WaypointExecutor-Aligned Packet Serialization, Consume-Time Logging, and Post-hoc Reconstruction Contract**，把 `C_{ser}`、`E_t=(emit,auth,bind,consume,trace)` 与 `R_{pkt}` 后验重建算子写实，继续把方法主张锁定为可序列化、可消费、可追责、可重放、可重建的 Semantic Waypoint Packet 接口。 |
| 2026-06-07 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：本地优先回扫近 30 天 L1 命中 **AerialVLA / OnFly / AirNav / LookasideVLN / LiveVLN / LMPath / StereoNav / AgentVLN / PEACE**，QMD 仍主要回流 D06 README/REPORT 与既有 source；补查 arXiv 最新 3 篇后，真正与当前 executor-facing 主张直接相关的仍是 **HANDOFF (2606.06493)** 这条 controller-interface abstraction 邻近线，但它已在当前 PAPER 吸收为 support family，因此本轮正式新增入库 0 篇。Phase 2 继续推进 PAPER.md：在 **2.21 Limitations** 新增两条缺口，明确现有工作仍缺少“controller-consumable command compactness vs cross-log replay equivalence”的分离报告；进一步把 D06 的方法主张收束为 **Semantic Waypoint Packet 不仅要易于控制器消费，还要在 AirSpark 的 manifest/frames/actions 三面日志中保持可追责、可重放、可重建的一致 semantic thread**。 |
| 2026-06-07 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：先做本地优先扫描（QMD 仍主要回流 D06 README/REPORT 与既有 AerialVLA source；近 30 天本地 L1 回扫 AerialVLA 与 UAV-VLN Survey，外部 arXiv 补充未发现值得完整入库的新 executor-facing UAV 论文），随后在 PAPER.md 的 **2.20 / 2.21** 新增 HANDOFF 作为 controller-interface abstraction baseline，把“紧凑控制器可消费命令空间”单列为独立扣减家族，进一步压实 D06 主张必须超越 *typed plan / world-model foresight / POI final-meters / responsive-agent / controller-interface abstraction* 五类解释，才能升级为完整 Semantic Waypoint Packet contract。 |
| 2026-06-05 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：先做本地优先扫描（QMD 仍主要回流 D06/REPORT、本地 survey 与既有 source；新回扫近 30 天本地 L1 的 **ImagineUAV (2606.01205)**、**AirDreamer (2606.03252)**、**PEACE (2606.00104)**，判断它们都属于 world-model / planner-executor 邻近支持族而非直接 packet-contract 证据，因此未触发新增入库），随后在 PAPER.md 的 **2.20** 与 **3.4** 补进 world-model 邻近基线的证据边界：明确 ImagineUAV/AirDreamer 可解释上游 foresight、kinodynamic feasibility 与 generalist robustness，但若未闭合 `C_{ser}/e^{auth}/e^{bind}/e^{consume}/c^{trace}`，只能冻结为 planner-side/world-model support，继续把方法主张锁定为可序列化、可消费、可追溯、可重建的 Semantic Waypoint Packet 接口 |
| 2026-06-05 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：先做本地优先扫描（QMD 仍主要回流 D06/REPORT、AerialVLA 与既有 source，近 30 天本地 L1 仍未发现新的成熟 executor-facing 论文，因此未触发新增入库），随后在 PAPER.md 的 2.20 与 3.4 继续压实 AirSpark 对齐证据：新增 post-hoc reconstructability 缺口，并把 `C_{ser}` 与 `R_{pkt}/c^{trace}` 分离，明确 packet 不仅要可序列化、可绑定、可消费，还要能从 `manifest.json / frames.jsonl / actions.jsonl` 事后重放成同一 semantic thread，进一步把方法主张锁定为可审计、可重建、可被 WaypointExecutor 消费的 Semantic Waypoint Packet 接口 |
| 2026-06-04 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：先做本地优先扫描（QMD 仍主要回流 D06/REPORT、AerialVLA、QuadAgent 与既有 source，近 30 天本地 L1 仍未发现新的成熟 executor-facing 关键论文，因此未触发新增入库），随后在 PAPER.md 中新增 QuadAgent-style responsive agent family，把响应式边控/快速重规划收益明确冻结为 `Q^{resp}_{agent}` 与 responsive-agent support，并同步补强 Limitations 与 route-closure，继续把方法主张锁定为可序列化、可追踪、可被 WaypointExecutor 消费的 Semantic Waypoint Packet 接口 |
| 2026-06-04 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：先做本地优先扫描（QMD 仍主要回流 AerialVLA 与既有 D06 source，近 30 天本地 L1 未发现新的 executor-facing 关键论文，因此未触发新增入库），随后修正 PAPER.md 的 Limitations 编号重复问题，并进一步压实 AirSpark 对齐叙事——把 executor-facing 缺口明确收敛到 `C_{ser}`、`e^{auth}`、`e^{bind}`、`e^{consume}`、`c^{trace}` 五类证据，继续把方法主张锁定为可序列化、可追踪、可被 WaypointExecutor 消费的 Semantic Waypoint Packet 接口 |
| 2026-06-01 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：先做本地优先扫描（WorldVLN / AerialVLA / OnFly + QMD 命中 AerialVLA 与既有 D06 报告，未触发新增入库），随后把 PAPER.md 的 Method 与 Experiments 明确补上 executor-view reduction，将 AerialVLA 冻结为 latent execution sufficiency、OnFly 冻结为 runtime continuity support，并把 `Q^{exec}_{view}` 与 `C_{ser}/e^{auth}/e^{bind}/e^{consume}/c^{trace}` 写入 promotion gate，进一步把方法主张收窄到可被 AirSpark WaypointExecutor 消费和审计的 packet 接口 |
| 2026-05-31 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注推进 D06 方法论文：基于本地锚点 AerialVLA / OnFly / LookasideVLN / LiveVLN / LMPath / StereoNav / SAGE / PLMD 回扫后未新增入库论文，直接把 PAPER.md 的 Related Work / Limitations / Method 继续向 AirSpark-WaypointExecutor 对齐，修正 Limitations 编号并压实 packet→`manifest.json`/`frames.jsonl`/`actions.jsonl` 的 serialization 与 consume-time trace contract，进一步把方法主张收窄为可审计、可消费的 Semantic Waypoint Packet 接口 |
| 2026-05-30 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮继续按批注收窄 D06：未扩平台/benchmark 叙事，而是把 PAPER.md 中 WorldVLN / active-perception / world-prior / semantic-completion 四条解释链统一压回 pre-consumption support，并把 `Q^{wam}_{plan}` 显式并入 matched subtraction gate，继续把方法论文重心锁定在 packet→WaypointExecutor 的最小证据栈 |
| 2026-05-28 | 2026-05-26 两条🔴批注（PAPER 拆分收窄 + AirSpark/WaypointExecutor 对齐） | 本轮优先按批注重写 D06 写作重心：继续维持方法论文聚焦 Semantic Waypoint Packet + 3D VL-Frontier Map，并把 experiments 新增 packet→executor schema alignment 门槛，明确 packet claim 需对齐 `manifest.json / actions.jsonl / frames.jsonl` 与 WaypointExecutor 消费字段 |
| — | — | — |
