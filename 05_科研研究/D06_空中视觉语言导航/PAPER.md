# Aerial Vision-Language Navigation with 3D Semantic Frontier Mapping and Dynamics-Aware Exploration

> 方向：D06 空中视觉语言导航 | 目标会议：ICRA 2027 | 状态：🟡 成形
> 最后更新：2026-05-17

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

2. **C2: Dynamics-Aware Navigation Policy**: We explicitly model UAV energy, velocity, and safety constraints within the frontier selection and path planning process, treating dynamics constraints as part of the exploration cost function to eliminate infeasible candidate paths.

3. **C3: Navigate-then-Manipulate (NtM) Architecture**: We design a unified architecture that seamlessly transitions from navigation mode to manipulation mode when the target enters the operational range, with closed-loop recovery enabling re-navigation upon manipulation failure.

4. **C4: Aerial VLN Benchmark**: We construct an evaluation benchmark covering indoor and outdoor aerial VLN scenarios with dynamics-aware metrics, providing the first systematic evaluation of aerial VLN with 3D spatial reasoning.

---

## 2. Related Work

### 2.1 Ground Vision-Language Navigation

Ground VLN has established strong baselines for language-guided exploration. VLFM [REF: ] uses VLM semantic relevance to guide 2D frontier exploration, demonstrating that language-conditioned frontier selection significantly outperforms geometric-only exploration. NaVILA [REF: ] adopts a hierarchical VLA design with high-level VLM reasoning and low-level action execution. ApexNav [REF: ] introduces adaptive semantic-geometric exploration balancing exploration and exploitation. SG-Nav [REF: ] uses scene graph representations for structured navigation reasoning. DRIVE-Nav [REF: ] enhances spatial reasoning through directional inference. These methods collectively demonstrate the value of semantic frontier maps but are fundamentally limited to 2D planar motion and cannot handle aerial dynamics.

### 2.2 Aerial Navigation Systems

OnFly [REF: ] introduces a dual-agent UAV navigation system with decoupled perception and control frequencies, the closest existing work to aerial VLN. OpenFly [REF: 2502.18041] provides a comprehensive aerial VLN platform combining UE/GTA V/Google Earth/3DGS rendering sources, automatic trajectory and instruction generation, and a keyframe-aware VLA model, serving as our primary data infrastructure reference. AirNav [REF: 2601.03707] presents the first real-world urban aerial VLN benchmark with AirVLN-R1 (SFT + RLFT training recipe), directly addressing the real-data evaluation gap. APEX [REF: 2602.00551] proposes Dynamic Spatio-Semantic Mapping with RL-based action decisions and target-guided exploration, providing an interpretable modular explorer suitable as an engineering reference for our GoalSearch component. Fly0 [REF: 2602.15875] explicitly decouples semantic grounding from geometric trajectory planning in three stages, demonstrating zero-shot, low-latency navigation with geometric robustness after visual loss. FineCog-Nav [REF: 2604.16298] introduces fine-grained cognitive modularization for zero-shot UAV VLN, decomposing language processing, perception, attention, memory, imagination, reasoning, and decision into role-specific modules with the AerialVLN-Fine benchmark for sentence-level instruction-trajectory alignment. SpatialFly [REF: 2603.21046] represents a complementary geometry-first line: rather than constructing an explicit 3D frontier map, it injects geometric priors into 2D semantic tokens and aligns them with 3D structural cues, showing that representation-level geometry alignment can improve unseen-scene path alignment and motion smoothness even without full volumetric reconstruction.

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

### 2.9 Live Packet Refresh under Streaming Outdoor Observations

A second under-explained gap in current aerial VLN systems is that **outdoor search improvements and online refresh improvements are often reported separately**, even though deployment-time failures usually appear exactly at their intersection. WildOS-style frontier systems show that better long-range region discovery can stabilize where the robot searches, while LiveVLN- and OnFly-style runtimes show that better guarded execution can stabilize when the robot refreshes action commitments. However, current literature still provides weak evidence on whether a packet that was improved by outdoor search remains semantically and structurally valid after multiple refresh cycles under streaming observations.

