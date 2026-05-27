# Packet-Centric Aerial VLN: 3D Semantic Frontier Mapping with Deployable Waypoint Interfaces

> 方向：D06 空中视觉语言导航 | 论文类型：方法论文 | 目标会议：ICRA 2027 / IROS 2027 | 状态：🟡 草稿重构中
> 评测平台：AirManip-Bench（见 PAPER1.md）
> 最后更新：2026-05-26
>
> ⚠️ 本文从原 PAPER.md 拆分而来。C3（NtM 架构）降级为应用场景，C4（数据集）已移至 PAPER1.md。
> 本文核心聚焦：**3D VL-Frontier Map（C1）+ Semantic Waypoint Packet 接口（C2）**

---

## Abstract

Aerial Vision-Language Navigation (VLN) requires unmanned aerial vehicles to follow natural-language instructions in open 3D environments, yet existing VLN methods remain poorly matched to aerial deployment because they inherit 2D frontier assumptions, weak dynamics awareness, and brittle planner-controller handoff. We propose a packet-centric aerial VLN framework that couples **3D Semantic Frontier Mapping**, **dynamics-aware frontier selection**, and a **Navigate-then-Manipulate (NtM)** execution interface. The core representation is a **Semantic Waypoint Packet**, which serializes target pose, yaw prior, altitude band, stage tag, runtime budget, and guarded execution prefix into a verifier-compatible object that can be refreshed online. This framing allows us to jointly evaluate semantic planning quality, directional instruction adherence, runtime continuity, and downstream controllability rather than collapsing them into a single navigation score. Compared with prior aerial systems such as OnFly, HTNav, LookasideVLN, and LiveVLN, our method is designed to preserve packet validity through the full `planner → verifier → controller` chain while retaining the ability to hand off from search-time navigation to manipulation-time local interaction. We further formalize packet-facing metrics, including verifier pass rate, packet staleness, packet handoff failure, context retention, and progress-trace consistency, to expose failure modes that standard success-rate reporting obscures. The resulting framework positions aerial VLN as a deployable interface problem rather than only a waypoint prediction problem.

---

## 1. Introduction

### 1.1 Problem Statement

Vision-Language Navigation (VLN) enables robots to navigate to language-described targets in unknown environments, a core capability for embodied intelligence. While ground VLN has seen substantial progress—VLFM [REF: ], NaVILA [REF: ], ApexNav [REF: ], SG-Nav [REF: ]—**aerial VLN remains severely underexplored**. Existing methods assume 2D planar motion, low speed, and stable viewpoints, fundamentally incompatible with the 6-DoF motion space, high-speed flight, dramatic pitch-angle changes, and dynamics constraints of unmanned aerial vehicles (UAVs).

The gap is not merely one of scale. Aerial platforms introduce three qualitatively distinct challenges absent from ground VLN: (1) **3D spatial exploration**: targets may be above, below, or at arbitrary elevations, requiring volumetric frontier representations rather than 2D maps; (2) **dynamics-aware planning**: energy budgets, velocity limits, and attitude constraints must be incorporated into exploration cost functions to avoid infeasible paths; and (3) **navigation-to-manipulation continuity**: aerial VLN naturally extends to Navigate-then-Manipulate (NtM) tasks where the robot must transition from search to precise end-effector operations upon target localization.

Recent surveys [REF: 2604.13654, 2604.07705] confirm that 3D spatial representation and dynamics-aware planning are the two core unsolved problems in aerial VLN. This paper directly addresses both.

### 1.2 Contributions

This paper makes the following contributions:

1. **C1: Aerial VL-Frontier Map (AVLFM)**: We extend 2D vision-language frontier maps to 3D volumetric representations, incorporating VLM semantic relevance scoring to guide exploration in the full 3D aerial workspace, including vertical dimension exploration and viewpoint-change robustness.

2. **C2: Semantic Waypoint Packet Interface**: We formalize the planner→verifier→controller handoff as a structured **Semantic Waypoint Packet** — serializing target pose, yaw prior, altitude band, stage tag, runtime budget, and guarded execution prefix into a verifier-compatible object that can be refreshed online. This reframes aerial VLN from waypoint prediction toward a deployable interface problem.

> **已移出本文的贡献：**
> - ~~C3: Navigate-then-Manipulate Architecture~~ → 降级为应用场景（Section 5），完整 NtM 链路评测见 PAPER1（AirManip-Bench）
> - ~~C4: Aerial VLN Benchmark~~ → 已移至 PAPER1（AirManip-Bench），本文使用其 benchmark 作为评测平台

---

## 2. Related Work

### 2.1 Ground Vision-Language Navigation

Ground VLN has established strong baselines for language-guided exploration. VLFM [REF: ] uses VLM semantic relevance to guide 2D frontier exploration, demonstrating that language-conditioned frontier selection significantly outperforms geometric-only exploration. NaVILA [REF: ] adopts a hierarchical VLA design with high-level VLM reasoning and low-level action execution. AgentVLN (arXiv:2603.17670) [REF: 2603.17670] proposes a VLM-as-Brain paradigm that decouples high-level semantic reasoning from perception and planning via a plug-and-play skill library, achieving SOTA on R2R-CE with only 3B parameters and enabling real-time edge deployment on quadruped robots—a modular paradigm highly relevant to aerial VLN module design. ApexNav [REF: ] introduces adaptive semantic-geometric exploration balancing exploration and exploitation. SG-Nav [REF: ] uses scene graph representations for structured navigation reasoning. DRIVE-Nav [REF: ] enhances spatial reasoning through directional inference. These methods collectively demonstrate the value of semantic frontier maps but are fundamentally limited to 2D planar motion and cannot handle aerial dynamics.

### 2.2 Aerial Navigation Systems

OnFly [REF: ] introduces a dual-agent UAV navigation system with decoupled perception and control frequencies, the closest existing work to aerial VLN. OpenFly [REF: 2502.18041] provides a comprehensive aerial VLN platform combining UE/GTA V/Google Earth/3DGS rendering sources, automatic trajectory and instruction generation, and a keyframe-aware VLA model, serving as our primary data infrastructure reference. AirNav [REF: 2601.03707] presents the first real-world urban aerial VLN benchmark with AirVLN-R1 (SFT + RLFT training recipe), directly addressing the real-data evaluation gap. APEX [REF: 2602.00551] proposes Dynamic Spatio-Semantic Mapping with RL-based action decisions and target-guided exploration, providing an interpretable modular explorer suitable as an engineering reference for our GoalSearch component. Fly0 [REF: 2602.15875] explicitly decouples semantic grounding from geometric trajectory planning in three stages, demonstrating zero-shot, low-latency navigation with geometric robustness after visual loss. FineCog-Nav [REF: 2604.16298] introduces fine-grained cognitive modularization for zero-shot UAV VLN, decomposing language processing, perception, attention, memory, imagination, reasoning, and decision into role-specific modules with the AerialVLN-Fine benchmark for sentence-level instruction-trajectory alignment. SpatialFly [REF: 2603.21046] represents a complementary geometry-first line: rather than constructing an explicit 3D frontier map, it injects geometric priors into 2D semantic tokens and aligns them with 3D structural cues, showing that representation-level geometry alignment can improve unseen-scene path alignment and motion smoothness even without full volumetric reconstruction. AeroVerse [REF: 2408.15511] complements these task-specific systems by providing a full-stack UAV-agent benchmark suite spanning simulation, pre-training, finetuning, and evaluation; for D06, its main relevance is not a packet-level method contribution but a systems-level reminder that aerial VLN claims should eventually be judged inside a broader aerial embodied stack including navigation, reasoning, and motion-decision evaluation.
KIO-planner [REF: 2605.19703] adds a useful low-level contrast point: its attention-guided single-stage motion planner with dual mapping shows that strong gains in local safety, narrow-space traversability, and controller-side latency can be obtained without solving language grounding or packet-level semantics. For D06, it should therefore be treated as a local execution-shell family that can justify stronger **geometric executability** and **near-field safety compliance**, but not by itself stronger direction-aware packet preservation or manipulation-ready handoff accountability.
FlyMirage [REF: 2605.19600] contributes from the data side rather than the packet side: by combining LLM-authored scene layouts, generative world models, 3DGS instantiation, and dynamics-feasible trajectory synthesis, it suggests that aerial VLN systems may soon benefit from scalable long-horizon data generation without manually flying or annotating every scenario. In our framing, FlyMirage can justify stronger **data coverage**, **trajectory-diversity support**, and **pretraining prior quality**, but it does not by itself establish better packet refresh honesty, controller-consumption stability, or NtM handoff preservation.

### 2.3 Aerial Manipulation

π-Make-It-Fly [REF: ] demonstrates that visual representations transfer to aerial platforms but control dynamics do not, requiring payload-aware guidance at inference time. Unified Aerial Grasping [REF: ] provides an end-to-end language-conditioned aerial grasping system with active exploration and 6-DoF grasping. AeroPlace-Flow [REF: ] addresses language-guided aerial object placement using Visual Foresight and Object Flow. These manipulation works assume known approximate target locations, lacking a systematic navigation front-end—the gap our NtM architecture addresses.

### 2.4 Direction-Aware Spatial Language Planning and Live Runtime Execution

LookasideVLN [REF: 2604.17190] highlights a previously under-modeled source of aerial VLN gain: explicit directional cues in language instructions. Instead of relying only on landmark mentions or deeper lookahead search, it introduces an Egocentric Lookaside Graph and a Spatial Landmark Knowledge Base to encode landmark-direction relations for multimodal path planning. Its strongest value for our setting is not a replacement of frontier exploration, but a lightweight planner frontend that can improve instruction adherence, waypoint proposal quality, and heading selection before the packet-verifier-controller chain. This suggests that direction-aware language parsing should be treated as an augmenting module for waypoint proposal quality, not as a substitute for 3D semantic frontier mapping or dynamics-aware execution.

OnFly [REF: 2603.10682] further strengthens the systems side of this argument from an aerial deployment perspective. Its onboard dual-agent design, hybrid keyframe/latest-frame memory, and semantic-geometric verification pipeline show that aerial VLN performance depends not only on semantic planning quality, but also on whether the runtime can maintain safe progress monitoring under onboard latency constraints. In our framing, this means that packet quality should be judged together with *verifiability* and *runtime continuity*, rather than by semantic relevance alone.

LiveVLN [REF: 2604.19536] further pushes the field toward temporally grounded, online navigation by exposing the deployment inefficiency of stop-and-go execution. It proposes a training-free runtime that splits an action sequence into an executed prefix, a guard buffer, and a revisable tail, enabling guarded handoff and real-time adaptation while preserving execution continuity. For our setting, its main value is not replacing aerial exploration itself, but motivating a **live packet refresh** mechanism that keeps frontier proposals updateable under streaming observations without forcing full replanning at every step. Together, these works motivate us to evaluate planner frontend quality not only by semantic relevance, but also by direction-conditioned adherence, verifier compatibility, and runtime continuity under packetized execution.

### 2.5 Packet-Centric Framing and the Limits of Existing Aerial VLN Pipelines

A common limitation across current aerial VLN systems is that planning quality, execution continuity, and downstream controllability are still entangled. Landmark-centric methods often produce semantically plausible targets without explicitly representing directional priors. Runtime-oriented systems improve continuity, but usually treat the planner output as a transient action list rather than a reusable interface object. Modular onboard systems add semantic-geometric verification, yet the intermediate representation passed from planner to controller is still weakly formalized. As a result, it remains difficult to diagnose whether failure comes from poor waypoint semantics, stale action handoff, verifier mismatch, or low-level control drift.

This motivates our packet-centric formulation: instead of asking only whether the planner predicts the right next move, we ask whether it emits a **semantic waypoint packet** that is direction-aware, budget-bounded, verifier-compatible, and refreshable online. Under this framing, the key unit of evaluation is not just task success, but whether the packet can survive the full `planner → verifier → controller` chain with low staleness, low heading drift, and low handoff failure. This reframes aerial VLN from pure navigation prediction toward a deployment-ready interface problem.

### 2.6 Baseline Families and Attribution-Consistent Reading Rules

To avoid inflating the contribution of a packet-centric aerial VLN system, we organize recent baselines into four *attribution families* and constrain what each family is allowed to explain. This is not merely a writing convenience; it is a deployment-facing accounting rule. If a baseline improves one failure surface but does not alter the others, its gain should stay attached to that surface instead of being retroactively merged into a larger "better aerial planner" narrative.

