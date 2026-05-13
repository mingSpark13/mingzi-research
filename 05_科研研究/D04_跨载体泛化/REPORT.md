# D04: 跨载体泛化 研究报告

> 最后更新：2026-04-20 | 成熟度：🟡中期（R851 已把接口通过后的首轮结果继续收束到“共享接口先成立，然后只允许在 geometry / morphology compensation / dynamics compensation 中冻结一条主补偿叙事”）
> 状态：🟡 推进中

> **R759 阶段更新**：① 新增 LAC-WM (ICLR 2026) — 统一 latent action space 机器人基础世界模型，验证 latent action 对齐在 scaling 下的 +46.7% 增益；② 创新点从 C1-C7 收束为四大轴；三/四节结构化重构；③ 新增统一实验对照表（Section 4）

> **R763 阶段更新**：① 新增 LAD (ICRA 2026) — Latent Action Diffusion for Cross-Embodiment Manipulation，扩散模型+latent action统一接口，ICRA 2026已接收；② 新增 Unified Latent Space for Humanoid Cross-Embodiment（arXiv:2601.15419），验证人型机器人共享latent表示可扩展性；③ 创新轴C（latent统一）获ICRA 2026直接验证，支撑更强；④ 深化轴C与轴D互补性论证

## Round 2026-05-12 12:21 CST | 方向: D04_跨载体泛化
- **D04_轻量扫描**：本轮按轮换继续覆盖 **D04 跨载体泛化**，满足近三轮继续覆盖 D01/D04/D06 且避免与上一轮主推进 **D07** 连续重复。严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md / 研究状态追踪`，并回扫本地近 30 天 D04 锚点 **GA3T / OmniRobotHome / FlexiTac / HandCDO / Breaking Lock-In / PokeVLA / VistaBot / AdaTracker**；补跑 QMD `cross embodiment demonstration translation contact-capable embodiment parameterization terrain-state completion --no-rerank` 后，结果仍主要回流 **PMI / 跨载体泛化概念页 / D04 README**，没有形成需要完整入库的新高价值论文，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- **D04_PAPER.md 推进**：本轮直接补强 `PAPER.md` 的 **Experiments**，新增 **4.2.18 Demonstration-Translation Completion before Interface Promotion** 与 **4.2.19 Minimal Sanity Toggle for Supervision-Side Completion**，并与后续 `4.2.20` 形成连续结果口径。核心新增是把一个此前只在 limitations 里出现、但还没进入实验协议的上游混淆项正式前置：如果跨载体路线的主要收益来自 **更贴近目标载体的演示翻译/重放/编辑监督**，那首先应记为 **demonstration-translation completion**，而不是更强的 geometry、latent 或 embodiment transfer。同步写入最小 sanity toggle：固定下游 stack，只比较 `raw source demonstrations → +state-completion controls → +embodiment-matched demonstration translation`；若 `DTC` 主导，reviewer-facing 口径必须停在 supervision-side completion。
- **核心价值**：这一步把 D04 从“会区分 terrain/contact/coordination completion”继续推进到“连 supervision 本身先被修好了，也不能偷算成 transfer interface 变强”。也就是说，D04 现在多了一个更靠前的 stop rule：**演示更对齐、场景更完整、接口更强** 这三种上游改进终于能在写作里拆开。
- **下轮建议**：按轮换优先切 **D01_世界模型** 或 **D06_空中视觉语言导航**；若继续回到 D04，优先统一 `4.2.18~4.2.20` 在全文中的重复编号与术语，并把 `DTC / STC / ITC` 压进唯一主表 schema。

## Round 2026-05-12 03:21 CST | 方向: D04_跨载体泛化
- **D04_轻量扫描**：本轮按轮换切回 **D04 跨载体泛化**，满足近三轮覆盖 D01/D04/D06 且避免与上一轮主推进 **D01** 连续重复。严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / REPORT.md`，并回扫近 30 天本地 D04 锚点 **GA3T / OmniRobotHome / FlexiTac / HandCDO / DexFormer / PokeVLA / VistaBot / Breaking Lock-In**。QMD 检索主题为 `cross-embodiment terrain-state completion coordination-state completion contact-interface enrichment mixed ground aerial transfer --no-rerank`，结果因会话超时未取回稳定文本；但结合本地方向已有覆盖远超 3 篇，当前增量已足够支撑写作推进，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- **D04_PAPER.md 推进**：本轮直接补强 `PAPER.md` 的 **Section 4.2**，新增 **4.2.18 First-Pass State-Completion Freeze before Transfer Promotion** 与 **4.2.19 Terrain-First Residual Readout for Mixed Ground--Aerial Transfer**。核心写入了 first-pass 诚实冻结协议：主表必须显式报告 `(TSG, CIG, CSC, TSR, weakest_tag)`，并规定 mixed ground--aerial 增益要先经过 **terrain-state completion / contact-interface enrichment / coordination-state completion** 三层解释过滤，只有剩余 `TSR` 才允许升级到 latent-transition sufficiency、policy-interface transfer 或 embodiment-residual recovery 叙事。
- **核心价值**：这一步把 D04 从“知道 terrain/contact/coordination 是 confound”推进到“知道主实验表第一轮到底该怎样停在 weakest sufficient explanation”。尤其是 GA3T、FlexiTac、OmniRobotHome、HandCDO 这组本地证据，现在不再只是 Related Work 旁证，而是被正式压成 **Results 级别的 first-pass 记账协议**。
- **下轮建议**：按轮换优先切 **D06_空中视觉语言导航** 或 **D07_Isaac强化学习机械臂控制**；若继续回 D04，优先统一 `4.2.17-4.2.22` 的编号与术语，顺手清理重复小节。

## Round 2026-05-11 01:59 CST | 方向: D04_跨载体泛化
- **D04_轻量扫描**：本轮按轮换切回 **D04 跨载体泛化**，满足近三轮覆盖 D01/D04/D06 且避免与上一轮主推进 **D06** 连续重复。严格先做本地优先：复核 `README.md / PAPER.md / OWNER_NOTES.md / 研究状态追踪 / REPORT.md`，并回扫本地近 30 天 D04 锚点 **Breaking Lock-In / AdaTracker / PokeVLA / VistaBot / FlexiTac / OmniRobotHome / HandCDO / GA3T / DexFormer**；同时交叉参考 D06 近期 `PAPER.md` 中关于 **controller-consumption / delayed-consumption honesty** 的写法，用来约束 D04 的 mixed ground--aerial 归因边界。受当前 cron allowlist 限制，QMD 与外部补查未能成功执行；结合本地方向覆盖已明显超过 3 篇且当前增量仍集中在 mixed ground–aerial attribution discipline，因此本轮 **高价值新增论文 0 篇，正式入库 0 篇**，未触发 arXiv / Tavily 外扩。
- **D04_PAPER.md 推进**：本轮直接补强 `PAPER.md` 的 **Abstract + Experiments**。一是重写 `Abstract` 的度量与 claim 纪律，把预注册元组从旧版 `(TR, IGS, LTS, MCG, DRB, VGS-xEmb, OC)` 扩展到 `(TR, IGS, LTS, MCG, DRB, VGS-xEmb, CIG, CSC, TSG, TSR, PTL, GRS, OC)`，并明确 mixed ground--aerial 结果必须先穿过 **terrain-state completion / contact-interface enrichment / coordination-state completion** 再允许升级。二是在 `4.2` 新增 **4.2.26 Cross-Direction Boundary: Transferred Packet Readiness versus Delayed Aerial Uptake**，把 D06 近期强调的 **controller-consumption / delayed aerial uptake honesty** 引入 D04：若共享几何与 latent packet 只把收益可靠地带到 pre-stabilization 边界，而最终成功差值是在后续 aerial rescue 才被真正消费，就必须冻结为 **transferred packet readiness with delayed aerial uptake**，不能膨胀成完整 cross-embodiment sufficiency。
- **核心价值**：这一步把 D04 从“知道 terrain/contact/coordination 都可能是 confound”进一步推进到“知道 mixed ground--aerial transfer 与 late aerial rescue 的边界到底该怎么在摘要和 Results 里收口”。也就是说，D04 现在不仅有 terrain-first / contact-first / coordination-first 的 first-pass discipline，还正式继承了 D06 的 **consumption-time honesty**：早期跨载体可迁移的 packet 结构可以被肯定，但若 decisive gain 只在后续 aerial stabilization 被消费，就必须老实写成 **bounded downstream uptake**。
- **下轮建议**：按轮换优先切 **D01_世界模型** 或 **D07_Isaac强化学习机械臂控制**；若继续回到 D04，优先统一 `Conclusion / 4.2.23-4.2.26` 的术语，并顺手清理重复的 `4.2.11-4.2.18` 历史块。

## 最新扫描（R910）

- **本地回扫**：本轮按轮换主推进 **D04 跨载体泛化**，满足“三轮内覆盖 D01/D04/D06 至少一个”且避免与上一轮主推进 **D01** 连续重复。先读 `OWNER_NOTES.md`（当前无新批注），再复核 `README.md`、`PAPER.md` 与近 30 天本地 L1 锚点 **DexFormer / AdaTracker / JoyAI-RA 0.1 / Breaking Lock-In / VistaBot / ResVLA / UniT / PokeVLA**；补跑 QMD `cross-embodiment morphology temporal residual history-conditioned inference --no-rerank` 后，结果继续主要回流 **DexFormer** 与既有 D04 状态追踪，说明本轮最有价值的增量仍不是扩新论文，而是把 **low-data adaptation / steerability collapse** 正式纳入 D04 的解释协议。由于本地相关覆盖已充足，本轮 **高价值新增外部论文 0 篇，正式入库 0 篇**。
- **PAPER.md 推进**：本轮直接补强 `D04/PAPER.md` 的 experiments 区：在 **Section 4.2.3** 新增 **post-training steerability guard**，明确 low-data adaptation 下若 `IGS` 与 rollout-window 归因基本稳定，但 object/spatial steerability 崩塌，则必须冻结为 **post-training lock-in under scarce target data**，不能误写成共享接口或 embodiment prior 失效；同时新增 **Section 4.2.4 Low-Data Adaptation and Steerability Preservation Control**，引入 `SRA (Steerability Retention under Adaptation)`，把 `no adaptation / naive low-data adaptation / steerability-preserving adaptation` 三档写成首轮对照协议。
- **本轮结论**：本轮没有新增正式入库论文；核心产出是把 D04 从“知道 morphology-aware gain 该按 static prior / temporal residual / mixed 拆账”继续推进到 **知道 low-data post-training lock-in 什么时候会伪装成 embodiment bottleneck**，从而让首轮结果在 foundation-scale、cross-view、rollout-window 之外，多了一层 **adaptation-time steerability** 负控。
- **下轮建议**：按轮换优先切 **D06_空中视觉语言导航** 或 **D07_Isaac强化学习机械臂控制**；若继续回到 D04，优先统一 `Abstract / Conclusion / 4.2.4` 的 steerability 术语，并顺手清理 `[REF]` 占位。

## 最新扫描（R909）

- **本地回扫**：本轮按轮换主推进 **D04 跨载体泛化**，满足“三轮内覆盖 D01/D04/D06 至少一个”，且避免与上一轮继续停在同一方向。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与近 30 天本地锚点 **Embedding Morphology into Transformers / DexFormer / AdaTracker / JoyAI-RA 0.1 / ResVLA**；当前主判断继续稳定：D04 里的 morphology-aware 结果不能只停留在 `SMG / HIG / TER` 三指标层，还必须进一步冻结成论文级结论路由。
- **QMD 本地检索**：补跑 `qmd query "cross-embodiment dexformer history-conditioned morphology inference residual refinement" --no-rerank`，结果继续主要回流 **Embedding Morphology into Transformers** 与既有 D04 状态追踪，说明当前最有价值的推进不是再扩新论文，而是把 morphology-aware 家族的 route-freezing 写成明确规则。
- **外部补充**：由于本地覆盖已超过 3 篇且当前增量集中在实验记账与结论收束，本轮不再扩 arXiv/Tavily；**高价值新增外部论文 0 篇，新增正式入库 0 篇**。
- **PAPER.md 推进**：本轮直接补强 `D04/PAPER.md`，在 **Section 4.2.2** 后新增 **Section 4.2.3 Route-Freezing Rule for Morphology-Aware Conclusions**。具体把 morphology-aware family 的论文级结论正式冻结成三路：`Route M1 static prior sufficient / Route M2 temporal embodiment residual recovery / Route M3 mixed embodiment adaptation`，并要求 `SMG / HIG / TER` 与 `{static prior, temporal residual, mixed}` attribution tag 在 interpolation / extrapolation / composition 三种 split 下稳定后，才允许把 embodiment-aware adaptation 升格为论文主结论。
- **本轮结论**：本轮没有新增正式入库论文；核心产出是把 D04 从“知道 static morphology 与 history inference 要拆账”继续推进到 **知道 morphology-aware 论文最终该怎么冻结结论，避免把局部时序补救误写成普适 embodiment gain**。下轮建议优先统一 `Abstract / Conclusion / 4.2.3` 的 route wording，并顺手清理 `[REF]` 占位。

## 最新扫描（R907）

- **本地回扫**：本轮按轮换主推进 **D04 跨载体泛化**，满足“三轮内覆盖 D01/D04/D06 至少一个”，且避免与上一轮继续锁在同一段 D04 子结论上。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与近 30 天本地锚点 **Embedding Morphology into Transformers / DexFormer / AdaTracker / ResVLA / JoyAI-RA 0.1 / LAD**；当前主判断继续稳定：D04 里 morphology-aware 家族必须拆成 **静态 morphology 先验**、**history-conditioned embodiment inference**、**temporal embodiment residual** 三层归因，不能再统记成一个 residual bucket。
- **QMD 本地检索**：补跑 `qmd query "cross-embodiment dexformer history-conditioned morphology inference residual refinement" --no-rerank`，结果主要回流 **Embedding Morphology into Transformers** 与既有 D04 研究状态，说明当前最有价值的推进不是补新外部论文，而是把“显式 morphology conditioning vs 在线 history inference”正式写成实验判别门。
- **外部补充**：由于本地已命中相关笔记且覆盖超过 3 篇，本轮不再扩 arXiv/Tavily；**高价值新增外部论文 0 篇，新增正式入库 0 篇**。
- **PAPER.md 推进**：本轮直接补强 `D04/PAPER.md` 的 **Section 4.2.2 Static Morphology Priors vs. History-Conditioned Embodiment Inference**。除既有 `SMG / HIG / TER` 三指标外，进一步写入首轮 ablation 结构：`+ static morphology token / + topology bias / + history-conditioned inference / + static+history hybrid residual` 四行，并要求每行携带 `{static prior, temporal residual, mixed}` attribution tag；只有该 tag 在 interpolation / extrapolation / composition 三种 split 下都稳定，才允许把 embodiment-aware adaptation 升格为论文主结论。
- **本轮结论**：本轮没有新增正式入库论文；核心产出是把 D04 从“知道 DexFormer/AdaTracker 有用”继续推进到 **知道静态 morphology、history inference、temporal residual 在 experiments 主表里该怎么拆账与路由**。下轮建议优先统一 `Section 3.5`、`Section 4.2.2` 与 `References` 中的 DexFormer/Embedding Morphology 占位格式。

## 最新扫描（R906）

- **本地回扫**：本轮按轮换继续主推进 **D04 跨载体泛化**，满足“三轮内覆盖 D01/D04/D06 至少一个”，且避免与上一轮 D06 连续重复。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与近 30 天本地锚点 **DexFormer / Embedding Morphology into Transformers / AdaTracker / ResVLA / JoyAI-RA 0.1 / LAD**；当前主判断继续稳定：D04 不能把 morphology-aware 方法统称为一个桶，而要明确拆成 **静态 morphology 先验**、**history-conditioned embodiment inference**、**temporal residual recovery** 三层归因。
- **QMD 本地检索**：补跑 `qmd query "cross-embodiment dexformer history-conditioned morphology inference residual refinement" --no-rerank`，结果主要回流 **Embedding Morphology into Transformers** 与既有 D04 研究状态，说明当前最有价值的推进不是补新外部论文，而是把“显式 morphology conditioning vs 在线 history inference”的实验判别门写进论文正文。
- **外部补充**：由于本地已命中相关笔记且覆盖超过 3 篇，本轮不再扩 arXiv/Tavily；**高价值新增外部论文 0 篇，新增正式入库 0 篇**。
- **PAPER.md 推进**：本轮直接补强 `D04/PAPER.md` 的 **Section 4.2.2 Static Morphology Priors vs. History-Conditioned Embodiment Inference**。具体新增 `SMG / HIG / TER` 三个 attribution 指标：分别对应静态 morphology 增益、history-conditioned inference 增益、temporal embodiment residual；并写死路由规则——若 `SMG` 为主，则论文应收成“静态 embodiment prior 已足够”，若 `HIG` 为主且收益集中在 `TER`，则必须记为 **temporal embodiment residual recovery**，不能直接夸大成“更强 embodiment representation”。
- **本轮结论**：本轮没有新增正式入库论文；核心产出是把 D04 从“知道 DexFormer/AdaTracker 有用”继续推进到 **知道 morphology token、history inference、temporal residual 在 experiments 里该怎么拆账**。下轮建议优先统一 `Section 3.5` 与 `Section 4.2.2` 的术语，并开始补 References 编号。

## 最新扫描（R905）

- **本地回扫**：本轮按轮换继续主推进 **D04 跨载体泛化**，满足“三轮内覆盖 D01/D04/D06 至少一个”且避免与上一轮 D06 连续重复。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与近 30 天本地锚点 **DexFormer / LAD / UniT / AdaTracker / JoyAI-RA 0.1 / VistaBot / ResVLA**；当前主判断继续稳定：D04 仍应坚持 `shared geometry → latent sufficiency → intent-anchored residual refinement / embodiment residual / dynamics residual` 的单向升级顺序，不能把 history-conditioned adaptation 与 morphology-aware gain 混成同一层解释。
- **QMD 本地检索**：补跑 `qmd query "cross-embodiment generalization morphology invariance policy" --no-rerank`，结果主要回流 **DexFormer** 与既有 D04 研究状态，说明当前本地方向新增最有价值的不是新外部论文，而是要把“静态 morphology token”与“在线 history-conditioned embodiment inference”这条边界写清楚。
- **外部补充**：由于本地已命中相关笔记且覆盖超过 3 篇，本轮不再额外扩 arXiv/Tavily，避免把有限预算耗在低相关候选上；**高价值新增外部论文 0 篇，新增正式入库 0 篇**。
- **PAPER.md 推进**：本轮直接补强 `D04/PAPER.md` 的 **Section 2.3 Morphology-Aware Approaches** 与 **Section 2.13 Limitations**。具体把 **DexFormer** 正式写入 morphology-aware 路线，强调其价值不只是“又一个跨载体灵巧手策略”，而是提供了 **history-conditioned online embodiment inference** 证据：残余 transfer gap 可能来自时间变化的 embodiment/dynamics 约束，而不只是静态 morphology label 缺失；同时新增 limitation，明确现有 morphology-aware 工作普遍没有把 **静态形态描述** 与 **时序残差适应** 分开检验。
- **本轮结论**：本轮没有新增正式入库论文；核心产出是把 D04 从“知道 morphology-aware 有用”继续推进到 **知道 morphology token、history-conditioned adaptation、intent-anchored refinement 三者在论文里该怎么分层记账**。下轮建议优先统一正文 `DexFormer / AdaTracker / ResVLA` 三者在 Method 3.5 与 Experiments 4.2 的归因口径。

## 最新扫描（R899）