This matters directly for aerial deployment because packet decay is rarely a one-shot failure. A packet may be frontier-correct at proposal time, remain verifier-compatible for one short horizon, yet still lose direction-conditioned clause fidelity or manipulation-shell validity after several refreshes triggered by viewpoint change, wind-induced drift, or target re-identification. We therefore treat **live packet refresh under streaming outdoor observations** as a distinct evidence route bridging outdoor search and consume-time packet accountability. Gains from this route are only allowed to explain stronger D06 claims when they preserve packet fields not just once, but across refresh episodes that occur before controller consumption.

### 2.8 Limitations of Existing Work

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

Concretely, we define a **refresh-stable packet gate**
\[
G_{\text{refresh}} = \mathbb{1}\Big[ \prod_{k=1}^{K} A^{dir}_{(k)} A^{ctx}_{(k)} A^{guard}_{(k)} = 1 \Big]
\]
for packet-contract promotion, and a stricter handoff gate
\[
G_{\text{NtM}} = \mathbb{1}\Big[ \prod_{k=1}^{K} A^{dir}_{(k)} A^{ctx}_{(k)} A^{guard}_{(k)} A^{shell}_{(k)} = 1 \Big]
\]
for manipulation-ready claims. Under this design, a method may benefit from WildOS-style outdoor narrowing or LiveVLN-style runtime continuity, but it still cannot be promoted to packet-contract or NtM language unless the packet survives refresh episodes all the way to consume time.

---

## 4. Experiments

### 4.1 Setup

We evaluate on indoor and outdoor aerial VLN settings with matched sensing, latency, and controller budgets. Core metrics include navigation success, verifier pass rate, packet staleness, context retention, packet handoff failure, and manipulation-ready promotion rate.

### 4.2 Main Results

Our main-result philosophy is conservative: a late-window gain is only allowed to support the strongest claim whose evidence route is fully closed at controller-consumption time.

### 4.2.1 Consume-Time Contract Table with Unified-Reasoning and Latent-Execution Freezes

We use a main comparison table of the form:

`Method | w+ | w†bind | w†consume | Freshness Regime | Route Tag | A^{dir} | A^{ctx} | A^{shell} | A^{guard} | ΔSR | ΔMRP | ΔCCR | ΔPKR | Weakest Honest Claim | Unified-Reasoning Freeze | AerialVLA Freeze`

This schema intentionally forces a field-level reading before any headline interpretation. A method that improves aggregate success but loses `A^{shell}` at the late boundary should not be described as preserving NtM handoff value.

### 4.2.2 Boundary-Time Reading Rule for the Weakest Honest Claim

The reviewer-facing order is: (1) locate `w+`; (2) check survival to `w†bind`; (3) check survival to `w†consume`; (4) inspect `A^{dir}/A^{ctx}/A^{shell}/A^{guard}` at boundary time; and (5) route the row to the strongest matched explanation family that still remains honest. D06 should prefer the weakest claim that exhausts the evidence rather than the strongest claim that sounds plausible.

### 4.2.3 Minimal Experiment Logging Fields for Contract-Survival Audits

We formalize the minimum D06 experiment record as
\[
\Lambda_{D06}=(w^+, w^{\dagger}_{bind}, w^{\dagger}_{consume}, A^{dir}, A^{ctx}, A^{shell}, A^{guard}, \rho_{dc}(\delta), \tau_{route}, \tau_{claim}).
\]
This tuple is mandatory rather than illustrative. Missing consume-time fields or an unlogged delayed-consumption regime automatically freeze the evidence below full packet-contract superiority.

### 4.2.4 Route-Closure Main Table Columns for Consume-Time Promotion Discipline

To make the route-closure rule operational at reporting time, the D06 main table must expose not only task outcomes but also the **promotion contract** that justifies each late-window claim. We therefore extend the main result schema with five reviewer-facing columns: **Family-Matched Comparator**, **Closure Level**, **Promotion Ceiling**, **Promotion Blocker**, and **Last Honest Consume Window**. The first column records which nearby baseline family is the fairest explanatory counterfactual—e.g., AerialVLA for latent execution sufficiency, OnFly/LiveVLN for runtime continuity, HTNav/Unified Aerial VLN for planner-time structured reasoning. The second column records the strongest route actually closed by the available evidence. The third column states the strongest claim the row is allowed to support. The fourth column records the first missing evidence item that prevents further promotion. The fifth records whether honesty survives only to planner time, verifier bind, or true controller consumption.