The first family is **clause- and direction-preserving planner frontends**, represented by FineCog-Nav [REF: 2604.16298] and LookasideVLN [REF: 2604.17190]. These methods are most informative when the dominant question is whether language-side structure is preserved before execution: clause-level intent, egocentric directional relation, memory-backed landmark anchoring, and sentence-to-waypoint consistency. In our paper, gains from this family are therefore only allowed to explain improvements in *direction-conditioned instruction adherence*, *pre-verifier semantic mismatch reduction*, and *packet-facing clause retention*. They are not sufficient evidence for runtime survivability, controller compatibility, or cross-stage recovery on their own.

The second family is **runtime-survivability and live-execution systems**, represented by OnFly [REF: 2603.10682] and LiveVLN [REF: 2604.19536]. Their primary value lies in maintaining executable continuity under latency, monitoring, and refresh constraints. In our attribution rules, gains from this family are allowed to explain improvements in *verifier pass rate under onboard latency*, *packet staleness reduction*, *guarded execution continuity*, and *handoff survivability*. They should not be over-read as evidence that the underlying semantic planner is intrinsically better at clause interpretation or frontier ranking.

The third family is **representation-level geometry alignment**, represented by SpatialFly [REF: 2603.21046] and related geometry-guided aerial grounding methods. These methods matter when the dominant failure comes from 2D-3D mismatch, viewpoint distortion, or weak structural alignment between semantic tokens and spatial geometry. In our framework, gains from this family are only allowed to explain *representation-level grounding robustness*, *cross-view alignment stability*, and *geometry-aware path smoothness*. They are not sufficient evidence that the system has solved packet serialization, verifier compatibility, or long-horizon recovery.

The fourth family is **recoverability- and replanning-aware systems**, represented by OpenVLN [REF: 2511.06182] and other value-guided aerial replanning pipelines. Their value is that they ask whether a locally executable step preserves a future correction corridor under uncertainty. In our reading rules, gains from this family are only allowed to explain *recovery-corridor preservation*, *replanning-value retention*, and *long-horizon correction friendliness*. They should not be over-read as proof of better clause parsing, lower-latency execution, or cleaner packet handoff.

### 2.7 WildOS-Style Open-Vocabulary Outdoor Search as a Negative-Control Frontier Family

WildOS [REF: 2602.19308] is not a canonical aerial VLN system, yet it is highly informative as a **negative-control frontier family** for our setting because it cleanly separates open-vocabulary target search from packetized language-conditioned handoff. Its core pipeline combines geometry-safe exploration, semantic boundary-node scoring, traversability prediction, and particle-filter-based long-range target belief updates in complex outdoor scenes. This makes it a strong reference for *open-vocabulary outdoor search competence* without automatically granting clause-level instruction following, direction-conditioned packet serialization, or NtM handoff accountability.

For D06, the main value of WildOS is therefore diagnostic rather than substitutive. If a future D06 variant improves outdoor target finding under weak language structure, that gain may still be fully explainable by a WildOS-like frontier-search family rather than by a better aerial VLN packet interface. In our attribution discipline, this family is only allowed to explain improvements in **open-vocabulary target recall**, **boundary-node exploration efficiency**, and **long-range semantic search stability**. It should not be over-read as evidence of stronger consume-time packet preservation, direction-aware clause adherence, or manipulation-ready handoff value.

This distinction matters because outdoor success in aerial embodied tasks can look deceptively similar across two very different routes: one route finds the right region through geometry-plus-semantic search, while the other preserves a language-grounded packet through the full `planner → verifier → controller → handoff` chain. Our paper should explicitly prevent these routes from being collapsed into the same headline. WildOS therefore serves as a useful matched negative-control family for any D06 result that appears strong in outdoor search but remains under-closed at consume time.

### 2.8 Negative-Control Route Discipline for Outdoor Search Transfer

To keep D06 honest when borrowing evidence from outdoor open-vocabulary search systems, we require an explicit **route-discipline check** before any transfer claim is promoted. A WildOS-style gain may enter our paper only through the route `frontier search competence → region discovery stability → target-zone narrowing`; it is not allowed to jump directly into `direction-aware packet preservation`, `consume-time controller compatibility`, or `NtM handoff readiness`. In other words, outdoor search evidence may justify a stronger *where-to-look-next* story, but not by itself a stronger *what-packet survived until use time* story.

Operationally, we treat WildOS-like systems as matched negative controls whenever a D06 ablation improves outdoor success while remaining weakly supervised at clause level or under-logged at controller-consumption time. If the dominant gain disappears after conditioning on boundary-window packet fields, then the result should stay frozen as **search-route improvement only**. If the gain survives and additionally preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`, it may be promoted to packet-contract language; only rows that also preserve `A^{shell}` are allowed to support manipulation-ready handoff claims. This discipline prevents us from over-crediting semantic search improvements as if they had already solved late-stage packet accountability.

### 2.9 Active-Elicitation Support improves Planner-Side Disambiguation but does not by itself Preserve Consume-Time Packet Honesty

MINT [REF: 2603.07824] exposes another route that can look deceptively strong in aerial VLN: **interactive or active elicitation before execution**. By querying missing constraints or refining task intent before committing to a plan, such systems may substantially improve planner-side ambiguity resolution, region narrowing, and waypoint proposal cleanliness. For D06, this is useful because active elicitation can reduce pre-verifier semantic mismatch and make `Q^{reason}_{route}` or `Q^{lang}_{narrow}` look much stronger. But that gain still lives primarily on the route `task disambiguation → proposal cleanup → better narrowing / better planner-side packet proposal`; it does not by itself prove that the emitted packet survives refresh episodes or remains honest at controller consumption.

We therefore treat MINT-style methods as an **active-elicitation support family**. Gains from this family are allowed to explain improvements in ambiguity resolution, query-efficient intent completion, and planner-side proposal quality, but they are not allowed to promote a row into packet-contract or NtM language unless the same row still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` after elicitation has already been subtracted. Only rows that additionally preserve `A^{shell}` may support manipulation-ready handoff claims. This matters because a system that asks better questions may still produce a packet that decays under streaming observations or loses shell validity before use time.

### 2.10 Search-Side Complementarity improves Narrowing Quality but does not by itself Close Packet Accountability

Recent local anchors make the search-side structure of D06 sharper. LMPath [REF: 2605.13782] improves **language-mediated region narrowing** by converting target-environment relations into aerial exploration priors before the target is directly seen. StereoNav [REF: 2605.13328] improves **geometry-grounded target anchoring** by using stereo cues and target-location priors to stabilize grounding once the target becomes partially observable. WildOS [REF: 2602.19308] strengthens **open-vocabulary outdoor search competence** through geometry-safe exploration and boundary-node semantic search. AgentVLN [REF: 2603.17670] adds a reasoning-side complement: modular VLM-as-Brain routing can improve clause decomposition, skill selection, and pre-verifier waypoint proposal quality without forcing a monolithic end-to-end controller. Taken together, these systems show that aerial navigation can become much stronger long before a packet is ever consumed by the low-level controller.

For D06, this means search-side gains should be treated as **complementary narrowing families** rather than implicit packet wins. LMPath-like gains are allowed to explain earlier `Q^{lang}_{narrow}` improvements and lower wasted coverage. StereoNav-like gains are allowed to explain stronger `Q^{geo}_{narrow}` and lower cross-view anchor drift. WildOS-like gains are allowed to explain region-discovery stability and open-vocabulary target recall. AgentVLN-like gains are allowed to explain stronger `Q^{reason}_{route}` and cleaner pre-verifier waypoint proposals. But none of these routes, alone or combined, is sufficient evidence that the packet preserves `A^{dir}`, `A^{ctx}`, `A^{guard}`, or `A^{shell}` through repeated refresh episodes and delayed controller consumption. In other words, better search and planner-side reasoning are prerequisites for D06, not yet proofs of packet accountability.

### 2.11 Route-Closure after Search-Side Complementarity

We therefore formalize a stronger route-closure discipline for search-side complementarity. A row that improves because LMPath narrows the search region better, StereoNav grounds the target more stably, WildOS recovers the correct outdoor semantic zone more reliably, or AgentVLN routes reasoning and skills more cleanly may only be promoted along the route `search-route win → refresh-stable packet support → consume-time packet preservation → manipulation-ready shell preservation`. If the evidence closes only on the first hop, the row freezes as **search-prior support** or **reasoning-route support**. If it survives refresh but loses packet fields before `w^{\dagger}_{consume}`, it freezes as **refresh-stable packet support**. Only rows preserving `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` may be promoted to packet-contract language, and only rows that additionally preserve `A^{shell}` may support NtM handoff claims.

This rule is especially important for D06 because recent local evidence now gives us four different search-side explanations with very different semantics: language prior quality, geometry-grounded anchoring quality, open-vocabulary outdoor search quality, and modular reasoning-route quality. Without an explicit route-closure protocol, those gains are too easy to merge into a single inflated story about packet survival. Our paper should instead force them to remain separate until delayed consumption evidence actually closes the loop.

### 2.12 Search-Side Local-Execution Shells are Necessary but Not Sufficient for Packet Claims

Recent low-level UAV planning work such as KIO-planner [REF: 2605.19703] shows that a strong **local execution shell** can materially improve geometric executability, minimum obstacle clearance, and inference latency in cluttered or narrow environments. This matters for D06 because any aerial VLN packet eventually has to pass through a local controller-facing execution layer, and poor near-field safety can destroy even a semantically correct packet. However, KIO-style gains still live primarily on the route `better local depth attention / safety shielding → stronger short-horizon geometric feasibility`, not on the route `direction-aware clause preservation → refresh-stable context retention → consume-time packet survival`.

We therefore treat local execution-shell methods as a separate support family. Their gains are allowed to explain improvements in **Geometric Executability Gate** pass rate, minimum-clearance robustness, and near-field controller safety under matched latency. But they are not allowed to justify stronger `Q^{lang}_{narrow}`, `Q^{reason}_{route}`, or packet-contract promotion unless the same row also preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`; `A^{shell}` remains the final gate for NtM handoff claims. This distinction is useful because a D06 variant may win by attaching a much better local shell to an otherwise unchanged planner, and that should be reported honestly as **execution-shell support** rather than as evidence that the packet interface itself has already become stronger.

### 2.13 Local Execution-Shell Support and Data-Scaling Support require an Explicit Experiment-Side Freeze

Recent local anchors sharpen two additional non-packet explanations that D06 must keep separate in both writing and experiments. **KIO-planner** [REF: 2605.19703] shows that a strong local execution shell can materially improve near-field geometric executability, obstacle clearance, and short-horizon safety under tight latency budgets. **FlyMirage** [REF: 2605.19600] shows that large gains may also come from upstream synthetic-data scaling, where generative world models improve data coverage, trajectory diversity, and pretraining priors before any consume-time packet field is ever tested. **LMPath** [REF: 2605.13782] and **StereoNav** [REF: 2605.13328] make the planner-side side of this story even sharper: language-mediated region priors and stereo-grounded target-location priors can both improve early narrowing and reduce wasted search effort before packet survival is ever stress-tested. All four routes are valuable for D06, but none should be allowed to silently inflate packet claims.

We therefore freeze them as distinct support families with different ceilings. KIO-style methods are allowed to explain stronger **geometric executability**, **near-field safety compliance**, and **controller-side local robustness**. FlyMirage-style methods are allowed to explain stronger **data coverage**, **trajectory-diversity support**, and **pretraining-prior quality**. LMPath-style methods are allowed to explain stronger **language-mediated search narrowing**, while StereoNav-style methods are allowed to explain stronger **geometry-grounded target anchoring** and lower cross-view drift. But none of these routes, alone or combined, is allowed to justify stronger consume-time packet preservation unless the same row still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`; `A^{shell}` remains the final gate for NtM handoff claims. In D06, all four families should therefore enter the evidential ladder only as subtraction routes: if a row's gain is exhausted by a better execution shell, better synthetic-data support, better language-side narrowing, or better geometry-side anchoring, it must freeze below packet-contract promotion.

### 2.14 Data-Scaling Support and Route-Closure for Synthetic Aerial Corpora

FlyMirage [REF: 2605.19600] strengthens an increasingly relevant upstream route for D06: **data scaling via generative world models**. By automatically synthesizing diverse UAV flight scenes, semantics-aligned trajectories, and dynamics-feasible long-horizon paths, it can materially improve data coverage and reduce the manual bottleneck of collecting aerial VLN supervision in the wild. For our paper, this matters because richer synthetic corpora may improve earlier `w^+`, lower planner-side search entropy, and stabilize proposal quality before deployment. In parallel, LMPath [REF: 2605.13782] and StereoNav [REF: 2605.13328] show that better planner-side priors can also shift `w^+` earlier: the former by turning language-mediated environment relations into search-region priors, the latter by using stereo-consistent target-location priors to stabilize geometric grounding after first target exposure.

