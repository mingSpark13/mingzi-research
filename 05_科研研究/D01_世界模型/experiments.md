# D01 世界模型实验设计

> 最后更新：2026-06-16
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

## E16. Temporal-Context / Contact-Semantics Packet Audit（R20260613 新增）

### 目标
把 D01 最近在 `PAPER.md 3.36` 冻结下来的新边界真正落到可观测实验日志：**包在 delayed consume 前，不仅要保 object/clause/thread identity，还要保 temporal episode context 与 contact-intent semantics。** 这一组实验专门回答：MemoryVLA++ 式 memory gain 与 iMaC 式 contact-aware action gain，是否真的穿过 bind/consume 审计，而不是只提升 proposal 或 bind 侧的好看数字。

### 对照组
1. **T0 base packet**：无显式 memory、无 contact-aware action token
2. **T1 +Memory**：加入 episodic retrieval + imagined-future context，但动作接口不变
3. **T2 +Contact**：加入 motion/contact-aware packetization，但不加 memory retrieval
4. **T3 +Memory+Contact**：同时保留 temporal context 与 contact semantics

### 最小日志 tuple
- `c_episode`：emit/refresh/bind/consume 时是否仍指向同一 episode context
- `c_future`：imagined near-future 是否仍与 remaining-plan 对齐
- `a_contact`：packet 是否仍保留相同 contact/motion semantics
- `h_bind`：bind-honest 是否成立
- `h_consume`：consume-honest 是否成立

可统一记为：
`τ_t = (c_episode, c_future, a_contact, h_bind, h_consume)`

### 核心指标
- **TCPR**（Temporal-Context Preservation Rate）：temporal episode context 保真的比例
- **CSPR**（Contact-Semantics Preservation Rate）：contact-intent semantics 保真的比例
- **HCMR**（History-Context Mis-Retrieve Rate）：历史检索命中错上下文的比例
- **DHLR**（Decode-Honesty Loss after Refresh）：refresh 后 contact/action 语义在 decode 端丢失的比例
- **PHC**（Packet Handoff Continuity）：包在 handoff 链路上的 continuity
- **CTTPR**（Consumption-Time Thread Preservation Rate）：最终 consume 时 thread 仍诚实保留的比例
- **Δplan**：consume 后 remaining-plan compatibility 的净变化

### 判线规则
- 若 `T1` 主要提升 `TCPR`、降低 `HCMR`，但 `CSPR / DHLR / CTTPR` 基本不动，则冻结为 **temporal-context support**。
- 若 `T2` 主要提升 `CSPR` 或降低 `DHLR`，但 `TCPR / HCMR / CTTPR` 基本不动，则冻结为 **contact-semantics support**。
- 若 `T3` 只在 `bind` 侧更稳，而 `consume` 侧仍掉线，则最多记为 **hover-window combined support** 或 **bounded-delay support**。
- 只有当 `T3` 在 `PHC + CTTPR + bounded Δplan` 上同时优于 `T1/T2`，并且提升不只是来自单边 memory/contact gain，才允许升级成 **temporal-context-and-contact-semantics preserving packet-contract support**。

### 当前预期结论
更诚实的首轮结果大概率是：`+Memory` 先稳住 history/episode continuity，`+Contact` 先稳住 consume-time local semantics，而真正能穿过 delayed-consumption 审计的会是两者结合后的少数 stress cells。这样能保护 D01 不把“记得更久”或“动作更像接触语义”直接冒领成完整 deployment-time supervisor 进步。

## E16b. Combined-Gain Promotion Gate for `+Memory+Contact`（R20260616 新增）

### 目标
避免把 `+Memory` 与 `+Contact` 两条单因子收益简单相加后，误写成已经解决 delayed-consumption packet contract。这个实验把 `T3=+Memory+Contact` 的 reviewer-facing 升级门槛写死：**只有组合残差穿过 consume-time stress cells，才配升格成 joint packet-contract support。**

