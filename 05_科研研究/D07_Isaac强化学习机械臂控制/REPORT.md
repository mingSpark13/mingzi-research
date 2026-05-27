# [D07] Isaac Lab 空中机械臂强化学习控制 研究报告

> 最后更新：2026-04-18 | 成熟度：🟡 有方向（R793补入 RL vs optimal control vs hybrid 控制范式对照轴）
> 状态：🟡 推进中

## 0. 本轮推进记录（2026-05-24 01:37）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md / experiments.md`，并回扫近 30 天本地 L1 锚点 **DiSCo / Reactive Dexterous Grasping / Hand-in-the-Loop / Find the Fruit / Q2RL**；补跑 QMD `Isaac Sim reinforcement learning moving-base end-effector guidance --no-rerank` 后，结果仍主要回流 **Isaac Lab / Squint / D07 本地方向文档**，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- Phase 2 核心继续直接推进 **PAPER.md** 与 **experiments.md**：在 `PAPER.md` 新增 **4.18 Guidance-Core Metric Attribution from the Current Local Anchor Set**，把 **copilot / retention / analytic projection / decomposition** 四类 support family 分别冻结到其默认应先解释的 guidance metric（`ΔBDEE / ΔCET / ΔPCST / ΔPGFR`）；同时在 `experiments.md` 新增 **9.8 guidance-family metric-first routing freeze**，把这套“family 必须先赢下自己最自然但仍最弱的 guidance metric，才允许再谈标题升级”的规则显式映射进实验路由。
- 当前最重要的新收束是：D07 现在不只要求所有路线先服从 guidance-first 主表字段，还进一步要求**每类路线先在自己最该赢的那一格里赢得诚实**，否则连 support-side 升格都不能谈；下轮最值钱动作应转向把这些 family→metric 约束继续映射成真实日志聚合脚本与 gate 检查项。

## 0. 本轮推进记录（2026-05-14 18:27）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D04** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，并回扫近 30 天本地 L1 锚点 **TMRL / Q2RL / Reactive Dexterous Grasping / KG-M3PO / DiSCo / RL vs Optimal Control**。本地方向相关笔记已明显超过阈值，且本轮未发现需要完整入库的新高价值论文，因此 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- Phase 2 核心直接推进 **PAPER.md**：在 `Method` 新增 **3.19 Disturbance-Localized Credit Ledger for First-Round D07 Claims**，在 `Experiments` 新增 **4.10 Disturbance-Localized Credit Ledger and Non-Promotion Audit**、**4.11 Minimal Logging Contract for `\Xi_{D07}` Rows**、**4.12 Current Evidence-Consistent Freeze after Local Re-read**，把 reward / retention / projection / exploration / dynamics-set / copilot 六类支持路线统一压进 `\Xi_{D07}` reviewer-facing 记账对象。
- 当前最重要的新收束是：D07 现在不仅有 route freeze 和标题升级闸门，还多了一层 **“哪条线在什么窗口、撑到哪级扰动、还没击败哪些更弱解释”** 的统一记账协议；下轮最值钱动作应转向 `experiments.md`，把 `\Xi_{D07}` 直接映射成真实日志键与首轮结果表模板。

## 0. 本轮推进记录（2026-05-12 22:24）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md / experiments.md`，并回看近 30 天本地 D07 锚点 **Q2RL / Reactive Dexterous Grasping / Isaac Lab**。本轮尝试 QMD 外补仍受 allowlist 限制，未形成可用新增；结合本地方向覆盖情况，**高价值新增论文 0 篇，正式入库 0 篇**。
- Phase 2 核心直接推进 **PAPER.md** 的 `Experiments`，新增 **4.47 Interface-Superiority Freeze against Infrastructure, Retention, and Projection Confounds** 与 **4.48 Minimal Claim Tuple for the First D07 Real Bundle**：前者要求任何 `deployable hybrid` 口径都必须先排除 **平台整洁度收益 / BC-retention 收益 / analytic projection 收益** 这三类更弱解释，后者把首轮真实结果压成统一 claim tuple `Ω_D07=(w^+, w^†, s^†, κ_dom, κ_def, κ_freeze)`，让日志、主表和标题冻结规则用同一个对象对齐。
- 当前最重要的新收束是：D07 现在不仅区分 `reward / retention / projection / interface` 四类 credit，还进一步把 **“击败了哪一个更弱解释族”** 写成标题升级前置条件；下轮最值钱动作应转向 `experiments.md`，把 `Ω_D07` 的字段映射到真实日志键与主表生成脚本。

## 0. 本轮推进记录（2026-05-12 07:21）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，结合近 30 天本地推进记录确认 QMD 近期对 D07 仍主要回流既有 **Isaac Lab / Q2RL / ARM / Reactive Dexterous Grasping** 线索；本轮补充外部兜底时仅确认 **Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning**（arXiv:2511.04831）作为高相关基础设施锚点，未形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 1 篇（平台锚点，已在本地知识链中引用，不新增入库）**、**正式入库 0 篇**。
- Phase 2 核心直接推进 **PAPER.md**，补强 `Section 2.7` 与 `Section 3.6`：前者新增 **Isaac Lab infrastructure-as-variable gap**，明确平台验证纪律与控制接口贡献不能混记；后者把 **Isaac-Lab-native infrastructure discipline** 写成显式 protocol axis，要求 B1-B4 共用 reset / disturbance / logging substrate，避免把平台一致性收益误写成控制方法优势。
- 当前最重要的新收束是：D07 现在不仅区分 `reward / retention / projection / interface` 四类主导 credit，还正式补上了 **platform-enabled reproducibility vs controller-interface gain** 这条解释边界；下轮最值钱动作应转向 `experiments.md`，把 reset 检查、disturbance slicer、日志字段和 gate 触发条件写成真正可跑的实验合同。

## 0. 本轮推进记录（2026-05-11 21:18）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，回扫近 30 天本地 L1 锚点 **ARM / Q2RL / Reactive Dexterous Grasping / Isaac Lab**，并补跑 QMD `Isaac Lab robotic arm reinforcement learning reward shaping recovery advantage model anti-forgetting hybrid control --no-rerank`；结果仍主要回流本地 **ARM** 与既有 D07 文档，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- Phase 2 核心继续推进 **PAPER.md** 的 `Experiments`，新增 **4.41 Reward-vs-Retention Non-Merger Rule for ARM and Q2RL Rows**，正式要求 **ARM 的 reward-origin recovery credit** 与 **Q2RL 的 BC-retention online bridge** 在首张可信主表里分列记账，禁止把 recovery shaping 与 anti-forgetting retention 混写成虚假的 hybrid robustness。
- 当前最重要的新收束是：D07 现在不仅区分 `R_rew / R_ret / R_proj`，还补上了 **reward credit 与 retention credit 不得合并升级** 这条 submission-ready 解释纪律；下轮最值钱动作应转向 `experiments.md`，把这些 tuple 映射成真实日志字段、聚合脚本与 gate 触发条件。

## 0. 本轮推进记录（2026-05-11 20:17）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，回扫近 30 天本地 L1 锚点 **Q2RL / Reactive Dexterous Grasping / ARM / Isaac Lab**，并补跑 QMD `Isaac Lab robotic arm reinforcement learning reward shaping recovery advantage model anti-forgetting hybrid control --no-rerank`；结果仍主要回流本地 **ARM** 与既有 D07 文档，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- Phase 2 核心继续推进 **PAPER.md** 的 `Experiments`，新增 **4.40 Disturbance-Tagged Interpretation Columns for B3 and B4**，把 **Q2RL** 对应的 BC-to-Q 行正式要求标注 `retain@W1/W2/W3 + s^\dagger_ret`，把 **Reactive Dexterous Grasping** 对应的 projection 行正式要求标注 `project-safe@W2 / project-stable@W3 + s^\dagger_proj`，进一步把 B3/B4 从“有主表判线”推进到“有带扰动边界标签的 submission-ready 读表位”。
- 当前最重要的新收束是：D07 现在不仅区分 `R_ret` 与 `R_proj`，还要求这两条部分成功路线显式交代自己究竟保住了 **哪一个窗口、哪一级扰动源**；下轮最值钱动作应转向 `experiments.md`，把这些列位真正映射成日志字段、聚合脚本与 gate 触发条件。

## 0. 本轮推进记录（2026-05-11 19:08）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，回扫近 30 天本地 L1 锚点 **Q2RL / Reactive Dexterous Grasping / ARM / Isaac Lab**，并补跑 QMD `Isaac Lab robotic arm reinforcement learning reward shaping recovery advantage model anti-forgetting hybrid control --no-rerank`；结果仍主要回流本地 **ARM** 与既有 D07 文档，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- Phase 2 核心继续推进 **PAPER.md** 的 `Experiments`，新增 **4.39 Q2RL- and Projection-Aware Main Table Interpretation Rule**，把 **Q2RL** 明确冻结为优先走 `R_ret`（anti-forgetting / retention bridge）解释、把 **Reactive Dexterous Grasping** 明确冻结为优先走 `R_proj`（analytic safety-shell / projection support）解释，要求主表按 `R_seg → R_ret → R_proj → R_rew → R_int` 顺序逐级升格，只有击败更弱家族解释后才允许升级到 deployable hybrid route。
- 当前最重要的新收束是：D07 现在不仅有 submission-ready 首表表头与四句结果段骨架，还正式补齐了 **Q-gated retention** 与 **analytic projection** 两条最容易被误升格的部分成功路线的主表判线规则；下轮最值钱动作应转向 `experiments.md`，把 B1-B4 bundle 细化成真实命令、日志字段与 gate 触发条件。

## 0. 本轮推进记录（2026-05-11 03:59）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，回扫近 30 天本地 D07 锚点与既有实验解释链；当前本地覆盖已足够支撑写作推进，但未形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**。
- Phase 2 核心继续推进 **PAPER.md** 的收尾与 reviewer-facing 结果纪律：补全 `Conclusion`，把 D07 的主结论正式冻结为 **dominant honest gain route** 写法，明确首轮可信表出来后论文只能收成 `acceleration / retention bridge / safety-shell support / relation-aware compensation / deployable hybrid control` 五档之一，不能再把 warm-start、reward shaping、projection 与 hybrid 成果混写成虚胖 whole-body 故事。
- 当前最重要的新收束是：D07 现在不只拥有最小实验包与标题升级闸门，还补齐了结论层的 **诚实降级出口**；下轮最值钱动作应转向 `experiments.md`，把 B1-B4 bundle 落成具体命令、日志字段和 gate 触发条件。

## 0. 本轮推进记录（2026-05-11 02:59）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，并回扫近 30 天本地 D07 锚点与既有实验解释链；当前本地覆盖已足够支撑写作推进，但未形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**。
- Phase 2 核心直接推进 **PAPER.md** 的实验后半段与收尾结构：清理了 `References` 之前误混入的重复实验段落，把 **4.35 Compute-Accountable Bundle Schedule and Stop Rules**、**4.36 Credit-Separated Experiment Table**、**4.37 Negative-Result Routing** 连成一条 submission-ready 结果判线，并补回规范的 `Conclusion` 与引用表。
- 当前最重要的新收束是：D07 现在不只是“知道首轮四行 baseline 怎么跑”，而是已经把 **算力预算 → dominant credit tuple → 失败降级路线** 全部写进论文草稿，后续首张可信表出来后就能直接决定标题该收成 acceleration / retention bridge / safety-shell / deployable hybrid 哪一档。

## 0. 本轮推进记录（2026-05-10 11:59）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与近期主推进 **D06 / D01 / D04** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，回扫近 30 天本地 L1 锚点 **Q2RL / Reactive Dexterous Grasping / ARM / Isaac Lab**，并补跑 QMD `Isaac Lab robotic arm reinforcement learning BC-to-Q warm start anti-forgetting reactive grasping --no-rerank`；结果仍主要回流既有 D07 文档与本地笔记，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- Phase 2 核心直接推进 **PAPER.md**：一方面清理了 Method 中重复的 `3.18 Hierarchical RL Planning with Analytic Safety Projection` 段落，避免草稿结构继续膨胀；另一方面补强 **Section 4.35 Compute-Accountable Bundle Schedule and Stop Rules**，把最小实验包正式冻结为 **3 seeds × 12h matched-compute** 的 B1/B2/B3 与 **4h disturbance-promotion** 的 B4 放行流程，并写死 `SR-1~SR-4` 停止规则。
- 当前最重要的新收束是：D07 现在不只知道“首轮应该跑哪四行 baseline”，还把 **算力预算、种子数、promotion slice 时长、以及何时必须降级叙事** 一并写进论文草稿；下轮最值钱动作应转向 `experiments.md`，把这套 bundle 细化成实际命令、日志字段和 gate 触发条件。

## 0. 本轮推进记录（2026-05-10 03:57）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与近期主推进 **D06 / D01** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，抽读近 30 天本地 L1 锚点 **Reactive Dexterous Grasping / DiSCo / KG-M3PO / RL-Based Sim-Real Co-Training**，并补跑 QMD `Isaac Lab manipulation reinforcement learning sim-to-real aerial manipulator --no-rerank`；QMD 结果仍主要回流既有 D07 文档与本地锚点，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未继续触发 arXiv / Tavily 外扩。
- Phase 2 核心直接推进 **PAPER.md** 的 **Section 4 Experiments**，新增 `4.33 Family-Control-Aware Minimal Experiment Bundle`，把首轮最小实验包正式压缩为 **B1 scratch PPO / B2 BC warm-start / B3 BC-to-Q gate / B4 task-space RL + analytic safety projection** 四行，明确每行都必须击败自己的最近弱解释族（planner-only / retention-only / projection-only / reward-only）。
- 同时补强 `4.34 Title-Claim Freeze by Matched Family-Control Defeat`，把 D07 标题放行条件收紧为：**W3 存活 + 到达 payload disturbance `s_p` + 击败最近 family control + 不再由 reward-origin 主导**，否则只能降级写成 acceleration / retention bridge / safety-shell support / reward-shaped recovery。
- 当前最重要的新收束是：D07 现在不只是“结果出来后知道怎么解释”，而是已经把**首轮最小可跑实验包**和**标题升级闸门**一并冻结；下轮最值钱的动作应转向 `experiments.md`，把这四行 bundle 细化成具体算力预算、种子数和 stop 条件。

## 0. 本轮推进记录（2026-05-09 18:56）

- 本轮按轮换主推进 **D07_Isaac强化学习机械臂控制**，满足“D07 每 3-4 轮覆盖一次”，且避免与上一轮主推进 **D06** 连续重复。
- 严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，抽读近 30 天本地 L1 锚点 **Reactive Dexterous Grasping / Q2RL / Isaac Lab**，并补跑 QMD `Isaac Lab robot arm reinforcement learning manipulation sim-to-real --no-rerank`；QMD 结果仍主要回流既有 D07 文档与本地锚点，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未继续触发 arXiv / Tavily 外扩。
- Phase 2 核心直接推进 **PAPER.md** 的 **Section 4 Experiments**，新增 `4.8 Semantic-State Ablation for Relation-Aware Compensation`、`4.9 Window-Localized Main Table Schema`、`4.10 First-Round Training Schedule and Honest Go/No-Go Rules`、`4.11 Reward-Origin Accountability for Long-Horizon Manipulation`。
- 当前最重要的新收束是：D07 的实验节现在不仅区分 `SEG / PBG / RLG / DHG`，还额外堵住了“reward shaping 带来的 late-window 改善被误写成控制接口创新”的口子；后续首轮结果出来后，可以更诚实地区分 **reward-side recovery shaping**、**anti-forgetting bridge**、**relation-aware compensation** 和 **deployable hybrid control**。

## 0. 本轮推进记录（2026-04-27）

- 22:41~22:49：本轮按轮换主推进 **D07**，严格先做本地优先。复核方向文档与近 30 天本地 L1 锚点后，确认当前最能直接支撑 PAPER 的本地证据是 **Isaac Lab / TIAGo+Isaac / Squint / ViserDex / RoTri-Diff** 五篇。
- 尝试 QMD `Isaac Sim robotic arm reinforcement learning manipulation policy --no-rerank` 仍在 cron 环境下被 SIGKILL，说明 heartbeat 阶段仍应坚持“方向文档 + 本地笔记”为主、QMD 为补，而不是反过来。
- 本轮没有新增需要完整入库的高价值论文，但直接推进了 `PAPER.md`：补全 `Section 3.4 Minimal System Instantiation for the First Round`、`Section 3.5 Layer-Specific Hypotheses`，以及实验部分的 `baseline matrix / disturbance-stratified evaluation / minimal verification questions`。
- 当前最重要的收束是：把四类证据固定为 **SEG（warm-start / sample efficiency）/ PBG（perception bridge）/ RLG（relation-aware local compensation）/ DHG（deployable hybrid gain）**。下轮一旦开始真实实验，就能根据主导稳定增益决定标题路线，而不是事后拼故事。

## 一、研究背景与动机

空中机械臂（UAV-mounted manipulator）在无人机执行巡检、搜救、精细操作等任务时面临独特挑战：无人机与机械臂存在强耦合动力学，无人机本体的姿态扰动会直接传导至机械臂末端精度，同时室外无动捕条件下的精确定位与快速响应控制仍是开放问题。

现有方案多将无人机控制与机械臂控制解耦独立设计，或依赖昂贵的动捕系统进行真机定位，导致系统部署成本高、适应性差。本方向旨在 Isaac Sim 高保真仿真环境中，通过强化学习训练空中机械臂快速响应策略，实现：
1. 无人机与机械臂解耦控制（抗扰动漂移）
2. 室外无动捕条件下的精确操作
3. 低成本从仿真到真机的策略迁移