However, FlyMirage-style gains still live primarily on the route `better data coverage → stronger pretraining prior → cleaner planner-side proposal`, LMPath-style gains on the route `better language prior → earlier region narrowing → lower wasted coverage`, and StereoNav-style gains on the route `better geometry prior → lower anchor drift → stabler target attachment`. None of these routes by themselves establishes stronger `A^{dir}`, `A^{ctx}`, `A^{guard}`, or `A^{shell}` at delayed controller consumption. We therefore treat synthetic-data scaling, language-prior narrowing, and geometry-prior anchoring as separate **pre-consumption support families**: their gains are allowed to explain stronger coverage, more diverse long-range priors, lower data sparsity, earlier semantic narrowing, and stronger cross-view anchoring, but they are not allowed to promote a row into packet-contract or NtM language unless the same row still preserves the consume-time packet fields after refresh episodes. This keeps D06 from confusing "trained on better data," "searched in a better region," or "anchored the target more stably" with "proved a stronger deployable packet interface."

### 2.15 Planner-Side Self-Awareness and Semantic-Geometric Decoupling as Strong but Bounded Mid-Level Baselines

AwareVLN [REF: 2605.22816] and Fly0 [REF: 2602.15875] sharpen a middle regime that sits between planner-side search priors and full packet-contract preservation. AwareVLN improves long-horizon navigation through **self-awareness and progress-structured reasoning**: it explicitly tracks agent state, task progress, and spatial relations, making the planner better at deciding *which stage it is in* and *whether the current evidence is sufficient to advance*. Fly0 instead decouples **semantic grounding** from **geometric planning**, showing that a UAV can obtain strong zero-shot navigation gains by first grounding a language-described target and then delegating motion realization to a geometry-driven planner. Both routes are highly relevant to D06 because they directly compete with our packet-centric framing at the level of mid-stage explanation: AwareVLN can explain better stage discipline and progress-consistent replanning, while Fly0 can explain cleaner semantic-to-geometric decomposition without requiring an explicit reusable packet.

For D06, these baselines should be treated as strong but bounded **mid-level support families**. AwareVLN-like gains are allowed to explain stronger planner-side stage awareness, progress-consistent recovery, and lower wrong-escalation rates at the `search → approach` boundary. Fly0-like gains are allowed to explain stronger semantic-geometric role separation, lower controller oscillation, and better zero-shot execution stability when semantic grounding is already correct. But neither route, by itself, proves that the emitted interface remains honest through repeated packet refresh and delayed controller consumption. In our route-closure discipline, AwareVLN-family gains freeze at **progress-aware planner support** unless they still preserve `A^{ctx}` and `A^{guard}` through `w^{\dagger}_{consume}`; Fly0-family gains freeze at **semantic-geometric decoupling support** unless they additionally preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` after geometric execution has already been matched. Only rows that also preserve `A^{shell}` are allowed to support full NtM handoff claims.

### 2.16 Planner-Side Active Perception, World Priors, and Semantic Completion are Strong Upstream Supports but not Consume-Time Packet Evidence

Recent local anchors make a new boundary unavoidable for D06: a row can improve substantially **before packet consumption** simply because the planner knows when to look again, inherits a stronger world prior, or fills unknown semantic regions more plausibly. **LMPath** [REF: 2605.13782], **StereoNav** [REF: 2605.13328], **WildOS** [REF: 2602.19308], and **AgentVLN** [REF: 2603.17670] already imply a planner-side active-perception route, where one more sensing action, a short verification orbit, or a tiny viewpoint shift can sharply reduce ambiguity before commitment. **SAGE** [REF: 2605.10118] adds a broader upstream route by supplying a physics-grounded semantic sandbox that improves open-world transfer priors, while **PLMD** [REF: 2605.05960] shows that language-conditioned semantic completion can sharpen goal maps even when the target region is still partially unobserved. All of these routes are highly useful, but none by itself proves that the emitted packet remains honest at delayed controller consumption.

For D06, we therefore freeze them as **planner-side active-perception support**, **world-prior transfer support**, and **semantic-completion support** families. Active-perception gains are allowed to explain lower uncertainty before packet emission, cheaper one-more-look disambiguation, and reduced pre-commit target entropy. World-prior gains are allowed to explain stronger open-world transfer, lower early search entropy, and more robust planning in previously unseen semantics. Semantic-completion gains are allowed to explain better unknown-region filling, sharper goal maps, and lower wasted exploration in partially observed scenes. But none of these routes may by itself promote a row into packet-contract or NtM language unless the same row still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` after those upstream supports have already been subtracted; `A^{shell}` remains the final gate for handoff claims.

### 2.17 Route-Closure after Active Perception, World Priors, and Semantic Completion

We therefore extend the D06 route-closure discipline with three additional subtraction checkpoints. A row that improves because the planner takes one more informative look, because a stronger world prior already regularizes early search, or because semantic completion fills useful unseen structure may only be promoted along the route `upstream support win → refresh-stable packet support → consume-time packet preservation → manipulation-ready shell preservation`. If the evidence closes only on the first hop, the row freezes respectively as **active-perception support**, **world-prior transfer support**, or **semantic-completion support**. If it survives refresh but loses packet fields before `w^{\dagger}_{consume}`, it may rise only to **refresh-stable packet support**.

Operationally, this means D06 should treat `Q^{unc}_{plan}`, `Q^{world}_{prior}`, and `Q^{comp}_{sem}` exactly like earlier reasoning- and search-family diagnostics: they are legitimate explanatory wins, but only at their own ceiling. A planner that simply knows when to spend one more sensing action is not yet a stronger packet interface. A model that searches better because an upstream sandbox taught stronger semantic priors is not yet a stronger packet interface. A route that becomes cleaner because unknown semantics were completed more helpfully is not yet a stronger packet interface. Only residual evidence that survives these matched explanations and still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through delayed consumption may support packet-contract language; only rows that additionally preserve `A^{shell}` may support NtM handoff claims.

### 2.18 Limitations of Existing Work

Existing aerial navigation and VLN approaches share critical gaps:
(1) No existing method provides a complete aerial VLN framework with 3D semantic frontier exploration.
(2) Ground VLN methods cannot transfer to aerial platforms due to 2D map assumptions and absence of dynamics modeling.
(3) Navigation and manipulation are treated as separate problems; no unified architecture handles the full search-to-grasp pipeline.
(4) Dynamics constraints are either ignored or handled as post-hoc filters rather than integrated into the exploration cost function.
(5) Existing aerial navigation benchmarks lack dynamics-aware metrics and 3D spatial reasoning evaluation.
(6) Directional cues and egocentric spatial relations in natural language remain under-modeled.
(7) Temporally updated online observations are still weakly integrated into planner-verifier-controller pipelines.
(8) The planner output is rarely formalized as a reusable packet-level interface.
(9) Existing responsive aerial systems improve latency but still provide limited evidence on whether packetized interfaces remain stable under downstream controller consumption and cross-stage handoff.
(10) Current aerial VLN papers also rarely align **experiment logs, main tables, and result-paragraph promotion rules** to the same contract.
(11) Closely related systems still lack an explicit **delayed-consumption violation taxonomy** that separates directional drift, context-anchor loss, shell collapse, and guarded-prefix invalidation, making late-window failures hard to attribute cleanly.
(12) Even when methods report stronger online continuity, they seldom specify a **minimal route-closure upgrade protocol** for deciding when a row may be promoted from planner-time gain to consume-time packet-contract or NtM-handoff language.
(13) Open-vocabulary outdoor search systems may substantially improve target discovery and long-range semantic exploration, but they still do not by themselves establish direction-aware clause following, packetized controller-consumption stability, or manipulation-ready handoff preservation.
(14) Existing aerial VLN papers also provide limited evidence on whether packets improved by outdoor search remain valid across repeated **live refresh episodes** under streaming observations before actual controller consumption.
(15) Semantic map completion and abstract physics-grounded navigation pretraining can improve upstream search priors, but current work still provides little guidance on when those gains remain only *search-prior improvements* versus when they genuinely survive into consume-time packet accountability.
(16) Cross-domain grounding methods and language-mediated search priors may each improve early target-zone narrowing, but current aerial VLN work still offers weak evidence on how these gains interact with refresh stability, controller-consumption integrity, and late-stage packet preservation.
(17) Minimalist end-to-end aerial VLA systems can already provide strong oracle-free continuous control, so packet-centric methods must still prove added value beyond **latent execution sufficiency** under matched onboard budgets.
(18) Existing papers rarely provide an explicit **route-closure discipline** separating planner-time reasoning, compact end-to-end execution, runtime continuity, and full consume-time packet preservation, which makes late-window claims too easy to over-promote.
(19) Modular VLM-as-Brain reasoning systems can significantly improve search-time instruction decomposition and edge-side skill routing, but current aerial VLN work still offers little evidence on when those gains survive refresh episodes and controller consumption strongly enough to justify packet-contract or NtM-handoff promotion.
(20) Full-stack aerial embodied benchmarks can improve upstream data and evaluation coverage, but they still do not by themselves explain whether a navigation packet remains semantically stable, refresh-consistent, and controller-consumable at the late handoff boundary.
(21) Current aerial VLN papers still under-specify how broader benchmark coverage should map to actual late-window evidence routes, leaving room to confuse **evaluation-scope expansion** with **consume-time packet preservation**.
(22) Active-elicitation or interactive clarification systems may greatly improve planner-side ambiguity resolution, but current aerial VLN work still provides weak evidence on whether those gains survive packet refresh and delayed controller consumption strongly enough to justify packet-contract promotion.
(23) Search-side complementarity is becoming richer—language-mediated priors, geometry-grounded anchoring, modular reasoning-route quality, and open-vocabulary outdoor search can all improve early narrowing—but current aerial VLN work still offers weak evidence on when these gains remain only *search-route improvements* versus when they genuinely survive refresh episodes and delayed controller consumption as packet-contract evidence.
(24) Existing aerial VLN papers still rarely provide a single route-closure protocol that jointly handles **language-prior narrowing, geometry-grounded narrowing, reasoning-route support, outdoor-search negative controls, and late consume-time packet survival**, making it too easy to over-promote search wins into manipulation-ready handoff claims.
(25) Strong local execution-shell planners can markedly improve near-field safety and geometric executability, but current aerial VLN work still provides weak evidence on when those gains remain only *controller-shell improvements* versus when they genuinely strengthen packet survival and late handoff accountability.
(26) Synthetic aerial data pipelines can dramatically improve upstream diversity and long-horizon supervision, but current aerial VLN work still provides weak evidence on when those gains remain only *pretraining-support improvements* versus when they genuinely survive refresh episodes and delayed controller consumption as packet-contract evidence.
(27) Self-aware progress-reasoning systems can substantially reduce stage confusion and wrong escalation during long-horizon navigation, but current aerial VLN work still offers weak evidence on when these gains survive repeated refresh episodes strongly enough to justify consume-time packet-contract promotion.
(28) Semantic-geometric decoupling systems can markedly improve zero-shot navigation stability and reduce controller oscillation, but current aerial VLN work still provides weak guidance on when those gains remain only *decoupled execution support* versus when they genuinely preserve packet fields through delayed controller consumption and NtM handoff.

---

## 3. Method

### 3.1 System Overview

Our system processes a natural language instruction through a three-stage pipeline:

```
Language Instruction
        │
   ┌────┴────┐
   │ VLM Goal │
   │  Parser  │
   └────┬────┘
        │
   ┌────┴──────────┐
   │ 3D VL-Frontier │
   │  Map + Dynamics│
   │  Cost Function │
   └────┬──────────┘
        │
   ┌────┴────┐
   │  Flight  │
   │ Controller│
   └────┬────┘
        │
   ┌────┴────┐
   │  NtM    │
   │  Module │
   └─────────┘
```

### 3.2 Aerial VL-Frontier Map (C1)

We represent the environment as a 3D occupancy voxel grid updated from UAV RGB-D observations. Frontier voxels are defined as free voxels adjacent to unknown voxels in 3D space, capturing exploration opportunities in the full volumetric workspace including vertical dimensions. Rather than directly selecting raw frontier cells, we cluster frontier voxels into candidate semantic viewpoints and attach a lightweight language-grounded proposal packet to each candidate, including target pose, yaw hint, altitude band, and semantic confidence.

For each frontier cluster, we compute a semantic relevance score from rendered observations and the goal embedding. We further augment this semantic score with a direction-conditioned prior extracted from the instruction. This module improves waypoint proposal quality without replacing 3D frontier exploration itself.

To support online execution, frontier proposals are emitted as packetized subgoals rather than one-shot plans. Each packet contains a guarded execution prefix and a revisable tail, allowing the system to refresh frontier ranking as new observations arrive while preserving short-horizon control continuity.