- **本地回扫**：本轮按轮换继续主推进 **D04 跨载体泛化**，满足“每 3 轮覆盖 D01/D04/D06 至少一个”，且避免切回刚重压的 D01/D06。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与近 30 天本地锚点 **UniT / AdaTracker / JoyAI-RA 0.1 / LAD / X-Sim / PointBridge / DeFM / GaussFly**；当前主判断继续稳定：D04 仍应坚持 `shared geometry → latent sufficiency → intent-anchored residual refinement / embodiment residual / dynamics residual` 的单向升级顺序，不能把 scale、history-conditioned adaptation 与 aerial rescue 混成并列主贡献。
- **QMD 本地检索**：补跑 `qmd query "cross embodiment shared geometry latent action aerial manipulation" --no-rerank`，结果继续主要回流 **LAD** 与既有研究状态，说明本地方向暂无足以改写主叙事的新结构性证据。
- **arXiv 外查**：按规则补做 Export API 外查，最新返回 **LoHo-Manip (2604.21924)**、**VistaBot (2604.21914)**、**ResVLA (2604.21391)**。其中前两者更偏 long-horizon planning / cross-view robustness，作为 D04 的 guardrail 旁证保留；**ResVLA** 继续支持把“stable low-frequency intent”与“high-frequency embodiment recovery”分开记账。本轮 **高价值新增旁证 1 篇（ResVLA），新增正式入库 0 篇**。
- **PAPER.md 推进**：本轮主推进 `D04/PAPER.md` 的 **Abstract** 与 **Section 4** 去重清理。具体补写了完整 abstract 草稿，把论文主张压缩成 `shared geometry packet + latent retargeting + residual escalation rule + four-way narrative routing`；同时删除了重复的 **4.2.1 Heterogeneous Pretraining Saturation and Narrative Routing** 段落，避免正文结构继续膨胀和自我重复。
- **本轮结论**：本轮没有新增正式入库论文；核心产出是把 D04 从“只有章节级骨架”推进到 **可直接继续精修的 abstract + 干净的 experiments 结构**。下轮建议优先统一正文 `[REF]` 占位与 References 编号，再把 abstract 里的四选一路由压缩成 title/intro 默认句式。

## 最新扫描（R898）

- **本地回扫**：本轮按轮换继续主推进 **D04 跨载体泛化**，满足“每 3 轮覆盖 D01/D04/D06 之一”，且避免切回刚连续重压的 D01/D06。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与本地锚点 **LAD / UniT / AdaTracker / JoyAI-RA 0.1 / X-Sim / PointBridge / DeFM / GaussFly**；当前主判断继续稳定：D04 仍应坚持 `shared geometry → latent sufficiency → intent-anchored residual refinement / embodiment residual / dynamics residual` 的单向升级顺序，不能把 scale、history adaptation 与 aerial rescue 混成并列主贡献。
- **QMD 本地检索**：补跑 `qmd query "cross embodiment shared geometry latent action aerial manipulation" --no-rerank`，结果继续主要回流 **LAD** 与既有研究状态，说明本地方向暂无足以改写主叙事的新结构性证据。
- **arXiv 外查**：按规则补做 Export API 外查，最新返回 **LoHo-Manip (2604.21924)**、**VistaBot (2604.21914)**、**Hi-WM (2604.21741)**。三者分别偏 long-horizon planning、cross-view robustness 与 world-model post-training，与 D04 当前 cross-embodiment 主链贴合度有限，因此本轮 **高价值新论文 0 篇，新增正式入库 0 篇**。
- **PAPER.md 推进**：本轮主推进 `D04/PAPER.md` 的 **Section 2.13 Limitations** 与 **Section 5 Conclusion**。具体补入一条 limitation，明确现有工作很少区分“shared intent 已稳”与“只是高频 residual policy 更强”；同时把结论段正式升级为 **四选一路由**：`shared geometry not yet established / shared geometry + latent sufficiency / intent-anchored residual refinement / embodiment-or-dynamics bottleneck`，让首轮实验后论文标题和摘要有可执行的诚实收束规则。
- **本轮结论**：本轮没有新增正式入库论文；核心产出是把 D04 从“概念上知道该怎么分流”继续压到 **PAPER.md 结论级 narrative routing**。下轮建议优先统一正文 `[REF]` 占位与 References 编号，并把这套四选一路由压缩进 abstract 草稿。

## 最新扫描（R897）

- **本地回扫**：本轮按轮换继续主推进 **D04 跨载体泛化**，满足“每 3 轮覆盖 D01/D04/D06 之一”，且避免切回上一轮已重压的 D04 子结论复述。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与本地锚点 **UniT / AdaTracker / JoyAI-RA 0.1 / LAD / X-Sim / PointBridge / DeFM / GaussFly**；当前主判断继续稳定：D04 仍应坚持 `shared geometry → latent sufficiency → embodiment residual → dynamics residual` 的单向升级顺序，不能把 heterogeneous pretraining、history-conditioned adaptation 与 aerial rescue 混成并列主贡献。
- **QMD 本地检索**：补跑 `qmd query "cross embodiment shared geometry latent action aerial manipulation" --no-rerank`，结果继续主要回流 **LAD** 与既有研究状态，说明本地方向暂无足以改写主叙事的新结构性证据。
- **arXiv 外查**：按规则补做 Export API 外查，最新返回 **LoHo-Manip (2604.21924)**、**VistaBot (2604.21914)**、**ResVLA (2604.21391)**。其中前两者更偏 long-horizon planning / cross-view robustness，与 D04 主链贴合度有限；**ResVLA** 虽不是直接的 cross-embodiment 方法，但其 **intent anchor + residual refinement** 分解，正好可作为 D04 区分“shared latent sufficiency”与“intent-stable but embodiment-specific high-frequency recovery”的新旁证，因此本轮记为 **高价值旁证论文 1 篇（ResVLA），新增正式入库 0 篇**。
- **PAPER.md 推进**：本轮主推进 `D04/PAPER.md` 的 **Section 2.13 / 5 Conclusion**。具体新增一条 limitation，明确当前文献普遍没有区分 **latent-transition sufficiency** 与 **intent-stable residual refinement**；同时改写 conclusion，把 D04 的最终落点从三选一（shared latent / embodiment compensation / dynamics bottleneck）扩展为四选一路由：在 latent 已稳但高频修正仍明显时，应单独收成 **intent-anchored residual refinement**，避免把 shared intent 与 embodiment-specific recovery 混写成一层。
- **本轮结论**：本轮没有新增正式入库论文，也没有继续扩 paper map；核心是把 D04 的论文终局判断再压实一层——以后首轮实验若出现“低频子目标结构稳定、但高频控制仍需 residual bridge”，就不再硬塞进 latent sufficiency 或 full embodiment compensation 里。下轮建议优先统一正文 `[REF]` 占位与 References 编号，再把这个四选一 narrative routing 压缩进 abstract 草稿。

## 最新扫描（R896）

- **本地回扫**：本轮按轮换继续主推进 **D04 跨载体泛化**，并满足“每 3 轮覆盖 D01/D04/D06 之一”的约束。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与本地锚点 **LAD / UniT / AdaTracker / JoyAI-RA 0.1 / X-Sim / PointBridge / DeFM / GaussFly**；当前主判断继续稳定：D04 仍应坚持 `shared geometry → latent sufficiency → morphology residual → dynamics residual` 的单向升级顺序，不能把 human anchor、history-conditioned adaptation、heterogeneous pretraining 与 aerial rescue 混成并列主贡献。
- **QMD 本地检索**：补跑 `qmd query "cross embodiment shared geometry latent action aerial manipulation" --no-rerank`，结果继续主要回流 **LAD** 与 D04 既有研究状态，说明本地方向暂无足以改写主叙事的新结构性证据。
- **arXiv 外查**：按规则补做 Export API 外查，最新返回 **LoHo-Manip (2604.21924)**、**VistaBot (2604.21914)**、**Hi-WM (2604.21741)**。三者分别偏 long-horizon VLA planning、cross-view robustness 与 world-model post-training，和 D04 当前“cross-embodiment shared geometry + latent interface”主链贴合度有限，因此本轮 **高价值新论文 0 篇，新增正式入库 0 篇**；但已将其登记进 `PAPER.md` references 备用，避免后续需要时重复补链。
- **PAPER.md 推进**：本轮主推进 `D04/PAPER.md` 的 **Section 4 Experiments**，新增 **4.2.1 Heterogeneous Pretraining Saturation and Narrative Routing**。核心是把 **JoyAI-RA-style heterogeneous pretraining baseline** 从普通 strong baseline 升级为“论文叙事分流器”：若大规模异构预训练 + 统一动作格式已基本吃掉 transfer gain，则 D04 应收成 *interface verification / attribution* 论文；若 scale 后 residual 仍明显存在，则继续维持 `geometry → latent → residual` 的 staged explanation。
- **本轮结论**：本轮没有新增入库论文，但把 D04 最缺的一块——**强基线赢了以后，论文到底怎么改口径**——正式写进 `PAPER.md`。下轮建议优先补 **正文 [REF] 占位与 References 编号统一**，再把 `Route A/B/C` 压缩进摘要与 conclusion 的默认句式。

## 最新扫描（R895）

- **本地回扫**：本轮按轮换继续主推进 **D04 跨载体泛化**，避免与上一轮重复 D04/D01 冲突的风险，且满足“每 3 轮覆盖 D01/D04/D06 之一”。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与近 30 天本地锚点 **UniT / X-Sim / PointBridge / DeFM / GaussFly / RAFL / Master Key**；当前主判断继续稳定：D04 的论文主体仍应坚持 `shared geometry → latent sufficiency → morphology residual → dynamics residual` 的单向升级顺序，不能把 human anchor、compact VLA、aerial rescue 同时写成并列主贡献来源。
- **QMD 本地检索**：补跑 `qmd query "cross-embodiment generalization sim2real morphology transfer UAV robot" --no-rerank`，结果继续主要回流 **D04 README**、**HEX**、**Octo** 与 `Sim2Real` 概念页；说明本地方向的新信息仍主要集中在已有 D04 主链，没有出现必须立即完整入库的新本地论文。
- **arXiv 外查**：按规则补做 Export API 外查，但请求再次遭遇 **HTTP 429** 限流，因此本轮保持“外查失败不伪造结论”的策略，不凭不稳定返回强行扩图谱。综合判断为 **高价值新论文 0 篇，新增正式入库 0 篇**。
- **PAPER.md 推进**：本轮主推进 `D04/PAPER.md` 的 **Section 2 Related Work**。具体新增 **2.9 Shared Human-Robot Physical Intent Tokens** 小节，把 **UniT** 从原先只在 latent-interface 段落里一笔带过，提升为独立论据：它支持把 `human demonstration → physical intent token → embodiment-specific recovery` 视作单独的解释层，有助于我们把 human anchors 明确记为“结构化接口监督”而不是松散预训练噪声；同时将后续的 morphology / dynamics 模块重新压回 residual execution 层。
- **本轮结论**：D04 这轮没有扩论文数量，而是把 **human→robot 统一 physical intent** 这条论据正式写进 PAPER 主体，让“共享几何 + latent 接口能否同时桥接 human 与 robot 数据”更像一个可检验论文命题。下轮建议继续补 **References 与 [REF] 占位统一**，并把 `3.4/3.5` 与 `4.2` 的 human-anchor 术语再完全对齐。

## 最新扫描（R894）

- **本地回扫**：本轮按轮换继续主推进 **D04 跨载体泛化**，避免与上一轮重复 D01，并满足“每 3 轮覆盖 D01/D04/D06 之一”。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与近 30 天本地锚点 **UniT / X-Sim / PointBridge / DeFM / GaussFly / RAFL**；当前主判断继续稳定：D04 的论文主体不该再把 geometry bridge、latent interface、morphology compensation 和 aerial dynamics rescue 混成同一层解释，而应坚持 `shared geometry → latent sufficiency → morphology residual → dynamics residual` 的单向升级顺序。
- **QMD 本地检索**：补跑 `qmd query "cross-embodiment generalization sim2real morphology transfer UAV robot" --no-rerank`，结果继续主要回流 **D04 README / HEX / Octo / Sim2Real 概念页**，说明本地方向的高价值增量仍主要集中在既有 D04 主链，没有出现必须立即完整入库的新本地论文。
- **arXiv 外查**：按规则补做 Export API 外查，最新返回里最值得保留的是 **PokeVLA (2604.20834)**。它虽然不是专门的 cross-embodiment 论文，但其 **multi-view geometry alignment + action expert** 设计，正好给 D04 当前“空间锚定的 latent/action interface”叙事补了一条 manipulation foundation model 侧的近期旁证；其余 **ALAS / VTouch++** 与 D04 当前主叙事贴合度较弱，本轮不升格为主线候选。**高价值外部候选新增 1 篇（PokeVLA），新增正式入库 0 篇。**
- **PAPER.md 推进**：本轮主推进 `D04/PAPER.md` 的 **Section 2.4 / 3.3 / 4.2 / References**。具体把 **PokeVLA** 写入 *Latent Action Interfaces* 相关工作，明确其价值在于“先做空间语义/几何对齐，再进入 action 专家路由”；同时在 *Method 3.3* 里把它转化为我们为何坚持“geometry-conditioned latent interface”而不是“纯 command-conditioned latent”的方法学支撑，并在 *Main Results 4.2* 中新增一个 **compact spatial-semantic baseline** 对照位，用来测试 `LTS` 能否在不开 morphology/dynamics 模块时先提升。
- **本轮结论**：D04 这轮没有继续扩论文名录，而是把一个最新 manipulation foundation model 证据压进现有主线，使 `shared geometry + latent sufficiency` 叙事更完整。下轮建议继续补 **References 与 [REF] 占位统一**，并把 `experiments.md` 里的 baseline 名称与 `PAPER.md 4.2/4.4` 对齐。

## 最新扫描（R892）

- **本地回扫**：本轮按轮换切到 **D04 跨载体泛化**，满足“每 3 轮至少覆盖 D01/D04/D06 之一”，并避免与上一轮 **D01** 连续重复。先复核 `D04/README.md`、`PAPER.md`、`REPORT.md` 与近 30 天本地 L1 锚点 **PointBridge / DeFM / GaussFly / RAFL**；当前判断更稳：**PointBridge / DeFM / GaussFly** 应统一归到 `shared geometry / representation bridge` 层，只能先回答“几何接口是否已经立住”，不能越级写成 morphology compensation 或 dynamics adaptation 的主证据。
- **QMD 本地检索**：补跑 `qmd query "cross embodiment shared geometry latent sufficiency morphology compensation dynamics gap aerial manipulation" --no-rerank`，结果继续主要回流 **Unified Latent Space / LAD / D04 既有文档**，说明 D04 当前本地增量仍集中在 `shared geometry → shared latent sufficiency → dynamics residual ordering` 主链，未出现足以触发完整入库的新高价值论文。
- **arXiv 外查**：本轮 Export API 查询未返回稳定新结果（空响应），因此不凭不完整外部结果强行更新论文图谱；综合判断为 **高价值新论文 0 篇，新增入库 0 篇**。
- **PAPER.md 推进**：本轮主推进 `D04/PAPER.md`。在 **Section 2 Related Work** 新增 **2.8 Real-to-Sim Geometry Anchors from Human Video**，把 **X-Sim (2505.07096)** 正式纳入相关工作，明确其价值不只是数据便宜，而是把 human video 变成 `task geometry / subgoal ordering / contact preparation` 的结构化接口监督；同时把 **Section 3 Method** 扩展出 **3.5 Real-to-Sim-to-Real Geometry Anchoring for Heterogeneous Sources**，把 human → sim relabel → robot supervision 写成我们方法里的真实模块，而不是停留在 REPORT 讨论层。进一步地，**4.2 Main Results** 也补入了与 D06 的记账边界：若 aerial 收益只在 payload/stability guidance 打开后才出现，就统一记为 dynamics-residual recovery，而不是额外跨载体增益。
- **本轮结论**：D04 这一轮不靠外查扩论文名录，核心是把 **human geometry anchor / real-to-sim-to-real** 正式抬进 PAPER 主体，让“共享几何 + latent 接口是否真的能同时吃下 human 与 robot 数据”变成可验证主张。下轮建议继续补 **References** 完整化，顺手把 `4.4/4.5` 与 `experiments.md` 的 SC0-SC4 指标命名再统一一遍。

## 最新扫描（R889）

- **本地回扫**：本轮按轮换主推进 **D04 跨载体泛化**，先复核 `D04/README.md`、`REPORT.md` 与近 30 天 D04 本地笔记锚点：**PointBridge / DeFM / RAFL / pi0.7 / Navigation Heads Path Deviation Detection / Master Key**。其中新入库的 **Master Key (2604.06377)** 进一步强化了“**共享低维能力子空间可先对齐、再迁移**”这个抽象判断，但它属于 **能力子空间/representation transfer** 证据，只能作为 D04 中 `shared latent sufficiency` 的弱旁证，**不能**越级改写成 embodiment-specific compensation 或 dynamics adaptation 的主证据。
- **QMD 本地检索**：按规则尝试 `qmd query "cross-embodiment transfer robot morphology generalization action representation" --no-rerank`，但本轮 cron 环境下进程被 **SIGKILL**，未得到稳定可用输出；结合近期多轮 D04 的 QMD 结果长期主要回流 **Unified Latent Space / LAD / 既有 D04 文档**，本轮仍判定本地方向增量主要集中在既有 `shared geometry → shared latent sufficiency → dynamics residual ordering` 主链。
- **arXiv 外查**：按规则补做 Export API 外查，但本轮请求遭遇 **HTTP 429** 限流，未拿到稳定结果；因此这轮不凭不完整外部返回强行更新论文图谱，保持“本地优先、外查失败不伪造结论”的策略。
- **本轮结论**：Phase 2 继续把 D04 从“shared latent 与 dynamics bottleneck 的分流门”推进到 **实验执行优先级冻结**：当 `IG0 + SC0` 已过后，首轮默认先跑 **最轻 shared-latent 路线**（`shared+adapter / latent retarget`），只有当 `DRB` 明显抬升时才升级 physics adapter；而 **Master Key** 这类能力子空间工作只用于解释“为什么 shared latent 可能已经足够”，不再给 morphology 或 dynamics 叙事添一条新平行主线。

## 最新扫描（R887）

- **本地回扫**：按轮换继续主推进 **D04**，先复核 `D04/README.md`、`REPORT.md` 与近 30 天本地锚点 **GaussFly / Unified Latent Space / LAD / AirVLA / R3D**。当前本地证据仍稳定落在同一条顺序链：**R3D / GaussFly** 负责证明 shared geometry / representation bridge 先立住，**Unified Latent Space / LAD** 只在 `IG0 + SC0` 已过后解释 `shared latent sufficiency`，而 **AirVLA** 继续作为 `dynamics gap / payload-aware guidance` 的主证据。
- **QMD 本地检索**：`cross embodiment shared geometry latent sufficiency morphology compensation dynamics gap aerial manipulation` 继续主要回流 **Unified Latent Space / LAD / D04 既有文档与 source 页面**，说明 D04 当前本地增量仍集中在既有 `shared geometry → shared latent sufficiency → dynamics residual ordering` 主链，没有冒出新的高价值分支。
- **arXiv 外查**：高位结果仍是 **OneVL (2604.18486)**、**XEmbodied (2604.18484)**、**DESPITE safety (2604.18463)**；分别偏 latent reasoning 自动驾驶、云侧 3D/physical cue foundation model 与 embodied planning safety benchmark，和 D04 当前“跨载体共享接口 + latent sufficiency + dynamics residual ordering”主叙事贴合度不足，因此本轮 **高价值论文新增 0 篇，入库 0 篇**。
- **本轮结论**：本轮没有继续扩论文图谱，而是把 D04 的默认解释门再压实一步：**只要 shared geometry 已稳、且 `MCG` 没有持续显著占优，默认收成 `shared geometry + latent sufficiency`；只有当 `DRB` 升高时，才允许把主解释切到 `dynamics adaptation bottleneck`**。

## 最新扫描（R886）

- **本地回扫**：已复核 `D04/README.md`、`REPORT.md`、研究状态追踪与近 30 天本地锚点 **GaussFly / Unified Latent Space / LAD / AirVLA / R3D**。其中 **GaussFly** 继续被确认只适合作为 `geometry/representation bridge` 证据：它说明 **real→3DGS sim→RL** 能先把视觉几何与表征质量立住，但并不直接证明共享 latent 已足够，也不直接支持 embodiment-specific compensation 主叙事。
- **QMD 本地检索**：`cross embodiment shared geometry latent sufficiency morphology compensation dynamics gap aerial manipulation` 继续主要回流 **Unified Latent Space / LAD / D04 既有文档与 source 页面**，说明当前本地增量仍集中在既有 `shared geometry → shared latent sufficiency → morphology/dynamics residual ordering` 主链，没有冒出新的高价值分支。
- **arXiv 外查**：高位结果仍是 **OneVL (2604.18486)**、**XEmbodied (2604.18484)**、**DESPITE safety (2604.18463)**；分别偏 latent reasoning 自动驾驶、云侧 3D/physical cue foundation model 与 embodied planning safety benchmark，和 D04 当前“跨载体共享接口 + latent sufficiency + residual ordering”主叙事贴合度不足，因此本轮 **高价值论文新增 0 篇，入库 0 篇**。
- **本轮结论**：外部结果仍未改写 D04 主线，研究重心继续留在 REPORT/实验协议收束，而非扩新论文。

## 最新扫描（R885）

