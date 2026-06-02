# D01 世界模型实验设计

> 最后更新：2026-04-18 R813
> 状态：E1 已立项，等待主人确认后执行

## E1. 部署前验收栈最小实验

### 目标
先不追“大而全世界模型”，而是验证 D01 是否能作为 **真机前部署验收栈** 稳定工作：
`Grounded tokenizer → evaluator → WAV verifier → F1/F2 分诊 → Dream2Fix-style recovery`

### 任务范围
- **任务**：短程接近-对位 + 末端轻接触前 smoke test
- **环境**：AirSim / UE5 可回放场景
- **对象**：局部目标点、简单障碍、固定目标物
- **为什么先做它**：把长程导航、复杂抓取、双动力学误差先拆开，只看“能否安全筛掉不该放行的动作，并在已知失败时给出恢复”

### 对照组
1. **B0 pass-only**：只有 evaluator 放行分数
2. **B1 pass + WAV**：加入 state plausibility / action reachability verifier
3. **B2 B1 + F1/F2 triage**：在危险预筛后继续区分已知失败与未知异常
4. **B3 B2 + R1 rule fallback**：已知失败后只允许规则回退
5. **B4 B2 + R3 Dream2Fix-style recovery**：已知失败后直接预测修正轨迹

### 关键指标
- ranking correlation（WM 评分 vs 仿真真实结果）
- danger-action 漏放率
- 误杀率
- anomaly recall / OOD 漏放率
- 已知失败恢复成功率
- 恢复后额外碰撞率
- 单次决策时延

### 验收门
- **G0**：ranking correlation 稳定为正，且波动可接受
- **G1**：B1 相比 B0 显著降低 danger-action 漏放率
- **G2**：B2 相比 B1 显著降低异常漏放率，且不过度升级已知失败
- **G3**：B4 相比 B3 在已知失败恢复率上有明确提升，且不明显增加额外碰撞

### 判停规则
- 若 B1 对 B0 没有预筛收益，暂停 recovery 线，先修接口层
- 若 B2 的误升级率过高，保留 pass+WAV，不进入 triage 常态化
- 若 B4 带来明显误恢复或额外碰撞，Dream2Fix recovery 降级为候选，不进入主线

## E1 输出物
- 一张 `B0~B4` 对照表
- 一组失败样例可视化（已知失败 / 未知异常 / 恢复成功 / 恢复失败）
- 一页 go / no-go 结论：D01 本阶段是否值得继续作为部署前验收栈推进

## E2. 分诊-恢复记账实验（R813 新增）

### 目标
不给 D01 的 recovery 线只留一个“恢复成功率”单指标，而是把 **恢复收益、异常漏放、人工接管负担** 一起记账，提前决定这条线有没有资格进论文主表。

### 对照组
1. **C0**：B2 `pass + WAV + F1/F2 triage`
2. **C1**：C0 + `R1 rule fallback`
3. **C2**：C0 + `R3 Dream2Fix-style recovery`
4. **C3**：C0 + `R1 + R3`（规则保底 + 学习式恢复）

### 核心指标
- **SRY**（Safe Recovery Yield）
- **AER**（Anomaly Escape Rate）
- **HHB**（Human Handoff Burden）
- **RDR**（Recovery Debt Ratio）
- **RCS**（Recovery Calibration Score）

### 关键问题
- 学习式恢复是否真的提高 `SRY`，还是只是把更多异常硬往下执行？
- `R1 规则回退` 和 `R3 反事实恢复器` 是替代关系，还是“规则保底 + 学习式精修”更稳？
- 对空中平台而言，哪一档方法能在不过度增加 `HHB` 的前提下压低 `AER`？

### 判停规则
- 若 C2 相对 C1 没有明确提升 `SRY`，则 Dream2Fix recovery 暂不升主线
- 若 C2/C3 的 `AER` 高于 C1，哪怕恢复率更高，也降级为候选
- 若 `HHB` 明显升高，则说明系统只是把复杂度转移给人工，不算主线收益

## E15. Refresh-Window Honesty Attribution Smoke Test（R20260522 新增）

### 目标
把 D01 最近几轮已经反复强调的 **refresh 变快 ≠ delayed-consumption 更诚实** 真正压成一组最小烟测，不再只在正文里做概念区分。这个实验只回答一个更硬的问题：**额外 refresh 预算带来的收益，到底主要落在 proposal 端、bind 端，还是 consume 端？**

### 对照组
1. **F0 single-release**：只在初次 release 时打一次分，不做 refresh
2. **F1 periodic refresh**：固定周期 refresh 后再下发 packet
3. **F2 event-triggered refresh**：只有遇到 stage drift / envelope drift / anchor drift 才 refresh
4. **F3 speculative async refresh**：参考 DexWorldModel/LeWorldModel 风格，把部分 refresh 计算前移并与执行重叠