This extension matters because many positive late-window outcomes are still underdetermined without an explicit promotion contract. A gain that beats a planner-structure baseline but loses `A^{shell}` at consume time should stay frozen below a full packet-contract claim even if aggregate success improves. A gain that beats a runtime baseline only through `A^{guard}` survival and bounded lag robustness still supports a continuity story, not a handoff-accountability story. By forcing every row to name its matched comparator family and closure level, the table prevents us from stitching unrelated gains into one oversized packet-first narrative.

We therefore recommend the following canonical column order for D06 main results: `Method | w+ | w†bind | w†consume | Freshness Regime | Family-Matched Comparator | Closure Level | A^{dir} | A^{ctx} | A^{shell} | A^{guard} | ΔSR | ΔMRP | ΔCCR | ΔPKR | Promotion Ceiling | Promotion Blocker | Weakest Honest Claim`. Under this contract, *Promotion Ceiling* is determined before prose is written. If the ceiling remains `planner-time reasoning gain`, the paragraph must not drift into consume-time handoff language. If the ceiling remains `runtime continuity gain`, the result must not be presented as packet-contract superiority. Only rows whose closure level reaches full consume-time packet preservation may support an NtM handoff headline.

### 4.2.5 Claim-Freezing Paragraph Template under Promotion Blockers

The result paragraph itself should mirror the table contract rather than reinterpret it. We therefore define a minimal paragraph template: **(i)** name the matched comparator family, **(ii)** state the earliest positive window and last honest consume window, **(iii)** report the surviving packet fields, **(iv)** state the promotion blocker, and **(v)** stop at the weakest honest claim. This template ensures that a row blocked by shell-validity loss cannot be rhetorically upgraded by stronger nearby metrics such as success rate or verifier pass rate.

Concretely, a D06 paragraph should read in the following order: *Compared with the family-matched baseline X, the proposed method first becomes positive at `w+`, remains honest through `w†consume`, preserves `{A^{dir}, A^{ctx}, ...}`, but is blocked from stronger promotion by `Promotion Blocker`; therefore the strongest supported interpretation is `Weakest Honest Claim`.* This fixed order matters because late-window aerial VLN gains are often tempting to narrate from the headline backward. Our contract instead forces prose to flow from evidence boundary to narrative ceiling.

The benefit is not only rhetorical hygiene. It also turns D06 into a submission where experiments, tables, and result text all share the same claim grammar. If a future ablation improves packet freshness but still loses `A^{shell}`, the prose automatically freezes at continuity or planner-side gain. If a route-closure upgrade removes the blocker and preserves all four consume-time fields through `approach → manipulate-ready`, then the paragraph is finally allowed to promote the result to full packet-contract or NtM handoff language.

### 4.2.6 Experiment-Contract Alignment as a Reporting Primitive

A final lesson from the recent local baseline cluster is that D06 should treat **experiment-contract alignment** itself as a primary reporting primitive rather than an afterthought. AerialVLA, OnFly, HTNav, LiveVLN, and Unified Aerial VLN each illuminate different gain routes, but none forces logs, tables, and prose to agree on one promotion contract. Our paper should therefore make this alignment part of the method-evaluation interface: a late-window improvement is incomplete unless it comes with the route identity, closure level, blocker, and claim ceiling needed to report it honestly.

Under this rule, D06 does not merely claim better aerial VLN performance; it claims a better **evidence discipline** for deciding what kind of aerial VLN improvement has actually been achieved. This is especially important for the `approach → manipulate-ready` boundary, where planner-side reasoning gains, latent control sufficiency, runtime continuity, and shell-level rescue can all look superficially similar.

### 4.2.7 Outdoor-Search Matched Negative-Control Logging Contract

WildOS-style outdoor search gains are useful for D06 only when they are reported as **matched negative controls** rather than silently merged into the packet-first story. For every result whose dominant gain may be explained by open-vocabulary target search, the experiment record should therefore add four reviewer-facing fields: **Negative-Control Family**, **Search-Only Win Window**, **Packet-Field Survival after Search Conditioning**, and **Promotion Blocker after Search Conditioning**. These fields make the reader ask a harder question than raw outdoor success: after subtracting the WildOS-like frontier-search route, what packet evidence still survives?