### 最小日志 tuple
- `TCPR`
- `CSPR`
- `HCMR`
- `DHLR`
- `PHC`
- `CTTPR`
- `Δplan`
- `Γ^{mc}`

其中

\[
\Gamma_t^{mc} = G_t^{(T3)} - \max\big(G_t^{(T1)}, G_t^{(T2)}\big)
\]

用于表示 `+Memory+Contact` 相对单边最强因子的**真实组合残差**。

### 判线规则
- 若 `T3` 只是同时提升 `TCPR` 与 `CSPR`，但在 `W2/B2` 仍出现 `CTTPR \le 0` 或明显负的 `Δplan`，则冻结为 **combined support under bounded delay**。
- 只有当 `Γ^{mc} > 0`、`PHC` 在 `W2/B1` 仍为正、且 `CTTPR` 在 `W2/B2` 不翻负时，才允许升级成 **temporal-context-and-contact-semantics preserving delayed-consumption support**。
- reviewer 默认只看 `W2/B1` 与 `W2/B2` 两类 hard cells，不允许用 easy bind-time cell 的平均值冲淡 consume-time 失真。

### 当前预期结论
更可能的诚实结果是：组合条件先在 bounded-delay 场景站稳，而真正能穿过 `W2/B2` consume-time hard cell 的只会是少数配置。这样能保护 D01 不把“两个 support 一起开”直接写成完整 handoff gain。

## E17. Object-Centric Planner Support versus Packet-Contract Residual（R20260616 新增）

### 目标
把今日新增本地锚点 **COMET (2606.14418)** 吸收到 D01 的实验审计里，但保持它只作为 **object-centric causal planning support family**，不让“更会在对象槽上做 MCTS / causal attention”自动冒领成 deployment-time packet-contract 进步。

### 对照组
1. **O0 monolithic latent planner**：单块 latent，无对象槽
2. **O1 object-centric slots without causal fusion**：有对象槽，但动作-对象绑定弱
3. **O2 object-centric causal planner**：COMET 式 action-slot fusion + object-causal attention
4. **O3 O2 + packet audit**：在 O2 上继续做 delayed-consumption bind/consume 审计

### 最小日志 tuple
- `OAR`：object-attention relevance
- `CPS`：causal-planning support
- `IAS`：identity-address stability（emit→refresh→bind→consume 是否仍是同一对象/锚点/子句）
- `BHR^{obj}`：扣掉 object-centric planning support 后剩余的 bind-honest 增益
- `CHR^{obj}`：扣掉 object-centric planning support 后剩余的 consume-honest 增益

可统一记为：
`Ω_t^{obj} = (OAR, CPS, IAS, BHR^{obj}, CHR^{obj})`

### 判线规则
- 若 `O2` 主要提升 candidate ranking、对象消歧或早期 sample efficiency，但 `IAS / CHR^{obj}` 弱，则冻结为 **object-centric proposal support**。
- 若 `IAS` 在 bind 前稳定、但 consume 时 referent 或 clause 漂移，则冻结为 **address-stable bind support**。
- 只有当 `CHR^{obj}` 在扣减 object-centric planning support 后仍为正，才允许升级成 **object-aware packet-contract residual**。
- reviewer-facing 默认先看 proposal gain，再看 `IAS`，最后才看 `CHR^{obj}`；不允许直接把对象级规划收益写成 full handoff gain。

### 当前预期结论
更诚实的首轮结果大概率是：COMET 先显著提升 **proposal-side object disambiguation** 与早期规划效率，但只有少数配置会把这部分增益真正带过 delayed-consumption 审计。这正好让 D01 把 **object-centric planner support** 与 **packet-contract residual** 分开记账。

## E18. WEAVER-Style Test-Time Planner Support versus Packet-Contract Residual（R20260618 新增）