### 最小日志 tuple
- `Δproposal`：refresh 后 planner-side ranking / screening 是否提升
- `Δbind`：refresh 后 controller bind honesty 是否提升
- `Δconsume`：refresh 后 true consume-time honesty 是否提升
- `Δaddr`：refresh 后 object/anchor/clause/thread identity 是否更稳
- `Δdecode`：refresh 后 latent-action decode honesty 是否更稳

可统一记为：
`ω_t = (Δproposal, Δbind, Δconsume, Δaddr, Δdecode)`

### 核心指标
- **PDS**（Proposal Density Support）：仅 proposal 侧受益的比例
- **BHR**（Bind-Honest Refresh gain）：仅 bind 侧受益的比例
- **CHR**（Consume-Honest Refresh gain）：真正落到 consume-time honesty 的净收益
- **ADR**（Address Drift after Refresh）：refresh 后仍发生 referent drift 的比例
- **DHLR**（Decode-Honesty Loss after Refresh）：refresh 后 decode-honest 崩掉的比例
- **RCL**（Refresh Compute Latency）：refresh 额外带来的时延开销

### 判线规则
- 若某 refresh 策略主要提升 `Δproposal`，但 `Δconsume ≈ 0`，则只能记为 **proposal-density support**，不得写成 handoff gain。
- 若 `Δbind > 0` 但 `Δconsume ≤ 0`，则冻结为 **bind-honest refresh support**。
- 只有当 `Δconsume / Δaddr / Δdecode` 同时改善时，才允许升级成 **refresh-enabled handoff gain**。
- 若 F3 虽降低 `RCL`，却恶化 `ADR` 或 `DHLR`，则 speculative refresh 只能作为系统技巧，不升主线。

### 当前预期结论
首轮更可能成立的是：**event-triggered refresh** 比固定周期 refresh 更诚实；而 **speculative async refresh** 更像 proposal/bind 侧增益，需要先证明自己没有把 delayed-consumption 问题藏起来，才配进入主标题。

## E15b. Semantic-Screening / Refresh-Density / Stale-Route Subtraction Smoke Test（R20260530 新增）

### 目标
把 D01 新近收束出的一个更危险混淆点单独压成烟测：**semantic latent 更强、refresh 更快、delayed semantic route 更稳**，并不自动等于 **packet contract 更强**。这一组实验专门检验：在扣除 `semantic ranking gain`、`refresh density gain`、`stale-route support` 之后，还剩下多少真实的 delayed-consumption 提升。

### 对照组
1. **S0 reconstruction latent + single-release**：重建型 latent，不做 refresh subtraction
2. **S1 semantic latent + single-release**：只看 semantic screening gain
3. **S2 semantic latent + periodic/event refresh**：叠加 refresh density gain
4. **S3 semantic latent + async refresh + stale-route audit**：完整做扣减审计

### 最小日志 tuple
- `Δsem-rank`：semantic latent 带来的 ranking / screening 提升
- `Δrefresh-density`：更快 refresh 带来的额外 proposal 机会提升
- `Δstale-route`：看起来更强的结果中，有多少仍可由 delayed semantic routing 解释
- `Δbind`：扣减后剩余的 bind-honest 提升
- `Δconsume`：扣减后剩余的 consume-honest 提升

可统一记为：
`ψ_t = (Δsem-rank, Δrefresh-density, Δstale-route, Δbind, Δconsume)`

### 核心指标
- **SRS**（Semantic Ranking Support）：仅由 semantic latent 提供的 proposal-side 增益
- **RDS**（Refresh Density Support）：仅由更快 refresh 提供的 proposal 密度增益
- **SRSR**（Stale-Route Support Residual）：扣减后仍可由 delayed semantic route 解释的剩余比例
- **BHR\***（Residual Bind-Honest gain）：扣掉前三项后剩余的 bind 提升
- **CHR\***（Residual Consume-Honest gain）：扣掉前三项后剩余的 consume 提升

### 判线规则
- 若 S1/S2 的主要收益只体现在 `Δsem-rank` 或 `Δrefresh-density`，则只能记为 **semantic-refresh support**。
- 若 async refresh 后 `Δbind > 0`，但扣掉 `Δstale-route` 后增益消失，则只能记为 **interface-side delayed-routing support**。
- 只有当 `CHR* > 0`，且不是由 semantic ranking 或 refresh density 借来的增益，才允许升级成 **packet-contract evidence**。
- 若 `SRSR` 长期偏高，说明当前实验更像在验证 delayed semantic-control interface，而不是 D01 自己的 delayed-consumption contract。

