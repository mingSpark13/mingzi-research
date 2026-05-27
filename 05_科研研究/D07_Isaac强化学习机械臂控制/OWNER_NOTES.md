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

<<<<<<< HEAD
=======
### [2026-05-26] 核心创新范式确立：机械臂作为高频稳定器
**类型**: 方向调整 + 创新点  
**优先级**: 🔴 立即执行

本方向的根本创新是一条**第三路线**，不是更好的整身控制，也不是更好的分开控制：

**核心主张**：无人机飞控只需保证系统在某一范围内稳定，机械臂凭借自身高频敏捷运动能力主动补偿无人机漂移，在不依赖动捕等外部精确定位的条件下，实现室外可部署的高精度末端跟踪。

**为什么这条路能走通**：传统分开控制精度差，根本原因不是"分开控制"本身，而是没有充分利用机械臂的敏捷性。只要机械臂控制频率高于无人机晃动频率，无人机的低频漂移就可以被机械臂实时补偿掉。

**当前已验证**：5轴机械臂 + 无人机yaw = 等效6轴机械臂，MuJoCo仿真已确认方案可行性。构型上无人机悬停在目标前下方，末端夹爪保持水平朝前，yaw参与联合解算。

**核心挑战**：机械臂敏捷运动策略（优化解算→RL训练）、机械臂侧独立轻量定位、机械臂运动对无人机的反作用扰动控制。

**对 PAPER.md 的引导**：当前论文框架过于通用，需要把"机械臂高频补偿无人机低频漂移"这一物理主张写成论文的核心假设和贡献，整身控制 / 传统分开控制 / 本方案的三路对比应成为 Introduction 的主线。实验核心验证指标应是：在不同无人机漂移幅度下，末端跟踪误差是否保持稳定（解耦曲线）。

---

>>>>>>> 1080f76346ff43cff0d7fb71910b283cdc15be6a
### [2026-05-18] 研究目标论文标题已切换后的章节收束
**类型**: 写作风格  
**优先级**: 🔴 立即执行

既然标题已经切换为 **MEGA: Moving-base End-effector Guidance and Agility for Aerial Manipulation**，后续 D07 的方法与实验写作要更直接围绕 **moving-base end-effector guidance** 展开：
- Method 不再泛写“aerial-arm control stack”，而要明确突出 **base-motion-aware end-effector guidance / contact-stage agility / post-contact stabilization** 三条主线
- Experiments 不再只写一般性的 retention / projection / hybrid 路由，而要补一层 **moving-base guidance-oriented metrics**，例如 base-drift 下末端误差、接触建立时间、接触后稳定时间、payload-bearing 下 guidance 失效率
- 如果某个模块（warm-start、BC-to-Q、projection、copilot）没有实际推动 **moving-base guidance quality**，它就只能作为 support route，不能抢标题叙事

### [2026-05-18] 更换引导研究目标论文标题
**类型**: 方向调整  
**优先级**: 🔴 立即执行

将 D07 PAPER.md 标题更换为 **MEGA: Moving-base End-effector Guidance and Agility for Aerial Manipulation**，以此作为本方向的引导研究目标论文。后续 Heartbeat 推进 PAPER.md 时，围绕 Moving-base 末端执行器引导与空中操作敏捷性这一核心主题展开。

---

## 📊 花火执行记录

> 花火每次读取此文件后，在此记录已响应的批注（避免重复执行）。