### 目标
把今日新增本地锚点 **WEAVER (2606.13672)** 吸收到 D01 的实验审计里，但保持它只作为 **test-time planner support family**：multi-view world model + reward prediction + flow matching + 评估/改进/规划三路打通，并不天然冒领成 deployment-time packet-contract 进步。

### 对照组
1. **T0 single-view latent WM**：单视角 latent，无 reward prediction，无 test-time planning
2. **T1 multi-view latent WM**：多视角 latent，训练目标同 T0
3. **T2 T1 + reward prediction**：WEAVER 式 latent + reward 联合预测
4. **T3 T2 + test-time planning**：WEAVER 完整版本，含 flow-matching policy improvement + test-time MCTS/planning
5. **T4 T3 + packet audit**：在 T3 之上继续做 delayed-consumption bind/consume 审计

### 最小日志 tuple
- `PMR`：planner-match relevance（候选 rollouts 与 same-cycle planner 的重合度）
- `TPL`：test-time planning lift（成功率 × 延迟综合指标）
- `PGS`：same-cycle proposal gain
- `BHR^{ttp}`：扣掉 test-time planner support 后剩余的 bind-honest 增益
- `CHR^{ttp}`：扣掉 test-time planner support 后剩余的 consume-honest 增益

可统一记为：
`Υ_t^{ttp} = (PMR, TPL, PGS, BHR^{ttp}, CHR^{ttp})`

### 判线规则
- 若 `T3` 主要提升 `PMR` 或 `TPL`，则冻结为 **test-time planner support**。
- 若 `PGS` 与 `BHR^{ttp}` 均为正、但 `CHR^{ttp}` 在 `W2/B1-B2` 翻负，则冻结为 **same-cycle bind-stable planner support**。
- 只有当 `CHR^{ttp}` 在 consume-time stress cells 仍为正、且 `CTTPR` 不退化时，才允许升级成 **test-time-planner-subtracted packet-contract residual**。
- reviewer-facing 默认先看 `PMR/TPL`（planner-side 解释力），再看 `BHR^{ttp}`，最后才看 `CHR^{ttp}`；不允许把 test-time planning 的胜利直接写成 full handoff gain。

### 当前预期结论
更可能的诚实结果是：WEAVER 先显著提升 **planner-match relevance** 与 **test-time planning lift**，但只有少数配置会把这部分 planner-side 增益真正带过 delayed-consumption 审计。这正好让 D01 把 **test-time planner support** 与 **packet-contract residual** 分开记账，避免被“同 cycle 内 test-time planning 跑得更好”误读成 deployment-time supervisor 也更强。

## E19. RepWAM-Style Shared Visual-Action Tokenizer as Representation-Alignment Support（R20260618 新增）

### 目标
把今日新增本地锚点 **RepWAM (2606.13674)** 吸收到 D01 的实验审计里，但保持它只作为 **representation-alignment support family**：shared semantic visual-action tokenizer + 对齐潜空间动作，并天然冒领成 deployment-time packet-contract 进步。

### 对照组
1. **R0 reconstruction-oriented WAM tokenizer**：传统面向像素重建的 tokenizer
2. **R1 semantic visual tokenizer**：用 VFM 表征对齐的 visual tokenizer，但 latent action 仍独立
3. **R2 R1 + latent action alignment**：RepWAM 完整版本，含 shared visual-action latent action
4. **R3 R2 + packet audit**：在 R2 之上继续做 delayed-consumption bind/consume 审计

### 最小日志 tuple
- `VAA`：visual-action alignment（tokenizer 潜空间中视觉与动作的对齐质量）
- `AAS`：latent action abstraction quality
- `AGP`：address-grounding preservation（emit/refresh/bind/consume 是否仍是同一对象/锚点/子句）
- `BHR^{ras}`：扣掉 representation-alignment support 后剩余的 bind-honest 增益
- `CHR^{ras}`：扣掉 representation-alignment support 后剩余的 consume-honest 增益