### 当前预期结论
更可能出现的诚实结论是：**semantic latent + fast refresh** 先稳定改善 proposal 侧筛选质量，但真正能穿过扣减审计、留下 `CHR*` 的方法会少得多；这正好能保护 D01 不把“更会选包”误写成“更会保包”。

## E13. 首轮主叙事冻结烟测（R862 新增）


### 目标
把 D01 现阶段已经出现的五种主叙事候选——`evaluator-first / triage-first / route-first / hover-recovery-first / interface-first`——放进同一张首轮判线表，不再靠直觉决定论文标题谁做主线。换句话说，本实验不再问“哪个模块看起来更酷”，而是直接问：**哪条叙事在首轮预算内带来最独占、最可部署、最能跨方向复用的净收益**。

### 叙事槽位
1. **N0 evaluator-first**：主收益来自 `rank_score / ranking correlation / danger-action filtering`
2. **N1 triage-first**：主收益来自 `F1/F2 known-failure vs anomaly` 分诊
3. **N2 route-first**：主收益来自 `route_action + stage-aware routing`，显著减少 `late stop / misroute`
4. **N3 hover-recovery-first**：主收益主要来自 `hover-bounded recovery`
5. **N4 interface-first**：主收益来自 D01→D06 的执行前 supervisor 接口，即同一预筛/路由接口可直接服务 packet 执行链

### 核心指标
- **CSG**（Core Safety Gain）：相对最弱基线减少的 danger-action 漏放、late stop、misroute 综合收益
- **NEX**（Narrative Exclusivity）：该收益是否只能由当前叙事解释，还是其他槽位也能轻松覆盖
- **CDU**（Cross-Direction Utility）：能否直接复用到 D06 / D07，而不只是 D01 自己闭环里成立
- **BGR**（Budget-to-Gain Ratio）：单位实验/工程预算换来的净收益是否足够高
- **RIF**（Risk Inflation）：该叙事引入的新风险是否在可控范围内，尤其关注 `AER / WRR / HHB / PSL`

### 判线规则
- 若 **N0/N1** 已拿到大部分 `CSG`，且 `N2/N3/N4` 的额外收益不独占，则论文主叙事优先冻结为 **evaluator-first + triage-first**，其余只做 supporting evidence。
- 若 **N2 route-first** 显著压低 `late stop / misroute`，且 `CDU` 高，说明 D01 更像 **stage-aware route supervisor**，可升主标题。
- 若 **N3 hover-recovery-first** 只有在停悬窗口带来局部收益，且 `RIF` 不够低，则明确降级为 **hover-bounded supporting evidence**，不争主标题。
- 若 **N4 interface-first** 在 D01→D06 接口烟测里同时改善 `DPR / WRR / PSL`，则可把 D01 主叙事冻结为 **interface-first execution supervisor**。
- 若任何叙事虽然提升局部指标，但 `BGR` 很差或 `RIF` 明显恶化，则不得升格为主线。

### 当前预期结论
首轮更值得竞争主标题的不是通用 recovery，而是 **stage-aware route supervisor** 或 **interface-first execution supervisor**；`hover-bounded recovery` 只有在出现低风险、跨阶段、独占性的净收益时，才有资格上升到主叙事。

## E14. D01→D06 packet 预筛接口烟测（R863 新增）

### 目标
把 D01 作为 D06 的 **执行前 pre-screen / route supervisor** 这条主线继续压成最小接口级烟测，不再泛谈“世界模型可做安全层”。这一轮只回答一个更硬的问题：**同一份 `Semantic Waypoint Packet` 在进入 D06 controller 前，D01 能否稳定给出比 `local-only` 更好的预筛、路由与停悬窗口补件判断**。

### 对照组
1. **X0 local-only**：D06 packet 直接走本地 verifier / controller，不接 D01
2. **X1 rank-score gate**：D01 只返回 `rank_score`，低分 packet 直接拦截
3. **X2 triage + route_action**：D01 返回 `rank_score + F1/F2 + route_action`
4. **X3 hover-bounded recovery**：在 X2 基础上，仅 `hover/search` 窗口允许 `packet repair / recovery_scope`

### 接口字段
- **D06 → D01**：`packet_id / stage_tag / semantic_waypoint_packet / planner_confidence / verifier_features`
- **D01 → D06**：`rank_score / F1-F2 / route_action / recovery_scope / risk_budget`