### 3.3 Dynamics-Aware Navigation Policy (C2)

The frontier selection policy minimizes a composite cost over travel distance, estimated energy, collision risk, and semantic relevance. We additionally attach stage-aware execution budgets to every frontier packet, including maximum velocity, minimum obstacle clearance, maximum climb/descent rate, and a bounded replanning horizon.

We define a **Semantic Waypoint Packet**
\[
\mathcal{W}_t = \{p_t^{\text{goal}},\; \psi_t^{\text{yaw}},\; b_t^{\text{alt}},\; c_t^{\text{sem}},\; q_t^{\text{dir}},\; g_t^{\text{stage}},\; u_t^{\text{budget}},\; \rho_t^{\text{guard}}\},
\]
which exposes what the planner wants, how strongly language supports it, and under what flight envelope it remains legal.

Execution follows a packet-verifier-controller chain. After the planner proposes a semantic waypoint packet, a verifier checks semantic validity, geometric executability, and budget compliance before the low-level controller commits to the guarded action prefix. If new observations invalidate the packet, only the revisable tail is refreshed.

### 3.4 Navigate-then-Manipulate Architecture (C3)

We model aerial VLN as a two-regime process with an explicit **handoff boundary** between search-time navigation and manipulation-time servoing. During navigation, the planner maintains a 3D semantic frontier map, semantic waypoint packets, and a persistent target hypothesis bank. Once semantic confidence, target pose covariance, and local safety-shell conditions are jointly satisfied, the system emits `handoff_tag = manipulate-ready` and switches to local approach and interaction control.

The handoff is reversible. If manipulation fails because of target drift, viewpoint misalignment, or local geometric infeasibility, the system first attempts packet repair inside a local recovery radius; only repeated failure downgrades the state back to `approach` or `search`.

### 3.5 Consume-Time Packet Contracts and Claim Routing

A packet that is semantically correct at planner time should not be assumed to retain the same execution privilege under delayed controller consumption. We therefore distinguish planner-time, verifier-bind, and controller-consumption windows, and we track four consume-time packet fields: **directional prior survival** `A^{dir}`, **context-anchor survival** `A^{ctx}`, **manipulation-shell survival** `A^{shell}`, and **guarded-prefix survival** `A^{guard}`.

We further attach a reviewer-facing routing tuple
\[
\Gamma = (w^+,\; w^{\dagger},\; r^*,\; q^*)
\]
where `w+` is the earliest positive window, `w†` is the last honesty-preserving window, `r*` is the dominant evidence route, and `q*` is the weakest honest claim allowed by that route. This prevents D06 from merging planner-side clause gains, verifier-side continuity gains, and controller-side rescue gains into one inflated packet-first story.

### 3.6 Refresh-Stable Packet Gating after Outdoor Search Narrowing

We extend the packet contract with a **refresh-stability gate** that activates after an outdoor-search module has already narrowed the candidate target zone. Intuitively, once the system believes it is searching in the right region, the key question is no longer only whether the next frontier is semantically promising, but whether repeated packet refreshes still preserve the same directional clause, context anchor, guarded execution prefix, and manipulation shell assumptions. We therefore define a refresh episode sequence `r_1, r_2, \dots, r_K` between `w^+` and `w^{\dagger}_{consume}` and require packet survival to be judged across the sequence rather than at one isolated window.

For each refresh episode `r_k`, the planner emits an updated packet \(\mathcal{W}_t^{(k)}\) while inheriting the previous packet's active semantic thread unless explicit evidence forces thread switching. The verifier then checks not only geometric executability and budget legality, but also whether the refreshed packet still preserves (i) directional clause consistency, (ii) context-anchor identity, (iii) guarded-prefix continuity, and (iv) local handoff shell validity. This turns refresh from a purely reactive runtime trick into a controlled packet-accountability mechanism.

We further distinguish two upstream narrowing priors before refresh is even invoked. A **geometry-grounded narrowing prior** uses multi-view depth or stereo-consistent target anchoring to stabilize where the packet should attach after the target first becomes partially observable. A **language-prior-guided narrowing prior** uses instruction-conditioned semantic search bias to stabilize which regions should be explored before direct target confirmation exists. These two priors improve different failure surfaces and therefore should remain separate in our method accounting: the former reduces cross-view anchor drift before packet update, while the latter reduces wasted search coverage before packet emission. Neither is allowed to count as consume-time packet superiority unless the resulting packet still passes the refresh-stability and handoff gates.

Concretely, we attach two auxiliary diagnostics to the pre-refresh stage: `Q^{geo}_{narrow}` for geometry-grounded narrowing quality and `Q^{lang}_{narrow}` for language-prior-guided narrowing quality. These terms are used only to explain earlier improvement in `w+` or reduced search inefficiency; they do not enter the promotion contract unless the downstream packet fields remain stable through `w^{\dagger}_{consume}`. This preserves a clean boundary between *helping the system search in a better place* and *proving that the packet stayed valid until use time*.

In parallel, we define a **latent-execution route tag** for compact end-to-end baselines such as AerialVLA. This tag is activated when the system improves trajectory stability or oracle-free autonomy through a direct observation-language-to-control mapping without explicitly exposing reusable packet fields. Such gains are allowed to raise the evidence ceiling from planner-time reasoning to **latent execution sufficiency**, but not to packet-contract preservation unless consume-time packet fields are still audited and preserved. This prevents D06 from misreading a strong minimalist VLA control baseline as if it had already validated a structured packet interface.

Concretely, we define a **refresh-stable packet gate**
\[
G_{\text{refresh}} = \mathbb{1}\Big[ \prod_{k=1}^{K} A^{dir}_{(k)} A^{ctx}_{(k)} A^{guard}_{(k)} = 1 \Big]
\]
for packet-contract promotion, and a stricter handoff gate
\[
G_{\text{NtM}} = \mathbb{1}\Big[ \prod_{k=1}^{K} A^{dir}_{(k)} A^{ctx}_{(k)} A^{guard}_{(k)} A^{shell}_{(k)} = 1 \Big]
\]
for manipulation-ready claims. Under this design, a method may benefit from WildOS-style outdoor narrowing or LiveVLN-style runtime continuity, but it still cannot be promoted to packet-contract or NtM language unless the packet survives refresh episodes all the way to consume time.

### 3.7 Reasoning-Route-Aware Packet Promotion Gate

We add a dedicated **reasoning-route-aware promotion gate** to prevent planner-side modular intelligence from being over-promoted into consume-time packet claims. Recent modular VLM-as-Brain systems such as AgentVLN show that stronger instruction decomposition, cleaner skill routing, and lighter edge-side planning can already improve search-time waypoint quality without yet proving that the resulting packet survives refresh episodes or controller consumption more honestly. We therefore treat the reasoning route as a separate evidence ladder that must be exhausted before any packet-interface promotion is allowed.

Concretely, after the planner emits a candidate packet, we log a reasoning-family diagnostic
\[
Q^{reason}_{route} = \Phi(\text{clause decomposition},\; \text{skill-routing fidelity},\; \text{pre-verifier semantic mismatch reduction})
\]
which measures how much of the gain is still attributable to modular reasoning before execution. This diagnostic may justify earlier `w+`, lower planner-side search entropy, or better pre-verifier waypoint proposals, but it does not by itself raise the claim ceiling beyond **planner-side modular reasoning gain**. Only after subtracting the reasoning-route explanation do we continue to the later gates for search-prior subtraction, compact-control subtraction, and consume-time packet survival.

### 3.8 Progress-Aware Escalation Control, Semantic-Geometric Decoupling, and World-Prior Audits

We further add two mid-level audits motivated by AwareVLN and Fly0, because both can create convincing improvements before full packet accountability is closed. The first audit is a **progress-aware escalation control** that tracks whether the planner promotes the agent from `search` to `approach` or from `approach` to `manipulate-ready` at the correct moment. Concretely, we maintain a stage-confidence vector
\[
\pi_t = (\pi_t^{search},\; \pi_t^{approach},\; \pi_t^{handoff})
\]
and define a wrong-escalation penalty when the active stage advances without sufficient support from packet fields, verifier evidence, and recent progress trend. This gives D06 a way to capture AwareVLN-style gains as **progress-consistent planning support** rather than letting them silently inflate packet-contract claims.

The second audit is a **semantic-geometric decoupling check** that asks whether a method's gain is mainly due to better role separation between semantic grounding and geometric execution. After a target hypothesis is grounded, we split downstream gains into a semantic-side term for target interpretation and a geometric-side term for controller-feasible realization. This yields a decoupling diagnostic
\[
Q^{dec}_{sg} = \Psi(\text{target grounding stability},\; \text{trajectory oscillation reduction},\; \text{goal-to-path realization fidelity}),
\]
which is allowed to justify stronger zero-shot execution stability and lower control jitter. However, `Q^{dec}_{sg}` does not by itself raise the claim ceiling beyond **semantic-geometric decoupling support** unless the packet still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`. In this way, D06 can absorb AwareVLN-style planner self-awareness and Fly0-style semantic-geometric separation without confusing either route with evidence that the reusable packet interface itself has already survived delayed use.

We additionally introduce a **world-prior audit** for SAGE- and PLMD-like gains, because stronger upstream world abstractions or semantic map completion can make the planner look substantially better before any packet is truly consumed. We define two diagnostics. The first is a world-prior transfer term
\[
Q^{world}_{prior} = \Upsilon(\text{open-world transfer gain},\; \text{physics-grounded prior quality},\; \text{early-stage search-entropy reduction}),
\]
which captures how much of the improvement is still attributable to learning in a physics-grounded semantic sandbox rather than to a better packet interface. The second is a semantic-completion term
\[
Q^{comp}_{sem} = \Omega(\text{unknown-region semantic completion quality},\; \text{goal-map sharpening},\; \text{exploration-waste reduction}),
\]
which captures how much of the gain still comes from predicting useful unseen semantics before direct confirmation. These diagnostics are allowed to justify stronger world-prior transfer and semantic-completion support, but they do not by themselves raise the claim ceiling beyond pre-consumption support families unless the packet still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` after those upstream advantages have already been subtracted.

Operationally, we insert the following gate before packet promotion:
\[
G_{reason} = \mathbb{1}[\text{residual gain remains after conditioning on } Q^{reason}_{route}, Q^{world}_{prior}, Q^{comp}_{sem}].
\]
If `G_{reason}=0`, the row freezes at **reasoning-route support**, **world-prior transfer support**, or **semantic-completion support**, depending on the dominant residual explanation. If `G_{reason}=1`, the row may proceed to search-prior subtraction, latent-execution matching, runtime continuity matching, and finally the packet-survival gates `A^{dir}`, `A^{ctx}`, `A^{guard}`, and `A^{shell}`. This ordering ensures that D06 only claims packet-contract superiority when the evidence cannot already be honestly exhausted by modular planner intelligence, upstream world priors, or semantic map completion alone.

### 3.9 Search-Route-Subtracted Packet Proposal Ranking

Our proposal layer explicitly ranks candidate packets under a **search-route-subtracted** objective so that earlier narrowing gains are not silently counted twice. We first parse the instruction into clause units, directional relations, and target-environment hints, then derive route-specific priors from three upstream families: language-mediated region narrowing (`Q^{lang}_{narrow}`), geometry-grounded target anchoring (`Q^{geo}_{narrow}`), and modular reasoning-route support (`Q^{reason}_{route}`). These priors are useful because they reduce wasted search coverage, pre-refresh drift, and pre-verifier mismatch, but they remain planner-side support signals rather than consume-time evidence.

For each candidate packet `\mathcal{W}_i`, we define a ranking score
\[
S(\mathcal{W}_i)=S_{sem}+\lambda_{dir}S_{dir}+\lambda_{geo}Q^{geo}_{narrow}+\lambda_{lang}Q^{lang}_{narrow}+\lambda_{reason}Q^{reason}_{route}-\lambda_{risk}C_{dyn},
\]
where `S_{sem}` is semantic relevance, `S_{dir}` is direction-conditioned adherence, and `C_{dyn}` is the dynamics-aware flight risk and budget cost. Crucially, the first three auxiliary route terms are only used to rank *which packet to test next*; they are not allowed to raise the final evidence ceiling unless the selected packet later survives refresh and controller consumption.

We further add a **local-shell feasibility term** `Q^{shell}_{local}` to capture whether a KIO-style controller shell can safely realize the proposed packet under near-field obstacle geometry and onboard latency constraints. This term may improve packet ranking by filtering proposals that are semantically strong but geometrically brittle in cluttered spaces. However, `Q^{shell}_{local}` is still an execution-support signal rather than a consume-time packet-survival proof: it may justify stronger Geometric Executability Gate performance, but not by itself stronger `A^{dir}`, `A^{ctx}`, or `A^{guard}` preservation.