## 二、相关工作梳理

### 2.1 仿真训练平台
| 方法 | 核心贡献 | 局限 | 与本方向关系 |
|------|---------|------|------------|
| **Isaac Lab** (2511.04831) | GPU原生并行物理+渲染，模块化支持RL/IL/遥操作，Isaac Gym升级版 | 非专门针对空中载体 | **核心基础设施** |
| **Isaac Sim** | 高保真单场景物理，适合场景级仿真 | 并行效率低 | 提供底层物理支持 |
| **TIAGo + Isaac** (2403.07091) | sim-to-real gap系统性分析（关节误差/碰撞约束/控制架构） | 移动机械臂，非空中 | 指导sim-to-real验收协议 |
| **WheelArm-Sim** (2601.21129) | Isaac Sim导航+操作联合数据平台，ROS2遥操作采集 | 非空中平台 | 提供联合任务数据管线参考 |
| **MobileManiBench** (2602.05233) | Isaac Sim+RL移动操作多模态数据+评测基准 | 移动平台，非飞行 | 验证Isaac+RL路线可行性 |
| **WHOLE-MoMa** (2604.12509) | WBC状态机先验采集 + 离线RL，两阶段推进 whole-body mobile manipulation | 非空中平台，依赖先验控制器 | 提供“控制先验/离线数据→RL精修”的强对照路线 |
| **A Comparison of Reinforcement Learning and Optimal Control for Aerial Manipulators** (2604.12628) | 将 DDPG 与 pseudo-spectral optimal control 放在同一空中机械臂任务里直接比较，显式暴露 reward design 与 terminal-constraint 这两套控制哲学的分工边界 | 更偏特定问题设定，未覆盖大规模并行与多任务泛化 | 直接提醒 D07 必须保留“RL vs optimal control vs hybrid”基线轴 |
| **Meta-Adaptive Beam Search Planning for Transformer-Based Reinforcement Learning Control of UAVs with Overhead Manipulators under Flight Disturbances** (2603.26612) | 以 Transformer-DDQN + adaptive beam search 规划 manipulator torque，在预定义飞行底座轨迹下补偿 UAV 扰动，强调“先固定飞行，再学操作臂”这条中间路线 | 飞行底座不参与学习，泛化到真正 whole-body 控制仍有限 | 给 D07 增加一条 **manipulator-only / fixed-flight** 强基线，帮助分离“飞行难点”和“操作难点” |
| **AGILE** (2603.20147) | 训练前配置校验、确定性场景测试、统一评测与部署工作流 | 更偏流程层，不直接给新策略 | 提供 D07 的 deterministic case-suite 与部署前 gate 设计锚点 |

### 2.2 训练器层（RL 算法对比）
| 训练器 | 代表工作 | 核心特点 | 适合场景 |
|--------|---------|---------|---------|
| **PPO** | Isaac Lab默认 | 稳定、样本高效、on-policy | 基线训练 |
| **SAC** | 连续控制常用 | 最大熵、最大回报 | 探索型任务 |
| **FlashSAC** (2604.04539) | 高维动作空间off-policy | 快速收敛 | 空中机械臂高频控制 |
| **ARM** (2604.03037) | Advantage Reward Modeling | 解决稀疏奖励+长时序问题 | 接触丰富任务 |
| **DICE-RL** (2603.10263) | 预训练生成式+residual off-policy RL | 保留预训练先验，适合高维像素输入 | 视觉型策略后训练 |
| **Pseudo-spectral Optimal Control** (2604.12628) | 解析/优化式控制，显式终端约束与运行代价 | 依赖任务建模质量，复杂接触与高维观测不易扩展 | 作为 D07 的强解析基线与 hybrid 组件来源 |
| **MPC+RL Synthesis Survey** (2502.02133) | 系统归纳 hybrid MPC+RL 的接口范式，包括 teacher-student、MPC safety shield、policy warm-start、optimizer-on-top-of-policy | 非空中机械臂专用，缺少 aerial 平台实证 | 用来细化 D07 的 P3 混合路线，不让“hybrid”停留在模糊口号 |

### 2.2+ 🆕 R769 新增：Sim-to-Real 关键文献
| 方法 | arXiv ID | 核心贡献 | 与D07关系 |
|------|---------|---------|----------|
| **Sim-to-Real for Mobile Robots** | 2501.02902 | Isaac Sim→Gazebo→Real ROS2 完整链路，Mobile robot RL迁移验证 | 提供从Isaac Sim到真机ROS2迁移的实测协议参考 |
| **Dexterous Sim-to-Real (人手)** | 2502.20396 | 视觉型接触丰富操作零样本迁移，divide-and-conquer distillation | **核心参考**：接触丰富任务的sim-to-real recipe，可迁移到机械臂末端精细操作 |
| **Beyond Imitation** | 2602.12628 | SFT warm-start + sim RL + real-data anchoring，OpenVLA+24% | VLA+RL联合训练参考，说明warm-start对视觉型操作的重要性 |
| **Direction Matters** | 2602.14174 | 学习力方向而非大小，零样本跨刚度泛化 | 力控方向作为额外奖励信号，可减少sim-to-real gap中的物理差异敏感度 |
| **Tac2Real** | 2603.28475 | 轻量触觉仿真+多GPU并行RL+TacAlign对齐 | 触觉sim-to-real链路，对机械臂精细操作尤其相关 |
| **Real-to-Sim-to-Real** | 2603.17016 | <5min遥操作→kNN surrogate→residual copilot RL，HITL refinement | 提供real-to-sim tuning的自动化协议，与PRISM互补 |

### 2.3 奖励层设计
| 方法 | 核心贡献 | 适合任务 |
|------|---------|---------|
| **Dense Reward** | 阶段奖励（接近→对准→接触→完成） | 基础训练 |
| **ARM** | 相对优势奖励建模，recovery-aware evaluation | 长时序操作 |
| **Robo-Dopamine** (2512.23703) | step-aware GRM + multi-view fusion + policy-invariant shaping，1条expert轨迹+150次在线rollout达95% | 高精度接触任务 |

### 2.4 Sim-to-Real 迁移
| 方法 | 核心贡献 | 与本方向关系 |
|------|---------|------------|
| **Dexterous Sim-to-Real** (2502.20396) | 视觉型接触丰富操作零样本sim-to-real | 证明视觉+接触路线可行 |
| **Beyond Imitation** (2602.12628) | SFT warm-start + sim RL + real-data anchoring，OpenVLA+24% | VLA+RL联合训练参考 |
| **Direction Matters** (2602.14174) | 学习力方向而非大小，零样本跨刚度泛化 | 触觉/力控接口参考 |
| **Tac2Real** (2603.28475) | 轻量触觉仿真+多GPU并行RL+TacAlign对齐 | 触觉sim-to-real链路 |
| **Real-to-Sim-to-Real** (2603.17016) | <5min遥操作→kNN surrogate→residual copilot RL | HITL refinement协议 |

### 2.5 部署前风险发现
| 方法 | 核心贡献 | 与本方向关系 |
|------|---------|------------|
| **ROBOGATE** (2603.22126) | 两阶段边界聚焦采样(20K粗扫→10K边界细化)，Panda/UR5e失效区发现 | **部署前必做验收层** |
| **PRISM** (2603.05574) | IL warm-start + RL refinement + human指令纠偏 | post-pretraining adaptation协议 |

### 2.6 现有工作的共同缺陷 / Gap
1. **训练平台空白**：多数工作使用PyBullet/MuJoCo，缺乏Isaac Lab原生GPU并行+高保真物理的空中机械臂方案
2. **耦合动力学处理不足**：现有方法要么忽略无人机姿态扰动，要么简化机械臂为固定基座
3. **无动捕室外部署能力未验证**：大多数sim-to-real工作依赖室内动捕系统
4. **部署前风险验收缺失**：训练完直接上真机，缺少系统性的失败边界发现流程
5. **语义关系状态缺位**：多数 Isaac Lab manipulation policy 只吃像素+本体状态，缺少可直接服务长时序操作的 3D 关系图状态
6. **whole-body 快速抓取协议不足**：现有 D07 更偏末端控制与 sim-to-real，对“底座/载体+机械臂+夹爪”联合高速协调、冲击稳定与触觉在线修正覆盖还不够
7. **缺少 RL 与最优控制的统一对照轴**：如果只比较 PPO/SAC/FlashSAC，容易把“学习器内部谁更强”误当成“学习方法本身优于解析/优化控制”；2604.12628 提醒 D07 必须回答哪些段该交给 RL，哪些约束段更适合最优控制或 hybrid 架构

### 2.7 🆕 R777 新增：语义关系状态 + 多任务RL
| 方法 | arXiv ID | 核心贡献 | 与D07关系 |
|------|---------|---------|----------|
| **KG-M3PO** | 2603.24083 | 在线3D scene graph + 动态关系边 + 多模态共享latent，多任务 manipulation RL | 说明 D07 可把末端-目标-障碍物关系显式编码进状态，而不只靠图像隐式学习 |
| **FastGrasp** | 2604.12879 | 两阶段RL: 先基于点云生成 grasp candidates，再做 mobile base+arm+hand 的 whole-body 协同控制，并用触觉做实时抓取修正 | 直接提醒 D07 不应只做“机械臂末端控制”，还要把 whole-body coordination + 触觉在线修正 单列成对照轴 |

## 三、我们的创新方向

### 3.1 核心创新点（Contribution）
1. **C1: Isaac Lab 原生空中机械臂 RL 训练协议**
   - 基于 Isaac Lab 统一 Isaac Sim 高保真物理 + GPU 并行多环境训练
   - Action space: 7-DoF（推力+力矩+夹爪），Observation: 机器人状态+目标+相对关系
   - 验证 IsaacLab-Gripper-Drone-Pickplace (uiseoklee/GitHub) 现有实现并做 ablution

2. **C2: 耦合动力学解耦控制策略**
   - 核心假设：无人机姿态扰动可被解耦为独立的"抗扰动补偿子策略"
   - 方法：双层控制架构（高层任务规划 + 低层快速响应 RL 策略），并保留 **optimal-control / inner-loop controller** 作为可替换内环
   - 🆕 **R771 实机验证支撑**：DSAM (2512.21085) 用 PPO policy + INDI/PID 内环已在真实双旋翼空中机械臂上验证——PPO policy 作为外环高层规划，INDI(Incremental Nonlinear Control) + PID 作为低层内环执行，实现 0.18ms 推理延迟、cm 级末端精度、16% payload 扰动稳定飞行。直接验证了 D07 C2 双层架构的可行性和实时性要求。
   - 🆕 **R793 补强**：2604.12628 说明同一空中机械臂问题下，reward-shaped RL 与 pseudo-spectral optimal control 各自擅长的约束段并不相同，因此 D07 不应预设“纯 RL 一定吞掉解析控制”，而应把 hybrid 设计视为正式方法位
   - 🆕 **R800 补强**：2502.02133 进一步提醒，所谓 hybrid 至少要区分四种接口形态，分别是 **teacher-student（MPC 生成专家/示教）**、**safety shield（MPC 做在线约束兜底）**、**policy warm-start（RL 给优化器初值）**、**optimizer-on-top-of-policy（策略提案，优化器修正）**。因此 D07 的 C2 不能只写“RL+内环控制器”，而要把接口类型本身当成实验变量
   - 训练协议：引入随机无人机姿态扰动（roll/pitch ±15°，yaw ±30°）+ 质量/摩擦 domain randomization（参照 DSAM Sec. IV-B ablation 设计）

3. **C3: 多层次奖励设计与长时序过程监督**
   - Level 1: 密集阶段奖励（phase score: approach→align→contact→complete）
   - Level 2: Robo-Dopamine 式 step-aware 通用奖励模型（GRM）+ 1-shot 适配
   - Level 3: ARM 式 Advantage Reward Modeling，recovery-aware evaluation
   - 三层联合训练 vs. 分层训练 ablation
   - 🆕 **R765 新增**: RoTO (2510.21609) 提供 Isaac Lab 触觉 RL 基准——Find/Bounce/Baoding 三任务——可作为 D07 接触丰富操作的过程奖励设计参考轴
   - 🆕 **R769 新增**: 2502.20396 的 divide-and-conquer distillation 机制——将长时序接触任务拆分为「接近→对准→接触→精细操作」子阶段，逐步 distill 到不同子策略，再联合微调。与 C3 的三层奖励设计高度互补，可作为「分层奖励 + 分层策略蒸馏」协同验证方案。

4. **C4: SIM-to-REAL 全链路验收协议**
   - 🆕 **R769 新增** (2501.02902): Isaac Sim→Gazebo→Real ROS2 完整链路提供了可复现的迁移协议基准，验证了从 Isaac Lab 到真机 ROS2 的零样本可行性。D07 可参照该协议设计自己的 sim-to-real 验收流程。
   - 🆕 **R769 新增** (2602.14174): Direction Matters 揭示「学习力方向而非大小」可实现跨刚度零样本泛化——D07 可将其作为 C3 奖励层的辅助奖励信号，在机械臂末端接触力上增加「力方向对齐」项，进一步减少 sim-to-real 物理差异敏感度。
   - 🆕 **R769 新增** (2602.12628): SFT warm-start → sim RL → real-data anchoring 三阶段路线（OpenVLA+24%）——说明在 sim RL 之前用 SFT 做行为克隆预热可显著提升 sample efficiency 和最终性能，D07 应在 PPO/SAC 训练前加入 SFT warm-start 阶段。
   - 训练后: ROBOGATE 式两阶段边界发现（20K LHS + 10K 边界细化）
   - 部署前: PRISM 式 IL warm-start + RL + HITL refinement
   - OOD 压测: 目标变化 / 摩擦变化 / 动力学偏移 / 无人机扰动幅度
   - 🆕 **R765 新增**: 2505.16547 (Zero-Shot Sim2Real RL for Occlusion-Aware Plant Manipulation) 证明 Isaac Lab 零样本 sim-to-real 在遮挡/植物/光照变化下可泛化——D07 应将其"遮挡感知"轴纳入 OOD 压测设计

### 3.2 拟定方法框架
```
[无人机状态估计]
       ↓
[高层任务规划器] ← 语言指令 / 目标图像
       ↓
[低层 RL 策略（Isaac Lab PPO/SAC/FlashSAC）]
  - 观测：无人机姿态 + 机械臂关节 + 末端-目标相对关系
  - 动作：机械臂关节控制 + 夹爪
  - 奖励：三层奖励（dense + GRM + ARM）
       ↓
[Sim: Isaac Sim 高保真物理]
  ↓ domain randomization（姿态扰动/摩擦/质量）
[Real: 零样本迁移 or PRISM HITL微调]
       ↓
[ROBOGATE 部署前风险评估]
```

### 3.3 与现有方法的关键差异
| 维度 | 现有方法（TIAGo/Isaac等） | 我们的方法 |
|------|------------------------|----------|
| 训练平台 | PyBullet / Mujoco / Isaac Gym | Isaac Lab + Isaac Sim（原生GPU并行） |
| UAV-ARM耦合 | 解耦独立控制 | 统一RL策略 + 姿态扰动作为domain randomization |
| 控制范式 | 默认只比学习式策略 | 明确对比 RL / optimal control / hybrid inner-loop |
| 奖励设计 | hand-crafted dense reward | 三层奖励（dense + GRM + ARM） |
| sim-to-real | 单一策略直接迁移 | ROBOGATE风险发现 + PRISM HITL微调 |
| 室外无动捕 | 依赖动捕定位 | 端到端学习，视觉/状态输入 |
| 部署前验收 | 直接上真机 | 两阶段边界发现 + OOD压测 |

### 3.3 首轮结果后的实验预算排序规则（R884 新增）
1. **先看 risk coverage / SARR，再看单点成功率**：只要 `L4` 边界覆盖或 `SARR` 仍不过线，任何 `whole-body` 或 `hybrid` 的局部优势都不得直接升格为主叙事。
2. **warm-start 只提速不提质时，自动降级为 data-gated acceleration**：若收益主要体现在达线步数，而 `L1/L2` 与 `SARR` 没有同步改善，则示教数据只保留为训练入口优化，不再继续抢 D07 的方法主线预算。
3. **fixed-flight 仍显著压制 whole-body 时，先补局部补偿与风险 gate**：这说明当前瓶颈主要还在底座耦合扰动与部署边界，不该提前把资源铺到 whole-body 大矩阵。
4. **只有在 fixed-flight 不再占优、且 hybrid 至少在 `L0/L4/SARR` 一轴稳定领先时，才允许升级为 deployable hybrid control**。
5. **若 hybrid 只在仿真平均成功率占优，但 `L4` 风险覆盖或 `NormCost` 明显恶化，则默认收成 research-only hybrid**：此时可写成研究原型，但不许抢“可部署控制”主标题。
6. **若 risk coverage 已过线而 warm-start + fixed-flight 组合在 `L1/L3` 最稳，则默认主叙事收成 deployable local compensation pipeline**：把 D07 诚实收束为“局部快速补偿 + 低成本迁移”路线，而不是勉强抬 whole-body。
7. **若 `Squint` 式 fast visual RL 只稳定改善首小时或首几万步样本效率，但 `L2/L4/SARR` 无同步增益，则统一降级为 sample-efficiency booster**：只能写成训练配方优化，不得改写 D07 的控制主叙事。
8. **若 `ViserDex` 式 3DGS 感知前端在 `L3` 零样本迁移上显著降低 sim-to-real gap，却没有同步改善 `L0/L2`，则默认收成 perception-bridge evidence**：主张聚焦“视觉桥接”而不是混成控制创新。
9. **若 `RoTri-Diff` 式显式三体几何约束只在高速接近/接触段显著降低碰撞与掉物，而 fixed-flight 仍压制 whole-body，则优先把 D07 收成 relation-aware local compensation**：说明当前几何关系建模值钱，但 whole-body 协同还不该抢标题。

