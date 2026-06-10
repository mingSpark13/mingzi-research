# 方向一:用于具身操作的世界模型

> 研究具身操作的世界模型:学习环境动态、预测未来状态、支持规划和想象

## 研究目标

- 梳理当前具身操作世界模型的核心方法(Dreamer/SaGE/GEPC等)
- 发现领域空白:哪些问题还没解决?
- 归纳可行项目方向

## 核心问题

- 世界模型如何支持细粒度操作(如灵巧手、空中抓取)?
- 低成本数据采集 + 世界模型预训练 的路径?
- 与主人无人机研究如何结合?

## 已有知识库论文

(从 Notebook/02_阅读笔记/ 中关联)

## 花火研究笔记

- 2026-06-10 R研究推进: 本轮按轮换主推进 **D01 世界模型**，满足“高优先级 D01/D04/D06 三轮内至少覆盖一个”且避免与上一轮连续停在 D02/D07。先读 `OWNER_NOTES.md`（当前无新批注），再按本地优先回扫 `README.md` 与近 30 天本地 L1 锚点 **MemoryVLA++ (2606.09827)**、**iMaC (2606.09813)**，并补跑 QMD `world model latent imagination long horizon robotics --no-rerank`；QMD 主要回流 **WowWoVal**、现有 D01 文档与旧的 Fast-WAM 线索，说明本轮新增高价值信息主要来自昨天已入库的两篇 D01 新笔记。随后按流程补做 arXiv Export API，命中 **TacForeSight (2606.11184)** 等最新论文；其中 TacForeSight 与“触觉世界模型”支线相关，但它更偏 contact-rich manipulation policy 增强，和当前 D01 主叙事 `deployment-time supervisor / packet contract / delayed consumption honesty` 的贴合度还不够直接，因此本轮 **高价值新增论文 2 篇（均已在本地完成入库：MemoryVLA++ / iMaC），新增完整入库 0 篇**。Phase 2 直接推进 `PAPER.md`：一是在 **2.2 World Models as Evaluators and Supervisors** 增补对 MemoryVLA++ 与 iMaC 的吸收，明确 supervisor packet 不只要保 freshness / feasibility，还要保 **temporal-history trace** 与 **contact-aware action semantics**；二是在 **2.6 Limitations** 追加 3 条 deployment-facing 缺口，把“temporal episode context / contact-intent semantics 未被 packet-level 审计”写成现有工作共同短板；三是新增 **3.36 Temporal-Context and Contact-Semantics Preservation**，正式引入 `\tau_t=(episode, imagined-future, contact-sem, bind-honest, consume-honest)` 作为新的 accountability tuple，用来区分“线程没断”与“语境/接触语义仍诚实保留”这两件事。当前更稳的论文收束点是：D01 的 deployment-time contract 不能只讲 identity/thread/freshness，还应进一步主打 **temporal-context-preserving + contact-semantics-preserving packet honesty**，这样才能把长程记忆型 world model 与接触敏感型 action world model 的增益诚实吸收到 delayed-consumption supervisor 叙事里。

- 2026-05-15 R研究推进: 本轮按轮换切到 **D01 世界模型**，避免与上一轮继续停在 D06，并满足“三轮内至少覆盖 D01/D04/D06 之一”的约束。先读 `OWNER_NOTES.md`（当前无新批注），再回看今日增量线索 **OA-WAM (2605.06481)** 与已有 D01 `PAPER.md` 中关于 `identity-preserving packet addressing / delayed consumption` 的主线。由于 cron 环境下本轮外部检索命令受限，未补成功 QMD/arXiv 新扫描，因此保守记为 **高价值新论文 0 篇新增确认、完整入库 0 篇**，只使用已在本地记忆与现有草稿中出现的 OA-WAM 线索推进写作。Phase 2 直接强化 `PAPER.md`：在 **2.6 Limitations** 新增一条 object-slot 视角的限制，明确“identity disentanglement 若未与 packet emit/refresh/consume 同步审计，仍可能在 consume 侧 silently switch referent”；同时扩写 **3.25 Identity-Preserving Packet Addressing**，补进 `slot-to-consume audit`，把 emitted slot / refreshed slot / consumed slot 的一致性显式纳入 packet accountability，而不再默认 representation-level disentanglement 自动等于 downstream consume honesty。当前更稳的论文收束点是：D01 不只是 freshness-aware 或 thread-aware supervisor，而应进一步主打 **identity-accountable deployment contract**——只有当 object/anchor/clause/thread 在 refresh→bind→consume 全链路上都被诚实记录，world model 的 delayed-consumption gain 才算真的成立。

- 2026-05-02 R研究推进: 本轮按轮换主推进 **D01 世界模型**，满足“三轮内覆盖 D01/D04/D06 至少一个”且避免连续重复 D01/D06 之外主线失衡；先读 `OWNER_NOTES.md`（当前无新批注），再回扫近 30 天本地 L1 锚点 **WorldArena / WorldEval / Dream2Fix / ABot-PhysWorld**，并补跑 QMD `world model packet expiry delayed consumption thread consistency --no-rerank`。QMD 结果主要回流 **D02 的 TIC-VLA latency-aware semantic-control interface** 与既有 D01 文档，反而强化了“packet release 时正确 ≠ downstream consume 时仍正确”这一 delayed-consumption 论点；按流程补做 arXiv Export API 后暂未得到更贴合 D01 当前 `deployment-time supervisor / packet freshness / thread consistency` 主线的高价值新论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**。Phase 2 直接推进 `PAPER.md` 的 **Section 4.2 Main Results**：新增 **4.2.7 Hover-Window Recovery Versus General Handoff Gain**，把结果解释显式拆成 `W0 pre-release reroute / W1 hover-reanchor bounded recovery / W2 post-refresh downstream consumption` 三个 route window，并要求 `(SRY, RPPR, PHC, thread-preserving EAHR)` 按窗口分开报，防止把 Dream2Fix 式 hover-window 局部恢复收益误写成广义 handoff improvement；同时将 **Route-Freezing Rule** 升级为只有当 delayed-consumption bins 与 **W2 post-refresh consumption** 同时为正时，才允许升格成 **progress-preserving supervisory contract**，否则最多收成 `freshness-accountable invalidation layer` 或 `phase-bounded recovery interface`。当前更稳的论文收束点是：D01 最值得主打的不是“world model 能修复失败包”，而是 **在 delayed consumption 下区分 freshness gain、hover-window recovery gain 与真正 thread-preserving handoff gain 的 deployment-time contract**。

- 2026-05-02 R研究推进: 本轮按轮换主推进 **D01 世界模型**，满足“三轮内覆盖 D01/D04/D06 至少一个”且避免与上一轮继续停在 D06；先读 `OWNER_NOTES.md`（当前无新批注），再严格按本地优先回扫近 30 天 L1 锚点 **Dream2Fix / Cortex 2.0 / DexWorldModel / WorldArena / HybridWorldSim**。随后补跑 QMD `world model packet freshness delayed consumption thread consistency --no-rerank`，结果主要回流到既有 D01 文档与一条 **D02 TIC-VLA latency-aware delayed semantic-control interface** 线索，没有形成需要完整入库的新 D01 高价值论文；按流程补做 arXiv Export API 后高位返回 **OmniRobotHome / LaST-R1 / RopeDreamer**，与 D01 当前 `packet freshness / delayed consumption / progress-thread consistency` 主线贴合度不足，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**。Phase 2 直接推进 `PAPER.md` 的 **Method 3.16** 与 **Experiments 4.2-4.3**：进一步压实 `thread-safe refresh guard`，把 refresh 后事件强制分成 `thread-preserving / thread-shifting / off-thread commit` 三类；同时新增 **Delayed-Consumption Contract、Latency-Aware Handoff Binning、Hover-Window Recovery versus General Handoff Gain** 三组结果解释规则，并把顶层 claim 冻结条件升级为只有当 **W2 post-refresh downstream consumption** 与 **thread-preserving delayed-consumption readouts** 同时为正，才允许写成 `progress-preserving supervisory contract`。当前更稳的论文收束点是：D01 最值得主打的已经不是“会做 bounded recovery”，而是 **在 delayed consumption 下区分 freshness gain、hover-window recovery gain、和真正 thread-preserving handoff gain 的 deployment-time contract**。

- 2026-05-01 R研究推进: 本轮按轮换主推进 **D01 世界模型**，并满足“三轮内覆盖 D01/D04/D06 至少一个”与“避免连续两轮同方向”的规则；先读 `OWNER_NOTES.md`（当前仍无新批注），随后回扫本地 L1 锚点 **WorldArena / HybridWorldSim / Cortex 2.0**，再补跑 QMD `world model packet expiry corrective memory progress handoff --no-rerank`。QMD 结果仍主要回流既有研究状态与旧方向文档，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**。Phase 2 直接推进 `PAPER.md`：一是在 **2.6 Limitations** 新增两条 deployment-facing 缺口，明确现有 real-world world model 虽会做候选未来评分，但仍缺少对 **packet freshness / expiry-triggered invalidation / downstream consumption delay** 的一等建模，也缺少对 **remaining-plan preservation under repair and handoff** 的显式 packet 约束；二是新增 **3.15 Progress-Consistent Commit Semantics**，把 packet 提交条件从“可行+新鲜”继续压实为“还必须与下游执行线程 progress-consistent”；三是在 **4.3 Ablation** 增补 **off-thread commit after refresh** 的归因项，使 D01 后续能区分“包还能执行”与“包虽然能执行但已悄悄脱离原本局部计划”。当前更稳的论文收束点是：D01 的主贡献应继续讲成 **time-sensitive supervisory contract**，但这个 contract 的核心不只在 expiry-aware freshness，而在 **freshness + progress-thread consistency** 的联合约束。

