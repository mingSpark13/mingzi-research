# D04 跨载体泛化 experiments

> 最后更新：2026-04-21 R884
> 目的：把 D04 首轮验证从“路线很多”压成“先排哪一层收益归属”，并明确首个主任务与两周执行包。

## 0. 本轮实验假设

- **H1 几何先验先于载体补偿**：如果 `human geometry anchor + 少量空中锚点` 在 L1 都站不稳，后面再堆 latent / specialist / physics adapter 都是在补错层。
- **H2 specialist 不是默认主线**：只有当 `shared+specialist head` 相对 `shared+adapter` 的收益稳定超过 3pp，且校准成本不过高时，specialist 才值得保留。
- **H3 physics adapter 主要解决 DRB**：如果主要掉点出现在 `L2 → L3`，优先怀疑动力学残差，而不是继续追加 paired data。
- **H4 壳层收益必须拆账**：若固定共享 planner/latent 后 `controller shell` 贡献过高，论文叙事必须改写为“D04 主干 + D06/D07 壳层协同”。

## 1. 首轮 sanity check 总览

| 编号 | 对应层 | 目标 | 最小对照 | 主指标 | 判停/放行 |
|---|---|---|---|---|---|
| **SC0** | 几何表征层 | 验证 3D backbone + PMI Packet 是否先把 `task_geometry_state` 学稳 | `2D encoder` vs `R3D 3D encoder`，统一输出 `PMI Packet` | `PGS`, 几何状态方差, packet 字段完整率 | 若 `PGS` 不稳，禁止进入 SC1 |
| **SC1** | 几何层 | 验证 human geometry anchor 是否真提升 pre-contact 几何质量 | `纯20条空中锚点` vs `human几何演示 + 20条空中锚点` | `L1 SR`, 接近位姿误差, `GTG` | 若 `L1 SR < 85%`，停止后续所有结构对照 |
| **SC2** | 形态层 | 判断 specialist head 是否真优于轻量 adapter / latent retarget | `shared+adapter` vs `shared+specialist head` vs `latent retarget` | `L2 SR`, `MCG`, 参数增量, 校准时间 | 若 `MCG < 3pp`，specialist 不进主线 |
| **SC3** | 动力学层 | 判断 physics adapter 是否是刚需，而不是可选补件 | `SC2最佳路线` vs `+physics adapter` | `DRB`, payload 条件成功率, recovery time | 若 DRB 大，优先保留 physics adapter |
| **SC4** | 壳层层 | 拆清 D04 主干收益与 D06/D07 壳层收益 | 固定共享 planner/latent，比 `direct execution` vs `controller shell` | `SDR`, controller regret, recovery gain | 若 `SDR > 0.5`，主文必须显式写协同关系 |

## 2. 实验执行顺序

### SC0. Perception-to-Geometry stability sanity
- **任务**：L0 几何表征，只输出 `PMI Packet`，不进入抓取控制。
- **对照**：
  - A组：2D encoder + 轻量 pose head
  - B组：R3D 3D encoder + 同等容量 head
- **统一输出字段**：`task_geometry_state / contact_affordance / phase_token / capability_bound`
- **记录**：
  - `PGS`
  - 几何状态方差（不同视角/轻微观测扰动下）
  - packet 字段完整率
- **目标**：先确认几何接口本身稳定，再进入 SC1，不把 backbone 问题误写成跨载体共享问题。

### SC1. Human geometry anchor sanity
- **任务**：L1 几何接近，只预测 pre-grasp / pre-contact pose，不执行闭环抓取。
- **数据**：
  - A组：纯 20 条空中载体锚点。
  - B组：human geometry 演示 + 同样 20 条空中载体锚点。
- **记录**：
  - `L1 SR`
  - 接近位姿平移/姿态误差
  - `GTG = L1 SR - L2 SR`（先只占位）
- **目标**：先验证人类/地面几何先验是不是高杠杆来源。

### SC2. Shared vs specialist vs latent retarget
- **任务**：L2 准静态抓取/放置。
- **固定项**：paired 数据预算先固定为 50 条；共享语义/视觉主干一致。
- **对照**：
  1. `shared + adapter`
  2. `shared + specialist head`
  3. `latent retarget`
- **记录**：
  - `L2 SR`
  - `MCG`
  - 参数增量
  - 校准时间
- **目标**：先判断“载体专属补偿”到底应落在 adapter、specialist 还是 latent 映射层。

