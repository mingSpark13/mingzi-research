# D07 experiments

> 最后更新：2026-05-26 | 当前状态：先冻结四行最小实验包，禁止并开 whole-body / tactile / scene-graph / shared-autonomy 扩展

## 0. 本轮结论

本轮不再扩论文名录，直接把 D07 首轮验证压成**四行最小实验包**：
- `B1 scratch PPO`
- `B2 BC warm-start PPO`
- `B3 BC-to-Q gated PPO`
- `B4 task-space RL + analytic safety projection`

目标不是追最高分，而是先回答一个更关键的问题：**D07 第一轮到底该冻结成 acceleration、retention bridge、safety-shell support，还是 deployable hybrid。**

在已有 guidance-first / verification-first 审计之外，本轮再补一层 **drift-amplitude decoupling** 读法：MEGA 的 reviewer-facing 首问，不再是“哪条 support family 看起来更强”，而是 **随着 base-drift 幅度增加，机械臂是否真的把末端误差稳定地从移动基座漂移里解耦出来**。因此后续四行最小实验包必须同时输出：
- **解耦主曲线**：`base-drift amplitude → end-effector error`
- **三类失败桶**：`arm agility deficit / local-state-quality deficit / arm-induced back-reaction`
- **两层 support subtraction**：`V_row`（verification shell）与 `I_row`（intervention hygiene / copilot support）

也就是说，本轮后 D07 的主表不只是判断谁更会纠偏，而是判断：**末端误差是否在更大漂移下仍保持 bounded，且这个 bounded gain 不能被验证壳更全、接管更平滑、或 copilot 更会修动作这些更弱解释吃掉。**

在这套读法上，本轮又补了一条**边界生存性判线**：同一行结果必须区分它是在 **固定飞行底座** 上显得更强，还是在 **自由漂移/耦合回授** 条件下仍然站得住。换句话说，D07 现在不只问“有没有 guidance gain”，还要问 **这个 gain 离开 artificially stabilized base 之后还能不能活下来**。因此首轮 bundle 需追加两项边界标签：
- `FFB`：fixed-flight boundary survival
- `FMB`：free-moving-base survival

若某行只在固定底座条件下压平 `drift_amp → BDEE`，一恢复 base-arm 耦合就失效，它最多只能记作 planner/projection-side support；只有同时穿过 `FFB + FMB`，并继续改善 `CET/PCST/PGFR` 的 residual，才更配进入 **MEGA = 机械臂高频稳定器** 的主叙事。

---

## 1. 四行最小实验包

### 1.1 设计原则
- 先比最弱解释族，再给更强 claim
- 先过 matched-compute，再谈 W2/W3 晚窗收益
- 先过 family-control，再谈标题升级
- 先冻结 stop 规则，再申请额外算力

### 1.2 默认实验行
| 行 | 方法 | 目的 | 最近弱解释族 |
|---|---|---|---|
| **B1** | scratch PPO | planner-side 最弱基线 | 无 |
| **B2** | BC warm-start PPO | 验证 warm-start 是否只是提速 | planner-only acceleration |
| **B3** | BC-to-Q gated PPO | 验证 retention bridge 是否越过 W1 | retention-only |
| **B4** | task-space RL + analytic safety projection | 验证 projection/hybrid 是否真推进到 W3 与 `s_p` | projection-only |

---

## 2. 统一预算与串行顺序

### 2.1 默认首轮预算
| 行 | seeds | 单 seed 墙钟 | 阶段 | 备注 |
|---|---:|---:|---|---|
| **B1** | 3 | 12h | S2 | 与 B2/B3 严格 matched-compute |
| **B2** | 3 | 12h | S2 | 检验 warm-start 是否保住 `WSR/PRS` |
| **B3** | 3 | 12h | S2 | 检验 `CGU` 是否从 W1 推到 W2/W3 |
| **B4** | 3 | 4h | S3 | 只做 D2/D3 + W2/W3 + payload promotion slice |

### 2.2 串行执行顺序
1. **S1 smoke test**：四行都先跑 `30-60 min` 缩小 batch 版本，只验 `reset / disturbance / checkpoint / reward / window logging` 五件事。
2. **S2 matched-compute**：只对 **B1/B2/B3** 开完整 `3 seeds × 12h`，保证 planner / retention 线在同成本下比较。
3. **S3 promotion**：从 B1-B3 中只保留 **最强一行**，再与 **B4** 做 `4h` 的 D2/D3 + W2/W3 + payload slice 对照。
4. **禁止并开扩展项**：semantic state / shared autonomy / extra reward variants / whole-body 大矩阵，均不得先于四行包结论抢算力。

---

## 3. S1 smoke test 清单

### 3.1 必过项
- [ ] **Smoke-S0 环境稳定**：3 个 seed 均可正常 reset / rollout，前 100 episode 无 NaN / 持续发散
- [ ] **Smoke-S1 日志完整**：能导出 `success / phase score / episode length / reset reason / attitude recovery time`
- [ ] **Smoke-S2 窗口可定位**：能记录 `W1 / W2 / W3`，不是只有单一总成功率
- [ ] **Smoke-S3 扰动可复现**：D2/D3 注入可控，payload slice 可单独开启
- [ ] **Smoke-S4 BC 可加载**：BC-50 或 BC-200 至少一组能成功初始化策略，且动作方差不塌缩
- [ ] **Smoke-S5 projection 可记录**：unsafe-action rejection / correction rate 至少能导出基础统计

### 3.2 放行规则
只有在以下条件全部满足时，才允许进入正式 S2/S3：
1. smoke test 全过
2. 至少一组 BC 数据能稳定初始化并跑满 30min
3. reset reason 可结构化统计
4. phase score 已拆成 W1/W2/W3 或等价窗口
5. payload slice 可单独开关

---

## 4. 首轮关键指标

### 4.1 通用指标
- 成功率曲线
- phase score 曲线
- 首次达到 60% / 80% success 的步数
- episode 平均长度
- reset / crash 原因统计
- 姿态恢复时间

### 4.2 D07 专用 routing 指标
- `ΔW1 / ΔW2 / ΔW3`
- `WSR / PRS / CGU`
- `unsafe-action rejection rate`
- `contact-preserving correction rate`
- `stabilization-after-projection gain`
- `R_rew=(AER, RCR, LRS, w^+_rew, s^dagger_rew)`
- 最高存活扰动源：`s_v / s_b / s_c / s_p`

### 4.3 MEGA 解耦主曲线与失败桶（2026-05-30 新增）
- **解耦主曲线**：`drift_amp → BDEE`，至少在 `D0 / D1 / D2 / D3` 四档漂移幅度上输出均值、方差与 slope。
- **曲线核心判读**：若 base drift 增大时 `BDEE` 只缓慢增长、且在 contact / post-contact 阶段仍保持 bounded，才说明“机械臂高频补偿无人机低频漂移”的核心物理主张初步站住。
- **失败桶分解**：
  - `F_arm`：**arm agility deficit**（机械臂响应频率/幅度不够，无法及时抵消 base drift）
  - `F_state`：**local-state-quality deficit**（局部观测/接触/目标状态不稳定，导致 arm 有能力但补偿方向不准）
  - `F_react`：**arm-induced back-reaction**（机械臂快速运动反过来激化机体扰动，形成耦合放大）