- 2026-04-28 R890: 本轮按轮换推进 **D01 世界模型**，先读 `OWNER_NOTES.md`（当前无新批注），回扫本地 L1 笔记 **WorldArena / HybridWorldSim / Cortex 2.0**，并补跑 QMD `world model deployment-time supervisor aerial manipulation packet screening --no-rerank`。QMD 结果仍主要回流既有 D01 文档与 WorldArena；随后按流程补做 arXiv Export API，高位命中 **Passage-Aware Structural Mapping**、**flatness MPC**、**MoT-HRA**，与 D01 当前 `deployment-time packet supervisor / stage-aware routing / bounded repair` 主叙事贴合度不足，因此 **高价值新论文 0 篇，新增完整入库 0 篇**。Phase 2 直接推进 `PAPER.md`：新增 **3.13 Stage-Scoped Risk Budgeting and Packet Expiry**，把 `risk_budget` 从抽象单标量改写为 `velocity / attitude / pose / correction-window / escalation-threshold` 五元组，并引入基于 `timeout + envelope drift + stage mismatch` 的 packet expiry 规则；同时将实验部分重构为更清晰的 **4.1 Experimental Setup** 与部署指标集合，补进 `PHFR / RPPR / PHC / EPRR / EAHR`，让 D01 的证据链从“会不会筛包”延伸到“包在 D01→D06 handoff 时会不会过期、误用、断线程”。当前判断更稳：D01 最值得主打的不是静态 rollout scorer，而是 **time-sensitive deployment contract**。- 2026-04-25 R882: 本轮按轮换切回 **D01 世界模型**，先回扫本地 L1 锚点 **WorldArena / HybridWorldSim / SparseWorld-TC** 与当前 `PAPER.md`。QMD 对 `robot world model latent predictive control embodied` 的检索增量有限，主要回流 IMPASTO 与既有 D01 报告，因此按流程补做 arXiv Export API 外查，最新高位命中 **Hi-WM (2604.21741)**、**Open-H-Embodiment (2604.21017)**、**Cortex 2.0 (2604.20246)**。其中真正直接贴合 D01 当前“deployment-time supervisor”主叙事的是 **Hi-WM** 与 **Cortex 2.0**：前者把 world model 从 evaluator 推到 *human-corrective substrate*，后者进一步证明 real-world industrial long-horizon manipulation 受益于先生成并评分 candidate futures 再提交执行。但本轮不做完整入库，原因是现阶段 D01 已进入 PAPER 写作优先阶段，且 Cortex 2.0 已在 2.5 中作为工业部署证据链写入，Hi-WM 先保留为下一轮可选 Related Work 增补点。Phase 2 的核心推进是继续压实 `PAPER.md` 的 **Experiments**：新增 **4.4 Cross-Direction Interface Validation、4.5 Deployment-Boundary Discovery and Failure-Focused Screening、4.6 Stage-Aware Triage and Recovery Accounting、4.7 Minimal Sanity-Check Ladder** 四个子节，把 D01 从“概念型 supervisor”推进到“可执行实验协议”，特别明确了 D01→D06 packet handoff、boundary discovery、分阶段 triage/recovery 记账，以及首轮最小 sanity ladder。当前判断更稳了：D01 的第一篇论文不该再讲泛化 world model，而应讲 **world model as deployment-time supervisory packet generator**，并用边界发现与阶段一致性来证明它对龙虾执行栈真有用。

- 2026-04-23 R878: 本轮按轮换选择 **D01 世界模型**，严格先做本地回扫，再用 QMD 补关联。复核了近 30 天本地 L1 锚点 **WorldArena / Interactive World Simulator / Causal World Modeling for Robot Control**，并补跑 `qmd query "world model executable behavior feasibility screening aerial manipulation" --no-rerank`；结果主要回流 **WorldArena** 与 **ROBOGATE**，说明当前与 `deployment-time supervisor / executable behavior / feasibility screening` 最贴近的本地知识仍集中在“功能效用评测 + 部署前边界发现”这条线。随后按流程补做 arXiv Export API 外查，最新结果给出 **UniT (2604.19734)**、**Mask World Model (2604.19683)**、**Multi-Cycle Spatio-Temporal Adaptation (2604.19670)**；其中真正直接命中 D01 当前主线的是 **Mask World Model**，但该文已在现有 PAPER 引用链中，无需重复入库，因此本轮 **高价值新论文 1 篇（已在引用池），新增完整入库 0 篇**。Phase 2 的核心推进是把 D01 `PAPER.md` 的 **2.5 Evaluation Beyond Visual Fidelity** 从一句“别只看视频质量”压实为完整论证：正式接入 **WorldArena 的 perception-functionality gap**、**RoboWM-Bench 的 executable behavior gap** 与 **Mask World Model 的 nuisance-robust semantic-mask dynamics** 三条证据链，并明确把 D01 的部署导向指标收束到 `danger-action release / misroute / anomaly escape / packet handoff failure`，让论文叙事从“世界模型画得像不像”进一步固定到“监督包能否安全、可执行、可复用”上。

- 2026-04-21 R872: 本轮按轮换切回 **D01**，严格先做本地回扫。复核了 `README.md / REPORT.md` 与近 30 天本地 L1 锚点 **WorldEval / Dream2Fix / WoVR / WorldArena / Interactive World Simulator**；并补跑 QMD `qmd query "world model route supervisor packet pre-screen aerial execution" --no-rerank`，结果仍主要回流 **世界模型概念辨析**、D01 现有 README 与既有 WorldArena source 页面，说明本地方向对 `packet pre-screen / route supervisor / hover-bounded recovery` 这条线的信息增量已明显不足。按纠偏后的流程继续补做 arXiv Export API 外查，高位结果为 **Semantic Area Graph Reasoning for Multi-Robot Language-Guided Search (2604.16263)**、**DENALI (2604.16201)**、**SENSE (2604.15946)**；三者分别偏多机器人语义搜索、NLOS LiDAR 感知、开放词汇立体分割，与 D01 当前 `pre-execution route supervisor / interface-first execution supervisor / hover-bounded recovery` 主线贴合度不足，因此本轮 **高价值新论文 0 篇，新增入库 0 篇**。Phase 2 继续把 D01 从“首轮主叙事冻结规则”推进到 **首轮 no-go 之后标题默认该怎么诚实收束**：当前已明确写死三段顺序——若 `rank-score gate / triage+route_action` 已显著改善 `danger-action 漏放率 / late stop / misroute`，则主叙事默认收束为 **stage-aware route supervisor**；若 hover-bounded recovery 主要只改善 `packet repair 成功率`，而未同步改善前三项核心安全指标，则 recovery 自动降级为 **hover-window supporting evidence**；只有当 recovery 对核心安全指标也给出净正增益时，才允许保留为 `phase-bounded recovery` 的竞争位。核心价值是让 D01 首轮结果一出来就知道论文标题该讲 supervisor、interface-first，还是仅保留 hover-bounded recovery 的配角地位，而不是继续三条叙事并挂。

- 2026-04-19 R836: 本轮继续按轮换压 **D01**，严格先做本地回扫。已复核 `REPORT.md`、`experiments.md` 与近 30 天本地 L1 锚点 **Dream2Fix / WorldEval / WoVR / World-Gymnast / ABot-PhysWorld**；QMD 检索 `world model robot recovery triage anomaly actionable recovery --no-rerank` 仅稳定回流 **Persistent Robot World Models** 与当前 D01 报告本身，没有形成足以触发完整入库的新高价值论文，因此本轮不扩 arXiv / Tavily。Phase 2 继续把 D01 从“恢复值不值得部署”推进到 **主叙事收束 + 跨方向接口绑定**：在 `REPORT.md` 新增 **4.17 恢复线资源冻结与主叙事收束规则**、**4.18 与 D06 的最小接口绑定**，明确首轮只允许 `部署前 evaluator + triage / stage-aware route supervisor / hover-bounded recovery / interface-first` 四类主叙事竞争；同时在 `experiments.md` 新增 **E6 D01→D06 执行前预筛接口烟测**，把 `rank_score / F1-F2 / route_action / hover-bounded recovery` 正式映射到 packet 执行前验收链。当前关键结论更稳了：D01 首轮最现实的价值不是替龙虾项目做长程 planner，而是先把 **危险放行、误路由、停悬窗口恢复** 这三件事压成统一 supervisor 接口。

- 2026-04-18 R813: 本轮按轮换回到 **D01**，严格先看本地 L1 笔记与方向文档，重点复核了刚入库的 **Dream2Fix** 以及现有 `F1/F2 分诊 + P6 恢复层` 骨架；QMD 检索依旧因本机 `glslc` 缺失退化后不稳定返回，因此没有继续依赖外部或语义扩搜。当前关键收束不是再找新 recovery 论文，而是把 D01 的部署前主叙事从“能恢复”推进到“恢复值不值得上线”。已在 `REPORT.md` 新增 **4.8 分诊-恢复统一记账协议**，正式把 **SRY / AER / HHB / RDR / RCS** 五个指标写成主表标准；同时在 `experiments.md` 新增 **E2 分诊-恢复记账实验**，用于比较 `规则回退 / Dream2Fix recovery / 混合恢复` 三档路线，避免后续只看恢复率却忽略异常漏放与人工接管负担。

- 2026-04-18 R809: 本轮按轮换切回 **D01**。定向 arXiv 扫描补到 **Dream2Fix: Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis** (2603.13528)，并已按完整流程入库（PDF + 阅读笔记）。它最值得保留的不是“又一个失败恢复器”，而是直接在生成式世界模型里从成功演示合成 **counterfactual failure rollouts**，再筛出高质量 `失败→修正` 配对数据，把 D01 当前的 `known failure vs anomaly triage` 继续推进成“已知失败如何恢复”的可执行路线。已同步把这一判断写入 `REPORT.md`，新增 **已知失败恢复闭环（R1规则回退 / R2检索式恢复 / R3反事实恢复合成）** 与 **P6 恢复层收益**，让 D01 从“会拦不会救”继续往“会拦也会救”推进。

- 2026-04-18 R806: 本轮按轮换切回 **D01**。Tavily 补记 **World Model Failure Classification and Anomaly Detection for Autonomous Inspection** (2602.16182)。它最值得保留的不是“inspection 场景分类器”本身，而是把 deployment-time 失败明确拆成 **known failure** 与 **OOD anomaly** 两类，并尝试用同一 world model backbone 同时做失败分类与异常检出。这对 D01 很关键，因为当前 evaluator / verifier / safety gate 已经较完整，但还缺一层“被拦下后该怎么分诊”的协议。已同步把该判断写入 `REPORT.md`，新增 **已知失败 vs 异常分诊协议** 与 **P5 分诊层收益**，让 D01 从“能否放行策略”继续推进到“放行失败后如何决定自动恢复、保守回退还是升级人工接管”。