We further add a **planner-side uncertainty and active-perception utility term** `Q^{unc}_{plan}` motivated by local evidence from LMPath, StereoNav, WildOS, and AgentVLN. LMPath shows that language-mediated priors can shrink the search region early, StereoNav shows that geometry-grounded target-location priors stabilize attachment once partial observation begins, WildOS shows that open-vocabulary outdoor search wins often come from choosing better observation frontiers rather than stronger late packet contracts, and AgentVLN shows that modular planner intelligence can improve which sensing/planning skill should be invoked before execution. In our framework, these signals naturally meet at a single planner-side question: **when should the agent spend one more sensing action to reduce ambiguity before committing the next packet?**

Concretely, we let `Q^{unc}_{plan}` summarize the expected value of one-step active perception under matched budget:
\[
Q^{unc}_{plan}=\Delta H_{target}+\eta_{dir}\Delta A^{dir}_{pre}+\eta_{ctx}\Delta A^{ctx}_{pre}-\eta_{time}C_{sense}-\eta_{risk}C_{hover},
\]
where `\Delta H_{target}` is the predicted reduction in target-zone uncertainty, `\Delta A^{dir}_{pre}` is the expected improvement in directional-clause stability before packet emission, `\Delta A^{ctx}_{pre}` is the expected improvement in anchor consistency before refresh, `C_{sense}` is the additional sensing-time cost, and `C_{hover}` is the exposure or hover risk incurred by delaying commitment. This term can raise proposal quality by explicitly preferring packets whose ambiguity can be cheaply reduced via one more look, a small altitude shift, or a short verification orbit.

Importantly, `Q^{unc}_{plan}` remains a **planner-side active-perception support signal**, not a packet-survival certificate. A row whose gain is exhausted by better uncertainty reduction or safer information gathering must freeze at **active-perception support** rather than packet-contract superiority. Only after subtracting this route together with reasoning, search-prior, latent-control, and local-shell explanations may a residual gain continue to the runtime and consume-time packet gates.

We therefore apply a subtraction rule before narrative promotion: if a row's gain disappears after conditioning on these upstream ranking routes, the row is frozen as **search-route improvement only**, **execution-shell support only**, or **active-perception support only**, depending on the dominant residual explanation. If residual gain remains, the packet must still pass `G_{reason}`, survive refresh episodes, and preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` before it may be promoted to packet-contract language; `A^{shell}` remains the last gate for manipulation-ready handoff claims. This design gives D06 a cleaner contract: better search, better local shells, and better ambiguity-aware sensing are welcome, but only consume-time packet survival earns deployment-grade language.

## 4. Experiments

### 4.1 Setup

We evaluate on indoor and outdoor aerial VLN settings with matched sensing, latency, and controller budgets. Core metrics include navigation success, verifier pass rate, packet staleness, context retention, packet handoff failure, and manipulation-ready promotion rate.

### 4.2 Main Results

Our main-result philosophy is conservative: a late-window gain is only allowed to support the strongest claim whose evidence route is fully closed at controller-consumption time.

### 4.2.1 Search-Prior Route-Closure Readout before Packet Promotion

To keep D06 honest when evaluating better search guidance, we introduce a dedicated readout for **search-prior route closure**. The key question is not whether a method finds promising regions earlier, but whether that earlier narrowing actually survives the packet lifecycle up to consume time. We therefore separate two upstream diagnostics from the later packet-contract fields: `Q^{lang}_{narrow}` measures how much language-mediated priors improve region narrowing before target confirmation, and `Q^{geo}_{narrow}` measures how much geometry-grounded anchoring reduces pre-refresh drift after partial target observation.

These two diagnostics may explain earlier `w+`, lower search inefficiency, or better target-zone concentration, but they are not allowed to directly promote a row into packet-contract or NtM language. A row is only allowed to leave the **search-prior support** bucket if the resulting refreshed packet still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`; only rows that additionally preserve `A^{shell}` may support manipulation-ready handoff claims. In practice, this creates a subtraction discipline for LMPath- and StereoNav-style gains: first test whether the gain is exhausted by better narrowing, then check whether any residual benefit survives the refresh episodes and consume-time boundary.

### 4.2.2 Reasoning-Family Subtraction before Packet-Contract Promotion

We introduce a dedicated subtraction step for **reasoning-and-skill-routing gains** motivated by AgentVLN-style modular navigation. The key question is whether a row improves because the system reasons better *before* execution—e.g., better clause decomposition, lower pre-verifier semantic mismatch, or cleaner skill dispatch—or because the emitted packet truly survives refresh and controller consumption more honestly. To separate these cases, we log a reasoning-family diagnostic `Q^{reason}_{route}` alongside the existing narrowing and packet-survival fields.

A row may use `Q^{reason}_{route}` to justify stronger planner-side semantic routing, earlier `w+`, or lower pre-verifier mismatch, but it is not allowed to claim packet-contract superiority unless the same row still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` after conditioning on reasoning-family gains. Only rows that additionally preserve `A^{shell}` may support manipulation-ready handoff language. In practice, this creates a matched subtraction discipline for AgentVLN-like baselines: first explain what was gained by modular reasoning and skill routing alone, then check whether any residual improvement survives the packet lifecycle to actual consume time. This prevents D06 from mistaking a better search-time VLM-as-Brain route for a solved packet-first deployment interface.

### 4.2.3 Search-Prior Subtraction against Minimalist Latent Execution and Local Execution Shells

A second failure mode in aerial VLN reporting is to treat earlier narrowing and stronger end-to-end control as if they automatically compose into a packet-interface win. Local evidence from **LMPath** and **StereoNav** suggests that search-route improvements can materially raise `Q^{lang}_{narrow}` and `Q^{geo}_{narrow}` before the target is firmly grounded, while **AerialVLA** shows that a compact end-to-end controller can already convert partial semantic evidence into stable low-dimensional flight actions without exposing an explicit packet object. **KIO-planner** adds a different confound: a strong local execution shell may substantially improve near-field safety, geometric feasibility, and latency even when the high-level packet semantics remain unchanged. This means a D06 row may look stronger simply because it searches more efficiently, because its latent execution route is already strong, or because its local shell rescues poor packets more effectively.

We therefore add a **search-prior and execution-shell subtraction rule** before any packet-centric promotion. For each result row, we first ask whether the gain is sufficiently explained by `Q^{lang}_{narrow}` and `Q^{geo}_{narrow}` alone. If yes, the row is frozen as **search-prior support**. If residual gain remains, we next ask whether the evidence is still fully explained by an **AerialVLA-style latent-execution family**, i.e., better oracle-free compact control under matched onboard budget and latency. If the answer is yes, the row is promoted at most to **latent execution sufficiency** rather than packet-contract preservation. We then ask whether the remaining gain is still fully explained by a **KIO-style local execution shell**, i.e., better geometric executability and short-horizon safety under matched planner semantics. If yes, the row is promoted at most to **execution-shell support** rather than packet-contract preservation.

Only rows whose residual gain survives all three subtractions and still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` may be upgraded to packet-contract language; `A^{shell}` remains the final gate for NtM handoff claims. Formally, the reviewer-facing order becomes
\[
(Q^{lang}_{narrow}, Q^{geo}_{narrow}) \rightarrow \tau_{latent} \rightarrow \tau_{shell} \rightarrow (A^{dir}, A^{ctx}, A^{guard}) \rightarrow A^{shell},
\]
where `\tau_{latent}` denotes the strongest residual explanation still attributable to the minimalist latent-execution family and `\tau_{shell}` denotes the strongest residual explanation still attributable to the local execution-shell family. This ordering forces D06 to answer a sharper question than ordinary aerial VLN papers: after subtracting better search guidance, stronger compact control, and stronger local safety shells, **is there still evidence that the packet itself survives until use time?**

### 4.2.4 Consume-Time Contract Table with Unified-Reasoning, Latent-Execution, and Local-Shell Freezes

We use a main comparison table of the form:

`Method | w+ | w†bind | w†consume | Freshness Regime | Route Tag | A^{dir} | A^{ctx} | A^{shell} | A^{guard} | ΔSR | ΔMRP | ΔCCR | ΔPKR | Weakest Honest Claim | Unified-Reasoning Freeze | AerialVLA Freeze | KIO-Shell Freeze`

This schema intentionally forces a field-level reading before any headline interpretation. A method that improves aggregate success but loses `A^{shell}` at the late boundary should not be described as preserving NtM handoff value.

### 4.2.5 Boundary-Time Reading Rule for the Weakest Honest Claim

The reviewer-facing order is: (1) locate `w+`; (2) check survival to `w†bind`; (3) check survival to `w†consume`; (4) inspect `A^{dir}/A^{ctx}/A^{shell}/A^{guard}` at boundary time; and (5) route the row to the strongest matched explanation family that still remains honest. D06 should prefer the weakest claim that exhausts the evidence rather than the strongest claim that sounds plausible.

### 4.2.3 Minimal Experiment Logging Fields for Contract-Survival Audits

We formalize the minimum D06 experiment record as
\[
\Lambda_{D06}=(w^+, w^{\dagger}_{bind}, w^{\dagger}_{consume}, A^{dir}, A^{ctx}, A^{shell}, A^{guard}, \rho_{dc}(\delta), \tau_{route}, \tau_{claim}).
\]
This tuple is mandatory rather than illustrative. Missing consume-time fields or an unlogged delayed-consumption regime automatically freeze the evidence below full packet-contract superiority.

### 4.2.4 Route-Closure Main Table Columns for Consume-Time Promotion Discipline

To make the route-closure rule operational at reporting time, the D06 main table must expose not only task outcomes but also the **promotion contract** that justifies each late-window claim. We therefore extend the main result schema with reviewer-facing columns such as **Family-Matched Comparator**, **Closure Level**, **Promotion Ceiling**, **Promotion Blocker**, and **Last Honest Consume Window**. The comparator column records which nearby baseline family is the fairest explanatory counterfactual—e.g., AerialVLA for latent execution sufficiency, KIO-planner for local execution-shell support, OnFly/LiveVLN for runtime continuity, and HTNav/Unified Aerial VLN for planner-time structured reasoning.

This extension matters because many positive late-window outcomes are still underdetermined without an explicit promotion contract. A gain that beats a planner-structure baseline but loses `A^{shell}` at consume time should stay frozen below a full packet-contract claim even if aggregate success improves. A gain that beats a runtime baseline only through `A^{guard}` survival and bounded lag robustness still supports a continuity story, not a handoff-accountability story. By forcing every row to name its matched comparator family and closure level, the table prevents us from stitching unrelated gains into one oversized packet-first narrative.

We therefore recommend the following canonical column order for D06 main results: `Method | w+ | w†bind | w†consume | Freshness Regime | Family-Matched Comparator | Closure Level | A^{dir} | A^{ctx} | A^{shell} | A^{guard} | ΔSR | ΔMRP | ΔCCR | ΔPKR | Promotion Ceiling | Promotion Blocker | Weakest Honest Claim`. Under this contract, *Promotion Ceiling* is determined before prose is written. If the ceiling remains `planner-time reasoning gain`, the paragraph must not drift into consume-time handoff language. If the ceiling remains `runtime continuity gain` or `execution-shell support`, the result must not be presented as packet-contract superiority. Only rows whose closure level reaches full consume-time packet preservation may support an NtM handoff headline.

### 4.2.5 Claim-Freezing Paragraph Template under Promotion Blockers

The result paragraph itself should mirror the table contract rather than reinterpret it. We therefore define a minimal paragraph template: **(i)** name the matched comparator family, **(ii)** state the earliest positive window and last honest consume window, **(iii)** report the surviving packet fields, **(iv)** state the promotion blocker, and **(v)** stop at the weakest honest claim. This template ensures that a row blocked by shell-validity loss cannot be rhetorically upgraded by stronger nearby metrics such as success rate or verifier pass rate.

Concretely, a D06 paragraph should read in the following order: *Compared with the family-matched baseline X, the proposed method first becomes positive at `w+`, remains honest through `w†consume`, preserves `{A^{dir}, A^{ctx}, ...}`, but is blocked from stronger promotion by `Promotion Blocker`; therefore the strongest supported interpretation is `Weakest Honest Claim`.* This fixed order matters because late-window aerial VLN gains are often tempting to narrate from the headline backward. Our contract instead forces prose to flow from evidence boundary to narrative ceiling.

### 4.2.6 Experiment-Contract Alignment as a Reporting Primitive

A final lesson from the recent local baseline cluster is that D06 should treat **experiment-contract alignment** itself as a primary reporting primitive rather than an afterthought. AerialVLA, KIO-planner, OnFly, HTNav, LiveVLN, and Unified Aerial VLN each illuminate different gain routes, but none forces logs, tables, and prose to agree on one promotion contract. Our paper should therefore make this alignment part of the method-evaluation interface: a late-window improvement is incomplete unless it comes with the route identity, closure level, blocker, and claim ceiling needed to report it honestly.

### 4.2.9 Experiment-Table Alignment for Search- and Reasoning-Family Route Closure

The main-results table must mirror the same promotion ladder used in our method and related-work accounting. In particular, any D06 row that may still be explained by **AgentVLN-style modular reasoning**, **LMPath-style language-mediated narrowing**, **StereoNav-style geometry-grounded anchoring**, **WildOS-style outdoor search**, or **AerialVLA-style compact latent execution** is not allowed to jump directly from an early positive window to packet-contract language. Instead, the row must first declare which upstream family remains matched and which subtraction steps have already been closed.

Concretely, every such row should expose at least the following fields before any late-window prose is promoted: `Planner-Modularity Family Match`, `Q^{reason}_{route}`, `Search-Prior Family`, `Q^{lang}_{narrow}`, `Q^{geo}_{narrow}`, `Search Route Win`, `Refresh-Stable Until`, `Closure Level`, `Promotion Ceiling`, and `Promotion Blocker`. These fields are not cosmetic reporting extras. They define whether the observed gain still lives at **reasoning-route support**, **search-prior support**, **latent execution sufficiency**, **runtime continuity support**, or whether a true packet-facing residual remains after subtraction. If the table omits these fields, then the corresponding row is evidence-incomplete and should be frozen below packet-contract promotion.

This alignment rule is especially important for D06 because recent local anchors now provide several superficially compatible but semantically distinct explanations for improvement: cleaner instruction decomposition, better search-region narrowing, stronger geometry anchoring, more robust open-vocabulary outdoor search, and smoother compact control. Without an experiment-table alignment rule, these gains can be mistakenly merged into one inflated late-window story. Our paper should instead force them to remain separate until the residual survives the full consume-time contract.

### 4.2.10 Current Evidence-Consistent Freeze after Search/Reasoning Table Alignment

Under the current anchor set, the most honest freeze is still conservative: rows primarily explained by `Q^{reason}_{route}` remain **reasoning-route support**; rows primarily explained by `Q^{lang}_{narrow}` or `Q^{geo}_{narrow}` remain **search-prior support**; rows primarily matched by AerialVLA-style direct control remain **latent execution sufficiency**; and rows whose main advantage is only guarded refresh or execution continuity remain **runtime continuity support**. Only rows that survive these matched explanations and still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` may be promoted to packet-contract language; only rows that additionally preserve `A^{shell}` may support NtM handoff claims.