- **本地回扫**：已复核近 30 天 D04 锚点笔记 **GaussFly / CAPO / RAFL / PointBridge / DeFM / Unified Latent Space / LAD / AirVLA / R3D**，确认当前本地证据仍稳定集中在 `shared geometry → shared latent sufficiency → morphology/dynamics residual ordering` 这条主链，没有冒出能改写主叙事的新分支。
- **QMD 本地检索**：`cross embodiment shared geometry latent sufficiency morphology compensation dynamics gap aerial manipulation` 继续主要回流 **Unified Latent Space / LAD / D04 既有文档与 source 页面**，说明 D04 当前“shared geometry 已成立后，剩余掉点究竟该解释为 latent 已足够、形态补偿有效，还是动力学残差主导”的本地增量基本已被吃干净。
- **arXiv 外查**：高位结果仍是 **OneVL (2604.18486)**、**XEmbodied (2604.18484)**、**DESPITE safety (2604.18463)**；分别偏 latent reasoning 自动驾驶、云侧 3D/physical cue foundation model 与 embodied planning safety benchmark，和 D04 当前“跨载体共享接口 + latent sufficiency + residual ordering”主叙事贴合度不足，因此本轮 **高价值论文新增 0 篇，入库 0 篇**。
- **本轮结论**：外部结果仍未改写 D04 主线，研究重心继续留在 REPORT/实验协议收束，而非扩新论文。

## 最新扫描（R884）

- **QMD 本地回扫**：`cross embodiment shared geometry latent sufficiency morphology compensation dynamics gap aerial manipulation` 继续主要回流 **Unified Latent Space / LAD / D04 既有文档与 source 页面**，说明 D04 当前本地增量仍集中在既有“shared geometry → latent sufficiency → residual ordering”链路，没有形成新的外部高价值增量。
- **arXiv 外查**：高位结果仍是 **OneVL (2604.18486)**、**XEmbodied (2604.18484)**、**DESPITE safety (2604.18463)**；分别偏 latent reasoning 自动驾驶、云侧 3D/physical cue foundation model 与 embodied planning safety benchmark，和 D04 当前“跨载体共享接口 + latent sufficiency + residual ordering”主叙事贴合度不足，因此本轮 **高价值论文新增 0 篇，入库 0 篇**。
- **本轮结论**：外部结果暂未改写 D04 主线，研究重心继续留在 REPORT/实验协议收束，而非扩新论文。

## 最新扫描（R777）

- **Scalable and General Whole-Body Control for Cross-Humanoid Locomotion** (arXiv:2602.05791) — XHugWBC 用 physics-consistent morphological randomization + 语义对齐的观测/动作空间，实现单策略跨多种 humanoid 设计零样本泛化，直接强化了「形态随机化 + 显式语义接口」这条路线。
- **CeRLP: A Cross-embodiment Robot Local Planning Framework** (arXiv:2603.19602) — 继续作为几何接口层代表，说明跨载体统一不只在动作层，也可以前移到感知-规划之间。
- **LAD: Latent Action Diffusion for Cross-Embodiment Manipulation** (arXiv:2506.14608, ICRA 2026) — 用扩散模型统一latent action space，验证了latent统一接口对跨载体操作的泛化增益，+latent diffusion路线获ICRA直接背书。
- **Unified Latent Space for Cross-Embodiment Humanoid Robot Control** (arXiv:2601.15419) — 人型机器人跨载体控制共享latent表示，验证了latent统一对多自由度复杂载体的可扩展性。

## 一、研究背景与动机

现有策略通常为特定机器人硬件训练,更换平台需重新采数据和训练。主人拥有无人机+机械臂双平台,需要策略能跨载体泛化。当前跨载体学习存在四大流派(动作空间统一/功能对齐/世界模型路线/数据策略),但尚无统一框架。

## 二、相关工作梳理

### 2.1 动作空间统一(CEI/FAAS/MOTIF/ROI-Driven)
用统一接口/表示对齐不同载体的动作空间。CEI 达 82.4% transfer ratio。

### 2.1+ 形态先验注入(Embedding Morphology into Transformers / UniMorphGrasp)
最新工作开始反过来质疑"完全 embodiment-agnostic 是否真的是最优解"。2603.00182 直接把运动学 token、拓扑注意力 bias、关节属性条件注入 transformer,说明**显式给模型喂形态结构**本身就可能提升跨载体鲁棒性。2602.00915 的 UniMorphGrasp 则进一步说明,morphology 不只该注入编码器,也可以作为扩散生成器的条件输入,直接约束跨手型抓取分布。

### 2.1++ 几何对齐 latent 动作空间(OPFA)
OPFA (2603.14522) 进一步提醒我们,跨载体统一策略不只存在"显式 morphology-aware backbone"这一路,也可以先学习 **geometry-aware latent action space**,再用 **unified latent retargeting decoder** 解出不同 embodiment 的动作。这条路线的好处是把对齐位置从输入侧推到 latent 动作层,更适合直接比较不同 embodiment 的技能共性和 retargeting 成本。

### 2.1+++ Latent Action Diffusion统一路线(LAD - ICRA 2026)
**LAD (arXiv:2506.14608, ICRA 2026)** 是 latent action 统一路线的重要进展:用扩散模型在统一 latent action space 中建模跨载体动作分布,无需显式对齐动作维度。与 LAC-WM 的世界模型路线相比,LAD 证明了纯扩散+latent 接口也能高效跨载体,并已在 ICRA 2026 获得同行验证。这条路线与轴C完全对齐,进一步确认 latent diffusion 是轴C的理想实现载体。

### 2.1++++ 共享Latent表示可扩展性(arXiv:2601.15419)
人型机器人跨载体共享 latent 表示工作验证了:latent space 随载体数量增加而持续 scaling,不因形态差异增大而崩溃。这直接支撑轴C的 scaling 假设,说明轴C在主人无人机+机械臂双平台同样具备扩展潜力。

### 2.1++ 几何接口层泛化(CeRLP)
CeRLP (2603.19602) 把跨载体泛化能力从 manipulation policy 延伸到了 **视觉导航 local planner**。它通过离线预标定修正单目深度尺度,再把异构视觉输入统一抽象成 **height-adaptive laser scan**,从而让不同机器人尺寸、相机参数与相机类型共享同一局部规划策略。这个结果很关键,因为它说明 D04 的"统一接口层"不必只定义在动作空间,也可以前移到几何感知与规划之间。

### 2.1+++++ 物理一致形态随机化路线(XHugWBC)
**XHugWBC (arXiv:2602.05791)** 进一步给了轴D一个很强的实证支撑: 不只是把 morphology 当静态条件喂给模型,而是把 **physics-consistent morphological randomization** 直接做成训练分布的一部分,再配合语义对齐的 observation/action space,让单策略对多种 humanoid 结构零样本泛化。它说明轴D最值得补的一环不是更复杂的 token 设计,而是把"形态变化"提前到训练分布层显式建模。

### 2.2 功能对齐(SoftAct)
不对齐关节轨迹,对齐功能受力模式。对接触任务更有效。

### 2.3 世界模型路线(DreamZero/WAM)
绕过动作空间对齐,直接建模未来物理演化。30分钟 play data 即可 few-shot 适配新载体。

### 2.3+ Morphology-conditioned WM 作为 physics adapter（R786新增）
**Toward Hardware-Agnostic Quadrupedal World Models via Morphology Conditioning** (2604.08780) 给了 D04 一个很关键的新接口位：冻结世界模型不只是做 rollout 预测器，还可以在部署时用 **explicit morphology parameters** 把未见载体的动力学先映射进统一 latent，再交给共享 policy。它最有价值的不是四足场景本身，而是明确展示了 **morphology-conditioned WM = real-time physics adapter** 这条中间路线，刚好补在轴C 的 latent 统一和轴D 的形态先验之间。

**对 D04 的意义**：
1. 统一接口层不必只定义在动作空间，也可以定义在 **dynamics-to-latent adapter**。
2. 新载体接入不再只有 `full retrain / adapter / latent retarget` 三种，还应补一类 `frozen WM physics adapter`。
3. 对主人双平台最现实的价值是：未来把地面机械臂或四足/空中平台的动力学差异外置到 adapter 层，尽量保住共享策略主干不动。

### 2.4 数据策略(Data Analogies/RoVi-Aug/Physics-Driven/Cross-Emb OffRL)
Paired 数据比海量未配对提升 22.5%;数据增强可 zero-shot 部署未见机器人。

### 2.4+ 低成本锚点数据策略（XRZero-G0 - 2026-04-17 R779 新增）
**XRZero-G0 (2604.13001)** 给轴B补了一条很实用的工程结论：跨载体泛化不一定非要大量目标机器人示教，而是可以用 **大规模 robot-free / human-kinematics 数据提供语义与空间多样性**，再用 **少量目标机器人真机数据作为 kinematic anchor** 补齐关节摩擦、控制延迟、奇异位姿等物理先验。论文给出的 10:1 混合比（大量 robot-free + 极少量 real-robot）已经能逼近纯真机基线，这对主人特别有价值，因为空中机械臂真机采集代价高、风险高，天然适合先走“廉价语义数据 + 少量目标载体锚点”的路线。

**对 D04 的意义**：
1. 轴B 不应只写成“paired data 越多越好”，而要细化成 **语义多样性来源** 与 **目标载体物理锚点** 两部分。
2. 这条路线和轴C/轴D不冲突，反而可作为 latent 统一或 morphology-aware backbone 的最低成本接入包。
3. 对空中平台最现实的实验形态，不是从零攒大量 UAV manipulation 真机数据，而是先混入人类/地面平台演示，再用少量空中平台数据补动力学缺口。

### 2.4++ Human geometry anchor 路线（Lidea - 2026-04-18 R789 新增）
**Lidea (2604.10677)** 把 human-to-robot transfer 拆成了两层很干净的桥接：先做 **implicit feature distillation** 保留人类演示里的任务语义，再做 **explicit geometry alignment** 把 human/robot 观测统一到共享的任务几何表述。它最值得 D04 吸收的点，不是“又来一条人类数据迁移路线”，而是提醒我们 **人类数据真正高杠杆的部分可能不是动作标签，而是任务几何与接触前布局**。

**对 D04 的意义**：
1. 轴B 可以再细分为 `robot paired demo` 与 `human geometry anchor` 两条低成本数据线。
2. 轴A 的功能接口层不只可写成末端位姿/接触语义，也应显式包含 **task geometry state**，方便 human/ground robot/aerial robot 三方共享。
3. 对主人最实际的价值是，可以先用人类或地面平台演示学“接近位姿/接触前几何”，再用少量空中载体锚点补动力学和执行壳，而不是要求所有数据都来自目标空中平台。

### 2.5 推理时动力学补偿(AirVLA - 2026-04-16 R743 新增)
**AirVLA (2603.25038)** 是跨载体泛化领域的里程碑工作:将固定基座 manipulation VLA (π0) 迁移到 aerial manipulation 平台。

**核心发现**:
1. **视觉表征可迁移** ✅ - VLA 的视觉 encoder 天然跨 embodiment
2. **动力学不可迁移** ❌ - 准静态假设 vs 欠驱动高动态飞行,称之为 "dynamics gap"
3. **推理时修正 > 重训练** - Payload-Aware Guidance 在 inference-time 向 flow-matching sampling 注入 payload 物理约束,无需 retrain foundation model

**方法亮点**:
- Payload-Aware Guidance(推理时注入载体约束,而非重训)
- Gaussian Splatting 合成 navigation 训练数据
- 落地效果:导航 81%→100%,pick-and-place 23%→50%

**对 D04 的意义**:
- 确立了「视觉先验迁移 + 推理时载体修正」的低成本路线
- 与 CeRLP (D04 2.1++) 共同指向:**统一接口层不必只定义在动作空间**,也可以是推理时的动态补偿模块
- **可落地方向**:在主人龙虾项目中引入 inference-time flight-stability constraint module,让地面先验(视觉/VLA)直接复用,动力学补偿外置到推理时

## 三、我们的创新方向

### 3.1 核心创新点收束（四大轴）

综合现有文献与主人双平台（无人机+机械臂）实际需求，创新点收敛为四条独立且互补的验收轴：

| 轴 | 编号 | 内容 | 代表工作/支撑证据 |
|---|------|------|----------------|
| **轴A：功能接口层** | C1 | 末端位姿+接触语义+任务阶段token作为跨载体中间表示 | CEI (82.4% transfer), LAP (零样本VLA) |
| **轴B：Paired数据飞轮** | C2 | 仿真中自动生成「同任务-不同载体」配对数据，解决跨载体数据稀缺 | Data Analogies (+22.5%), paired优于海量未配对 |
| **轴C：Latent Action统一** | C3+C5 | 先学共享 latent action space，再统一 retargeting decoder，比直接注入形态先验更利于多载体联合训练 | LAC-WM (ICLR 2026, +46.7%), LAD (ICRA 2026), OPFA |
| **轴D：形态感知结构注入** | C4 | 不完全追求统一动作空间，额外注入运动学拓扑与关节语义作为鲁棒性增强器；与轴C互补而非竞争 | Embedding Morphology into Transformers, DexFormer, Being-H0.5 |

> **注**：C6（形态条件生成）和 C7（新载体接入代价建模）是轴C和轴D的具体实验设计细节，不再作为独立创新点。

### 3.1+ 轴C深度论证（R763更新）
LAD (ICRA 2026) + LAC-WM (ICLR 2026) + arXiv:2601.15419 共同验证了轴C的核心假设：
- **扩散模型 > 自回归模型**：LAD 证明 latent diffusion 对跨载体动作生成的稳定性优于 latent autoregressive（对应轴C的技术选型依据）
- **Scaling 成立**：LAC-WM 的 +46.7% 增益 + 人型机器人 latent scaling 共同证明，pretraining 载体越多，latent 统一越强（轴C scaling 假设获双重验证）
- **与轴D互补**：轴C提供 latent 层面的统一，轴D提供 morphology 层面的结构偏置；LAD+UniMorph 的组合即轴C+轴D协同的最佳例证

### 3.2 拟定方法框架

```
输入:自然语言指令 + 源载体演示轨迹 + 目标载体运动学参数
         │
    ┌────┴────┐
    │ 任务语义  │  高层:解析末端位姿+接触语义+任务阶段token（轴A）
    │ 解析单元  │
    └────┬────┘
         │
    ┌────┴──────────┐
    │ Paired Demo    │  轴B: 仿真自动生成「同任务-不同载体」配对数据
    │ 生成引擎(D05)  │
    └────┬──────────┘
         │
    ┌────┴────────┐
    │ Latent Action │  轴C: 共享 latent action space + unified retargeting decoder
    │ 统一模块     │  → 兼容不同末端执行器、关节配置
    └────┬────────┘
         │
    ┌────┴────────────┐
    │ 形态感知结构注入  │  轴D: kinematic tokens + topology-aware attention
    │  (增强器)       │     轻量注入，不强制统一动作空间
    └────┬────────────┘
         │
    ┌────┴────┐
    │ 目标载体  │  输出:目标载体的功能等价动作
    │ 动作输出  │
    └─────────┘
```

### 3.3 与现有方法的关键差异

| 对比维度 | CEI/LAP | LAC-WM (World Model路线) | LAD (Diffusion路线) | Morphology注入路线 | 我们的方法 |
|---------|---------|----------------------|------------------|----------|
| 核心思路 | 功能空间接口 | 共享latent WM | 共享latent扩散 | 形态结构偏置 | 轴A+轴B+轴C+轴D四轴并行 |
| 动作空间 | 显式统一接口 | 隐式统一latent | 隐式统一latent | 不统一 | 按需选择最优路线 |
| 数据需求 | 需paired对应数据 | pretraining载体越多越好 | pretraining载体越多越好 | 单载体数据即可 | paired+仿真双保险 |
| 新载体接入 | adapter微调 | 轻量adapter | 轻量adapter | 零样本 | 低成本adapter+latent retarget双模式 |
| 空中机械臂适配 | 部分适配 | 需验证 | ICRA2026验证中 | 偏地面 | 空中优先，导航+操作统一 |
| 理论验证 | 82.4% transfer | +46.7% scaling增益 | ICRA 2026已接收 | 单载体零样本 | 目标:达Mode1的90%@Mode3代价 |

### 3.4 新载体接入代价建模（实验核心指标）

将接入代价显式建模为独立对照轴：
- **Mode 1**: Full retrain — 全量重训练目标载体
- **Mode 2**: Lightweight adapter — 冻结主模型，仅微调轻量adapter
- **Mode 3**: Unified latent retargeting — 零训练，仅通过latent space映射

目标：证明轴A+轴C组合在Mode 3下即可达到Mode 1的90%+性能，且接入代价（人工correction轮次/数据量）显著低于竞品。

### 3.5 面向龙虾项目的最小系统闭环（R789推进）

把四轴真正落到主人当前“地面机械臂 → 空中机械臂”链路，最小系统不该一上来就做 full-task end-to-end，而应拆成三层：

1. **共享任务几何层（A+B）**
   - 输入统一成 `目标物体局部几何 + 目标接触位姿 + 接触前约束区间`。
   - 数据优先级：`human/ground robot 演示 → paired robot demo → 少量空中锚点`。
   - 目标是先学会“该靠近哪里、以什么姿态靠近”。

2. **跨载体技能层（C+D）**
   - 用 unified latent action 复用接近/抓取技能主干。
   - 再用 morphology token / physics adapter 补不同载体的运动学与动力学差异。
   - 目标是把“技能共性”和“载体差异”分开建模，而不是全丢给一个策略硬背。

3. **部署修补层（D06/D07接口）**
   - 接近 D06 的 flight-stability / replanning 壳层。
   - 接近 D07 的 disturbance rejection / contact recovery 壳层。
   - 目标是让 D04 论文主体聚焦“跨载体共享”，把执行时修补明确外置，避免方法定义过宽。

### 3.6 PMI式可验证意图接口（R825新增）

基于本地 `PMI跨躯体意图接口` 框架笔记、`R3D` 与现有 `Unified Latent Space / AirVLA / Hardware-Agnostic QuadWM`，D04 现在可以把轴A从“功能接口层”进一步写实成 **PMI-style verified intent packet**。这一步很关键，因为 D04 后续若只写“共享 latent + morphology token + physics adapter”，仍然容易把高层任务几何、载体能力边界和执行壳层混在一起。

**统一接口包 `PMI Packet`**：
- `task_geometry_state`：目标物体局部几何、pre-contact 位姿、目标区域约束
- `contact_affordance`：允许接触面、力方向、禁止接触区域
- `phase_token`：`approach / align / grasp / lift / place`
- `capability_bound`：当前载体 reachability、payload、末端开合范围、允许姿态带
- `execution_budget`：最大校准步数、允许恢复次数、时延/能耗预算
- `verification_tag`：`geometry-valid / morphology-valid / dynamics-risk / shell-required`

**为什么它值得写进主线**：
1. **把 D04 的共享能力和 D06/D07 壳层彻底拆开**。共享主干只负责生成 `PMI Packet`，controller shell 只负责把它安全执行。
2. **让 human geometry anchor 真正可复用**。人类或地面平台提供的，不必是目标载体动作标签，而可以先落成 `task_geometry_state + contact_affordance`。
3. **让 physics adapter 有明确插入位**。若 `geometry-valid` 但 `dynamics-risk`，优先调用 physics adapter，而不是误判成共享主干失败。
4. **让 R3D 这类 3D backbone 的价值有归属**。R3D 主要改善 `task_geometry_state` 的稳定性，而不是直接宣称提升跨载体控制本体。

**当前主判断**：D04 后续主文不该写成“统一 latent 表示直接输出动作”，而应写成“共享表示先输出可验证 PMI Packet，再由 embodiment-specific adapter / controller 执行”。这样更容易证明跨载体共享到底发生在几何-意图层，还是只是发生在末端控制补偿层。

### 3.7 轴A进一步收束：3D几何先验先于补偿层（R830新增）

结合本地新增的 **R3D: Revisiting 3D Policy Learning (2604.15281)** 与现有 `HEX / Unified Latent Space / AirVLA`，D04 当前最需要的不是再争论“specialist head、latent retarget、physics adapter 谁更强”，而是先回答一个更前置的问题：**共享几何接口本身有没有站稳**。