这套排序的作用，是让 D07 的实验资源分配优先服从 **风险覆盖 → 层级站稳 → 训练提速**，而不是被单轮 success rate 带偏。

### 3.4 新增本地锚点后的主张映射（R886 新增）

> 本轮先做本地回扫，新增确认 **Squint / ViserDex / RoTri-Diff** 三类证据的正确落位，目的不是扩论文地图，而是防止后续把“训练提速”“视觉桥接”“几何约束”三种不同价值混写成一个控制创新故事。

| 本地锚点 | 最稳妥的吸收位置 | 能支持什么 | 不能越级支持什么 |
|---|---|---|---|
| **Squint** (2602.21203) | 训练协议层 / warm-start 邻近对照 | `分钟级视觉RL`、高样本效率、低算力快速达线 | 不能单独证明 whole-body 或 deployable hybrid control |
| **ViserDex** (2604.11138) | `L3 sim-to-real` 感知桥接层 | 3DGS 预渲染随机化、单目视觉桥接、降低真实视觉分布差异 | 不能单独证明底座抗扰、控制器优越或 risk coverage 成立 |
| **RoTri-Diff** (2603.07165) | `L1/L2` 几何关系建模层 | 显式 robot-object triadic pose 约束、降低碰撞/抓持失稳 | 不能绕过 fixed-flight vs whole-body 判线，直接宣称统一协同成立 |

**当前判断**：D07 如果首轮出现“Squint 提速 + ViserDex 降 gap + RoTri-Diff 降碰撞”这种多点正信号，默认也只能先收成 **relation-aware local compensation + perception bridge + sample-efficiency recipe** 的组合证据；除非 `L0/L4/SARR` 同步站住，否则不允许把它们打包写成 `deployable whole-body control`。


### 3.5 锚点信号出现后的正文/标题收束规则（R888 新增）

> 目的：把 `warm-start 提速 / 3DGS 感知桥接降 gap / triadic pose 降碰撞` 这三类局部正信号，从“各自落在哪层”继续推进到 **摘要第一句默认怎么写、哪些词绝对不能抢主标题**，避免首轮结果一出来又把多个 supporting evidence 拼成“统一 whole-body 可部署控制”。

1. **若只看到 warm-start / Squint 式提速**：摘要第一句默认写成 **sample-efficiency improvement for Isaac RL training**，正文聚焦“更快达线 / 更低算力 / 更少 rollout”；不得写成控制架构升级。
2. **若只看到 ViserDex/3DGS 式降 sim-to-real gap**：摘要第一句默认写成 **perception bridge for sim-to-real transfer**，正文聚焦“视觉分布差异缩小 / 零样本迁移更稳”；不得替代 `L0` 稳定性或 `L4` 风险覆盖结论。
3. **若只看到 RoTri-Diff/triadic pose 式降碰撞或稳抓持**：摘要第一句默认写成 **relation-aware local compensation under coupled disturbance**，正文聚焦“局部几何关系显式建模值钱”；若 `fixed-flight` 仍压制 whole-body，不得写成统一 whole-body 控制成立。
4. **若三类信号同时出现，但 `L0/L4/SARR` 未同步站住**：摘要与标题默认只能收成 **relation-aware local compensation + perception bridge + sample-efficiency recipe**；三者都归入 supporting evidence 组合，不允许抢 `deployable whole-body control` 或 `deployable hybrid control` 标题位。
5. **只有当局部信号之外，`L0` 稳定、`L4` 风险覆盖与 `SARR` 至少一轴同步占优时**，才允许把摘要第一句升级成 **deployable hybrid control** 或 **deployable whole-body control**。

这条规则的作用，是把 D07 的论文口径固定成 **局部亮点先降级、层级站稳再升级、部署口径最后放行**，避免实验一有几个好看数字就把主叙事吹胖。

## 四、实验设计

### 4.1 数据集与仿真环境
- **Isaac Lab** + **Isaac Sim**（GPU并行，128环境同步）
- **IsaacLab-Gripper-Drone-Pickplace** (GitHub uiseoklee) 作为基线环境
- 扩展：加入随机无人机姿态扰动（roll/pitch ±15°，yaw ±30°）

### 4.2 基线对比
| 基线 | 说明 |
|------|------|
| SAC (Isaac Lab默认) | 连续控制常用基线 |
| PPO (Isaac Lab默认) | on-policy稳定基线 |
| FlashSAC | 高维动作空间off-policy |
| ARM | reward modeling基线 |
| DICE-RL | 预训练+residual RL基线 |
| Pseudo-spectral Optimal Control | 强解析/优化基线，检验 reward-shaped RL 是否真的带来额外收益 |
| Hybrid outer-RL + inner-controller | 外环学习策略 + 内环优化/控制器，检验混合路线是否更适合强约束段 |
| WBC + 离线RL (WHOLE-MoMa路线) | 传统控制+RL两阶段 |

### 4.3 评价指标
- **主指标**: 任务成功率（pick-place / door-open / drawer-open）
- **鲁棒性**: 无人机扰动幅度增加时的成功率衰减曲线
- **样本效率**: 达到80%成功率所需环境步数
- **Sim-to-Real Gap**: 仿真成功率 vs. 真机成功率（用PRISM微调后）
- **部署风险**: ROBOGATE发现的失败边界参数空间覆盖率

### 4.3+ 五层统一验收矩阵（R784 新增）

> 目的：把 D07 从“论文堆叠”推进到真正能筛路线的实验协议，避免把训练器效果、whole-body 协同、sim-to-real 差距和部署风险混成一个总成功率。

| 验收层 | 代表路线 | 核心问题 | 主指标 | 典型失败解释 |
|---|---|---|---|---|
| **L0 基础飞行/底座稳定** | DSAM, PPO+INDI/PID | 载体本体在扰动下是否先稳得住 | 姿态误差、末端漂移、恢复时间 | 机械臂没问题，但底座先失稳 |
| **L1 末端到目标局部操作** | PPO/SAC/FlashSAC 基线 | reach-align-contact 的局部闭环是否成立 | phase score、接触成功率、抓取率 | 训练器能学动作，但接触段不稳 |
| **L2 whole-body 协同** | FastGrasp, WHOLE-MoMa | 底座/载体+机械臂+夹爪是否需要联合协调 | 高速接近成功率、冲击后稳定时间、掉物率 | 单独末端策略够不到真实高速场景 |
| **L3 sim-to-real / 适配效率** | Beyond Imitation, PRISM, Real-to-Sim-to-Real | 迁移要不要大量真机修补，代价多高 | 零样本成功率、warm-start收益、HITL轮次 | 仿真分高，但真机要大量修补 |
| **L4 部署前风险覆盖** | ROBOGATE | 上线前是否已经摸到危险边界 | 边界覆盖率、漏检风险区、误报率 | 平均分高，但危险角落根本没测到 |

**使用规则**：
1. 新方法先过 L0/L1，再谈 L2 whole-body，不把基础稳定性问题误判成策略创新问题。
2. 若 L1 提升但 L2 无提升，说明方法更像“末端局部修补”，不能宣称 whole-body 路线成立。
3. 若仿真里 L2 很强但 L3 很差，应优先回头补 warm-start / 真实锚点 / HITL，而不是继续堆训练步数。
4. D07 后续所有 baseline 默认按这五层表汇报，禁止只报单个 success rate。

### 4.3++ 稳定性-适配-风险统一主指标（R810 新增）

D07 后续不能只用 `平均成功率` 排方法，因为这会系统性高估两类路线：
1. **仿真里很强，但真机修补代价极高** 的策略；
2. **局部任务分数很高，但风险边界和 whole-body 协同明显缺口** 的策略。

因此新增一个统一主分数 **SARR（Stability-Adaptation-Risk Rating）**：

\[
\text{SARR} = 0.20 \cdot L0 + 0.25 \cdot L1 + 0.20 \cdot L2 + 0.20 \cdot L3 + 0.15 \cdot L4 - \lambda \cdot \text{NormCost}
\]

其中：
- `L0` = 基础稳定分（姿态恢复、末端稳态误差归一化后求均值）
- `L1` = 局部操作分（approach / align / contact / complete phase score）
- `L2` = whole-body 协同分（冲击后稳定时间、掉物率、联合控制收益）
- `L3` = 迁移适配分（零样本成功率 + warm-start / HITL 单位修补收益）
- `L4` = 风险覆盖分（ROBOGATE 边界覆盖率、漏检风险区惩罚）
- `NormCost` = 归一化后的 `GPU小时 + 真实锚点条数 + HITL轮次 + 推理时延`
- 默认先取 `λ = 0.12`

**使用规则**：
1. 主结果表必须同时给出 `平均成功率` 与 `SARR`，不允许只报其一。
2. 若某路线 `成功率高但 SARR 低`，默认它更像高成本特调方案，不作为 D07 主线。
3. 若 `P0 fixed-flight` 在 L1 高、但 L2/L3 明显低，说明它更适合作为局部操作基线，而不是 whole-body 方案。
4. 若 `hybrid P3` 的平均成功率未必最高，但 SARR 最高，说明它更适合论文主叙事，因为 D07 真正目标是“可部署控制”，而不是单次最优分数。

### 4.3+++ deterministic case-suite 与阶段 gate（R790 新增）

> 参考 AGILE 的工作流层思想，把“训练能收敛”与“部署前真的可放行”拆开。

| Case 组 | 主要覆盖 | 最小场景设置 | 必过指标 | 失败后优先回查 |
|---|---|---|---|---|
| **S1 基础稳定组** | hover + 末端微调 | 静止目标，无接触，3档姿态扰动 | 姿态恢复时间、末端稳态误差 | L0 内环 / 观测延迟 |
| **S2 接近接触组** | approach → align → contact | 固定目标，2档摩擦，2档质量偏置 | 接触成功率、首次接触冲击峰值 | L1 奖励 / action scaling |
| **S3 whole-body 组** | 高速接近 + 抓取/推靠 | 初始速度、目标偏航、夹爪误差 | 掉物率、冲击后稳定时间 | L2 协同策略 / 候选抓取生成 |
| **S4 sim-to-real 组** | 仿真到真机最小迁移 | 选 1 个最稳任务做零样本+少量修补 | 零样本成功率、50次内修补增益 | L3 warm-start / real-anchor |
| **S5 风险边界组** | 部署前 corner case 扫描 | 摩擦、质量、风扰、初始位姿联合采样 | 漏检风险区比例、边界覆盖率 | L4 风险发现 / 训练分布覆盖 |

**阶段 gate**：
- **Gate-G0**：S1 通过前，不进入任何接触任务。
- **Gate-G1**：S2 通过后，才允许比较训练器优劣。
- **Gate-G2**：S3 通过后，才允许宣称 whole-body 路线成立。
- **Gate-G3**：S4 至少证明“零样本可跑”或“<50 次修补显著提升”，否则不进入真机扩展。
- **Gate-G4**：S5 未过时，禁止说“可部署”，哪怕平均成功率很高。

### 4.3++++ 专家轨迹接入与确定性回放准入协议（R819 新增）

> 来自本地回扫 **Isaac Lab** 与 **AGILE** 的共同提醒。D07 现在已经把 `E1 warm-start vs scratch` 立起来了，但如果不先把 **专家轨迹质量** 和 **确定性回放能力** 单独验收，后面很容易把“warm-start 无收益”误判成算法问题，实际上只是数据入口或 replay 协议脏掉了。

| 准入层 | 要回答的问题 | 主指标 | 没过时优先回查 |
|---|---|---|---|
| **T0 字段一致性** | BC 数据与 PPO 训练时的 obs/action 空间是否完全一致 | schema mismatch rate、归一化偏差 | 数据导出脚本、action scaling |
| **T1 回放可复现性** | 专家轨迹能否在环境里稳定 replay，不因 reset/随机性漂移失真 | replay success rate、deterministic drift | 环境 reset、随机种子、物理步长 |
| **T2 phase 标签可信度** | `approach / align / contact / complete` 是否与轨迹真实阶段一致 | phase consistency、phase transition error | phase 标注逻辑、奖励接口 |
| **T3 reset 痕迹完整性** | 失败轨迹是否保留结构化 reset reason，能支撑后续 warm-start 失败归因 | reset trace completeness | 日志接口、回放记录 |

**当前判断**：D07 的 warm-start 价值不应只按“是否提分”来判断，而要先通过 `T0-T3`。只有这样，后续才能分清是 **BC 数据入口有问题**，还是 **warm-start 本身不值得保留**。

### 4.3+++++ 首轮读数判定表（R825 新增）

> D07 现在已经把 `E1 warm-start vs scratch`、`P0 fixed-flight / manipulator-only`、`P3 hybrid inner-loop` 都挂上了，但如果没有首轮读数判定表，后续 12h 级实验很容易只产出“看起来都差不多”的模糊结论。这里先把 **第一轮结果 → 下一步动作** 固定下来。

| 首轮读数模式 | 典型表现 | 当前解释 | 下一步动作 |
|---|---|---|---|
| **R1 warm-start 明显更快** | BC-50/200 在 `60% / 80% success` 达线步数上稳定优于 scratch，且 `RVS/PCS/RTC` 全过 | 说明数据入口有效，D07 应保留 `SFT/BC warm-start → RL` 作为默认入口 | 进入 `E2 whole-body vs fixed-flight`，判断 warm-start 是否也能迁移到耦合控制 |
| **R2 scratch 与 warm-start 接近** | 三组差异小于 10~15%，但训练曲线都稳 | 说明当前任务更受奖励/观测而非初始化影响 | 暂缓继续堆示教，优先补 `关系状态 / 奖励层 / reset`，warm-start 降级为可选 |
| **R3 fixed-flight 显著更稳** | `P0 manipulator-only` 在 phase score、恢复时间、掉物率上明显优于 whole-body | 说明当前瓶颈仍主要在飞行底座与耦合扰动，而不是机械臂局部策略 | D07 主线先收缩到 `局部操作补偿`，whole-body 只保留为远期目标 |

### 4.3++++++ E1→E3 最小验证顺序（R838 新增）

> 目的：D07 现在已有 `warm-start vs scratch`、`fixed-flight vs whole-body`、`RL vs optimal control vs hybrid` 三条主对照，但首轮算力与时间不够同时摊开。先把 **最小验证顺序** 固定，避免一上来把归因混掉。

| 顺序 | 本轮只回答的问题 | 最小设置 | 过线标准 | 没过时优先结论 |
|---|---|---|---|---|
| **E1 数据入口与 warm-start** | BC / SFT 入口到底有没有真实价值 | 单任务、固定目标、PPO、3 seeds、`BC-50 / BC-200 / scratch` | `RVS/PCS/RTC` 过线，且 warm-start 至少一档在达线步数或首小时成功率上稳定优于 scratch | 先查 expert data / replay / phase 标签，不急着否定 warm-start |
| **E2 fixed-flight vs whole-body** | 当前瓶颈主要在飞行底座还是末端局部控制 | 固定飞行轨迹 + manipulator-only 对照 whole-body | fixed-flight 若显著更稳，则说明 whole-body 还不该升主线 | 主叙事先收缩到局部操作补偿，不继续扩大动作空间 |
| **E3 hybrid vs pure RL / optimal control** | 强约束段是否值得交给 inner-loop / optimizer | 选 E2 里最稳任务，只比较 `pure RL / pseudo-spectral / hybrid` | 若 hybrid 的 `SARR` 明显更高，即使平均成功率不是第一，也允许升主线 | D07 主叙事转向可部署混合控制，而非纯学习路线 |

**执行规则**：
1. 默认 **E1 先于 E2，E2 先于 E3**，除非已有证据证明前一层完全稳定。
2. 任一阶段没过，不用急着扩环境或堆训练器，先回到上游归因表。
3. 只有当前一阶段读数稳定，下一阶段结论才允许写进主表，不然只记到 appendix/supporting evidence。

### 4.3+++++++ 烟测失败优先归因表（R838 新增）

> 目的：12h 正式实验前，先用 30min~1h 烟测把最常见的假失败筛掉，别把环境/数据问题误判成算法问题。

| 烟测现象 | 第一优先怀疑 | 第二优先怀疑 | 立即动作 |
|---|---|---|---|
| reward 有波动但 success 始终贴地 | phase 奖励断裂 / goal 判定错 | 动作缩放不合理 | 先查 reward hook 与 success 判定，不急着换训练器 |
| BC 初始化后表现比 scratch 还差 | expert data schema / replay drift | 归一化或 action clipping | 回查 `T0/T1`，冻结 warm-start 扩展 |
| fixed-flight 稳、whole-body 完全不稳 | 底座扰动建模 / 观测缺关键姿态量 | action space 过大 | 先缩回 manipulator-only 主线 |
| pure RL 能学、hybrid 学不动 | inner-loop 接口不连续 / shield 太强 | reward 与控制器目标冲突 | 先把 hybrid 降成 safety shield 或 warm-start，不急着判死 |
| 三个 seed 差异极大 | reset / 初始化分布漂移 | 训练步长与并行环境不匹配 | 先修环境稳定性，不解释方法优劣 |