### SC3. Physics adapter necessity check
- **任务**：L3 空中弱扰动抓取。
- **对照**：
  - `SC2 最佳路线`
  - `SC2 最佳路线 + physics adapter`
- **记录**：
  - `DRB = L2 SR - L3 SR`
  - payload / 弱扰动条件成功率
  - recovery time
- **目标**：确认 AirVLA / Hardware-Agnostic QuadWM 提醒的“动力学补偿层”是不是主瓶颈。

### SC4. Shell dependency accounting
- **任务**：L3/L4 共享高层目标不变，仅替换执行壳层。
- **对照**：
  - `direct execution`
  - `controller shell / recovery shell`
- **记录**：
  - `SDR`
  - controller regret
  - recovery gain
- **目标**：防止把 controller shell 的收益夸写成 D04 跨载体共享能力。

## 3. 首轮统一记录模板

每次实验至少记下面 9 项：

1. `split`：S1 / S2 / S3
2. `stage`：L0 / L1 / L2 / L3 / L4
3. `route`：2D / R3D / shared+adapter / specialist / latent retarget / physics adapter / shell
4. `data budget`：paired 条数 + 目标载体锚点条数 + 是否含 human geometry
5. `SR`（L0 可记 N/A）
6. `PGS / GTG / MCG / DRB / SDR`（未涉及项可记 N/A）
7. `校准时间 / GPU小时 / 参数增量`
8. `PMI Packet 完整率`：关键字段是否齐全、是否可验
9. `失败归因`：L-G / L-M / L-D / L-S

## 4. 当前放行规则

- **先过 SC0，再做 SC1**。几何接口不稳时，不讨论 human anchor 和 specialist 有没有用。
- **若 PGS 不稳或 PMI Packet 字段缺失率高，优先修 3D backbone / 字段定义，不进入任何跨载体对照。**
- **先过 SC1，再做 SC2**。几何层不稳时，不讨论 specialist 有没有用。
- **SC2 只要 MCG 连续偏低，就收缩 specialist 路线**，避免继续在载体专属头上浪费预算。
- **SC3 一旦显示 DRB 高，优先把资源转给 physics adapter / payload-aware guidance**。
- **SC4 若 SDR 高于 0.5，D04 后续结论必须改成“共享主干 + 部署壳层协同”**。

## 5. 两周执行包（R818）

### Week 1, 先把主任务锁死
- **主任务**：`T1 静态单物体接近→抓取→抬升10cm`
- **不做**：导航串联、连续多物体、多阶段长任务
- **目标**：先拿到 `SC1 + SC2` 第一版结果，确认几何先验和 specialist 路线到底值不值

### Week 1 必交付
1. `T1` 仿真脚本固定版（目标物体、起始位姿扰动范围、抬升成功判据）
2. `2D encoder` vs `R3D 3D encoder` 的 SC0 对照，至少拿到 `PGS + PMI Packet 完整率`
3. `纯20条空中锚点` vs `human几何演示 + 20条空中锚点` 的 SC1 对照
4. `shared+adapter / shared+specialist head / latent retarget` 的 SC2 对照
5. 统一结果表，至少包含：`PGS / L1 SR / L2 SR / GTG / MCG / 参数增量 / 校准时间`

### Week 2 必交付
1. 在 W1 最优路线之上叠 `physics adapter` 或 `payload-aware guidance`
2. 跑 SC3, 记录 `DRB / recovery time / payload条件成功率`
3. 跑 SC4, 记录 `SDR / controller regret / recovery gain`
4. 给出一句明确结论：当前 D04 的高杠杆补偿层更像 `specialist`、`physics adapter`，还是 `deployment shell`

## 6. 首轮读数判定卡（R822）

为避免 Week 1 跑完后仍然只得到“看起来都还行”的模糊结论，本轮把四个核心指标直接绑定到路线决策：

| 指标 | 阈值 | 默认判断 | 下一步 |
|---|---|---|---|
| `GTG` | `> 20pp` | 几何层没站稳 | 停止 SC2/SC3，先回修 human geometry anchor / task geometry state |
| `MCG` | `< 3pp` | specialist 收益不够 | specialist 出主线，保留 shared+adapter / latent retarget |
| `DRB` | `> 20pp` | 动力学残差主导 | SC3 后优先保留 physics adapter / payload-aware guidance |
| `SDR` | `> 0.5` | 壳层收益过高 | 论文叙事改写为 D04 主干 + D06/D07 壳层协同 |