| 日期 | 响应的批注 | 执行动作 |
|------|-----------|---------|
<<<<<<< HEAD
| 2026-05-26 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 **MEGA** 标题收束 D07 PAPER 与 experiments：在 PAPER 新增 **3.22 Verification-Shell and Benchmark-Coverage Subtraction Before Guidance Promotion** 与 **3.23 Metric-First Family Rights under the Current Local Anchor Set**，把 **MobileManiBench** 明确冻结为 `verification-support / benchmark-shell` family，并要求任何行先同时提交 guidance tuple `\mathcal{G}_{row}` 与 verification tuple `V_{row}`，再决定是否还能宣称 moving-base guidance 改进；同步在 experiments.md 扩充 **9.11 guidance tuple + verification tuple 联合日志模板**，把 `C_task / C_fail / C_slice / T_build / κ_verify` 映射到训练日志与 submission-ready 主表，进一步防止“只是验证壳更宽、更会暴露失败”被误写成 MEGA guidance-bearing 方法增益。 |
| 2026-05-26 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES / experiments，并回扫近 30 天本地 L1 锚点 **MobileManiBench / Find the Fruit / Q2RL / Reactive Dexterous Grasping**；QMD 检索 `Isaac RL arm control sim-to-real manipulation policy --no-rerank` 仍主要回流 D07 README 与历史 round 记录，未形成需要完整入库的新高价值论文，因此本轮 **高价值扫描命中 4 篇本地锚点，正式新增入库 0 篇**。Phase 2 直接推进 PAPER/experiments 的 verification-first 减法审计，而不是继续扩论文名录。 |
=======
>>>>>>> 1080f76346ff43cff0d7fb71910b283cdc15be6a
| 2026-05-25 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES / REPORT / experiments，并回扫近 30 天本地 L1 锚点 **Bounded ES RL / RFS / Invariant Rewards**；QMD 检索 `Isaac Sim robotic arm reinforcement learning policy training --no-rerank` 仍主要回流 D07 本地方向文档与既有锚点，未形成需要完整入库的新高价值论文，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 继续直接推进 **PAPER.md** 与 **experiments.md**：在 PAPER 新增 **4.107-4.108**，把 `invariant reward` 与 `deployment-time residual steering` 明确冻结为 guidance-first 审计下的 `reward-generalization support / post-contact correction support` 两类解释家族；同时在 experiments.md 扩充 **9.8 guidance-family metric-first routing freeze**，补进这两类 family 的默认首要 guidance 指标与升级上限，进一步要求所有 OOD reward / test-time correction 路线先证明 moving-base guidance quality，不能借“更会纠偏”直接抢占 MEGA 标题叙事。 |
| 2026-05-24 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES，并回扫本地 L1 锚点 **Isaac Lab / Aerial-Manipulator-RL(DSAM) / ViserDex**；补做 QMD 检索 `Isaac Sim manipulation reinforcement learning robot arm policy --no-rerank`，结果继续主要回流 D07 本地方向文档与既有锚点，未形成需要完整入库的新高价值论文，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 继续直接推进 **PAPER.md**：新增 **4.105 Guidance-Metric-First Family Freeze from the Current Local Anchor Set** 与 **4.106 Current Evidence-Consistent Next Step after the Isaac-Lab / ViserDex / DSAM Re-read**，把 `Isaac Lab → infrastructure-hygiene support`、`ViserDex → BDEE-first perception bridge`、`DSAM → PCST/PGFR-first hybrid stabilization` 的 metric-first explanatory rights 正式写进实验路由，进一步把 D07 收束到“先赢对应 guidance metric 上最弱但最自然的解释家族，再谈 MEGA 标题升级”的 reviewer-facing 纪律。 |
| 2026-05-24 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES / experiments 与近 30 天本地 L1 锚点（DiSCo / Reactive Dexterous Grasping / Hand-in-the-Loop / Find the Fruit / Q2RL），并补做 QMD 检索 `Isaac Sim reinforcement learning moving-base end-effector guidance --no-rerank`；结果继续主要回流 D07 本地方向文档、IsaacLab 框架综述与既有 sim2real/RL 锚点，未形成需要完整入库的新高价值论文，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 继续直接推进 **PAPER.md** 与 **experiments.md**：在 PAPER 新增 **4.18 Guidance-Core Metric Attribution from the Current Local Anchor Set**，把 copilot / retention / analytic projection / decomposition 四类 support family 分别冻结到其默认应先解释的 guidance metric（`ΔBDEE / ΔCET / ΔPCST / ΔPGFR`）；同时在 experiments.md 新增 **9.8 guidance-family metric-first routing freeze**，把这套“family 必须先赢下自己最自然但仍最弱的 guidance metric，才允许再谈标题升级”的规则显式映射进实验路由。 |
| 2026-05-23 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES / experiments 与近 30 天本地 L1 锚点（Reactive Dexterous Grasping / Hand-in-the-Loop / Find the Fruit / DiSCo / IsaacLab-Arena），并补做 QMD 检索 `moving-base end-effector guidance aerial manipulation Isaac Lab BC-to-Q reactive projection --no-rerank`；结果仍主要回流 D07 本地方向文档与既有锚点，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 继续直接推进 **PAPER.md**：新增 **4.14 Guidance-Bearing Method Freeze after Re-reading Hand-in-the-Loop and Find-the-Fruit** 与 **4.15 Guidance-First Main Table Bridge from experiments.md to Submission Routing**，把 HandITL 明确冻结为 intervention-hygiene / correction-smoothing support route，把 Find-the-Fruit 明确冻结为 decomposition / uncertainty-exposure support route，并把 submission-facing 主表字段与 `experiments.md` 的 guidance-first 日志映射正式打通，进一步把 D07 收束到 `base-motion-aware end-effector guidance / contact-stage agility / post-contact stabilization under payload-bearing disturbance` 三条 title-bearing 主线 |
| 2026-05-23 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES / experiments 与近 30 天本地 L1 锚点（Reactive Dexterous Grasping / Hand-in-the-Loop / DiSCo），并补做 QMD 检索 `isaac sim reinforcement learning manipulation robot arm --no-rerank`；结果主要回流 D07 本地方向文档、IsaacLab 框架综述与既有 sim2real/RL 锚点，未形成需要完整入库的新高价值论文，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 继续直接推进 **PAPER.md** 与 **experiments.md**：在 PAPER 新增 **4.102 Guidance-Bearing Method Narrowing after Re-reading Reactive Projection and Hand-in-the-Loop**，把方法主叙事进一步冻结为 `base-motion-aware end-effector guidance / contact-stage agility / post-contact stabilization` 三条 title-bearing 路径，并明确 Hand-in-the-Loop 默认只能作为 intervention-hygiene support route，除非实际改善 `ΔBDEE / ΔCET / ΔPCST / ΔPGFR`；同时在 experiments.md 新增 **9.7 guidance-core wording freeze**，把下一轮 D07 写作与主表口径进一步对齐到 MEGA guidance-first 约束 |
| 2026-05-23 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES 与近 30 天本地 L1 锚点（Reactive Dexterous Grasping / Q2RL / DiSCo / Find the Fruit），并补做 QMD 检索 `Isaac Sim reinforcement learning moving-base end-effector guidance --no-rerank`；结果继续主要回流 Isaac Lab 框架综述、Squint source 与 D07 本地方向文档，未形成需要完整入库的新高价值论文，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 直接推进 **PAPER.md** 与 **experiments.md** 的对齐：在 PAPER 新增 **4.97 Guidance-First Logging Bridge from experiments.md to the Submission-Facing Main Table**，把 submission-facing 主表字段固定为 `Method / ΔBDEE / ΔCET / ΔPCST / ΔPGFR / g^+ / g^† / s^† / SupportFamilyExplanation / GuidanceSubtractedCeiling / PromotionBlocker`；同时在 experiments.md 新增 **第9节 MEGA guidance-first 日志字段映射**，把四行最小实验包与这些字段一一对齐，进一步把 D07 从“有 guidance-first 口径”推进到“下一次真实 bundle 能直接导出 submission-ready 主表”的状态 |
| 2026-05-22 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES 与近 30 天本地 L1 锚点（DiSCo / Reactive Dexterous Grasping / KG-M3PO），并补做 QMD 检索 `Isaac Lab arm reinforcement learning manipulation sim2real --no-rerank`；结果继续主要回流 D07 本地方向文档与既有笔记，外部 arXiv 轻扫 `Isaac Lab + aerial manipulation` 结果为 0，未形成需要完整入库的新高价值论文，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 直接推进 **PAPER.md** 的 Experiments：新增 **4.95 Guidance-Led Experiment Logging Schema for the First Trustworthy MEGA Bundle** 与 **4.96 Minimal Submission-Ready Result Paragraph Template under the Guidance Ladder**，把首个可信 bundle 所需的 guidance-first 日志字段（`BDEE / CET / PCST / PGFR / g^+ / g^† / s^† / SupportFamilyExplanation / GuidanceSubtractedCeiling / PromotionBlocker`）和 submission-facing 三句式结果模板正式写进论文草稿，进一步把 D07 从“概念上按 MEGA 收束”推进到“日志与结果段可直接按 moving-base guidance 口径落表与写作” |
| 2026-05-22 | 无新增批注 | 按默认轮换主推进 D07，严格先读 README / PAPER / OWNER_NOTES / experiments 与近 30 天本地 L1 锚点（TMRL / Reactive Dexterous Grasping / Q2RL / KG-M3PO / DiSCo / Find-the-Fruit / Hand-in-the-Loop）；QMD 结果继续主要回流本地方向文档与既有笔记，未形成需要完整入库的新高价值论文，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 直接推进 **PAPER.md** 的实验主体，补写 **4.1 Setup / 4.2 Moving-Base Guidance Metrics / 4.3 First-Round Bundle and Execution Protocol / 4.4 Main Routing Rules**，把 D07 的首轮验证从“泛化的 retention / projection / hybrid 路由”进一步收束成围绕 **base-drift end-effector error、contact-establishment time、post-contact stabilization time、payload-bearing guidance failure rate** 的 guidance-first 实验框架，并明确只有真实提升 `\mathcal{G}_{row}` 的路线才允许抢占 MEGA 标题叙事 |
| 2026-05-22 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER：新增 **4.93 Guidance-Bearing Ceiling after Re-reading HandITL / DiSCo / PRISM / Find-the-Fruit** 与 **4.94 Guidance-First Submission Paragraph Contract**，把 HandITL / DiSCo / PRISM 明确冻结为 `intervention-hygiene / sequence-copilot / instruction-guided refinement` support routes，把 Find-the-Fruit 明确冻结为 `environment-decomposition support route`；并要求后续 submission-facing 结果段必须先报 `ΔBDEE / ΔCET / ΔPCST / ΔPGFR / g^+ / g^† / s^†`，再说明 support-family 解释与 title ceiling，进一步堵住 support-side gain 抢占 MEGA 标题叙事 |