**新收束判断**：
1. `R3D 3D encoder + PMI Packet` 应作为 D04 首轮默认入口，而不是可有可无的感知备选；如果 `task_geometry_state` 在视角变化、轻微遮挡、相机扰动下都不稳定，后续任何跨载体增益都不应被解释成共享主干能力。
2. `HEX` 更适合解释 **高 DoF 协同与形态补偿层** 的收益，而不是拿来替代几何接口层；它主要回答的是 `MCG`，不是 `GTG`。
3. `AirVLA / Hardware-Agnostic QuadWM` 更适合解释 **dynamics gap** 与 `DRB`，也不该提前抢走轴A的问题定义。
4. 因此，D04 的首轮实验叙事应该固定为：**先证实 `2D encoder → R3D 3D encoder` 是否显著提升 `PMI Packet` 稳定性，再进入 specialist / latent / physics adapter 的收益归因**。

**研究意义**：
- 这一步把 D04 从“很多补偿层并行竞争”继续压成了“先几何、后形态、再动力学”的可证伪顺序。
- 也让 D04 与 D06/D07 的边界更清晰：D04 主体先负责把 `共享任务几何` 立住，后续载体补偿和控制恢复再分别记到 D04 后半段与 D06/D07 壳层。

**默认结论**：在首轮主任务 `T1 静态单物体接近→抓取→抬升10cm` 上，只要 `R3D` 不能稳定提升 `PGS / PMI Packet 完整率 / 接近位姿误差`，就不允许把后续性能差距解读为跨载体补偿层设计优劣。

## 3.9 接口通过后的主叙事冻结规则（R846新增）

结合本轮继续回扫的 **R3D / PointBridge / DeFM / CAPO / PMI跨躯体意图接口 / Unified Latent Space / AirVLA / Hardware-Agnostic QuadWM**，D04 现在已经不只需要“接口优先验证”，还需要在接口通过后立刻**冻结论文主叙事**，避免再次回到 `specialist / latent retarget / physics adapter / shell` 同时抢标题的散乱状态。

## 3.9.4 shared geometry 过线后的解释顺序冻结（R864新增）

结合本轮继续回扫的 **R3D / AirVLA / Unified Latent Space**，D04 现在已经不只需要“接口通过后只保留一个主叙事”，还要进一步冻结 **主叙事选择前的解释顺序**。否则很容易在首轮结果出来后，又回到 `specialist / latent retarget / physics adapter` 同时都想保留一点的老问题。

**新的默认解释顺序**：
1. **先看 shared geometry 是否真的已经过线**：若 `PGS / IFR / ICS` 仍不稳，后续所有补偿层讨论一律无效，先回修 `R3D / PMI Packet / human geometry anchor`。
2. **再看 shared latent 是否已经足够承载跨载体共性**：若 `GTG` 已明显下降，且 `MCG < 3pp`，默认解释为 **Unified Latent Space / latent retarget 已足够**，不再主动放大 specialist 路线。
3. **只有在 shared geometry 与 shared latent 都不足以解释剩余掉点时，才继续区分 morphology compensation 和 dynamics compensation**。
4. **若 geometry 已稳、GTG 已低，但 `DRB` 高**，默认优先判成 `dynamics gap` 主导，主线切向 `AirVLA / physics adapter / payload-aware guidance`，而不是继续细拆 morphology compensation。

**为什么这样冻结**：
- **R3D** 的价值主要在前置几何稳定性，而不是补偿层；
- **Unified Latent Space** 的价值主要在证明共享 latent 本身可能已经足够省掉大量 embodiment-specific 头；
- **AirVLA** 则明确提醒我们：当地面/固定基座视觉与任务几何已可迁移时，真正拖垮空中平台的常常不是“形态差一点”，而是 **动力学不兼容**。

**因此 D04 的当前默认顺序** 不再是“接口过了以后 morphology 与 dynamics 谁更强”，而是：
- 先看 shared geometry；
- 再看 shared latent；
- 只有 shared 层不够时，才允许 morphology compensation 和 dynamics compensation 抢主叙事。

这让 D04 从“接口优先验证”继续推进到“接口通过后也不会重新发散”，更适合主人的地面机械臂 → 空中机械臂双平台链路。

### 3.9.1 三档主叙事，只能三选一

当 `IG0 + SC0` 已过、说明 `PMI Packet` 与共享几何接口基本可信后，D04 主体只允许在下面三档里选一条：

1. **Narrative-G：几何主导**
   - 条件：`GTG` 仍是首要瓶颈，且 `PGS / IFR / ICS` 的改善与成功率改善直接同向。
   - 主标题写法：`Verified Geometry Intent Interface` / `Shared Task Geometry First`
   - 允许保留：R3D / PointBridge / DeFM / PMI Packet
   - 降级项：specialist、physics adapter 都只能做次级补件。

2. **Narrative-M：形态补偿主导**
   - 条件：`IG0 + SC0` 已稳、`GTG` 已低，且 `MCG` 连续稳定高于阈值，同时 `DRB` 不主导。
   - 主标题写法：`Shared Geometry, Embodiment-Aware Compensation`
   - 允许保留：HEX / morphology token / specialist head
   - 降级项：physics adapter 只能做补充实验，不得抢主标题。

3. **Narrative-D：动力学补偿主导**
   - 条件：`IG0 + SC0` 已稳、`GTG` 已低，但 `MCG < 3pp` 或不稳定，同时 `DRB` 持续偏高。
   - 主标题写法：`Shared Geometry with Inference-Time Physics Adaptation`
   - 允许保留：AirVLA / Hardware-Agnostic QuadWM / payload-aware guidance / physics adapter
   - 降级项：specialist / morphology token 只能作为 supporting evidence。

### 3.9.2 新默认判断：specialist 不是默认主角

本轮把一个此前容易反复摇摆的点正式写死：
- **只要 `IG0 + SC0` 已过、`GTG` 已低，但 `MCG < 3pp`，specialist / morphology-aware head 一律不得继续占主叙事。**
- 换句话说，形态补偿层默认只是待证伪候选，不再是默认主角；只有它在首轮结果里给出持续、稳定、可复现的增益，才配从 supporting evidence 升格。

### 3.9.3 对主人当前双平台问题的实际含义

对“地面机械臂 → 空中机械臂”这条链路，D04 当前更现实的论文路线不再是“什么都统一”，而是：
1. 先证明 **共享任务几何 + PMI Packet** 立得住；
2. 再判断差距主要来自 **形态补偿** 还是 **空中动力学补偿**；
3. 最后只保留一条主补偿叙事，不让 morphology 与 dynamics 同时抢主标题。

这让 D04 后续更像一篇**先证明共享层，再证明哪种补偿层最必要**的论文，而不是杂糅多条补偿路线的工程报告。

### 3.9.4 与 D06 / D07 的边界再次钉死

- 若 `Narrative-D` 成立，D04 仍只主讲 **共享几何 + physics adapter**，不去抢 D06/D07 的 controller shell 与 recovery 叙事。
- 若后续 `SDR` 偏高，则必须继续降级 D04 的部署表述，承认最终收益已部分转移到 D06/D07 壳层。

### 3.9.5 接口通过后的首轮主叙事冻结补充（R851新增）

在本轮继续回扫本地锚点 **PMI 接口 / R3D / PointBridge / DeFM / HEX / AirVLA / Hardware-Agnostic QuadWM** 后，D04 可以把 `IG0 + SC0` 通过后的首轮冻结规则再压实一层：

1. **若 `GTG` 仍高**，则论文主句继续写成 `Verified Geometry Intent Interface / Shared Task Geometry First`，禁止 specialist、latent retarget 或 physics adapter 抢主标题。
2. **若 `GTG` 已低、`MCG < 3pp` 且 `DRB` 高**，则默认主句切到 `Shared Geometry with Inference-Time Physics Adaptation`，明确把剩余困难解释为动力学残差，而不是形态补偿不足。
3. **若 `GTG` 已低、`MCG ≥ 3pp` 且 `DRB` 不主导**，才允许把 morphology-aware compensation 升格为主叙事；否则它只能停留在 supporting evidence。
4. **若 `SDR` 偏高**，则 D04 主文必须主动降级为“共享主干 + D06/D07 壳层协同”，不能把部署壳层收益继续写成 D04 独立贡献。

这一步的意义，不是再加新路线，而是让 D04 首轮结果一出来，就能立刻决定论文到底讲 **geometry-first / dynamics-first / morphology-compensation-first** 哪一句，而不是继续并列讲三句。

**本轮最小结论**：D04 现在最值钱的，不只是拿到 `IFR / ICS / DMS / PGS`，而是拿到这些数之后，能立刻把主文冻结到 `几何主导 / 形态补偿主导 / 动力学补偿主导` 三档之一。这样下一轮起，D04 才不会再次被 specialist、physics adapter 和 shell 三线同时拉扯。

### 3.9.6 首轮结果出来后的摘要/标题默认收束口径（R875新增）

结合本轮继续回扫的 **R3D / AirVLA / Unified Latent Space / CeRLP / Being-H0.5**，以及在 QMD 回流后补做 arXiv Export API 外查但未发现更贴合 D04 主线的新高价值论文，D04 现在已经不只需要冻结 **解释顺序**，还要继续把 **首轮结果出来后摘要和标题默认该怎么写** 也一并写死。否则很容易在首轮读数出来后，又重新回到 `specialist / latent / physics adapter` 三条线都想占一点主贡献的位置。

**默认收束顺序固定为三段**：
1. **若 `PGS / IFR / ICS` 仍不过线**，摘要只能写成 **shared geometry interface not yet established**，不得提前宣称跨载体补偿有效；此时所有 `specialist / latent / physics adapter` 结果都只能当诊断证据，不能升格为主贡献。
2. **若 `IG0 + SC0` 已稳、`GTG` 已低且 `MCG < 3pp`**，则默认把摘要与标题收成 **shared geometry + latent sufficiency**；这意味着 shared geometry 与 shared latent 已足以解释大部分跨载体收益，`specialist / morphology-aware compensation` 自动降级为 supporting evidence。
3. **只有当 shared 层已稳、`MCG` 持续占优且 `DRB` 不主导时**，才允许升格为 **embodiment-aware compensation**；反之若 `DRB` 高，则默认把论文主叙事收成 **shared geometry + physics adaptation bottleneck**，明确把问题归到 `AirVLA / physics adapter / payload-aware guidance` 这条线。

**为什么要把口径写死**：
- `R3D / PMI Packet` 的职责是证明共享任务几何先站稳；
- `Unified Latent Space / latent retarget` 的职责是证明 shared 层是否已经足够；
- `AirVLA / Hardware-Agnostic QuadWM` 才是 dynamics gap 的主解释层；
- 若不提前冻结摘要口径，D04 很容易在首轮结果后重新退回 `specialist / latent / physics adapter` 三线并挂的老问题。

**当前 D04 默认 go/no-go 映射**：
- `PGS / IFR / ICS` 不过线 → 只允许写 **shared geometry interface not yet established**
- `GTG` 已低、`MCG < 3pp` → 默认写 **shared geometry + latent sufficiency**
- `MCG` 持续占优、`DRB` 不主导 → 允许写 **embodiment-aware compensation**
- `DRB` 高 → 默认写 **shared geometry + physics adaptation bottleneck**

### 3.9.8 首轮结果解释的唯一决策树（R884新增）

在 `IG0 (Interface Gate)`、`SC0`、`GTG / MCG / DRB / SDR` 已逐步写进协议后，D04 现在需要的已经不是再加一层“默认解释门”，而是把**首轮结果的唯一解释路径**彻底写死，避免同一批结果在汇报、正文、摘要里被反复改写成 geometry gain、latent gain、morphology gain、dynamics gain 四套说法。

**唯一决策顺序**：
1. **先判 IG0**：若 `IFR / ICS / DMS` 任一不稳，则所有结果统一收成 **shared geometry interface not yet established**，禁止讨论 latent sufficiency、specialist 或 physics adapter。
2. **再判 SC0**：只有 `IG0` 通过后，才看 `PGS / PMI Packet 完整率 / 几何状态方差`；若 `SC0` 不过，统一收成 **geometry bottleneck**，继续只修 `R3D / PMI Packet / geometry field definition`。
3. **再判 GTG**：若 `IG0 + SC0` 通过，但 `GTG` 仍高，则 shared geometry 虽已成形但接近阶段仍未稳，当前主结论仍是 **geometry bottleneck**，不允许提前把收益写给 specialist 或 dynamics adapter。
4. **再判 MCG**：若 shared geometry 已稳且 `GTG` 明显下降，同时 `MCG < 3pp`，默认解释为 **shared geometry + latent sufficiency**；只有 `MCG` 连续占优并超过阈值，才允许进入 **embodiment-aware compensation** 解释。
5. **最后判 DRB / SDR**：若 `DRB` 高，则自动改写为 **shared geometry + dynamics adaptation bottleneck**，优先保留 physics adapter / payload-aware guidance；若 `DRB` 不高但 `SDR` 高，则主文必须改写为 **shared backbone + deployment shell collaboration**，禁止把壳层收益记到账到 D04 主干。

**证据归位最终冻结**：
- **R3D / PointBridge / DeFM / GaussFly**：只负责 geometry / representation 过线证据
- **Unified Latent Space / LAD**：只在 shared geometry 已过线后解释 latent sufficiency
- **HEX / morphology-aware specialist**：只在 `MCG` 连续占优时进入主文核心段
- **RAFL / AirVLA / Hardware-Agnostic QuadWM**：只负责 dynamics residual / physics adapter 解释
- **CAPO**：只作为 domain-factor suppression 支线，不再跨段抢主叙事
- **D06/D07 shell**：只负责 `SDR` 与部署协同解释，不参与 D04 主干创新记账

**核心价值**：D04 现在不只冻结了正文顺序、证据归位和接口门，还把首轮结果一出来后的唯一解释路径写死；后续实验不再会把 geometry gain、latent gain、morphology gain、dynamics gain 混写在同一层。

### 3.9.7 正文固定四段排序规则（R879新增）

结合本轮继续回扫的 **GaussFly / CAPO / X-Nav / Unified Latent Space / LAD**，以及在 QMD 回流后补做 arXiv Export API 外查但未发现更贴合 D04 主线的新高价值论文，D04 现在可以把“标题/摘要默认收束口径”继续压成 **正文固定四段排序规则**。也就是说，后续第一版结果出来后，正文不再允许按作者主观偏好自由排段，而必须遵守一套先 shared、后 compensation 的固定论证顺序。

**正文默认顺序固定为四段**：
1. **shared geometry 是否成立**
   - 只看 `PGS / IFR / ICS / PMI Packet 完整率`。
   - 只要这些指标还没过线，正文第一段就只能写 **shared geometry interface not yet established**。
   - 此时 CAPO 式 prompt orchestration、GaussFly 式表征增强、specialist head、physics adapter 全都只能作为诊断证据，不得冒充主贡献。

2. **shared latent 是否已足够**
   - 当前段只在 shared geometry 已稳后才允许展开。
   - 若 `GTG` 已低且 `MCG < 3pp`，正文第二段默认收成 **shared geometry + latent sufficiency**。
   - 这时 `Unified Latent Space / LAD / latent retarget` 自动升为主解释，specialist 路线必须主动降级。

3. **morphology compensation 是否真有持续收益**
   - 只有 shared geometry 已稳、shared latent 也不足以解释剩余掉点时，才允许写这一段为核心段落。
   - 触发条件是 `MCG` 持续占优，且这种优势在不同载体/任务子集上都稳定可复现。
   - 若不满足，就不能把 morphology-aware head、prompt orchestration、embodiment token 写成论文主位。

4. **dynamics gap 是否才是主残差**
   - 若 `DRB` 持续偏高，则正文后半默认自动改写为 **shared geometry + physics adaptation bottleneck**。
   - 此时 `AirVLA / physics adapter / payload-aware guidance / Hardware-Agnostic QuadWM` 才是主解释层。
   - 也就是说，只要动力学残差主导，就不能继续把问题伪装成 morphology compensation 不足。

**为什么这一步重要**：
- `GaussFly` 提醒我们高保真表征收益并不等于跨载体共享已成立；
- `CAPO` 提醒我们 prompt/representation 收益不能跳过 shared geometry 验证直接上升为跨载体主贡献；
- `Unified Latent Space / LAD` 说明 shared latent 可能已经足够解释大部分收益；
- `AirVLA` 系结果则持续提醒，空中平台很多剩余误差最终是 dynamics gap，而不是“再加一点 embodiment token”就能解决。

**当前默认结论**：D04 现在不只冻结标题和摘要，也把正文论证顺序一并写死。后续第一版结果一出来，就能立刻判断该先证明共享几何、shared latent 已够，还是动力学残差才配占正文主位，不再让 `specialist / latent / physics adapter` 三线同时挂在论文核心段落上。

### 3.8 首轮结果后的论文主叙事切换条件（R832新增）

结合本地近 30 天内已经稳定沉淀的 **R3D / Unified Latent Space / AirVLA / HEX / PointBridge / DeFM / Hardware-Agnostic QuadWM**，D04 现在已经不缺“还能引用哪些路线”，真正缺的是：**首轮结果一出来，论文主叙事到底切到哪条主线**。否则很容易继续把 `shared geometry / latent retarget / specialist head / physics adapter / shell` 五条线都留着，最后写成没有主贡献的拼盘。

因此，本轮把 D04 的主叙事切换条件正式钉死：

#### Narrative-A：共享几何主导
**触发条件**：`PGS` 显著提升，且 `GTG` 明显下降；而 `MCG / DRB / SDR` 都未显著主导。

**对应叙事**：
- 主贡献写成 **3D geometry-grounded PMI Packet** 是跨载体共享的真正核心。
- `R3D / PointBridge / DeFM` 主要作为“共享任务几何先站稳”的支撑位。
- `specialist / physics adapter / shell` 仅保留为次级补件，不占主标题。

**适合的论文表述**：
- “Cross-Embodiment Transfer via Verified Geometry Intent Interface”
- “Shared Task Geometry Before Morphology Compensation”

#### Narrative-B：形态补偿主导
**触发条件**：`GTG` 已低，但 `MCG` 持续高于阈值，且 `DRB / SDR` 不主导。

**对应叙事**：
- 主贡献写成 **共享几何/latent 主干 + 轻量形态补偿层**。
- `HEX / morphology-aware token / specialist head` 成为主方法位。
- 几何接口保留为前提，不再作为全文核心 novelty。

**适合的论文表述**：
- “Shared Geometry, Embodiment-Aware Compensation”
- “Lightweight Morphology Compensation for Cross-Embodiment Transfer”

#### Narrative-C：动力学补偿主导
**触发条件**：`GTG` 与 `MCG` 都不算主瓶颈，但 `DRB` 持续偏高。

**对应叙事**：
- 主贡献写成 **共享视觉/几何先验可迁移，但 aerial dynamics gap 必须由 inference-time physics adapter 显式修补**。
- `AirVLA / Hardware-Agnostic QuadWM` 进入主方法位。
- `specialist head` 退为次级对照，不再消耗主要篇幅。

**适合的论文表述**：
- “Cross-Embodiment Transfer with Inference-Time Physics Adaptation”

### 3.9 首轮接口优先级进一步收束：先锁 PMI Packet，再谈补偿层（R845新增）

结合本轮回扫的本地锚点 **CAPO / PointBridge / DeFM / PMI跨躯体意图接口**，D04 现在可以把“几何先于补偿”再压实一步：**首轮真正该优先锁定的，不只是 3D backbone，而是 `PMI Packet` 这套共享意图接口本身是否足够稳定、可验证、可跨载体复用。**

这几篇本地材料给出的共同信号很一致：
1. **PointBridge** 强调跨域/跨机器人迁移真正稳定的前提，是先把外观变化和任务几何解耦；这说明 D04 的共享主干首先应服务 `task_geometry_state` 稳定，而不是急着输出动作。
2. **DeFM** 证明深度/几何先验更适合做 sim-to-real 与跨平台不变表征；这进一步支撑 `PMI Packet` 里的几何字段应优先绑定 3D/depth-grounded 表征，而不是只靠 RGB 语义特征。
3. **CAPO** 虽然更偏 D03/D04 交界，但它提醒一个关键事实：跨载体掉点里有相当一部分来自 domain factor 混叠（视角/FOV/光照/旋转），如果这些因素没被前置解耦，后续 specialist 或 physics adapter 很容易在补错层。
4. **PMI 框架** 则给了 D04 一个最清晰的接口边界：共享主干先输出 `task_geometry_state / contact_affordance / phase_token / capability_bound / verification_tag`，再由 embodiment-specific adapter 与 D06/D07 壳层去执行。

**因此本轮的新判断不是“再补一层新方法”**，而是正式把 D04 的首轮主线写死成三步：
- **Step-1：接口稳定性** —— 先验证 `PMI Packet` 完整率、字段一致性与视角/观测扰动下的稳定性；
- **Step-2：共享几何收益** —— 只有当 `PGS` 与 `GTG` 站稳后，才允许比较 `specialist / latent retarget / morphology token`；
- **Step-3：动力学与壳层拆账** —— 只有在前两步已基本过线时，才把 `DRB / SDR` 写进主叙事，判断 physics adapter 或 D06/D07 shell 是否主导。