- **最小新增日志字段**：
  - `mega.drift.amp`
  - `mega.drift.bdee_mean`
  - `mega.drift.bdee_std`
  - `mega.failure.arm_agility`
  - `mega.failure.local_state`
  - `mega.failure.back_reaction`
  - `mega.vss.task_coverage`
  - `mega.vss.failure_coverage`
  - `mega.vss.slice_coverage`
  - `mega.vss.benchmark_build_cost`
- **解释纪律**：若某行 guidance tuple 看起来变强，但解耦曲线斜率没改善，或失败主要从 `F_arm/F_state/F_react` 某一桶泄露，则该行最多保留为 support-side 改善，不得直接升格为 **deployable hybrid**。
- **新增 support-family subtraction**：若某行主要通过更真实的接触状态表征改善 W2/W3，则先记作 `contact-state support`；若某行主要通过 critic-guided diffusion / value-guided 去噪改善训练效率、恢复平滑度或探索质量，则先记作 `critic-guided optimization support`。这两类默认只能解释 `ΔCET/ΔPCST` 或早期 guidance 稳定性，除非同一行还能继续压平 `drift_amp → BDEE` 斜率、存活到 `W3` 并降低 `ΔPGFR`，否则不得升级到 MEGA guidance-bearing 叙事。
- **新增 bundle-internal metric-first rights**：`B2` 默认先解释 `WSR / PRS / W1` 早窗收益，`B3` 默认先解释 retention-gated 的 `W2/W3` 保持与有限 `CET` 改善，`B4` 默认先解释 `unsafe-action rejection / contact-preserving correction / 局部 PCST` 增益。只要一行的优势仍停留在其机制原生指标上，就不得直接升级成“机械臂高频稳定器”主张；必须在对应 support ceiling 之外继续改善 `BDEE/CET/PCST/PGFR`，才允许进入 MEGA residual 审计。
- **新增四类首过标签**：首轮每行都必须先标注 `PRS / ROS / VSS / TPS` 的主解释归属，再看 residual guidance。也就是说，下一步不是继续扩 family，而是先回答：这行到底是 **平台更稳 / 奖励更会记账 / 验证壳更完整 / sim-real 协议更顺**，还是确实还剩下 arm-side 高速补偿残差。
- **新增边界生存标签**：
  - `FFB`：fixed-flight boundary survival，测试在人工稳定底座下该行是否仍保有 guidance gain
  - `FMB`：free-moving-base survival，测试恢复 base-arm 耦合后该行 residual 是否仍成立
- **边界判读纪律**：如果某行只在 `FFB` 站得住、而在 `FMB` 失效，则默认先冻结为 planner-side / projection-side / local-arm support；只有同时通过 `FFB + FMB`，并继续压平 `drift_amp → BDEE`、改善 `CET/PCST/PGFR`，才允许进入真正的 MEGA 高频稳定器叙事。
- **deployment-risk coverage 后置闸门**：即便某行已通过 `PRS / ROS / VSS / TPS / MCS / WMPS / TFOS / KAS / MTS` subtraction，并在 `FFB + FMB` 下保住 residual guidance，也还必须接受 **ROBOGATE 式两阶段边界聚焦风险发现**。默认流程：先做 coarse sweep，再对成功率过渡区做 boundary-focused refinement；若 transition zone 过窄、风险边界过陡、或 payload / latency / contact-timing 一扰就塌，则该行只能记作“mean-metric 下看似可用”的 support-side 结果，不能直接升格为最强 MEGA wording。
- **最小新增日志字段**：`mega.risk.coarse_pass_rate / mega.risk.boundary_transition_width / mega.risk.boundary_collapse_axis / mega.risk.coverage_ceiling`。
- **风险判读纪律**：首轮 reviewer-facing 主表除 `DriftSlope / FFB / FMB` 外，还必须补一句 `boundary-risk note`，明确 residual guidance 是在**宽容边界**上成立，还是只在**狭窄可用区**内成立。只有 residual 同时通过 support subtraction、FFB/FMB、生存到 `g^†=W3`，并且 boundary-focused risk coverage 不显示脆弱窄边界时，才允许进入“机械臂高频稳定器”最强结论。
- **新增 row-native support match 纪律**：四行最小 bundle 必须先标注各自最自然的 support ceiling，再看是否还有 residual guidance。`B2` 默认先解释 `WSR / PRS / W1` 早窗收益；`B3` 默认先解释 retention-gated 的 `W2/W3` 保持与有限 `CET` 改善；`B4` 默认先解释 `unsafe-action rejection / contact-preserving correction / 局部 PCST` 增益。若优势仍停留在机制原生指标上，则结论必须先冻结为 `acceleration / retention bridge / safety-shell support`，不得直接升级成“机械臂高频稳定器”。
- **新增 local-guidance-state 审计**：首轮 bundle 除了 support subtraction，还必须补一层 `LGS_row` 检查，至少区分 `joint-response consistency / contact-state reliability / collision-consistent correction` 三类局部状态质量。若某行的 `BDEE/CET/PCST` 改善主要来自更干净的局部状态假设、固定底座便利、或接触状态被模拟器过度简化，则该行默认先冻结为 `transfer/infrastructure/hybrid support`，不得直接写成 moving-base guidance residual。
- **最小 LGS 日志字段**：`mega.lgs.joint_response_mismatch / mega.lgs.contact_state_reliability / mega.lgs.collision_consistent_correction / mega.lgs.local_state_ceiling / mega.lgs.residual_survives`
- **LGS 判读纪律**：只有当某行在 `SEG / TPS / VSS / OCS / WMPS` 扣除后，仍能在局部状态受压条件下保住更平的 `drift_amp -> BDEE` 曲线、并继续改善 `CET/PCST`，才允许把该 residual 继续上推到 strongest MEGA wording。
- **新增 immediate gate**：在既有 `PRS / ROS / VSS / TPS / MCS / WMPS / TFOS / KAS / MTS` subtraction 之后，还必须再过 `FFB + FMB` 双边界与 `ROBOGATE-style boundary-risk coverage`；只有在 support subtraction 之后 residual 仍同时通过固定底座、自由漂移底座、以及边界聚焦风险发现三层测试，才允许进入 strongest MEGA wording。
- **新增 execution-scheduling support freeze**：若后续引入 EQRL 一类执行调度分支，其默认最弱解释权应先落在 **EQS（elastic-query scheduling support）**，只允许先解释 `average_inference_cost / query_allocation_efficiency / chunk_length_adaptation / latency_sensitive_stability`；除非同一行在 matched subtraction 后继续压平 `drift_amp -> BDEE`、改善 `CET/PCST`、存活到 `g^†=W3` 并降低 `PGFR`，否则不得升级成机械臂高频稳定器证据。
- **新增 execution/warm-start/protocol ceiling tags**：除既有 `EQS` 外，首轮主表还必须显式记录 `SEG`（warm-start/sample-efficiency gain）与 `TPS`（transfer-protocol support）两类 ceiling。若某行优势主要来自更快收敛、BC 初始化更稳、或 sim-real handoff 更顺，则它默认先冻结为 `SEG/TPS support-dominant`，不能直接升格成机械臂高频稳定器残差。
- **最小新增日志字段**：`mega.seg.ceiling / mega.seg.time_to_threshold_gain / mega.seg.early_window_gain / mega.tps.ceiling / mega.tps.transfer_cost_gain / mega.tps.real_anchor_gain / mega.main.eqs_ceiling / mega.main.seg_ceiling / mega.main.tps_ceiling`。
- **support-tag 判读纪律**：只有当一行在 `EQS/SEG/TPS` 三类 ceiling 都被显式标记为 `subtracted` 后，仍继续压平 `drift_amp -> BDEE`、改善 `CET/PCST`、存活到 `g^†=W3`，并在 `FFB + FMB` 下保住 residual，才允许进入 strongest MEGA wording。