可统一记为：
`Φ_t^{ras} = (VAA, AAS, AGP, BHR^{ras}, CHR^{ras})`

### 判线规则
- 若 `R2` 主要提升 `VAA` 与 `AAS`、但 `AGP` 在 refresh 后漂移，则冻结为 **tokenizer-side representation support**。
- 若 `AGP` 在 bind 前稳定、但 `CHR^{ras}` 在 consume-time stress cells 翻负，则冻结为 **address-stable representation bind support**。
- 只有当 `AGP` 在 emit/refresh/bind/consume 全程稳定、且 `CHR^{ras}` 在 consume-time stress cells 仍为正时，才允许升级成 **representation-subtracted packet-contract residual**。
- reviewer-facing 默认先看 `VAA/AAS`（representation-side 解释力），再看 `AGP`，最后才看 `CHR^{ras}`；不允许把 tokenizer 升级的胜利直接写成 full handoff gain。

### 当前预期结论
更可能的诚实结果是：RepWAM 先显著提升 **visual-action alignment** 与 **latent action abstraction**，但只有少数配置会把这部分 representation-side 增益真正带过 delayed-consumption 审计，且 `AGP` 稳定性是关键瓶颈。这正好让 D01 把 **representation-alignment support** 与 **packet-contract residual** 分开记账，避免被“tokenizer 语义对齐”误读成 deployment-time supervisor 也更强。

## E20. Persistent Task Simulator with Cross-Episode Memory as Refresh-Stable Latent Support（R20260620 新增）

### 目标
把今日扫描本地新增锚点 **Mem-World (2606.18960)** 吸收进 D01 的实验审计，但保持它只作为 **persistent task simulator support family**：long-horizon memory token + 跨 episode reset/replay 协议，并天然冒领成 deployment-time packet-contract 进步。重点是验证 Mem-World 风格的长时程 coherent rollouts 是否真的能在 `W2/B1-B2` consume-time stress cells 中保持 consume-honest，还是只能停留在 planner-side 或 refresh-side 增益。

### 对照组
1. **M0 observation-only action-conditioned world model**：标准 ACWM，无 memory 模块
2. **M1 frame-stacking baseline**：naive 帧堆叠历史观测，不做 memory 压缩
3. **M2 Mem-World 完整版本**：long-horizon memory token + 当前视觉 token 联合预测未来帧
4. **M3 M2 + packet audit**：在 M2 之上继续做 delayed-consumption bind/consume 审计，跨 episode reset 强制 vs 自然触发对照

### 最小日志 tuple
- `mem-token`：memory token 自身的压缩质量、跨 refresh 一致性、drift 曲线
- `long-horizon`：memory-conditioned 未来是否仍保持 multi-step coherent
- `consume-honest`：D01 packet-contract 残留指标
- `address-stable`：memory token 在跨 episode reset 后是否仍指向同一对象 / waypoint / 子句
- `reset-protocol`：跨 episode reset 是显式触发（训练侧）还是隐式触发（部署侧）
- `sim2real`：persistent simulator 跨域是否需要 retraining

可统一记为：
`Μ_t = (mem-token, long-horizon, consume-honest, address-stable, reset-protocol, sim2real)`

### 判线规则
- 若 `M2` 主要提升 `mem-token` 与 `long-horizon`、但 `consume-honest` 在 delayed uptake 下塌缩，则冻结为 **persistent simulator representation support**。
- 若 `consume-honest` 仅在跨 episode `reset-protocol` 与 refresh 同步触发时才为正，则冻结为 **reset-coupled support**。
- 只有当 `consume-honest` 与 `address-stable` 在 `W2/B1` 与 `W2/B2` consume-time stress cells 中均为正、且 reset 协议不强制锁定到 consume time 时，才允许升级为 **persistent-task-simulator-subtracted packet-contract residual**。
- reviewer-facing 默认先看 `mem-token / long-horizon`（representation-side 解释力），再看 `address-stable`，最后才看 `consume-honest`；不允许把 Mem-World 的 rollout fidelity 提升直接写成 full handoff gain。

