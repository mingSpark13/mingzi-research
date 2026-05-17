# D07_Isaac强化学习机械臂控制 — 主人批注 (Owner Notes)

> 📌 **花火必读**：每次推进 D07_Isaac强化学习机械臂控制 研究前，先读此文件，按最新批注调整 PAPER.md 方向。
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

> 目前暂无批注，等待主人添加。

---

## 📊 花火执行记录

> 花火每次读取此文件后，在此记录已响应的批注（避免重复执行）。

| 日期 | 响应的批注 | 执行动作 |
|------|-----------|---------|
| 2026-05-14 | 无新增批注 | 按默认轮换推进 D07，严格先扫本地 README / PAPER / OWNER_NOTES / experiments，与近 30 天本地锚点（TMRL / Reactive Dexterous Grasping / Q2RL / KG-M3PO / DiSCo / RL vs Optimal Control）；当前会话下 QMD/命令检索受限，故本轮以本地方向文档沉淀为主，未触发 arXiv / Tavily 外扩，也未新增正式入库。补写 PAPER.md 新增首轮真实 bundle 的统一 credit-ledger 与 title-routing 约束，把 retention / projection / reward / exploration / dynamics-set / copilot 六类支持路线正式并入一套 reviewer-facing 记账对象，继续收紧“日志字段 → 主表 → 标题冻结”的写作链路 |
| 2026-05-14 | 无新增批注 | 按默认轮换推进 D07，严格先扫本地 README / PAPER / OWNER_NOTES 与近 30 天 L1 锚点（DiSCo / Reactive Dexterous Grasping / KG-M3PO）；QMD 命中 D07 本地方向文档且本地相关笔记已≥3，因此未触发 arXiv / Tavily 外扩。补写 PAPER.md 4.74-4.75，新增 `\Xi_{D07}` disturbance-localized credit ledger 与最小日志字段契约，把 reward / retention / projection / exploration / dynamics-set / copilot 六类支持路线压成可直接由首轮真实 bundle 日志填表的统一记账对象，继续收紧“实验日志 → 主表 → 标题路由”的论文写作链路 |
| 2026-05-14 | 无新增批注 | 按默认轮换推进 D07，严格先扫本地 README / PAPER / OWNER_NOTES 与近 30 天 L1 锚点（DiSCo / Reactive Dexterous Grasping / KG-M3PO）；QMD 命中 D07 本地方向文档且本地相关笔记已≥3，因此未触发 arXiv / Tavily 外扩。补写 PAPER.md 4.73，新增 `\Omega_{cop}^{D07}` sequence-copilot retention boundary，明确 DiSCo 式序列 copilot 默认只计入 sequence-level data shaping / bounded assistance support，除非同样穿过 W2/W3、payload-bearing 扰动边界并击败 matched weaker family，不能升级成 retention robustness、analytic projection 或 deployable hybrid interface 主张 |
| 2026-05-14 | 无新增批注 | 按默认轮换推进 D07，严格先扫本地 README / PAPER / OWNER_NOTES 与近 30 天 L1 锚点（Reactive Dexterous Grasping / PRISM / RL vs Optimal Control / Zero-Shot Reactive Catching）；QMD 命中 D07 本地方向文档且本地相关笔记已≥3，补做 arXiv 轻扫后仅发现 2605.09789 与当前“高反应 + zero-shot sim2real + uncertainty-set robustness”支线高度相关，但已在本地阅读笔记中存在，故未重复入库。补写 PAPER.md 4.72，新增 `\Omega_{dris}^{D07}` dynamics-set route freeze，明确 DRIS 式多实例随机动力学训练只能先作为 uncertainty-set robustness / reactive zero-shot bridge，除非同样穿过 W2/W3、payload-bearing 扰动边界并击败 matched weaker family，不能升级成 retention、projection 或 deployable hybrid interface 主张 |
| 2026-05-14 | 无新增批注 | 按默认轮换推进 D07，严格先扫本地 README / PAPER / OWNER_NOTES 与近 30 天 L1 锚点（TMRL / Reactive Dexterous Grasping / Q2RL / KG-M3PO / DiSCo）；QMD 再次因 cron 环境被 SIGKILL，未扩 arXiv / Tavily。补写 PAPER.md 4.71，新增 exploration-bridge non-promotion rule，明确 TMRL 式 diffusion-timestep exploration 只能先作为 warm-start/exploration support，除非同样穿过 W2/W3、payload-bearing 扰动边界并击败 matched weaker family，不能升级成 retention robustness 或 deployable interface 主张 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（TMRL / KG-M3PO / DiSCo / Q2RL / Reactive Dexterous Grasping）补写 PAPER.md 4.70，新增 `\Omega_{expl}^{D07}` exploration-bridge freeze，明确 diffusion-timestep exploration 只能先作为 warm-start/retention 路线上的探索桥接证据，除非同样穿过 W2/W3、强扰动边界与 matched-family defeat，不能升级为新控制接口主张 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（KG-M3PO / DiSCo / Q2RL / Reactive Dexterous Grasping）补写 PAPER.md 4.69，新增 `\Gamma_{src}^{D07}` disturbance-source-disambiguation route tag，明确 overlay 回归后必须继续区分 target misalignment / base drift / obstacle conflict / contact instability 四类失败来源，且只有真正推动 W2/W3 + 扰动边界的 overlay 才能影响标题路由 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于 experiments.md 已冻结的四项路由日志字段，补写 PAPER.md 4.68，新增 `\Upsilon_{route}^{D07}` 路由日志契约，把 winner row / earliest positive window / highest disturbance boundary / frozen title route 正式并入论文实验节，统一 PAPER 与可执行实验工作流 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（RL vs Optimal Control / Q2RL / Reactive Dexterous Grasping / ARM）补写 PAPER.md 4.67，新增 RL-versus-optimal-control routing 规则，要求未来最优控制/轨迹优化对照继续服从同一套 `W2/W3 + s_p + matched-family-defeat` 诚实升级闸门 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（KG-M3PO / DiSCo / Reactive Dexterous Grasping / Q2RL / RL vs Optimal Control）补写 PAPER.md 4.56-4.57，新增 overlay freeze 与 `\Omega_{overlay}^{D07}` 规则，明确 semantic-state 与 sequence-copilot 只能在核心四行 bundle 完成 conflict routing、sim2sim 一致性与 fixed-flight→coupled-base 晋级后，作为 support-side overlay 重新介入 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（KG-M3PO / DiSCo / Reactive Dexterous Grasping / ARM）补写 PAPER.md 4.66，新增 disturbance-disambiguation overlay 规则，明确 semantic-state 与 sequence-copilot 只能在四行核心 bundle、reward-retention-projection 冲突裁决、sim2sim 一致性与 fixed-flight→coupled-base 晋级通过后，作为 support-side overlay 解锁 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（RL vs Optimal Control / Squint / Reactive Dexterous Grasping）补写 PAPER.md 4.65，新增 RL-versus-optimal-control routing 规则，要求后续 RL/最优控制对照继续服从同一套 W2/W3、sim2sim、一致性与 coupled-base promotion 闸门 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（DiSCo / KG-M3PO / ARM / Reactive Dexterous Grasping）补写 PAPER.md 4.64，新增 sim2sim-consistent deployment ladder，明确 semantic/shared-autonomy 只能在四行核心 bundle 通过 reward-retention-projection 冲突裁决、Sim2Sim 一致性与 fixed-flight→coupled-base 晋级后再介入 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（KG-M3PO / DiSCo / ARM / Reactive Dexterous Grasping）补写 PAPER.md 4.62-4.63，新增 semantic/shared-autonomy deferred-promotion 与 reward-retention-projection conflict-resolution 规则，继续锁死首轮标题路由边界 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（DiSCo / KG-M3PO / Reactive Dexterous Grasping / Squint）补写 PAPER.md 4.59-4.61，把四行最小实验包、S1→S3 串行协议、smoke-test 完整性门槛正式写进论文实验节，和 experiments.md 执行工作流对齐 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（Q2RL / Reactive Dexterous Grasping / ARM / RL sim-real co-training）补写 PAPER.md 4.57-4.58，新增 retention-versus-projection route freeze 与 dominant-credit freeze，进一步锁死首轮真实 bundle 的标题路由边界 |
| 2026-05-12 | 无新增批注 | 按默认轮换推进 D07，补写 PAPER.md Section 4.8-4.12（semantic-state ablation 后续平台锁定解释规则 / platform-vs-controller 分离模板 / first real bundle 结论冻结） |
| 2026-05-09 | 无新增批注 | 按默认轮换推进 D07，补写 PAPER.md Section 4.8-4.11（semantic-state ablation / window-localized table / first-round go-no-go / reward-origin accountability） |