This means D06 should currently resist a common writing temptation: if a variant both narrows search earlier and refreshes more smoothly, it may still be fully explainable by a mixture of planner modularity, search priors, and compact control. Such a row does not yet earn a packet-first headline. The headline is only justified when the residual after aligned table subtraction remains visible at the consume-time boundary.

### 4.2.9 Experiment-Table Alignment for Search- and Reasoning-Family Route Closure

The main-results table must mirror the same promotion ladder used in our method and related-work accounting. In particular, any D06 row that may still be explained by **AgentVLN-style modular reasoning**, **LMPath-style language-mediated narrowing**, **StereoNav-style geometry-grounded anchoring**, **WildOS-style outdoor search**, or **AerialVLA-style compact latent execution** is not allowed to jump directly from an early positive window to packet-contract language. Instead, the row must first declare which upstream family remains matched and which subtraction steps have already been closed.

Concretely, every such row should expose at least the following fields before any late-window prose is promoted: `Planner-Modularity Family Match`, `Q^{reason}_{route}`, `Search-Prior Family`, `Q^{lang}_{narrow}`, `Q^{geo}_{narrow}`, `Search Route Win`, `Refresh-Stable Until`, `Closure Level`, `Promotion Ceiling`, and `Promotion Blocker`. These fields are not cosmetic reporting extras. They define whether the observed gain still lives at **reasoning-route support**, **search-prior support**, **latent execution sufficiency**, **runtime continuity support**, or whether a true packet-facing residual remains after subtraction. If the table omits these fields, then the corresponding row is evidence-incomplete and should be frozen below packet-contract promotion.

This alignment rule is especially important for D06 because recent local anchors now provide several superficially compatible but semantically distinct explanations for improvement: cleaner instruction decomposition, better search-region narrowing, stronger geometry anchoring, more robust open-vocabulary outdoor search, and smoother compact control. Without an experiment-table alignment rule, these gains can be mistakenly merged into one inflated late-window story. Our paper should instead force them to remain separate until the residual survives the full consume-time contract.

### 4.2.10 Current Evidence-Consistent Freeze after Search/Reasoning Table Alignment

Under the current anchor set, the most honest freeze is still conservative: rows primarily explained by `Q^{reason}_{route}` remain **reasoning-route support**; rows primarily explained by `Q^{lang}_{narrow}` or `Q^{geo}_{narrow}` remain **search-prior support**; rows primarily matched by AerialVLA-style direct control remain **latent execution sufficiency**; and rows whose main advantage is only guarded refresh or execution continuity remain **runtime continuity support**. Only rows that survive these matched explanations and still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` may be promoted to packet-contract language; only rows that additionally preserve `A^{shell}` may support NtM handoff claims.

This means D06 should currently resist a common writing temptation: if a variant both narrows search earlier and refreshes more smoothly, it may still be fully explainable by a mixture of planner modularity, search priors, and compact control. Such a row does not yet earn a packet-first headline. The headline is only justified when the residual after aligned table subtraction remains visible at the consume-time boundary.

### 4.2.11 Search-Side Complementarity as a Narrowing Family, not a Packet Win

LMPath and StereoNav sharpen an important methodological boundary for D06: **better search-side narrowing is useful, but it is still not the same thing as packet survival**. LMPath contributes a language-mediated prior that can reduce wasted region coverage before the target is directly observed, while StereoNav contributes geometry-grounded anchoring that can stabilize target attachment once partial observation begins. These gains should be welcomed because they improve where the system looks and how stably it keeps the target hypothesis aligned during early navigation. However, they remain upstream to the refresh-and-consume boundary.

We therefore treat LMPath- and StereoNav-like gains as a dedicated **narrowing family** inside the experiment readout. A row may use `Q^{lang}_{narrow}` to explain earlier target-zone concentration or reduced search entropy, and may use `Q^{geo}_{narrow}` to explain lower cross-view anchor drift or more stable partial-target attachment. But unless the same row later preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`, the result must remain frozen as **narrowing support only**. If `A^{shell}` is also missing, the row is doubly barred from manipulation-ready language.

This separation is essential because D06 now has enough local evidence to tell two different success stories that can look similar in aggregate metrics. One story is that the system found the right region faster and anchored the target more stably. The other is that a packet preserved directional clause, context anchor, and guarded execution privilege all the way until controller use time. Our experiments should never let the first story masquerade as the second.

### 4.2.12 Refresh-Episode Audits after Narrowing Gains

Once narrowing gains are admitted as their own family, D06 must also audit what happens **between the first search win and actual packet consumption**. We therefore require every row with non-trivial `Q^{lang}_{narrow}` or `Q^{geo}_{narrow}` gain to log a refresh-episode trace over the interval from `w^{+}` to `w^{\dagger}_{consume}`. At minimum, this trace should record `Refresh Count before Consume`, `First Refresh Violation Type`, `Refresh-Repaired before Consume`, and the last window where the same directional clause and anchor identity still survive.

This audit matters because many search-side wins decay quietly under streaming observations. A row may look strong when the target zone is first narrowed, yet lose the active clause, swap anchors, or invalidate the guarded prefix after one or two refreshes. In such cases, the gain is still valuable as **refresh-stable narrowing support** if the packet survives long enough to reduce search waste, but it should not be promoted to packet-contract superiority. Only rows whose narrowing-family gains survive the refresh sequence and still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` at consume time may move up the promotion ladder.

### 4.2.13 Search-Prior Logging Contract aligned with Refresh and Promotion Gates

To make the above discipline executable, D06 should use a minimal search-prior logging contract for all rows potentially explained by LMPath-, StereoNav-, WildOS-, or AerialVLA-adjacent gains. The recommended fields are: `Search-Prior Family`, `Narrowing Win Source`, `Q^{lang}_{narrow}`, `Q^{geo}_{narrow}`, `Search Route Win`, `Refresh Count before Consume`, `First Refresh Violation Type`, `Refresh-Repaired before Consume`, `Search-Subtracted Claim Ceiling`, and `Packet-Promotion Eligibility after Compact-Control Matching`.

The purpose of this contract is to align four phenomena that are often conflated in practice: **better narrowing**, **more refreshes**, **smoother compact control**, and **actual packet survival**. If a row improves only because it finds the right region earlier, it should freeze at **search-prior support**. If it survives refresh but is still fully explained by compact latent control, it should freeze at **latent execution sufficiency**. If only the residual after both checks still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`, then and only then may the row enter packet-contract language.

### 4.2.14 Unified Reading Order for Planner Modularity, Search Priors, Runtime, and Packet Survival

Given the growing number of nearby explanatory families, D06 needs a fixed evidential reading order. We therefore freeze the reviewer-facing ladder as: **planner modularity → search-prior narrowing → compact latent execution → runtime continuity → consume-time packet preservation → manipulation-ready handoff**. This means the burden of proof flows from earlier, cheaper explanations toward later, stronger ones.

Under this rule, a row that is still fully explainable by better instruction decomposition or skill routing stays at **reasoning-route support**. A row that additionally beats planner modularity but is still exhausted by better target-zone narrowing stays at **search-prior support**. A row that further survives those checks but is still matched by AerialVLA-style direct control remains at **latent execution sufficiency**. A row that only adds guarded refresh and continuity remains **runtime continuity support**. Only the residual that survives all earlier families and still preserves consume-time fields earns **packet-contract** language; only if `A^{shell}` also survives does the row earn **NtM handoff** language.

This ordering is intentionally strict. Without it, D06 risks stitching together several early positive signals into a single inflated claim about deployable packet interfaces. With it, the paper can instead argue something stronger and cleaner: after all cheaper explanations are exhausted, there is still packet-level residual evidence at the actual controller-use boundary.

### 4.2.15 Reasoning-Route Family Alignment in the Main Results Table

The current D06 anchor set now makes one gap obvious: `Q^{reason}_{route}` is already part of the method contract, but it is still too easy for the experiments section to treat modular reasoning gains as prose-only caveats rather than table-level evidence gates. We therefore require the main-results table to expose a dedicated **reasoning-route family alignment** block before any late-window packet claim is interpreted. At minimum, each row that may still be explained by AgentVLN-style modular reasoning must explicitly report `Planner-Modularity Family Match`, `Q^{reason}_{route}`, `Planner-Only Explanation Remaining`, and `Route-Closure Outcome`.

This addition matters because planner-side modularity can improve clause decomposition, skill routing, and pre-verifier waypoint cleanliness without proving that the emitted packet survives refresh episodes or delayed controller consumption. A row that still owes most of its gain to modular reasoning should therefore freeze at **reasoning-route support**, even if downstream metrics also move slightly in the right direction. Only after the row remains positive *after conditioning on* `Q^{reason}_{route}` may it continue to the later subtraction stages for search priors, compact latent execution, runtime continuity, and consume-time packet preservation.

### 4.2.16 Unified Search/Reasoning/Latent/Runtime Promotion Ladder

We further collapse the current family-specific caveats into one reviewer-facing promotion ladder:
\[
Q^{reason}_{route} \rightarrow (Q^{lang}_{narrow}, Q^{geo}_{narrow}, \tau_{search}) \rightarrow \tau_{latent} \rightarrow \tau_{runtime} \rightarrow (A^{dir}, A^{ctx}, A^{guard}) \rightarrow A^{shell},
\]
where `\tau_{search}` denotes the strongest residual explanation still attributable to search-side complementarity, `\tau_{latent}` denotes the strongest residual explanation still attributable to compact end-to-end latent control, and `\tau_{runtime}` denotes the strongest residual explanation still attributable to guarded live-execution continuity. This makes explicit that **reasoning-family gains should be exhausted first**, because they can contaminate both narrowing quality and pre-verifier packet plausibility before any controller-facing evidence appears.