### 6.1 Week 1 最低验收输出
1. `SC0` 必须给出 `PGS + 几何状态方差 + PMI Packet 完整率`。
2. `SC1` 必须给出 `L1 SR + 接近位姿误差 + GTG占位`。
3. `SC2` 必须给出 `L2 SR + MCG + 参数增量 + 校准时间`。
4. 若 `latent retarget` 已接近 `shared+specialist head`，默认优先保留更轻路线，不主动放大 specialist。

### 6.2 Week 2 最低验收输出
1. `SC3` 必须给出 `DRB + payload条件成功率 + recovery time`。
2. `SC4` 必须给出 `SDR + controller regret + recovery gain`。
3. 只要 `DRB` 与 `SDR` 同时偏高，后续结论就不再写成“D04 单独解决跨载体”，而写成“共享主干 + 部署壳层协同”。

## 6.3 首轮判线后继动作表（R826新增）

在 `GTG / MCG / DRB / SDR` 四项阈值之外，还需要把**指标组合**直接映射到下一轮资源收缩策略，否则首轮结果出来后仍可能陷入“每条线都想再补一点”的拖延。为此新增下面这张后继动作表：

| 读数组合 | 结论 | 下一轮资源动作 | 论文叙事动作 |
|---|---|---|---|
| `GTG高` + 其余暂未显著 | 共享几何层未站稳，后续比较均无效 | 停止 SC2/SC3/SC4 扩展；只回修 `R3D / PMI Packet / human geometry anchor` | 主文暂不宣称跨载体共享成立，只写接口稳定性问题 |
| `GTG低` + `MCG低` + `DRB高` | geometry 够用，但 morphology 补偿不是主瓶颈，动力学才是主导 | specialist 收缩为对照支线；优先投入 physics adapter / payload-aware guidance | 主文把主补偿层写成 `shared backbone + physics adapter` |
| `GTG低` + `MCG高` + `DRB低` | 形态补偿已足够解释大部分收益，动力学不是首要障碍 | 保留 specialist / morphology token 主线；physics adapter 降为补充实验 | 主文主线偏向 `shared geometry + morphology compensation` |
| `GTG低` + `MCG低` + `DRB低` + `SDR高` | D04 主干收益有限，部署壳层在主导结果 | 冻结 D04 继续扩模型；转向 D06/D07 shell 协同实验 | 主文必须改写为“共享主干 + shell 协同”，避免夸大 D04 |
| `GTG低` + `MCG中高` + `DRB中高` | 形态层与动力学层都在起作用 | 保留双路径：specialist / morphology token 与 physics adapter 并行，但先压缩到单任务单物体 | 主文写成双补偿层串联，不提前宣称单一路线胜出 |

### 6.4 与本地方向锚点的角色对齐（R828新增）

结合本地方向里已吸收的 **R3D / PMI-style interface / HEX / Unified Latent Space / AirVLA / Hardware-Agnostic QuadWM**，四类代表工作的角色现在可以进一步钉死，避免后续引用时混账：

- **R3D / PMI-style geometry interface**：主要回答 `GTG`，即共享几何接口和 `PMI Packet` 是否先站稳；这一类如果没过，不允许 specialist / physics adapter 抢预算。
- **HEX / morphology-aware 系**：主要回答 `MCG`，即高 DoF 协同与形态补偿是否值得保留为主补偿层。
- **Unified Latent Space / OPFA 系**：主要回答共享几何与 latent 统一是否足够撑起 `shared backbone`，是 `GTG/MCG` 的中间支撑位。
- **AirVLA 系**：主要回答 `DRB`，即当视觉与任务几何已可迁移时，推理时动力学修补是否能低成本补上 aerial dynamics gap。
- **Hardware-Agnostic QuadWM / physics adapter 系**：主要回答 `DRB` 在更广义 morphology-conditioned dynamics adapter 视角下是否应升级为长期主线。
- **D06/D07 controller shell**：主要回答 `SDR`，只负责解释部署层收益，不与 D04 主干创新抢“是谁解决了跨载体主问题”的记账。

这意味着 D04 下轮即使不新增论文，也已经足够按“**几何 → 形态 → 动力学 → 壳层**”四段做主线收缩，不再需要靠继续扩候选论文来获得方向感。

## 6.5 首轮主补偿层选择卡（R828新增）