### 主指标
- **DPR**（Dangerous Pass Rate）：本应拦截却被放行的 packet 比例
- **Late Stop Rate**：本该前置阻断却拖到执行后期才停下的比例
- **Misroute Rate**：本该 `repair/replan/hover` 却继续执行或错误升级的比例
- **PRY**（Packet Repair Yield）：停悬窗口内 packet repair 真正带回的净收益
- **PSL**（Packet Screening Latency）：单次 packet 预筛时延

### 解释顺序（冻结）
1. `DPR`
2. `Late Stop Rate`
3. `Misroute Rate`
4. `PRY`
5. `PSL`

### 判线规则
- 若 **X1** 对 **X0** 不能明显降低 `DPR`，说明 D01 还不具备跨方向执行前预筛资格。
- 若 **X2** 相对 **X1** 不能明显降低 `Late Stop Rate / Misroute Rate`，则 D01 暂不升为 route supervisor，只保留 score gate。
- 若 **X3** 只提升 `PRY`，却不能同步改善前三项核心指标，则 `hover-bounded recovery` 明确降级为 supporting evidence。
- 若 `PSL` 过高，即便判断更准，也只能作为低频 gate 或离线筛查，不默认接在线链路。

### 当前预期结论
首轮若出现净收益，最可能成立的是 **rank-score gate → triage+route_action** 这条主线；`hover-bounded recovery` 更像停悬窗口内的补件证据，而不是 D01 的主标题。

## E7. 阶段感知恢复部署窗口烟测（R820/R830 整理合并）

### 目标
把 D01 的 recovery 从“统一在线开关”进一步压成 **phase-bounded recovery**，直接验证它到底只适合 `停悬/回锚`，还是能安全进入 `运动中执行`。

### 对照组
1. **P0**：offline recommendation only（只做离线建议）
2. **P1**：hover-gated recovery（仅在停悬/回锚阶段允许 `R3 recovery`）
3. **P2**：approach-window recovery（只在低速接近窗口允许短窗 recovery）
4. **P3**：in-motion recovery（运动中直接允许 recovery，作为高风险对照）

### 核心指标
- **HSR**（Hover-stage Success Recovery）
- **MSR**（Motion-stage Success Recovery）
- **AER**（Anomaly Escape Rate）
- **Jerk/碰撞超限率**
- **Gate-to-act latency**（从分诊到恢复动作发出的时延）

### 关键问题
- Dream2Fix-style recovery 的真实甜区是不是 `停悬/回锚阶段`，而不是运动中在线接管？
- 若 `P1 > P0` 但 `P3` 明显恶化，D01 就该明确把 recovery 写成 **阶段性恢复器**。
- `P2` 是否能成为折中位，即在低速接近段保留有限 recovery 收益，但不付出 `P3` 那样的安全代价？

### 判停规则
- 若 `P1` 都不能稳定优于 `P0`，则 R3 recovery 不升主线
- 若 `P3` 的 `AER` 或 jerk/碰撞超限率明显高于 `P1/P2`，则在线 recovery 只保留到停悬或低速窗口
- 若 `P2` 与 `P1` 接近，则论文主线优先写 **停悬/回锚后恢复**，不强求运动中恢复

## E8. 阶段感知路由烟测（R820 新增）

### 目标
验证 D01 新补的 `rank_score + failure_state + route_action` 三元输出，能不能真正把 **WorldEval evaluator / F1-F2 分诊 / Dream2Fix recovery** 收成一条统一决策链，而不是三套彼此割裂的模块。

### 对照组
1. **R0 score-only**：只有 `pass score`，不输出恢复路由
2. **R1 score + triage**：输出 `pass / F1 / F2`，但无阶段感知路由
3. **R2 stage-aware routing**：输出 `rank_score + failure_state + route_action`
4. **R3 aggressive routing**：在 P2/P3 也尽量放开 recovery，作为风险对照

### 核心指标
- **Route Precision**：推荐的 `route_action` 与最终最优处置是否一致
- **Late Stop Rate**：本应更早 `hard stop` 却被拖到后续阶段才拦下的比例
- **Recovery Misroute Rate**：本该 `fallback/hard stop` 却被错误送入 `gated_recovery` 的比例
- **Stage Transfer Delay**：从发现问题到进入正确处置阶段的额外时延

### 关键问题
- 单有 `pass score` 是否会把大量“该停悬后再处理”的情况误判成还能继续飞？
- `route_action` 能否显著降低 `Late Stop Rate` 与 `Recovery Misroute Rate`？
- 对空中平台而言，阶段感知路由是不是比“更强 recovery 模块”本身更值钱？