### 4.3++++++++ warm-start 保留/降级规则（R838 新增）

> 目的：D07 现在很容易因为“warm-start 听起来合理”就长期保留它，但如果首轮收益不稳定，它会吞掉大量数据清洗与回放成本。这里把保留条件写死。

| 首轮读数 | 结论 | 后续动作 |
|---|---|---|
| warm-start 在 3 seeds 下稳定降低达线步数，且不恶化 `L4` 风险覆盖 | **保留为默认入口** | 后续 E2/E3 默认继续带 warm-start 对照 |
| warm-start 只在单个 seed 或单一奖励设定下有效 | **降级为候选** | 不再作为默认入口，只在 appendix 保留 |
| warm-start 提升首小时曲线，但最终成功率/风险覆盖变差 | **仅保留为训练加速技巧** | 不写成主贡献，不进入论文主叙事 |
| warm-start 触发明显 replay/data 维护负担，收益又不稳定 | **冻结** | 后续主线改走 scratch / controller prior / hybrid |

**主张**：D07 后续不该把 warm-start 当信仰。只有它同时带来 **更快达线 + 不恶化风险覆盖 + 维护成本可控**，才配留在主线里。
### 4.3+++++++++ 首轮结果→资源冻结规则（R839 新增）

> 目的：D07 现在已经有 `主叙事收束表`，但还缺一张更硬的 **资源冻结规则**。首轮实验最怕的不是结果差，而是三条线都“有一点点希望”，然后继续平均烧算力。这里把第一轮结果直接映射到 **冻结 / 保留 / 升格** 动作。

| 首轮结果模式 | 优先结论 | 资源动作 | 允许进入主表的内容 |
|---|---|---|---|
| `E1` 都不稳，`RVS/PCS/RTC` 未过线 | 数据入口与环境稳定性未站住 | **冻结 warm-start 讨论**，先只修数据/日志/环境 | 仅保留训练与验收协议，不讲方法优劣 |
| warm-start 只带来早期提速，最终 `SARR/L4` 无增益 | warm-start 更像训练加速技巧 | **降级为 appendix / engineering trick** | 可写“训练效率优化”，不可写主贡献 |
| `fixed-flight` 明显优于 whole-body | 当前瓶颈主要在底座耦合与状态建模 | **冻结 whole-body 扩张**，主线回缩到 local compensation | 允许主讲 `局部补偿/固定飞行下快速操作` |
| whole-body 有增益，但 hybrid 无明显收益 | 学习策略本身仍是主力 | **冻结 hybrid 扩张**，先保留 pure RL 主线 | 允许主讲 whole-body RL，但内环只算工程兜底 |
| hybrid 在 `L0 / L4 / SARR` 任一稳定占优，且维护成本可控 | 强约束段确实值得交给 inner-loop / optimizer | **升格 hybrid 为主线**，压缩 pure RL 为对照 | 允许主讲可部署混合控制 |
| sim-to-real 零样本弱，但 `<50` 次修补收益稳定且 HITL 成本低 | 适配协议具备论文价值 | **保留 sim-to-real 适配线**，但不扩 whole-body 新任务 | 允许主讲低成本适配协议 |
| L4 风险覆盖始终差，即使平均成功率高 | 方法尚不可部署 | **冻结所有“可部署”表述**，只保留仿真主张 | 禁止写 deployable / real-ready |

- 2026-04-20 R843: 本轮按轮换主推进 **D07**，继续严格执行“先本地、后外部”。已复核 `D07/README.md`、`REPORT.md`、`experiments.md` 与近 30 天本地 L1 锚点 **Isaac Lab / TIAGo+Isaac / RL-Based Sim-Real Co-Training**，并补跑 QMD `qmd query "Isaac Sim manipulation reinforcement learning robot arm" --no-rerank`；结果仍主要回流现有 D07 文档和既有本地笔记，说明本地方向覆盖已足够，本轮无需 Tavily。随后仅做最小 arXiv 补扫，看到 **VLAJS / 2604.13733**（VLA 引导 PPO 早期探索，主价值是 sample efficiency 提升）、**A Mechanistic Analysis of Sim-and-Real Co-Training / 2604.13645**（解释 structured representation alignment 与 importance reweighting 的机制）、以及 **FastGrasp / 2604.12879**（whole-body+触觉的地面移动操作强对照）；三者都与 D07 有关，但当前更适合作为训练协议/机制解释/远期 whole-body 对照轴，尚不足以触发完整入库。Phase 2 的核心推进不是再扩论文表，而是在 `REPORT.md` 新增 **supporting evidence 降级补充表**，正式规定：VLA guidance 与 co-training 机制类证据只能支持 `data-gated acceleration` 或 `low-cost adaptation`，不能越级写成 `控制创新/可部署 whole-body`。核心价值是把 D07 从“知道哪些结果只能降级”继续推进到“知道哪些**新论文类型**也只能降级”，防止后续被 sample efficiency 或表征对齐结果重新带偏主叙事。

### 4.3+++++++++++ supporting evidence 降级协议（R842 新增）

> 目的：D07 现在最怕的不是没有结果，而是**每条线都有一点正信号**，最后 warm-start / fixed-flight / whole-body / hybrid / sim-to-real 一起写进标题、摘要和主表。这里正式规定：哪些结果只能算 supporting evidence，不能抢主叙事。

| 结果形态 | 允许定位 | 禁止定位 | 备注 |
|---|---|---|---|
| warm-start 只稳定带来更快收敛、但最终 `SARR/L4` 无增益 | `training recipe / data-gated acceleration` | 核心方法贡献 | 只能写进训练协议或 appendix，不进标题 |
| fixed-flight / manipulator-only 明显优于 whole-body | `local compensation baseline` 或阶段性主线 | `统一 whole-body 协同成立` | 说明当前主要瓶颈仍在底座耦合 |
| hybrid 只在单个 seed 或单一任务更稳 | `strong engineering baseline` | `deployable hybrid control` | 必须过稳定性+风险双门槛才可升格 |
| sim-to-real 只能靠大量 HITL 修补才成立 | `adaptation evidence` | `zero-shot / low-cost deployment` | 修补成本必须进主表 |
| 某路线平均成功率高，但 `L4` 风险覆盖差 | `simulation-only result` | `real-ready / 可部署` | 一律冻结部署口径 |

**硬规则**：
1. 摘要、主表、第五节写作计划里，**同一轮只保留 1 条主叙事**。
2. 其余有效结果统一降级为 `supporting evidence / appendix / training recipe / engineering baseline` 四类之一。
3. 只要 `L4` 没过，任何“可部署”“可上线”“real-ready”表述自动作废。

### 4.3++++++++++++ 首轮统一汇报模板（R842 新增）

> 目的：把首轮结果直接约束成 4 句，防止汇报时重新摊大饼。

1. **本轮主线**：`训练协议 / data-gated acceleration / local compensation / whole-body / hybrid / low-cost adaptation` 六选一。
2. **站住的证据**：只写与主线直接相关的 `L0-L4 / SARR` 结果。
3. **自动降级项**：明确哪条线只算 `supporting evidence`。
4. **唯一下一步**：只能保留 1 个动作，不并开。

### 4.3+++++++++++++ D07 主叙事冻结准则（R842 新增）

- 若 **warm-start 只带来提速**：主叙事只能写 `data-gated acceleration`，不得写控制创新。
- 若 **fixed-flight 长期压制 whole-body**：主叙事只能写 `local compensation`，whole-body 降为远期扩展。
- 若 **hybrid 同时过 SARR / L4 / 维护复杂度 三门槛**：才允许升为 `deployable hybrid control` 主线。
- 若 **sim-to-real 依赖 <50 次修补且收益稳定**：才允许写 `low-cost adaptation`；否则只能写“仿真内成立，迁移仍待验证”。

### 4.4++++ E2/E3 的默认放行顺序（R832 新增）

> 目的：D07 现在已经有 `资源冻结规则` 和 `hybrid 升格门槛`，但还缺一张更直接面向论文写作的 **主叙事冻结协议**。首轮结果一出来，最容易犯的错不是判断不出方向，而是把 `warm-start / fixed-flight / whole-body / hybrid / sim-to-real` 五条线都写成贡献，最后每条都不够硬。这里把“论文到底讲哪句话”正式冻结。

| 首轮主读数 | 允许冻结成的论文主叙事 | 必须降级为 supporting evidence 的内容 | 标题/摘要可用说法 |
|---|---|---|---|
| warm-start 只带来显著达线提速，但最终 `SARR/L4` 无明显提升 | **低成本训练加速协议** | 不得把 warm-start 写成核心方法创新；whole-body / hybrid 仅保留对照 | `sample-efficient warm-start for aerial manipulation RL` |
| `fixed-flight / manipulator-only` 稳定优于 whole-body | **局部快速补偿优先于全身协同** | 不得主讲 whole-body；hybrid 只算部署补件 | `fast local compensation under fixed-flight disturbances` |
| whole-body 在 `L2` 稳定增益，但 `L3/L4` 仍弱 | **whole-body 协同在仿真内成立** | 禁止写 `deployable`、`real-ready`；sim-to-real 只作未来工作/小节说明 | `whole-body coordination for aerial manipulation in Isaac Lab` |
| hybrid 在 `L0/L4/SARR` 中至少一项稳定占优，且维护成本受控 | **可部署混合控制主线** | pure RL 降级为对照；warm-start 只保留为入口技巧 | `deployable hybrid aerial manipulator control with learned outer-loop and safe inner-loop` |
| 零样本弱，但 `<50` 次修补显著抬升 `L3` 且 HITL 成本低 | **低成本适配协议** | 不得夸大为零样本 sim-to-real；whole-body 若未过线不得抢标题 | `low-cost post-sim adaptation for aerial manipulator control` |
| `L4` 风险覆盖长期不过线 | **仅能讲仿真验证 / 风险发现协议** | 一切 `deployable / robust in the wild / real-world ready` 说法全部冻结 | `risk-aware evaluation protocol for aerial manipulator RL` |

**冻结规则**：
1. **每轮首轮结果只允许保留 1 条主叙事**，其余全部自动降级为对照、补件或 appendix。
2. 如果 `fixed-flight` 仍显著占优，D07 默认主叙事必须回缩到 `局部操作补偿`，不得抢跑 `whole-body`。
3. 如果 `hybrid` 没同时过 **稳定性门槛 + 风险门槛**，默认不允许写成主贡献，只能算工程兜底。
4. 如果 `L4` 没过线，再高的平均成功率也不能使用 `可部署` 语义。

### 4.3++++++++++++++ supporting evidence 降级补充表（R843 新增）

> 目的：把本轮新补到的 **VLA 引导 warm-start** 与 **co-training 机制分析** 正式放进 D07 的叙事约束里，避免后面一看到 sample efficiency 提升，就又把训练配方误写成控制贡献。

| 新证据类型 | 可以支持什么 | 不能直接支持什么 | 写作位置建议 |
|---|---|---|---|
| **VLA guidance / action regularization 让 PPO 更快收敛** | `data-gated acceleration`、训练入口更稳、稀疏奖励下更容易过 G1 | `whole-body 协同成立`、`hybrid 可部署控制`、`sim-to-real 已解决` | 第三节训练协议小节 / 第四节 warm-start 对照 / appendix |
| **sim-and-real co-training 改善表示对齐** | `low-cost adaptation` 或 `warm-start/real-anchor` 的机制解释 | `零样本真实部署成立`、`控制架构创新` | 第二节相关工作机制分析 / 第三节 real-anchor 设计 |
| **FastGrasp 这类 whole-body+触觉结果在地面移动操作上成立** | D07 的 `L2 whole-body` 与 `触觉在线修正` 值得保留为远期强对照轴 | 当前空中机械臂已经具备同等级 whole-body 证据 | 第二节 related work / 第四节 E2-E3 远期扩展 |

**硬规则补充**：
1. 只要证据主要体现在 **sample efficiency / 表示对齐 / warm-start 稳定性**，默认归入 `training recipe` 或 `data-gated acceleration`，不升格为控制创新。
2. 只要证据主体不是 **空中机械臂 + L4 风险不过度恶化**，默认不得写成 `deployable`。
3. `whole-body` 相关外部证据若不在空中载体上成立，只能作为 D07 的 **对照轴合法性来源**，不能当成 D07 已站住的结果。

### 4.3++++++++++++++++ 首轮结果→标题级收束映射（R878 新增）

> 目的：前面已经冻结了主叙事、摘要句式和降级协议，但还缺最后一层——**论文标题默认该落在哪一条线上**。如果这层不写死，后面很容易出现正文已经收束，标题却还把 `warm-start / whole-body / hybrid / sim-to-real` 一起挂上的问题。

| 首轮结果模式 | 标题默认收束 | 可以保留的副标题信息 | 禁止再挂进标题的内容 |
|---|---|---|---|
| warm-start 只改善达线速度，`L1/L2/SARR` 无显著增益 | **data-gated acceleration for aerial manipulator RL** | Isaac Lab 训练协议、BC/SFT 入口、样本效率提升 | whole-body、deployable、hybrid control |
| `fixed-flight / manipulator-only` 稳定压制 whole-body | **local compensation under coupled aerial disturbances** | 固定飞行设定、局部操作补偿、耦合瓶颈分析 | whole-body coordination、统一耦合控制 |
| whole-body 仅在 `L2` 仿真层稳定占优，`L3/L4` 仍弱 | **whole-body coordination in simulation for aerial manipulation** | Isaac Lab 平台、仿真内冲击恢复、协同收益 | deployable、real-ready、low-cost sim-to-real |
| hybrid 在 `L0/L4/SARR` 至少一轴稳定占优且维护成本可控 | **deployable hybrid aerial manipulator control** | outer-loop / inner-loop 分工、风险覆盖、稳定性收益 | zero-shot real-world ready、统一 whole-body intelligence |
| `<50` 次修补显著抬升 `L3` 且 HITL 成本低 | **low-cost post-sim adaptation for aerial manipulator control** | PRISM/HITL、real-anchor、少样本修补 | zero-shot sim-to-real solved、whole-body 已成立 |
| `L4` 风险覆盖始终差，即使平均成功率高 | **risk-aware evaluation protocol for aerial manipulator RL** | 风险发现协议、边界覆盖、部署前验收 | deployable、robust in the wild、field-ready |

**硬规则**：
1. 标题默认只允许落在上表 **1 条主线**，其余结果一律降级为副标题、章节名或 appendix。
2. 只要 `fixed-flight` 仍显著更稳，标题中就**不得出现** `whole-body`。
3. 只要 `L4` 没过，标题中就**不得出现** `deployable / real-ready / field-ready`。
4. 只要 warm-start 的收益主要停在前期曲线，标题中它就只能是 **acceleration / training recipe**，不能冒充控制创新。

### 4.3+++++++++++++++++ D07 次方向扫描留痕（R878 新增）

- **本地轻量扫描**：本轮按轮换主推进 **D07**。先复核 `D07/README.md`、`REPORT.md`、`experiments.md`，并回扫本地锚点 **Isaac Lab / TIAGo+Isaac / RL-Based Sim-Real Co-Training / UAV_Bimanual_VLA_Review**。同时补跑 QMD `qmd query "Isaac Lab manipulation reinforcement learning aerial manipulator warm-start fixed-flight hybrid" --no-rerank`，结果仍主要回流 D07 现有方向文档、既有 round 记录与 Isaac Lab 框架综述，没有形成足以触发完整入库的新高价值论文。
- **外部补充扫描**：按纠偏后的流程继续补做 arXiv Export API 外查，高位结果为 **Fisher Decorator (2604.17919)**、**Can Explicit Physical Feasibility Benefit VLA Learning? (2604.17896)**、**SpaceDex (2604.17888)**。三者分别更偏 flow-based offline RL、VLA 显式可行性监督与受限空间灵巧抓取，对 D07 当前 `warm-start / fixed-flight / whole-body / hybrid inner-loop` 主线只有间接参考价值，尚不足以改写控制范式或触发完整入库，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。
- **Phase 2 核心推进**：本轮不再扩论文名录，而是把 D07 从“摘要该怎么写”继续推进到 **标题级收束映射**：现在首轮结果一出来，就必须在 `data-gated acceleration / local compensation / whole-body in simulation / deployable hybrid / low-cost adaptation / risk-aware evaluation` 六条标题桶里 **六选一**，禁止再把 `warm-start / whole-body / hybrid / sim-to-real` 同时挂进标题。核心价值是让 D07 的论文产出从摘要、主表到标题完全共用同一套收束口径。

### 4.3+++++++++++ sim-to-real 升格条件（R839 新增）

> 目的：D07 不能因为“终于能在真机上跑起来”就过早把 sim-to-real 写成主叙事。真正值得升格的是 **低成本、可复用、能稳定复现的适配协议**。

| 条件 | 说明 | 未满足时处理 |
|---|---|---|
| **Z1 零样本可跑** | 至少能稳定完成最小任务，不出现持续失稳或不可恢复发散 | 只写成“真机可运行”，不写 sim-to-real 成立 |
| **Z2 小样本修补有效** | `<50` 次真实修补或少量 HITL 就能带来稳定增益 | 否则说明仿真锚点不够，先回补训练/观测 |
| **Z3 风险不放大** | 修补后 `L4` 不得变差，不能靠冒险换成功率 | 否则不升格，只保留为案例 |
| **Z4 可复用性** | 迁移协议可在第二个近似任务上复现，不是单任务手搓 | 否则只算 case study |
| **Z5 维护成本可接受** | 真机调参与标注成本不应高到抵消仿真训练价值 | 否则不写“低成本适配” |