为了避免 Week 1/2 跑完之后仍然出现“每条线都还想再补一点”的拖延，本轮把结果直接映射成下一轮优先预算对象：

| 结果模式 | 默认主补偿层 | 下一轮先做什么 | 暂缓什么 |
|---|---|---|---|
| `GTG高` | 无（先修共享几何层） | 只修 `R3D / PMI Packet / human geometry anchor` | 暂缓 `specialist / physics adapter / shell` 扩展 |
| `GTG低 + MCG高 + DRB低` | 形态补偿层 | 先压实 `shared+specialist / morphology token` 的复现稳定性 | physics adapter 降为补充验证 |
| `GTG低 + MCG低 + DRB高` | 动力学补偿层 | 先压实 `physics adapter / payload-aware guidance`，把 `DRB` 压到黄色区以下 | specialist 收缩为对照支线 |
| `GTG低 + MCG中高 + DRB中高` | 先动力学，后形态 | 先收敛弱扰动与 payload 条件下的 `DRB`，再回看 `MCG` | 不扩任务宽度，不先做 shell 优化 |
| `GTG低 + MCG高 + DRB高` | 双补偿并存，但只锁单任务 | 在 `T1` 上并行保留 `specialist + physics adapter`，禁止扩到长链任务 | 暂缓 D06 式 planner 扩展 |
| `GTG低 + MCG低 + DRB低 + SDR高` | 部署壳层 | 冻结 D04 主干扩展，把资源转给 D06/D07 shell 协同 | 暂缓 shared backbone 结构改造 |

**默认优先级**：`几何层 > 动力学层 > 形态层 > 壳层表述`。
只要几何接口没站稳，后面都不许抢预算；而在空中载体场景里，只要 `DRB` 与 `MCG` 同时高，默认先处理动力学层，因为它更接近真机不可执行风险。

## 6.6 首轮预算冻结协议（R837新增）

在已有 `GTG / MCG / DRB / SDR` 判线与主补偿层选择卡之外，本轮继续把 D04 的执行策略从“知道该先修哪层”推进到 **结果一出来就冻结哪些层、避免预算继续平均摊**。因为当前最容易浪费 GPU/工时的，不是判断错一次，而是首轮已经给出明显信号后，geometry / specialist / physics adapter / shell 四层还都想再补一点。

| 首轮主读数 | 默认冻结动作 | 允许继续拿预算的层 | 说明 |
|---|---|---|---|
| `PGS` 不稳 / `PMI Packet` 完整率低 | **冻结 SC1-SC4** | 仅 `R3D / PMI Packet / 几何字段定义` | 几何接口没站稳前，后续所有跨载体收益都不应记账 |
| `GTG` 仍高 | **冻结 specialist / physics adapter / shell 扩展** | 仅 `human geometry anchor / R3D 3D encoder` | 先把共享任务几何站稳，不允许把掉点误写成补偿层问题 |
| `GTG` 低、`MCG < 3pp` | **冻结 specialist 主线** | `shared+adapter / latent retarget / physics adapter` | 形态专属头收益不足时，不再继续烧预算追求微弱提升 |
| `GTG` 低、`DRB` 高 | **冻结新的 specialist 变体** | `physics adapter / payload-aware guidance` | 空中场景里动力学残差优先级更高，先压执行风险 |
| `GTG/MCG/DRB` 都不高、但 `SDR` 高 | **冻结 D04 主干扩模** | `D06/D07 shell 协同` | 主收益已落到部署壳层，D04 不应再夸写成单独主解 |
| `MCG` 与 `DRB` 同时中高 | **冻结任务宽度扩张** | 保留单任务上的 `specialist + physics adapter` 双线 | 先在 `T1` 锁住谁主谁辅，再谈长链任务 |

## 6.8 首轮唯一解释路径（R884新增）

在 `IG0 / SC0 / GTG / MCG / DRB / SDR` 都已经被逐步写进协议后，本轮继续把 D04 的结果解释压成**唯一决策树**，避免后续同一批结果被反复改写成 geometry gain、latent gain、morphology gain、dynamics gain 四种说法。

### 6.8.1 唯一决策顺序

1. **先判 IG0**
   - 若 `IFR / ICS / DMS` 任一不稳，所有结果统一收成 **shared geometry interface not yet established**。
   - 此时禁止讨论 latent sufficiency、specialist 或 physics adapter。