**最关键的收束点**：
- 若 `PMI Packet` 不稳，D04 主文应老老实实讲 **shared geometry interface problem**，而不是抢写 morphology/generalization；
- 若 `PMI Packet` 稳、但 `MCG` 高，才轮到 specialist / morphology-aware 路线拿主位；
- 若 `PMI Packet` 稳、`MCG` 不高、但 `DRB` 高，主文应切到 inference-time dynamics adaptation；
- 若前三者都不算主瓶颈而 `SDR` 偏高，必须承认主要收益落在 D06/D07 壳层协同。

**一句话压缩**：D04 当前最该证明的不是“哪种补偿最强”，而是 **共享意图接口到底有没有先站稳**；只有这一步成立，后面的 specialist、latent、physics adapter 才配谈谁是主贡献。


#### Narrative-D：壳层主导，D04 降级为前置支撑
**触发条件**：`SDR` 显著高于其它三项，说明最终收益主要来自 D06/D07 的部署壳层或恢复控制。

**对应叙事**：
- 不把本轮结果硬写成 D04 主论文成功。
- D04 退回到“共享几何/latent 预训练与先验层”的 supporting paper 或前置章节。
- 主论文应改投 D06/D07 链路，D04 只保留为 ablation/supporting evidence。

**适合的论文表述**：
- 不建议单独立 D04 主稿；改为“shared prior for aerial embodied control”支撑章节。

#### Narrative-E：几何未站稳，暂停扩补偿层
**触发条件**：`PGS` 没提升或 `GTG` 仍高，说明共享任务几何接口本身不稳定。

**对应叙事**：
- 暂停讨论 `specialist / latent / physics adapter` 谁更优。
- 下一轮只允许继续压 `R3D / PointBridge / DeFM / PMI Packet`，先把几何层打稳。
- 这类结果不能被解释成“跨载体补偿方案失败”，因为问题还停在更前置的表征层。

**一句话规则**：
> **先看 `PGS/GTG`，再决定 D04 值不值得讨论补偿层；补偿层结果只有在共享几何先站稳后才有解释权。**

### 3.9 地面臂→空中臂主叙事选择表（R831新增）

> 这张表专门服务主人当前最现实的主场景：**地面机械臂技能迁到空中机械臂**。目的不是再列方法，而是让首轮结果一出来，就能直接决定 D04 的论文标题该押哪条主线。

| 首轮主要信号 | 主叙事归属 | D04中的方法定位 | 立即动作 |
|---|---|---|---|
| `PGS↑` 且 `GTG↓` 最明显 | **共享几何主线** | `R3D / PointBridge / DeFM / PMI Packet` 升为主方法 | 下一轮继续加大 3D 几何接口与 packet 校验 |
| `PGS` 稳了，但 `MCG` 最高 | **形态补偿主线** | `HEX / morphology token / specialist head` 升为主方法 | 减少几何争论，主攻 embodiment-aware compensation |
| `GTG/MCG` 都还行，但 `DRB` 最高 | **动力学补偿主线** | `AirVLA / QuadWM physics adapter` 升为主方法 | 明确写 aerial dynamics gap，不再混成通用跨载体问题 |
| `SDR` 最高 | **壳层主线（转 D06/D07）** | D04 退为 shared prior/background | 不强行立 D04 主稿，转支撑 D06/D07 论文 |
| `PGS` 不升反降 | **暂停写主叙事** | 所有补偿层都降为候选 | 只修几何表征与 PMI 完整率 |

**当前结论**：
- `PointBridge` 与 `DeFM` 的价值，应该统一归到 **Narrative-A 共享几何主线**，而不是散落在“sim2real表征增强”角落里。
- `HEX` 的价值，应该归到 **Narrative-B 形态补偿主线**。
- `AirVLA / Hardware-Agnostic QuadWM` 的价值，应该归到 **Narrative-C 动力学补偿主线**。
- 只要 `SDR` 主导，就说明真正的收益被 D06/D07 壳层吃走，D04 不该冒领主贡献。

### 3.10 首轮主叙事选择器：先几何、再补偿、最后壳层（R834 新增）

> R830-R832 已把 D04 收到“共享几何 / 形态补偿 / 动力学补偿 / 壳层”四段判线，但还缺最后一步：**首轮结果出来后，论文标题级主贡献到底押哪条线**。这一轮把它正式压成选择器，避免 D04 最后把 `R3D / PMI Packet / morphology token / AirVLA adapter / D06-D07 shell` 全写成并列创新。

| 首轮结果模式 | 优先判断 | 论文主叙事 | 其他模块在文中的位置 |
|---|---|---|---|
| `PGS` 与 `PMI Packet` 完整率显著改善，`GTG` 下降最明显 | 共享几何先验才是核心瓶颈 | **Verified Geometry Intent Interface** | morphology / dynamics / shell 退为次级补偿 |
| `GTG` 已低，但 `MCG` 长期居高，且 `HEX`/specialist 明显改善 | 共享几何够了，真正缺的是载体形态补偿 | **Shared Geometry + Lightweight Morphology Compensation** | R3D 成为前提模块，physics adapter 为对照 |
| `GTG/MCG` 都不算主瓶颈，但 `DRB` 高且 `AirVLA` 型 adapter 明显收益 | 视觉/几何已可迁移，瓶颈在 aerial dynamics gap | **Inference-Time Physics Adaptation for Cross-Embodiment Transfer** | geometry 接口作为共享前提，specialist 降级 |
| `SDR` 明显高于前三者，D06/D07 壳层拿走主要收益 | 当前收益主要来自执行壳，而非 D04 主干 | **不宜直接写成 D04 主论文**；改写成系统 paper 或将 D04 缩成子模块 | D04 主体收缩，壳层转交 D06/D07 叙事 |
| 多条线都略有提升，但没有单线主导 | 结果仍发散，主贡献未收敛 | **继续保持“共享几何优先”的默认叙事**，不提前扩张贡献 | 先补更强判别实验，不急着立标题 |

**默认规则**：
1. D04 的标题级贡献默认优先顺序：`共享几何接口` > `形态补偿层` > `动力学 adapter` > `执行壳层`。
2. 只有当 `GTG` 已明显压低，才允许把 morphology compensation 升为主标题。
3. 只有当 `GTG + MCG` 都不主导，才允许 `AirVLA / QuadWM` 进入主贡献位。
4. 若 `SDR` 主导，就说明当前结果更像系统工程收益，不该硬写成 D04 跨载体主干创新。

### 3.11 首轮主叙事→论文标题映射表（R836新增）

> 上面已经有判线和选择器，但还差最后一个给主人真正省时间的东西：**首轮结果出来后，标题、摘要第一句、主方法图到底怎么写**。这一节把 D04 的主叙事直接映射成可落笔的论文外壳，避免后面继续在 `共享几何 / morphology compensation / physics adapter / shell` 之间来回摇摆。

| 首轮主导信号 | 推荐标题方向 | 摘要第一句应强调什么 | 主方法图中心模块 | 必须降级到 supporting 的部分 |
|---|---|---|---|---|
| `PGS↑ + PMI Packet 完整率↑ + GTG↓` | **Verified Geometry Intent Interface for Cross-Embodiment Transfer** | 共享任务几何与可验证意图包是跨载体迁移的真正瓶颈 | `R3D / PointBridge / DeFM / PMI Packet` | specialist / physics adapter / shell |
| `GTG低，但 MCG主导` | **Shared Geometry with Lightweight Morphology Compensation** | 共享几何已经足够，剩余误差主要来自 embodiment-specific morphology gap | `shared geometry + morphology token / specialist head` | 纯 geometry novelty、physics adapter |
| `GTG低 + MCG低，但 DRB主导` | **Inference-Time Physics Adaptation for Cross-Embodiment Aerial Transfer** | 视觉与几何先验可迁移，但 aerial dynamics gap 决定最终可执行性 | `shared geometry + physics adapter / payload-aware guidance` | specialist head、shell 扩展 |
| `SDR主导` | **Shared Prior for Embodied Aerial Execution**（不建议单立 D04） | 当前收益主要来自 deployment shell 与恢复控制协同 | `shared prior + D06/D07 shell interface` | 把 D04 写成独立主贡献 |
| `PGS/GTG未改善` | **不立标题，继续修共享几何层** | 当前问题仍停留在前置表征层，尚不能讨论跨载体补偿主线 | `R3D / PMI Packet` 调试图 | morphology / dynamics / shell 的正面 claim |

**硬规则**：
1. 只有 `PGS / PMI Packet` 先站稳，D04 才允许从“共享几何”切到“形态补偿”或“动力学补偿”标题。
2. 只要 `SDR` 主导，就不把 D04 硬写成独立论文成功，而是老老实实转成 D06/D07 系统叙事的 shared prior 章节。
3. D04 的默认标题优先级固定为：**共享几何接口 > 轻量形态补偿 > 推理时动力学修补 > 共享先验支撑章节**。

### 3.12 首轮结果后的摘要骨架（R836新增）

为了让后续不再重新组织话术，这里直接把 4 种主叙事的摘要骨架写死：

- **共享几何主线**：
  - 句1：现有跨载体方法把失败混在形态差异与控制补偿里，但真正前置瓶颈是共享任务几何不稳定。
  - 句2：我们提出 `verified PMI Packet`，结合 3D geometry encoder，把任务几何、接触约束和阶段信息统一到可验证意图接口。
  - 句3：在地面臂→空中臂迁移中，该接口显著降低 `GTG`，并减少后续 morphology / dynamics 补偿需求。

- **形态补偿主线**：
  - 句1：共享几何可迁移后，跨载体剩余误差主要来自 morphology-specific execution gap。
  - 句2：我们在共享几何主干上引入轻量 morphology compensation（token / specialist head），只在载体相关层补偿结构差异。
  - 句3：该设计在保持共享主干不变的前提下，显著降低 `MCG` 并减少新载体接入代价。

- **动力学补偿主线**：
  - 句1：共享视觉与任务几何先验可以迁移，但 aerial embodiment 的核心难点是 inference-time dynamics gap。
  - 句2：我们将 payload-aware / physics adapter 外置到执行时，保持共享主干不重训。
  - 句3：该设计在地面臂→空中臂迁移中显著压低 `DRB`，证明跨载体收益主要来自动力学修补而非重新学习任务语义。

- **壳层协同主线**：
  - 句1：共享先验本身不足以解释最终系统收益，真正决定成败的是 deployment shell 与恢复控制。
  - 句2：我们将 D04 共享主干收缩为 shared prior，再与 D06/D07 壳层协同执行。
  - 句3：系统结果表明，shared prior 的价值在于减少壳层搜索与恢复负担，而非单独解决跨载体执行问题。

### 3.13 下轮默认建议（R836新增）

基于当前本地材料密度与既有收束，**下轮默认不再扩 D04 论文地图**，而是直接做这三件事：
1. 先拿 `R3D encoder vs 2D encoder` 的 `PGS / PMI Packet 完整率 / GTG` 首轮读数；
2. 若几何已站稳，再做 `shared latent only vs + morphology compensation` 的 `MCG` 对照；
3. 只有在 `GTG + MCG` 都不主导时，才允许把 `AirVLA / QuadWM physics adapter` 升成下一轮主推进。

这三步能直接把 D04 从“路线很多”砍成“只剩一条标题主线”。

### 3.9 地面臂→空中臂首轮判线协议（R834新增）

结合本轮本地回扫的 **PMI 框架 / R3D / HEX / AirVLA**，D04 现在可以把“先几何、后形态、再动力学”的顺序继续压成一张真正可执行的 **P1-P4 判线协议**。这样首轮实验一出来，就不会再把 `shared geometry / morphology compensation / dynamics adapter / shell repair` 混成同一类贡献。

#### P1. 几何接口先验是否站稳（Geometry First）
**目的**：先判断共享 `PMI Packet` 是否真的可跨视角、轻遮挡、相机微扰稳定生成。

**默认配置**：
- 2D encoder baseline
- `R3D 3D encoder + diffusion decoder`
- 输出统一 `task_geometry_state / pre-contact pose / phase_token`

**首轮看三件事**：
- `PGS`：PMI geometry stability（同任务多视角输出一致性）
- `PIR`：PMI packet integrity rate（字段完整率）
- `APE`：approach pose error（接近位姿误差）

**判线规则**：
- 若 `R3D` 不能稳定提升 `PGS / PIR / APE`，则本轮**禁止**讨论后续 specialist / latent / physics adapter 谁更强。
- 若 `R3D` 显著提升几何稳定性，则 D04 主线继续保留“共享几何接口”为第一贡献位。

#### P2. 形态补偿是不是主瓶颈（Morphology Compensation Check）
**目的**：在几何接口已站稳前提下，判断跨载体掉点主要来自 kinematic / coordination mismatch，还是根本不是形态层问题。

**候选补偿层**：
- `HEX` 类 aligned-expert / specialist head
- morphology token / topology-aware attention
- unified latent retargeting 轻量 adapter

**核心读数**：
- `MCG`：morphology compensation gap
- `CFS`：cross-form success delta（地面臂→空中臂迁移成功率差）
- `RCR`：retarget correction rounds（为适配新载体需要的人类纠偏轮次）

**判线规则**：
- 若 `MCG` 高、但 `PGS` 已稳，则主叙事应转向 **shared geometry + lightweight morphology compensation**。
- 若 `MCG` 不高，则 HEX / specialist 不应抢主贡献位，只保留为对照或补件。

#### P3. 动力学修补是否主导（Dynamics Risk Check）
**目的**：确认问题是不是像 AirVLA 所示，视觉/几何已可迁移，但真正卡在 aerial dynamics gap。

**候选修补层**：
- `AirVLA` 式 inference-time payload-aware guidance
- `Hardware-Agnostic WM` 式 physics adapter
- 轻量 disturbance-aware rollout filter

**核心读数**：
- `DRB`：dynamics risk burden
- `TSR`：trajectory stabilizing ratio（加入 dynamics 修补后稳定回归比例）
- `PDS`：payload disturbance sensitivity（载荷/姿态扰动敏感度）

**判线规则**：
- 若 `PGS` 和 `MCG` 都已可接受，但 `DRB` 仍高，则论文主叙事切到 **共享几何先验 + inference-time physics adaptation**。
- 若 dynamics 修补收益只在极端扰动下出现，则保留为部署层，不上升为方法主贡献。

#### P4. 壳层收益是否被误记到 D04（Shell Attribution Check）
**目的**：防止把 D06 replanning 壳层或 D07 recovery controller 的收益误记成 D04 跨载体主干增益。

**需要单列的壳层模块**：
- D06: planner / frontier replanning / flight-stability shell
- D07: disturbance rejection / contact recovery / reflex controller

**核心读数**：
- `SDR`：shell dominance ratio
- `RGS`：recovery gain share（恢复控制带来的成功率占比）
- `RPS`：replan save rate（靠重规划救回的比例）

**判线规则**：
- 若提升主要来自 `RGS / RPS`，则收益应记到 D06/D07 接口层，不得作为 D04 主体贡献。
- 只有在关掉壳层后，D04 主干仍显著优于 baseline，才允许宣称“跨载体共享本身成立”。

#### 首轮默认顺序
1. **先跑 P1**：R3D 是否把 PMI Packet 立住
2. **再跑 P2**：若几何已稳，判定是否需要 HEX / specialist / latent retarget
3. **再跑 P3**：若形态层不是主因，检查 dynamics gap 是否主导
4. **最后跑 P4**：把 D06/D07 壳层收益从 D04 账本里剥离

#### 一句话主判断
D04 下一阶段不该再问“哪条跨载体路线最强”，而应先按 **P1 几何 → P2 形态 → P3 动力学 → P4 壳层归因** 跑出首轮证据；只有这样，论文主贡献才不会被补偿层和部署层冲淡。

### 3.9.7 首轮结果后的正文论证顺序冻结（R876新增）

结合本轮继续回扫的 **PointBridge / DeFM / CAPO / GaussFly**，以及在 QMD 回流后补做 arXiv Export API 外查但未发现比现有主线更贴合 D04 的高价值新论文，D04 现在已经不只需要冻结 **标题/摘要口径**，还要进一步把 **首轮结果出来后的正文论证顺序** 也写死。否则很容易出现一种假收束：标题似乎已经选了 shared geometry 或 physics adaptation，但正文里又重新让 `prompt / representation / specialist / latent / physics adapter` 五条线轮流抢解释权。

**正文默认排序固定为四段**：
1. **先论证共享几何是否成立**：只要 `PGS / IFR / ICS` 任一不过线，正文第一主段必须停在 **shared geometry interface not yet established**；此时 PointBridge / DeFM / CAPO / R3D 这类工作只能作为“为什么共享几何还没站稳”的诊断与修补线索，不能被写成跨载体共享已经成立。
2. **再论证 shared latent 是否已足够**：当 `IG0 + SC0` 已稳且 `GTG` 已低时，正文第二主段默认检查 shared latent 是否已经解释了大部分跨载体收益；若 `MCG < 3pp`，正文直接收成 **shared geometry + latent sufficiency**，specialist / morphology-aware head 自动降级为 supporting evidence。
3. **只有 shared 层不够时，才论证 morphology compensation**：只有在 shared geometry 已稳、shared latent 也不足以解释剩余误差，且 `MCG` 持续占优、`DRB` 不主导时，正文第三主段才允许升级为 **embodiment-aware compensation**。这一步等于把 morphology-aware 路线从“默认要讲”改成“必须赢了才配讲”。
4. **若 `DRB` 高，则正文直接转为 dynamics 残差主导**：当 shared geometry 已稳、`GTG` 已低，但 `DRB` 持续偏高，正文第四主段默认写成 **shared geometry + physics adaptation bottleneck**，把剩余困难明确归到 AirVLA / Hardware-Agnostic QuadWM / payload-aware guidance 这条线，而不是继续把 specialist 或 prompt orchestration 勉强写成主贡献。

**为什么要把正文顺序也冻结**：
- **PointBridge / DeFM** 的价值在于前置统一几何与跨域表征，而不是直接证明 embodiment-specific 补偿；
- **CAPO** 更像 domain factor 解耦与动态提示调度，它只有在 shared geometry 未稳时才更像诊断工具，而不是 D04 的最终主叙事；
- **GaussFly** 则再次提醒我们，高保真几何/表征改进之后，残差很可能继续落到 dynamics gap，而不是自然导向 morphology compensation。

**因此 D04 当前默认正文逻辑** 被正式冻结为：
- 先讲 shared geometry 是否立住；
- 再讲 shared latent 是否已经足够；
- 只有 shared 层不够，才允许 morphology compensation 升格；
- 若 dynamics residual 更高，则直接切向 physics adaptation bottleneck。

这一步的价值，是让 D04 在首轮结果出来后，不只知道标题怎么写、摘要怎么收，还知道正文第一段到第三段该按什么顺序组织证据。这样后续就不会再让 `specialist / latent / physics adapter` 三条线在正文主干里反复争位。

### 3.9.7 首轮结果出来后的正文排序规则（R878新增）

结合本轮继续回扫的 **RAFL / DeFM / PointBridge / CAPO / GaussFly**，以及 QMD 回流后补做 arXiv 外查但未发现更贴合 D04 主线的新高价值论文，D04 现在不只需要冻结 **标题/摘要口径**，还要把 **正文第一版该按什么顺序论证** 也正式写死。否则很容易出现标题已经收束，但正文里又把 `specialist / latent / physics adapter` 三条线全部摊开、重新变散的问题。

**正文默认顺序固定为四段**：
1. **先证明 shared geometry interface 是否成立**：若 `PGS / IFR / ICS / PMI Packet 完整率` 仍不过线，正文第一核心段只能写成 **shared geometry interface not yet established**，不得提前讨论 latent sufficiency、morphology compensation 或 physics adapter 的优劣。
2. **若 shared geometry 已稳，再证明 shared latent 是否已足够**：当 `GTG` 已低且 `MCG < 3pp` 时，正文默认收成 **shared geometry + latent sufficiency**；此时 `specialist / morphology-aware head` 自动降级为 supporting evidence，而不是平行主线。
3. **只有 shared 层解释不完，才允许 morphology compensation 升格**：只有当 `MCG` 连续占优、且 `DRB` 不主导时，正文中段才允许转入 **embodiment-aware compensation**，把 `HEX / morphology token / specialist head` 升格为核心解释层。
4. **若 `DRB` 高，则正文后半自动改写为 dynamics bottleneck**：一旦 shared geometry 已稳、shared latent 已基本够用，但 `DRB` 持续偏高，则正文默认收成 **shared geometry + physics adaptation bottleneck**，把 `AirVLA / payload-aware guidance / Hardware-Agnostic QuadWM` 放到主解释位，而不是继续细拆 morphology 路线。