### 当前预期结论
更可能的诚实结果是：Mem-World 先显著提升 **memory token 压缩质量** 与 **长时程 coherent rollouts**，但只有少数配置会把这部分 persistent simulation 增益真正带过 delayed-consumption 审计，且 `address-stable` 在跨 episode reset 后是否仍指向同一对象是核心瓶颈。这正好让 D01 把 **persistent simulator support** 与 **packet-contract residual** 分开记账，避免被"长时程一致 rollouts"误读成 deployment-time supervisor 也更强。

## E21. RL-Augmented World-Action Model as Action-Honest Refresh Prior（R20260620 新增）

### 目标
把今日扫描本地新增锚点 **WAM-RL (2606.17906)** 吸收进 D01 的实验审计，但保持它只作为 **RL-augmented WAM support family**：reconstruction reward + online video SFT，并天然冒领成 deployment-time packet-contract 进步。重点是验证 WAM-RL 风格的 representation-action 闭环耦合是否能在 world-model refresh 与 action-head update 显式解耦后仍保持 action-honest，还是只能停留在 same-cycle long-horizon 增益。

### 对照组
1. **W0 imitation-only WAM**：纯模仿学习的 World-Action Model baseline
2. **W1 WAM + reconstruction reward（无 online SFT）**：仅加 RL 信号，不做 online self-rollout fine-tune
3. **W2 WAM-RL 完整版本**：reconstruction reward + Online Video SFT 联合训练
4. **W3 W2 + de-synchronized packet audit**：在 W2 之上故意把 world-model refresh 与 action-head update 解耦，看 action-honest 是否塌缩

### 最小日志 tuple
- `recon-reward`：训练 / 决策时 action head 受 WM 重建质量影响的强度
- `online-sft`：action head 从 self-rollout 更新的频率与幅度
- `action-honest`：released action 在 refresh 后是否仍指向同一 clause / waypoint / contact intent
- `consume-honest`：D01 packet-contract 残留指标
- `drift`：训练重建目标与部署观测的域漂移
- `sim2real`：RL-augmented WAM 在真实空中操作平台上的迁移表现

可统一记为：
`Ρ_t = (recon-reward, online-sft, action-honest, consume-honest, drift, sim2real)`

### 判线规则
- 若 `W2` 主要提升 `recon-reward` 与 `online-sft`、但 `action-honest` 与 `consume-honest` 在 delayed uptake 下都塌缩，则冻结为 **RL-shape support**。
- 若 `action-honest` 仅在训练/部署场景匹配时为正，则冻结为 **same-domain RL support**。
- 若 `consume-honest` 仅在 world-model refresh 与 action-head update 同步触发时为正，则冻结为 **synchronous RL support**。
- 只有当 `action-honest`、`consume-honest` 与 `drift` 在 `W1/B1`、`W2/B1`、`W2/B2` 三个 stress cells 中均为正、且 reconstruction reward 在 refresh-induced gap 后仍处于 active 状态时，才允许升级为 **RL-augmented packet-contract residual**。
- reviewer-facing 默认先看 `recon-reward / online-sft`（RL-shape 解释力），再看 `drift`，最后才看 `consume-honest`；不允许把 WAM-RL 的 CALVIN long-horizon 胜利直接写成 full handoff gain。

### 当前预期结论
更可能的诚实结果是：WAM-RL 先显著提升 **重建奖励强度** 与 **online SFT 频次**，但只有少数配置会把 representation-action 闭环耦合真正带过 consume-time audit，且 de-synchronized refresh 时 `action-honest` 极易塌缩。这正好让 D01 把 **RL-augmented support** 与 **packet-contract residual** 分开记账，避免被"representation-action 闭环耦合"误读成 deployment-time supervisor 也更强。