2. **再判 SC0 / 几何层**
   - 只有 `IG0` 通过后，才看 `PGS / PMI Packet 完整率 / 几何状态方差`。
   - 若 `SC0` 不过，统一收成 **geometry bottleneck**，继续只修 `R3D / PMI Packet / geometry field definition`。

3. **再判 GTG**
   - 若 `IG0 + SC0` 通过，但 `GTG` 仍高，说明 shared geometry 已基本成立但接近阶段仍未稳，当前主结论仍是 **geometry bottleneck**，不允许提前把收益写给 specialist 或 dynamics adapter。

4. **再判 MCG**
   - 若 shared geometry 已稳且 `GTG` 明显下降，同时 `MCG < 3pp`，默认解释为 **shared geometry + latent sufficiency**。
   - 只有 `MCG` 连续占优并超过阈值，才允许进入 *embodiment-aware compensation* 解释。

5. **最后判 DRB / SDR**
   - 若 `DRB` 高，则自动改写为 **shared geometry + dynamics adaptation bottleneck**，优先保留 physics adapter / payload-aware guidance。
   - 若 `DRB` 不高但 `SDR` 高，则主文必须改写为 **shared backbone + deployment shell collaboration**，禁止把壳层收益记到账到 D04 主干。

### 6.8.2 证据归位最终冻结

- **R3D / PointBridge / DeFM / GaussFly**：只负责 geometry / representation 过线证据
- **Unified Latent Space / LAD**：只在 shared geometry 已过线后解释 latent sufficiency
- **HEX / morphology-aware specialist**：只在 `MCG` 连续占优时进入主文核心段
- **RAFL / AirVLA / Hardware-Agnostic QuadWM**：只负责 dynamics residual / physics adapter 解释
- **CAPO**：只作为 domain-factor suppression 支线，不再跨段抢主叙事
- **D06/D07 shell**：只负责 `SDR` 与部署协同解释，不参与 D04 主干创新记账

### 6.8.3 使用规则

- 同一轮结果只能沿这棵树收成 **一个主结论**。
- 不允许在 geometry 未过线时讨论 latent sufficiency。
- 不允许在 `MCG < 3pp` 时继续保留 specialist 主线。
- 不允许在 `DRB` 高时把主叙事写成 morphology compensation。
- 不允许在 `SDR` 高时继续宣称 D04 单独解决了跨载体问题。

结合本轮回扫的 **CAPO / PointBridge / DeFM / PMI跨躯体意图接口**，首轮实验顺序还需要再收紧一层：**先验证共享意图接口是不是稳定，再讨论任何补偿层是否有效。** 否则 `specialist / latent retarget / physics adapter` 很容易只是在给不稳定输入擦屁股。

### 6.7.1 新增首轮前置门：Interface Gate（IG0）

在进入 `SC0` 之前，先做一个更轻的接口烟测 `IG0`：
- **输入扰动**：视角轻偏移、FOV变化、光照变化、轻微遮挡、深度噪声
- **检查字段**：
  - `task_geometry_state`
  - `contact_affordance`
  - `phase_token`
  - `capability_bound`
  - `verification_tag`
- **必记指标**：
  - `IFR (Interface Field Recall)`：关键字段非空且语义正确的比例
  - `ICS (Interface Consistency Score)`：同任务不同观测下 packet 字段一致性
  - `DMS (Domain-Mixing Score)`：domain factor 变化对 packet 核心字段的扰动幅度

### 6.7.2 IG0 的放行规则
- 若 `IFR < 0.95`：说明 packet 字段定义本身还没收紧，先修字段 schema，禁止进入 SC0。
- 若 `ICS < 0.90`：说明共享意图接口还不稳定，优先回修 `R3D / PointBridge / task_geometry_state`，禁止进入 SC1-SC4。
- 若 `DMS` 偏高：优先怀疑 **CAPO / domain-factor suppression** 是否该作为 geometry 前置清洗支线，而不是提前讨论 specialist 或 physics adapter。

### 6.7.3 Geometry-first 证据归位规则
为防止不同论文证据继续混段，新增一条固定归位：
- **GaussFly / PointBridge / DeFM**：只允许作为 `shared geometry / representation bridge` 过线证据；
- **RAFL**：只允许作为 `dynamics residual` 证据；
- **CAPO**：只允许作为 `domain-factor suppression / interface cleaning` 支线证据；
- **Unified Latent Space / LAD**：只允许在 shared geometry 已过线后，解释 `shared latent sufficiency`。