**主张**：只有 `Z1+Z2+Z3` 至少同时成立，D07 才允许把 sim-to-real 放进主表；若再满足 `Z4/Z5`，才配升成论文主叙事。

**硬规则**：
1. 一轮实验只允许有 **1 条主叙事**，其余收益都降级为 supporting evidence。
2. 若 `C0/C1` 成立，就不允许把 `whole-body` 或 `sim-to-real` 写成主标题方向。
3. 若 `C2` 成立但 `C4` 不成立，论文应明确讲 **deployable hybrid control**，而不是硬讲 unified whole-body intelligence。
4. 若 `C3` 成立但 `C2/C4` 都不成立，主叙事只能是 **data-gated acceleration**，不能夸成控制架构突破。
5. 只有 `C4` 成立时，D07 才有资格把 `whole-body coordination` 升为论文主贡献。

### 4.3+++++++++ 贡献改写规则（R835 新增）

> 目的：避免首轮结果出来后，贡献点还沿用旧版本口号，导致标题、摘要、实验主表各说各话。

| 若主叙事是 | C1 应改写为 | C2 应改写为 | C3/C4 应保留什么 |
|---|---|---|---|
| **C0 验收协议** | Isaac Lab 原生训练与验收协议 | 部署前 gate 与风险覆盖优先 | 奖励/whole-body 只作次要变量 |
| **C1 局部操作补偿** | 固定底座/弱扰动下的高效 RL 训练协议 | 局部补偿器抗扰动设计 | whole-body 仅作失败对照 |
| **C2 hybrid 可部署控制** | Isaac Lab 训练协议 | RL 与 inner-loop/controller 的混合接口 | warm-start 与奖励层作增益来源 |
| **C3 data-gated acceleration** | 专家轨迹准入 + warm-start 训练协议 | 控制范式保持中性 | 强调数据入口和样本效率，而非控制哲学 |
| **C4 whole-body 协同** | whole-body 任务建模与训练协议 | 协同控制/冲击恢复设计 | warm-start / hybrid 作 enabling factor |
| **C5 sim-to-real 适配** | 仿真训练协议 + 真实锚点接入 | 少样本修补/人类纠偏协议 | whole-body/训练器只保留最稳一条 |

**使用规则**：
1. 先定主叙事，再回改 Contribution，不允许先写死 Contribution 再硬找结果贴合。
2. 一旦主叙事切到 `C1/C2/C3/C5`，`whole-body` 自动降为配角；只有 `C4` 才允许 whole-body 升格。
3. 这样 D07 的 REPORT 就能从“研究方向很多”真正收束成“论文只讲一件最站得住的事”。

### 4.3++++++++++ 数据入口升级门槛（R835 新增）

> 目的：把 `warm-start 看起来有用` 和 `值得长期维护专家轨迹治理链` 区分开。

| 观察结果 | 默认判断 | 对数据入口的动作 |
|---|---|---|
| 仅 `60% success` 提前，但 `80% success` 无明显优势 | warm-start 只改善早期探索 | 保留最小 BC 入口，不扩数据治理链 |
| `60% / 80% success` 都稳定提前，且 `HHB/调参负担` 下降 | 数据入口具有主线价值 | 升级专家轨迹准入、phase 标注与 replay 基础设施 |
| warm-start 提升只出现在单任务、换任务即消失 | 数据收益高度任务依赖 | 只保留任务特定入口，不写成通用贡献 |
| warm-start 收益明显，但 whole-body / hybrid 仍不稳 | 数据入口是 enabling factor，不是主叙事 | 保留为支持项，优先继续收束控制范式 |

**一句话原则**：
只有当 warm-start 的收益能跨 `任务 / seed / 控制范式` 稳定保留时，D07 才值得把“数据入口治理”升级成论文主贡献；否则它只是加速器，不是故事中心。

### 4.3++++++ 首轮协议后继动作：结果解释优先级（R832 新增）

D07 现在已经有了 `R1-R6` 的首轮读数判定表，但执行时还差一个常见误区防护：
**当首轮结果同时触发多种现象时，很容易先盯住“最像方法创新”的读数，而忽略更基础的基础设施/风险问题。**

因此补一条更硬的 **结果解释优先级**，用于保证后续不会在 `warm-start 看起来有效` 时，跳过 `风险覆盖缺口` 或 `基础环境不稳` 这两类更致命问题。

| 优先级 | 触发模式 | 默认解释 | 默认动作 |
|---|---|---|---|
| **P0** | `R6 三条线都不稳` | 问题还在环境/动作缩放/奖励日志层，任何方法比较都不可信 | 收缩回最小场景，暂停 whole-body / sim-to-real / hybrid 扩展 |
| **P1** | `R5 风险覆盖明显缺口` | 当前路线更像 demo 方案，不具备部署资格 | 先补 `ROBOGATE + OOD case-suite`，不扩任务复杂度 |
| **P2** | `R3 fixed-flight 显著更稳` | 主要瓶颈仍在飞行底座耦合，而不是 manipulator 局部策略 | 先把 D07 收缩到 `局部操作补偿` 主线，whole-body 降级 |
| **P3** | `R4 hybrid 优于 pure RL` | 强约束段默认应保留 inner-loop controller / optimization | 扩 `teacher-student / shield / warm-start / optimizer-on-top` 四种接口 |
| **P4** | `R1 warm-start 明显更快` | 数据入口有效，BC/SFT 值得保留为默认入口 | 进入 E2/E3，看 warm-start 能否迁移到更复杂控制范式 |
| **P5** | `R2 scratch 与 warm-start 接近` | 当前任务更受奖励/观测制约，而非初始化方式 | 优先补观测/奖励/reset，不再继续堆示教 |

**硬规则**：
1. 若同时命中多类，必须按 `P0 → P1 → P2 → P3 → P4 → P5` 解释，不允许跳级。
2. 只要 `P0/P1` 成立，任何“方法优于方法”的结论都只能写成暂定观察，不能写成主叙事。
3. 只有 `P0/P1/P2` 都不成立时，`warm-start` 与 `hybrid` 的方法差异才有资格进入论文主结论。
4. 这样 D07 后续每轮都能先排基础问题与部署风险，再决定该不该继续把 GPU 小时押给方法本身。

### 4.3+++++++ 首轮后资源收缩表（R832 新增）

为了把 `结果解释优先级` 真正落到资源调度，D07 再补一张 **首轮后资源收缩表**。它只回答一件事：
**第一轮 12h 结果出来后，哪些线继续拿预算，哪些线必须冻结。**

| 首轮结论 | 继续拿预算的线 | 必须冻结的线 | 默认下一轮动作 |
|---|---|---|---|
| `P0 基础环境不稳` | 环境 / 日志 / reward / action scaling | whole-body / hybrid / sim-to-real | 只修最小训练闭环 |
| `P1 风险覆盖缺口大` | OOD case-suite / ROBOGATE / deterministic tests | 更复杂任务扩展 | 先把部署前验收站稳 |
| `P2 fixed-flight 更稳` | manipulator-only / local compensation | whole-body 叙事扩张 | 先明确局部操作上限 |
| `P3 hybrid 更优` | inner-loop / shield / warm-start / optimizer-on-top | 纯 RL 扩参扩算力 | 把混合接口做细，不再盲加训练步数 |
| `P4 warm-start 更优` | BC/SFT 入口、专家轨迹治理 | 盲目新增训练器 | 先把 warm-start 稳定迁到 E2/E3 |
| `P5 warm-start 无显著收益` | 关系状态 / 奖励层 / reset 归因 | 继续堆更多示教轨迹 | 转回观测与奖励优化 |

**冻结原则**：
1. 没拿到主预算的方向，只保留最小对照，不继续加复杂度。
2. `sim-to-real` 默认最后拿预算，除非 `G0/G1` 已稳定通过。
3. `whole-body` 只有在 `P2` 不成立时才继续扩，不允许一边 fixed-flight 明显更稳、一边还继续扩 whole-body 叙事。
4. 这样 D07 后续就不会再出现“每条线都再试一点”的摊大饼推进。

### 4.3+++++++++++ supporting evidence 降级协议（R842 新增）

> 目的：D07 现在最怕的不是没有结果，而是**每条线都有一点正信号**，最后 warm-start / fixed-flight / whole-body / hybrid / sim-to-real 一起写进标题、摘要和主表。这里正式规定：哪些结果只能算 supporting evidence，不能抢主叙事。

| 结果形态 | 允许定位 | 禁止定位 | 备注 |
|---|---|---|---|
| warm-start 只稳定带来更快收敛、但最终 `SARR/L4` 无增益 | `training recipe / data-gated acceleration` | 核心方法贡献 | 只能写进训练协议或 appendix，不进标题 |
| fixed-flight / manipulator-only 明显优于 whole-body | `local compensation baseline` 或阶段性主线 | `统一 whole-body 协同成立` | 说明当前主要瓶颈仍在底座耦合 |
| hybrid 只在单个 seed 或单一任务更稳 | `strong engineering baseline` | `deployable hybrid control` | 必须过稳定性+风险双门槛才可升格 |
| sim-to-real 只能靠大量 HITL 修补才成立 | `adaptation evidence` | `zero-shot / low-cost deployment` | 修补成本必须进主表 |
| 某路线平均成功率高，但 `L4` 风险覆盖差 | `simulation-only result` | `real-ready / 可部署` | 一律冻结部署口径 |

**硬规则**：
1. 摘要、主表、第五节写作计划里，**同一轮只保留 1 条主叙事**。
2. 其余有效结果统一降级为 `supporting evidence / appendix / training recipe / engineering baseline` 四类之一。
3. 只要 `L4` 没过，任何“可部署”“可上线”“real-ready”表述自动作废。

### 4.3++++++++++++ 首轮汇报模板（R842 新增）

> 目的：把首轮结果直接约束成 4 句，防止汇报时重新摊大饼。

1. **本轮主线**：`训练协议 / data-gated acceleration / local compensation / whole-body / hybrid / low-cost adaptation` 六选一。
2. **站住的证据**：只写与主线直接相关的 `L0-L4 / SARR` 结果。
3. **自动降级项**：明确哪条线只算 `supporting evidence`。
4. **唯一下一步**：只能保留 1 个动作，不并开。

### 4.3+++++++++++++ D07 主叙事冻结准则（R842 新增）

- 若 **warm-start 只带来提速**：主叙事只能写 `data-gated acceleration`，不得写控制创新。
- 若 **fixed-flight 长期压制 whole-body**：主叙事只能写 `local compensation`，whole-body 降为远期扩展。
- 若 **hybrid 同时过 SARR / L4 / 维护复杂度 三门槛**：才允许升为 `deployable hybrid control` 主线。
- 若 **sim-to-real 依赖 <50 次修补且收益稳定**：才允许写 `low-cost adaptation`；否则只能写“仿真内成立，迁移仍待验证”。

### 4.3++++++++++++++ 主叙事禁词表与标题冻结规则（R847 新增）

> 目的：把 D07 从“知道哪些结果该降级”继续推进到“知道摘要、标题、主表里哪些词绝对不能乱用”。以后首轮结果一出来，先套这张表，再决定论文怎么讲。

| 当前首轮读数 | 允许使用的主叙事词 | 禁止使用的词 | 默认标题方向 |
|---|---|---|---|
| warm-start 仅显著提速，最终 `L4/SARR` 无额外收益 | `data-gated acceleration` / `efficient warm-start` | `novel control architecture` / `deployable policy` | *Efficient Warm-Start for Isaac-Lab Aerial Manipulation* |
| fixed-flight / manipulator-only 稳定压住 whole-body | `local compensation` / `manipulator-first control` | `whole-body coordination` / `unified aerial manipulation` | *Local Compensation for Disturbance-Robust Aerial Manipulation* |
| whole-body 仅在仿真里有增益，但 L3/L4 站不住 | `whole-body in simulation` / `in-sim coordination evidence` | `real-ready whole-body control` / `deployable whole-body` | *Whole-Body Coordination Evidence in Isaac Simulation* |
| hybrid 只有在 `L0/L4/SARR` 至少一轴稳定占优且维护复杂度可控 | `deployable hybrid control` / `safety-aware hybrid interface` | `end-to-end pure RL superiority` | *Safety-Aware Hybrid Control for Aerial Manipulation* |
| sim-to-real 主要靠 `<50` 次修补/HITL 拉起来 | `low-cost adaptation` / `minimal real-anchor tuning` | `zero-shot sim-to-real` / `real-ready out of the box` | *Low-Cost Adaptation for Aerial Manipulation Policies* |
| 风险覆盖未过、但均值成功率漂亮 | `promising in simulation` / `requires further risk coverage` | `deployment-ready` / `field-ready` / `ready for real-world use` | *Promising In-Sim Control with Unresolved Deployment Risks* |

**冻结规则：**
1. **标题只允许保留 1 条主叙事**：`training acceleration / local compensation / whole-body / hybrid / low-cost adaptation` 五选一。
2. `warm-start`、`co-training`、`VLA guidance` 这类结果，除非它们直接带来 `L0/L4/SARR` 实质提升，否则一律不得抢 `control` 相关词。
3. 只要 `fixed-flight` 仍显著优于 whole-body，标题、摘要、主表中一律禁用 `unified whole-body`。
4. 只要 `L4` 风险覆盖未过，标题、摘要、结论一律禁用 `deployable / real-ready / field-ready`。
5. 若多个方向都“有一点点赢”，默认收缩到更保守那条主叙事，不允许并列双标题。

### 4.3+++++++++++++++

> 目的：把首轮结果直接约束成 4 句，防止汇报时重新摊大饼。

1. **本轮主线**：`训练协议 / data-gated acceleration / local compensation / whole-body / hybrid / low-cost adaptation` 六选一。
2. **站住的证据**：只写与主线直接相关的 `L0-L4 / SARR` 结果。
3. **自动降级项**：明确哪条线只算 `supporting evidence`。
4. **唯一下一步**：只能保留 1 个动作，不并开。

### 4.3+++++++++++++ D07 主叙事冻结准则（R842 新增）

- 若 **warm-start 只带来提速**：主叙事只能写 `data-gated acceleration`，不得写控制创新。
- 若 **fixed-flight 长期压制 whole-body**：主叙事只能写 `local compensation`，whole-body 降为远期扩展。
- 若 **hybrid 同时过 SARR / L4 / 维护复杂度 三门槛**：才允许升为 `deployable hybrid control` 主线。
- 若 **sim-to-real 依赖 <50 次修补且收益稳定**：才允许写 `low-cost adaptation`；否则只能写“仿真内成立，迁移仍待验证”。

### 4.4++++ E2/E3 的默认放行顺序（R832 新增）

在 E1 之后，D07 现在最容易分散的地方，是同时想做 `whole-body`、`hybrid`、`sim-to-real`。为避免首轮结果还没收束就扩线，补一个默认放行顺序：

1. **先 E2：fixed-flight / local compensation vs whole-body**
   - 先判断当前难点主要在飞行底座，还是在 manipulator 本体。
2. **再 E3：pure RL vs hybrid / control prior**
   - 只有当 E2 证明 whole-body 值得保留时，才继续回答 hybrid 是否应升为主线。
3. **最后 E4：最小 sim-to-real**
   - 只挑 E2/E3 中最稳的一条进真机，不让真机调试吞掉主线判断。

**默认规则**：
- 若 E2 里 `fixed-flight` 已明显优于 `whole-body`，则 E3 不再优先比较 whole-body hybrid，而是先比较 `local compensation + inner-loop`。
- 若 E2 里 `whole-body` 的优势不显著，D07 当前论文主叙事应自动收缩为“局部操作补偿 + 可部署控制协议”，而不是继续强调统一 whole-body 控制。
- 这样 D07 的每一轮推进都会更像“快速排除错误主线”，而不是把所有方向同时保留。

### 4.4++++ R840 新增：首轮后主叙事冻结协议

> 目的：R839 已经把 `资源冻结规则 / hybrid 升格门槛 / sim-to-real 升格条件` 写出来了，这一轮继续把它压成 **一句话就能决定下一周主线** 的冻结协议。避免 D07 每次首轮结果一出来，又把 `warm-start / whole-body / hybrid / sim-to-real` 同时保留成“都值得继续看看”。

| 首轮最稳定信号 | 默认主叙事 | 必须降级的内容 | 下一轮唯一允许主动作 |
|---|---|---|---|
| `E1` 先站住，warm-start 主要带来更快达线，但 `L2/L4` 没明显新收益 | **data-gated acceleration** | 不许夸成控制架构突破；whole-body / hybrid 只算 supporting evidence | 只继续验证 warm-start 能否跨任务/控制范式稳定复现 |
| `fixed-flight / manipulator-only` 明显更稳 | **local compensation under fixed-flight** | 不许继续把 whole-body 写成默认主标题；sim-to-real 只保留最小验证 | 只补关系状态、局部奖励与接触稳定性 |
| whole-body 比 local compensation 明显更强，但 `hybrid` 还没站住 | **whole-body RL coordination** | inner-loop / optimal-control 只算工程兜底，不抢主叙事 | 只继续压 whole-body 的状态接口与冲击恢复 |
| hybrid 在 `L0/L4/SARR` 稳定占优 | **deployable hybrid control** | pure RL 降级为对照；warm-start 只保留为 enabling factor | 只细化 hybrid 接口（shield / warm-start / optimizer-on-top） |
| `<50` 次修补就让真机表现稳定提升，且 `L4` 不恶化 | **low-cost sim-to-real adaptation** | 不许再扩 whole-body 新任务；训练器比较退居配角 | 只验证第二个近似任务上的可复用性 |
| `L4` 一直站不住，即使平均成功率好看 | **仿真内成立的训练/控制协议** | 全部 deployable / real-ready / 可上线 说法冻结 | 只补风险覆盖与 corner-case 扫描 |