---

## 5. stop 规则

### 5.1 family-control stop rules
- **SR-1**：若 **B2** 在 matched-compute 下无法稳定击败 **B1**，或 `WSR/PRS` 不站住，则 warm-start 只能降级为训练便利项。
- **SR-2**：若 **B3** 只改善 retention 指标、`CGU` 仍集中在 W1，则冻结为 **anti-forgetting bridge**，不得吸收 W2/W3 叙事预算。
- **SR-3**：若 **B4** 主要提升 unsafe-action rejection，却不提升 `Δcontact / Δstabilize / s_p`，则冻结为 **projection-only safety-shell support**。
- **SR-4**：若某行在 family-control 检查后仍由 `R_rew` 主导解释，则标题路径自动降级为 **reward-shaped recovery support**。

### 5.2 基础判停
- 若 6h 后 **B1/B2/B3** 全都未过 40% success，先停，回查 reward / observation / action scaling / logging
- 若窗口日志缺失，直接判该轮无效，不进入标题 routing
- 若 payload slice 无法稳定复现，则禁止使用 `deployable hybrid` 口径

---

## 6. 首轮结果 → 标题冻结规则

### 6.1 唯一允许的标题口径
- `acceleration`
- `retention bridge`
- `safety-shell support`
- `reward-shaped recovery`
- `deployable hybrid`

### 6.2 升级条件
只有同时满足以下四项，才允许升到 **deployable hybrid**：
1. 存活到 `W3`
2. 到达扰动源 `s_p`
3. 击败最近 family control
4. 不再由 `R_rew` 主导解释

任意一项失败，标题必须降到最弱仍成立的那一档。

---

## 7. 首轮结束后唯一要填的七项
- **赢家行**：B1 / B2 / B3 / B4
- **最早站住窗口**：W1 / W2 / W3
- **最高存活扰动源**：`s_v / s_b / s_c / s_p`
- **冻结出的标题口径**：acceleration / retention bridge / safety-shell support / reward-shaped recovery / deployable hybrid
- **解耦曲线斜率**：`slope(drift_amp → BDEE)`
- **主失败桶**：`F_arm / F_state / F_react`
- **是否仍被 support subtraction 吃掉**：verification shell / intervention hygiene / copilot / reward / decomposition / none

---

## 8. 下一轮唯一动作
- [ ] 把四行 bundle 细化成**实际训练脚本接口 + 日志字段清单 + payload slice 开关位置**
- [ ] 确认 BC checkpoint 加载入口、BC-to-Q gate 开关点、analytic projection 统计输出位置
- [ ] 先准备 S1 smoke test，不并开额外方向
- [ ] 新增路由日志：`winner_row / w^+ / s^dagger / τ_title / τ_credit`，与 PAPER.md 的 `\Omega_{route}^{D07}` 对齐

---

## 9. MEGA guidance-first 日志字段映射（2026-05-23 新增）

### 9.1 主表必填列
| 列名 | 含义 | 最低要求 |
|---|---|---|
| `Method` | B1/B2/B3/B4 行标识 | 固定四行 |
| `ΔBDEE` | base-drift end-effector error 改善量 | D1/D2 至少各一组统计 |
| `ΔCET` | contact-establishment time 改善量 | W2 必填 |
| `ΔPCST` | post-contact stabilization time 改善量 | W3 必填 |
| `ΔPGFR` | payload-bearing guidance failure rate 改善量 | `s_p` slice 必填 |
| `g^+` | 最早稳定正增益 guidance window | `W1/W2/W3` |
| `g^†` | 最晚仍存活 guidance window | `W1/W2/W3` |
| `s^†` | 最高存活扰动源 | `s_v/s_b/s_c/s_p` |
| `DriftSlope` | `drift_amp → BDEE` 解耦曲线斜率 | 至少四档幅度拟合 |
| `FailureBucketDominant` | 主失败桶 | `F_arm/F_state/F_react/none` |
| `FFB` | fixed-flight boundary survival | `pass/fail + note` |
| `FMB` | free-moving-base survival | `pass/fail + note` |
| `SupportFamilyExplanation` | 当前最弱仍成立的 support-family 解释 | acceleration / retention / projection / reward / copilot / decomposition |
| `GuidanceSubtractedCeiling` | 扣除 guidance 改善后该行还能宣称到哪一档 | acceleration / retention bridge / safety-shell support / reward-shaped recovery / deployable hybrid |
| `PromotionBlocker` | 当前不能升格的直接原因 | late-window 缺失 / 未到 `s_p` / family-control 未击败 / `R_rew` 主导 / drift-decoupling 不成立 / FFB-FMB 边界失效 |

### 9.1e row-native support match, boundary survival, and deployment-risk coverage freeze（2026-06-09 新增）
- **row-native support ceilings**：
  - `B2 -> acceleration / warm-start support`：默认先解释 `WSR / PRS / W1 alignment gain`
  - `B3 -> retention bridge support`：默认先解释 gated retention、`W2/W3` 保持与有限 `ΔCET`
  - `B4 -> projection / safety-shell support`：默认先解释 `unsafe_action_rejection / contact_preserving_correction / local_PCST_gain`
- **新增最小日志字段**：`row_native_support_match / row_native_metric_frontier / row_native_residual_guidance / mega.ffb.pass / mega.ffb.note / mega.fmb.pass / mega.fmb.note / mega.boundary_survival_ceiling / mega.risk.coarse_pass_rate / mega.risk.boundary_transition_width / mega.risk.boundary_collapse_axis / mega.risk.coverage_ceiling / mega.risk.boundary_note`
- **边界生存升级纪律**：任一行即便通过 `PRS / ROS / VSS / TPS / MCS / WMPS / TFOS / KAS / MTS` subtraction，只要 `FMB` 失败，就不能升级到 MEGA strongest wording；默认冻结在 planner-side / projection-side / local-arm support。只有 residual 同时通过 `FFB + FMB`，并继续压平 `DriftSlope`、保持 `g^†=W3`、降低 `ΔPGFR`，才允许升级为 **mechanical-arm high-frequency stabilizer** 叙事。