### 6.7.4 新的默认解释顺序（R882）
在 `IG0 + SC0` 都通过后，D04 默认只按下面顺序解释首轮结果：
1. **shared geometry 是否成立**：若 `IFR / ICS / PGS / PMI Packet 完整率` 任何一项不稳，正文与汇报只能收成 `shared geometry interface not yet established`；
2. **shared latent 是否已足够**：若 shared geometry 已稳，且 `GTG` 下降、`MCG < 3pp`，默认收成 `shared geometry + latent sufficiency`；
3. **morphology compensation 是否真有必要**：只有 `MCG` 连续占优且 `DRB` 不主导时，才允许升格为 `embodiment-aware compensation`；
4. **dynamics gap 是否才是主残差**：若 `DRB` 高，则默认把主文后半改写成 `shared geometry + dynamics adaptation bottleneck`。

### 6.7.5 R882 本轮收束
- 本轮本地回扫重点命中：`GaussFly / CAPO / RAFL / Unified Latent Space / LAD / AirVLA / R3D`。
- QMD 结果继续主要回流本地既有材料，说明 D04 当前在“shared geometry → latent sufficiency → morphology/dynamics residual”链路上的本地增量已接近饱和。
- 外部 arXiv 补扫高位结果仍是 **OneVL / XEmbodied / DESPITE safety**，与 D04 当前主线贴合度不足，因此 **高价值新论文 0 篇，新增入库 0 篇**。
- 因此本轮不扩论文地图，直接把实验侧与报告侧进一步冻结到 **IG0 → SC0 → shared latent sufficiency → morphology/dynamics residual** 这一条解释链，避免后续继续把 representation gain、latent gain、residual gain 混写在一层。


### 6.7.2 Interface Gate 放行规则

| 条件 | 结论 | 后续动作 |
|---|---|---|
| `IFR < 0.95` | 接口字段不完整 | 先修 packet schema / parser / 感知字段，不进 SC0 |
| `ICS` 明显波动 | 共享意图接口不稳定 | 先修 3D/depth 表征与字段定义，不进 SC1 |
| `DMS` 偏高 | domain factor 混入共享意图 | 先加 domain prompt / 视角解耦 / depth grounding，不进补偿层对照 |
| 三项都过线 | 共享接口基本可信 | 允许进入 `SC0 → SC1 → SC2` |

### 6.7.3 对应到本地方向材料的角色分工

- **CAPO**：主要提醒 `DMS` 不能忽视，若视角/FOV/光照变化持续扰动 packet，说明问题仍在 domain disentangling，而不是 embodiment compensation。
- **PointBridge**：主要支撑 `ICS`，即 3D 几何表征能否把跨域差异压到共享几何之外。
- **DeFM**：主要支撑深度/几何先验对 `IFR + ICS` 的提升，尤其适合做 sim-to-real 与跨平台不变表征底座。
- **PMI 接口**：给 `IG0` 提供字段真源与验证边界，避免共享主干与执行壳层再次混账。

### 6.7.4 新的默认执行顺序

从本轮开始，D04 默认顺序改成：
`IG0 接口烟测 → SC0 几何表征 → SC1 human geometry anchor → SC2 形态补偿 → SC3 动力学补偿 → SC4 壳层拆账`

只要 `IG0` 或 `SC0` 没过，后面所有“谁更强”的比较都不成立。

### 6.7.5 本轮最小结论

D04 当前最值钱的已不是再补一条新路线，而是尽快拿到 **`IFR / ICS / DMS / PGS`** 这一组首轮硬读数。只要这组数还没出来，就不该继续扩大 specialist、physics adapter 或 shell 的篇幅。

### 6.7.5 本轮新增主判断（R877）

- 本地近 30 天锚点已覆盖 **PointBridge / DeFM / R3D / AirVLA / Unified Latent Space / CeRLP / CAPO / RAFL**，QMD 继续主要回流 D04 既有主文与概念页，说明当前增量已经不在“再补哪篇论文”，而在**把 IG0→SC0→SC3 的判线顺序彻底写死**。
- 新补的 **RAFL (2603.22039)** 虽然是软体机器人 sim-to-real，但它把 **共享 residual acceleration field** 明确成可迁移动力学桥接层，更适合被吸收到 `SC3 physics adapter` 解释位，而不是改写 D04 主叙事。
- 因此 D04 当前默认解释顺序继续冻结为：`共享接口/几何层 → shared latent sufficiency → morphology compensation → dynamics compensation`；只有前两层都站稳后，RAFL/AirVLA 一类动力学补偿才允许抢主补偿层预算。