**硬规则**：
1. 一轮首轮结果出来后，**只能保留 1 条主叙事**；其余全部自动降级成 appendix / supporting evidence。
2. 若 `L4` 没过，就算 `L0-L3` 很漂亮，也不允许使用 `deployable / 可部署 / real-ready` 这类词。
3. 若 `fixed-flight` 明显更稳，`whole-body` 自动退出标题竞争；除非后续专门证明 local compensation 上限已到。
4. 若 `hybrid` 占优但解释不清“赢在什么约束段”，也不得升主线，只能先当 engineering evidence。

### 4.4+++++ R840 新增：首轮后默认汇报模板

> 目的：让 D07 后续每次 heartbeat 或正式实验汇报时，都优先说“现在最站得住的故事是什么”，而不是把所有观察并排堆出来。

**默认四句模板**：
1. **哪一层站住了**：`L0/L1/L2/L3/L4` 中本轮真正过线的是哪几层。
2. **当前主叙事**：`data-gated acceleration / local compensation / whole-body RL / deployable hybrid / low-cost adaptation / 仿真内成立协议` 六选一。
3. **必须降级的内容**：哪些现象只能算 supporting evidence，不能写进摘要标题。
4. **下轮唯一动作**：只保留 1 个主推进动作，不并开 whole-body / hybrid / sim-to-real 三条线。

**语言约束**：
- 只有 `L4` 过线，才允许说 **可部署 / real-ready**。
- 只有 `whole-body` 明显优于 `fixed-flight`，才允许说 **whole-body coordination**。
- 只有 `hybrid` 过了稳定性 + 风险门槛，才允许说 **deployable hybrid control**。
- 其余一律用：**训练加速 / 局部补偿 / 支持性证据 / 仿真内成立**。 

### 4.4++++++ R840 新增：首轮后默认对外汇报骨架

> 目的：把研究内核和给主人的汇报口径彻底对齐，防止内部已经冻结主叙事，外部汇报还把所有候选线并排念一遍。

| 若当前冻结主叙事是 | 对外第一句应怎么说 | 明确不能怎么说 |
|---|---|---|
| **data-gated acceleration** | 本轮确认 warm-start/数据入口主要带来训练提速，先不宣称控制架构突破 | 不能说 whole-body 或 hybrid 已成立 |
| **local compensation** | 本轮更支持固定飞行/局部补偿路线，当前瓶颈仍在底座耦合而非统一 whole-body | 不能说统一协同控制已跑通 |
| **whole-body RL** | 本轮 whole-body 在高速接近/冲击恢复上已出现清晰增益 | 不能说可部署，除非 L4 也过线 |
| **deployable hybrid** | 本轮 hybrid 在稳定性/风险至少一轴稳定占优，说明强约束段值得保留内环/优化器 | 不能把 warm-start 说成主贡献 |
| **low-cost adaptation** | 本轮真机侧更支持低成本修补/适配协议，而不是扩大训练器比较 | 不能再并讲 whole-body 新任务 |
| **仿真内成立协议** | 本轮只确认了仿真内训练/验收协议站住，部署相关表述继续冻结 | 不能说 real-ready / 可上线 |

**硬规则**：
1. 发给主人或写 round log 时，先按上表选 1 条口径，不并列讲 2 条主线。
2. 若 `L4` 没过，就算 `L0-L3` 很漂亮，也只能说“仿真内成立”或“支持某条训练/控制路线”。
3. 若 `fixed-flight` 明显更稳，对外汇报里 `whole-body` 只能放在“尚未站住”的降级项里。 

### 4.4+++++++ R872 新增：首轮后标题/摘要默认收束模板

> 目的：R840/R841 已经把 D07 的主叙事冻结到只能保留 1 条，但还缺最后一层更直接的写作模板：**首轮结果一出来，摘要第一句和标题到底默认写哪种句式。** 这一节专门防止内部虽然知道该收束，外部汇报和后续论文草稿却还在 `warm-start / whole-body / hybrid` 三线并写。

| 首轮主要读数 | 默认标题/摘要句式 | 可否做主标题 | 说明 |
|---|---|---|---|
| `warm-start` 只明显改善达线速度、样本效率，`L1/L2/SARR` 不显著抬升 | **data-gated acceleration for Isaac aerial manipulation RL** | 否 | 只能当训练协议贡献，不能宣称控制方法突破 |
| `fixed-flight / manipulator-only` 持续压制 whole-body，且 `L0/L2` 缺口明显 | **local compensation under coupled-disturbance bottleneck** | 是 | 主叙事改讲局部快速补偿，不再让 whole-body 抢标题 |
| `hybrid outer-RL + inner-controller` 在 `L0/L4/SARR` 至少一轴稳定占优，且成本不过度恶化 | **deployable hybrid control for aerial manipulators** | 是 | 只有这类读数才允许把“可部署”写进摘要主句 |
| whole-body 只在分布内成功率略优，但 `L3/L4` 明显吃亏 | **whole-body gains remain deployment-limited** | 否 | 只能写成限制项或讨论项 |
| 风险覆盖不足、边界漏检明显 | **performance gains remain non-deployable due to uncovered risk boundaries** | 否 | 无论平均成功率多高，都不得写 deployable / real-ready |

**执行规则**：
1. 先看 `L0/L4/SARR`，再看平均成功率；D07 默认是部署导向排序。
2. `warm-start` 若只带来提速，必须降级为 recipe / enabling factor，不抢标题。
3. `fixed-flight` 若明显更稳，默认就把主摘要收束到 **local compensation**。
4. 只有 hybrid 同时过稳定性、风险覆盖与成本门槛，才允许升成 **deployable hybrid control**。


> 目的：R840 已经把 D07 的主叙事冻结到只能留 1 条，但还差一个更实用的写作闸门：**哪些结果即使显著，也只能做 supporting evidence，不能抢标题/摘要/主表。** 这一步专门防止 `warm-start / fixed-flight / hybrid / sim-to-real adaptation` 四条线同时争主贡献。

| 结果模式 | 允许保留的位置 | 明确不能怎么写 | 默认降级结论 |
|---|---|---|---|
| `warm-start` 只带来更快收敛，但终局 `SARR / L4` 没明显提升 | recipe、小表、附录曲线 | 不能写成“核心控制方法突破” | **低成本训练加速器** |
| `fixed-flight / manipulator-only` 显著优于 whole-body | 主表基线、误差分析主段 | 不能反过来宣称 whole-body 已成立 | **局部快速补偿更现实** |
| `hybrid` 平均成功率更高，但 `L4 风险覆盖` 或维护复杂度更差 | appendix、secondary result、风险讨论 | 不能写成“可部署混合控制已成立” | **高性能候选路线，暂未部署级成立** |
| `sim-to-real` 只在大量 HITL / 真实锚点后成立 | 适配章节、case study | 不能写成“低成本/零样本迁移成立” | **依赖真实修补的迁移路线** |
| `whole-body` 只在单任务/单姿态窗成立 | 受控子实验 | 不能写成“通用 whole-body 协同策略” | **受限任务窗内成立** |

**硬规则**：
1. 标题、摘要、主表只允许服务 **1 条主叙事**，其余结果默认降级为 supporting evidence。
2. 若某路线不能同时解释 `SARR`、`L4 风险覆盖`、维护复杂度三项，就不能抢主贡献。
3. 凡是只证明“更快训练 / 更容易调参 / 在受控设定里更强”的结果，默认写成 recipe 或 engineering evidence，而不是论文核心 claim。
4. D07 后续每轮首轮结果汇报，必须先判断“能不能升主线”，再决定写进主表还是 appendix。

### 4.4++++++++ R841 新增：首轮汇报模板

> 目的：让 D07 后续每次实验汇报都先说清“现在唯一能讲的故事是什么”，而不是把所有正结果并排堆出来。

**固定顺序**：
1. **主叙事候选是谁**：`data-gated acceleration / local compensation / whole-body RL / deployable hybrid / low-cost adaptation / 仿真内成立协议`
2. **哪条线被降级**：明确写出哪些结果只能算 supporting evidence
3. **还缺哪类证据**：是缺 `L4`、缺 `SARR`，还是缺维护复杂度优势
4. **下一轮唯一动作**：只保留 1 个主修方向，不并开 whole-body / hybrid / sim-to-real 三线

**推荐句式**：
- 若 `warm-start` 仅提速：`本轮主结论不是控制更强，而是 warm-start 可作为低成本训练加速器；控制主线尚未改写。`
- 若 `fixed-flight` 压制 whole-body：`本轮 whole-body 不升主线，主叙事收束为局部快速补偿；whole-body 仅保留为 appendix 对照。`
- 若 `hybrid` 提分但风险覆盖不足：`hybrid 目前只能算高性能候选路线，尚不足以宣称可部署主线，优先补 L4 风险覆盖。`

| 实验 | 变量 | 预期结论 |

|------|------|---------|
| Exp-A1 | 训练器对比（PPO/SAC/FlashSAC/ARM/DICE） | 最优训练器 |
| Exp-A2 | 奖励层对比（dense / GRM / ARM / 三层联合） | 奖励层设计重要性 |
| **Exp-A3** | RL vs optimal control vs hybrid inner-loop | 判断哪些约束段该交给学习器，哪些更适合解析/优化控制 |
| **Exp-A4** | Teacher-student vs safety shield vs policy warm-start vs optimizer-on-top-of-policy | 判断 P3 混合路线里到底哪种接口最适合空中机械臂强约束控制 |
| **Exp-A5** | 无准入协议 vs `T0-T3` 专家轨迹准入协议 | 验证 warm-start 实验的主要不稳定来源到底来自算法还是数据入口 |
| Exp-B1 | 姿态扰动domain randomization幅度 | 鲁棒性-性能权衡 |
| Exp-B2 | paired demo数据量（0/10/50/200条） | paired data scaling |
| Exp-C1 | HITL refinement轮次（0/50/200/500） | HITL效率曲线 |
| Exp-C2 | sim-to-real物理差异建模（摩擦/质量/延迟） | gap来源分析 |
| **Exp-C3** | SFT warm-start + sim RL vs. 直接 sim RL | warm-start提升幅度（参照2602.12628） |
| **Exp-C4** | 力方向奖励信号 vs. 纯位置奖励 | 跨刚度泛化效果（参照2602.14174） |
| **Exp-C5** | 原始视觉状态 vs. 增加3D关系图状态 | 验证 scene-graph state 对长时序操作和遮挡恢复的增益（参照2603.24083） |
| **Exp-C6** | 末端局部控制 vs. whole-body 协同控制 | 仅机械臂/夹爪控制 vs. 联合底座/载体+机械臂+夹爪的两阶段策略（参照2604.12879） | 验证 whole-body coordination 对高速接近、冲击稳定和抓取鲁棒性的提升 |
| Exp-D1 | 训练策略在真机上的零样本迁移 | 未经微调基线 |
| Exp-D2 | PRISM微调后成功率 | HITL有效性 |

### 4.4+ 控制范式对照协议（R796 新增）

> 目的：把 R793 的 `RL vs optimal control vs hybrid` 从一句口号压成可执行对照，同时补入 `fixed-flight / manipulator-only` 中间基线，避免 whole-body 结论被过度宣称。

| 范式 | 代表实现 | 飞行底座是否学习 | 机械臂是否学习 | 最适合回答的问题 | 主要风险 |
|---|---|---|---|---|---|
| **P0 Fixed-flight / manipulator-only** | 2603.26612 路线 | 否，预定义轨迹/TTC/MPC | 是，RL/beam planning 只管机械臂补偿 | 当前难点主要在操作臂补偿，还是在飞行底座耦合 | 容易高估局部控制能力，低估真实耦合难度 |
| **P1 Pure RL whole-body** | PPO / SAC / FlashSAC / DICE-RL | 是 | 是 | 学习式策略能否端到端吃掉强耦合动力学 | 训练不稳，真机 gap 大 |
| **P2 Pure optimal control** | pseudo-spectral / MPC / terminal-constraint | 是，解析或优化式 | 是，解析或优化式 | 解析/优化控制在强约束段能否更稳、更省风险 | 对模型误差敏感，扩到复杂观测和多任务困难 |
| **P3 Hybrid outer-RL + inner-controller** | DSAM / RL+INDI-PID / RL+MPC | 部分学习 | 部分学习 | 哪些快环约束应交给控制器，哪些策略决策该交给 RL | 接口设计不好会互相打架 |

**P3 内部再细分四类接口**（R800）:
1. **Teacher-student**: 先用 MPC / optimal controller 产专家轨迹或在线 teacher，RL 学策略近似它，优先回答“控制知识能否更快蒸馏进策略”。
2. **Safety shield**: RL 正常输出动作，MPC / CBF / inner-loop controller 只在违反约束时兜底，优先回答“能否保住安全边界而不明显拖慢策略”。
3. **Policy warm-start**: RL / policy 先给优化器初值或候选轨迹，再由 MPC/优化器细修，优先回答“策略能否降低在线优化负担”。
4. **Optimizer-on-top-of-policy**: 策略只给粗提案，优化器始终在上层做约束修正，优先回答“高约束段是否必须持续由解析/优化控制接管”。

**建议执行顺序**：
1. 先跑 **P0**，确认“只学 manipulator 补偿”能站到什么程度，快速判断 D07 的主要瓶颈位置。
2. 再跑 **P1 vs P3**，回答 whole-body 是否真的值得，以及内环控制器是不是必要。
3. 最后才拿 **P2** 做强解析基线，判断是否该把某些高约束段永久交给 optimal control。

**判据**：
- 若 `P0 ≈ P1`，说明当前主要瓶颈不在 whole-body 学习，而在局部操作/状态接口，应优先补观测和奖励。
- 若 `P3 > P1` 且稳定性更好，说明 D07 主线应默认保留 inner-loop controller，不再执着纯 RL。
- 若 `P2` 在风险覆盖和约束满足上显著更强，但任务成功率不低，说明某些阶段应交给解析/优化控制，不应全部学习化。

### 4.5 硬件需求
- **仿真**: NVIDIA GPU（RTX 3090+），Isaac Sim + Isaac Lab
- **真机**: 空中机械臂平台（如DJI M600 + 协作机械臂）、Intel RealSense RGB-D相机
- **遥操作采集**（可选）: 遥控手柄 + 示教软件

### 4.5+ 资源与墙钟预算表（R810 新增）

> 目的：把 D07 从“理论上要跑很多实验”继续压成主人现实可执行的资源计划，避免 whole-body / sim-to-real / tactile 三条线同时开导致资源摊薄。

| 阶段 | 优先实验 | 最低资源 | 推荐资源 | 预计墙钟 | 放行条件 |
|---|---|---|---|---|---|
| **Stage A** | E1 warm-start vs scratch | 1×3090 / 24GB | 1×4090 | 2-3天 | 至少确认 warm-start 是否提升样本效率 |
| **Stage B** | E2 末端局部 vs whole-body | 1×3090 / 24GB | 1×4090 | 3-4天 | 只有 whole-body 明显占优才继续扩这条线 |
| **Stage C** | Exp-A3/Exp-A4 控制范式对照 | 1×4090 | 2×4090 或 1×48GB | 4-6天 | 明确 P1/P2/P3 哪条最值得主推 |
| **Stage D** | E3 控制先验/离线数据接入 | 1×4090 + 采集脚本 | 2×4090 + 独立日志机 | 5-7天 | 若先验显著降早期无效探索，则保留 WHOLE-MoMa/DSAM 路线 |
| **Stage E** | E4 最小 sim-to-real | 1台真机 + 单卡日志机 | 真机 + 独立记录机 + 遥操作采集 | 1-2天/轮 | <50次修补有明显收益，否则先退回补仿真真实性 |

**当前资源建议**：
1. 先只开 **Stage A + Stage B**，不同时启动 tactile 或 multi-GPU 复杂线。
2. 若 Stage B 没证明 whole-body 显著必要，D07 主线就先收缩为 `固定底座/弱扰动 + manipulator compensation`。
3. tactile / visuotactile 基础设施（TacEx / Tac2Real）先保留为扩展位，不抢当前主线 GPU 预算。

### 4.6 最小可验证实验路径（R784 新增）

> 目标：先验证 D07 的关键分歧到底在“训练器”“控制先验”“whole-body 协同”还是“sim-to-real 适配”，不一开始就把所有变量搅在一起。

#### E1：纯 RL vs warm-start + RL
- **对比**：PPO/SAC 从零训练 vs SFT warm-start + 同训练器
- **场景**：IsaacLab-Gripper-Drone-Pickplace 基础抓取任务
- **指标**：达到 80% 成功率所需步数、phase score 收敛速度、训练稳定性
- **门槛**：若 warm-start 样本效率提升 ≥20%，则后续默认保留 warm-start 入口
- **本轮收缩后的执行版本（R812）**：第一轮只跑 `PPO scratch vs PPO+BC warm-start`，固定 **1 个任务、3 个随机种子、12 小时墙钟上限**。只记录 `success rate / phase score / 首次达到 60% 与 80% 成功率的步数 / crash-or-reset 次数`，暂不并开 SAC、whole-body、scene-graph、触觉。这样可以先回答一个最值钱的问题：**warm-start 值不值得常驻默认入口**。