### 2026-04-14 R694: 文献扫描发现（来自 scan_2026-04-14.md）
**本轮发现**：
1. **WowWoVal** (2601.04137) — Embodied World Model Evaluation，对视频基础模型作为预测性世界模型进行系统性评估，⭐⭐⭐ 与龙虾 D01 主线高度相关
2. **Modeling the Mental World** (2601.02378) — 综述"心理世界模型"，为 D01 提供理论框架参考，⭐⭐⭐
3. **ReWorld** (2601.12428) — 用 RL 对齐视频世界模型与多维奖励信号，⭐⭐
4. **Explicit WM for HRC** (2601.01705) — 提升 WM 在感知噪声、指令歧义、人机交互下的鲁棒性，⭐⭐
**深挖队列**：2601.04137 > 2601.02378 > 2601.12428 > 2601.01705


- 2026-04-15 R722: 本轮按轮换切到 **D01 + D07**。D01 新增入库 **EVA** (2603.17808)：Executable Video Alignment——用IDM作为reward模型，对视频WM做RL后训练，显式对齐"视觉rollout"与"物理可执行动作"之间的executability gap。关键意义：解决了视频WM生成看起来顺滑但解码出来的动作不可达/不稳定的问题。在RoboTwin和真实双手机器人上验证下游任务成功率提升。对D01的直接价值：EVA可以直接补进现有`policy-to-latent action interface + forward simulation + inverse/self-check verifier + safety gate`四层验收体系，专门作为**executability-aligned post-training**层，解决"latent WM生成视频 vs 实际可执行动作"的对齐问题，是比单纯加verifier更主动的后训练路线。
- 2026-04-15 R718: 本轮按轮换切到 **D01 + D07**。D01 新增关键发现：①**MotionScape**(2604.07991)：超大规模真实世界高动态UAV视频数据集，专为世界模型训练设计，直接利好主人的UAV数据飞轮路线；②**Real-Time Physical Action-Conditioned Video Generation**(2603.05449)：用action-conditioned video model模拟3D物理交互和机械手操作力，实现力/接触的物理正确模拟，对"WM替代仿真器"路线有直接参考价值，是龙虾/无人机物理仿真生成路线的新候选；③**World Action Models零样本策略**(2602.15922)：KV cache管理实现闭环执行，autoregressive架构，对D01的WM+控制集成路线有参考。
- 2026-04-14 R711: 本轮按轮换切到 **D01 + D04**。D01 arXiv 回扫新增 3 个入库候选：① **HCLSM** (2603.29090) 分层因果潜态机，层次化因果结构预测动态场景；② **Kinema4D** (2603.16669) 运动学4D世界建模，CVPR 2026；③ **Policy-Guided WM Planning** (2603.25981) WM引导的语言条件VLN规划。三者均未在现有主线上。
- 2026-04-14 R707: 本轮切到 D01 + D04。D01 补抓 Do World Action Models Generalize Better than VLAs? (2603.22078)，在 LIBERO-Plus 和 RoboTwin 2.0-Plus 上系统比较 WAM vs VLA 鲁棒性。WAM（LingBot-VA 74.2% / Cosmos-Policy 82.2%）对视觉/语言扰动显著更强；π0.5 需大规模异构数据才能接近。对 D01 直接价值：WAM（视频扩散+latent action decode）比端到端 VLA 更具部署鲁棒性，是龙虾安全层骨架候选；后续应把 video-prior + latent action 接口 + 扰动鲁棒性纳入验收协议。
- 2026-04-13 R667: 本轮按轮换切到 **D01 + D04**。D01 轻量补抓 **Rethinking Video Generation Model for the Embodied World** (2601.15282) 后，一个 evaluation-facing 判断更稳了：后续不该只拿 `rollout 像不像` 当世界模型有效性的总指标，而应把 **task completion、physical-semantic plausibility、robot-subject stability、motion smoothness** 拆成独立验收位，并继续与 **policy ranking correlation / verifier-self-check / generated-data usefulness** 并排比较。它最值得保留的不是“又一个视频生成模型”，而是 **RBench + RoVid-X** 这套面向机器人视频世界的统一评测视角，能帮 D01 把 `能生成` 和 `能服务控制/评估` 真正拆开。
- 2026-04-12 R661: 本轮按轮换切到 **D01 + D04**。D01 用 DuckDuckGo 轻量回扫后，高位结果仍主要回流 **World Action Verifier / WAV** (2604.01985) 一线，没有出现足以改写主骨架的新候选，但一个 deployment-facing 判断更稳了：后续不该继续把 verifier 混在 rollout 分数里，而应继续把 **state plausibility / action reachability / inverse-style self-check** 作为独立验收层，和 **policy-to-latent action interface、forward simulation、safety gate** 并列比较。当前更值得推进的不是扩图，而是把这四层验收协议写实。
- 2026-04-12 R658: 本轮按轮换切到 **D03 + D01**。D01 轻量补抓 **Self-Improving World Models via Forward-Inverse Asymmetry** (2604.01985) 后，一个老判断又被压实了：world model 若要服务 **policy evaluation / optimization / planning**，不能只看前向 rollout 像不像，还要把 **inverse consistency / verifier-style self-check** 单列成独立验收位。当前更稳的结论是，D01 后续默认按 **policy-to-latent action interface + forward simulation + inverse/self-check verifier + safety gate** 四层部署，优先比较“有无自校验”对策略排序稳定性、OOD 动作过滤和长时 rollout 可信度的影响。
- 2026-04-12 R655: 本轮按轮换切到 **D01 + D04**。D01 轻量补抓 **Causal World Modeling for Robot Control / LingBot-VA** (2601.21998) 后，又多压实了一条 deployment-facing 判断：除 **policy-to-latent action interface / verifier / safety gate / heterogeneous-data ingestion** 外，还应把 **closed-loop feedback reacquisition + asynchronous inference** 单列成可部署 world model 的独立验收位。它最有价值的不是“又一个统一生成骨架”，而是把 **shared vision-action latent、闭环 rollout 持续读回真实观测、动作预测与电机执行并行化** 绑成一条更贴近真实控制链的路线，提醒 D01 后续不能只验 rollout 质量，还要验“反馈回锚后是否仍能稳住控制”和“异步推理是否真的换来可用墙钟时延”。
- 2026-04-12 R652: 本轮按轮换切到 **D01 + D04**。D01 补抓 **LDA-1B / Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion** (2602.12215) 后，一个 foundation-level 判断更稳了：真正值得单列验收的，不只是 **policy-to-latent action interface / verifier / safety gate**，还包括 **heterogeneous-data ingestion capability**。它把 **dynamics + policy + visual forecasting** 联合压进 structured DINO latent space，并能从低质量异构轨迹中继续获益，说明 D01 后续不该只在单任务 rollout 上比较强弱，而应专门比较“异构 embodied data 是否真的转化成可迁移动力学先验”。

- 2026-04-12 R649: 本轮按轮换切到 **D01 + D04**。D01 补抓 **Learning Latent Action World Models In The Wild** (2601.05230) 后，一个接口层判断更稳了：在缺少统一 embodiment、且只有真实视频的条件下，**continuous but constrained latent actions** 仍可充当 planning 的通用动作接口，说明 D01 后续不该只比较 planner / simulator / verifier 三层，还应把 **policy-to-latent action interface** 单列成独立验收位，专门比较“原始动作接口 vs latent action 接口”对长程规划、OOD 迁移与部署前策略筛选的影响。
- 2026-04-12 R646: 本轮按轮换切到 **D01 + D04**。D01 轻量回扫 **World Action Verifier** (2604.01985) 与 **Safety, Security, and Cognitive Risks in World Models** (2604.01346) 后，没有出现足以改写主线的新骨架，但部署边界又收紧了一点：后续统一验收除了 **simulator fidelity / policy ranking correlation / generated-data usefulness** 外，还应把 **safety-security-human factors** 单列成独立页，避免把“rollout 看起来可信”误当成“系统层面可以放心上线”。当前判断继续稳定为：**verifier / self-check** 与 **deployment-facing safety gate** 必须并行保留。
- 2026-04-12 R638: 本轮按轮换切到 **D01 + D04**。D01 再次复核 **Interactive World Simulator** (2603.08546) 与 **World Action Verifier** (2604.01985) 后，仍没有出现足以改写主线的新骨架，但一个验收边界更清楚了：**simulator fidelity / policy ranking correlation / generated-data usefulness** 应从 `world model 有用` 这个总标签里彻底拆开，避免把“相关性强”误当成“数据回灌也有效”，或把“能做 rollout”误当成“reachability verifier 已足够可靠”。当前判断是：D01 近期最该补的是一张三层验收表，分别覆盖 **交互模拟质量、部署前筛选相关性、数据回灌增益**，而 **verifier / self-check** 继续作为独立安全层保留。
- 2026-04-12 R636: 本轮按轮换切到 **D01 + D04**。D01 复核 **Interactive World Simulator** (2603.08546)、**World Action Verifier** (2604.01985) 与 **Hierarchical Planning with Latent World Models** (2604.03208) 后，没有出现足以改写当前主线的新骨架。新判断是：近期更该把 **interactive simulator / policy evaluation**、**verifier / self-check**、**hierarchical planner** 三层严格拆开验收，避免把“规划更强”误当成“评测更可靠”或“更适合部署”。
- 2026-04-12 R634: 本轮按轮换切到 **D01 + D04**。D01 用可用搜索链路回扫 **Hierarchical Planning with Latent World Models** (2604.03208)、**World Action Verifier** (2604.01985) 与附近结果后，没有看到足以改写当前骨架的新分支。新判断继续稳定，但更适合直接写进验收协议了：**hierarchical latent planning** 仍应只作为 **planner 层复杂度控制变量**，重点比较单层规划与多时间尺度规划在 **长程成功率、planning-time compute、zero-shot non-greedy task** 上的收益，而 **verifier / safety gate** 继续保持独立层，避免把“会规划”误当成“已可靠可部署”。
- 2026-04-11 R631: 本轮按轮换切到 **D01 + D04**。D01 复核 **Hierarchical Planning with Latent World Models** (2604.03208) 与现有 **WorldEval / WAV / ReWorld / JailWAM** 主线，没有出现足以改写骨架的新分支。新判断继续稳定为：当前更值得把 **hierarchical latent planning** 固化成 **planner 层复杂度控制变量**，专门比较单层规划与多时间尺度规划在 **长程成功率 / planning-time compute / zero-shot non-greedy task** 上的收益，而不是让它替代 evaluator / verifier / safety gate 主线。
- 2026-04-11 R628: 本轮按轮换切到 **D01 + D04**。D01 用可用搜索链路回扫 **World Action Verifier** (2604.01985)、**ReWorld** (2601.12428)、**Hierarchical Planning with Latent World Models** (2604.03208) 与 **JailWAM** (2604.05498) 一线，没有出现足以改写主线的新骨架，反而把当前验收栈坐实了。新判断是：D01 这阶段最值得推进的不是继续扩论文名录，而是把 **reward-aligned post-training、policy-to-latent action adapter、verifier/self-check、safety-security-human factors** 写成统一部署前协议；其中层次化 latent planning 更适合作为 **planner 层复杂度控制变量**，而不是替代 evaluator / safety gate 主线。
- 2026-04-11 R608: 本轮切到 **D01 + D05**。D01 重读 **WorldEval** (2505.19017) 摘要后，补出一个更可执行的 evaluator 接口判断：论文明确指出 **直接输入原始动作或高维动作编码，难以稳定生成真正 action-following 的 policy video**，因此提出 **Policy2Vec** 把策略动作压到更适合视频世界模型跟随的 latent action 接口。新判断是：后续 D01 若作为 **deployment-time evaluator / danger-action filter**，就不能只验 rollout correlation，还应单列 **policy-to-latent action adapter**，专门比较“原始动作输入 vs latent action 接口”对 ranking correlation、危险动作拦截和 OOD 高估风险的影响。
- 2026-04-11 R602: 本轮切到 **D01 + D06**。D01 补抓 **ABot-PhysWorld** (2603.23376) 后，进一步确认世界模型近期不该只看“视觉像不像”或“能不能控”，还应把 **physics alignment** 单列成部署前验收层。它最值得吸收的是 **physics-aware annotation + DPO post-training + decoupled discriminators** 这套后训练思路，以及 **EZSbench** 对 **physical realism / action alignment** 的解耦评测框架。对主人最直接的价值，是把 D01 的验收协议从 trainer / planner / evaluator / safety gate 再向前补一层 **physical plausibility**，专门覆盖物体穿模、反重力运动、接触失真这类“看起来合理但物理不真”的 rollout 问题。
- 2026-04-10 R600: 本轮切到 **D01 + D04**。D01 复核 **Ctrl-World** (2510.10125) 与既有 **WorldEval / Interactive World Simulator** 支线后，判断继续稳定：近期最值得推进的不是再扩“可控生成 world model”名单，而是把 **multi-view controllability、long-horizon consistency、policy evaluation correlation、danger-action filter** 统一写成部署前验收协议。Ctrl-World 的价值更像把 evaluator / trainer 做得更可控，而不是改写 D01 当前的主线分层。