## 6.9 首轮“共享几何已过线后该先修哪一层”判线卡（R864新增）

结合本轮本地回扫的 **R3D / AirVLA / Unified Latent Space**，D04 当前最值得继续压实的，不是再补“哪条路线都能试一点”，而是把 **接口过线之后的第一轮结果解释顺序** 继续冻结。因为本地方向已经足够说明三件事：
- **R3D** 主要回答 `共享几何是否真的站稳`，属于 `GTG` 前置层；
- **Unified Latent Space** 主要回答 `共享 latent / 轻量 retarget 是否已足够承载跨载体共性`，属于 `GTG→MCG` 之间的中间支撑位；
- **AirVLA** 主要回答 `geometry 已可迁移时，剩余掉点是否主要来自 dynamics gap`，属于 `DRB` 主对照位。

所以从本轮开始，D04 在 `IG0 + SC0 + SC1` 过线后，统一按下面的顺序解释首轮结果，禁止再把 morphology compensation、latent retarget、physics adapter 混成同一个“补偿层都挺重要”的模糊结论。

| 观察信号 | 优先判断 | 推荐动作 | 暂缓动作 |
|---|---|---|---|
| `PGS / IFR / ICS` 仍不稳 | 共享几何接口未站稳 | 只修 `R3D / PMI Packet / human geometry anchor` | 暂缓 `specialist / latent retarget / physics adapter` |
| `PGS` 已稳，`GTG` 下降但 `MCG < 3pp` | 形态补偿不是主差异源，shared latent 已足够 | 优先保留 `shared+adapter / Unified Latent Space / latent retarget` | specialist 不升格 |
| `PGS` 已稳，`GTG` 低，但 `DRB` 高 | geometry 可迁移、dynamics gap 主导 | 优先转 `AirVLA / physics adapter / payload-aware guidance` | 暂缓继续细拆 morphology 路线 |
| `PGS` 已稳，`GTG` 低，`MCG` 高且 `DRB` 不主导 | 形态补偿层值得保留主线 | 保留 `specialist / morphology token / HEX 类路线` | physics adapter 降为附录或次级实验 |
| `GTG / MCG / DRB` 都不高，但 `SDR` 高 | 主收益已落到部署壳层 | D04 主文改写为 `shared backbone + D06/D07 shell synergy` | 暂缓继续扩 D04 主干 |

### 6.9.1 新的默认主张

D04 后续不该再把 `shared geometry / shared latent / morphology compensation / dynamics compensation` 写成并列主贡献，而应固定成：
1. **先证共享几何**（R3D / PMI Packet）
2. **再证 latent 是否已足够**（Unified Latent Space / latent retarget）
3. **只有 latent 不够时，才继续区分 morphology compensation 还是 dynamics compensation**

这一步的核心价值，是把 D04 从“很多补偿层都可能有用”继续压成“先看共享层够不够，只有不够时才让补偿层抢预算”。这样更适合主人的双平台链路，也能避免 specialist 和 physics adapter 在首轮后继续同时烧预算。

## 6.8 接口通过后的主叙事三选一规则（R846新增）

在 `IG0 → SC0 → SC1` 之后，D04 不能再让 `specialist / latent retarget / physics adapter / shell` 同时继续吃预算。本轮新增一个更硬的**主叙事三选一规则**：

| 条件模式 | 允许保留的主叙事 | 默认冻结对象 | 说明 |
|---|---|---|---|
| `IG0/SC0` 未过 | 无主叙事，先修接口 | 冻结 SC1-SC4 | 接口没站稳时，不允许比较补偿层 |
| `IG0/SC0` 过，但 `GTG` 仍高 | **几何主导** | 冻结 specialist / physics adapter | 先继续修 R3D / PMI Packet / human geometry anchor |
| `IG0/SC0` 过、`GTG` 低、`MCG ≥ 3pp`、`DRB` 不主导 | **形态补偿主导** | physics adapter 降级为补充实验 | 允许保留 specialist / morphology token 主线 |
| `IG0/SC0` 过、`GTG` 低、`MCG < 3pp`、`DRB` 高 | **动力学补偿主导** | specialist / morphology token 降级为 supporting evidence | 默认切到 AirVLA / physics adapter 主线 |
| `IG0/SC0` 过、`GTG` 低、`MCG` 与 `DRB` 都高 | 先锁 **动力学补偿主导**，形态层只保留单任务对照 | 冻结任务扩张 | 空中场景里先处理可执行风险，再回头比较形态补偿 |
| 任一路线成立后 `SDR` 高 | 主文改写为 **共享主干 + D06/D07 壳层协同** | 冻结 D04 主干扩模 | 避免把部署壳层收益误写成 D04 主创新 |