This contract matters because an outdoor row may achieve better region discovery or boundary-node exploration while still providing no evidence that the language-conditioned packet remained stable at controller-consumption time. If the gain disappears after conditioning on the negative-control family, the row must remain frozen as **search-route improvement only**. If the gain survives and preserves `A^{dir}`, `A^{ctx}`, and `A^{guard}` through `w^{\dagger}_{consume}`, it may be promoted to packet-contract language. Only rows that also preserve `A^{shell}` may support manipulation-ready handoff claims. In this way, WildOS stops being merely a cautionary citation and becomes a hard reporting gate for outdoor D06 claims.

### 4.2.8 Refresh-Episode Survival Audit for Streaming Outdoor Execution

To evaluate whether outdoor-search gains survive real execution rather than only proposal time, we add a **refresh-episode survival audit** between the search-only route and the final consume-time promotion decision. For each packet that enters a narrowed target zone, we log the number of refresh episodes before controller consumption, the first refresh that breaks a packet field, and whether the break is repaired before `w^{\dagger}_{consume}`. This yields three practical fields for the D06 result table: **Refresh Count before Consume**, **First Refresh Violation Type**, and **Refresh-Repaired before Consume**.

The audit is necessary because streaming outdoor execution often creates a deceptive pattern: a method wins the search route, stays positive through one verifier bind, and then loses packet identity after two or three observation-driven refreshes. Without refresh-episode accounting, such a row may still look like packet-contract progress even though its gain is only region-level. Under our protocol, only methods whose packet fields survive repeated refresh episodes are allowed to upgrade from `search-route improvement` to `refresh-stable packet-contract gain`; only those that additionally preserve `A^{shell}` across refresh episodes may support `manipulation-ready handoff` language.

### 4.2.9 Current Evidence-Consistent Freeze after Outdoor Search Negative-Control Alignment

Under the current evidence base, D06 should freeze any WildOS-adjacent improvement below a full packet-contract headline unless it is simultaneously **family-matched**, **consume-time closed**, and **negative-control subtracted**. In practical writing terms, this means that an outdoor success-rate jump without explicit consume-time packet survival should still be narrated as `frontier-search improvement`, `region-discovery stability gain`, or at most `search-assisted packet support`, rather than as `direction-aware handoff preservation` or `manipulation-ready packet superiority`.

This freeze is useful because it keeps D06 aligned with its own evidence discipline: the paper is not trying to prove that every stronger outdoor navigation result automatically supports the packet-centric thesis. It is trying to prove that **when an outdoor gain survives matched negative-control subtraction and still preserves packet fields at consume time, then—and only then—does it count as evidence for the packet-centric aerial VLN interface**.

### 4.2.10 Search-to-Refresh Upgrade Discipline under Streaming Outdoor Evidence

Outdoor aerial VLN rows often improve in two temporally different ways: they first become better at *finding the correct target region*, and only later may or may not become better at *preserving a controller-consumable packet*. We therefore add a **search-to-refresh upgrade discipline** that explicitly separates these two stages. Let `R_search` denote evidence that the method improves target-zone discovery or open-vocabulary region narrowing, and let `R_refresh` denote evidence that the packet survives one or more refresh episodes with the same directional clause, context anchor, and guarded execution semantics. A result may be promoted from `search-assisted packet support` to `refresh-stable packet-contract gain` only when `R_search` remains positive *after* refresh-episode accounting and when the surviving packet fields are still visible at `w^{\dagger}_{consume}`.

This discipline prevents a common overclaiming pattern in outdoor aerial systems: a row wins because it searches better, then inherits stronger language as if it also refreshed better. In D06, these are separate privileges. Search-route superiority only shows that the system reaches the right semantic neighborhood more reliably. Refresh-stable packet superiority requires the stronger statement that the packet still preserves directional intent and controller-facing structure after streaming observations have repeatedly revised the proposal. Only when both conditions hold should the row be allowed to move above the negative-control ceiling set by WildOS-style frontier search.

### 4.2.11 Minimal Main-Table Columns for Search-to-Refresh Closure