### 判停规则
- 若 R2 相比 R1 没有显著降低 `Late Stop Rate`，则阶段感知路由暂不升主线
- 若 R3 的 `Recovery Misroute Rate` 明显恶化，则明确禁止在 P3 默认放开 recovery
- 若 `Stage Transfer Delay` 过高，则 route_action 只保留给离线评测，不进入在线控制

## E6. D01→D06/D07 路由接口烟测（R824 新增）

### 目标
验证 D01 的 `route_action` 是否真能作为 **跨方向统一安全路由接口**，而不是只在 D01 自己的评测栈里自洽。

### 对照组
1. **X0 local-only**：D06/D07 各自用本地方向里的 fallback 规则，不接 D01 路由
2. **X1 D01 route supervisor**：统一接 `rank_score + failure_state + route_action + stage_tag`
3. **X2 aggressive cross-use**：在 D06/D07 中尽量放开 `gated_recovery`，作为风险对照

### 观察任务
- **D06 侧**：planner packet 下发、packet repair、local replan、hover stop
- **D07 侧**：policy rollout、shield fallback、residual correction、emergency stop

### 核心指标
- **Cross-Task Route Precision**：同一接口在 D06/D07 上是否都能把动作送到正确处置分支
- **Fallback Consistency**：相近风险等级下，两条链是否给出一致保守度，而不是一条过激一条过松
- **Late Stop Rate**：应更早停下却拖到下游才停的比例
- **Interface Overhead**：接 D01 路由后新增的决策时延

### 关键问题
- D01 的 `route_action` 能否减少 D06/D07 各自重复发明 verifier/shield 规则？
- `gated_recovery` 在 D06 的低速导航窗口可能成立，但在 D07 的高接触不确定区间是否应默认更保守？
- 若统一接口成立，D01 就能从“单方向评测器”升级成跨方向 **route supervisor**。

### 判停规则
- 若 X1 相比 X0 没有明显降低 `Late Stop Rate`，则 4.12 只保留为概念接口，不升为主线
- 若 X2 在任一方向明显放大误恢复或误放行，则跨方向接口默认禁用激进 recovery
- 若 `Interface Overhead` 超过短程控制预算，则 D01 路由只保留给离线评测或低速阶段

## E9. D01→D06 packet 预筛接口烟测（R844/R849 收束版）

### 目标
验证 D01 作为 **D06 planner packet 进入执行链前的统一 supervisor** 是否真的值钱：不是替 D06 做规划，而是稳定完成 `预筛 → 分诊 → 路由 → 限定恢复`，并用统一首轮规则直接冻结 D01 主叙事。

### 对照组
1. **P0 local-only**：D06 仅用本地 verifier / fallback 规则
2. **P1 rank-score gate**：D06 接入 D01 的 `rank_score`
3. **P2 rank + triage + route_action**：接入 `rank_score + F1/F2 + route_action`
4. **P3 P2 + hover-bounded recovery**：仅在 `hover / re-anchor` 阶段允许 `recovery_scope=hover_only`

### 观察阶段
- `search`
- `hover`
- `re-anchor`
- `approach`
- `inspect`

### 核心指标（固定优先级）
1. **danger-action 漏放率**
2. **late stop rate**
3. **misroute rate**（本该 fallback / human-review 却继续执行）
4. **packet repair 成功率**
5. **hover 阶段恢复成功率**
6. **新增执行时延**

### 首轮主叙事冻结规则（R849 新增）
- 若 **P1** 相比 **P0** 已显著降低 `danger-action 漏放率`，说明 D01 至少具备 evaluator-first 价值。
- 若 **P2** 相比 **P1** 继续显著降低 `late stop / misroute`，则 D01 主叙事默认冻结为 **pre-execution route supervisor**。
- 若 **P3** 只提升 `packet repair 成功率` 或 `hover 阶段恢复成功率`，但对前三项核心指标净收益不足，则 recovery 只保留为 **阶段性补件 / supporting evidence**，不得抢主标题。
- 只有当 **P3** 在不明显恶化时延的前提下，同时改善前三项核心指标中的至少两项，recovery 才允许进入下一轮主线讨论。

### 判停规则
- 若 P1 对 P0 几乎不降 danger-action 漏放率，D01 暂不宣传跨方向 packet 预筛价值。
- 若 P2 对 P1 不能明显降低 late stop / misroute，说明 route supervisor 还不值得抢主叙事。
- 若 P3 的净收益只体现在 `hover / re-anchor`，则 recovery 明确保留为 **hover-bounded mechanism**，不扩到更激进阶段。
- 若 P3 带来额外时延却不改善 repair / recovery 成功率，则 recovery 不进入 D06 首轮接口方案。

