# D07 experiments

> 最后更新：2026-05-26 | 当前状态：先冻结四行最小实验包，禁止并开 whole-body / tactile / scene-graph / shared-autonomy 扩展

## 0. 本轮结论

本轮不再扩论文名录，直接把 D07 首轮验证压成**四行最小实验包**：
- `B1 scratch PPO`
- `B2 BC warm-start PPO`
- `B3 BC-to-Q gated PPO`
- `B4 task-space RL + analytic safety projection`

目标不是追最高分，而是先回答一个更关键的问题：**D07 第一轮到底该冻结成 acceleration、retention bridge、safety-shell support，还是 deployable hybrid。**

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

## 7. 首轮结束后唯一要填的四项
- **赢家行**：B1 / B2 / B3 / B4
- **最早站住窗口**：W1 / W2 / W3
- **最高存活扰动源**：`s_v / s_b / s_c / s_p`
- **冻结出的标题口径**：acceleration / retention bridge / safety-shell support / reward-shaped recovery / deployable hybrid

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
| `SupportFamilyExplanation` | 当前最弱仍成立的 support-family 解释 | acceleration / retention / projection / reward / copilot / decomposition |
| `GuidanceSubtractedCeiling` | 扣除 guidance 改善后该行还能宣称到哪一档 | acceleration / retention bridge / safety-shell support / reward-shaped recovery / deployable hybrid |
| `PromotionBlocker` | 当前不能升格的直接原因 | late-window 缺失 / 未到 `s_p` / family-control 未击败 / `R_rew` 主导 |

### 9.2 推荐日志 key（训练侧直接导出）
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

<<<<<<< HEAD
### 9.10.3 本轮 D07 冻结结论（2026-05-27）
- 本轮高价值扫描命中 **3 个本地锚点**：`MobileManiBench (2602.05233)`、`Hand-in-the-Loop (2605.15157)`、`DiSCo (2603.22787)`。
- **新增正式入库 0 篇**：本地覆盖已足够，不触发 arXiv / Tavily 外扩。
- PAPER 侧新增重点：把 `verification-support` 与 `intervention-hygiene / copilot-support` 两条最容易误升格的 support family 明确压进 D07 的 guidance-first promotion 边界，新增 `V_row` 与 `I_row` 两层减法审计。
- 下轮优先动作：把 `TakeoverJitter / CorrectionQuality / InterventionSmoothness / CopilotSupportFamily` 以及 `TaskCoverage / FailureCoverage / SliceCompleteness / ViewCompleteness` 真正接进训练日志与首张 submission-ready 主表。

它们的作用不是增加报表好看程度，而是强制回答：**这行结果到底是真的推进了 moving-base guidance，还是仍可被 verification shell / intervention hygiene / copilot support / decomposition / retention / projection 这些更弱解释吃掉。**

### 9.10.4 intervention-hygiene / verification-shell 日志字段（2026-05-27 新增）

#### intervention-hygiene tuple
- `mega.intervention.takeover_jitter`
- `mega.intervention.correction_quality`
- `mega.intervention.smoothness`
- `mega.intervention.support_family`
- `mega.intervention.subtracted_ceiling`

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

=======
>>>>>>> 1080f76346ff43cff0d7fb71910b283cdc15be6a
### 9.10.3 本轮 D07 冻结结论（2026-05-26）
- 本轮高价值扫描命中 **3 个本地锚点**：`Isaac Lab (2511.04831)`、`RL-Based Sim-Real Co-Training (2602.12628)`、`MobileManiBench (2602.05233)`。
- **新增正式入库 0 篇**：本地覆盖已足够，不触发 arXiv / Tavily 外扩。
- PAPER 侧新增重点：把 `verification-support / infrastructure-hygiene / sim-real protocol support` 明确并入 D07 的 guidance-first promotion 边界。
- 下轮优先动作：把 `VerificationSupportFamily / TaskCoverageDiversity / FailureModeCoverage / DisturbanceSliceCompleteness / VerificationSubtractedCeiling` 真正接进训练日志与首张 submission-ready 主表。

它们的作用不是增加报表好看程度，而是强制回答：**这行结果到底是真的推进了 moving-base guidance，还是仍可被 decomposition / retention / projection / copilot / reward 这些更弱解释吃掉。**

### 9.10.2 guidance-family 默认最弱解释顺序
默认 reviewer-facing 读取顺序固定为：
1. 先看 `ΔBDEE / ΔCET`（是不是只有早期 guidance acquisition）
2. 再看 `ΔPCST`（是不是只在接触后局部稳一点）
3. 最后看 `ΔPGFR + g^† + s^†`（有没有真的活到 payload-bearing 晚窗）
4. 再判 `SupportFamilyExplanation`
5. 最后才给 `GuidanceSubtractedCeiling`

若某行在第 1-3 步就站不住，则后面 family 解释再漂亮，也不得升格为 `deployable hybrid`。

### 9.10.3 本地锚点的默认 ceiling
- **Find-the-Fruit / decomposition family**：默认只能先解释更强任务准备、遮挡鲁棒性、或间接 `ΔBDEE / ΔCET` 改善；若没有把 gain 推到 `ΔPGFR + W3 + s_p`，只能停在 **decomposition support**。
- **Q2RL / retention family**：默认先解释 `g^†` 延长、W2 carryover 更稳；若 `ΔPGFR` 不改善，只能停在 **retention bridge**。
- **Reactive projection / analytic safety-shell family**：默认先解释 `ΔPCST`；若主要收益只是 safer projection / unsafe-action rejection，而没有把 gain 带到 payload-bearing guidance survival，只能停在 **safety-shell support**。
- **copilot / intervention-hygiene family**：默认只允许先解释 `ΔBDEE` 或早期 `ΔCET`；若没有继续推进 `W3` 与 `ΔPGFR`，只能停在 **intervention-hygiene support**，不得借 smoother correction 抢标题位。

### 9.10.4 当前唯一诚实的标题冻结纪律
只有同时满足以下四项，才允许从 support-family 升到 `deployable hybrid`：
- `ΔPCST` 站住
- `ΔPGFR` 站住
- `g^† = W3`
- `s^† = s_p`

否则，一律冻结到最弱仍成立的那一档：`acceleration / retention bridge / safety-shell support / reward-shaped recovery / decomposition support`。

## 9.11 MobileManiBench 对齐的 verification-first schema（2026-05-26 新增）

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

<<<<<<< HEAD
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
- 本轮高价值扫描命中本地锚点：**MobileManiBench / Find the Fruit / Q2RL / Reactive Dexterous Grasping**
- 正式新增入库：**0 篇**
- D07 下一步不该扩 paper list，而应优先把 `guidance tuple + verification tuple` 真正映射进首轮 bundle 的训练脚本与主表导出逻辑
=======
>>>>>>> 1080f76346ff43cff0d7fb71910b283cdc15be6a