**为什么这一步必要**：
- **PointBridge / DeFM / CAPO** 更适合被放在 shared geometry 与 representation 这两段中解释，而不是提前拿去支撑 embodiment-specific 补偿；
- **GaussFly** 提醒我们很多“迁移有效”其实可能来自高质量场景/表征桥接，而不是补偿头本身；
- 若正文不按这四段顺序写，D04 很容易再次回到“什么都有一点贡献”的工程汇报口径，而不是可投稿论文应有的单主线论证。

**当前默认正文骨架**：
- 第一节：`shared geometry interface established or not`
- 第二节：`shared latent sufficient or not`
- 第三节：`morphology compensation necessary or not`
- 第四节：`physics adaptation bottleneck or not`

这一步的核心价值，是让 D04 从“标题知道怎么冻结”继续推进到“正文也知道先证明什么、后证明什么”，避免首轮结果一出来又重新摊大饼。

## 3.9.7 首轮结果出来后的正文排序规则（R878新增）

结合本轮继续回扫的 **RAFL / DeFM / PointBridge / CAPO / GaussFly**，并在 QMD 回流后补做 arXiv 外查但未发现更贴合 D04 当前主线的新高价值论文，D04 现在已经不只需要冻结 **标题 / 摘要口径**，还要把 **正文第一版的默认论证顺序** 一并写死。否则一旦首轮结果出来，很容易又回到 `specialist / latent / physics adapter` 三条线都想在正文核心段落里占位的老问题。

**正文默认按四段固定顺序写作**：
1. **shared geometry 是否真的成立**：先看 `PGS / IFR / ICS / PMI Packet 完整率`。只要这里不过线，正文第一核心段就只能写成 **shared geometry interface not yet established**，不得提前放大 CAPO 式 prompt orchestration、PointBridge/DeFM 式表征收益，或任何 specialist / adapter 的跨载体价值。
2. **shared latent 是否已经足够**：只有当 shared geometry 已稳时，才继续看 `GTG`。若 `GTG` 已低且 `MCG < 3pp`，正文默认收成 **shared geometry + latent sufficiency**，把 `Unified Latent Space / LAD / latent retarget` 升为 shared 层主解释，specialist 自动降级为 supporting evidence。
3. **morphology compensation 是否真有持续收益**：只有当 shared geometry 已稳、而 shared latent 仍解释不完剩余掉点，且 `MCG` 连续占优、`DRB` 不主导时，才允许把正文主位升到 **embodiment-aware compensation**，让 `HEX / morphology-aware token / specialist head` 进入核心论证段。
4. **dynamics gap 是否才是主残差**：若 `DRB` 高，即使前两层已成立，正文后半也应自动改写成 **shared geometry + physics adaptation bottleneck**，把 `AirVLA / Hardware-Agnostic QuadWM / inference-time physics adapter` 升为主解释，而不再继续细拆 morphology compensation。

**这条规则的核心价值**：
- `RAFL / PointBridge / DeFM` 主要服务 shared geometry 是否成立；
- `Unified Latent Space / LAD` 主要服务 shared latent 是否已足够；
- `HEX / specialist head` 只有在 shared 层解释不完时才配升格；
- `GaussFly / AirVLA / physics adapter` 负责解释 residual dynamics gap。

也就是说，D04 现在不只冻结了标题与摘要，也把 **正文第一版该先证明什么、后证明什么** 一并写死。这样首轮结果一出来，就能立刻判断论文该先证明共享几何、shared latent sufficiency，还是把剩余问题收成动力学残差，而不会再让 `specialist / latent / physics adapter` 三条线同时挂在主文核心段落上。

### 3.9.8 IG0 前置后，证据归位与摘要模板继续冻结（R886新增）

在 R885 已把 `IG0 (Interface Gate)` 放到 `SC0` 前面之后，本轮继续把 **证据归位** 与 **摘要默认句式** 写得更死，避免首轮结果出来后又把 `geometry gain / latent gain / compensation gain` 混写到一段里。

**新增冻结规则**：
1. **GaussFly / R3D / PointBridge / DeFM** 这类工作，默认只允许为 **shared geometry / representation bridge 已过线** 提供证据；即它们只能回答“几何接口是否立住”，不能直接拿来证明 shared latent 已足够，更不能越级证明 embodiment-aware compensation 必不可少。
2. **Unified Latent Space / LAD** 只允许在 `IG0 + SC0` 已过线后出场，作为 **shared latent sufficiency** 的主证据；若 `IFR / ICS / PMI Packet 完整率` 还没稳，就算 latent 模型读数漂亮，也只能降级为 supporting evidence。
3. **RAFL / AirVLA / dynamics adapter** 相关证据只在 `DRB` 高时升格为正文主解释；否则一律不得提前抢走 shared latent 的叙事位。
4. **CAPO** 这类 domain-factor / prompt 组织类证据，只保留为 `domain-factor suppression` 的旁证，默认不参与 D04 主标题竞争。

**新的摘要默认模板**：
- 若 `IG0` 未过：摘要第一句只能写 **shared geometry interface not yet established**。
- 若 `IG0 + SC0` 已过、且 `GTG` 下降而 `MCG < 3pp`：摘要第二句默认写 **shared geometry plus latent sufficiency explains most cross-embodiment gain**。
- 只有当 `MCG` 连续占优且 `DRB` 不主导时，摘要第三句才允许升格为 **embodiment-aware compensation remains necessary after shared latent alignment**。
- 若 `DRB` 高，则第三句自动改写为 **residual error is dominated by dynamics adaptation bottleneck rather than morphology compensation**。

**核心价值**：D04 现在不只冻结了接口门顺序，还把“哪些论文证据能落在哪一层解释”与“摘要最终该怎么诚实落句”一起写死。这样后续首轮实验一出来，就能直接判成 geometry 未立住、latent 已足够、compensation 仍必要，还是 dynamics bottleneck 主导，不再把 representation gain / latent gain / residual gain 混成一句漂亮话。

## 3.9.7 首轮结果出来后的正文排序规则（R880新增）

结合本轮继续回扫的 **RAFL / PointBridge / DeFM / CAPO / GaussFly / Unified Latent Space / LAD**，D04 现在不只需要冻结标题、摘要和主叙事，还需要把**正文第一版的论证顺序**彻底写死。否则就算标题已经收成 `shared geometry`、`latent sufficiency` 或 `physics adaptation bottleneck`，正文里仍然可能偷偷把 `specialist / representation boost / sim2real residual` 全塞回核心段落，重新摊大饼。

**正文默认固定四段顺序**：
1. **先证明 shared geometry interface 是否成立**：正文第一核心段固定只讨论 `PGS / IFR / ICS / PMI Packet 完整率`。只要这几项不过线，正文第一版就只能写成 **shared geometry interface not yet established**，不得提前放大 PointBridge 的 3D 表征收益、DeFM 的 depth foundation gain、CAPO 的 orchestration 提升，或 RAFL/GaussFly 的 sim2real 收益。
2. **shared geometry 成立后，再看 shared latent 是否已经足够**：若 `GTG` 已低，且 latent 共享路线能解释大部分跨载体增益，正文第二段默认收成 **shared geometry + latent sufficiency**，把 `Unified Latent Space / LAD / latent retarget` 升为主解释，不再默认给 morphology-aware specialist 留主位。
3. **只有 shared 层解释不完时，才允许 morphology compensation 升格**：若 `MCG` 连续稳定占优，且这种收益不能被 shared geometry / shared latent 吸收，正文第三段才允许写成 **embodiment-aware compensation**；否则 morphology token / specialist head / embodiment-aware residual 一律降级为 supporting evidence。
4. **若 dynamics gap 持续主导，正文后半自动改写为 physics adaptation bottleneck**：当 `DRB` 高、且 RAFL/GaussFly/AirVLA 一类结果持续显示主要瓶颈在 sim2real residual、payload-aware correction 或 dynamics mismatch，正文后半默认切成 **shared geometry + physics adaptation bottleneck**，把 residual field / physics adapter / inference-time correction 提升为主残差解释，而不是继续纠缠 morphology token。

**为什么本轮值得把正文顺序写死**：
- **PointBridge / DeFM** 提醒我们：很多“跨载体提升”其实先来自更稳的几何/深度表征，如果 geometry interface 还没立住，就不该过早谈更高层补偿。
- **Unified Latent Space / LAD** 提醒我们：shared latent 可能已经解释了大部分共性收益，此时 specialist 不该默认留在主位。
- **RAFL / GaussFly / AirVLA** 则提醒我们：当 shared 几何已成立、shared latent 也不差，但 real-world 掉点仍高，主残差往往已经转向 dynamics gap，而不是 morphology mismatch 本身。

**因此 D04 当前正文第一版的固定顺序正式冻结为**：
`shared geometry 是否成立 → shared latent 是否已足够 → morphology compensation 是否真有持续收益 → dynamics gap 是否才是主残差`

这让 D04 不只知道标题和摘要该怎么诚实收束，连正文核心段落也有了固定排序；后续首轮结果一出来，就能直接判断论文正文该先证明共享几何、shared latent 已够，还是动力学残差才配占正文主位，不再让 `specialist / latent / physics adapter` 三条线同时挂在主文核心段落上。

### 3.9.7 IG0 前置门后的最终解释闸门（R885新增）

结合本轮继续回扫的 **GaussFly / CAPO / RAFL / PointBridge / DeFM / Unified Latent Space / LAD / AirVLA / R3D**，D04 现在可以把“接口门前置 + shared latent sufficiency 默认优先”再往前压一层：**不仅要冻结解释顺序，还要冻结‘什么条件下根本不允许谈 latent sufficiency’**。否则很容易在 `IFR / ICS / PMI Packet 完整率` 还没站稳时，就提前把轻微提升误解成 shared latent 已经足够，重新把 geometry gain、latent gain、residual gain 混写到一起。

**新增最终解释闸门如下**：
1. **IG0（Interface Gate）必须先过**：只要 `IFR / ICS / DMS / PMI Packet 完整率` 任一不过线，正文与汇报一律只能收成 **shared geometry interface not yet established**；此时 `Unified Latent Space / LAD` 都不得升格为主解释，只能作为“如果接口稳住后可继续验证的候选机制”。
2. **SC0 过线后才允许谈 shared latent sufficiency**：当 `IG0 + SC0` 已稳、`GTG` 下降且 `MCG < 3pp`，默认解释直接收成 **shared geometry + latent sufficiency**；也就是说，只要 shared geometry 已立住、额外 embodiment-aware compensation 还没给出稳定持续收益，就不再默认把 specialist / morphology-aware 头保留在主叙事位。
3. **只有 shared 层解释不完时，才允许 residual 抢位**：若 `MCG` 连续占优且 `DRB` 不主导，才允许升格为 **embodiment-aware compensation**；反之若 `DRB` 高，则自动改写为 **shared geometry + dynamics adaptation bottleneck**，把主解释切向 `AirVLA / payload-aware guidance / physics adapter`。
4. **证据归位进一步写死**：`GaussFly / PointBridge / DeFM` 只负责证明 geometry / representation 层是否过线；`RAFL` 只负责说明 dynamics residual 是否依旧主导；`CAPO` 只允许作为 domain-factor suppression 的次级证据；`Unified Latent Space / LAD` 只在 `IG0 + SC0` 已稳后，才允许出场解释 shared latent sufficiency。

**这一步的意义**：D04 现在不只冻结了“先 geometry、再 latent、最后 residual”的解释顺序，还把“什么时候才有资格谈 latent sufficiency”写成了明确闸门。后续只要首轮实验一出来，就能更快把结论判成 `geometry 未立住 / latent 已足够 / morphology compensation 生效 / dynamics bottleneck 主导` 四档之一，避免 representation gain、latent gain、payload gain 再被写成一锅粥。

## 四、实验设计

### 4.1 数据集/仿真环境
- **仿真**: UE5 + AirSim/AirSpark（主人已有经验）
- **跨载体实验平台**: 地面机械臂（Franka/自研）→ 空中机械臂（龙虾项目）
- **配对数据**: 仿真自动生成「同任务-不同载体」配对轨迹
- **真机验证**: 龙虾无人机 + 地面机械臂双平台

### 4.1+ 首个主任务锁定建议（R818新增）

基于本地已读的 **Unified Latent Space / Hardware-Agnostic QuadWM / AirVLA**，D04 首轮主任务不宜直接选“导航→接近→抓取→运送”全链条，而应先锁到一个足够短、却能同时暴露几何层/形态层/动力学层差异的最小任务：
| 候选任务 | 优点 | 风险 | 结论 |
|---|---|---|---|
| **T1 静态单物体接近→抓取→抬升10cm** | 最容易拆账 `GTG/MCG/DRB`，能直接比较 adapter / specialist / physics adapter | 任务语义较简单，论文故事需要靠跨载体对照撑住 | **首选主任务** |
| T2 抓取→放置 | 比 T1 多一个放置位姿约束，更接近真实操作 | 容易把末端放置误差与飞行稳定误差混在一起 | 第二阶段再上 |
| T3 导航→接近→抓取连续任务 | 最贴近 D06/D04 联合闭环 | 太容易把 planner 壳层收益误记成 D04 主干收益 | 暂不作为首轮主任务 |

**本轮建议**：先把 D04 第一阶段正式锁到 **T1 静态单物体接近→抓取→抬升10cm**。
原因很简单：
1. 它已经足够包含 `几何接近 → 末端构型匹配 → 动力学扰动` 三层误差来源。
2. 它最容易和 `human geometry anchor / latent retarget / specialist head / physics adapter` 做干净对照。
3. 一旦 T1 站稳，再升到 T2/T3 时，才能清楚知道新增收益来自任务延长，而不是首轮定义混乱。

### 4.2 统一对照实验表（核心产出）

| 实验编号 | Paired数据量 | 形态先验注入 | Latent统一方案 | 新载体接入模式 | 验证任务 |
|---------|------------|------------|--------------|--------------|---------|
| **Exp-A1** | 0（零样本） | 无 | 无 | Latent Retarget | 抓取/放置 |
| **Exp-A2** | 50条paired | 无 | 无 | Latent Retarget | 同上 |
| **Exp-A3** | 200条paired | 无 | 无 | Latent Retarget | 同上 |
| **Exp-B1** | 50条paired | kinematic tokens | 无 | Adapter微调 | 同上 |
| **Exp-B2** | 50条paired | 无 | LAC-WM-style latent | Adapter微调 | 同上 |
| **Exp-B3** | 50条paired | kinematic tokens | LAC-WM-style latent | Adapter微调 | 同上 |
| **Exp-B4** | 50条paired | morphology params | frozen WM physics adapter | 零训练/极少校准 | 同上 |
| **Exp-B5（R795新增）** | 50条paired | generalist backbone + embodiment specialist head | unified latent | 只训练轻量 specialist head | 同上 |
| **Exp-C1** | 0 | 无 | 无 | Full Retrain | 同上 |
| **Exp-C2** | 200条paired | 无 | 无 | Full Retrain | 同上 |
| **Exp-D1（ours）** | 50条paired | kinematic tokens | unified latent | Lightweight adapter | 同上 |
| **Exp-D2（ours）** | 200条paired | kinematic tokens | unified latent | Lightweight adapter | 同上 |
| **Exp-D3（ours）** | 200条paired | kinematic tokens | unified latent | Latent Retarget（零训练） | 同上 |
| **Exp-E1（R789新增）** | `human几何演示` + 20条空中锚点 | 无 | 无 | Adapter微调 | 接近位姿预测 |
| **Exp-E2（R789新增）** | `human几何演示` + 20条空中锚点 | kinematic tokens | unified latent | Lightweight adapter | 接近+抓取 |
| **Exp-E3（R789新增）** | `ground robot paired` + `human几何演示` + 20条空中锚点 | kinematic tokens | unified latent + physics adapter | 零训练/极少校准 | 接近+抓取+扰动恢复 |

**预期结果**: Exp-D3 成功率接近 Exp-C2（<5% gap），但接入代价（数据量/微调轮次）接近 Exp-A1。R789 额外要验证的是：**Exp-E2 / E3 是否能用极少空中锚点复现大部分目标载体几何先验与执行收益**。

### 4.2+ 任务阶梯与 baseline 家族（R789推进）

| 阶段 | 任务定义 | 目的 | 建议baseline家族 |
|------|---------|------|----------------|
| **L0 几何表征** | 只输出 `task_geometry_state`，不进入控制层 | 先验证 3D backbone 与 PMI Packet 是否稳定，不把感知锅记成跨载体锅 | R3D 3D encoder / 2D encoder baseline |
| **L1 几何接近** | 只预测 pre-grasp / pre-contact 位姿，不执行闭环抓取 | 先验证 human geometry anchor 是否真有价值 | CEI / Lidea-style geometry alignment |
| **L2 准静态抓取** | 固定底座或弱扰动下完成抓取/放置 | 验证 latent 统一与 morphology token 的真实增益 | OPFA / LAD / LAC-WM |
| **L3 空中弱扰动抓取** | 挂载空中平台，小幅姿态漂移 | 验证 physics adapter / payload-aware 修补是否必要 | AirVLA-style guidance / physics adapter |
| **L4 空中动态恢复** | 加入接触后偏移、目标轻微移动、二次接近 | 验证 D04 方法在真实部署场景的保真度 | D07 recovery / ROBOGATE-style failure coverage |

### 4.2++ Generalist vs Specialist 接入协议（R795新增）

R792 的 **Embodiment-Aware Generalist Specialist Distillation** 说明，D04 后续不能只把“共享主干”与“载体差异”粗暴地二选一，而应把它写成一条独立 baseline 家族：

| 家族 | 共享部分 | 载体专属部分 | 预期优势 | 主要风险 |
|------|---------|-------------|---------|---------|
| **G0 Full shared** | encoder + policy + decoder 全共享 | 无 | 参数最省，接入最简 | 易被 morphology conflict 拖慢，新载体上限低 |
| **G1 Shared + adapter** | 主干共享 | 小型 adapter | 成本低，容易接已有模型 | adapter 容量不足时补不动动力学差异 |
| **G2 Shared + specialist head** | 感知/语义/latent 主干共享 | 轻量 embodiment head | 兼顾共享技能与载体补偿，适合新载体低成本接入 | specialist 可能偷学任务本体，导致共享层价值被高估 |
| **G3 Physics adapter + shared policy** | 共享 policy / latent | dynamics/physics adapter | 更适合空中载体这类动力学差异大场景 | 需要额外校准与稳定的系统辨识 |

**本轮决定**：把 `G2 Shared + specialist head` 正式升为 D04 的标准对照位，与 `adapter / latent retarget / physics adapter` 并排，而不是继续把 specialist 只当 engineering trick。

### 4.2+++ Benchmark 拆分协议（R803新增）

受 **AnyBody (2505.14986)** 启发，D04 后续不能只报一个“跨载体平均成功率”，而应把泛化显式拆成三档：

| split | 含义 | D04 中对应问题 | 最该比较的路线 |
|---|---|---|---|
| **S1 Interpolation** | 同一形态家族内，只改几何尺寸或轻微参数 | 方法是否只是记住了同类机器人的尺度变化 | `shared + adapter`、`morphology token` |
| **S2 Extrapolation** | 训练时见过多种形态，但测试时是新 link structure / 新载体类别 | latent 统一、physics adapter 是否真能跨结构外推 | `latent retarget`、`physics adapter`、`generalist+specialist` |
| **S3 Composition** | 测试载体由训练中见过的部件重新组合而成 | 方法是否真正学会了“部件功能组合”，而不是记住具体机体 | `human geometry anchor`、`generalist+specialist`、`morphology-randomized pretraining` |

**使用规则**：
1. D04 主结果表至少同时报告 `S1/S2/S3`，不再只报平均 SR。
2. 若方法只在 S1 强，默认它更像“同家族适配器”，不能宣称强跨载体泛化。
3. 若方法在 S3 明显掉点，优先回查 `任务几何表述` 和 `形态组合先验`，而不是盲目增加目标载体数据量。
4. 空中机械臂最终更贴近 **S2+S3**，因此论文主结论应以这两档为主，不被 interpolation 成绩误导。

### 4.2++++++ 首轮结果→主补偿层判线表（R826新增）