### 9.1j off-policy throughput support freeze（2026-06-10 新增）
- **目标**：预先冻结未来 FlashSAC / replay-efficient off-policy 分支的最弱解释权，防止“训练更快/critic 更稳”被误写成 moving-base guidance 已经更强。
- **默认最弱解释权**：`OTS（off-policy throughput support）` 先解释 `time-to-threshold / replay-efficiency / critic-stability / seed-variance reduction`。
- **新增最小日志字段**：
  - `mega.ots.match`
  - `mega.ots.time_to_threshold_gain`
  - `mega.ots.replay_efficiency_gain`
  - `mega.ots.critic_stability_gain`
  - `mega.ots.seed_variance_gain`
  - `mega.ots.support_ceiling`
  - `mega.ots.residual_guidance`
- **判读纪律**：若某行优势主要停留在 OTS 指标，而 `DriftSlope / CET / PCST / PGFR / FMB` 未同步改善，则结论必须先冻结为 **training-shell support**；只有在 matched subtraction 后 residual 仍通过 `FFB + FMB`，继续压平 `drift_amp -> BDEE`、保住 `g^†=W3` 并降低 payload-bearing 失败，才允许进入更强的 MEGA guidance wording。

### 9.1k row-native support frontier, FFB/FMB, and boundary-risk freeze（2026-06-10 新增）
- **row-native support frontiers**：
  - `B2 -> acceleration / warm-start support`：默认先解释 `WSR / PRS / W1 alignment gain`
  - `B3 -> retention bridge support`：默认先解释 gated retention、`W2/W3` 保持与有限 `ΔCET`
  - `B4 -> projection / safety-shell support`：默认先解释 `unsafe_action_rejection / contact_preserving_correction / local_PCST_gain`
- **新增最小日志字段**：
  - `mega.row_native_support_match`
  - `mega.row_native_metric_frontier`
  - `mega.row_native_residual_guidance`
  - `mega.ffb.pass`
  - `mega.ffb.note`
  - `mega.fmb.pass`
  - `mega.fmb.note`
  - `mega.boundary_survival_ceiling`
  - `mega.risk.coarse_pass_rate`
  - `mega.risk.boundary_transition_width`
  - `mega.risk.boundary_collapse_axis`
  - `mega.risk.coverage_ceiling`
  - `mega.risk.boundary_note`
- **边界生存升级纪律**：任一行即便通过 support subtraction，只要 `FMB` 失败，就不能升级到 MEGA strongest wording；默认冻结在 planner-side / projection-side / local-arm support。只有 residual 同时通过 `FFB + FMB`，并继续压平 `DriftSlope`、保持 `g^†=W3`、降低 `ΔPGFR`，才允许升级为 **mechanical-arm high-frequency stabilizer** 叙事。
- **boundary-risk 后置闸门**：即便 residual 已通过 `FFB + FMB`，若 `boundary_transition_width` 过窄、`boundary_collapse_axis` 明显、或 payload / latency / contact-timing 一扰就塌，则该行只能记作“mean-metric 下看似可用”的 support-side 结果，不能直接进入 strongest MEGA wording。

### 9.1ib reviewer-facing main-table note discipline（2026-06-09 新增）
- 主表中凡涉及 Any2Any/X-DiffVLA 风格路线，`SupportFamilyExplanation` 必须优先写成 `KAS` 或 `MTS`，除非 row-wise residual 已通过 `WMPS / TFOS / KAS / MTS` 四层 subtraction。
- `PromotionBlocker` 新增合法值：`cross-embodiment support still sufficient`，用于明确说明“当前结果还可被更容易迁移/共享动作头充分解释”。
- 若 `KAS/MTS` 已经解释掉大部分增益，则 `GuidanceSubtractedCeiling` 最多只能到 `transfer-structure support`，不得直接写成 `deployable hybrid` 或 `mechanical-arm high-frequency stabilizer`。
- **ROBOGATE 风险覆盖纪律**：即便 `FFB/FMB` 通过，也还必须补做两阶段 boundary-focused risk coverage；若 `boundary_transition_width` 过窄、或 collapse 主要集中在 payload / latency / contact-timing 轴，则结论默认冻结为“deployment-risk 未过”的 support-side 版本，不能直接进入最强标题口径。

### 9.1f curriculum-shell / platform-survey freeze（2026-06-04 新增）
- **MT-Libero + DGPO (2606.03335) → MCS（multi-task curriculum shell）**：默认只允许先解释 demonstration-guided initialization quality、shared task-family coverage、on-policy optimization stability、adaptation-cost reduction；若没有同步压平 `drift_amp → BDEE`、把 `g^†` 推进到 `W3`，并在 payload slice 降低 `PGFR`，不得升级为高频稳定器证据。
- **NVIDIA Isaac Sim Survey (2606.03551) → PSS（platform-survey support）**：默认只允许先解释 Isaac Sim / Isaac Lab 作为实验基座的物理、传感器、数据与生态合理性，不参与方法增益归因。
- **最小 subtraction 字段**：`MCS_match / task_family_coverage_gain / demo_guidance_gain / adaptation_cost_delta / PSS_match / infrastructure_justification_only`。
- **升级纪律**：只要一行结果仍可被“更会做 multi-task curriculum / demonstration-guided optimization / platform choice 更合理”解释，就不能冒领 **mechanical-arm high-frequency stabilizer** 叙事。

### 9.1d world-model / training-free strong-control family freeze（2026-06-04 新增）
- **TD-MPC2 (2310.16828) → WMPS（world-model planning support）**：默认只允许先解释 latent dynamics prediction、更平滑的 receding-horizon proposal、cross-regime adaptation、以及 planner-side disturbance handling；若没有在 moving-base 条件下继续压平 `drift_amp → BDEE`、推进 `g^†` 到 `W3` 并降低 payload-bearing `PGFR`，不得升级为机械臂高频稳定器证据。
- **DIAL-MPC (2409.15610) → TFOS（training-free optimizer support）**：默认只允许先解释更强 full-order online refinement、tracking-error reduction、以及 solver-side short-horizon disturbance rejection；若主要增益仍可由 sampling-based MPC + diffusion-style annealing 解释，而非 arm-side residual compensation，则不得升级为 MEGA guidance-bearing 证据。
- **最小 subtraction 字段**：`WMPS_match / latent_prediction_gain / planner_refinement_gain / TFOS_match / full_order_solver_gain / training_free_tracking_gain / planner_vs_arm_residual_split`。
- **升级纪律**：只要一行结果仍可被“planner 已经更会预测/优化”解释，就不能冒领 **mechanical-arm high-frequency stabilizer** 叙事；只有在扣除 `WMPS/TFOS` 后仍保持 `DriftSlope` 更平、`g^†=W3`、且 `ΔPGFR` 继续下降时，才允许继续升级到 deployable hybrid 或更强 guidance claim。