#### E2：末端局部控制 vs whole-body 协同
- **对比**：只控机械臂/夹爪 vs 联合载体+机械臂+夹爪
- **场景**：带初始速度的高速接近抓取或短距推靠任务
- **指标**：接触成功率、冲击后稳定时间、掉物率
- **门槛**：若 whole-body 在高速场景显著更优，则 Exp-C6 升级为 D07 主实验轴

#### E3：控制先验/离线数据是否值得接入
- **对比**：纯 RL vs WHOLE-MoMa 式 `WBC/状态机数据 → 离线RL/在线精修`
- **场景**：门/抽屉/放置三类长时序任务任选一类先跑通
- **指标**：初始成功率、收敛墙钟时间、失败类型分布
- **门槛**：若控制先验能明显减少早期无效探索，则后续把“控制先验+RL”列为主线，而不是只留纯 RL

#### E4：最小 sim-to-real 检查
- **对比**：零样本部署 vs 少量 HITL/PRISM 修补
- **指标**：真机成功率、修补轮次、每轮带来的边际收益
- **门槛**：若 <50 次人类修补就能显著拉升成功率，则保留 PRISM/real-anchor 路线；否则优先回头补仿真真实性和观测接口

**首轮建议顺序**：
1. 先做 E1，尽快确认 warm-start 值不值得常驻。
2. 再做 E2，判断 D07 是否真的需要往 whole-body 走。
3. E3 只在 E2 成立后展开，避免过早引入复杂控制先验。
4. E4 放在最末，只挑最稳的一条策略去真机，不让真机调试吞掉研究节奏。

**与阶段 gate 的绑定方式**：
- E1 对应 Gate-G0/G1，重点看 S1/S2 是否能快速过线。
- E2 对应 Gate-G2，只有 whole-body 在 S3 明显占优才升级为主实验轴。
- E3 用来决定“纯 RL”还是“控制先验+RL”成为默认路线。
- E4 只有在 Gate-G3 通过后才允许扩更多真机任务。

### 4.6+ E1 首轮执行蓝图（R812 新增）

| 项 | 固定设置 |
|---|---|
| **任务** | IsaacLab-Gripper-Drone-Pickplace 最基础抓取子任务，不加遮挡、不加图状态 |
| **训练器** | PPO only |
| **对照组** | Scratch / BC-50 / BC-200 |
| **随机种子** | 3 个 |
| **统一预算** | 每组最多 12h 或达到 85% success 即停 |
| **统一日志** | success、phase score、episode length、reset 原因、姿态恢复时间 |
| **放行条件** | BC-50 或 BC-200 至少一组在 80% success 步数上优于 scratch ≥20% |
| **判停条件** | 若 3 组在 6h 后都未过 40% success，则先回查 reward / observation，不继续扩 whole-body |

**为什么先这么收缩**：
1. 这一步直接服务 REPORT 第五节的四周排期，不再停留在“实验矩阵很多”。
2. 它和本地笔记 `Isaac Lab`、`Aerial-Manipulator-RL` 的共同结论一致，先确认 **统一训练底座 + warm-start** 是否能减少早期无效探索。
3. 若这一步都不成立，后面 whole-body、hybrid、sim-to-real 大概率只是在更贵地复现同样问题。

### 4.6++ E1 烟测门槛与专家轨迹接入契约（R814 新增）

### 4.6+++ E1 数据质量记账规则（R819 新增）

> 这一步是把 4.3++++ 的 `T0-T3` 真正接到 E1 上，避免 12h 跑完才发现问题出在数据。

| 记账项 | 定义 | 用途 |
|---|---|---|
| **DCS (Demo Coverage Score)** | 专家轨迹对 `approach / align / contact / complete` 四段的覆盖均衡度 | 防止 BC 数据只覆盖接近段，导致 warm-start 看起来“无效” |
| **RVS (Replay Validity Score)** | 专家轨迹在固定 seed 下可稳定 replay 的比例 | 判断是否值得把该批数据用于 BC 初始化 |
| **PCS (Phase Consistency Score)** | 轨迹 phase 标签与实际状态转移的一致性 | 防止 phase score 改善只是标签噪声 |
| **RTC (Reset Trace Completeness)** | 带结构化 reset reason 的轨迹比例 | 支撑后续失败归因与 smoke test 排错 |

**执行规则**：
1. `BC-50 / BC-200` 在进入 E1 正式跑数前，至少要满足 `RVS ≥ 0.9`、`RTC = 1.0`。
2. 若 `DCS` 严重偏斜，允许 warm-start 继续跑，但结论只能写成“局部阶段 warm-start”，不能宣称全任务有效。
3. 若 `PCS` 不稳定，先修 phase 标签，不允许把 phase score 作为主结论。

> 目的：避免一上来就开 12h 正式实验，结果 6 小时后才发现 BC 数据格式、phase 日志或 reset 统计根本没接好。

#### Step 0: 30min smoke test（正式训练前必过）
- **Smoke-S0 环境可启动**：3 个 seed 都能正常 reset / rollout，前 100 episode 无持续 NaN / 爆振。
- **Smoke-S1 日志完整**：`success / phase score / episode length / reset reason / attitude recovery time` 五类日志都能导出。
- **Smoke-S2 PPO 基线可学**：scratch 组在 30min 内至少看到 `phase score` 有单调爬升趋势，而不是纯随机噪声。
- **Smoke-S3 BC 权重可加载**：BC-50/BC-200 至少能成功初始化策略，且前 10 个 episode 动作方差不塌缩。

若 `Smoke-S0~S3` 有任一失败，本轮禁止进入 12h 正式跑数，先修接口。

#### 专家轨迹最小字段契约
每条 expert trajectory 至少应包含：
- `obs`: 与 PPO 完全一致的观测字段顺序
- `action`: 与环境动作空间完全一致的维度和归一化范围
- `done / truncated`
- `phase label`: `approach / align / contact / complete`
- `reset reason`（若来自回放或示教失败片段，也要保留）

**硬规则**：
1. BC 数据和 PPO 训练观测字段不允许有“少一个关系量、或额外多一个辅助量”的漂移。
2. phase label 若缺失，则 BC 数据最多只用于 warm-start 行为克隆，不允许拿来解释为什么 phase score 提升。
3. 若 reset reason 缺失，后续不允许把 warm-start 失败归因为“策略不稳”，因为可能只是回放数据本身脏。

#### 正式 12h 训练前的放行条件
- smoke test 全过
- 至少有 1 组 BC 数据能成功初始化并跑满 30min
- reset reason 可聚合成结构化统计，而不是只剩 console 文本
- phase score 已拆到 `approach / align / contact / complete` 四段

**这一步的研究价值**：
它把 D07 当前最容易“假推进”的部分钉死了。后续如果 warm-start 无收益，就能更干净地区分是 **BC 数据入口有问题**，还是 **warm-start 本身确实不值得保留**。

### 3.6 🆕 R777 新增：C3/C4 的图状态补强
KG-M3PO (2603.24083) 给 D07 一个很实用的补强点：把 open-vocabulary 检测结果在线落到 **metric 3D scene graph**，再让策略只查询少量关系节点（如末端-目标距离、遮挡边、可接近边、容器/支撑关系），可以显著降低纯像素策略在遮挡和长时序任务里的状态歧义。对 D07 来说，这不是替代 RL，而是给 C3 奖励层和 C4 验收层补一个更稳定的语义状态接口。

## 4.5 硬件/服务器需求
- **开发机 / 训练机**：至少 1× RTX 4090 / A6000 级 GPU（24GB+ 显存）作为 Isaac Lab 首轮训练基线；若做 `128 env` 并行 + 视觉输入，优先 48GB 显存或多卡。
- **最小可运行配置**：单卡 24GB + 降低并行环境数（如 32/64 env）+ 状态输入优先，用于 E1/E2 烟测与 schema/replay 验证。
- **多卡扩展**：当进入 `触觉 / 多视角 / whole-body + risk coverage` 联合阶段，再考虑 2×GPU 或多节点；在 E1/E2 之前禁止因为“未来要多模态”提前扩资源。
- **CPU / 内存**：建议 16 核 CPU、64GB RAM 起步；若同时跑大规模日志、回放与风险边界扫描，优先 128GB RAM，避免 replay / case-suite 与训练抢内存。
- **存储**：NVMe SSD 1TB+，单独预留 `checkpoints / replay buffer / expert trajectories / deterministic case-suite logs`。
- **真机前验证资源**：L4 风险覆盖（ROBOGATE 式粗扫+边界细化）与 case-suite 回放默认与主训练分离，避免训练过程把风险扫描算力吞掉。

### 4.6 四周执行时间线（面向真正开跑）
| 周次 | 目标 | 唯一交付物 | 禁止事项 |
|---|---|---|---|
| **W1** | 站住 E1 数据入口与烟测 | `RVS/PCS/RTC` 过线 + 30min smoke test 全绿 | 禁止提前开 whole-body / tactile / scene-graph |
| **W2** | 完成 E1 正式对照 | `warm-start vs scratch` 首轮结论 + 资源冻结动作 | 禁止因为单个 seed 漂亮就扩主叙事 |
| **W3** | 只做 E2 | `fixed-flight vs whole-body` 结论 | 禁止同时并开 hybrid 与 sim-to-real |
| **W4** | 只在 E2 稳定后做 E3 或最小 sim-to-real | `pure RL / optimal / hybrid` 中的 go/no-go | 禁止 L4 未过时使用 deployable / real-ready 口径 |

### 4.7 sim-to-real 升格条件（R840补强）
> D07 现在最容易犯的错，是仿真里一条线刚跑顺，就急着说“可以上真机”。这里把升格条件写死。

只有同时满足以下条件，D07 才允许从“仿真内成立”升格到“值得做最小真机验证”：
1. **L0/L1 已稳定**：至少基础稳定与局部操作在 3 seeds 下可重复。
2. **当前主线已冻结**：`local compensation / whole-body / hybrid` 只能有 1 条主叙事，不能三条并存。
3. **L4 不显著掉线**：风险覆盖不能明显差于当前最稳基线。
4. **适配成本受控**：若要靠 HITL / real-anchor 修补，默认要求 `<50` 次修补内能看到稳定增益，否则不升格。
5. **表达降级规则生效**：即使进入真机最小验证，只要 L4 还没完全站住，对外仍统一表述为 `low-cost adaptation` 或 `仿真到真机最小验证`，不能直接写 deployable。

### 4.8 当前默认下轮建议
- 若 E1 仍未形成结构化首轮读数：继续守 `data-gated acceleration`，优先修 replay / schema / phase 标签。
- 若 E1 已稳但 E2 未做：下轮唯一动作就是 `fixed-flight vs whole-body`。
- 若 E2 证明 whole-body 不值：主线冻结为 `local compensation`，不再让 hybrid 抢戏。
- 若 E2 已证实 whole-body 值得继续：再进 E3，比较 `pure RL / optimal control / hybrid`。

## 4.7 首轮 no-go 后的主叙事默认收束规则（R871 新增）

> 来自本轮对 `D07/README.md`、`experiments.md`、近几轮 D07 收束记录与 QMD 回流结果的再次压缩。既然前面已经把 `warm-start → fixed-flight vs whole-body → hybrid vs pure RL` 的串行门槛写出来了，下一步就不能只停在“哪些线该降级”，还要继续回答：**首轮结果出来后，论文默认该收成哪一句话，按什么顺序冻结标题位。** 否则 D07 仍会让 `data-gated acceleration / local compensation / whole-body / hybrid` 同时占主标题候选。

### 默认收束顺序固定为三段

1. **先看 warm-start 是否只是入口层收益**  
   若 `BC/SFT warm-start` 只改善 `60%/80% success 达线步数`，但对 `L1 局部操作质量`、`L2 whole-body 协同`、`SARR` 没有稳定正收益，则默认把它收成 **data-gated acceleration**，只能讲“训练入口更省样本”，不能越级写成控制创新。

2. **再看 fixed-flight 是否揭示主瓶颈仍在耦合扰动**  
   若 `P0 fixed-flight / manipulator-only` 持续在 `phase score / 掉物率 / 冲击后稳定时间` 上压制 whole-body，则默认先把 whole-body 主叙事判为 no-go，论文收成 **local compensation under coupled-disturbance bottleneck**；也就是当前更诚实的结论是“先把底座扰动与局部补偿处理好”，而不是硬讲统一 whole-body 协同已经成立。

3. **只有前两者都不过主导位时**，才允许 hybrid 抢主标题  
   也就是说，只有当 hybrid 在 `L0 基础稳定 / L4 风险覆盖 / SARR` 至少一轴稳定占优，且维护复杂度、内环依赖、部署额外成本没有明显恶化时，才允许正式收成 **deployable hybrid control**。否则 hybrid 仍默认留在 supporting evidence 或工程兜底位。

### 为什么要把顺序写死
- `warm-start` 很容易因为曲线更好看，被误包装成“策略更强”；
- `fixed-flight` 很容易因为局部更稳，被忽视成“只是简化 baseline”，但它其实可能在诚实暴露 D07 的真实瓶颈还在耦合底座；
- `hybrid` 很容易因为工程上更稳，被直接写成主创新，但如果它只是靠更高维护成本换稳定，就不该自动抢论文主叙事。

### 当前 D07 默认 go/no-go 规则
- **只省样本，不增 L1/L2/SARR** → 收成 `data-gated acceleration`
- **fixed-flight 持续压制 whole-body** → 收成 `local compensation`
- **hybrid 稳定占优且成本不过度恶化** → 才收成 `deployable hybrid control`
- 其余情况默认维持 `仿真内成立 / 不足以主讲部署`

### 4.3++++++++++++ 首轮摘要句式冻结规则（R873 新增）

> 目的：D07 现在最容易出现的失控点，不是实验不会跑，而是首轮结果一出来后 **warm-start / fixed-flight / hybrid / whole-body** 四条线都能各讲一句漂亮话，最后标题、摘要、主表同时拥挤。这里把 **首轮结果 → 默认摘要句式** 写死，保证论文主叙事只保留 1 条主句，其余全部降级为 supporting evidence。

| 首轮结果模式 | 允许使用的默认摘要句式 | 禁止越级表述 | 应降级的 supporting evidence |
|---|---|---|---|
| **warm-start 只改善达线速度**，但 `L1/L2/SARR` 无稳定提升 | **data-gated acceleration for aerial manipulation RL** | 不得写成 `better control policy` / `deployable sim-to-real method` | BC/SFT 提速、早期 loss 更稳、首小时收益 |
| **fixed-flight / manipulator-only** 持续压制 whole-body | **local compensation under coupled-disturbance bottleneck** | 不得写成 `whole-body coordination solved` | fixed-flight phase score 更高、局部接触更稳 |
| **hybrid** 在 `L0/L4/SARR` 至少一轴稳定占优，且维护成本可控 | **deployable hybrid control for constrained aerial manipulation** | 不得再把纯 RL 写成主线 | inner-loop 兜底、风险覆盖更高、恢复更稳 |
| whole-body 仅在单任务或单 seed 略优，跨扰动不稳 | **whole-body remains a long-horizon target, not the current contribution** | 不得写成 `general whole-body aerial manipulation` | 某单任务提升、个别场景更平滑 |
| sim-to-real 零样本弱，但 `<50` 次修补稳定有效 | **low-cost post-sim adaptation protocol** | 不得写成 `zero-shot sim-to-real success` | HITL 修补收益、warm-start 迁移提速 |

**执行规则**：
1. 首轮后只允许从上表选 **1 条主句** 进入标题/摘要第一句，其余现象全部降到主表附注或 appendix。
2. 若没有任何一条完全满足，就默认退回 **`current evidence supports only a staged validation protocol, not a new control claim`**。
3. 后续新增论文只能增强这些句式里的某一条，不能新开第五条主叙事。

### 4.3+++++++++++++ 首轮主叙事选择优先级（R873 新增）

> 当多个结果同时为正时，按下面顺序抢主摘要位，低优先级不得覆盖高优先级。

1. **deployable hybrid control**
2. **local compensation under coupled-disturbance bottleneck**
3. **low-cost post-sim adaptation protocol**
4. **data-gated acceleration**
5. **whole-body remains future work**（只能作约束句，不能作主卖点）

这条优先级的含义很简单：D07 是部署导向方向，不是单纯追训练提速。只要 hybrid 或可部署局部补偿站住，就不能再让 warm-start 抢标题位。

## 五、论文写作计划

- **目标会议**: ICRA 2027 或 IROS 2027（机器人+无人机交叉方向）
- **DDL**: ~2026-09（ICRA submission）
- **时间线**:
  - 2026-05~06: Isaac Lab环境部署 + 基线训练跑通
  - 2026-06~07: 消融实验 + sim-to-real验证
  - 2026-07~08: PRISM微调实验 + ROBOGATE风险评估
  - 2026-08~09: 论文撰写 + 图表制作

### 5.1 投稿证据包（R804新增）

> D07 后续不能只说“跑通了训练 + 做了真机”，而要提前锁定哪些证据足以支撑论文主张，避免到 7 月才发现结果很多但故事线不闭环。