Operationally, this means every D06 row should name (i) the earliest family that can still honestly explain the gain, (ii) the last family it survives after subtraction, and (iii) the first late-window field that fails. If a row still collapses at the reasoning-family stage, it must not inherit stronger language from later packet fields. If it survives reasoning and search subtraction but is still matched by AerialVLA-style direct control, it freezes at **latent execution sufficiency**. If it further survives latent subtraction but wins only through guarded refresh and continuity, it freezes at **runtime continuity support**. Only the residual after all these stages may enter packet-contract language.

### 4.2.17 Reasoning-Route Logging Contract aligned with Search-Prior and Packet Gates

To make the above ladder executable, D06 needs a minimal logging contract for reasoning-family subtraction that is symmetric with the existing narrowing-family and compact-control contracts. We therefore require any row potentially explained by modular planner intelligence to record: `Planner-Modularity Family Match`, `Q^{reason}_{route}`, `Instruction-Decomposition Gain`, `Skill-Routing Gain`, `Pre-Verifier Mismatch Reduction`, `Planner-Only Explanation Remaining`, `Route-Closure Outcome`, and `Promotion Ceiling after Reasoning Subtraction`.

These fields are not optional diagnostics. They answer a concrete reporting question: did the method genuinely preserve a better packet until use time, or did it simply produce a cleaner packet proposal before execution? If the latter explanation still exhausts the gain, the row must stay at **reasoning-route support** and may not borrow stronger language from consume-time packet fields. This logging contract is especially important now that AgentVLN-family evidence is strong enough locally to become a plausible rival explanation for many early D06 improvements.

### 4.2.18 Experiment-Field Alignment for Reasoning/Search/Latent/Runtime Promotion Ladders

The experiments section should expose the *same* evidential ladder that the method and related-work sections already assume. In practice, this means that any D06 row potentially explained by **AgentVLN-style modular reasoning**, **LMPath-style language-mediated narrowing**, **StereoNav-style geometry-grounded anchoring**, **WildOS-style outdoor search**, **AerialVLA-style compact latent control**, or **LiveVLN/OnFly-style runtime continuity** must declare where it first becomes positive, which family explanations have already been subtracted, and where the gain finally stalls before consume time.

Concretely, we require every such row to log a minimal aligned schema:
`Planner-Modularity Family Match | Q^{reason}_{route} | Search-Prior Family | Q^{lang}_{narrow} | Q^{geo}_{narrow} | Search Route Win | Refresh-Stable Until | AerialVLA-Matched Win | Runtime-Family Match | First Unrepaired Refresh Violation | Closure Level | Promotion Ceiling | Promotion Blocker | Weakest Honest Claim`.
These fields are not reporting decoration. They determine whether the observed gain still lives at **reasoning-route support**, **search-prior support**, **latent execution sufficiency**, **runtime continuity support**, or whether a true packet-facing residual remains after subtraction. If the row omits any of these fields, the evidence is incomplete and must be frozen below packet-contract promotion.

This alignment rule matters because D06 now has enough strong local anchors that several superficially positive rows can be over-explained in different ways. A row may decompose instructions better, narrow the target zone earlier, anchor the target more stably, refresh more smoothly, and execute compactly under low latency—all before proving anything about consume-time packet survival. Our experiments must therefore report the subtraction path itself, not only the final outcome.

### 4.2.19 Current Evidence-Consistent Freeze after Field-Level Promotion Alignment

Under the current D06 anchor set, the most honest freeze remains conservative. Rows whose gains are still exhausted by `Q^{reason}_{route}` remain **reasoning-route support**. Rows that beat planner modularity but are still exhausted by `Q^{lang}_{narrow}`, `Q^{geo}_{narrow}`, or WildOS-style outdoor-search subtraction remain **search-prior support**. Rows that survive those checks but are still matched by **AerialVLA-style compact latent control** remain **latent execution sufficiency**. Rows whose main residual advantage is only guarded refresh or execution continuity remain **runtime continuity support**. Only rows that survive all these matched explanations and still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` may be promoted to packet-contract language; only rows that additionally preserve `A^{shell}` may support NtM handoff claims.

This freeze is intentionally strict. If a row looks good early because it both narrows search better and refreshes more gracefully, it may still be fully explainable by the combination of reasoning, search-prior, latent-control, and runtime families. Such a row does not yet earn a packet-first headline. The headline belongs only to the residual that remains visible at the consume-time boundary after the full aligned ladder has been honestly traversed.

### 4.2.20 Planner-Uncertainty and Active-Perception Support must be Logged before Packet Promotion

The current local anchor set also shows a quieter route that can easily inflate D06 claims: **planner-side uncertainty reduction through active perception**. LMPath improves search efficiency by injecting language-mediated region priors, StereoNav improves attachment stability through target-location priors, WildOS improves frontier choice through open-vocabulary search cues, and AgentVLN improves which sensing/planning skill should be called at the right moment. These gains often manifest not as a better late packet per se, but as a better decision about whether the system should spend one more observation step before committing the next packet.

We therefore require every D06 row potentially helped by ambiguity-aware sensing to expose an additional alignment block: `Active-Perception Family Match | Q^{unc}_{plan} | One-More-Look Gain | Sensing-Cost Penalty | Active-Perception-Only Explanation Remaining | Packet-Promotion Eligibility after Uncertainty Matching`. Here `Q^{unc}_{plan}` summarizes the residual gain still attributable to better uncertainty reduction, safer short verification maneuvers, or cheaper ambiguity resolution before packet emission. If the gain is exhausted by this route, the row must freeze at **active-perception support** rather than packet-contract language.

This matters because a system that chooses better moments to pause, orbit, rise, or re-observe may look substantially stronger in aggregate navigation success while still saying little about whether the eventual packet survives repeated refresh and delayed controller consumption. Our experiments should therefore distinguish **better ambiguity handling before commitment** from **better packet survival after commitment**.

### 4.2.21 Unified Promotion Ladder with Active-Perception Gates

Under the updated D06 anchor set, the reviewer-facing default reading order should now be
\[
Q^{reason}_{route} \rightarrow (Q^{lang}_{narrow}, Q^{geo}_{narrow}, \tau_{search}) \rightarrow Q^{unc}_{plan} \rightarrow Q^{data}_{prior} \rightarrow \tau_{latent} \rightarrow Q^{shell}_{local} \rightarrow \tau_{runtime} \rightarrow (A^{dir}, A^{ctx}, A^{guard}) \rightarrow A^{shell},
\]
where `Q^{unc}_{plan}` denotes the strongest residual explanation still attributable to planner-side uncertainty reduction and active-perception utility, `Q^{data}_{prior}` denotes the strongest residual explanation still attributable to synthetic-data scaling, and `Q^{shell}_{local}` denotes the strongest residual explanation still attributable to local execution-shell improvements. This ordering is strict on purpose: richer priors, cleaner local shells, smoother compact control, and cheaper ambiguity reduction are all welcome, but only the residual after these cheaper explanations are honestly exhausted may enter packet-contract promotion.

Operationally, each row should now report the earliest family that still explains the gain, the last family it survives after subtraction, and the first late-window field that fails. Rows exhausted by `Q^{unc}_{plan}` freeze at **active-perception support**; rows exhausted by `Q^{data}_{prior}` freeze at **pretraining-support only**; rows exhausted by `Q^{shell}_{local}` freeze at **execution-shell support**. Only rows that survive reasoning, search, active-perception, data, latent-control, and shell matching—and still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`—may be promoted to packet-contract language; `A^{shell}` remains the final gate for NtM handoff claims.

### 4.2.23 Planner-Side Active-Perception Family Match after Re-reading LMPath / StereoNav / WildOS / AgentVLN

The current local anchor set suggests that D06 should no longer treat planner-side active perception as one monolithic utility term. **LMPath** improves one-more-look value mainly by using language-mediated priors to decide *where an extra observation is likely to collapse the search space most cheaply*. **StereoNav** improves one-more-look value mainly by using geometry-grounded target-location priors to decide *when another view is likely to repair cross-view anchor drift before commitment*. **WildOS** improves one-more-look value mainly by using open-vocabulary frontier-search cues to decide *which boundary node is worth re-checking before a full route commitment*. **AgentVLN** improves one-more-look value mainly by using modular skill routing to decide *which sensing or planning skill should be invoked before the next packet is emitted*. These are all real planner-side gains, but they are still best understood as different routes to **cheap ambiguity reduction before packet commitment**, not as packet-contract evidence by default.

We therefore require an additional family-matched logging block before packet promotion: `LMPath-One-More-Look Match | StereoNav-Recheck Match | WildOS-Frontier-Recheck Match | AgentVLN-Skill-Routed Sensing Match | Q^{unc}_{plan} | One-More-Look Gain | Sensing-Cost Penalty | Hover-Risk Penalty | Active-Perception-Only Explanation Remaining | Guidance-after-Look Ceiling`. Here `One-More-Look Gain` records how much the row improves after one extra sensing opportunity under matched budget, `Sensing-Cost Penalty` records the temporal or energy cost of delaying commitment, and `Hover-Risk Penalty` records the additional exposure or instability risk incurred by that delay. If a row's gain is still honestly exhausted by these planner-side one-more-look routes, the row must freeze at **active-perception support** rather than packet-contract language, regardless of whether later aggregate navigation success looks strong.

### 4.2.24 World-Prior and Semantic-Completion Families must be Subtracted before Packet Promotion

SAGE and PLMD expose two additional upstream explanations that D06 must now keep explicit in the experiments section. SAGE-like systems may win because a physics-grounded semantic sandbox produces better open-world transfer, lower early search entropy, and stronger planner-side priors before any packet has been stress-tested at consume time. PLMD-like systems may win because diffusion-style label-map completion sharpens unknown-region semantics, predicts goal-relevant structure behind occlusion, and reduces exploratory waste before direct confirmation. Both routes can materially improve `w^+`, early target-zone concentration, and search efficiency, but they still live upstream of packet accountability.

We therefore require every D06 row potentially helped by these routes to log: `World-Prior Family Match | Q^{world}_{prior} | Semantic-Completion Family Match | Q^{comp}_{sem} | Early-Stage Search-Entropy Reduction | Unknown-Region Goal-Map Gain | World-Prior-Only Explanation Remaining | Semantic-Completion-Only Explanation Remaining | Packet-Promotion Eligibility after World/Completion Matching`. If a row's gain is exhausted by better sandbox priors or better map completion, it must freeze at **world-prior transfer support** or **semantic-completion support** rather than packet-contract language.

This subtraction matters because D06 now has enough local evidence to tell a tempting but inflated story: the planner enters the right region earlier, carries a cleaner target hypothesis, and appears more stable under refresh, so the packet must be better. Our contract rejects that shortcut. Only residual gains that remain after subtracting SAGE-style world-prior advantages and PLMD-style semantic-completion advantages, and that still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`, may be promoted to packet-contract language; only rows that additionally preserve `A^{shell}` may support NtM handoff claims.

### 4.2.25 Current Evidence-Consistent Freeze after World-Prior and Semantic-Completion Matching

Under the current D06 anchor set, the evidence ceiling remains deliberately conservative. Rows primarily explained by `Q^{reason}_{route}` remain **reasoning-route support**; rows primarily explained by `Q^{lang}_{narrow}` or `Q^{geo}_{narrow}` remain **search-prior support**; rows primarily explained by `Q^{world}_{prior}` remain **world-prior transfer support**; rows primarily explained by `Q^{comp}_{sem}` remain **semantic-completion support**; rows primarily matched by AerialVLA-style direct control remain **latent execution sufficiency**; and rows whose main advantage is only guarded refresh or runtime continuity remain **runtime continuity support**. Only rows that survive all these matched explanations and still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` may be promoted to packet-contract language; only rows that additionally preserve `A^{shell}` may support NtM handoff claims.

This means D06 should still resist over-promotion even when a variant simultaneously benefits from better world priors, cleaner semantic completion, and smoother refresh behavior. Such a row may still be fully explainable by upstream abstraction quality and uncertainty reduction rather than by a stronger reusable packet interface. The packet-first headline remains reserved for residual evidence that survives all these subtractions at actual controller-use time.

### 4.2.26 Planner-Side Active-Perception Family Match under the Current Local Anchor Set

LMPath, StereoNav, WildOS, and AgentVLN jointly suggest that some of the strongest recent aerial-VLN gains may come from a deceptively simple route: the system becomes better at deciding whether it should spend **one more look** before committing the next packet. LMPath contributes language-mediated uncertainty reduction, StereoNav contributes geometry-grounded verification utility, WildOS contributes frontier-search-driven semantic recheck value, and AgentVLN contributes modular skill-routing for sensing choices. In our experiment contract, these gains should be logged as an **active-perception family** rather than silently merged into packet survival.