为了让 D04 真正在**第一轮实验结果出来后就能收缩路线**，需要把 `GTG / MCG / DRB / SDR` 从“描述性指标”进一步推进成**判线表**。核心目的不是再造一套指标，而是防止 `shared geometry / specialist / physics adapter / shell` 四层在首轮之后继续混账。

| 首轮读数模式 | 更可能的主瓶颈 | 默认收缩动作 | 对 D04 主文的影响 |
|---|---|---|---|
| `GTG高` | 几何接口层没站稳 | 暂停 specialist / physics adapter 扩展，只修 `PMI Packet + 3D geometry backbone` | 只写共享意图接口未稳，不宣称跨载体主干成立 |
| `GTG低 + MCG低 + DRB高` | 动力学残差主导 | specialist 降级为对照支线，优先上 `physics adapter / payload-aware guidance` | 主文改为 `shared backbone + dynamics repair` |
| `GTG低 + MCG高 + DRB低` | 形态补偿主导 | 保留 `specialist head / morphology token` 为主线，physics adapter 留作补充实验 | 主文偏向 `shared geometry + morphology compensation` |
| `GTG低 + MCG低 + DRB低 + SDR高` | 部署壳层主导 | 冻结 D04 继续扩模型，把资源转向 D06/D07 shell 协同 | 主文必须写成“共享主干 + 部署壳层协同” |
| `GTG低 + MCG中高 + DRB中高` | 形态层 + 动力学层双补偿 | 两条补偿线并存，但先压缩到单任务单物体，不再扩任务宽度 | 主文写成串联双补偿，不提前押单一路线 |

这张表把 D04 从“比很多路线”继续推进到“**第一轮就知道谁该缩、谁该留**”。对主人最直接的价值，是后续即使只拿到一组 12h 级实验，也能立刻判断下一周该把 GPU 小时押给 `HEX/形态补偿` 还是 `AirVLA/QuadWM/动力学修补`。

### 4.2+++++++ 首轮主补偿层选择协议（R828新增）

R826 已经把 `GTG / MCG / DRB / SDR` 压成了首轮判线表，但 D04 现在还差最后一步：**当首轮结果同时出现两个中高读数时，下一轮到底优先给谁预算**。这件事如果不写死，后面很容易出现 `specialist 也想再补一点、physics adapter 也想再补一点、shell 也先留着` 的拖延式推进。

因此补一张 **主补偿层选择协议**，只回答一个问题：**下一轮 GPU 小时与实现精力先押给谁**。

| 首轮结果模式 | 默认主补偿层 | 默认次补偿层 | 下一轮优先动作 | 暂缓动作 |
|---|---|---|---|---|
| `GTG高` | 无（先修共享几何层） | 无 | 只修 `R3D / PMI Packet / human geometry anchor` | 暂缓 `specialist / physics adapter / shell` 扩展 |
| `GTG低 + MCG高 + DRB低` | **形态补偿层** | latent retarget | 先压实 `shared+specialist / morphology token`，把 `MCG` 做成稳定复现 | physics adapter 降为补充验证 |
| `GTG低 + MCG低 + DRB高` | **动力学补偿层** | latent/shared backbone | 先压实 `physics adapter / payload-aware guidance`，把 `DRB` 压到黄色区以下 | specialist 降为对照支线 |
| `GTG低 + MCG中高 + DRB中高` | **先动力学，后形态** | 形态补偿层 | 先做弱扰动与 payload 条件下的 `DRB` 收敛，再回头看 `MCG` 是否仍显著 | 不扩任务宽度，不先做 shell 优化 |
| `GTG低 + MCG高 + DRB高` | **双补偿并存，但先锁单任务** | shell | 在 `T1 单物体接近→抓取→抬升` 上并行保留 `specialist + physics adapter`，禁止扩到长链任务 | 暂缓 D06 式 planner 扩展 |
| `GTG低 + MCG低 + DRB低 + SDR高` | **部署壳层** | 无 | 冻结 D04 主干扩展，把资源转给 D06/D07 shell 协同 | 暂缓再做 shared backbone 结构改造 |

**默认优先级原则**：
1. **几何层 > 动力学层 > 形态层 > 壳层表述**。几何接口没站稳时，后面都不许抢预算。
2. 当 `DRB` 与 `MCG` 同时高时，**先看真实部署风险**——空中平台默认优先处理动力学层，因为它更可能直接导致真机不可执行。
3. 只有当 `DRB` 已被压到黄色区，`MCG` 仍显著时，specialist / morphology token 才升级为下一轮主补偿层。
4. 若 `SDR` 持续高，即使 `MCG / DRB` 也有收益，论文主叙事仍必须保留“共享主干 + 壳层协同”，不能把部署壳层从故事里删除。

这样 D04 下轮就不再是“继续看情况”，而是能在第一组结果出来后立刻决定：**先修 geometry、先押 physics adapter，还是正式保留 morphology compensation 为主线**。

### 4.2+++++++++ 首轮预算冻结协议（R831新增）

R828 已经把 `GTG / MCG / DRB / SDR` 压成了**主补偿层选择协议**，但真到执行时还会剩最后一个常见混乱：
**同一轮里，geometry / specialist / physics adapter / shell 往往都“看起来值得再补一点”**，于是预算就会被平均撒开，结果下一轮什么都没真正判清。

所以本轮继续把 D04 往执行侧压一格，补一张 **首轮预算冻结协议**，只回答一件事：
**当首轮结果出来后，下一轮哪些层允许继续拿预算，哪些层必须冻结为只读对照。**

| 首轮状态 | 允许继续拿预算的层 | 必须冻结为只读对照的层 | 默认下一轮动作 |
|---|---|---|---|
| `GTG高` | `R3D / PMI Packet / human geometry anchor` | `specialist / physics adapter / shell` | 只修共享几何层，先把 `PGS` 与 `PMI Packet 完整率` 拉稳 |
| `GTG低 + MCG高 + DRB低` | `specialist head / morphology token` | `physics adapter / shell` | 只放大形态补偿层，验证 `MCG` 是否能稳定复现 |
| `GTG低 + MCG低 + DRB高` | `physics adapter / payload-aware guidance` | `specialist / shell` | 只压动力学残差，先把弱扰动和 payload 条件下跌幅收下来 |
| `GTG低 + MCG中高 + DRB中高` | `physics adapter`（主）+ `specialist`（副） | `shell` | 先单任务压 `DRB`，待动力学进黄区后再看 `MCG` 是否还显著 |
| `GTG低 + MCG低 + DRB低 + SDR高` | `D06/D07 shell` | `D04 主干结构改造` | 明确转入“共享主干 + 壳层协同”叙事，不再扩 D04 主干参数 |
| `GTG低 + MCG高 + DRB高` | `specialist + physics adapter`（仅限单任务） | `任务扩展 / planner壳层` | 只保留 `T1 接近→抓取→抬升` 单任务，禁止扩到长链任务 |

**冻结原则**：
1. **没领到主预算的层，只能保留最小对照，不允许继续加参数、加数据、加实现复杂度。**
2. **Shell 默认最后拿预算**。除非 `SDR` 已明确过高，否则不允许先把工程时间投给 D06/D07 壳层优化。
3. **当 `DRB` 与 `MCG` 同时高时，先保真机可执行性**——空中平台默认先修动力学层，再回头判断 specialist 是否仍有独立收益。
4. **任务宽度晚于补偿层归因**。只要主补偿层还没判清，禁止从 `T1` 扩到 `T2/T3`。

这张表的意义很简单：D04 现在不只是“知道下一步大概该修哪层”，而是能在首轮结果出来后，**立刻冻结不该继续烧 GPU/工时的层**。这样后面每一轮推进都更像论文收束，而不是工程摊大饼。

### 4.3 评价指标
- **SR**: 任务成功率
- **Transfer Ratio**: 源载体→目标载体的成功率维持比（CEI标准）
- **Onboarding Cost**: ①目标载体训练数据量②人工correction轮次③微调GPU小时
- **PGS (Perception-to-Geometry Stability)**: 同一任务在不同观测扰动/不同载体视角下，`task_geometry_state` 的方差与一致性，用来判断几何接口是否先站稳
- **Anchor Efficiency**（R779新增）: 每增加 1 条目标载体锚点数据带来的成功率提升，用来衡量“少量真机数据是否真的高杠杆”
- **Specialist Gain per Parameter（R795新增）**: 每增加一单位 specialist 参数带来的成功率/恢复率提升，用来判断“载体专属补偿”是否真的比 full retrain 划算
- **Latent Space质量**: 对齐度（CCA/MMD）、插值平滑性
- **Split-wise Generalization Gap（R803新增）**: 分别统计 `S1→S2` 与 `S2→S3` 的性能跌落，用来判断方法是卡在结构外推，还是卡在部件组合泛化

### 4.3+ 成本归一化主指标（R807新增）

仅报 `平均成功率 + onboarding cost` 还不够，因为 D04 很容易出现两种伪优势：
1. **只在 S1 interpolation 强**，却把结果写成“强跨载体泛化”；
2. **靠大量目标载体锚点或 specialist 参数堆上去**，却把结果写成“低成本接入”。

因此 D04 后续统一采用一个 **成本归一化跨载体分数**，先把泛化质量和接入代价绑在一起：

\[
\text{CEES} = 0.2 \cdot SR_{S1} + 0.4 \cdot SR_{S2} + 0.4 \cdot SR_{S3}
- \lambda \cdot \text{NormCost}
- \gamma \cdot \text{SplitGap}
\]

其中：
- `NormCost` = 归一化后的 `目标载体真机数据量 + 人工纠偏轮次 + GPU小时 + specialist参数增量`
- `SplitGap` = `max(S1-S2, 0) + max(S2-S3, 0)`，用于惩罚“只会 interpolation，不会 extrapolation/composition”的路线
- 默认权重先取 `λ=0.15, γ=0.10`，后续按主人真实采集成本再调

**使用规则**：
1. 主结果表必须同时给出 `平均SR` 与 `CEES`，不允许只报其一。
2. 若某路线 `平均SR` 高但 `CEES` 低，默认它更像“高成本特调方案”，不能作为 D04 主线。
3. 若某路线 `S1` 很高但 `S2/S3` 明显掉点，即使平均分不差，也优先回查 `任务几何表述 / latent统一 / physics adapter`，而不是继续加目标载体数据。
4. 论文主结论优先按 `CEES` 排名，而不是按单一成功率排名，这样更贴合主人真正关心的“能不能低成本把新载体接进来”。

### 4.3++ 失效归因协议（R812新增）

D04 后续还有一个很容易混账的问题：
同样是“新载体失败”，原因可能根本不是同一类。有些是 **任务几何没对齐**，有些是 **morphology 补偿不够**，还有些其实已经超出 D04，落到 **D06 的 planner/controller 壳层** 或 **D07 的扰动恢复/接触控制壳层**。如果不先拆账，后面很容易把执行壳层问题误记成跨载体共享主干失效。

因此统一增加一个 **四段失效归因表**：

| 归因层 | 典型症状 | 优先回查 | 更像该归谁 |
|---|---|---|---|
| **L-G 几何层** | pre-contact 位姿就偏，接近方向错，抓取前构型不合理 | `human geometry anchor` / `task geometry state` / anchor 标注质量 | D04 轴A/轴B |
| **L-M 形态层** | 几何接近对，但换载体后 reachability、关节协同或末端构型崩 | `kinematic token` / `specialist head` / morphology-aware backbone | D04 轴D |
| **L-D 动力学层** | 静态任务能过，弱扰动或飞行状态一加就掉点 | `physics adapter` / payload-aware guidance / frozen WM adapter | D04 轴C/D，且与 D06/D07 交界 |
| **L-S 壳层层** | 共享子目标本身合理，但 replanning、局部回稳、碰撞恢复差 | planner-controller interface / disturbance recovery / controller shell | 优先记到 D06/D07，不直接算 D04 主干失败 |

**配套诊断指标**：
- **GTG (Geometry Transfer Gap)**：`L1几何接近成功率 - L2准静态抓取成功率`，大 gap 说明几何表示可用但执行映射失真。
- **MCG (Morphology Compensation Gain)**：`shared+specialist` 或 `morphology token` 相对 `full shared` 的收益，低于 3pp 时不值得把载体差异继续堆进结构分支。
- **DRB (Dynamics Residual Burden)**：`L2准静态` 到 `L3空中弱扰动` 的跌幅，用于判断动力学失配是否已成为主瓶颈。
- **SDR (Shell Dependency Ratio)**：共享 planner/latent 固定后，`controller shell` 相对 `direct execution` 的收益占比；若 SDR 很高，说明当前优势主要来自部署壳层，不应夸大 D04 共享主干贡献。

**使用规则**：
1. 任何 D04 主结果都至少要带 `GTG + DRB`，否则无法判断失败究竟卡在跨载体共享，还是卡在飞行/接触执行壳层。
2. 若 `GTG` 小但 `DRB` 大，优先接 D06/D07 修补，不继续盲加 paired data。
3. 若 `MCG` 持续很低，优先保留 `shared+adapter` 或 `latent retarget`，不强推 specialist 路线。
4. 若 `SDR` 高于预设阈值（如 0.5），论文叙事必须明确写成“共享主干 + 部署壳层协同”，不能把收益全部记成 D04 本体创新。

### 4.4 消融实验
1. paired-data quantity (Exp A系列)
2. morphology-aware backbone (Exp B1 vs B2)
3. latent action统一 (Exp B2 vs B3)
4. 接入模式四路对比 (Full Retrain vs Adapter vs Latent Retarget vs Frozen-WM Physics Adapter)
5. 空中特有：动力学约束注入对跨载体成功率的影响（接D06）
6. **Anchor ratio ablation（R779新增）**：固定总数据预算，对比 `纯目标载体真机`、`robot-free/human数据 + 少量目标载体锚点`、`地面机器人数据 + 少量空中载体锚点` 三组混合比，验证“少量物理锚点是否足以替代大规模目标载体采集”
7. **Physics-adapter ablation（R786新增）**：固定 policy 主干与 paired 数据量，对比 `kinematic token`、`latent retarget`、`frozen WM physics adapter` 三种接入方式，记录零样本成功率、校准步数与动力学失配恢复能力
8. **Human-geometry ablation（R789新增）**：固定空中锚点数量，对比 `无human几何`、`只加human语义蒸馏`、`human语义+显式几何对齐` 三组，验证 Lidea 式桥接究竟提升的是 pre-contact 几何质量、还是只是视觉表征更稳
9. **Generalist-specialist ablation（R795新增）**：固定共享主干与 paired 数据预算，对比 `full shared`、`shared+adapter`、`shared+specialist head`、`shared+physics adapter` 四类接入方式，记录新载体成功率、恢复率、参数增量与接入校准时间
10. **PMI Packet ablation（R825新增）**：固定共享 latent 与 adapter 预算，对比 `直接输出动作`、`只输出pre-contact pose`、`输出完整 PMI Packet` 三组，记录 `PGS / GTG / DRB / SDR`，验证显式可验证意图接口是否真能减少“感知失败被误写成跨载体失败”的混账

### 4.4+ 阶段判停门槛（R789推进）
- **Gate-G0（R825新增）**: 若 `PGS` 不稳定，或 L0 在视角扰动下 `task_geometry_state` 明显飘移，禁止进入 L1，先修 3D backbone / PMI Packet 字段定义。
- **Gate-G1**: 若 L1 几何接近成功率 < 85%，禁止进入 L2，先修任务几何表述或锚点标注。
- **Gate-G2**: 若 L2 相对 Full Retrain 的 gap > 10%，优先补 latent / morphology 结构，不急着上空中平台。
- **Gate-G2.5（R795新增）**: 若 `shared + specialist head` 比 `shared + adapter` 提升 < 3pp，但参数/校准成本明显更高，则说明 specialist 路线对当前任务不划算，优先保留更轻的 adapter/latent retarget。
- **Gate-G3**: 若 L3 在弱扰动下 recovery failure > 20%，优先接 D06/D07 修补层，不把问题误归因于跨载体共享主干。
- **Gate-G4**: 只有当 L4 达到可重复演示后，才把 D04 成熟度从 🟡 推向 🟢。

### 4.4++ 首轮最小验证顺序（R817新增）

基于本地已读的 **Unified Latent Space / HEX / Hardware-Agnostic QuadWM / AirVLA**，D04 首轮不该再把 `latent统一`、`specialist补偿`、`physics adapter`、`deployment shell` 一次性全堆进同一实验。更稳的推进方式是先按下面四步做最小验证，逐层排除收益归属：

| 顺序 | 目标问题 | 最小对照 | 关键记录 | 放行条件 |
|---|---|---|---|---|
| **Step-1 几何层站稳** | human/ground 几何先验是否真能迁到目标载体 | `纯空中锚点` vs `human geometry + 少量空中锚点` | `L1 SR`, `GTG`, 接近位姿误差 | 若 `L1 SR ≥ 85%` 且 GTG 不恶化，放行到 Step-2 |
| **Step-2 共享主干 vs specialist** | 新载体收益到底来自共享 latent，还是来自载体专属头 | `shared+adapter` vs `shared+specialist head` vs `latent retarget` | `L2 SR`, `MCG`, 参数增量, 校准时间 | 若 MCG < 3pp，默认 specialist 不进主线 |
| **Step-3 动力学补偿必要性** | 掉点是跨载体主干问题，还是飞行/扰动动力学问题 | `latent/shared best route` vs `+physics adapter` | `DRB`, 恢复时间, payload 条件下成功率 | 若 DRB 大于预设阈值，优先保留 physics adapter |
| **Step-4 壳层收益拆账** | D04 收益是否已被 D06/D07 壳层吞掉 | 固定共享 planner/latent, 比较 `direct execution` vs `controller shell` | `SDR`, controller regret, recovery gain | 若 SDR > 0.5，论文叙事必须改为“共享主干 + 壳层协同” |

**本轮判断**：D04 当前最有价值的不是继续争论“specialist 要不要上”，而是先用 Step-2 和 Step-3 判断 `specialist head` 与 `physics adapter` 谁才是真正高杠杆补偿层。这样后续即使接 D06/D07，也不会把部署壳层收益误记成 D04 的跨载体共享能力。

### 4.4+++ 两周首轮执行包（R818新增）

为了避免 D04 一直停在“协议越来越完整、但第一组结果还没起跑”，本轮把首轮执行包压成两周：

| 周次 | 目标 | 必做产物 | 放行条件 |
|---|---|---|---|
| **W1** | 跑通 T1 数据与评测骨架 | `T1 任务脚本`、L1/L2 评测器、`GTG/MCG` 统计模板、20条空中锚点基线 | 至少拿到 `SC1 + SC2` 第一版结果 |
| **W2** | 判断动力学补偿是否主导 | `physics adapter` 或 `payload-aware guidance` 最小实现、`DRB/SDR` 统计、弱扰动验证 | 能明确回答“D04 下一阶段主补偿层是谁” |

**W1 具体交付**：
1. 固定主任务为 `T1 静态单物体接近→抓取→抬升10cm`。
2. 只保留三条路线：`shared+adapter` / `shared+specialist head` / `latent retarget`。
3. 统一记录 `L1 SR / L2 SR / GTG / MCG / 参数增量 / 校准时间`。

**W2 具体交付**：
1. 在 W1 最优路线之上叠 `physics adapter` 或 `payload-aware guidance`。
2. 只在弱扰动条件下比较 `DRB / SDR / recovery time`。
3. 若 `DRB` 高、`SDR` 也高，就明确把论文叙事写成 **D04 共享主干 + D06/D07 部署壳层协同**，不再强行把所有收益塞进 D04 本体。

### 4.4++++ 首轮读数判定表（R822新增）

R818 已把路线压成 `SC1→SC4`，但还缺一个能直接决定“下一轮该投谁”的读数门槛。本轮基于本地已读 **Unified Latent Space (2601.15419)**、**Hardware-Agnostic QuadWM (2604.08780)**、**AirVLA (2603.25038)**，进一步把首轮判断钉成下面这张表：

| 读数 | 绿色区 | 黄色区 | 红色区 | 下一步动作 |
|---|---|---|---|---|
| **GTG** | `≤ 10pp` | `10-20pp` | `> 20pp` | 红色时先回修 `human geometry anchor / task geometry state`，停止讨论 specialist |
| **MCG** | `≥ 5pp` | `3-5pp` | `< 3pp` | 绿色保留 `specialist head`，红色直接收缩回 `shared+adapter / latent retarget` |
| **DRB** | `≤ 10pp` | `10-20pp` | `> 20pp` | 红色时优先把资源转给 `physics adapter / payload-aware guidance`，不再追加 paired data |
| **SDR** | `< 0.3` | `0.3-0.5` | `> 0.5` | 红色时论文叙事必须改成 `D04主干 + D06/D07壳层协同` |