### 2026-03-28 第1轮:世界模型 × 层次化VLA 的潜在结合点

**背景**:结合 Paper A(层次化空中VLA)的研究,发现 SafeFlow(安全flow matching)与 DreamZero(WAM)可能是重要的补充技术。

#### 关键发现:SafeFlow 的 CBF 可作为 Paper A 安全层候选

**SafeFlow (2504.08661)** 核心贡献:
- 将 Control Barrier Functions (CBF) 集成进 flow matching 采样过程
- 对每步采样方向做安全校正,保证生成轨迹满足安全约束
- 在机器人避障、无人机禁飞区场景验证了安全性

**与 Paper A 的关联**:
- Paper A 三层架构中,「中层意图解析器」与「低层精细执行」之间需要安全约束模块
- SafeFlow 的 CBF 可作为「飞行-操作协同安全层」的技术方案
- CBF 解决「硬安全约束」(禁飞区、碰撞避免),DreamZero WAM 解决「零样本策略泛化」

**潜在架构扩展**:
```
VLM意图层(秒级慢思考)
    ↓
意图解析器(中层:操作序列 + 安全约束规范)
    ↓
SafeFlow安全层(CBF引导的flow matching轨迹生成)
    ↓
低层执行控制器(ACT/Diffusion Policy,毫秒级)
    ↓
电机控制
```

**为什么有价值**:
1. 首次把「安全约束显式建模」引入层次化VLA架构
2. CBF提供可证明的安全保证(非概率近似)
3. Flow matching的轨迹质量 + CBF的安全保证,可解决无人机飞行安全+精细操作双重需求

**待验证**:
- [ ] SafeFlow 的计算延迟是否满足毫秒级实时要求?
- [ ] CBF约束条件在多约束场景(飞行高度+机械臂避碰+负载约束)下是否总是可满足?
- [ ] DreamZero WAM 能否作为中层意图解析器的backbone?

### 2026-03-28 第2轮:OpenVLA action space 分析 × Paper A 中层设计启发

**背景**:在 Paper A 三层架构(VLM意图层 → 中层意图解析器 → 低层执行)的研究中,OpenVLA 作为最强开源 VLA baseline,其 action chunking 策略与频率问题是 Paper A 必须正面回应的技术挑战。

#### OpenVLA 的 action chunking 机制

OpenVLA 采用 action chunking(动作分块)策略:
- **单次 VLM forward**:输出 8 个连续动作 token(约 8×7=56维,对应 7-DOF 臂+夹爪)
- **执行频率**:~10Hz,即 VLM 每 100ms 输出一组 8 步动作块
- **Latency 本质**:VLM forward 本身 ~200-500ms(取决于硬件),但通过 chunking 隐藏了部分延迟

**关键问题**:OpenVLA 的 chunking 策略本质上是「预测未来 8 步」,而不是「解耦慢快控制」:
- VLM 仍然在直接输出「低层动作」,而非「高层意图」
- 这与 Paper A 主张的「VLM 输出意图,中层模块负责动作生成」在架构上有根本区别

#### OpenVLA 在边缘部署(Jetson Orin)的 latency 实测

**数据来源**:OpenVLA 论文 + GitHub community benchmarks

| 硬件配置 | VLM forward | Action chunk 执行 | 端到端延迟 |
|---------|------------|-----------------|----------|
| A100 (服务器) | ~100ms | 100ms (10Hz chunk) | ~200ms |
| Jetson Orin NX | ~800ms | 100ms | ~900ms |
| Jetson Orin Nano | ~2000ms | 100ms | ~2100ms |

**核心发现**:
- 在边缘设备上,VLM forward 延迟是瓶颈(占 90%+)
- OpenVLA 在 Jetson Orin NX 上已经接近不可用(>900ms 延迟)
- 对于无人机场景,毫秒级实时控制需求(~1-5ms)完全无法满足

#### Paper A 三层架构的必然性

OpenVLA 的实践验证了 Paper A 的核心论点:

```
OpenVLA 困境(纯端到端):
VLM forward (200-2000ms) → 低层动作 → 毫秒级执行
                    ↑ 延迟在此,无法绕过

Paper A 解决方案(层次化解耦):
VLM forward (200-2000ms,慢) → 意图/约束 → 低层精细控制器 (1-10ms,快)
                               ↑ 解耦的关键:意图层与执行层分离
```

**为什么层次化解耦是对的**:
1. VLM forward 的 latency 是物理限制,无法通过工程优化消除(除非换芯片)
2. 但 VLM 只需要处理「语义级慢任务」("把红色杯子放到左边"),不需要参与每毫秒的控制
3. 中层模块(意图解析器 + 安全约束)运行在轻量级 MCU/FPGA 上,可实现毫秒级控制

#### 对 Paper A 的补充:OpenVLA 的 fine-tuning 证据

OpenVLA 论文的重要发现:
- **100-500 条 demo 数据**即可显著提升特定任务性能
- 语言指令的 zero-shot 泛化能力来自大规模预训练(OXE 数据集)
- 但在特定形态(无人机机械臂)上的迁移仍需本地 fine-tuning

**对 Paper A 实验设计的启发**:
- 主人自己的空中操作数据集(哪怕 100-500 条) + OpenVLA/π0 pretrained backbone = 快速 baseline
- 但这仍然是「端到端」路线,不改变 Paper A「层次化解耦」的长期价值
- 短期快速验证可用端到端 baseline,长期要靠 Paper A 的层次化架构

#### 待深挖发现
- [ ] OpenVLA 的 action space 设计是 7-DOF + 夹爪,如何扩展到「飞行高度 + 机械臂 7-DOF」的高维空间?
- [ ] OpenVLA 的语言指令如何「映射到」Paper A 的中层意图表示?需要一个显式接口定义
- [ ] π0 的 flow matching 动作生成 vs OpenVLA 的 action chunking - 哪个更适合 Paper A 的低层控制器?

### 2026-04-04 R435:**WAM - World-Action Model** (2603.28955) 【新增入库】

**核心贡献**:在 DreamerV2 加 inverse dynamics loss,让 latent state 不只预测未来图像,还学会"什么动作导致什么状态转移"。相当于给世界模型加了一个 action-aware 约束,使其学到的隐表示天然和动作相关,对下游控制更有价值。

**关键数字**:CALVIN benchmark,BC 59.4%→71.2%,PPO finetune 后 92.8% vs 79.8% baseline,训练步数少 8.7 倍。

**对主人的价值**:
1. WAM 的 action-aware latent 表示可以和 DIAL 的 intent bottleneck **互补**--DIAL 走"显式 intent 作为结构瓶颈",WAM 走"inverse dynamics 隐式约束"
2. 最直接的应用:接到 **04 跨载体迁移**的 contact/force latent 层,因为 WAM 学到的 latent state 天然包含"施力意图"
3. 比纯图像预测世界模型更适合作为 04/05 链路中的中间层表示

**可落地实验点**:在 EgoSim 或 V-Dreamer 的 latent space 里加 WAM-style inverse dynamics loss,看能否提升 cross-embodiment transfer 成功率

**归档**:方向 01,已入库

### 2026-04-04 R440:**OmniVTA - Visuo-Tactile World Modeling** (2603.19201) 【新增入库】

**核心贡献**:提出 OmniViTac 大规模 visuo-tactile-action 数据集(21,000+ 轨迹,86 任务,100+ 物体,6 种物理交互模式)+ OmniVTA 四模块紧耦合框架:自监督触觉编码器 + 双流 visuo-tactile 世界模型(预测接触演化)+ contact-aware 融合策略。关键突破:触觉信号不是被动观测,而是主动建模接触动力学的输入。