## E7. 阶段感知恢复部署窗口烟测（R820/R830 整理合并）- **对比**：按首轮结果分别统计 `evaluator+verifier`、`triage+route supervisor`、`hover-bounded recovery`、`D01→D06 interface supervisor` 四条子线的净收益与预算占用
- **场景**：复用 E1/E2/E6/E8 的统一日志，不新增新环境；目标是做主叙事冻结，不是再刷成功率
- **主指标**：Net Narrative Gain, Budget Share, Human Burden, Cross-direction Reuse Value, Risk Inflation
- **判据**：
  - 若 `evaluator+verifier` 收益最高且最稳，则 D01 主叙事固定为 **deployment-time evaluator**
  - 若 `triage+route supervisor` 对 late stop / misroute 改善最明显，则固定为 **stage-aware supervisor**
  - 若 recovery 只在停悬阶段收益稳定，则固定为 **phase-bounded recovery**
  - 若 D01→D06 复用价值最高，则主叙事转向 **interface-first execution supervisor**
- **失败先查**：先确认是不是同一收益被多条子线重复记账；若重复严重，优先合并叙事而不是并列写贡献
- **备注**：该实验直接服务 R839，强制 D01 首轮后只保留一条论文主叙事，避免报告继续发散

### 对照输入
- **Z0 evaluator-first**：B1/B2 结果最佳时采用
- **Z1 triage-first**：F1/F2 分诊收益最稳时采用
- **Z2 recovery-first**：Y3 hover-bounded recovery 成立时采用
- **Z3 route-first**：route_action 在跨方向任务中收益最稳时采用
- **Z4 interface-first**：Grounded tokenizer / geometry backbone 增益最大时采用

### 决策指标
- 主线对应指标提升幅度是否 **稳定且可复现**
- 其他路线是否只提供边际增益，适合降为 supporting evidence
- 是否与 D06 当前真实需求直接对齐（预筛 / 分诊 / 阶段化处置）
- 是否需要额外高风险在线闭环才成立

### 冻结规则
- 若 `AER` 或 `RCS` 不稳，**Z2 recovery-first** 自动失去主叙事资格
- 若 `route_action` 只在 D01 内自洽、不具跨方向收益，**Z3** 降级
- 若接口层 / 几何主干解释了大部分收益，**Z4** 优先级高于 recovery 线
- 最终只允许保留 1 个 `Z*` 作为论文摘要与标题主线

### 输出物
- 一张“主叙事选择表”
- 一页 supporting evidence 清单
- 一页冻结清单（明确哪些线本轮不再追加实验预算）

## E11. D01→D06 最小接口烟测（R834 新增）

### 目标
验证 D01 对龙虾/D06 最现实的价值，是不是 **执行前预筛 + 阶段化处置 supervisor**，而不是替 D06 planner 做重规划。

### 对照组
1. **L0 D06 local-only**：只用 D06 自己的 packet 规则
2. **L1 + rank_score**：加入 D01 预筛分数
3. **L2 + failure_state**：再加入 F1/F2 分诊
4. **L3 + route_action**：统一 `continue / hover / fallback / human review`
5. **L4 + hover-bounded recovery**：只在停悬窗口允许小范围修补

### 核心指标
- packet 危险放行率
- hover stop 触发是否更及时
- recovery misroute rate
- planner packet 被错误过度拦截的比例
- 接口额外时延

### 判停规则
- 若 L3 相比 L2 没有显著降低误路由或晚停，`route_action` 暂不升跨方向主线
- 若 L4 只带来边际收益却抬高误放行或时延，D01 对 D06 仅保留 `rank_score + failure_state`
- 若 L1/L2 已覆盖大部分收益，说明当前最值钱的是预筛与分诊，而非 recovery

### 对照维度
1. **V线**：`evaluator + WAV + F1/F2 triage`
2. **R线**：`stage-aware route_action`
3. **C线**：`Dream2Fix-style recovery`

### 核心指标
- **danger-action 漏放率**
- **Late Stop Rate**
- **Route Precision**
- **SRY / AER / RCS**
- **单位收益对应的额外预算消耗**（GPU小时 / 标注 / 人工确认）

### 判线规则
- 若 verifier/triage 还没稳定压低漏放率 → **冻结 C线**，预算先回 V线
- 若 `Route Precision↑` 且 `Late Stop Rate↓`，但 recovery 收益有限 → **冻结 C线扩展**，主线转 R线
- 若 recovery 只在 `P1 hover` 成立 → **冻结 P2/P3**，保留 hover-bounded 证据包
- 若 `AER` 或 `RCS` 长期不过线 → 自动恢复整体降级为 recommendation-only
- 任何时刻只允许 **一条主线** 占主实验槽位，其余降为对照
5. **Y4 low-speed window online**：仅在低速接近窗口允许 `R3`
6. **Y5 unrestricted online**：运动中也允许 `R3`，作为高风险反例

