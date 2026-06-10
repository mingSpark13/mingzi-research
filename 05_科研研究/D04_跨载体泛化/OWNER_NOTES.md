# D04_跨载体泛化 — 主人批注 (Owner Notes)

> 📌 **花火必读**：每次推进 D04_跨载体泛化 研究前，先读此文件，按最新批注调整 PAPER.md 方向。
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

### [2026-05-27] 推进 Method 3.x 具体技术描述
**类型**: 写作风格
**优先级**: 🟡 下轮执行

D04 的 Related Work 结构健康（真实的方法分类，不是路由规则堆积），核心贡献（geometry-first 跨载体迁移协议）独立有价值。主要问题是 Method 的具体技术描述还不够完整。

**执行要求**：
1. **禁止**在 Related Work 下继续新增子章节，现有 2.1-2.11 已足够
2. 本轮及后续轮次的 80% 精力集中在 **Method 3.x**：
   - **3.1 Geometry-First Transfer Protocol**：具体写出 shared geometry packet 的数据结构定义，以及 geometry verification 的判断条件（公式层面）
   - **3.2 Geometry-Conditioned Latent Action Retargeting**：具体写出 latent action 重定向的网络架构和训练目标
   - **3.3 In-Context Embodiment Residual Modeling**：具体写出在线载体上下文推断的机制
   - **3.4 Escalation Rule**：将现有文字描述的升级规则转化为可执行的算法步骤
3. 当 Method 各子章节完成后，再写 Abstract
4. 每轮推进后同步更新头部 `最后更新` 字段

---

## 📊 花火执行记录

> 花火每次读取此文件后，在此记录已响应的批注（避免重复执行）。