**判定原则**：
1. **先看 GTG，再看 MCG**。几何层没站稳时，不允许把 specialist 的小收益写成主线结论。
2. **DRB 优先级高于 paired data 扩量**。一旦 `L2→L3` 掉点过大，先怀疑动力学残差，而不是继续补配对数据。
3. **SDR 是论文叙事开关**。只要壳层收益过高，D04 就不能再单独宣称“共享主干已经解决跨载体主问题”。
4. **Unified Latent Space 默认作为轻量基线锚点**。若 `latent retarget` 在 `GTG` 稳定时已接近 `shared+specialist`，优先保留更轻方案，避免无意义增加 embodiment-specific 参数。

### 4.4+++++ 地面臂→空中臂首轮判线协议（R822推进）

结合本地回扫的 **HEX** 与 **AirVLA**，D04 现在最值得补的不是再加一条方法轴，而是把“共享主干收益”和“载体动力学差异”先分段判清。否则 humanoid/高 DoF 协同收益、以及 aerial payload guidance 的动态补偿收益，很容易被一起写成“跨载体主干有效”。

| 判线阶段 | 固定不变 | 允许变化 | 主要回答的问题 | 对应指标 |
|---|---|---|---|---|
| **P1 几何共享段** | 任务目标、场景、目标物体、`PMI Packet.task_geometry_state` | encoder 类型、是否使用 human geometry anchor | 不同载体是否先共享同一 pre-contact 几何与接近意图 | `PGS`, `L1 SR`, 接近位姿误差 |
| **P2 形态补偿段** | `task_geometry_state` 与 `contact_affordance` 固定 | `shared+adapter / specialist / latent retarget` | 在几何意图已共享时，载体差异更适合由谁来补 | `GTG`, `MCG`, 参数增量, 校准时间 |
| **P3 动力学修补段** | P2 最优路线固定 | `physics adapter / payload-aware guidance / shell` | 掉点是否主要来自 aerial dynamics gap，而非共享主干不足 | `DRB`, payload 条件成功率, recovery time |
| **P4 协同归因段** | planner 与共享 latent 固定 | `controller shell / recovery shell` | 真实收益有多少已经来自 D06/D07 壳层 | `SDR`, controller regret, recovery gain |

**执行约束**：
1. **P1 没站稳，不进入 P2-P4**。否则会把几何表征问题误判成跨载体策略问题。
2. **P2 结论优先于论文口号**。如果 `latent retarget` 已接近 `specialist head`，默认优先保留更轻路线。
3. **P3 只回答 dynamics gap，不再追加 paired data**。这一段优先复用 AirVLA 式 payload-aware guidance 思想。
4. **P4 只做收益归因，不抢主线**。若 `SDR` 高，D04 主文必须老实写成“共享主干 + 部署壳层协同”。

**当前推荐主叙事**：先把 D04 写成“**PMI 几何意图共享 + 轻量形态补偿 + dynamics-aware 外置修补**”三段式，而不是直接宣称单一 unified policy 已经解决地面臂→空中臂全部问题。

## 3.9.7 首轮结果出来后的正文排序规则（R877新增）

结合本轮继续回扫的 **R3D / Unified Latent Space / CeRLP**，以及 QMD 仍主要回流 **D04 README / PMI 框架 / Unified Latent Space** 等既有材料、外部 arXiv 补扫因 **HTTP 429 限流** 未拿到新的稳定增量结果，D04 现在可以把前面冻结到“摘要/标题怎么写”的规则，再向下推进一层：**正文第一版出来后，各章节默认按什么顺序论证，也必须提前写死。** 当前判断不变：本地方向对 `shared geometry → shared latent sufficiency → morphology / dynamics residual` 这条线已接近信息饱和，因此这轮继续优先消化已有锚点而不是为补外查而补外查。

**正文默认排序固定为四步**：
1. **先证明 shared geometry interface 是否成立**
   - 先报 `PGS / IFR / ICS / PMI Packet 完整率`。
   - 只要这些指标不过线，正文第一节只能停在 **shared geometry interface not yet established**，后续任何 latent / specialist / physics adapter 收益都只算诊断信号，不能当方法主贡献。
2. **再判断 shared latent 是否已经足够**
   - 若 shared geometry 已稳，优先报 `GTG` 与 `MCG`。
   - 一旦出现 `GTG` 已低且 `MCG < 3pp`，正文默认写成 **shared geometry + latent sufficiency**，说明 unified latent / retarget 已足以承载大部分跨载体共性，specialist 头自动降级为 supporting evidence。
3. **只有 shared 层解释不完，才讨论 embodiment-aware compensation**
   - 只有当 shared geometry 已稳、shared latent 仍解释不完，且 `MCG` 连续占优、`DRB` 不主导时，正文第三层才允许升格为 **embodiment-aware compensation**，把 morphology token / specialist head 写成主补偿线。
4. **若 `DRB` 高，则直接把剩余问题收成 dynamics bottleneck**
   - 一旦 `DRB` 持续高于 morphology 解释力，正文默认切到 **shared geometry + physics adaptation bottleneck**，主讲 `AirVLA / Hardware-Agnostic QuadWM / inference-time adapter`，而不是继续细抠 specialist 是否还能再抢一点贡献。

**为什么这一步重要**：
- **R3D / CeRLP** 已经足够说明共享几何接口先站稳，才有资格谈后续补偿；
- **Unified Latent Space** 说明 shared latent 本身可能已经吃掉大部分跨载体差异；
- 这意味着 D04 第一版正文不该再从“我们有 geometry、latent、specialist、physics adapter 四条贡献线”起笔，而应按 **shared geometry → shared latent sufficiency → residual compensation** 的顺序逐层收束。

**当前默认 go/no-go 到正文结构的映射**：
- `PGS / IFR / ICS` 不过线 → 第一节止于 **shared geometry interface not yet established**
- `GTG` 已低、`MCG < 3pp` → 第二节默认写 **shared geometry + latent sufficiency**
- `MCG` 持续占优、`DRB` 不主导 → 第三节才允许写 **embodiment-aware compensation**
- `DRB` 高 → 后半正文改写为 **physics adaptation bottleneck**

这一步把 D04 从“主标题怎么冻结”继续推进到“正文怎么排段也被冻结”，后续只要第一轮结果出来，就知道该先证明共享几何、shared latent 已够，还是动力学残差才配占正文主位，不再让 `specialist / latent / physics adapter` 三条线同时挂在主文核心段落上。

### 3.9.5 首轮结果的证据归档表冻结（R882新增）

在 `3.9.4 shared geometry 过线后的解释顺序冻结` 基础上，D04 还需要继续防止一种常见失真：**实验结果有了，但不同类型的 gain 被混写到同一层解释里**。尤其本地近期高频锚点已经很清楚地分成了三类：
- **几何/表征桥接**：`GaussFly / PointBridge / DeFM`
- **domain-factor 抑制**：`CAPO`
- **动力学残差补偿**：`RAFL`

如果不把这些证据先绑定到固定段落，后续很容易再次出现“representation gain、prompt gain、residual gain 同时都想升格主叙事”的老问题。

**本轮新增的证据归档规则**：
1. **GaussFly / PointBridge / DeFM** 只允许作为 `shared geometry / representation bridge` 证据：
   - 支持 `PGS / IFR / ICS / PMI Packet 完整率` 过线；
   - 不允许直接拿去证明 morphology compensation 或 dynamics adaptation 已成立。
2. **CAPO** 只允许作为 `domain-factor suppression` 支线：
   - 只能解释视角、光照、FOV、prompt-conditioned observation cleaning 带来的改进；
   - 不允许在标题、摘要里替代 shared geometry 或 shared latent 成为主叙事。
3. **RAFL** 只允许作为 `dynamics residual / adapter` 证据：
   - 只能支撑 `DRB`、residual field、physics adapter 一类解释；
   - 不允许把 residual gain 误写成 shared representation 已足够。
4. **若首轮结果表现为 mixed gain**，默认归档顺序固定为：
   - 先问 geometry 是否过线；
   - 再问 latent/shared 层是否已足够；
   - 仍解释不完时，才允许把 CAPO 归到 domain cleanup、把 RAFL 归到 dynamics residual。

**冻结后的默认写作动作**：
- `PGS / IFR / ICS / PMI Packet 完整率` 不过线 → 结论只能写 **shared geometry interface not yet established**；
- shared geometry 已稳且 `GTG` 下降、`MCG < 3pp` → 默认收成 **shared geometry + latent sufficiency**；
- `MCG` 连续占优且 `DRB` 不主导 → 才允许升格 **embodiment-aware compensation**；
- `DRB` 高 → 自动改写为 **shared geometry + dynamics adaptation bottleneck**。

**核心意义**：D04 现在不只冻结标题、摘要、正文顺序，也把**不同论文证据该归到哪一层**写死。后续第一版实验一出来，就能立刻把结论归档到 `geometry sufficiency / latent sufficiency / morphology compensation / dynamics bottleneck` 之一，而不是再让表征收益、prompt收益、残差收益混在同一个解释层里。

### 4.4++++++ 实验执行优先级冻结卡（R889新增）

本轮结合 **Master Key (2604.06377)** 与既有 **Unified Latent Space / LAD / AirVLA / R3D** 的位置分工，把 D04 从“正文怎么写”继续推进到 **首轮实验到底先跑哪条最省成本的验证线**。核心思想很简单：如果 shared geometry 已稳，那就先用**最轻 shared-latent 路线**证明共性是否已经足够，只有读数明确表明 latent 不够、且 `DRB` 抬升时，才升级到 physics adapter。

| 条件 | 默认首跑路线 | 允许升级条件 | 冻结项 |
|---|---|---|---|
| `IG0 / SC0` 未过 | `R3D + PMI Packet` 几何修复 | `PGS / IFR / ICS` 过线后再进共享层实验 | 冻结 `specialist / physics adapter / shell` |
| `IG0 / SC0` 已过，且 `DRB` 未抬升 | `shared+adapter` 与 `latent retarget` 二选一先跑 | 只有当 `GTG` 低、但 `MCG` 或 `DRB` 解释不完剩余掉点时才升级 | 冻结 `physics adapter` 的实现扩展 |
| `IG0 / SC0` 已过，`DRB` 明显抬升 | 在最优 shared-latent 路线上叠 `physics adapter / payload-aware guidance` | `DRB` 回落到黄色区以下 | 冻结继续扩 paired data 与 specialist 规模 |
| `IG0 / SC0` 已过，`MCG` 小于 3pp | 默认判定 specialist 不值得先拿预算 | 仅当低成本复现后连续占优才重新开闸 | 冻结 embodiment-specific head 扩参 |

**为什么这样排**：
1. **Master Key** 说明低维能力方向/子空间迁移本身是 plausible 的，所以 D04 首轮更该先验证 *shared latent sufficiency*，而不是条件反射地先堆 embodiment-specific 模块。
2. **AirVLA** 已经告诉我们，对空中载体最容易直接拖垮执行的是 dynamics gap，因此只要 `DRB` 抬升，就应比 specialist 更早拿预算。
3. **R3D / PMI Packet** 仍是所有后续结论的前置门——几何接口不稳时，任何 latent gain 或 dynamics gain 都不能拿来写主结论。

**执行口令化结论**：
- 先几何；
- 再 shared latent；
- 只有 `DRB` 抬头才升级 physics adapter；
- `MCG < 3pp` 时 specialist 默认不加预算。

### 4.5 硬件需求
- 仿真: 1x RTX 3090+ (本地)
- VLM推理: Qwen-VL/InternVL (API或服务器GPU)
- 真机: 龙虾项目平台 + 地面机械臂

## 五、论文写作计划

- **目标会议**: ICRA 2027（主投）/ CoRL 2027（备选）
- **ICRA 2027 会议时间**: 2027年5月24-28日
- **ICRA 2027 投稿截止**: 约2026年9月初（参考ICRA 2026为9月2日截稿）
- **CoRL 2027 投稿截止**: 约2026年7-8月

### 详细写作时间线

| 阶段 | 时间 | 内容 |
|------|------|------|
| **Phase 0 立项确认** | 4月下旬 | ①选定主实验任务（抓取/放置 vs 导航-操作连续任务）；②与主人确认实验资源（GPU服务器、Isaac Sim部署进度）；③确认实验设计细节 |
| **Phase 1 核心实验** | 5月 | 完成Exp-A/B/C系列，验证：①paired data质量 vs quantity；②latent统一 vs morphology先验；③新载体接入三模式对比 |
| **Phase 2 联合实验** | 6月 | 完成Exp-D系列（ours）；空中机械臂真机演示验证 |
| **Phase 3 论文撰写** | 7月-8月初 | 全文草稿：Abstract→Related Work→Method→Experiment→Conclusion；补充附录 |
| **Phase 4 打磨投稿** | 8月中旬 | 论文精修、格式检查、supplementary materials准备 |
| **投稿** | 8月底-9月初 | ICRA 2027投稿（首选）；CoRL 2027备案 |

### 关键里程碑（需主人确认）

- [ ] 4月内：确认主实验任务 + Isaac Sim环境就绪
- [ ] 5月底：Exp-A/B/C结果汇总，判断是否需要调整实验设计
- [ ] 6月底：Exp-D完成 + 真机演示视频
- [ ] 7月底：论文初稿完成
- [ ] 8月底：投稿ICRA 2027

### 5.1 投稿物料清单（R799新增）

> 目标不是“实验做完再想怎么写”，而是现在就把后续论文最贵的图表与证据位锁死，避免 6-7 月只剩结论没有故事线。

| 论文物料 | 对应实验/证据 | 最迟产出时间 | 进入论文的位置 |
|---|---|---|---|
| **Fig.1 方法总览图** | 轴A/B/C/D 四轴框架 + 部署修补层接口 | 5月上旬 | Method / Intro 首页大图 |
| **Fig.2 新载体接入成本曲线** | Full retrain / adapter / latent retarget / specialist / physics adapter 五路对比 | 5月下旬 | Main result |
| **Fig.3 Anchor efficiency 曲线** | `纯目标载体` vs `human几何+少量空中锚点` vs `ground+human+空中锚点` | 6月上旬 | Main result |
| **Fig.4 失败类型可视化** | 几何接近失败 / 动力学失配 / 接触恢复失败 三类 case | 6月中旬 | Analysis / Appendix |
| **Tab.1 统一主结果表** | L1-L4 任务阶梯 + G0-G3 baseline 家族 | 5月下旬 | Main result |
| **Tab.2 消融表** | latent 统一 / morphology token / specialist head / physics adapter / human geometry anchor | 6月中旬 | Ablation |
| **Tab.3 Onboarding cost 表** | 数据量、人工纠偏轮次、GPU 小时、校准时长 | 6月中旬 | Deployment cost |
| **Video 1 真机演示** | 地面臂→空中臂接近/抓取/扰动恢复最小闭环 | 6月底 | Submission supplement |

### 5.2 投稿放行条件（R799新增）

- **主投 ICRA 2027**：至少要有 `Tab.1 + Tab.2 + Fig.2`，并且 L3 弱扰动抓取相对 full retrain 的 gap ≤ 10%。
- **降级 CoRL 2027**：如果真机演示或 L3 结果延后，但接入成本曲线和 anchor efficiency 证据已完整，可主打“cross-embodiment onboarding efficiency”。
- **暂不投稿**：如果当前最强结果仍停在 L1 几何接近或 L2 准静态抓取，就继续收敛方法，不急着进入写作冲刺。

### 5.3 首轮结果后的正文结论冻结卡（R888 新增）

> 来自本轮对 **GaussFly / Unified Latent Space / LAD / AirVLA / R3D** 的本地回扫，以及 QMD 与 arXiv 外查均未带来更贴近主线的新论文增量。D04 现在不只需要“shared latent sufficiency 与 dynamics bottleneck 的默认分流门”，还要把 **正文第一段、摘要主句、证据落位** 继续冻结成一张卡，避免首轮结果出来后又把 representation gain / latent gain / payload residual 混写成同一种增益。

**默认冻结规则**：
1. **只要 `IG0 + SC0` 已过、且 `MCG` 没有持续显著占优**，正文与摘要默认都收成 **shared geometry + latent sufficiency**。这意味着 shared geometry 已足够把跨载体共性立住，而 `Unified Latent Space / LAD` 已足够解释大部分剩余增益，morphology compensation 不再抢主叙事。
2. **只有当 `DRB` 持续升高，且 payload / 飞行稳定性残差对性能掉点的解释力明显大于 `MCG`**，才允许把正文主解释切到 **dynamics adaptation bottleneck**；此时论文主线默认转向 `AirVLA / physics adapter / payload-aware guidance` 一侧，而不再继续放大 shared latent 的边际收益。
3. **证据落位继续写死**：
   - **GaussFly / R3D** 只允许作为 `shared geometry / representation bridge` 证据；
   - **Unified Latent Space / LAD** 只允许在 shared geometry 已稳后解释 `latent sufficiency`；
   - **AirVLA** 只允许在 `DRB` 主导时升格为主证据；
   - 任何单次 specialist 或 prompt-like gain，都不得跨层改写正文主结论。

**核心价值**：让 D04 首轮实验一出来，不止知道“先讲 shared latent 还是讲 dynamics gap”，连 **正文第一段该怎么写、摘要第一句该怎么落、哪些论文证据能落在哪一层** 都直接冻结。这样 D04 才能真正从“多条补偿路线并列”收束到“shared geometry 立住后，默认先看 latent sufficiency，只有 dynamics residual 明确主导时才切主叙事”。

## 六、后续 TODO

- [x] **R759**: 创新点收束为四大轴（轴A/B/C/D）
- [x] **R759**: 新增统一实验对照表（Exp-A1~D3）
- [x] **R763**: 新增 LAD (ICRA 2026) + arXiv:2601.15419 最新扫描；轴C理论支撑获双重验证；对比表更新
- [x] **R777**: 新增 XHugWBC (2602.05791)，确认「物理一致形态随机化 + 语义对齐接口」可作为轴D的训练分布增强方案
- [x] **R799**: 新增投稿物料清单 + 投稿放行条件，把 D04 从“实验路线”继续推进到“论文成稿证据清单”
- [ ] 选定主实验任务（抓取/放置/导航→操作连续任务）
- [ ] 构建最小跨载体实验（地面臂→空中臂简单抓取任务）
- [ ] 完成 Exp-A/B/C 系列，验证 latent 统一 vs morphology 先验的核心假设
- [ ] 新增 anchor-ratio 最小实验：先做 `500条低成本数据 + 50条目标载体锚点` 对照 `纯50条目标载体`，验证 XRZero-G0 式混合策略是否适合空中平台
- [ ] 新增 human-geometry 最小实验：先做 `human几何演示 + 20条空中锚点` 对照 `纯20条空中锚点`，验证 Lidea 式桥接是否能先把 pre-contact 几何学稳
- [ ] 新增 generalist-specialist 最小实验：先做 `shared+adapter` 对照 `shared+specialist head`，验证 embodiment-specific head 是否真能以更低成本补偿载体差异
- [x] **R822**: 新增首轮读数判定表，把 `GTG / MCG / DRB / SDR` 直接绑到 `specialist / physics adapter / shell` 的下一步决策，避免继续只写协议、不下判断
- [x] **R822**: 新增 `地面臂→空中臂首轮判线协议`，把共享几何、形态补偿、动力学修补、壳层归因拆成 P1-P4 四段，避免把 HEX 式高 DoF 协同收益与 AirVLA 式 dynamics gap 修补写成同一类贡献
- [x] **R825**: 把轴A进一步写实成 `PMI Packet` 可验证意图接口，并新增 `L0 几何表征 / PGS / PMI Packet ablation / Gate-G0`，先把“感知几何是否稳定”从跨载体主干收益里拆出来
- [ ] 新增失效归因最小表：首轮必须同时记录 `GTG / MCG / DRB / SDR`，避免把 D06/D07 壳层收益误记成 D04 主干收益
- [ ] 对比 LAC-WM-style latent 与 OPFA-style geometry-aware latent 的实际效果差异
- [ ] 设计 paired demo 自动生成管线（接 D05 数据飞轮）
- [x] 5月前确认 ICRA 2027 DDL 并更新此处（2027年5月24-28日，截稿约9月初）
- [ ] 与主人讨论实验服务器资源安排（Isaac Sim部署 + GPU资源确认）
- [ ] 4月内确认主实验任务（抓取/放置 vs 导航-操作连续任务）