### 6.8.1 新默认优先级

本轮起 D04 的默认优先级写死为：
`接口可信 > 共享几何 > 动力学补偿 > 形态补偿 > 壳层表述`

原因很直接：在空中载体场景里，`DRB` 更接近真机可执行风险，而 `MCG` 更像在共享层已站稳后才值得精修的性能项。也就是说，**specialist 不再是默认主线，只是待证伪候选。**

### 6.8.2 本轮最小执行结论

只要下一轮拿到 `IFR / ICS / DMS / PGS + GTG/MCG/DRB` 第一组硬读数，就必须立即按上表冻结主叙事；不允许再出现“几何、specialist、physics adapter 都各补一点看看”的拖延。

## 6.8.3 接口后的首轮读数→主叙事冻结表（R851新增）

为避免 `IG0/SC0` 通过后再次回到“每层都想再试一点”的拖延，本轮把接口通过后的**最小冻结规则**再写死一层：

| 首轮读数模式 | 主叙事结论 | 必须冻结 | 允许继续 |
|---|---|---|---|
| `IG0/SC0` 未过 | 共享接口未成立 | 冻结 `SC1-SC4` | 仅修 `PMI Packet / R3D / depth grounding` |
| `IG0/SC0` 过，`GTG` 高 | **Geometry-first** | 冻结 `specialist / latent retarget / physics adapter` 扩展 | 继续 `human geometry anchor + shared task geometry` |
| `IG0/SC0` 过，`GTG` 低，`MCG < 3pp`，`DRB` 高 | **Dynamics-first** | 冻结 `specialist / morphology token` 主线 | 继续 `physics adapter / payload-aware guidance / capability bound` |
| `IG0/SC0` 过，`GTG` 低，`MCG ≥ 3pp`，`DRB` 不高 | **Morphology-compensation-first** | 冻结新的 `physics adapter` 变体 | 继续 `specialist / morphology token / latent retarget` 单任务复验 |
| `IG0/SC0` 过，`GTG` 低，`MCG` 与 `DRB` 都高 | **先动力学后形态** | 冻结任务扩张与长链任务 | 仅在 `T1` 上保留 `physics adapter + morphology compensation` 双线 |
| 任一模式下 `SDR` 高 | **共享主干 + 壳层协同** | 冻结 D04 主干扩模 | 转向 D06/D07 shell 记账 |

### 6.8.4 对主人当前链路的现实含义（R851新增）

对“地面机械臂 → 空中机械臂”这条线，D04 当前最现实的论文结构已经进一步收束成：
1. 先证明 `PMI Packet + shared task geometry` 在跨观测扰动下稳定；
2. 再判断剩余 gap 主要来自 **动力学残差** 还是 **形态补偿不足**；
3. 最后只保留一条主补偿叙事，不让 `morphology` 与 `physics` 同时抢标题。

这等于把 D04 从“多种跨载体补偿方法并列罗列”，继续压成“**共享接口先成立，然后只选一个主补偿层**”的论文结构。

## 7. 本轮结论（R845）

结合本地回扫与本轮新增锚点 **CAPO / PointBridge / DeFM / PMI 接口**，D04 当前最稳的执行顺序继续收束为：
1. **先过 `IG0 + SC0`**，把 `PMI Packet` 的字段完整率、一致性、domain factor 解耦与 3D几何稳定性先跑出来；
2. **只有共享意图接口站稳后，才比较 `specialist / latent retarget / morphology token`**，避免补错层；
3. **若 `DRB` 偏高，再切 physics adapter / payload-aware guidance**，由 `AirVLA / Hardware-Agnostic QuadWM` 解释动力学残差；
4. **若 `SDR` 偏高，就冻结 D04 主干扩模**，明确改写成“共享主干 + D06/D07 壳层协同”。

这意味着 D04 下一轮最值钱的，不是继续找论文，而是先把 **`IFR / ICS / DMS / PGS / PMI Packet 完整率`** 变成第一组硬结果。有了这组数，后面的 morphology、physics 和 shell 才配谈谁该拿主叙事。