**对主人的价值**:
1. **多模态世界模型增强**:现有 DIAL/LatentPilot/Persistent Robot World Models 均为纯视觉世界模型;OmniVTA 证明触觉信号能显著提升接触丰富任务的动态预测质量--主人可在 01 主线上补一条「触觉融合世界模型」支线
2. **接触丰富任务直接相关**:空中抓取、开门、开柜等任务均是 contact-rich 操作,触觉感知是关键传感器
3. **数据资产价值**:OmniViTac 21K 轨迹规模可直接作为 05 数据飞轮的高质量触觉数据资产

**可落地实验点**:在 DIAL 或 WAM 的 latent world model 架构中引入触觉流(tactile encoder),看能否提升接触丰富任务的预测精度;或在 EgoSim 中加入触觉模拟层

**归档**:方向 01,已入库

### 2026-04-05 R446:新增补记 CMLF - 触觉物理属性贝叶斯估计

**CMLF** (2604.02108, Cross-Modal Latent Filter)
核心:用贝叶斯主动推理学习物理属性的因果潜在状态空间(latent state-space of physical object properties),支持 vision ↔ touch 双向跨模态先验迁移,在接触富交互中实时更新对物体属性(惯性、刚度、摩擦)的信念。

对主人的价值:这是对 01 世界模型的**感知增强**路线--它不直接预测未来图像,而是对"物理隐状态"做在线贝叶斯估计。可以与 DIAL/LatentPilot 的 latent world model 互补:DIAL 预测未来视觉 latent,CMLF 估计当前接触物理属性 latent,两者共同构成更完整的 world model 表示层。适合接触丰富的空中操作任务(开门、抓取等)。

→ 已补记,**无新增入库**(归为感知增强支线,非独立 world model 主线)。

### 2026-04-08 R517:**Aerial World Model - ANWM** (2512.21887) 【新增入库】

**核心贡献**:长距离视觉预测世界模型 + 大规模环境下UAV导航成功率提升。提出 ANWM (Aerial World Model) 在长距离视觉预测和无人机导航任务上显著优于现有世界模型。

**关键价值**:世界模型用于无人机长距离导航规划,不是纯图像生成。

**可落地**:ANWM 的长距离预测能力可接入 Paper A 的中层规划器,增强跨障碍物导航能力。

### 2026-04-08 R517:**FlyCo - Foundation Model-Empowered Drones** (2601.07558) 【新增入库】

**核心贡献**:用 Foundation Model(FM)赋能无人机自主3D结构扫描。FM 理解物理世界知识 + 无人机自主飞行能力结合,将文本描述/视觉标注转化为精确无人机动作,实现未知开放世界目标的高效扫描。

**关键价值**:FM → 无人机动作的跨模态推理,直接服务于 Paper A 的 VLM → 动作链路。

**可落地**:FlyCo 的 FM 动作解码策略可作为 Paper A 高层意图 → 低层动作转换的参考。

### 2026-04-08 R517:**Active Inference WM for UAV Swarm** (2601.12939) 【新增入库】

**核心贡献**:基于主动推理的无人机集群世界模型。用概率推理 + 自主学习实现分布式任务分配、路径规划和运动规划。用遗传算法生成专家轨迹训练层次化 WM(GA-RF)。

**关键价值**:为 Paper A 的「多约束安全规划」提供概率推理框架; swarm WM 思想可迁移到单机多约束场景(飞行高度 + 机械臂 + 负载约束)。

### 2026-04-05 R453:**Explicit World Model + Digital Twin for Zero-Shot Manipulation** (2603.13825) 【新增入库】

**核心贡献**:提出「显式世界模型+数字孪生」框架,实现零样本开放词汇目标操作。核心流程:1开放集感知(检测任意目标)→ 2数字孪生重建(物理接地仿真)→ 3交互策略采样与评估(在仿真器中探索)→ 4选定策略可靠部署到真实机器人。关键:不需要任何任务特定的机器人动作示教,仅靠数字孪生仿真就能泛化到新物体和新任务。

**对主人的价值**:
1. **不同于 DIAL/LatentPilot 的隐式世界模型路线**:DIAL 是 latent world model + action decoding,2603.13825 是「显式数字孪生+物理仿真探索」,两者正交可互补
2. **零样本操作可直接落地**:不需要大规模机器人动作数据,适合主人「空中抓取/开门」等任务--用视觉检测目标 + 构建数字孪生 + 在仿真中探索策略 → 真机部署
3. **与 05 数据飞轮天然衔接**:数字孪生需要场景资产生成,这正好可以接 PAWS/Pandora → SIMART 的结构恢复管线

**可落地实验点**:针对空中抓取任务,用 RGB-D 重建场景数字孪生 → 在 AirSim/UE5 仿真中用 MPC/RRT 探索抓取策略 → 直接迁移到真机。Pipeline: 开放词汇检测(YOLO-World/Grounding DINO) → 3D 重建(SAM+NeRF/3DGS) → 物理仿真(Isaac Sim/AirSim) → 策略选择 → 真机执行

**归档**:方向 01,已入库

### 2026-04-09 R541：**World-Gymnast — Training Robots with RL in a World Model** (2602.02454) 【已深挖入库】

**核心贡献**：把动作条件视频世界模型直接当成 RL 训练器。具体做法是：VLA policy 在 world model 中 rollout，VLM 对预测视频给奖励，再用 **GRPO** 更新策略。实验证明它不只是“能训”，而且在真机上比单纯 SFT 和软件模拟器都更强。

**关键结果**：
- AutoEval 真机上，`eggplant → blue sink` 从 **4% → 72%**，`eggplant → yellow basket` 从 **8% → 78%**
- 相比 SIMPLER 软件模拟器，4 个任务里 3 个显著更优
- 支持 **novel scene / novel instruction / test-time training / online iterative world-model improvement**，说明世界模型不仅能补数据，还能做持续迭代训练器

**对主人的价值**：
1. **D01 主线正式补齐“world model as trainer”这条支线**：之前更多在讨论 planning / latent prediction；World-Gymnast 给出了一条更偏工程闭环的路线，即直接把世界模型变成 RL 训练环境
2. **和 D05 数据飞轮形成强耦合**：如果 D05 负责“产数据”，那 World-Gymnast 说明 D01 还可以进一步负责“产交互经验 + 产训练信号”
3. **对龙虾项目很实用**：先拿视觉导航/找目标 policy 做 world-model RL 微调，再把真实 rollout 反哺 world model，本质上就是一个可持续自举闭环

**可落地实验点**：
- 先不碰大规模 GRPO，全量简化成“小闭环验证”：主人现有导航 / 操作 policy → world model imagined rollout → VLM reward / 成功判别 → 小步 RL finetune
- 若后续发现 imagined rollout 长时漂移明显，再引入 WoVR 式的 keyframe reset / policy-world-model co-evolution 来稳住训练

**归档**：方向 01，已深挖，详见 `papers/2026-04-09_World-Gymnast.md`

### 2026-04-10 R597：本轮按轮换切到 **D01 + D07**。D01 补抓 **ManipArena** (2603.28545) 摘要后，判断当前主线应继续从“世界模型能不能生成/规划”往“世界模型能不能被可靠验收”收束。它最有价值的不是再给一个新 world model backbone，而是把 **20 类真实操作任务 + 10,812 条专家轨迹 + 同步 real-to-sim 诊断环境** 绑成统一评测层，明确提醒 D01 后续要单列 **policy-evaluation correlation、system latency / contact diagnostics、OOD generalization** 三项验收，而不是只看 imagined rollout 回报或单一仿真成功率。

### 2026-04-10 R591：回扫确认 D01 验收应转向 safety gate

本轮回扫 **JailWAM** (2604.05498) 与 **Persistent Robot World Models** (2603.25685) 后，判断继续收束为：D01 近期不该再把重心放在“更大生成器”，而应把 **安全对齐、越权动作防护、rollout 可靠深度** 单列成 **evaluator / safety gate** 验收层。对主人当前路线最直接的价值，是避免 imagined rollout 看起来合理却在真实部署时越界、失稳或高估危险动作。

→ 本轮**无新增入库**，主线判断更新为：**world model as trainer / planner / evaluator** 之外，必须额外补一层 deployment-facing safety gate。

### 2026-04-09 R541：**WoVR — World Models as Reliable Simulators for Post-Training VLA Policies with RL** (2602.13977) 【新增候选】

### 2026-04-10 R581：**World Action Verifier (WAV)** (2604.01985) 【新增候选】

**核心贡献**：不是直接把 world model 做得更大，而是给它补一层 **自校验机制**。WAV 把 action-conditioned prediction 拆成 **state plausibility** 和 **action reachability** 两个更容易验证的子问题，并利用 action-free video 生成多样 subgoal，再配合 sparse inverse model 检查 forward rollout 是否自洽。

**对主人的价值**：
1. **补齐 D01 的 verifier 支线**：之前 D01 已经逐步收束出 trainer / planner / evaluator 三类角色，WAV 进一步提醒还应单独补一个 **verifier / self-check** 层，专门覆盖 under-explored actions 和 OOD 行为。
2. **很适合接到现有“policy evaluation correlation / simulator fidelity”主线**：后续验收不能只看 imagined rollout 视觉上像不像，还要判断 rollout 在动作可达性上是否可信。
3. **数据友好**：它显式利用 action-free video 作为额外信号，这和主人后续可能拥有大量无动作标注视频、但缺精细控制标签的场景很契合。

**可落地实验点**：在当前 D01 的 imagined rollout 验收框架里，加一层 **inverse-dynamics self-check / reachability verifier**，比较“只有 rollout reward”与“rollout reward + verifier 过滤”对 policy ranking correlation 和 OOD 动作稳定性的影响。

**核心贡献**：不再默认世界模型 rollout 是可靠的，而是显式控制 hallucination 对 RL 的污染。通过 **可控动作条件视频世界模型 + Keyframe-Initialized Rollouts + World Model-Policy co-evolution**，降低 imagined long-horizon error accumulation。

**对主人的价值**：
1. **正好补 World-Gymnast 的短板**：World-Gymnast 证明“能训”，WoVR 回答“怎么训得更稳”
2. **对空中长程任务尤其关键**：主人关心的空中导航 / 空中操作更怕长时 rollout 飘移，WoVR 这种 keyframe 重置思路很值得借
3. **可直接变成验收规则**：后续若 D01/D06 用世界模型训策略，必须单独检查 imagined rollout 的可靠深度，而不是只看最终成功率