To operationalize this reporting rule, we extend the D06 main results with four compact columns: **Search Route Win**, **Refresh-Stable Until**, **Search-Subtracted Claim Ceiling**, and **First Unrepaired Refresh Violation**. `Search Route Win` records whether the row still outperforms its family-matched outdoor-search negative control after aligning for region-discovery competence. `Refresh-Stable Until` records the last refresh episode before which `A^{dir}`, `A^{ctx}`, and `A^{guard}` remain intact. `Search-Subtracted Claim Ceiling` states the strongest claim allowed after outdoor-search explanations have been subtracted. `First Unrepaired Refresh Violation` records the first refresh-time failure that survives to consume time without repair.

These columns are intentionally narrow. They do not add another metric buffet; they add just enough structure to keep the paper honest about *what kind* of improvement has actually been achieved. If a row has `Search Route Win = yes` but loses `A^{ctx}` after the second refresh episode, the result should remain a search-route improvement with weak packet support. If the row stays refresh-stable through `w^{\dagger}_{consume}` but loses `A^{shell}`, it may support packet-contract language but not manipulation-ready handoff claims. This is the precise reporting bridge D06 needs between WildOS-style outdoor search competence and the packet-centric aerial VLN interface thesis.

### 4.2.12 Evidence-Consistent Freeze for the Current D06 Storyline

Given the current local evidence cluster, the most defensible D06 storyline is still that packet-centric aerial VLN should be judged by **search-to-consume continuity**, not by search success alone. WildOS-family results justify why outdoor target-zone narrowing matters. OnFly and LiveVLN justify why runtime continuity and guarded execution matter. LookasideVLN and FineCog-Nav justify why clause-level and direction-level instruction structure matter before execution. But none of these families alone closes the full route from outdoor search to manipulation-ready handoff.

Our current evidence-consistent freeze is therefore straightforward: D06 may claim that a packet-centric interface is necessary to connect these gains into one deployable contract, but it should not yet narrate any outdoor-search improvement as if the full packet contract has already been proven. Until matched negative-control subtraction, refresh-episode survival, and consume-time field preservation are all jointly satisfied, the paper should continue to phrase the strongest rows as **search-assisted packet support**, **runtime-stable packet continuity**, or **consume-time packet-contract gain**, reserving full NtM-handoff language only for rows that also preserve `A^{shell}` through the manipulate-ready boundary.

### 4.3 Delayed-Consumption Violation Taxonomy

We introduce a minimal **delayed-consumption violation taxonomy** with four violation types aligned with the packet contract fields: `V_dir` for directional-prior drift, `V_ctx` for context-anchor loss, `V_shell` for manipulation-shell collapse, and `V_guard` for guarded-prefix invalidation. This taxonomy is used to prevent planner-time wins from being over-promoted into full Navigate-then-Manipulate claims.

Each violation type maps to a distinct promotion blocker. `V_dir` indicates that clause-aware or direction-aware gains do not survive enough of the execution horizon to support any consume-time directional-control claim. `V_ctx` indicates that semantic anchors or memory-bound references decay before late-stage controller use, so the method may still support planner-time semantic reasoning but not handoff-accountable packet preservation. `V_shell` is the strongest blocker for NtM language: once the local manipulation shell collapses, the row must freeze below any manipulate-ready or handoff-stable claim, even if aggregate success remains high. `V_guard` captures failures where the guarded executable prefix no longer remains trustworthy under delay, refresh, or asynchronous monitoring, forcing the result to stay in a runtime-fragility reading.

To keep the taxonomy operational rather than descriptive, every main-table row should log the **first dominant violation**, the **window at which the violation first appears**, and whether the violation is repaired before `w^{\dagger}_{consume}`. This makes it possible to distinguish late-window rows that merely look better because they postpone failure from rows that actually restore packet validity before controller consumption. Under this rule, late-stage D06 gains are only allowed to upgrade when the dominant violation either disappears or is explicitly repaired in a route-consistent way.

### 4.4 Route-Closure Upgrade Protocol from Planner-Time Gains to NtM Handoff Claims