#### 9.1f transfer-protocol support freeze（2026-06-06 新增）
- **RL-Based Sim-Real Co-Training for VLA (2602.12628) → TPS（transfer-protocol support）**：默认只允许先解释初始化保真、sim-real 适配成本下降、real-anchor continuity、以及 early-window deployment readiness；若没有在 matched subtraction 后继续压平 `drift_amp → BDEE`、把 `g^†` 推进到 `W3`，并在 payload-bearing slice 降低 `PGFR`，不得升级为 **mechanical-arm high-frequency stabilizer** 证据。
- **四重减法审计**：后续 reviewer-facing 最小残差需显式穿过 `PRS`（platform/reproducibility support）、`ROS`（reward-origin support）、`VSS`（verification-shell support）、`TPS`（transfer-protocol support）四层扣减；只要某行 guidance gain 仍可主要由这四层之一解释，就只能停在对应 support-family ceiling。

#### 9.1g off-policy throughput support freeze（2026-06-09 新增）
- **FlashSAC (2604.04539) → OTS（off-policy throughput support）**：默认只允许先解释更快 `time-to-threshold`、更高 `replay_efficiency`、更稳 `critic_stability`、以及更低 `seed_variance` 的优化侧收益；若没有在 matched subtraction 后继续压平 `drift_amp → BDEE`、把 `g^†` 推进到 `W3`，并在 payload-bearing slice 降低 `PGFR`，不得升级为 **mechanical-arm high-frequency stabilizer** 证据。
- **最小 subtraction 字段**：`OTS_match / time_to_threshold_gain / replay_efficiency_gain / critic_stability_gain / seed_variance_gain / ots_support_ceiling / ots_residual_guidance`。
- **升级纪律**：只要一行结果仍可主要被“off-policy 训练更快、更稳、critic 更不漂”解释，就不能冒领 arm-side guidance residual；只有在扣除 `OTS` 后 residual 仍同时通过 `FFB + FMB`、继续压平 `DriftSlope`、改善 `CET/PCST` 并降低 `ΔPGFR`，才允许进入更强的 MEGA wording。
- **最小新增日志 key**：
  - `mega.tps.match`
  - `mega.tps.real_anchor_gain`
  - `mega.tps.adaptation_cost_delta`
  - `mega.tps.early_window_readiness_gain`
  - `mega.residual.prs_subtracted`
  - `mega.residual.ros_subtracted`
  - `mega.residual.vss_subtracted`
  - `mega.residual.tps_subtracted`
  - `mega.residual.high_freq_stabilizer_survives`