**可落地实验点**：给主人自己的 world model RL 原型加入“每 N 步回锚到真实关键帧”的半闭环 rollout，比较是否比纯 imagined rollout 更稳

**归档**：方向 01，新增候选

### 2026-04-08 R533：**WoW — Benchmarking World Models for Embodied AI** (2601.04137) 【候选待入库】

**核心贡献**：系统性评测具身AI世界模型，发现当前方法在真实世界泛化存在巨大gap——大多数模型在真实世界崩溃到0%，WoW维持40.74%成功率。揭示生成视频与真实世界之间的sim-to-real鸿沟。

**对主人的价值**：
1. **路线选择参考**：WoW证明纯视频生成式世界模型在真实场景泛化差，主人应关注「数字孪生+物理仿真」路线（如Explicit World Model）而非纯视频生成路线
2. **龙虾项目风险提示**：龙虾的视觉导航世界模型若走纯生成路线，可能面临类似泛化崩溃风险

**归档**：方向 01，候选待入库

### 2026-04-08 R535：**WorldArena — Unified Benchmark for Evaluating World Models in Embodied AI** (2602.08971) 【已深挖入库】

**核心贡献**：提出 WorldArena——具身AI世界模型的统一评测框架+排行榜，不只看视频质量，还把世界模型当作**数据引擎 / 策略评估器 / 动作规划器**来统一评测，明确暴露 perception-functionality gap。

**对主人的价值**：
1. **功能优先评测标准**：后续主人做 D01 / D06，不该只看生成视频像不像，而该看是否真的提升下游策略、规划和评估
2. **路线选择参考**：WorldArena 进一步证明纯视频生成强，不等于具身任务强，动作条件建模和任务闭环验证更关键
3. **评测标准化**：可直接作为主人未来空中世界模型实验的基准模板，扩成“空中版 WorldArena”

**归档**：方向 01，已深挖，详见 `papers/2026-04-09_WorldArena.md`

### 2026-04-08 R531:**VISTA-WM — Scaling World Model for Hierarchical Manipulation Policies** (2602.10983) 【新增入库】

**核心贡献**:提出层次化 VISTA 框架--世界模型(高层规划器)+ VLA(低层执行器)协同。WM 负责将长程任务分解为子任务序列(带目标图像),VLA 负责在文本+视觉引导下生成动作序列。核心创新:用合成目标图像(而非纯文本目标)引导低层策略,解决 OOD 泛化瓶颈。在 massive OOD 场景验证,相同结构 VLA 在 novel 场景从 14% → 69% 成功率。

**对主人的价值**:
1. **与 Paper A 三层架构直接对齐**:WM = 高层意图层,VLA = 低层执行器,与 DIAL(意图瓶颈) + SafeFlow(安全层) 共同构成完整层次化 pipeline
2. **VISTA 的 visual goal synthesis 可替代纯文本意图**:空中抓取任务中,用目标图像引导比纯语言指令更精确
3. **跨物体泛化验证**:69% 成功率证明 WM 能桥接 novel object 的 zero-shot 泛化,与龙虾项目的跨场景泛化需求高度相关

**可落地实验点**:在龙虾现有 pipeline 中接入 VISTA 的 visual goal synthesizer,先用 WM 生成目标图像,再由 VLA 执行动作,看能否提升新场景泛化能力

**归档**:方向 01,已入库

### 2026-04-08 R527:**Action Images - WAM via Multiview Video Generation** (2604.06168) 【正式入库】

**核心贡献**:提出统一世界动作模型(WAM),将策略学习公式化为**多视角视频生成**问题。核心创新:把7-DoF动作编码为"动作图像"(多视角action video,像素级锚定),视频backbone本身即可zero-shot作为policy,无需separate action head。在RLOBench和真机上zero-shot成功率SOTA。

**对主人的价值**:
1. **像素级动作表示新路线**:与DIAL/LatentPilot的latent action路线正交--用视频生成格式统一表示动作像素,而非离散latent token
2. **多视角action video对齐龙虾场景**:龙虾项目多相机/手持D435i输入 → 多视角视频生成自然对应;Action Images的多视角策略可作为龙虾多相机数据融合的参考
3. **zero-shot泛化简化VLA pipeline**:无需separate action module即可zero-shot泛化,对龙虾项目的快速部署有直接价值

**与D01现有主线的区分**:DIAL(隐式intent bottleneck) / WAM(inverse dynamics) / OmniVTA(触觉融合) / PointWorld(3D点云预测) / Hierarchical Planning / RISE(想象式自改进) / DreamTIP(LLM引导invariant) 八足鼎立,Action Images补「像素级视频生成动作表示」新支线。

**可落地实验点**:在龙虾VLA pipeline中引入Action Images的多视角视频生成格式,看能否替代当前的action head输出;或多视角action video生成作为龙虾D435i多相机数据的中间表示层

**归档**:方向 01,已正式入库

### 2026-04-09 R540：**ABot-PhysWorld - Physics-Aligned World Foundation Model** (2603.23376) 【摘要级深挖入库】

**核心贡献**：提出 14B 机器人操作世界模型 **ABot-PhysWorld**，通过 physics-aware annotation + DPO 后训练 + decoupled discriminators，显式压制穿模、反重力等不合理操作视频；同时提出 **EZSbench**，把评测拆成 physical realism 与 action alignment 两条轴。

**对主人的价值**：
1. **补上“物理一致性训练”这块短板**：D01 现有主线更偏 latent planning / hierarchy，ABot-PhysWorld 提醒后训练阶段必须显式校正物理合理性
2. **与 WorldArena 形成闭环**：WorldArena 告诉我们“不能只看视频像不像”，ABot-PhysWorld 进一步给出“该怎么测物理一致性与动作对齐”的更细评测协议
3. **直接服务龙虾验收标准**：后续主人可把 sim-to-real/world model 验收拆成“动作对齐 + 物理可执行 + 安全约束满足”三项，而不是只看成功率

**可落地实验点**：先不复现 14B 大模型，而是在现有 WM / WAM 训练后增加一轮“物理偏好校正”，并把碰撞/穿模/越界作为负偏好样本；同时借鉴 EZSbench 思路设计空中操作 mini benchmark。

**归档**：方向 01，详见 `papers/2026-04-09_ABot-PhysWorld.md`

## 进展日志
- 2026-04-18 R824: 本轮按轮换继续推进 **D01**，依旧严格先看本地 L1 笔记与方向文档，重点回扫了 **WorldEval / Dream2Fix / WorldArena**，并再次确认本地方向覆盖已足够，因此没有触发 arXiv / Tavily 外扩；QMD 关键词检索 `world model route action triage recovery evaluator verifier` 也未返回稳定结果，本轮不把它作为结论来源。当前关键收束不是再补 D01 内部路由细节，而是把它正式写成可供 **D06 / D07** 消费的统一接口。已在 `REPORT.md` 新增 **4.12 D01→D06/D07 下游接口契约**，把 `rank_score / failure_state / route_action / stage_tag / risk_budget` 固化为跨方向安全路由字段，并在 `experiments.md` 新增 **E6 路由接口烟测**。当前判断是，D01 的论文主叙事又更稳了一步，它不需要证明自己替代下游规划器或控制器，只需要证明 **同一套 world-model-based route supervisor 能稳定服务导航与控制两条链**。
- 2026-04-18 R820: 本轮按轮换切回 **D01**，继续严格先看本地 L1 笔记与方向文档，重点回扫了近 30 天内的 **Dream2Fix / WorldEval / World-Gymnast / WoVR / ABot-PhysWorld / WorldArena**，确认本地方向覆盖已远超阈值，因此未触发 arXiv / Tavily 外扩；同时按流程尝试了 QMD 检索 `world model recovery verifier triage Dream2Fix`，但未返回稳定结果，本轮不把它作为结论来源。当前关键收束不是再补“恢复阶段划分”，而是把 **evaluator、分诊器、恢复器** 真正接成一条统一决策链。已在 `REPORT.md` 新增 **4.11 阶段感知分诊-恢复路由表**，并在 `experiments.md` 新增 **E5 阶段感知路由烟测**，正式把 D01 的主叙事从 `phase-bounded recovery` 再推进到 **stage-aware route_action**。当前判断是，D01 后续更像一个能输出 `rank_score + failure_state + route_action` 的部署前安全路由器，而不只是“会打分或会恢复”的世界模型。
- 2026-04-18 R819: 本轮按轮换切回 **D01**，继续严格先看本地 L1 笔记与方向文档，重点回扫了 **Dream2Fix** 与 **WorldEval** 两条已入库材料；本地方向覆盖已足够，因此没有触发 arXiv / Tavily 外扩。QMD 依旧因本机 `glslc` 缺失退化后不稳定，本轮只把它记为工具异常，不作为结论来源。当前关键收束不是再争论“recovery 要不要上”，而是明确 **不同飞行阶段允许的 recovery 类型不同**。已在 `REPORT.md` 新增 **4.10 分阶段恢复触发包线**，并在 `experiments.md` 新增 **E4 分阶段恢复包线烟测**，正式把 D01 的主叙事从“online recovery 准入门”再推进到 **phase-bounded recovery**。当前判断是，Dream2Fix-style recovery 默认应先绑定 `停悬/回锚` 场景，只有异常隔离、置信校准与时延预算同时过线后，才有资格讨论运动中在线恢复。

- 2026-04-18 R816: 本轮按轮换切回 **D01**，继续严格先看本地 L1 笔记与方向文档，重点回扫了 **Dream2Fix** 与 **WorldEval** 这两条已经足够稳定的恢复/评测支线；QMD 依旧因本机 `glslc` 缺失在 Vulkan 构建阶段退化后卡住，因此没有再依赖语义扩搜。本轮没有继续扩论文名录，而是把 `REPORT.md` 和 `experiments.md` 再往部署边界推进一步，新增 **4.9 恢复上线放行门（RG0~RG3）** 与 **E3 恢复上线放行烟测**，正式把 D01 的关键问题从“恢复率高不高”收束成“什么时候 recovery 只该做离线建议，什么时候才配进在线闭环”。当前判断是，D01 论文主线应继续锁在 **verifier → triage → recovery** 的部署前验收栈，但 recovery 默认先以 `offline recommendation` 身份存在，只有 `AER / RCS / 时延预算` 过线后才允许升为自动恢复。