We further define a **minimal route-closure upgrade protocol** to decide when a result may be promoted across claim ceilings. A row begins at the weakest route justified by its earliest positive window `w+`. It may only upgrade when three conditions hold simultaneously: **(i)** the matched comparator family has been exhausted, meaning the gain can no longer be fully explained as planner-only structure, runtime continuity, geometry-only alignment, or recoverability-only preservation; **(ii)** the dominant delayed-consumption violation is either absent or demonstrably repaired before `w^{\dagger}_{consume}`; and **(iii)** the surviving packet fields at consume time are sufficient for the target ceiling. In practice, a planner-time structured-reasoning gain may be upgraded to runtime continuity only after guarded-prefix survival and latency-coupled execution remain intact. A runtime continuity gain may be upgraded to packet-contract preservation only after `A^{dir}`, `A^{ctx}`, and `A^{guard}` remain stable through controller consumption. A packet-contract claim may only be upgraded to NtM handoff language once `A^{shell}` also survives and the manipulate-ready boundary remains honest.

This protocol matters because D06 is explicitly trying to stop a common failure pattern in aerial VLN writing: a method becomes positive early, looks robust in aggregate, and then gets rhetorically promoted all the way to full deployment readiness without showing which closure step actually happened. Our protocol forces the order to remain `matched family → dominant violation → repaired window → surviving fields → claim ceiling`. If any step is missing, promotion stops immediately.

### 4.5 Ablation Study

To keep first-round results interpretable, we pre-register five mutually exclusive result routes. **Route A — frontier semantics bottleneck**: semantic proposal quality is weak. **Route B — packet deployability bottleneck**: semantic proposal quality is acceptable, but packets do not survive online refresh and controller consumption. **Route C — stage-handoff bottleneck**: search and approach metrics are strong, but failure concentrates around the `approach → manipulate-ready` boundary. **Route D — controller-shell bottleneck**: packet quality and verifier compatibility are high, yet final success still depends on downstream local stabilization. **Route E — recoverability bottleneck**: accepted packets collapse future correction options.

We evaluate the following ablations:
- **A1**: 2D frontier map vs. 3D volumetric frontier map
- **A2**: Without dynamics cost vs. with dynamics-aware frontier selection
- **A3**: Without direction prior vs. with direction-conditioned packet fields
- **A4**: Stop-and-go execution vs. live packet refresh with guarded prefix
- **A5**: Planner output as raw action list vs. Semantic Waypoint Packet interface
- **A6**: Geometry-guided representation alignment only vs. explicit packet-centric frontier pipeline
- **A7**: Frontier-score-only packet ranking vs. frontier + recovery-corridor-aware packet ranking
- **A8**: Refresh without retention gate vs. retention-guided refresh gating
- **A9**: Monolithic planner vs. fine-grained cognitive planner under a shared packet-verifier-controller chain
- **A10**: Monolithic planner vs. hierarchical planner under the same packet schema
- **A11**: Cloud-scale planner vs. onboard distilled planner under the same packet schema and latency budget
- **A12**: Latent memory usage without packet serialization vs. memory-conditioned packet fields explicitly exposed to verifier and controller

### 4.5 Minimal Packet-Level Sanity Checks

Before benchmark-scale comparison, we verify that packetization itself is useful rather than cosmetic. We test direction-conditioned waypoint improvement, live refresh stability under delayed observations, and planner-family fairness under a shared packet schema.

### 4.6 Runtime-Coupled Packet Diagnostics

We define runtime-coupled diagnostics that localize which part of the packet chain fails first under onboard execution pressure: semantic misgrounding, directional mismatch, packet staleness, handoff failure, and cross-stage drift.

---

## 5. Conclusion

We present a packet-centric aerial VLN framework that reframes aerial navigation as a deployable interface problem rather than only a waypoint prediction problem. By combining 3D semantic frontier mapping, dynamics-aware exploration, and a Navigate-then-Manipulate handoff architecture, the framework exposes where language grounding, runtime continuity, delayed controller consumption, and local interaction readiness truly succeed or fail. More importantly, the paper argues for a stricter evidence discipline: planner-time gains, runtime continuity gains, latent execution sufficiency, and full packet-contract preservation should not be conflated. This framing gives D06 a clearer path toward honest evaluation and, eventually, a stronger aerial embodied intelligence system.

## References

[TODO: complete bibliography with aligned arXiv ids and venue metadata]