- **解释纪律**：最终允许占据 MEGA 标题的，不是“sim-real 共训后更像能部署”的总印象，而是**在扣除平台、奖励、验证壳与迁移协议优势后，仍持续压平 `DriftSlope`、存活到 `g^†=W3`、并降低 `ΔPGFR` 的 residual guidance gain`。**


#### 9.1f verification-shell support freeze（2026-06-05 新增）
- **MobileManiBench (2602.05233) → VSS（verification-shell support）**：默认只允许先解释 `task coverage / failure-mode surfacing / slice completeness / benchmark construction cost`，不直接参与 moving-base guidance 增益归因。
- **最小 subtraction 字段**：`VSS_match / task_coverage_gain / failure_coverage_gain / slice_coverage_gain / benchmark_build_cost_delta / verification_shell_only`。
- **升级纪律**：只要一行结果仍可被“验证壳更全、更容易暴露差异、更系统地定位失败”解释，就不能冒领 **mechanical-arm high-frequency stabilizer** 叙事；只有在扣除 VSS 后仍保持 `DriftSlope` 更平、`g^†=W3`、且 `ΔPGFR` 继续下降时，才允许继续升级。

#### 9.1g sim-real protocol support freeze（2026-06-05 新增）
- **RL-Based Sim-Real Co-Training for VLA (2602.12628) → PSC（protocol support / sim-real continuity）**：默认只允许先解释 `sim-real anchoring continuity / adaptation-cost reduction / curriculum continuity / transfer readiness`，以及离开仿真后的早期 `ΔBDEE` 或温和 `ΔCET` 改善。
- **最小 subtraction 字段**：`PSC_match / simreal_anchoring_gain / adaptation_cost_delta / curriculum_continuity_gain / transfer_readiness_gain / protocol_only`。
- **升级纪律**：只要一行结果仍可被“sim-real protocol 更连续、更容易适配真机”解释，就不能冒领 **mechanical-arm high-frequency stabilizer** 叙事；只有在扣除 PSC 后仍保持 `DriftSlope` 更平、`g^†=W3`、且 `ΔPGFR` 继续下降时，才允许继续升级。

#### 9.1h PSC-VSS coupled subtraction for the first real bundle（2026-06-05 新增）
- **PSC-VSS 耦合风险**：真实部署 bundle 中，`protocol continuity` 与 `verification-shell completeness` 很可能同时增强，容易把“更顺的 sim-real 迁移”与“更干净的验证壳”误写成 controller-side guidance advance。
- **默认解释边界**：
  - `PSC` 只允许先解释 `adaptation continuity / warm-start survivability / sim-real friction reduction`
  - `VSS` 只允许先解释 `task coverage / failure coverage / slice completeness / benchmark-shell cleanliness`
- **最小耦合 subtraction 字段**：`PSC_VSS_coupled_match / real_bundle_protocol_gain / real_bundle_shell_gain / coupled_support_ceiling`。
- **升级纪律**：首个 real bundle 只有在**同时扣除 PSC 与 VSS** 后，残差仍继续改善 `ΔBDEE / ΔCET / ΔPCST / ΔPGFR`，并保持 `DriftSlope` 更平、`g^†=W3`、`ΔPGFR` 继续下降时，才允许继续升级到 MEGA guidance-bearing 叙事。
- **解释纪律**：如果一行 post-transfer 结果更强，但主要可由“迁移协议更顺”或“验证壳更全”解释，则 ceiling 只能停在 **protocol support** 或 **verification-shell support**，不得冒领 mechanical-arm high-frequency stabilizer。

#### 9.1i multi-task curriculum shell freeze（2026-06-06 新增）
- **MT-Libero + DGPO (2606.03335) → MCS（multi-task curriculum shell）**：默认只允许先解释 `demonstration-guided initialization quality / heterogeneous task-family coverage / on-policy optimization stability / adaptation-cost reduction`，以及少量早期 `ΔBDEE` 收敛稳定性改善。
- **最小 subtraction 字段**：`MCS_match / demo_init_gain / task_family_coverage_gain / onpolicy_stability_gain / adaptation_cost_delta / curriculum_shell_only`。
- **metric-first rights**：MCS 最自然先解释的是 `seed variance ↓ / early ΔBDEE stabilization / adaptation-cost ↓`，而不是 `ΔPCST / ΔPGFR`；若没有同步把 `g^†` 推进到 `W3`、压平 `DriftSlope`、并在 payload slice 降低 `ΔPGFR`，不得升级成 mechanical-arm high-frequency stabilizer 证据。
- **升级纪律**：只要一行结果仍可被“curriculum 设计更好、示教引导更顺、多任务壳更稳”解释，就不能冒领 **MEGA guidance-bearing** 叙事；只有在扣除 MCS 后 residual 仍持续改善 `ΔBDEE / ΔCET / ΔPCST / ΔPGFR`，才允许继续升级。

#### 9.1ia cross-embodiment transfer-structure freeze（2026-06-08 新增）
- **Any2Any (2605.23733) → KAS（kinematic-alignment support）**：默认只允许先解释 action-space translation、更低 embodiment mismatch、target-side adaptation cost 下降，以及 shared action interface 带来的早期稳定性改善。
- **X-DiffVLA (2605.25044) → MTS（morphology-tree support）**：默认只允许先解释 morphology reuse、shared action-head organization、以及 embodiment-family generalization 效率提升。
- **最小 subtraction 字段**：`KAS_match / embodiment_translation_gain / action_head_reuse_gain / adaptation_cost_delta / MTS_match / morphology_reuse_gain / cross_embodiment_support_ceiling`。
- **metric-first rights**：KAS/MTS 最自然先解释的是 `adaptation-cost ↓ / early ΔBDEE stabilization / transfer readiness ↑`，而不是 `ΔPCST / ΔPGFR`；若没有同步把 `g^†` 推进到 `W3`、压平 `DriftSlope`、并在 payload slice 降低 `ΔPGFR`，不得升级成 **mechanical-arm high-frequency stabilizer** 证据。
- **升级纪律**：只要一行结果仍可被“embodiment 对齐更顺 / morphology reuse 更强 / 动作头共享更有效”解释，就不能冒领 **MEGA guidance-bearing** 叙事；只有在扣除 `KAS/MTS` 后 residual 仍持续改善 `ΔBDEE / ΔCET / ΔPCST / ΔPGFR`，才允许继续升级。

#### 9.1j transfer-protocol residual freeze and four-way support audit（2026-06-09 新增）
- **RL-Based Sim-Real Co-Training for VLA (2602.12628) → TPS（transfer-protocol support）**：默认只允许先解释 `initialization alignment / real-world adaptation-cost reduction / sim-real continuity / early deployment readiness`，以及温和的早窗 `ΔBDEE` 或 `ΔCET` 改善；若没有在 matched subtraction 后继续压平 `drift_amp → BDEE`、把 `g^†` 推进到 `W3`、并在 payload-bearing slice 降低 `ΔPGFR`，不得升级成 **mechanical-arm high-frequency stabilizer** 证据。
- **四重减法最小审计**：后续 submission-facing bundle 至少显式记录 `PRS / ROS / VSS / TPS` 四层 first-pass explanation，并额外回答 `residual guidance survives?`。也就是说，下一步最值钱的不是再扩 family，而是先判断：该行到底是 **平台更稳 / 奖励更会记账 / 验证壳更完整 / 迁移协议更顺**，还是在扣除这些解释后，真的还剩下 arm-side 高速补偿残差。
- **最小新增日志 key**：
  - `mega.tps.match`
  - `mega.tps.init_alignment_gain`
  - `mega.tps.real_adaptation_cost_delta`
  - `mega.tps.simreal_continuity_gain`
  - `mega.tps.early_readiness_gain`
  - `mega.residual.prs_subtracted`
  - `mega.residual.ros_subtracted`
  - `mega.residual.vss_subtracted`
  - `mega.residual.tps_subtracted`
  - `mega.residual.guidance_survives`
- **解释纪律**：最终允许占据 MEGA 标题的，不是“从 Isaac Lab 更顺地迁到真机”的总体印象，而是**在扣除 PRS / ROS / VSS / TPS 后，仍持续压平 `DriftSlope`、存活到 `g^†=W3`、并降低 `ΔPGFR` 的 residual guidance gain**。

#### 9.1k high-frequency-stabilizer residual after MCS subtraction（2026-06-07 新增）
- **MT-Libero + DGPO (2606.03335) → MCS（multi-task curriculum shell）** 已正式并入高频稳定器残差定义；后续 D07 的最强 reviewer-facing 残差不再是 `Δ^HF_row = ΔG_row \ (PRS ∪ ROS ∪ VSS ∪ TPS)`，而是 **`Δ^HF_row = ΔG_row \ (PRS ∪ ROS ∪ VSS ∪ TPS ∪ MCS)`**。
- **MCS 默认解释边界**：只允许先解释 `demonstration-guided initialization quality / task-family coverage / on-policy optimization stability / adaptation-cost reduction / early-window variance reduction`，不能直接解释 payload-bearing `ΔPGFR` 或 `g^†=W3` 的稳定 guidance-bearing 增益。
- **最小新增日志 key**：
  - `mega.mcs.match`
  - `mega.mcs.demo_init_gain`
  - `mega.mcs.task_family_coverage_gain`
  - `mega.mcs.onpolicy_stability_gain`
  - `mega.mcs.adaptation_cost_delta`
  - `mega.residual.mcs_subtracted`
  - `mega.residual.high_freq_stabilizer_survives_after_mcs`
- **解释纪律**：只要一行结果仍可被“multi-task curriculum 更好、示教引导更顺、训练壳更稳”解释，就不能冒领 **mechanical-arm high-frequency stabilizer** 叙事；只有在扣除 `MCS` 后 residual 仍继续压平 `DriftSlope`、推进 `g^†=W3`、并降低 `ΔPGFR` 时，才允许继续升级。

#### 9.1l promotion-ladder + TPS/VSS coupled residual audit（2026-06-10 新增）
- **目标**：把现有 `F0 fixed base -> F1 low-drift -> F2 bounded-drift-with-contact -> F3 payload-bearing drift` 促升梯子，与 `TPS/VSS` 扣减审计绑成同一份 reviewer-facing 结果合同，防止“更顺的 sim-real protocol”或“更完整的 verification shell”被误写成机械臂高频稳定器已经站住。
- **最小 promotion 字段**：
  - `mega.promotion.f0_pass`
  - `mega.promotion.f1_pass`
  - `mega.promotion.f2_pass`
  - `mega.promotion.f3_pass`
  - `mega.promotion.highest_stage`
- **最小 coupled-subtraction 字段**：
  - `mega.tps_vss.coupled_match`
  - `mega.tps_vss.protocol_gain`
  - `mega.tps_vss.shell_gain`
  - `mega.tps_vss.coupled_support_ceiling`
  - `mega.residual.guidance_survives_after_tps_vss`
- **解释纪律**：若某行主要靠更稳的 real-anchor continuity、curriculum continuity、task coverage 或 failure surfacing 才通过 `F1/F2`，则默认先冻结为 `protocol support` 或 `verification-shell support`；只有在 `TPS/VSS` matched subtraction 后，row 仍继续压平 `drift_amp -> BDEE`、把 `g^†` 推进到 `W3`、并在 `F3` 降低 `PGFR`，才允许继续升级到 **mechanical-arm high-frequency stabilizer** 叙事。
- **默认 reviewer-facing 读法**：先看 `highest_stage`，再看 `TPS/VSS coupled support ceiling`，最后才看 `residual guidance survives`。只要 residual 在 `F3` 前消失，即便 row 看起来更会迁移、更会验证，也不得冒领 MEGA strongest wording。

## 9.2 推荐日志 key（训练侧直接导出）
- `mega.bdee.mean_d1`
- `mega.bdee.mean_d2`
- `mega.cet.mean_w2`
- `mega.pcst.mean_w3`
- `mega.pgfr.payload`
- `mega.guidance.first_positive_window`
- `mega.guidance.last_surviving_window`
- `mega.guidance.highest_disturbance_source`
- `mega.drift.amp`
- `mega.drift.bdee_mean`
- `mega.drift.bdee_std`
- `mega.drift.slope`
- `mega.failure.arm_agility`
- `mega.failure.local_state`
- `mega.failure.back_reaction`
- `mega.route.support_family`
- `mega.route.guidance_subtracted_ceiling`
- `mega.route.promotion_blocker`
- `mega.support.wmps_match`
- `mega.support.tfos_match`
- `mega.support.planner_vs_arm_residual_split`
- `mega.support.psc_match`
- `mega.support.simreal_anchoring_gain`
- `mega.support.adaptation_cost_delta`
- `mega.support.curriculum_continuity_gain`
- `mega.support.transfer_readiness_gain`
- `mega.vss.task_coverage`
- `mega.vss.failure_coverage`
- `mega.vss.slice_coverage`
- `mega.vss.benchmark_build_cost`
- `mega.vss.subtracted_ceiling`
- `mega.promotion.f0_pass`
- `mega.promotion.f1_pass`
- `mega.promotion.f2_pass`
- `mega.promotion.f3_pass`
- `mega.promotion.highest_stage`
- `mega.tps_vss.coupled_match`
- `mega.tps_vss.protocol_gain`
- `mega.tps_vss.shell_gain`
- `mega.tps_vss.coupled_support_ceiling`
- `mega.residual.guidance_survives_after_tps_vss`

### 9.3 四行 bundle 的默认 guidance-first 解读
- **B1 scratch PPO**：只作为零 support 最弱基线；若 `ΔBDEE/ΔCET/ΔPCST/ΔPGFR` 全弱，则仅保留 planner-side lower bound。
- **B2 BC warm-start PPO**：默认先看 `ΔBDEE` 与 `ΔCET`；若只更快达线但不改善 guidance tuple，则冻结为 **acceleration**。
- **B3 BC-to-Q gated PPO**：默认先看 `g^†` 是否推进到 `W2/W3`、`ΔCET/ΔPGFR` 是否实际改善；若只保住 BC 行为，则冻结为 **retention bridge**。
- **B4 task-space RL + analytic safety projection**：默认先看 `ΔPCST` 与 `ΔPGFR`；若只提升 unsafe-action rejection 而 guidance tuple 不站住，则冻结为 **safety-shell support**。

### 9.5 anchor-to-guidance-metric 默认归因（2026-05-23 新增）
- **DiSCo / copilot / intervention-hygiene family**：默认只允许先解释 `ΔBDEE` 或早期 `ΔCET`；若没有把 gain 带到 `W2/W3`，不得借口 smoother correction 升格为 late-window guidance evidence。
- **Q2RL / retention family**：默认先看 `ΔCET` 与 `g^†`；若只是保住 BC 行为、不推进 `PCST/PGFR`，则冻结为 **retention bridge**。
- **Reactive Dexterous Grasping / analytic projection family**：默认先看 `ΔPCST`，随后才看 `ΔPGFR`；若只提升 unsafe-action rejection 或接触瞬间稳定性，则冻结为 **projection-only safety-shell support**。
- **Find-the-Fruit / decomposition family**：默认只允许解释更强 uncertainty exposure、task preparation，或间接的 `ΔBDEE/ΔCET` 改善；若没有 moving-base 晚窗 gain，不得占据 MEGA guidance-bearing 叙事。

## 9.10 Find-the-Fruit / Q2RL / Reactive Projection / Copilot 对齐的 guidance-first submission schema（2026-05-25 新增）

### 9.10.2 verification-first 支撑字段（2026-05-26 新增）
在 guidance-first 主表之外，下一轮 bundle 还必须补一组 **verification-first** 字段，用于扣除基础设施 / 验证壳 / sim-real protocol 带来的伪增益：
- `VerificationSupportFamily`
- `TaskCoverageDiversity`
- `FailureModeCoverage`
- `DisturbanceSliceCompleteness`
- `VerificationSubtractedCeiling`

推荐训练侧直接导出：
- `mega.verify.support_family`
- `mega.verify.task_coverage_diversity`
- `mega.verify.failure_mode_coverage`
- `mega.verify.disturbance_slice_completeness`
- `mega.verify.subtracted_ceiling`

默认解释纪律：
- **Isaac Lab / infrastructure family**：默认先解释 reset 稳定、disturbance injection 一致、日志可复现；若 guidance tuple 不动，只能算 **infrastructure-hygiene support**。
- **RL-Based Sim-Real Co-Training family**：默认先解释更稳的 sim-real anchoring / curriculum continuity；若 gain 主要停在早期 `ΔBDEE/ΔCET`，只能算 **protocol support**。
- **MobileManiBench / verification family**：默认先解释 task coverage、failure surfacing、slice completeness；若只是让问题“更容易被看见”，不能占据 MEGA guidance-bearing 叙事。

### 9.10.3 本轮 D07 冻结结论（2026-05-28）
- 本轮高价值扫描命中 **3 个本地锚点**：`MobileManiBench (2602.05233)`、`Hand-in-the-Loop (2605.15157)`、`DiSCo (2603.22787)`。
- **新增正式入库 0 篇**：本地覆盖已足够，不触发 arXiv / Tavily 外扩。
- PAPER 侧新增重点：把 `verification-support` 与 `intervention-hygiene / copilot-support` 两条最容易误升格的 support family 明确压进 D07 的 guidance-first promotion 边界，新增 `V_row` 与 `I_row` 两层减法审计。
- 下轮优先动作：把 `TakeoverJitter / CorrectionQuality / InterventionSmoothness / CopilotSupportFamily` 以及 `TaskCoverage / FailureCoverage / SliceCompleteness / ViewCompleteness` 真正接进训练日志与首张 submission-ready 主表。

它们的作用不是增加报表好看程度，而是强制回答：**这行结果到底是真的推进了 moving-base guidance，还是仍可被 verification shell / intervention hygiene / copilot support / decomposition / retention / projection 这些更弱解释吃掉。**

### 9.10.5 contact-state / critic-guided optimization support 字段（2026-06-01 新增）
在现有 guidance-first、verification-first、intervention-hygiene 审计之外，下一轮 D07 bundle 还必须补两条新的 support-family 日志，用来扣除“接触状态更真”和“critic-guided 训练更高效”带来的伪增益：
- `ContactStateSupportFamily`
- `CriticGuidanceSupportFamily`
- `ContactStateSubtractedCeiling`
- `CriticGuidanceSubtractedCeiling`

推荐训练侧直接导出：
- `mega.contact.support_family`
- `mega.contact.state_quality_gain`
- `mega.contact.post_contact_jitter_reduction`
- `mega.contact.subtracted_ceiling`
- `mega.critic.support_family`
- `mega.critic.sample_efficiency_gain`
- `mega.critic.recovery_quality_gain`
- `mega.critic.subtracted_ceiling`

默认解释纪律：
- **Physics-Grounded Contact Representation / CoP family**：默认先解释 `F_state` 的改善、W2/W3 接触状态更真、post-contact jitter 更低；若没有同步压平 `drift_amp → BDEE` 斜率并稳住 `ΔPGFR`，只能算 **contact-state support**。
- **CGPO / critic-guided diffusion RL family**：默认先解释训练更快、探索更稳、恢复动作更接近高 Q 路线；若没有同步把 guidance gain 推到 `g^†=W3` 与 payload-bearing `s_p`，只能算 **critic-guided optimization support**。

它们的作用不是增加表项，而是强制回答：**这行结果到底是真的证明“机械臂在高频补偿无人机低频漂移”，还是仍可被“接触状态更真 / critic guidance 更会训策略”这些更弱解释吃掉。**

#### verification-shell tuple
- `mega.verify.task_coverage_diversity`
- `mega.verify.failure_mode_coverage`
- `mega.verify.disturbance_slice_completeness`
- `mega.verify.view_completeness`
- `mega.verify.support_family`
- `mega.verify.subtracted_ceiling`

#### 默认解释纪律
- **Hand-in-the-Loop**：默认先解释 takeover jitter 降低、纠偏轨迹更平滑、correction dataset 更干净；若 guidance tuple 不推进到 `W2/W3 + s_p`，只能算 **intervention-hygiene support**。
- **DiSCo**：默认先解释 sequence-level bounded assistance 与 intent-preserving correction；若收益主要停在 `ΔBDEE/ΔCET` 或用户可控性上，不能升级成 late-window MEGA evidence。
- **MobileManiBench**：默认先解释任务覆盖、失败暴露、验证壳更完整；若只是更容易发现问题，而不是 guidance residual 变强，不能占据控制主叙事。

### 9.10.5 guidance-family 默认最弱解释顺序
默认 reviewer-facing 读取顺序固定为：
1. 先看 `ΔBDEE / ΔCET`（是不是只有早期 guidance acquisition）
2. 再看 `ΔPCST`（是不是只在接触后局部稳一点）
3. 最后看 `ΔPGFR + g^† + s^†`（有没有真的活到 payload-bearing 晚窗）
4. 再判 `SupportFamilyExplanation`
5. 最后才给 `GuidanceSubtractedCeiling`

若某行在第 1-3 步就站不住，则后面 family 解释再漂亮，也不得升格为 `deployable hybrid`。

### 9.10.6 当前唯一诚实的标题冻结纪律
只有同时满足以下四项，才允许从 support-family 升到 `deployable hybrid`：
- `ΔPCST` 站住
- `ΔPGFR` 站住
- `g^† = W3`
- `s^† = s_p`

否则，一律冻结到最弱仍成立的那一档：`acceleration / retention bridge / safety-shell support / reward-shaped recovery / decomposition support / intervention-hygiene support / verification-support`。

## 9.11 MobileManiBench 对齐的 verification-first schema（2026-05-28 新增）

### 9.11.1 新增 verification tuple
在 guidance-first 主表之外，下一轮 D07 训练/验证日志必须再补一组 verification tuple：
- `C_task`：自动生成验证任务的覆盖度
- `C_fail`：暴露出的失败模式桶数量/多样性
- `C_slice`：`D0-D3` + payload slice 是否完整覆盖

推荐统一记为：
- `V_row = (C_task, C_fail, C_slice)`

作用很简单：防止某一行只是因为**验证壳更宽/更干净**而看起来更强，却被误写成 controller/interface 真变强。

### 9.11.2 MobileManiBench 默认角色冻结
- **MobileManiBench / verification family**：默认只允许先解释
  - 更强任务覆盖
  - 更快失败模式暴露
  - 更完整 disturbance/payload slice 组织
- 它**不能**单独解释 `MEGA` 标题里的 moving-base guidance gain。
- 若一行结果主要收益来自更好的验证基准与自动任务构造，而不是 `ΔBDEE / ΔCET / ΔPCST / ΔPGFR` 本身改善，则冻结为 **benchmark/verification support**。

### 9.11.3 reviewer-facing 默认读取顺序（更新）
1. 先看 `ΔBDEE / ΔCET / ΔPCST / ΔPGFR / g^† / s^†`
2. 再看 `SupportFamilyExplanation / GuidanceSubtractedCeiling / PromotionBlocker`
3. 最后补看 `V_row=(C_task, C_fail, C_slice)`

只有在 **guidance tuple 站住** 且 **verification tuple 没有暴露“只是验证壳更好”** 时，才允许继续往 `deployable hybrid` 升格。

### 9.11.4 推荐新增日志 key
- `mega.verify.task_coverage`
- `mega.verify.failure_bucket_count`
- `mega.verify.slice_completeness`
- `mega.route.verification_support_flag`
- `mega.route.verification_subtracted_ceiling`

### 9.11.5 guidance tuple + verification tuple 联合日志模板（2026-05-26 补充）

后续四行 bundle 的训练日志和 submission-ready 主表都必须同时输出两组字段：

#### guidance tuple（标题相关）
- `mega.bdee.mean_d1`
- `mega.bdee.mean_d2`
- `mega.cet.mean_w2`
- `mega.pcst.mean_w3`
- `mega.pgfr.payload`
- `mega.guidance.first_positive_window`
- `mega.guidance.last_surviving_window`
- `mega.guidance.highest_disturbance_source`
- `mega.route.support_family`
- `mega.route.guidance_subtracted_ceiling`
- `mega.route.promotion_blocker`

#### verification tuple（减法审计相关）
- `mega.verify.support_family`
- `mega.verify.task_coverage_diversity`
- `mega.verify.failure_mode_coverage`
- `mega.verify.disturbance_slice_completeness`
- `mega.verify.build_maintenance_cost`
- `mega.verify.subtracted_ceiling`

其中 verification tuple 对应：
- `C_task` = task coverage diversity
- `C_fail` = failure mode coverage
- `C_slice` = disturbance / payload slice completeness
- `T_build` = build & maintenance cost of the verification shell
- `κ_verify` = dominant verification-support family

#### 当前本地锚点的默认 verification-family 归因
- **Isaac Lab**：默认先解释 `reset stability / disturbance reproducibility / deployment logging consistency`，只能作为 **infrastructure-hygiene support**
- **RL-Based Sim-Real Co-Training**：默认先解释 `sim-real anchoring continuity / curriculum hygiene`，只能作为 **protocol support**
- **MobileManiBench**：默认先解释 `task coverage / failure surfacing / slice completeness`，只能作为 **benchmark-shell support**

#### 本轮冻结结论
- 本轮高价值扫描命中本地锚点：**RL-Based Sim-Real Co-Training for VLA / IsaacLab-Arena / MobileManiBench**
- 正式新增入库：**0 篇**
- D07 下一步不该扩方法矩阵，而应优先把 `F0/F1/F2/F3 + TPS/VSS coupled subtraction + residual guidance survives` 真正映射进首轮 bundle 的训练脚本与主表导出逻辑
- 当前最重要的新收束：**先回答 row 是不是只靠 protocol continuity / verification shell 更顺地爬上 promotion ladder，再回答机械臂 residual guidance 是否仍活到 `F3`**