| 论文物料 | 对应实验/证据 | 最迟产出时间 | 进入论文的位置 |
|---|---|---|---|
| **Fig.1 控制范式总览图** | `P0/P1/P2/P3` 四类控制范式 + D07 五层验收矩阵 | 5月上旬 | Intro / Method |
| **Fig.2 稳定性-成本主结果图** | `pure RL / optimal control / hybrid inner-loop` 在成功率、恢复时间、推理延迟上的三维对比 | 6月上旬 | Main result |
| **Fig.3 sim-to-real 适配效率曲线** | 零样本、warm-start、PRISM/HITL 修补的成功率-修补轮次曲线 | 6月中旬 | Main result |
| **Tab.1 控制范式统一主表** | P0-P3 × S1-S5 case-suite / Gate-G0~G4 结果 | 6月上旬 | Main result |
| **Tab.2 奖励与观测消融表** | dense / GRM / ARM / 力方向奖励 / 3D关系图状态 | 6月中旬 | Ablation |
| **Tab.3 部署前风险覆盖表** | ROBOGATE 边界覆盖率、漏检风险区、误报率 | 6月下旬 | Safety / Deployment |
| **Video 1 真机闭环演示** | 至少 1 个扰动下抓取/推靠任务，展示恢复而非只展示最顺利样例 | 7月 | Supplement |

### 5.2 投稿放行条件（R804新增）

- **主投 ICRA 2027**：至少要有 `Tab.1 + Fig.2 + Fig.3`，并且 hybrid 路线在 **稳定性或风险覆盖** 上相对 pure RL 有清晰优势，不要求所有任务都绝对最高分。
- **备投 IROS 2027**：如果真机补证较弱，但 `控制范式统一对照 + sim-to-real 适配效率 + 风险覆盖` 三块证据完整，可主打空中机械臂 RL 的系统协议与部署方法学。
- **暂不投稿**：如果当前结果仍停在 L0/L1，或只证明某个训练器略强，但没有回答“为什么 inner-loop / hybrid 值得保留”，则继续收敛实验，不急着成稿。

### 5.3 四周执行排期与判停规则（R811新增）

> 目的：把 D07 从“实验列表很多”继续压成主人能真的开跑的四周推进单，不让 GPU 时间被 whole-body、sim-to-real、触觉三条线同时吃光。

| 周次 | 主任务 | 只保留的变量 | 交付物 | 判停条件 |
|---|---|---|---|---|
| **Week 1** | 跑通 `E1 warm-start vs scratch` | 只固定 1 个基础抓取任务，训练器先锁 PPO | 收敛曲线、达到 80% 成功率步数、失败回放 10 条 | 若 warm-start 提升 <10%，后续降级为可选入口，不再占主线 |
| **Week 2** | 跑 `E2 末端局部 vs whole-body` | 只比较 `manipulator-only` 与 `whole-body`，不并开触觉/图状态 | 高速接近任务结果表、冲击后稳定时间、掉物率 | 若 whole-body 优势不显著，则 D07 主线先收缩到局部操作补偿 |
| **Week 3** | 跑 `Exp-A3/Exp-A4` 控制范式对照 | 只保留 `P1 pure RL / P2 optimal control / P3 hybrid` 三类 | 控制范式统一主表、SARR 初版排序 | 若 hybrid 不优于 pure RL 且成本更高，则不再把 inner-loop 作为论文主轴 |
| **Week 4** | 只挑最稳路线做 `E4 最小 sim-to-real` | 禁止多路线同时上真机 | 零样本结果、<50 次修补收益、风险边界首轮记录 | 若修补 50 次内仍无明显提升，先退回补仿真真实性与观测接口 |

**执行硬规则**：
1. 每周只允许一个主问题，不同时开 whole-body、tactile、scene-graph 三条扩展线。
2. 只有上一周结论成立，下一周才继续；否则立刻收缩路线，不做“再跑一点看看”。
3. 四周结束后若仍只证明“某训练器略强”，D07 就不该继续写成论文主线，而应降级成空中机械臂控制 baseline 工程线。

### 5.4 论文主叙事选择器（R811新增）

根据前四周结果，D07 只保留三种成稿叙事，避免后面故事线反复漂移：

1. **Hybrid 主叙事**
   - 条件：`P3 hybrid` 的 SARR 最高，且 L0/L3/L4 明显优于 pure RL
   - 论文核心句：**空中机械臂的关键不是把一切都学掉，而是让 RL 负责任务适应，让 inner-loop/optimizer 守住快环约束与部署风险**
2. **Whole-body 主叙事**
   - 条件：`E2` 明确证明 whole-body 在高速接近/冲击恢复中显著更强
   - 论文核心句：**空中机械臂真正的难点在载体-机械臂强耦合，局部末端补偿不足以支撑高速精细操作**
3. **Adaptation 主叙事**
   - 条件：warm-start / PRISM / real-anchor 带来的 L3 收益最大，而控制范式差异次之
   - 论文核心句：**D07 的瓶颈主要不是训练器，而是 sim-to-real 适配效率与部署前风险收敛速度**

**默认优先级**：Hybrid 主叙事 > Whole-body 主叙事 > Adaptation 主叙事。只有当前一条叙事证据不足时，才降到下一条。

### 3.4 🆕 R775 新增：C2 耦合动力学的 DSAM 关键细节深化

**DSAM (2512.21085) 作为 C2 架构的实测锚点**，已在 R771 引入，以下是其 RL-policy 设计的关键实现细节，对 D07 实验设计有直接指导价值：

| 设计维度 | DSAM 具体做法 | D07 可复用/改进点 |
|---------|------------|----------------|
| **Observation space** | 29维：无人机线速度+角速度+旋转矩阵+关节角+末端目标相对位置+末端姿态误差 | D07 扩展：加入机械臂末端-目标距离/力矩传感器读数 |
| **Action space** | 2-DoF aerial manipulator（2个关节电机），输出归一化关节力矩 | D07 扩展：7-DoF 机械臂 + 夹爪，动作空间更大 |
| **训练器** | PPO（on-policy），inner-loop 用 INDI + PID | D07 对比：SAC / FlashSAC + 不同 inner-loop 对比 |
| **Domain randomization** | 摩擦随机化（无摩擦 → 正常摩擦 5 倍范围）+ 质量随机化（±16%） | D07 扩展：参照 DSAM Sec. IV-B，加入姿态扰动 DR（roll/pitch ±15°，yaw ±30°）|
| **Sim-to-real gap 处理** | 仅靠摩擦+质量 DR 即可零样本迁移（双臂旋翼平台） | D07 关键问题：6-DoF 空中机械臂是否仍可零样本？或需要额外 DR？ |
| **实机部署** | 0.18ms 推理延迟（PPO policy + INDI/PID），cm 级末端精度 | D07 目标：7-DoF 末端精度 + 推理延迟 < 5ms |

**DSAM 给 D07 的关键 insight**：
- C2 双层架构（PPO outer + INDI/PID inner）已被 DSAM 验证是可行且高效的
- 关键 DR 项：摩擦随机化 > 质量随机化 >> 其他物理参数 DR
- 零样本迁移的前提：仿真物理足够准确（Isaac Sim > PyBullet/MuJoCo）

### 3.5 🆕 R775 新增：Exp-C3 详细设计（基于 SFT Warm-Start）

参照 **Beyond Imitation (2602.12628)** 的三阶段路线，D07 的 Exp-C3 设计如下：

**实验设置**：
- **任务**：Isaac Lab Lift-Cube 任务（扩展到带无人机姿态扰动的变体）
- **基线组**：直接 PPO 训练（无 SFT warm-start）
- **实验组**：SFT warm-start → PPO fine-tuning

**SFT warm-start 具体流程**：
1. 收集 50/200/500 条专家轨迹（遥操作或动捕回放）
2. 用行为克隆（BC）在专家轨迹上预训练 policy
3. 用预训练 policy 初始化 PPO 训练

**预期结论**：
- SFT warm-start 应在 < 50 条轨迹时带来 > 20% sample efficiency 提升
- 轨迹数 > 200 时，warm-start vs. scratch 差距缩小（PPO 本身 sample efficient）
- 关键控制点：warm-start policy 是否在 PPO 阶段快速遗忘（alignment forgotten）

**新增 TODO**：
- [ ] 🆕 R775: 确认 IsaacLab-Gripper-Drone-Pickplace 是否支持导入外部专家轨迹
- [ ] 🆕 R775: 评估 50 条 vs. 200 条 vs. 500 条专家轨迹的采集成本

## 六、后续 TODO
- [ ] 确认 IsaacLab-Gripper-Drone-Pickplace 代码可复现性
- [ ] Isaac Lab 在主人服务器上的部署验证
- [ ] 确定具体空中机械臂平台型号
- [ ] 设计 phase score 具体奖励函数
- [ ] 确认是否需要 RealSense 相机集成
- [ ] 🆕 R775: 确认 IsaacLab-Gripper-Drone-Pickplace 是否支持导入外部专家轨迹（Exp-C3 前置）
- [ ] 🆕 R775: 评估 50/200/500 条专家轨迹的采集成本（Exp-C3 前置）
- [x] 🆕 R765: 引入 RoTO (2510.21609) 触觉 RL 基准设计作为过程奖励参考
- [x] 🆕 R765: 引入 2505.16547 遮挡感知零样本泛化路线纳入 OOD 压测设计
- [x] 🆕 **R769**: 引入 2502.20396 divide-and-conquer distillation → C3 分层奖励协同方案
- [x] 🆕 **R769**: 引入 2501.02902 Isaac→ROS2 迁移协议 → sim-to-real 验收参考
- [x] 🆕 **R769**: 引入 2602.14174 力方向学习 → C3 奖励辅助信号
- [x] 🆕 **R769**: 引入 2602.12628 SFT warm-start → 实验 Exp-C3
- [x] 🆕 **R775**: DSAM (2512.21085) 关键实现细节深化 → C2 架构验证
- [x] 🆕 **R775**: Exp-C3 详细实验设计（warm-start vs. scratch 对比方案）
- [x] 🆕 **R800**: 引入 2502.02133，将 P3 hybrid 路线细分为 teacher-student / safety shield / policy warm-start / optimizer-on-top-of-policy 四类接口，并新增 Exp-A4
- [x] 🆕 **R796**: 新增 4.4+「控制范式对照协议」，把 `fixed-flight/manipulator-only vs pure RL vs optimal control vs hybrid` 四类路线压成正式实验矩阵
- [x] **R780**: 新增 FastGrasp (2604.12879) 到 related work，补出 Exp-C6“末端局部控制 vs whole-body 协同控制”对照，开始把 D07 从纯末端策略扩到高速 whole-body 抓取协议。
- [x] **R811**: 新增 5.3「四周执行排期与判停规则」+ 5.4「论文主叙事选择器」，把 D07 从“实验矩阵齐全”继续推进到“按周收缩路线、按证据选论文故事线”的可执行状态
- [x] **R841**: 新增「sim-to-real 升格条件」与「首轮后唯一主叙事选择器」，明确只有在 L4 风险覆盖与低成本修补/零样本门槛同时成立时，才允许把 D07 从“仿真内成立”升级为 deployable / low-cost adaptation 叙事；否则一律冻结为 supporting evidence，避免 whole-body / hybrid / adaptation 三线并烧。

## R841 更新（2026-04-20）

**本轮推进：把 D07 的“首轮之后怎么冻结主线”正式写死。**

### 新增判断 1：sim-to-real 不再跟着仿真结果自动升格
- 即使 warm-start、hybrid 或 whole-body 在仿真里有增益，也**不能自动写成可部署**。
- 只有同时满足：
  1. 至少 1 个最小任务零样本可跑，或 `<50` 次修补就能稳定提升；
  2. `L4` 风险覆盖不过度劣化；
  3. 修补收益能清晰归因到 `warm-start / HITL / real-anchor / hybrid shield` 之一；
  才允许把 D07 叙事升级到 `low-cost adaptation` 或 `deployable hybrid`。

### 新增判断 2：首轮后只允许保留 1 条主叙事
D07 首轮实验结束后，只允许在下面 5 条里选 **1 条** 做主叙事：
- **A. data-gated acceleration**：warm-start 稳定提速，但 whole-body / hybrid / sim-to-real 还没站住
- **B. local compensation**：fixed-flight / manipulator-only 明显更稳
- **C. whole-body coordination**：E2 证明联合协调确实带来稳定增益
- **D. deployable hybrid control**：hybrid 同时过稳定性 + 风险 + 成本门槛
- **E. low-cost adaptation**：零样本一般，但低成本修补稳定有效

其余所有线默认降级为 **supporting evidence**。如果 A-E 都不满足，则当前只能对外表述为：
> **D07 仿真内训练/验收协议已收紧，但尚未进入方法主张冻结阶段。**

### 本轮结论
- **扫描方向**：D07 Isaac RL 机械臂控制
- **本地扫描结果**：QMD 检索 `Isaac Lab aerial manipulator reinforcement learning warm-start hybrid inner-loop sim-to-real fixed-flight --no-rerank` 仍主要回流 D07 本地方向文档与既有锚点，未发现需要立即完整入库的新高价值论文，因此本轮 **0 篇新入库**。
- **REPORT 推进点**：不是再扩论文，而是把 `仿真增益 ≠ 可部署`、`首轮只许 1 条主叙事` 这两条规则写死，避免后续 whole-body / hybrid / sim-to-real 三线并烧。
- **下轮建议**：继续 D07 但只做一个动作——把 `E1/E2/E3` 的首轮结果记录模板补成可直接填数值的表格，方便一出来就冻结路线。


### 4.3++++++++++++++++ 首轮后默认标题收束规则（R873 新增）

> 目的：D07 现在已经把 `data-gated acceleration / local compensation / deployable hybrid control / low-cost adaptation` 这些主叙事桶写清楚了，但还缺最后一步——**一旦某条线首轮判 no-go，标题默认该怎么诚实收束**。否则实验里已经知道 whole-body 或 hybrid 不该抢标题，写作时又会把 `warm-start / whole-body / hybrid / sim-to-real` 一起塞回摘要和标题。

| no-go 触发模式 | 默认标题收束 | 不再允许并列竞争的项 | 默认后续动作 |
|---|---|---|---|
| `warm-start` 主要只改善达线速度，`L1/L2/SARR` 无显著净增益 | **data-gated acceleration for aerial manipulator policy training** | `control innovation`、`whole-body coordination`、`deployable hybrid control` | 继续补数据入口、phase 标签与 reset 契约，不再把 warm-start 当控制贡献 |
| `fixed-flight / manipulator-only` 长期压制 whole-body，且 `L2` 迟迟不过线 | **local compensation under coupled-disturbance bottleneck** | `whole-body aerial manipulation` 主标题位 | 把 whole-body 收缩为远期扩展，优先压实底座扰动归因与局部补偿甜区 |
| `hybrid` 只在单 seed / 单任务 / 单指标占优，`L4` 或维护复杂度不过线 | **hybrid as supporting engineering baseline** | `deployable hybrid control`、`field-ready control` | hybrid 只保留为强对照，不再抢主线资源 |
| 零样本迁移弱，但 `<50` 次修补能稳定抬升 `L3` 且 HITL 成本低 | **low-cost post-sim adaptation for aerial manipulator control** | `zero-shot sim-to-real`、`real-ready whole-body` | 主打低成本适配协议，不夸大为零样本部署 |
| `whole-body` 在 `L2` 有局部正信号，但 `L0/L4` 仍明显不稳 | **whole-body remains supporting evidence under deployment constraints** | `unified whole-body intelligence`、`deployable whole-body control` | whole-body 只保留为补充实验，先回补基础稳定与风险覆盖 |

**冻结规则**：
1. 首轮结果出来后，D07 标题默认只允许保留 **1 条主叙事**；其余全部自动降级为 supporting evidence、对照或 appendix。
2. 只要 `fixed-flight / manipulator-only` 仍显著更稳，标题里一律不得抢跑 `whole-body`。
3. 只要 `hybrid` 没同时过 `SARR / L4 / 维护复杂度` 三门槛，就不得用 `deployable`、`field-ready` 之类词。
4. 只要 `warm-start` 的收益主要停在首小时曲线，标题里它就只能是 **training recipe / data-gated acceleration**，不能冒充控制架构突破。

### 4.3+++++++++++++++++ D07→D01 汇报句式对齐规则（R873 新增）

> 目的：让 D07 的对外汇报口径与 D01 当前的 `interface-first / stage-aware supervisor / hover-window evidence` 收束方式一致——都遵守“**先讲主增益来源，再讲哪些线只是 supporting evidence**”。这样后续跨方向汇报不会又把 warm-start、whole-body、hybrid 同时端上来。

| 首轮结果模式 | 汇报第一句默认写法 | supporting evidence 默认写法 |
|---|---|---|
| warm-start 只改善提速 | **本轮确认 warm-start 主要是训练入口加速器，不是控制创新。** | whole-body / hybrid 暂不升主叙事 |
| fixed-flight 显著更稳 | **本轮确认当前主瓶颈仍在耦合扰动下的局部快速补偿。** | whole-body 仅作远期扩展证据 |
| hybrid 过 `SARR/L4/维护复杂度` 三门槛 | **本轮确认 hybrid 更适合作为可部署控制主线。** | warm-start 退为训练配方，whole-body 退为实现形态 |
| `<50` 次修补显著提升 `L3` | **本轮确认 D07 当前最强卖点是低成本后适配协议。** | 零样本迁移与 whole-body 不抢标题 |

**规则**：
1. 汇报第一句只能讲 **唯一主叙事**，第二句才允许补 supporting evidence。
2. 只要 `L4` 没过，汇报里一律不用 `可部署 / 可上真机 / field-ready`。
3. 若 `whole-body` 未过 `L2`，汇报里一律不得先写 whole-body 成立。
