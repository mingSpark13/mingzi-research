---
type: "overview"
id: "overview.方向_空中VLN_技术路线图"
pageType: "overview"
tags: ["空中视觉语言导航", "VLA", "3D感知", "D06"]
summary: "D06 继续收束为 packet-first + verifier-first 主链，同时吸收 Action Agent 的 imagined-goal 中介与 SAGA 的高速局部避障经验，优先增强 packet 到 controller 的低延迟闭环。"
origins: ["../../05_科研研究/D06_空中视觉语言导航/REPORT.md"]
updated: "2026-05-08"
---

# 方向_空中VLN_技术路线图

**一句话结论**: D06 当前最稳的骨架仍是 **packet-first + verifier-first + stage-bounded recovery**，planner 内部是否值得显式细分认知模块，现在只作为强对照位而非默认主方法。

## 技术格局：四条路线

| 路线 | 代表工作 | 当前价值判断 | 风险边界 |
|------|---------|-------------|---------|
| **端到端VLA** | [[sources/AerialVLA_2603.14363|AerialVLA]], AutoFly, DroneVLA | 适合做轻量低延迟基线，能覆盖 tracking-heavy 近场执行 | 语义约束与安全边界难显式诊断 |
| **层次化/Packet-first** | HTNav, OnFly, Ro-SLM | 仍是 D06 默认主链，利于统一 planner, verifier 与 controller 契约 | packet schema 若欠表达，晚期阶段会持续 reject |
| **细粒度认知模块化** | FineCog-Nav | 先作为 diagnostic baseline，检查 instruction adherence 与 memory-hit-to-waypoint 转化 | 若只提升 benchmark 可解释性，不得抢主叙事 |
| **Benchmark+数据工厂** | UAV-VLN Survey, OpenFly, AirNav | 支撑数据闭环与现实评测，是方法判线的必要底座 | 自身不提供主算法净收益 |

## 当前三大 Gap

1. **3D语义搜索仍缺统一可执行 packet**：收益必须先转成更高质量的 `Semantic Waypoint Packet`，不能只停在 planner 内部解释。
2. **late-stage recovery 容易越界**：search 阶段可能有效，但 approach/inspect/manipulate-ready 往往更像 handoff 或 tracking shell 的问题。
3. **模块化 planner 的净收益尚未证实**：FineCog-Nav 只有同时改善 `instruction adherence + memory-hit-to-waypoint conversion + pre-verifier semantic mismatch` 时，才允许升格。

## 我们的切入点

- **主执行链**：`planner -> verifier -> controller`，统一通过 `Semantic Waypoint Packet` 交接。
- **恢复边界**：默认只保留 `search-bounded` 在线恢复，晚期阶段优先 recommendation-only、packet repair 或 hard-stop。
- **最新推进（2026-05-08）**：在保留 FineCog-Nav `diagnostic baseline first` 定位的前提下，新增吸收 Action Agent 的 imagined goal video 中介思路，以及 SAGA 的固定 motion anchor 高速局部规划经验，优先增强 `packet -> controller` 的低延迟执行层。

## 关键技术装置

- **Semantic Waypoint Packet**: `goal_type / target_pose / semantic_confidence / safety_budget / handoff_tag`
- **Imagined Goal Intermediate**: 在 search / long-horizon 阶段可用目标视频或短时视觉 rollout 做中介，但必须回写成 packet 可消费字段
- **Verifier-Gated Execution**: `Semantic Validity + Geometric Executability + Budget Compliance`
- **Fixed-Anchor Local Planner**: 在近场高速避障段优先采用固定 motion anchor / ranking 机制，减少 controller 侧抖动
- **Stage-Bounded Recovery**: search 阶段完整 `retry / repair / replan / escalate`，approach 以后逐步收紧
- **D01 Supervisor Interface**: 在需要时接入执行前 `rank_score / failure_state / route_action`

## 链接

- [[05_科研研究/D06_空中视觉语言导航/REPORT]] — 详细技术方案
- [[concepts/空中视觉语言导航]]
- [[concepts/VLA架构]]
- [[comparisons/端到端VLA_vs_层次化VLA]]
- [[comparisons/端到端空中VLA_vs_分层Explorer导航]]
- [[sources/FineCog-Nav_2604.16298]]
- [[sources/OnFly_2603.10682]]
- [[sources/source.2605.01477_Action_Agent]]
- [[sources/source.2026-05-06_2605.02301_SAGA_UAV_Autonomous_Navigation]]
- [[sources/UAV-Flow_2026|UAV-Flow Colosseo]]
- [[sources/ORTrack_2026-04-07|ORTrack (2504.09228)]]
- [[sources/AerialVLN_Survey_2604.07705]]
- [[sources/AerialVLA_2603.14363|AerialVLA (2603.14363)]]