### 统一记账指标
- **SRY**（Safe Recovery Yield）
- **AER**（Anomaly Escape Rate）
- **HHB**（Human Handoff Burden）
- **RDR**（Recovery Debt Ratio）
- **RCS**（Recovery Calibration Score）

### 首轮读数判线
- 若 **Y2/Y3** 不能稳定优于 **Y0/Y1** 的 `SRY`，则 Dream2Fix recovery 不升主线
- 若 `SRY` 上升但 `AER` 或 `HHB` 同时明显恶化，则 recovery 仅保留 recommendation-only
- 若 `Y3` 成立而 `Y5` 明显恶化，则正式把 D01 主叙事写成 **phase-bounded recovery**
- 若 `RCS` 长期失准，则 recovery 禁止默认自动执行
- 若 `RDR` 明显高于规则回退，则 recovery 仅保留给高价值任务或停悬阶段

### 输出物
- 一张 `Y0~Y5` 统一记账对照表
- 一页 go / no-go 结论：`offline recommendation` / `hover-only` / `low-speed window` / `not worth deploying`

## E8. 执行阶段恢复部署判线烟测（R830 新增）

### 目标
把 E7 的统一记账结果直接压成 **部署结论**，不再停在“哪组指标更好”，而是明确回答 recovery 到底该停留在 `offline recommendation`、`hover-bounded online`、`low-speed window online`，还是根本不该部署。

### 输入来源
- 直接复用 `Y0~Y5` 的实验结果
- 统一使用 `SRY / AER / HHB / RDR / RCS`
- 按 `P1 停悬/回锚`、`P2 低速接近`、`P3 运动中执行` 三段分别判线

### 判线表
1. **Z0 不部署**：`SRY` 无明显提升，或 `RDR` 明显偏高
2. **Z1 仅离线建议**：`SRY↑` 但 `AER` 明显恶化
3. **Z2 人工确认后执行**：`SRY↑`、`AER` 稳定，但 `HHB` 很高或 `RCS` 失准
4. **Z3 仅停悬窗口部署**：`Y3 >> Y2`，且 `AER/HHB/RDR/RCS` 都可控
5. **Z4 停悬+低速窗口部署**：`Y4 ≈ Y3` 且未带来明显额外风险
6. **Z5 禁止 unrestricted online**：`Y5` 才有收益但 `AER` 或 `RCS` 波动明显

### 输出物
- 一张 `Y0~Y5 → Z0~Z5` 的部署映射表
- 一页 go / no-go 结论：`not worth deploying / recommendation-only / human-confirmed / hover-only / hover+low-speed`
- 一句论文级主结论：D01 recovery 的真实部署边界是什么

## E12. D01→D06 接口主导权判线烟测（R850 新增）

### 目标
把 D01 与 D06 的边界再压硬一点：首轮不再只问 D01 能不能当 packet supervisor，而要直接回答 **收益主要来自 D01 的执行前预筛，还是来自 D06 自己的 packet schema / verifier 修补**，避免跨方向接口把功劳和锅继续混在一起。

### 对照组
1. **H0 D06-local**：仅修 D06 本地 `packet schema + verifier`，不接 D01 supervisor
2. **H1 D01-pre-screen**：在 H0 基础上接入 D01 `rank_score + F1/F2 + route_action`
3. **H2 D01-pre-screen + hover-only recovery**：H1 再加 `recovery_scope=hover_only`
4. **H3 aggressive-cross-use**：把恢复放宽到 `approach`，作为高风险反例

### 核心指标
- **Supervisor Gain Ratio (SGR)**：H1/H2 相对 H0 的净收益占比
- **Schema Defect Share (SDS)**：失败中可直接归因到 `target_pose / yaw_hint / altitude_band / handoff_tag` 缺陷的比例
- **Cross-Boundary Misattribution (CBM)**：本属 D06 接口问题却被误记成 D01 路由收益/失败的比例
- **Hover-only Net Benefit (HNB)**：`hover / re-anchor` 阶段限定恢复的净收益
- **Approach Risk Spillover (ARS)**：把恢复扩到 `approach` 后新增的误路由/额外风险

### 关键问题
- 若 H0 通过单修 packet schema 就已明显降低 late stop / misroute，是否说明首轮主收益仍在 D06，而不是 D01？
- 若 H1 明显优于 H0，D01 才配被写成 **pre-execution supervisor**；否则应退回 supporting interface。
- 若 H2 的收益集中在 `hover / re-anchor` 而 H3 明显恶化，是否应把跨方向恢复正式冻结为 **hover-only**？

