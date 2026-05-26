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
| — | — | — |