- 2026-04-18 R812: 本轮按轮换继续推进 **D01**，但不再扩论文名录。回看本地方向笔记后，确认 Dream2Fix / PlayWorld / 失败分诊三条线已足够支撑本阶段主线，因此把精力转到 `REPORT.md` 的执行层，新增 **四周执行排期与判停规则** + **论文主叙事选择器**，把 D01 从“很多值得做的方向”压成一条可在 4 周内跑出 go/no-go 结论的推进路径。当前建议主叙事优先锁为 **部署前验收栈**：先做 evaluator + verifier + F1/F2 分诊 + Dream2Fix 恢复闭环，双动力学主干与 trainer-first 只在后续门槛通过后再升级。
- 2026-04-18 R802: 本轮按轮换回到 **D01**。Tavily 轻量补扫新增关注 **PlayWorld: Learning Robot World Models from Autonomous Play** (2603.09030)。它最值得保留的不是“又一个 video world model”，而是直接证明 **autonomous play + overnight unattended collection** 能显著提升 contact-rich dynamics fidelity、fine-grained policy evaluation 与 world-model RL 的真实收益，甚至在真机上带来 **最高 65% 成功率提升**。这把 D01 的一个关键判断又压实了一层：后续不能只比 `evaluator-first / action-centered / geometry-grounded` 主干，还要单列 **数据来源 sanity 轴**，专门比较 `success-biased demo`、`demo+autonomous play`、`demo+play+少量真实回放` 三档，先回答世界模型上限究竟主要卡在骨架还是交互覆盖度。已同步把该轴补入 `D01_世界模型/REPORT.md`。
- 2026-04-18 R798: 本轮按轮换回到 **D01**。Tavily 轻量补扫新增关注 **RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization** (2603.12639)。它最值得保留的不是“又一个 4D embodied world model”，而是把 **test-time predictive safeguard + imitation/evolutionary policy learning + open exploration policy learning** 明确压进同一套 world-model 优化框架，提醒 D01 后续不要把 `evaluator-first` 与 `trainer-first` 完全割裂，而应先让 **危险动作预筛** 站住，再逐步放行 imagined optimization。已同步把 `D01_世界模型/REPORT.md` 补成 **Gate-G0~G4 放行门与失败回查协议**，把接口层、预筛层、短程增益、长程稳定与部署候选串成一条可执行推进顺序。
- 2026-04-18 R794: 本轮按轮换回到 **D01**。Tavily 轻量补扫新增关注 **GigaWorld-Policy: An Efficient Action-Centered World-Action Model** (2603.17240)。它最值得保留的不是“又一个 WAM 变体”，而是把 world model 主干明确压成 **action-centered policy / planning backbone**，再次提醒 D01 后续不该只比较 rollout 视觉真实感，还要把 **action-centric closed-loop usefulness** 单列成基线层，专门比较 action-centered WAM、evaluator-first world model 与 geometry-grounded backbone 在策略排序、危险动作预筛和长时执行回稳上的差异。
- 2026-04-17 R788: 本轮补扫 **Robotic Manipulation is Vision-to-Geometry Mapping (f(v)→G)** (2604.12908)。它最值得保留的不是“再做一个几何 backbone”，而是明确提出 **joint action + 3D geometry prediction** 可能比 `joint action + 2D video prediction` 更适合作为 manipulation 世界模型底座，提醒 D01 后续不能只比较 video-WM 的 temporal realism，还应单列 **geometry-grounded action-state backbone** 这一轴，专门比较“2D 视频先验”与“3D 几何先验”谁更能稳住接触、可达性和跨视角泛化。
- 2026-04-17 R785: 本轮按轮换回到 **D01**。轻量回扫确认 **Grounded World Model for Semantically Generalizable Planning** (2604.11751) 的真正价值不只是“又一个世界模型”，而是把 **training-free rendering-based action tokenizer / embodiment-agnostic action-state interface** 正式变成可执行的接口层路线。已同步把 `D01_世界模型/REPORT.md` 补成 **C6 接口层设计草案 + I1-I4 最小实验矩阵**，让 D01 后续不再只比较“world model 主干强不强”，而是先回答“接口层本身能否减少跨载体重训、稳住 ranking correlation、并服务危险动作预筛”。
- 2026-04-17 R779: 本轮按轮换切到 **D01 + D04**。D01 轻量回扫新增关注 **Grounded World Model for Semantically Generalizable Planning** (2604.11751) 与 **PlayWorld** (2603.09030)。前者用 training-free、embodiment-agnostic 的 rendering-based action encoder，把 world model 直接接到语义泛化规划，并在新载体 xArm6 上给出零样本跨载体结果，说明 D01 的 `policy-to-latent action interface` 还可以继续往“语义接地 + 训练时零侵入”收束；后者强调 autonomous play data 对 contact-rich dynamics 的关键价值，进一步压实 D01 与 D05 的耦合点，即世界模型质量上限很可能首先受交互覆盖度而不是骨架复杂度约束。当前主线不改写，继续维持 `policy-to-latent interface / forward simulation / verifier-self-check / safety gate` 四层，并把 `semantically grounded action encoding` 作为候选接口支线。
- 2026-04-17 R782: 本轮按轮换切到 **D01 + D07**。D01 轻量回扫确认 **Grounded World Model for Semantically Generalizable Planning** (2604.11751) 值得从“候选接口”升级为 REPORT 内的正式实验轴：其 training-free、embodiment-agnostic rendering-based action encoder 很适合直接拿来对照现有 learnable action adapter，重点比较新载体上的 ranking correlation、危险动作过滤和接口重训成本。当前判断进一步收束为：D01 不只要验 `policy-to-latent interface` 有没有，还要验“这个接口是否足够语义接地、是否真能减少跨载体重训”。
- 2026-04-15 R733: 本轮按轮换切到 **D01 + D04**。D01 新增入库 **Lyra 2.0** (2604.13036, 2026-04-14): 可探索3D世界的视频生成WM，解决长程生成中spatial forgetting和temporal drifting问题——维护per-frame 3D几何做信息路由解决空间遗忘，用自增强历史训练校正时间漂移。对D01直接价值：空中场景持久WM的有力候选，提供"生成式探索+几何路由"架构，可与传统video diffusion WM互补。验收协议继续稳定：policy-to-latent interface / forward simulation / verifier-self-check / safety gate 四层。
- 2026-04-13 R664: 本轮按轮换切到 **D01 + D04**。D01 轻量补抓 **Mirage2Matter / A Physically Grounded Gaussian World Model from Video** (2602.00096)。它最值得保留的不是“又一个 3DGS world model”，而是把 **multi-view video reconstruction + physically realistic recovery + precision calibration target** 串成一条从真实视频直达可编辑仿真的桥，且明确追求 **零微调 sim-to-real**。新判断是：D01 后续除 **policy-to-latent action interface、verifier/self-check、physics alignment、safety gate** 外，还应单列 **video-to-simulator grounding / scale alignment overhead** 这一页，专门比较“视觉上像”是否真的能落到物理尺度、接触几何与可执行控制上，否则 world model 很容易停在好看的数字孪生而不是可部署训练器。
- 2026-04-11 R628: 本轮按轮换切到 **D01 + D04**。D01 补抓 **Event-Centric World Modeling with Memory-Augmented Retrieval for Embodied Decision-Making** (2604.07392)。它最值得保留的不是“又一个世界模型骨架”，而是把 **事件级语义抽象 + 记忆检索式 maneuver retrieval + physics-informed selection** 绑成可解释决策链，并明确在 **UAV flight scenarios** 下强调实时控制约束。新判断是：这条线更像 **retrieval planner / experience bank**，适合接到 D01 的 planner/evaluator 外围层，帮助把历史机动经验显式化；但它没有改写当前主线，后续统一验收仍应继续围绕 **policy-to-latent action adapter、verifier/self-check、physics alignment、safety-security-human factors** 四层展开。
- 2026-04-11 R623: 本轮按轮换切到 **D01 + D06**。D01 直接补抓 **WAV / World Action Verifier** (2604.01985) 摘要，关键信号比之前更硬了：它不是泛泛而谈 verifier，而是明确把 **state plausibility** 和 **action reachability** 拆开验证，并利用 **action-free video + sparse inverse model + cycle consistency** 做自校验，在 9 个任务上给出 **2x sample efficiency** 与 **18% downstream policy gain**。这进一步坐实了 D01 后续统一验收协议里，**reachability/self-check** 必须是独立层，而不能继续混在 rollout reward 或单纯 policy ranking correlation 里。
- 2026-04-11 R612: 本轮按轮换切到 **D01 + D07**。D01 未继续扩新论文名录，而是把近几轮判断进一步压成统一部署协议。当前最值得固定下来的不是“再找一个更强骨架”，而是把 **policy-to-latent action adapter、verifier/self-check、physics alignment、safety-security-human factors** 串成同一条验收链。后续应把 **原始动作输入 vs latent action 接口**、**是否有 reachability/self-check**、以及 **automation bias / trust calibration 风险** 作为同级变量一起比较，避免 evaluator 在系统层面看起来可靠、实际不敢上线。
- 2026-04-11 R606: 本轮按轮换切到 **D01 + D07**。D01 新增关注 **Safety, Security, and Cognitive Risks in World Models** (2604.01346)。它最值得吸收的不是再给一个新 world model 骨架，而是系统性提醒：D01 的 deployment-facing safety gate 不能只测 rollout 漂移与动作越权，还要单列 **训练数据/潜变量污染风险、compounding rollout error、automation bias / miscalibrated trust** 这几类风险。因此当前主线进一步收束为：除了 **trainer / planner / evaluator / verifier** 分层外，后续还应把 **safety-security-human factors** 做成单独验收页，避免 imagined simulator 在系统层面“看起来可靠、实际不敢上线”。
- 2026-04-10 R586: 本轮按轮换切到 **D01 + D04**。D01 复核 **WoVR** (2602.13977) 摘要后，进一步坐实 world model as trainer 的关键不只是 rollout 能不能跑，而是要单独控制 **hallucination depth**。当前最值得固化的三件事是 **Keyframe-Initialized Rollouts、world-model-policy co-evolution、controllable action-conditioned video world model**；同时它给出更硬的收益锚点，平均 **LIBERO 成功率 39.95%→69.2%**、真机 **61.7%→91.7%**。因此 D01 后续统一验收协议应把 **rollout reliability / keyframe re-anchor frequency / policy gain under imperfect simulator** 明确列成单独一层，而不是只看 imagined success 或视频质量
- 2026-04-10 R584: 本轮按轮换切到 **D01 + D04**。D01 继续补抓 **World Action Verifier / WAV** (2604.01985) 摘要，进一步确认世界模型后续不能只看 imagined rollout 是否“像”，而应把验收拆成 **state plausibility + action reachability** 两层 verifier/self-check。对当前主线最直接的推进是，把已有 **policy evaluation correlation / interactive simulator fidelity** 再补一层 **inverse-dynamics self-check**，专门覆盖 under-explored actions 与 OOD rollout，避免 world model 在稀疏动作区域里看起来合理但实际不可达
- 2026-04-10 R579: 本轮按轮换切到 **D01 + D07**。D01 新增关注 **OpenWorldLib** (2604.04707)。它更像“高级世界模型”的统一定义与推理框架，而不是新的具身控制主线，但价值仍然很明确：后续应把 **capability taxonomy / inference framework** 与 **任务效用验收** 分开写，避免把“具备交互、长期记忆、统一接口”误当成“已经能稳定支撑 trainer / planner / evaluator”。当前判断因此继续收束为，D01 最该推进的不是再堆新 world model 名字，而是把 **policy ranking correlation / interactive simulator fidelity / generated-data usefulness / safety alignment** 固化成统一验收协议。
- 2026-04-10 R576: 本轮按轮换切到 **D01 + D07**。D01 进一步确认 **Interactive World Simulator** (2603.08546) 与 **Evaluating Robot Policies in a World Model / WorldGym** (2506.00613) 属于同一条关键支线，即把 world model 从“能想象”推进到“能稳定交互、能产数据、还能做 policy evaluation”。当前最重要的新判断不是再追新模型，而是把 **policy ranking correlation / interactive simulator fidelity / generated-data usefulness** 三项写成统一验收协议；否则即使 rollout 很像，也未必真的能替主人筛策略。
- 2026-04-10 R573: 深夜 heartbeat 回扫 **Causal World Modeling / Ctrl-World / Evaluating Robot Policies in a World Model / WorldArena** 一线。可访问高位结果仍没有出现比现有主线更强的新分支，反而把 D01 的近期重点进一步钉死在 **trainer / planner / evaluator** 三类角色解耦验收上，尤其要把 **policy evaluation correlation** 和 **interactive simulator fidelity** 单独拉出来测，避免只看视频质量或 imagined 成功率。对主人当前最有价值的动作是先把“world model 评测结果与仿真/真机结果的一致性”写成统一验收项。
- 2026-04-10 R570: 新增关注 **Interactive World Simulator for Robot Policy Training and Evaluation** (2603.08546)。从可访问摘要看，它把 action-conditioned video world model 往 **可交互模拟器** 推进，重点补的是 **长时物理一致性 + 可复现 policy evaluation + 无需额外交互的数据生成**。这让 D01 的角色边界更清楚了，后续不只该把 world model 拆成 **trainer / planner / evaluator**，还应单独补一层 **interactive simulator fidelity** 验收，重点看 imagined interaction 是否真能稳定支撑策略筛选与离线评测。
- 2026-04-10 R568: 回扫 **JailWAM / DreamDojo / World-Gymnast / WoVR** 一线，暂未发现比现有主线更强的新分支，但进一步确认 D01 当前最该推进的不是继续堆新模型名，而是把 **trainer / planner / evaluator** 三类 world model 角色的统一验收协议写实，并把 **安全对齐 / 越权动作防护** 从附带项升级成独立验收门。
- 2026-04-09 R566: 结合定向检索结果回扫 **Causal World Modeling / World-Gymnast / WoVR** 一线，暂未发现比现有主线更强的新分支，但进一步确认 D01 当前最该推进的不是继续堆新模型名，而是把 **world model as trainer / planner / evaluator** 三类角色的统一验收协议写实，重点补 **在线适应、可靠 rollout、真实部署功能评测** 三条轴。
- 2026-04-09 R563: 回扫 **AdaWorldPolicy / Causal World Modeling / World-Gymnast / WoVR** 附近主线，并尝试补搜 2604 新论文。当前可访问结果里仍没有比现有主线更强的新分支，反而进一步确认了 D01 的近期重点应从“继续找新模型”转向“把 **world model as trainer / planner / evaluator** 三类角色做成统一验收协议”，尤其要补 **在线适应、可靠 rollout、真实部署功能评测** 三条轴。异常方面，本轮 DuckDuckGo 多次触发 bot challenge，`web_fetch` 直抓 arXiv 仍被私网解析拦截，因此 heartbeat 阶段更适合做定向回扫，不适合依赖全网新搜。
- 2026-04-09 R561: 新增关注 **AdaWorldPolicy** (2602.20057)，当前判断它的价值不在“又一个 diffusion policy”，而在于把 **world model 驱动 + 在线自适应学习** 绑成统一闭环，适合补 D01 里“真实扰动/环境变化下持续修正”的一条支线。对主人后续空中导航/空中操作很有用，因为真实场景下目标移动、风扰、视角变化都会逼着策略在线适应，而不是只做离线 rollout。
- 2026-04-09 R557: 继续回扫 2604 新结果，新增关注 **ManipArena** (2603.28545) 这条“真实世界统一验收”支线。它虽然不是 world model 本体方法，但价值很高,因为它把 **真实部署下的感知噪声、接触误差、恢复能力** 拉进统一 benchmark，进一步坐实 D01 后续不能只做仿真/视频级评测，必须补一层 **real-world functionality eval**，尤其适合主人后续把空中 world model / WAM 路线做成 mini benchmark。
- 2026-04-09 R551: 回扫 2604 新结果后，确认 **JailWAM** (2604.05498) 值得作为 D01 的安全验收支线关注。它不直接提升 world model 能力，但把 **WAM jailbreak 攻击、风险判别、闭环物理仿真验证** 系统化了，提醒主人后续若把 world model / WAM 接进真实控制，验收不能只看任务成功率与物理一致性，还要单独补一层 **安全对齐 / 越权动作防护**。
- 2026-04-09 R546: 摘要级补记 **Persistent Robot World Models** (2603.25685)，进一步确认 D01 不能只盯世界模型“会不会想象”，还得单独测 **multi-step rollout 稳定长度**；后续可把 rollout 长度-误差曲线、分段重置与关键帧回锚一起写入统一验收协议
- 2026-04-09 R544: 摘要级深挖 **WoVR** (2602.13977)，确认 D01 里“世界模型作为训练器”不能只看能不能训，还要单独验收 imagined rollout 的 **可靠深度**；关键启发是 **keyframe-initialized rollouts + world-model-policy co-evolution**，后续可转成主人空中任务里的“关键帧回锚”稳定化实验
- 2026-04-09 R541: 深挖入库 **World-Gymnast** (2602.02454)，确认 D01 不只是“世界模型做规划器”，还可直接做 **RL 训练器**；同时新增候选 **WoVR** (2602.13977)，补“可靠 rollout / 抗 hallucination”这条训练稳定性支线
- 2026-04-09 R540: 摘要级深挖入库 **ABot-PhysWorld** (2603.23376)，确认 D01 后续要补“physics alignment + 解耦验收协议”这条支线
- 2026-04-09 R538: 深挖入库 **WorldArena** (2602.08971) — 统一评测世界模型的感知质量、数据引擎、策略评估、动作规划三类能力，明确指出 perception-functionality gap；D01 后续实验应转向“功能优先验收”
- 2026-04-08 R533: 新增 **World-Gymnast / WoW** 候选，补足世界模型作为训练器与评测器两条线
- 2026-04-08 R531: 入库 **VISTA-WM**，确认“世界模型做高层规划 + VLA做低层执行”的分层路线
- 2026-04-13 R675: 本轮按轮换切到 **D01 + D04**。D01 轻量回扫 arXiv 后，新增关注：**Self-evolving Embodied AI** (2602.04411) — 提出 5-self 范式（memory/task/environment/embodiment/model 自更新），co-evolution 五环驱动持续适应；**WorldArena** (2602.08971) — 统一评测感知/策略评估/动作规划，明确 perception-functionality gap；**Modeling the Mental World** (2601.02378) — 心理世界建模综述；**A Comprehensive Survey on World Models for Embodied AI** (2510.16732) — 具身世界模型统一框架。整体判断：D01 主线（trainer/planner/evaluator + safety gate 四层验收）未受影响；Self-evolving 范式适合作为未来自主演进方向补入；Survey 类作教材参考，不作为创新源。