### 判停规则
- 若 **SDS 高而 SGR 低**，优先判定为 D06 packet/interface 问题，暂停夸大 D01 价值。
- 若 **H1 相对 H0 增益不稳定**，D01 仅保留 `rank_score` 观测位，不升主叙事。
- 若 **HNB 为正而 ARS 明显恶化**，恢复边界正式冻结为 `hover-only`，不再讨论 `approach` 扩张。
- 若 **CBM 持续偏高**，先补统一日志标签与责任归因表，再继续跨方向接口实验。

### 输出物
- 一张 `H0~H3` 的主导权判线表
- 一页“D01 收益 / D06 接口收益 / 边界混淆”责任拆账表
- 一句主结论：当前跨方向主收益究竟在 supervisor，还是在 packet schema 修补

### 判停规则
- 只要 `AER` 或 `RCS` 明显恶化，就禁止升到默认在线 recovery
- 若 `Y3` 成立但 `Y4/Y5` 不成立，主叙事固定为 `phase-bounded / hover-bounded recovery`
- 若 `Z2` 长期成立而进不到 `Z3`，则 recovery 仅保留作辅助系统，不占论文主贡献槽位

## E13. 首轮主叙事冻结烟测（R861 新增）

### 目标
把 D01 当前已经铺开的 `evaluator / verifier / triage / route supervisor / hover-bounded recovery / cross-direction interface` 六条线，进一步压成 **首轮结果一出来就能冻结论文主标题** 的单一判线协议，避免继续在 REPORT 里并列扩张。

### 对照叙事槽位
1. **N1 evaluator-first**：主收益来自 `rank_score + WAV/self-check`
2. **N2 triage-first**：主收益来自 `F1/F2 已知失败 vs 异常` 分诊
3. **N3 route-first**：主收益来自 `route_action` 降低 late stop / misroute
4. **N4 hover-recovery-first**：主收益来自 `hover-bounded recovery`
5. **N5 interface-first**：主收益来自 `D01→D06 packet pre-screen supervisor`

### 统一冻结指标
- **Core Safety Gain (CSG)**：`danger-action 漏放率 + late stop rate + misroute rate` 的净改善
- **Narrative Exclusivity (NE)**：该叙事解释的独占收益占比，避免多条线重复记账
- **Cross-Direction Utility (CDU)**：是否能稳定复用到 D06，而不是只在 D01 内自洽
- **Budget-to-Gain Ratio (BGR)**：单位收益所需额外预算/链路复杂度
- **Risk Inflation (RI)**：是否靠抬高 `AER / HHB / RCS / latency` 换取表面增益

### 冻结规则
- 若 **N1/N2** 已解释大部分 `CSG`，则 **N4** 自动降为 supporting evidence，不得抢主标题。
- 若 **N3** 对 `late stop / misroute` 的净改善最稳定，且 `RI` 可控，则 D01 主叙事冻结为 **stage-aware route supervisor**。
- 若 **N5** 的 `CDU` 最高，且收益不主要来自 D06 自己修 packet schema，则主叙事冻结为 **interface-first execution supervisor**。
- 若 **N4** 只在 `hover / re-anchor` 有稳定收益，则只能冻结为 **phase-bounded recovery supporting line**，不能升为摘要主线。
- 任意叙事只要 `RI` 明显上升，立即失去主叙事资格。

### 输出物
- 一张 `N1~N5` 主叙事选择表
- 一页 supporting evidence 清单（明确谁降级）
- 一句冻结结论：D01 首轮之后到底该把自己写成 evaluator、route supervisor，还是 interface-first supervisor

## 下轮可接续
- 若 E1 通过：进入 `video-WM vs geometry-WM` 的短程对位对照
- 若 E2 通过：把 `SRY/AER/HHB` 固化为 D01 论文主表指标
- 若 E3 通过：把 `RG0~RG3` 固化为 recovery 准入协议
- 若 E4 通过：把 `phase-bounded recovery` 固化为 D01 主叙事的一部分
- 若 E5 通过：把 `route_action` 固化为 D01 对 D06/D07 的统一接口输出
- 若 E6 通过：把 D01 升级为跨方向 `route supervisor`，并回写 D06/D07 的实验接口
- 若 E7 通过：把 D01 的 recovery 正式收束为“值不值得部署 + 该部署在哪个阶段”的主结论
- 若 E13 通过：强制只保留 1 条论文主叙事，其余全部降为对照或 supporting evidence
- 若 E1 未通过：回到 C6 接口层，只做 tokenizer + evaluator 稳定性修正