We therefore require any row whose gain depends on extra sensing, short verification motion, hover-and-check behavior, or ambiguity-aware commitment delay to report: `Active-Perception Family Match`, `Q^{unc}_{plan}`, `One-More-Look Gain`, `Sensing-Cost Penalty`, `Hover-Risk Penalty`, and `Active-Perception-Only Explanation Remaining`. If the observed gain disappears after conditioning on these fields, the row must freeze at **active-perception support**. Only if a residual remains and later survives delayed consumption with preserved `A^{dir}`, `A^{ctx}`, and `A^{guard}` may the row be promoted further.

### 4.2.27 Packet-Promotion Eligibility after Active Perception, World Priors, and Semantic Completion

To unify the newer families with the older ladder, we recommend the following reviewer-facing order for late-window D06 rows:
\[
Q^{reason}_{route} \rightarrow (Q^{lang}_{narrow}, Q^{geo}_{narrow}, \tau_{search}) \rightarrow Q^{unc}_{plan} \rightarrow (Q^{world}_{prior}, Q^{comp}_{sem}) \rightarrow \tau_{latent} \rightarrow \tau_{runtime} \rightarrow (A^{dir}, A^{ctx}, A^{guard}) \rightarrow A^{shell}.
\]
A row may only be promoted to the next stage if the earlier family-matched explanation no longer exhausts the gain. This gives D06 one clean answer to a reviewer's hardest question: after subtracting planner modularity, search narrowing, one-more-look active perception, world priors, semantic completion, compact latent execution, and runtime continuity, **is there still packet-level residual evidence at actual consume time?**

If not, the result should stop at the earliest honest ceiling. If yes, and only then, D06 may promote the row to packet-contract language; `A^{shell}` still decides whether that packet survives strongly enough to support full NtM handoff claims.

### 4.2.28 Mid-Level-and-Shell/Data Unified Promotion Schema

The re-read of **AwareVLN** and **Fly0** makes one mid-level risk explicit: D06 may appear stronger simply because it (i) escalates stages more cautiously, or (ii) hands geometric realization to a cleaner downstream planner after semantic grounding. Both are useful, but neither is equivalent to proving that a reusable packet stayed honest until delayed controller consumption. We therefore freeze a dedicated mid-level ladder before any packet-facing claim is allowed.

Concretely, rows matched by **AwareVLN** are first evaluated as **progress-aware planner support**: their gains may explain lower wrong-escalation rates, more stable `search → approach` transitions, and better alignment between progress state and verifier evidence. Rows matched by **Fly0** are first evaluated as **semantic-geometric decoupling support**: their gains may explain lower oscillation after grounding, cleaner separation between target interpretation and local trajectory realization, and stronger zero-shot execution stability. But unless the same row still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` after subtracting these mid-level routes, it must not be promoted to packet-contract language; `A^{shell}` remains the final gate for NtM handoff claims.

Operationally, the reviewer-facing reading order becomes: `Q^{reason}_{route} → (Q^{lang}_{narrow}, Q^{geo}_{narrow}, τ_{search}) → Q^{unc}_{plan} → Q^{data}_{prior} → τ_{latent} → Q^{shell}_{local} → (AwareVLN-style progress-aware support, Fly0-style semantic-geometric support) → τ_{runtime} → (A^{dir}, A^{ctx}, A^{guard}) → A^{shell}`. This ordering matters because it prevents D06 from mistaking **better stage discipline** or **cleaner semantic-geometric decomposition** for genuine evidence that a packet survived refresh, recommit, and delayed use more honestly.

### 4.2.26 Submission-Ready Logging Contract for Mid-Level Family Matching

To make the above ladder executable, D06 needs a submission-ready logging schema that aligns experiments with the new mid-level anchors. We therefore require any row potentially explained by AwareVLN or Fly0 to record: `Progress-Aware Match | Wrong-Escalation Penalty | Stage-Confidence Consistency | Progress-Only Explanation Remaining | Semantic-Geometric Decoupling Match | Q^{dec}_{sg} | Oscillation Reduction after Grounding | Decoupling-Only Explanation Remaining | Last Surviving Family after Subtraction | Promotion Ceiling | Promotion Blocker | Weakest Honest Claim`.

These fields answer a concrete paper-writing question: after reasoning, search, active-perception, data, latent-control, and local-shell subtraction have been applied, is the remaining gain still fully explained by **better progress-aware stage control** or **better semantic-geometric decomposition**? If yes, the row must freeze there and cannot borrow stronger language from later consume-time metrics. Only rows whose residual survives the full mid-level subtraction and still closes `A^{dir}`, `A^{ctx}`, and `A^{guard}` at `w^{\dagger}_{consume}` may be promoted to packet-contract language.

### 4.2.27 Current Evidence-Consistent Freeze after Mid-Level Family Alignment

Under the current D06 anchor set, the most honest freeze remains conservative even after adding AwareVLN and Fly0. Rows primarily explained by `Q^{reason}_{route}` remain **reasoning-route support**. Rows exhausted by `Q^{lang}_{narrow}`, `Q^{geo}_{narrow}`, or WildOS-style outdoor-search subtraction remain **search-prior support**. Rows exhausted by `Q^{unc}_{plan}` remain **active-perception support**. Rows exhausted by `Q^{data}_{prior}` remain **pretraining-support only**. Rows matched by AerialVLA-style compact control remain **latent execution sufficiency**. Rows matched by KIO-style local shells remain **execution-shell support**. Rows exhausted by AwareVLN-style stage discipline remain **progress-aware planner support**. Rows exhausted by Fly0-style role separation remain **semantic-geometric decoupling support**. Rows whose main residual advantage is only guarded refresh or continuity remain **runtime continuity support**.

Only the residual that survives all of these matched explanations and still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` may be promoted to packet-contract language; only rows that additionally preserve `A^{shell}` may support NtM handoff claims. This freeze is intentionally strict. A row that both escalates more cautiously and flies more smoothly after grounding may still be fully explained by mid-level planner discipline and semantic-geometric decomposition. Such a row does not yet earn a packet-first headline.

### 4.2.29 Direction-Conditioned Recommit Audit must be Closed before Packet Promotion

LMPath-, StereoNav-, WildOS-, and AgentVLN-style gains often improve the *decision to look again* rather than the truthfulness of the same packet after that extra look. D06 therefore needs an explicit recommit audit that separates **better planner-side re-observation policy** from **better post-look packet survival**. We require every row that benefits from one-more-look behavior to log `Post-Look Direction Retention`, `Post-Look Context-Thread Retention`, `Refresh-to-Commit Delay`, `Recommit Drift after One-More-Look`, and `Packet-Survival after Active-Perception Recommit` before any packet-facing promotion is allowed.

These fields answer a concrete deployment question: after a planner-side recheck, did the system preserve the *same* directional clause and context thread, or did it quietly swap to a nearby but different hypothesis and then claim success under a stronger packet story? If the gain is still honestly exhausted by better re-observation timing, lower ambiguity, or cheaper planner-side recommitment, the row must freeze at **active-perception support**. Only rows whose refreshed packet still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` after the post-look recommit may continue to packet-contract language; `A^{shell}` remains the final gate for NtM handoff claims.

### 4.2.30 Current Evidence-Consistent Freeze after Re-reading LMPath / StereoNav / AwareVLN / Fly0 / FlyMirage

Under the current local anchor set, the most honest family-matched freeze is now sharply stratified. **LMPath** is best treated as **language-mediated search-prior support**, because its main gain is earlier target-zone narrowing from environmental semantics rather than consume-time packet preservation. **StereoNav** is best treated as **geometry-grounded anchoring support**, because its main gain is lower cross-view target drift and stabler partial-target attachment before delayed use. **AwareVLN** is best treated as **progress-aware planner support**, because its main gain is cleaner stage discipline, lower wrong-escalation rates, and better alignment between progress state and verifier evidence. **Fly0** is best treated as **semantic-geometric decoupling support**, because its gain is largely explained by cleaner separation between target grounding and geometric realization, with lower oscillation after grounding. **FlyMirage** is best treated as **synthetic data-scaling support**, because its main value is richer data coverage and stronger pretraining priors rather than stronger packet honesty.

This freeze is deliberately conservative. A D06 row may look impressive because it searches better, anchors better, escalates more cautiously, flies more smoothly after grounding, or benefits from richer synthetic aerial corpora. Those are all real gains, but none is yet packet superiority by default. Unless a residual still remains after all five matched explanations have been subtracted—and unless that residual still preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`—the row must remain below packet-contract language. Only rows that additionally preserve `A^{shell}` may support full NtM handoff claims. In other words, D06 gets stronger here not by claiming more, but by stating more clearly which weaker explanation has already been ruled out and which one has not.

## 5. Conclusion

We present a packet-centric aerial VLN framework that reframes aerial navigation as a deployable interface problem rather than only a waypoint prediction problem. By combining 3D semantic frontier mapping, dynamics-aware exploration, and a Navigate-then-Manipulate handoff architecture, the framework exposes where language grounding, runtime continuity, delayed controller consumption, and local interaction readiness truly succeed or fail. More importantly, the paper argues for a stricter evidence discipline: planner-time gains, runtime continuity gains, latent execution sufficiency, and full packet-contract preservation should not be conflated. This framing gives D06 a clearer path toward honest evaluation and, eventually, a stronger aerial embodied intelligence system.

### 4.2.28 Mid-Level-and-Shell/Data Unified Promotion Schema

Recent local anchors show that D06 now has four strong non-packet explanations that may all produce convincing gains before full consume-time packet accountability is closed: **AwareVLN-style progress-aware stage control**, **Fly0-style semantic-geometric decoupling**, **KIO-planner-style local execution shells**, and **FlyMirage-style synthetic-data scaling**. If these routes are logged separately in related work but not jointly subtracted in experiments, a row can still be rhetorically over-promoted from "better stage discipline / smoother execution / safer near-field shell / richer training prior" into an inflated packet-contract story. We therefore require a unified promotion schema that keeps all four families on the same evidential ladder.

Concretely, every D06 row potentially explained by these families must expose at least the following fields before any late-window promotion is allowed: `Progress-Aware Match`, `Wrong-Escalation Penalty`, `Stage-Confidence Consistency`, `Progress-Only Explanation Remaining`, `Semantic-Geometric Decoupling Match`, `Q^{dec}_{sg}`, `Oscillation Reduction after Grounding`, `Decoupling-Only Explanation Remaining`, `Local-Shell Family Match`, `Q^{shell}_{local}`, `Shell-Only Explanation Remaining`, `Synthetic-Data Family Match`, `Q^{data}_{prior}`, `Data-Only Explanation Remaining`, `Last Surviving Family after Subtraction`, `Promotion Ceiling`, `Promotion Blocker`, and `Weakest Honest Claim`. These fields force the paper to answer a stricter question than ordinary aerial VLN reporting: after subtracting progress-aware planning, semantic-geometric role separation, local execution-shell support, and synthetic-data prior support, **is there still packet-facing residual evidence at the actual consume-time boundary?**

This schema also fixes the reading order for the current D06 mid-level regime. A row that is still fully explained by better stage discipline freezes at **progress-aware planner support**. A row that survives that check but is exhausted by cleaner semantic-geometric separation freezes at **semantic-geometric decoupling support**. A row whose remaining gain is still fully explained by a stronger KIO-style near-field shell freezes at **execution-shell support**. A row whose remaining gain is still explained by richer FlyMirage-style pretraining or coverage freezes at **pretraining-support only**. Only rows that survive all four family matches and still preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}` may be promoted to packet-contract language; `A^{shell}` remains the final gate for NtM handoff claims.

### 4.2.29 Current Evidence-Consistent Freeze after Mid-Level + Shell/Data Alignment

Under the current anchor set, the most evidence-consistent freeze remains conservative. Gains dominated by AwareVLN-style self-awareness should be reported as **progress-aware planner support**; gains dominated by Fly0-style grounding/execution role separation should be reported as **semantic-geometric decoupling support**; gains dominated by KIO-planner-style near-field safety and executability should be reported as **execution-shell support**; gains dominated by FlyMirage-style data diversity and pretraining coverage should be reported as **pretraining-support only**. These explanations are all valuable, but none of them by itself proves that the reusable packet survives refresh episodes and delayed controller consumption more honestly.

This matters because D06 is now strong enough to produce many superficially impressive rows without yet proving packet superiority. A variant may escalate stages more carefully, oscillate less after grounding, fly more safely through clutter, or generalize better because it saw richer synthetic trajectories. Such rows deserve credit—but only at the family-matched level that exhausts the evidence. The headline may be promoted to packet-contract language only when a residual still remains after these four explanations are subtracted and the row continues to preserve `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`; only rows that additionally preserve `A^{shell}` may support NtM handoff preservation.

## References

[TODO: complete bibliography with aligned arXiv ids and venue metadata]