| 日期 | 响应的批注 | 执行动作 |
|------|-----------|---------|
| 2026-06-10 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 的实验章节：基于本地近30天锚点 **Any2Any / RIO / Human2Humanoid** 与 QMD 复核，在 `PAPER.md` 中实质补写 **4.1 Setup / 4.2 Main Results / 4.3 Ablation Study**，把 `Human2Humanoid` 冻结为 unpaired geometry-anchor control，把 `Any2Any` 冻结为 kinematic-alignment + tiny-PEFT bounded-adaptation control，把 `RIO` 冻结为 representation/infrastructure exposure control，并定义 `\mathcal{B}^{D04}`、`\mathcal{A}^{D04}` 与三类 canonical rows，明确 D04 结果只有在这些更弱解释都被 matched subtraction 后才允许晋升为 shared latent sufficiency 或 remaining embodiment structure；同步更新 PAPER 头部时间戳 |
| 2026-06-08 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：基于本地近30天锚点 **D-CLING / Human-Robot Copilot / RIO / Any2Any / Human2Humanoid** 与 QMD 复核，在 **3.14 Data-First Interface Formation** 中压实 `\mathcal{D}_t=(K_t^{align},G_t^{map},A_t^{sens},\rho_t,\phi_t)` 与 `\Omega_t=(KAG,DAG,RIG,LTS,HRS,CW,PC,PB_{lat})` 的弱解释边界；同时首次补出 **4.1-4.3 Experiments** 骨架与 `\Upsilon_{row}^{D04}` 主表字段，把 *kinematic alignment / tiny PEFT dynamics patch* 明确冻结为 alignment-support 或 bounded-adaptation-support，避免被过早晋升为 shared latent sufficiency；同步更新 PAPER 头部时间戳 |
| 2026-06-08 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：基于本地近30天锚点 **Human2Humanoid / Any2Any / RIO** 回扫与 QMD 复核，在 **3.14 Data-First Interface Formation** 中补写 `\mathcal{D}_t=(K_t^{align},G_t^{map},A_t^{sens},\rho_t,\phi_t)` 与 `\Omega_t=(KAG,DAG,RIG,LTS,HRS,CW,PC,PB_{lat})`，把 **显式运动学对齐 + 小规模 PEFT 动力学补丁** 明确冻结为 *kinematic-alignment gain / bounded dynamics-adaptation gain*，避免 Any2Any 式路线被过早升格为 shared latent sufficiency；同步更新 PAPER 头部时间戳 |
| 2026-06-07 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：在 **3.12 Human-to-Humanoid Geometry Anchors** 之后新增 **3.13 Family-Matched Unified-Latent Survival after Human-Anchor Subtraction**，写入 `\Lambda_t^{hum}=(UGA,PEC,MIE,RIG,BPA,IEC,LTS,HRS^{lat},CW,PC,PB_{hum-lat})`，把 Human2Humanoid 的无配对锚点监督与 RIO / D-CLING / AdaTracker 三类更弱解释一起压进 shared-latent 晋升门槛；原 **Data-First Interface Formation** 顺延为 **3.14**，并同步更新 PAPER 头部时间戳 |
| 2026-06-07 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：将 **Human2Humanoid (2606.03476)** 正式固化进 **3.12 Human-to-Humanoid Geometry Anchors without Paired Demonstrations**，写入 `\Psi_t=(UGA,PEC,MIE,LTS,HRS^{hum},CW,PC)`，把无配对 human→humanoid 增益严格拆成 unpaired geometry-anchor / physics-executability / morphology-invariant end-effector alignment 三类上游监督来源；同时清理重复编号，把后续 **Data-First Interface Formation** 顺延为 **3.13**，并同步更新 PAPER 头部时间戳 |
| 2026-06-06 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：在 **3.10** 后新增 **3.11 Unified-Prior Saturation and Context-Conditioned Latent Survival**，把 **JoyAI-RA 0.1** 形式化为 `\Sigma_t=(FPC, IEC, LTS, HRS^{sat}, CW, PC, PB_{sat})` 的强先验饱和阻断器；同时补强 **3.10**，把 **Human-Robot Copilot** 明确并入 `\Lambda_t` 的 bounded supervision 路线，要求 shared-latent claim 必须同时击败 online embodiment-context、prior-preserving bounded adaptation 与 sparse copilot support；同步更新 PAPER 头部时间戳 |
| 2026-06-05 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：新增 **3.11 Human-to-Humanoid Geometry Anchors without Paired Demonstrations**，把 **Human2Humanoid** 的 skeleton-aware 几何锚、morphology-invariant 末端一致性与 physics-aware feasibility 正式压进 `\Psi_t=(UGA,PEC,MIE,LTS,HRS^{hum},CW,PC)`，明确无配对 human→humanoid 增益必须先冻结为 unpaired geometry-supervision / physics-aware retargeting support，再决定是否晋升为 shared latent sufficiency；同步更新 PAPER 头部时间戳 |
| 2026-06-04 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：补强 **3.10 Family-Matched Shared-Latent Survival after In-Context Embodiment Inference**，把 **AdaTracker** 的 embodiment-context inference、**D-CLING** 的 bounded adaptation、**RIO** 的 representation exposure 与 **VistaBot** 的 cross-view packet repair 一起压进 `\Lambda_t=(LTS,IEC,BPA,BSC,HRS^{ctx},CW,PC,PB_{ctx})`，明确 shared-latent claim 必须先击败 context-conditioned explanation 再能晋升；同步更新 PAPER 头部时间戳 |
| 2026-06-04 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：新增 **3.10 Family-Matched Shared-Latent Survival after In-Context Embodiment Inference**，把 AdaTracker 的在线载体上下文推断、D-CLING 的 bounded adaptation、Human-Robot Copilot 的 bounded supervision 一起压成 `\Lambda_t=(LTS,IEC,BPA,BSC,HRS^{ctx},CW,PC,PB_{ctx})`，明确 shared latent claim 只有在 context-conditioned explanation 也被扣除后才允许晋升；同步更新 PAPER 头部时间戳 |
| 2026-06-03 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：在原 3.10 前插入 shared-latent promotion blocker `Ω_t=(KAG,DAG,RIG,LTS,HRS,CW,PC,PB_lat)`，把 kinematic alignment / 轻量 PEFT dynamics adapter / representation exposure 与真正的 latent-transition sufficiency 分开；并新增 family-matched specialist blocker `Ξ_t=(RIG,BPA,BSC,LTS,SRS,CW,PC,PB)`，用 D-CLING / Human-Robot Copilot / specialist distillation 三类本地锚点压实 specialist 晋升门槛；同步更新 PAPER 头部时间戳 |
| 2026-06-01 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：在 3.8 specialist promotion blocker 之后新增 shared-latent promotion blocker `Ω_t=(KAG,DAG,RIG,LTS,HRS,CW,PC,PB_lat)`，用 Any2Any / RIO / 轻量 PEFT 适配三类证据把“kinematic alignment + tiny adaptation”与真正的 shared latent sufficiency 分开；同步更新 PAPER 头部时间戳 |
| 2026-06-01 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：在 3.7 后新增 family-matched specialist promotion blocker，形式化 `Ξ_t=(RIG,BPA,BSC,LTS,SRS,CW,PC,PB)` 与 `SRS > max(BPA,BSC)+τ_spec` 的晋升条件，把 D-CLING / Human-Robot Copilot / specialist distillation 三类本地锚点压成可执行的 weakest-honest subtraction 规则；同步更新 PAPER 头部时间戳 |

| 2026-05-28 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：细化 3.3 latent retargeting 的 token 化架构与训练目标，补写 3.5 in-context residual 的双分支机制与路由损失，重写 3.7 escalation 为可执行 shortest-honest algorithm，并同步更新时间戳；本轮本地扫描命中 RIO / Human-Robot Copilot / D-CLING / Any2Any / OPFA，无新增正式入库 |
| 2026-05-28 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 主推进 D04 Method 3.x：重写 3.1 几何包与验证判据、3.3 latent retargeting 架构与目标、3.5 context residual 机制、3.7 escalation algorithm；同步更新 PAPER 头部日期 |
