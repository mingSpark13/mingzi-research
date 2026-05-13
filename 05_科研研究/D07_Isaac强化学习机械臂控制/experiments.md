# D07 experiments

> 最后更新：2026-05-10 | 当前状态：先冻结四行最小实验包，禁止并开 whole-body / tactile / scene-graph / shared-autonomy 扩展

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