| 2026-05-22 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER：在 **2.10 Limitations** 新增第七条 limitation，明确当前文献仍未分清 guidance-bearing 与 guidance-adjacent gains；并在 Method 新增 **3.20 Moving-Base Guidance Ladder and Support-Route Ceiling**、**3.21 Guidance-Bearing Interpretation of the Current Anchor Set**，把 Q2RL / Reactive Dexterous Grasping / DiSCo 三类本地锚点直接压到 `BDEE / CET / PCST / PGFR` 的 guidance ladder 上，明确 support-side gain 若不推动 moving-base guidance quality 就只能停留在 support route |
| 2026-05-22 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER：新增 **4.89 Guidance-Oriented Method Routing after the Current D07 Anchor Re-read** 与 **4.90 Guidance-Ladder Experiment Freezing Rule for the Next D07 Bundle**，把 Method/Experiments 进一步压到 `base-motion-aware guidance → contact-stage agility → post-contact stabilization` 三条主线，并要求下一轮 bundle 直接按 `BDEE → CET → PCST / PGFR + s_p` 的 guidance ladder 冻结标题升级边界 |
| 2026-05-21 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER：在 Related Work 新增 **2.9 Guidance-Bearing versus Guidance-Adjacent Families under the MEGA Title**，明确 Reactive Dexterous Grasping / DSAM 为 guidance-bearing，而 Q2RL / DiSCo / KG-M3PO / Find the Fruit 默认仅为 guidance-adjacent；并在实验尾部新增 **4.85-4.86**，进一步冻结 guidance-bearing vs guidance-adjacent 的升级边界，要求后续首张可信表必须直接记录 `BDEE / CET / PCST / PGFR` 与 guidance window，未推动 moving-base guidance quality 的路线一律不得占据 MEGA 标题叙事 |
| 2026-05-22 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER：新增 **4.91 Guidance-First Main Table Columns after Re-reading Hand-in-the-Loop and Find-the-Fruit** 与 **4.92 Current Evidence-Consistent Next-Step Priority**，把首张 submission-facing 主表进一步冻结到 `Support-Family Explanation / Guidance-Subtracted Ceiling` 两列，并明确下轮应优先把 `ΔBDEE / ΔCET / ΔPCST / ΔPGFR / g^+ / g^† / Highest Disturbance Source` 等字段映射进 `experiments.md`，先打通 guidance-centric 指标到标题路由的可执行桥接 |
| 2026-05-21 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER 的 Experiments：新增 **4.9 Main Table Schema for Moving-Base Guidance Routing**、**4.10 Guidance-Bearing versus Guidance-Adjacent Support Families**、**4.11 First-Round Honest Promotion Rule under MEGA**、**4.12 Next-Bundle Logging Requirement for Guidance-Centric D07** 与 **4.13 Guidance-Adjacent Transfer Support from Find-the-Fruit-Style Decomposition**，把四行 bundle 的主表字段、promotion blocker、guidance-bearing/support-side 边界正式写死，进一步要求只有真正改善 `BDEE / CET / PCST / PGFR` 且穿过 `s_p` 的路线才可占据 MEGA 标题叙事 |
| 2026-05-20 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER 的 Experiments：新增 **4.13 Find-the-Fruit-Style Decomposition as Guidance-Adjacent Transfer Support** 与 **4.14 Guidance-Centered First-Pass Paragraph Template**，把 Find the Fruit 明确冻结为 **guidance-adjacent transfer support** 家族，并正式写死 reviewer-facing 段落顺序为 `guidance first → family second → title last`，进一步要求任何 transfer / retention / reward / projection 路线若不实际改善 `BDEE / CET / PCST / PGFR`，一律不能占据 MEGA 标题叙事 |
| 2026-05-20 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER 的 Experiments：新增 **4.10 Moving-Base Guidance-Aligned Method Interpretation after Local Re-read**、**4.11 Guidance-Bearing versus Guidance-Adjacent Promotion Rule**、**4.12 Next-Bundle Logging Requirement for `\mathcal{G}_{row}`**，把 Reactive Dexterous Grasping / Q2RL / DiSCo / KG-M3PO / Find the Fruit 等本地锚点统一压回 moving-base guidance 口径，明确凡是不实际改善 `BDEE / CET / PCST / PGFR` 的路线一律冻结为 support route，不能占据 MEGA 标题叙事 |
| 2026-05-20 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER 的 Experiments：补写 **4.10 Moving-Base Guidance-Aligned Method Interpretation after Local Re-read**，把 Reactive Dexterous Grasping / Q2RL / DiSCo / KG-M3PO 等本地锚点重新压回 `BDEE / CET / PCST / PGFR` 四类 moving-base guidance 指标，明确凡是不能实际改善 moving-base guidance quality 的模块，一律只能作为 support route，不能抢标题叙事 |
| 2026-05-19 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已继续按 MEGA 标题收束 D07 PAPER 的 Experiments：把原 **4.7 First-Round Baseline Matrix** 重写为 **4.7 Guidance-Coupled Four-Row Bundle for MEGA**，新增 **4.8 Guidance-Localized Readout Contract**，明确四行 bundle 必须用 `\mathcal{G}_{row}=(ΔBDEE, ΔCET, ΔPCST, ΔPGFR, g^+, g^\dagger)` 证明 moving-base guidance quality，未推动 guidance 的 retention / projection / reward 路线一律冻结为 support route |
| 2026-05-19 | [2026-05-18] 研究目标论文标题已切换后的章节收束 | 已按批注推进 D07 PAPER 的 Experiments 主体：新增 **4.5 Moving-Base End-Effector Guidance Metrics** 与 **4.6 Guidance-Centered Title Routing**，把评测中心正式改写为 `BDEE / CET / PCST / PGFR` 四类 moving-base guidance 指标，并明确 warm-start / BC-to-Q / projection / copilot 若不改善 guidance quality 只能作为 support route |
| 2026-05-18 | [2026-05-18] 更换引导研究目标论文标题 | 已按批注复核 D07 PAPER 标题为 **MEGA: Moving-base End-effector Guidance and Agility for Aerial Manipulation**，并在 PAPER.md 新增 4.83-4.84，把实验节从通用 route ledger 进一步收束到 **moving-base guidance-centric metrics**（base-drift 下末端误差、接触建立时间、接触后稳定时间、payload-bearing guidance failure rate）与 `\mathcal{G}_{MEGA}` / `\tau_{final}^{MEGA}` 约束，明确只有真正推动 moving-base end-effector guidance 的路线才能占据标题叙事 |
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