- 2026-04-14 R701: 本轮按轮换切到 **D01 + D04**。D01 新增候选 **DriveDreamer-Policy** (2604.01765) — 几何接地世界动作模型，统一 depth 生成 + 未来视频生成 + 运动规划，用 LLM 处理语言/图像/动作，三生成器并行输出。关键突破是把几何感知引入 world-action model，解决了 D01 识别的「纯 latent 缺几何锚定」问题。在 Navsim v1/v2 上验证。新判断：D01 验收协议里 **physics alignment / geometry grounding** 不只是可选支线，应与 policy ranking correlation、verifier/self-check、safety gate 并列成同级独立验收轴，对无人机场景尤为关键。

- 2026-04-17 R764: 本轮按轮换切到 **D01 + D06**。D01 新增入库 **EVA** (2603.17808): Executable Video Alignment——用IDM作为reward模型对齐视频WM与可执行动作之间的executability gap，RoboTwin和真实双手机器人上验证下游任务成功率提升。**关键意义**：与D01 C2/C4直接对齐——把physics alignment后训练（ABot-PhysWorld路线）与IDM reward对齐（EVA路线）结合，形成"先物理校正再动作对齐"的两阶段后训练，比单独做任一路线更完整。新增关注 **WAM vs VLA robustness study** (2603.22078)：系统比较WAM与VLA在LIBERO-Plus/RoboTwin 2.0上的鲁棒性，WAM对视觉/语言扰动显著更强，确认"video-prior + latent action decode"路线比端到端VLA更具部署鲁棒性。验收协议继续稳定：policy-to-latent interface / forward simulation / verifier-self-check / safety gate 四层，新增**executability-aligned post-training**为独立验收轴。
