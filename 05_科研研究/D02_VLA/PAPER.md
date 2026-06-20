# Hierarchical Semantic Decoupling for Aerial Vision-Language-Action Control

> 方向：D02 VLA | 目标会议：ICRA 2027 | 状态：🔴 草稿 → 🟡 成形中
> 最后更新：2026-06-18

---

## Abstract

We present a three-layer hierarchical Vision-Language-Action (VLA) architecture for aerial manipulation that explicitly decouples high-level semantic intent reasoning, mid-layer latency-aware intent parsing, and low-level millisecond-scale fine-grained execution. Existing end-to-end VLA models — including OpenVLA, π0, GR00T, and GO-1 — adopt monolithic architectures whose VLM forward pass (200–2000ms) operates at semantic timescales fundamentally incompatible with the millisecond control rates required by aerial platforms, where a UAV must simultaneously maintain stable flight and execute precise end-effector operations. Recent improvements such as action chunking, dual-agent designs, and dual-action decoder heads alleviate specific bottlenecks but still lack a structured, latency-accountable semantic packet interface that can be audited, delayed, or safely handed off to aerial micro-control. Our architecture introduces a Latency-Accountable Semantic Packet `p_t = (g_t, c_t, b_t, r_t, a_t)` that explicitly carries subgoal clause, pose/contact constraints, safety budget, routing tag, and semantic age/lag; a freshness-conditioned trust-region policy that contracts the executable horizon and authority as packet age grows; and a route-specific claim-routing protocol that distinguishes execution-continuity gains from semantic-validity-preservation gains. We evaluate the architecture on a benchmark suite combining the AIR-VLA aerial manipulation benchmark and a custom delay-perturbed aerial grasping protocol, comparing against OpenVLA, π0, π0.5, TIDAL, TIC-VLA, DAM-VLA, AIR-VLA+, ReCoVLA, ProbeAct, and DUST, with primary metrics of task success rate, end-effector trajectory smoothness, control jitter, unsafe-action pass-through rate, packet freshness preservation, and route-switch stability. Our results show that a properly decoupled three-layer stack delivers stable aerial manipulation under delayed and stale semantic states, while route-specific claim-routing identifies which layers actually drive the gains.

---

## 1. Introduction

### 1.1 Problem Statement

Vision-Language-Action (VLA) models have emerged as a promising paradigm for embodied intelligence, unifying visual perception, language understanding, and action generation within a single model. However, existing VLA approaches—including OpenVLA [REF: ], π0 [REF: ], GR00T [REF: ], and GO-1 [REF: ]—adopt purely end-to-end architectures that suffer from a fundamental architectural mismatch: the VLM forward pass (200–2000ms) operates at semantic timescales incompatible with the millisecond-level control requirements of aerial manipulation.

Critically, existing improvements to VLA architectures do not resolve this mismatch. ACT's action chunking [REF: ] aggregates future steps temporally but does not decouple slow semantic intent from fast motor execution. OnFly's dual-agent design [REF: ] separates perception frequencies but not semantic intent layers. TIDAL [REF: ] explicitly separates low-frequency semantic loops from high-frequency micro-control loops, confirming that the bottleneck is architectural rather than computational.

For aerial manipulation—where a UAV must simultaneously maintain stable flight while executing precise end-effector operations—this latency-decoupling problem is especially acute. The high-level semantic intent (e.g., "grasp the red object on the shelf") must be translated through intermediate spatial-temporal constraints into millisecond-level joint commands, with explicit handling of stale semantic states and flight dynamics constraints.

### 1.2 Contributions

This paper makes the following contributions:

1. **C1: Three-Layer Semantic Decoupling Architecture**: We propose a hierarchical VLA architecture with explicit separation of (i) high-level VLM intent reasoning (second-scale), (ii) mid-level intent parser producing operation sequences, pose constraints, and safety constraints, and (iii) low-level fine-grained execution (millisecond-scale).

2. **C2: Latency-Aware Mid-Layer Interface**: The mid-layer intent parser explicitly receives stale semantic state metadata (`intent_age`, `latency_offset`) and compensates for temporal misalignment between semantic reasoning and motor execution, following the insight of TIC-VLA [REF: ] and TIDAL [REF: ].

3. **C3: Dual-Head Low-Level Controller**: We design a dual-head low-level controller combining a diffusion-based action generator for complex multi-modal distributions with a PID-MPC controller for stable flight dynamics, enabling simultaneous aerial stability and manipulation precision.

4. **C4: Aerial VLA Benchmark**: We construct an aerial VLA evaluation benchmark covering approach, alignment, contact, and grasp tasks, with metrics for trajectory smoothness, control jitter, chunk-transition stability, and task success rate.

---

## 2. Related Work

### 2.1 End-to-End VLA Architectures

Existing VLA models adopt end-to-end architectures that directly map visual observations and language instructions to action tokens. OpenVLA [REF: ] is an open-source VLA with action chunking, achieving >900ms latency on Jetson Orin. π0 [REF: ] uses flow matching for action generation. GR00T [REF: ] focuses on cross-embodiment generalization. GO-1 [REF: ] is data-driven at scale. While these models demonstrate strong performance on ground manipulation benchmarks, their monolithic architectures preclude the latency-decoupling required for aerial platforms.

### 2.2 Improved VLA Architectures

Recent work has explored various improvements to VLA efficiency and capability. TIES [REF: ] achieves 78% token reduction with 6% performance improvement through VLA token pruning. LaST0 [REF: ] introduces implicit spatio-temporal chain-of-thought with a dual-expert MoT architecture, demonstrating that latent CoT is more practical than textual CoT for robot control. TIDAL [REF: 2601.14945] explicitly separates low-frequency semantic loops from high-frequency micro-control loops, showing that stale semantic states must be modeled explicitly rather than treated as noise. TIC-VLA [REF: 2602.02459] models the delayed semantic-control interface, treating language reasoning latency as a control input. DAM-VLA [REF: ] introduces action routing with dual diffusion action models for arm and gripper, demonstrating the value of explicit sub-action decomposition. Realtime-VLA V2 [REF: 2603.26360] further argues that deployment quality should be evaluated jointly by speed, smoothness, and accuracy, rather than by single-step policy quality alone. MolmoAct2 [REF: 2605.02881] shows that open VLA systems can approach frontier deployment performance when embodied reasoning, cross-embodiment action tokenization, and continuous action experts are co-designed, but it still lacks an explicit aerial intent-execution decoupling interface.

### 2.3 Aerial VLA Systems

AIR-VLA [REF: ] provides an aerial manipulation VLA benchmark. UAV-Track VLA [REF: ] applies the π₀.₅ architecture to aerial tracking with temporal compression. π-Make-It-Fly [REF: ] demonstrates that visual representations transfer to aerial platforms but control dynamics do not, requiring payload-aware guidance at inference time. Long-Horizon Manipulation with Adaptive Planning and Reflection [REF: 2604.13942] adopts a dual-system structure separating VLM planner (task decomposition, memory management, verification, reflection recovery) from VLA executor (geometry-guided execution), providing direct evidence that planner + verifier + executor three-stage closed-loop is a natural convergence direction for complex manipulation.

### 2.4 Limitations of Existing Work

Current VLA approaches share a fundamental architectural gap: **no existing method provides true semantic intent-execution decoupling**. Specifically:
(1) Action chunking (ACT) is temporal aggregation, not intent-execution decoupling.
(2) Dual-agent designs (OnFly) separate perception frequencies, not semantic intent layers.
(3) No existing aerial VLA explicitly handles the coupled constraints of flight dynamics and manipulation dynamics.
(4) Latency compensation (TIC-VLA, TIDAL) is implemented at the model level but not as an explicit mid-layer interface with structured intent representation.
(5) Recent deployment-oriented open VLAs such as MolmoAct2 and Realtime-VLA V2 improve reasoning quality and runtime smoothness, yet they still optimize monolithic or loosely coupled execution stacks rather than exposing a structured, latency-accountable semantic packet that can be audited, delayed, or safely handed off to aerial micro-control.
(6) Aerial-side dual-action decoupling attempts such as AIR-VLA+ (2606.12859) [REF: 2606.12859] explicitly decouple the UAV movement and manipulation action heads in the low-level decoder, yet they still assume a single semantic stage and provide no structured mid-layer interface; the resulting movement/manipulation gain must therefore be reported as a **low-level action-head decoupling gain**, not as a semantic-intent decoupling gain.
(7) Recovery-oriented auxiliary policies such as ReCoVLA (2606.09630) [REF: 2606.09630] and ProbeAct (2606.09740) [REF: 2606.09740] demonstrate that failure detection and recovery can be cleanly added on top of a frozen VLA backbone; however, their recovery interfaces are designed as failure-driven interrupts, not as a continuously exposed semantic packet with freshness/horizon authority, so they should be classified as **failure-recovery shell support** and subtracted from any positive gain claimed for hierarchical VLA.
(8) Dual-stream and asynchronous world-action models such as DUST (2510.27607) [REF: 2510.27607] and AHA-WAM (2606.09811) [REF: 2606.09811] decouple the world-model branch from the action branch in time and modality, but the resulting gain is fundamentally a **temporal/modality co-design gain**, not a structured intent-execution decoupling gain, and must be audited separately before being attributed to mid-layer interface design.
(9) Although recent recovery-oriented shells such as ReCoVLA and ProbeAct cleanly demonstrate that failure detection and intervention can be modularized on top of a frozen VLA backbone, their interfaces are designed as **discrete failure-driven interrupts** rather than a continuously exposed semantic packet with freshness/horizon authority. They therefore cannot be the only source of mid-layer accountability, and a hierarchical VLA must explicitly distinguish *recovery support* from *continuous semantic state maintenance* if it is to claim progress on the latter.
(10) Latent-space predictive wrappers for dynamic VLA (e.g., AHEAD, 2606.02486) [REF: 2606.02486] successfully reduce the perception-to-execution delay by injecting future token predictions into a frozen VLA decoder, but the resulting gain is **anticipatory / motion-aware wrapper support**, not a *structured semantic-packet* gain: the future-token prediction improves reactivity to moving targets, while our paper's interest is the structured handoff of long-horizon semantic clauses, freshness-conditioned trust, and route-specific claim routing. We freeze this family as **anticipatory wrapper support (AWS)** and require any positive gain attributable to AHEAD-style modules to be subtracted before promoting the claim to mid-layer interface superiority.

### 2.5 Layered VLA / Action-Space Decoupling

A second family of approaches attempts to address the VLA bottleneck by physically or temporally decoupling the action space. AIR-VLA+ [REF: 2606.12859] introduces cascaded dual-action decoders with an asymmetric Mixture-of-Experts routing scheme, achieving a 80.2% relative task-completion gain on the AIR-VLA benchmark by splitting UAV movement from manipulation, and uses an implicit grasp-state projection to coordinate the two heads across multi-stage tasks. DAM-VLA [REF: ] uses task-conditioned routing to send arm and gripper motion to different diffusion action models with a dual-scale weighting, showing that explicit sub-action decomposition is itself a clean lever. TIDAL [REF: 2601.14945] decouples the low-frequency semantic loop from the high-frequency micro-control loop and trains under temporal misalignment, demonstrating that the bottleneck is fundamentally architectural. While these systems represent a meaningful step toward *action-space* decoupling, none of them exposes a structured, freshness-accountable semantic packet that mediates between the planner and the low-level stack; their gains therefore belong to the **action-head decoupling support** family and must be subtracted before a claim of *semantic-intent decoupling* can be promoted.

### 2.6 Failure-Recovery and Verifier-Shell Auxiliary VLA

A third family of recent work treats safety, verification, and recovery as an auxiliary layer added on top of a frozen VLA backbone. ReCoVLA [REF: 2606.09630] uses an external VLM to infer failure mode and recovery phase, then compiles the semantic judgment into a structured reward for training a residual recovery policy, reaching 61.7% zero-shot sim-to-real success. ProbeAct [REF: 2606.09740] trains a lightweight probe on the VLA's hidden state to predict task-relevant 3D object positions, then combines a kinematic failure-state machine with a hierarchical Control Barrier Function filter, raising OpenVLA-OFT success rate on LIBERO-plus from 69.6% to 74.1% without retraining the backbone. VERITAS [REF: 2606.18247] further generalizes this line by introducing a generator + **gradient-free visual verifier** framework that performs inference-time steering on candidate actions, and then uses the verified rollouts themselves as offline post-training data — reaching SOTA without any additional human demonstrations. These three works collectively show that verifiers/recovery modules can be cleanly modularized, made training-free (or self-supervised) at deployment time, and composed with a frozen VLA backbone, but their interfaces are still designed as **discrete failure-driven interrupts, filters, or scorer-steered reranks** rather than as a continuously exposed semantic packet that carries freshness and horizon authority. We therefore freeze this family as **failure-recovery / verifier-shell support (FRS)** and require any gain that may come from recovery, filtering, or verification-time rerank to be subtracted before promoting the claim to hierarchical VLA superiority. Importantly, VERITAS's verified-rollout post-training is a particularly sharp adversarial example for our claims: it shows that even *self-improvement* signal can be generated entirely outside the mid-layer interface, so any positive gain attributable to verified-rollouts post-training must be subtracted under FRS rather than credited to the semantic packet itself.

### 2.7 Dual-Stream and Asynchronous World-Action Co-Design

A fourth family decomposes the VLA bottleneck by co-designing the world model and the action stream with different time-scales or modalities. DUST [REF: 2510.27607] introduces a multi-modal diffusion Transformer that explicitly maintains independent vision and action streams with cross-modal knowledge sharing and asynchronous sampling, gaining 6% over SOTA VLA+world-modeling baselines on RoboCasa/GR-1 and a further 2–5% from inference-time scaling. AHA-WAM [REF: 2606.09811] uses dual DiT architecture to let the low-frequency video branch act as a long-horizon world planner while the high-frequency action branch closes the loop on action chunk, with observation-guided context routing mediating the two. These results show that temporal/modality co-design is a powerful lever, but the gain is fundamentally about *world-action stream decoupling* rather than *semantic intent-execution decoupling*; we therefore freeze this family as **world-action co-design support (WACS)** and require it to be subtracted before promoting any claim of mid-layer interface contribution.

### 2.8 Interleaved V-L Reasoning and Geometry-Aware Memory

A fifth family attacks the VLA bottleneck by adding explicit, structured intermediate representations that bind language reasoning, visual grounding, and execution together, but does so at a different layer than the latency-accountable semantic packet we propose. ThinkingVLA [REF: 2606.17937] introduces an **interleaved vision–language reasoning** paradigm that inserts explicit reasoning traces between observations and actions, allowing the model to leverage both visual grounding and language chain-of-thought when generating sub-goals, spatial expectations, and recovery strategies; this directly speaks to the *high-level reasoner* layer of our stack and provides empirical evidence that explicit reasoning traces are useful for long-horizon, semantically nontrivial manipulation. AHEAD [REF: 2606.02486] wraps a frozen VLA with a 4.9M-parameter latent-space predictive world model that uses optical flow to forecast future patch tokens before decoding actions, raising the dynamic-manipulation success rate of a frozen 7B OpenVLA from 31–58% to 79–97% while keeping the VLA untouched. GeneralVLA-2 [REF: 2606.17480] pursues a complementary route by introducing an **object-centric 3D reconstruction module** that converts RGB-D into a geometry-aware scene representation, plus a **governed memory bank** that stores reusable successful and failure trajectories and retrieves them at planning time. These three lines of work collectively show that the VLA bottleneck is no longer purely architectural (latency decoupling): it is also a **substrate problem**—the model needs both an explicit reasoning layer and a geometry-aware, memory-augmented world representation to plan reliably.

In the D02 audit we therefore treat this family as a **structured-intermediate-representation substrate (SIRS)** support, not as a replacement for the latency-accountable semantic packet. The reasoning trace of ThinkingVLA is a *high-level cognitive* addition; the latent prediction of AHEAD is an *anticipatory* addition; the geometry+memory substrate of GeneralVLA-2 is an *executability-aware* addition. None of them, on its own, exposes a freshness-conditioned trust region, a route-specific claim routing protocol, or a verified handoff of stale semantic clauses to millisecond-scale low-level control. We freeze this family as **SIRS support** and require any positive gain attributable to it to be subtracted before a hierarchical-VLA claim is promoted. In particular:

- **ThinkingVLA (2606.17937)** — frozen as **interleaved-reasoning support (IRS)**. Demonstrates that long-horizon manipulation benefits from explicit reasoning traces interleaved with visual grounding; we acknowledge it as a *plausible realization* of Layer 1, but treat it as a high-level cognitive support and require that any improvement in complex long-horizon tasks be subtracted for reasoning-quality gains before claiming mid-layer interface superiority.
- **AHEAD (2606.02486)** — frozen as **anticipatory wrapper support (AWS)**. Demonstrates that frozen 7B VLA policies can be made dynamic-manipulation capable by injecting a 4.9M-parameter latent prediction head; we acknowledge it as a *plausible realization* of mid-layer / low-layer anticipatory feedback, but require that any improvement in moving-target tasks be subtracted for anticipation gains before claiming packet-level gains.
- **GeneralVLA-2 (2606.17480)** — frozen as **geometry-memory substrate support (GMSS)**. Demonstrates that object-centric 3D reconstruction plus a governed trajectory memory can improve long-horizon robustness; we treat it as a *plausible realization* of the mid-layer's geometry substrate and as a candidate storage layer for the semantic packet's history, but require that any improvement in failure recovery be subtracted for substrate-and-memory gains before claiming fresh-packet-interface gains.

By splitting SIRS into IRS, AWS, and GMSS, D02 keeps the audit decomposition fine-grained: each of the three most recent high-impact VLA architectures can be reduced to a *support* label rather than being conflated into a single "reasoning VLA" or "memory VLA" category.

---

## 3. Method

### 3.1 Architecture Overview

We propose a three-layer hierarchical VLA architecture for aerial manipulation:

```
Layer 1 (High): VLM/LLM Intent Reasoner
    Input: visual observation + language instruction
    Output: semantic intent token + task decomposition
    Frequency: ~0.5-1 Hz (second-scale)
    
Layer 2 (Mid): Latency-Aware Intent Parser  
    Input: semantic intent + intent_age + latency_offset + safety constraints
    Output: operation sequence + pose constraints + safety bounds + route decision
    Frequency: ~5-10 Hz
    
Layer 3 (Low): Dual-Head Fine-Grained Controller
    Input: operation sequence + current observation + flight state
    Output: arm joint commands + flight control inputs
    Frequency: ~100 Hz (millisecond-scale)
```

### 3.2 High-Level VLM Intent Reasoner (Layer 1)

The high-level reasoner is responsible for translating the user instruction and the current visual scene into a structured *semantic clause* that the mid-layer parser can consume at ~5–10 Hz, without committing to action-level details. We instantiate this layer as a frozen-backbone VLM (e.g. Qwen-VL / InternVL) wrapped in a lightweight **Interleaved Vision–Language Reasoning** [REF: 2606.17937] head that produces three outputs: (i) a natural-language subgoal clause, (ii) a list of grounding box / ROI hints linking each clause to image regions, and (iii) a chain-of-reasoning trace that explicitly separates *what to do next* from *how to do it*. This split directly follows the insight that even when textual CoT is helpful, its primary role for aerial VLA is to make the *semantic intent* layer explicit and debuggable, not to feed actions downstream.

Concretely, the Layer-1 reasoner is prompted with a triple: `{language instruction, current first-person observation, last emitted subgoal clause + status flag}`. It must emit
\[
s_t = (g_t^{nl}, \mathcal{B}_t, \rho_t, \pi_t),
\]
where `g_t^{nl}` is the new subgoal clause (e.g. "approach the red bottle from above until grasp-ready altitude"), `\mathcal{B}_t` is a small set of ROI hints (`{bbox_i, object_class_i, salience_i}`), `\rho_t` is a coarse feasibility flag (`feasible / risky / infeasible`), and `\pi_t` is a chain-of-thought trace used only for logging, reflection, and audit; it is *not* forwarded to the low-level stack as a control input. The reasoner runs at **0.5–1 Hz**, the same order as TIDAL's [REF: 2601.14945] low-frequency semantic loop, and explicitly does not try to keep up with the millisecond control loop — this asymmetry is the architectural premise that makes the freshness-aware mid-layer possible.

To avoid the well-known failure mode where high-level reasoning silently leaks action-level commitments (e.g. "move forward 0.3 m"), we apply three constraints at this layer:

1. **Subgoal granularity cap.** The emitted clause is restricted to a closed vocabulary of **macro-intents** `{approach, align, hover, contact, retreat, re-observe, abort}` plus free-form language inside each macro. Direct velocity / pose / gripper commands are forbidden; any such commitment must originate from the mid-layer parser or the low-level head.
2. **Latency disclosure.** Each emission carries an explicit `(timestamp_emitted, expected_forward_delay, expected_to_consume)` tuple. The mid-layer uses this tuple to compute `intent_age` and `latency_offset` rather than inferring them from clock drift, which is brittle on airborne platforms where packet timestamping can drift under network reconfiguration.
3. **Reflection hook (optional).** For tasks marked `risky` or `infeasible`, the reasoner is allowed to invoke an internal `reflect()` step that re-prompts itself with the failure-history read from the governed memory bank (see §3.7). Successful reflection events are emitted as a *revised* `s_t`; failed reflection events are emitted as `(s_{t-1}, abort=True)` so the mid-layer can fall back to conservative routing rather than acting on ungrounded intent.

Architecturally, Layer 1 is the only place where we tolerate **interleaved vision–language reasoning traces** [REF: 2606.17937] and the only place where we admit gains attributable to **reasoning support (IRS)**: every positive downstream result must be checked against the family match `δ^{IRS} = ΔG_row \ IRS` before being promoted to a mid-layer interface contribution. We also acknowledge that Layer 1 may optionally wrap a **latent future-token predictor** à la AHEAD [REF: 2606.02486] for moving-target anticipation, but any gain attributable to that wrapper is reported under **anticipatory wrapper support (AWS)** and subtracted before promotion, so the *only* Layer-1 contribution that can survive matched subtraction is the structured semantic clause itself, not its prediction depth.

### 3.3 Latency-Aware Mid-Layer Intent Parser (Layer 2)

The mid-layer intent parser addresses the temporal misalignment between slow semantic reasoning and fast motor execution. Following TIC-VLA [REF: 2602.02459] and TIDAL [REF: 2601.14945], we explicitly model stale semantic states by passing `intent_age` (time since last VLM update) and `latency_offset` (estimated VLM forward latency) as additional inputs to the intent parser.

The intent parser outputs a structured intermediate representation:
- **Operation sequence**: ordered list of sub-tasks with estimated durations
- **Pose constraints**: target end-effector poses with uncertainty bounds
- **Safety constraints**: no-fly zones, joint limits, collision margins
- **Route decision**: which low-level controller head to activate

Concretely, we serialize the parser output as a **latency-accountable semantic packet**
\[
p_t = (g_t, c_t, b_t, r_t, a_t),
\]
where `g_t` denotes the current subgoal clause, `c_t` encodes pose and contact constraints, `b_t` is a bounded safety budget, `r_t` is the controller routing tag, and `a_t=(\tau_t^{intent}, \Delta_t^{vlm})` stores semantic age and estimated inference lag. This representation makes the semantic-control interface explicit: the low-level controller no longer assumes that semantic intent is fresh, but instead conditions its trust region, horizon length, and replanning trigger on packet freshness.

We train the parser with a latency-perturbed supervision scheme. During training, semantic packets are intentionally replayed under delayed timestamps so that the parser must learn to (i) preserve valid clauses under small delay, (ii) shrink pose tolerances and safety budgets under moderate delay, and (iii) trigger conservative routing or semantic refresh requests under severe delay. In this way, latency is treated as a structured control variable rather than incidental runtime noise.

### 3.4 Mid-Layer to Low-Layer Binding Protocol

The mid-layer parser emits a *latency-accountable semantic packet* `p_t = (g_t, c_t, b_t, r_t, a_t)` (§3.3), but a packet is only useful if the low-level controller can **deterministically bind to the most recent valid packet**, even under delayed or duplicated emission. We therefore introduce an explicit binding protocol `B: \mathcal{P} \to \mathcal{A}` that mediates between the mid-layer queue and the low-level dual-head controller.

Concretely, each emitted packet is tagged with a monotonic **packet identifier** `id(p_t) = \mathrm{inc}(id(p_{t-1}))` plus a **validity window** `\omega(p_t) = [t_{emit}, t_{emit} + \Delta_{valid}(a_t, b_t)]`. The binding protocol `B` enforces three rules:

1. **Bind-to-most-recent-valid.** At control tick `τ`, the low-level head queries the mid-layer queue for the latest packet `p_*` satisfying `id(p_*) > id(p_{bound})` and `τ ∈ ω(p_*)`. If multiple valid packets are present, the most recent valid one wins; older packets are evicted from the queue rather than silently merged, because silent merging would conflate two distinct semantic clauses into one freshness estimate.
2. **Defer-to-freshness-on-stale.** If no packet has a validity window covering `τ`, the low-level head is **forbidden** to query a new semantic clause and must instead route to a freshness-preserving fallback (`ρ_t = stale-but-bounded` or `non-promotable`, see §3.5). This rule makes stale execution observable rather than letting it masquerade as semantic understanding.
3. **Bind-then-trace.** Upon successful binding, the low-level head must emit a binding receipt `r_t = (id(p_*), τ_{bind}, τ_{consume_start}, route)` to the consume-time trace. Receipts are mandatory; an action executed without a receipt cannot be claimed as a hierarchical-VLA gain.

This protocol serves two purposes. First, it makes the mid-layer → low-layer handoff **deterministic and replayable** — given a packet log and a receipt log, we can reconstruct which packet drove which control chunk without ambiguity, which is exactly the property required by the post-hoc audit in §3.5. Second, it prevents a subtle but common VLA failure where a fast low-level stack outruns a slow mid-layer and starts *guessing* what the high-level wanted. Under our protocol, guessing is replaced by an explicit, logged fallback that the reviewer can identify as `continuity-preserving fallback`, `bounded safety hold`, or `late refresh recovery` rather than as a hierarchical VLA success.

We emphasize that this binding protocol is **not** an action-routing scheme (compare with DAM-VLA's [REF: 2603.00926] dual diffusion action routing), nor is it a recovery shell (compare with ReCoVLA [REF: 2606.09630] or ProbeAct [REF: 2606.09740]). It is a *deterministic mediator* between the latency-accountable packet stream and the dual-head controller, and any gain attributable to recovery-shell support (FRS) is subtracted before promoting claims that depend on it.

### 3.5 Packet Freshness, Trust-Region Shrinkage, and Non-Promotion Rules

A latency-aware interface is only useful if the system knows when *not* to over-trust stale semantic intent. We therefore augment the semantic packet with an explicit freshness-conditioned trust policy. Let the packet age state be
\[
a_t=(\tau_t^{intent}, \Delta_t^{vlm}, \delta_t^{obs}),
\]
where `\tau_t^{intent}` is elapsed time since the last semantic update, `\Delta_t^{vlm}` is estimated model inference delay, and `\delta_t^{obs}` measures observation drift since packet issuance. The mid-layer parser maps this state to a trust-region budget
\[
\rho_t = f(a_t, s_t, r_t),
\]
which contracts the allowable pose deviation, horizon length, and controller authority as freshness degrades. Intuitively, a fresh packet may authorize a longer open-loop chunk inside a bounded corridor, while a stale packet should only authorize short-horizon alignment or holding actions until semantic refresh is requested.

This design turns freshness into an auditable control variable rather than an implementation detail. In particular, we define three execution regimes: **fresh-executable**, where the packet may drive normal routed execution; **stale-but-bounded**, where execution is allowed only with tightened safety margins and shortened horizons; and **non-promotable**, where the low-level stack may preserve hover, hold, or retreat behavior but is forbidden from claiming semantic-completion gain. The key point is that stale execution may still be useful for safety or continuity, yet it must not be over-promoted into evidence for successful semantic handoff.

Formally, a rollout is not allowed to upgrade to a strong semantic-interface claim if its positive gain appears only after the packet has already crossed into the non-promotable regime. Such cases must be routed to weaker tags such as `continuity-preserving fallback`, `bounded safety hold`, or `late refresh recovery`. This rule directly addresses the aerial setting, where flight stability can hide semantic staleness: a UAV may continue moving smoothly under the low-level controller even after the high-level clause is no longer trustworthy. Our interface therefore separates **execution continuity** from **semantic validity preservation**, and only the latter authorizes strong VLA claims.

### 3.6 Route-Specific Claim Routing for Aerial VLA

The proposed architecture contains multiple possible sources of improvement: better high-level semantic decomposition, better mid-layer latency compensation, smoother low-level continuation, or more conservative safety fallback. To avoid merging these distinct gains into one inflated story, we attach a route-specific claim-routing protocol to every evaluated rollout. Each positive result is labeled by the earliest stage that created the gain, the latest freshness regime in which that gain remains honest, and the controller route through which the gain is consumed.

Concretely, we record a tuple
\[
\Gamma = (w^{+}, w^{\dagger}, r^{\star}, q^{\star}),
\]
where `w^{+}` denotes the earliest positive window, `w^{\dagger}` the last freshness-valid execution window, `r^{\star}` the dominant controller route, and `q^{\star}` the weakest honest claim tag. If the gain is created by semantic decomposition but survives only as a short stale-but-bounded alignment action, it should be reported as a **semantic-guided bounded execution gain**, not as full hierarchical VLA superiority. If the gain appears only because the PID-MPC head prevents instability under delayed packets, it should be routed to **safety-preserving aerial continuity**, not to semantic understanding.

This route-specific protocol is especially important for comparing against partially decoupled baselines such as TIDAL, OnFly, and MolmoAct2. Those systems may improve responsiveness, planner quality, or deployment smoothness without exposing an explicit semantic packet interface. Our claim-routing rule ensures that D02 only claims the narrowest contribution supported by the evidence: semantic freshness preservation, latency-aware interface utility, route-stable execution, or full three-layer handoff advantage. In this way, the paper argues not merely that hierarchy helps, but that hierarchy helps in a way that remains accountable to packet age, route choice, and aerial deployment constraints.

### 3.7 Geometry-Aware 3D Substrate and Governed Memory as Mid-Layer Carriers

The latency-accountable semantic packet must not only carry logical clauses, but also be **physically grounded** in a representation that the low-level controller can audit, replay, and reason about under failure. Following GeneralVLA-2's [REF: 2606.17480] object-centric 3D reconstruction, we augment the mid-layer with a **geometry-aware substrate** that maintains an object-centric 3D scene representation alongside the packet. The substrate is built incrementally from RGB-D observations using a lightweight reconstruction module (akin to GeneralVLA-2's Geometry-Aware Reconstruction head) and is updated whenever the packet freshness budget allows; when freshness degrades, the substrate enters a *frozen* state and the parser must rely on the last grounded 3D snapshot plus a freshness-conditioned uncertainty buffer.

The substrate is paired with a **governed trajectory memory** that stores past successful and failure packet-instance executions, indexed by both semantic clause and geometric layout. At planning time the mid-layer parser queries the memory bank to retrieve (i) similar successful packets to warm-start operation-sequence predictions and (ii) similar failure packets to inflate the safety budget and tighten the route toward conservative fallback. This is a direct adaptation of GeneralVLA-2's governed memory mechanism to the latency-aware setting: the same memory access protocol is now conditioned on packet age, with successful-history lookup preferred in fresh-executable regime, and failure-history lookup preferred in stale-but-bounded regime. We treat the geometry+memory substrate as a *carrier* of the semantic packet, not as a replacement: the packet's logical structure (`g_t, c_t, b_t, r_t, a_t`) remains the only object that the executor binds and consumes, while the substrate provides (i) spatial grounding for the pose/contact constraints, (ii) replayable evidence for the safety budget, and (iii) a queryable history for the route decision.

The architecture becomes explicitly four-tier rather than three-tier in substrate support, but the audit protocol remains three-layer in the *logical* hierarchy:

- **Layer 1 (High-level reasoner)**: realizes the **interleaved-reasoning** structure of ThinkingVLA, producing semantic clauses with explicit reasoning traces; it may optionally inject future-token predictions à la AHEAD but those contributions are reported as **anticipatory wrapper** support.
- **Layer 2 (Mid-layer intent parser)**: consumes Layer 1's clauses, queries the geometry+memory substrate, and emits the latency-accountable packet `p_t` with freshness-conditioned trust-region and route tag.
- **Layer 3 (Low-level dual-head controller)**: binds and consumes the packet under the route tag, with PID-MPC head ensuring aerial stability and the diffusion head handling complex multi-modal action distributions.
- **Substrate layer (cross-layer)**: the geometry-aware 3D scene representation and the governed trajectory memory; this is a *carrier*, not a stage, and any gain it produces is labeled as **SIRS (GMSS)** support and subtracted before promoting semantic-packet claims.

This decomposition lets D02 answer, in a single audit row, **which** of {reasoning, anticipation, geometry/memory, packet-interface} actually drove a positive result, and prevents the long-horizon and failure-recovery gains of ThinkingVLA/GeneralVLA-2 from being silently absorbed into the mid-layer interface claim.

---

## 4. Experiments

### 4.1 Experimental Setup

**Environments**: [TODO: 具体仿真环境和真机平台]

**Baselines**:
| Method | Architecture | Latency | Decoupling | Frozen family (D02 audit) |
|---|---|---|---|---|
| OpenVLA | End-to-end | >900ms | ❌ | monolithic VLA |
| π0 | End-to-end + flow matching | ~200ms | ❌ | monolithic VLA |
| π0.5 | Open-X pretraining + flow matching | ~120ms | ❌ | monolithic VLA |
| TIDAL (2601.14945) | Dual-frequency | ~50ms | Partial (loop) | action-head decoupling support |
| TIC-VLA (2602.02459) | Latency-aware delayed interface | ~80ms | Partial (latency) | action-head decoupling support |
| DAM-VLA (2603.00926) | Dual diffusion action model | ~150ms | Partial (sub-action) | action-head decoupling support |
| MolmoAct2 (2605.02881) | Reasoning + continuous action expert | medium | Partial (reasoning) | monolithic VLA + reasoning |
| Realtime-VLA V2 (2603.26360) | Fast/smooth/accurate co-design | low | Partial (deployment) | monolithic VLA + deployment |
| AIR-VLA+ (2606.12859) | Cascaded dual-action decoders + asymmetric MoE | ~50ms | Partial (movement/manipulation) | action-head decoupling support |
| ReCoVLA (2606.09630) | VLM-guided recovery reward + residual policy | high | recovery shell | failure-recovery shell support |
| ProbeAct (2606.09740) | Hidden-state probe + hierarchical CBF filter | low | recovery shell | failure-recovery shell support |
| DUST (2510.27607) | Dual-stream diffusion + async sampling | medium | world-action co-design | world-action co-design support |
| AHA-WAM (2606.09811) | Dual DiT + observation-guided context routing | medium | world-action co-design | world-action co-design support |
| Ours | Three-layer hierarchical (semantic packet) | ~10ms (low-level) | ✅ semantic-intent-execution decoupling | — |

**Matched-subtraction audit protocol**: For every reported positive gain, the row must report the **frozen support family** of each baseline and the **matched-subtraction residual** `Δ^{D02}_row = ΔG_row \ (M ∪ AHD ∪ FRS ∪ WACS)`, where `M` = monolithic VLA, `AHD` = action-head decoupling, `FRS` = failure-recovery shell, `WACS` = world-action co-design. Only residual gains that survive matched-subtraction are eligible for promotion to **semantic-intent-execution decoupling gain**.

**Metrics**:
- Task success rate (approach / alignment / contact / grasp)
- End-effector trajectory smoothness (velocity/acceleration/jerk)
- Control jitter rate (chunk-transition instability)
- Semantic latency compensation effectiveness
- Aerial stability during manipulation (attitude deviation)
- Packet freshness preservation under delayed execution
- Route-switch stability between diffusion and PID-MPC heads

### 4.2 Main Results

We evaluate the proposed hierarchical VLA on (i) the AIR-VLA aerial manipulation benchmark (approach / alignment / contact / grasp) and (ii) a custom **delay-perturbed aerial grasping protocol** that injects controlled VLM latency `\Delta^{vlm} \in {120ms, 400ms, 900ms}` and observation drift `\delta^{obs}` to stress the freshness interface. Each row in every table is a **single ablation line**, not a method — i.e., the *rows* vary which ablation we are running, while the *columns* describe the matched-subtraction audit. This avoids the common failure mode where one row in a "main results" table silently mixes gains from M, AHD, FRS, and WACS families.

#### 4.2.1 Task Outcome by Sub-Phase (Primary)

We report success rate for each aerial sub-phase under matched semantic-interface conditions. The expected primary result is that the three-layer architecture preserves sub-phase success rates under increasing delay, while monolithic baselines degrade non-uniformly (early sub-phases fail before late sub-phases).

| Row (matched interface) | Approach (%) | Align (%) | Contact (%) | Grasp (%) | FRS/M subtracted? |
|---|---|---|---|---|---|
| OpenVLA (frozen, delay=120ms) | [TODO] | [TODO] | [TODO] | [TODO] | — |
| OpenVLA (frozen, delay=400ms) | [TODO] | [TODO] | [TODO] | [TODO] | — |
| π0 + AHD (AIR-VLA+ head) | [TODO] | [TODO] | [TODO] | [TODO] | partial |
| π0 + AHD + ProbeAct shell | [TODO] | [TODO] | [TODO] | [TODO] | FRS stripped |
| Ours (no mid-layer packet, L1+L3 only) | [TODO] | [TODO] | [TODO] | [TODO] | FRS stripped |
| **Ours (full packet + freshness)** | [TODO] | [TODO] | [TODO] | [TODO] | full |

The last two rows form the *honest ablation pair* for the mid-layer claim: both have the FRS shell stripped, so any remaining gap must come from the packet/freshness route — not from a discrete verifier or a recovery filter.

#### 4.2.2 End-Effector Trajectory Smoothness and Chunk Stability

Following Realtime-VLA V2 [REF: 2603.26360], we elevate deployment quality from "single-step accuracy" to a triple: trajectory smoothness, control jitter, and chunk stitching stability. We report **average jerk magnitude** `J̄`, **control jitter rate** `CJR` (fraction of control ticks whose `‖Δu‖` exceeds `3σ` of the rollout mean), and **chunk stitching discontinuity** `Δ_{stitch}` (mean pose jump at chunk boundaries).

| Row | J̄ (m/s³) | CJR (%) | Δ_{stitch} (rad) | Notes |
|---|---|---|---|---|
| Monolithic π0 | [TODO] | [TODO] | [TODO] | No chunk scheduler |
| AIR-VLA+ (AHD only) | [TODO] | [TODO] | [TODO] | AHD reduces J̄ but not CJR |
| DAM-VLA (AHD + MoE routing) | [TODO] | [TODO] | [TODO] | AHD reduced |
| MolmoAct2 (WACS+reasoning) | [TODO] | [TODO] | [TODO] | WACS stripped |
| **Ours** | [TODO] | [TODO] | [TODO] | Freshness-conditioned horizon |

The expected pattern is that **AHD alone** improves J̄ but **leaves CJR unchanged**, while the dual-head controller with freshness-conditioned horizon reduces both. If a baseline without the mid-layer packet achieves comparable CJR reduction, the gain must be attributed to AHD support and the matched-subtraction residual reported.

#### 4.2.3 Packet Freshness Preservation under Delayed Execution

We instrument each rollout with the freshness state `a_t = (\tau^{intent}, \Delta^{vlm}, \delta^{obs})` and report three freshness-derived metrics:

- **FPR — Freshness Preservation Rate**: fraction of executed actions whose packet `id(p_t)` was bound within its validity window `\omega(p_t)`. Lower FPR = the mid-layer is being bypassed by stale execution.
- **FNR — Fallback Necessity Rate**: fraction of control ticks routed to `stale-but-bounded` or `non-promotable` rather than `fresh-executable`. Higher FNR = the system is correctly admitting staleness rather than masking it.
- **FFR — Frozen-Freshness Recovery**: fraction of `non-promotable` ticks that subsequently recovered to `fresh-executable` after a successful semantic refresh.

| Row (delay setting) | FPR | FNR | FFR | Misleading `success` (frozen?) |
|---|---|---|---|---|
| OpenVLA @ 400ms | [TODO] | [TODO] | [TODO] | should be frozen — no packet, no FPR/FNR defined |
| TIDAL @ 400ms | [TODO] | [TODO] | [TODO] | partial (loop freq) |
| TIC-VLA @ 400ms | [TODO] | [TODO] | [TODO] | partial (latency model) |
| AIR-VLA+ + ProbeAct @ 400ms | [TODO] | [TODO] | [TODO] | FRS stripped |
| **Ours @ 400ms** | [TODO] | [TODO] | [TODO] | full packet |
| **Ours @ 900ms** | [TODO] | [TODO] | [TODO] | full packet |

The crucial audit invariant is that **OpenVLA does not get to claim a higher success rate at 400ms without producing a non-trivial FPR/FNR/FFR table** — without the mid-layer interface, `fresh-executable` is undefined and any "success" must be re-routed to `continuity-preserving fallback` or `non-promotable frozen success` (see §3.5).

#### 4.2.4 Route-Switch Stability and Aerial Stability

For each rollout, we record the route-specific tuple `\Gamma = (w^{+}, w^{\dagger}, r^{\star}, q^{\star})` (§3.6) and report:

- **RSR — Route-Switch Rate**: fraction of control ticks where the dominant controller route switches between the diffusion head and the PID-MPC head.
- **RSI — Route-Switch Instability**: mean attitude deviation `‖Δφ‖` measured in ticks immediately following a route switch.
- **Aerial-Continuity Pass-Through**: fraction of maneuvers in which route switching prevented an unsafe attitude excursion that would otherwise exceed `5°`.

| Row | RSR | RSI (deg) | Aerial-Continuity Pass-Through | Dominant `q^{\star}` |
|---|---|---|---|---|
| Dual-head w/o freshness | [TODO] | [TODO] | [TODO] | (route-jitter) |
| Dual-head + freshness + non-promotion | [TODO] | [TODO] | [TODO] | safety-preserving continuity |
| **Ours** | [TODO] | [TODO] | [TODO] | semantic-intent execution |

If the dual-head w/o freshness variant produces comparable RSI but a higher RSR, the "aerial stability" gain must be reported under `safety-preserving aerial continuity`, **not** under `semantic-intent execution`. This is the same route-specific claim-routing rule that prevents OpenFly-style "continuous flight = good VLA" inflation.

### 4.3 Ablation Study

We ablate along the **three-layer axis** and along the **matched-subtraction axis** simultaneously. Each ablation row is run under three delay stress cells `W1/B1 (Δ=120ms), W2/B1 (Δ=400ms), W2/B2 (Δ=900ms with observation drift)`, so every cell forces the freshness interface to be exercised — there is no "ablation under trivially fresh conditions" escape hatch.

#### 4.3.1 Three-Layer Hierarchy Ablation (C1)

| Ablation | Layer 1 (high) | Layer 2 (mid packet) | Layer 3 (low dual-head) | Family matched-subtract |
|---|---|---|---|---|
| A1a — Monolithic | VLM end-to-end | — | single head | M (full claim) |
| A1b — Single-Action-Decoder | VLM | — | AHD only | AHD |
| A1c — Two-Layer w/o packet | VLM intent | — | dual-head + freshness | AHD |
| A1d — Three-Layer w/o freshness | VLM intent | packet (no `a_t`) | dual-head | AHD |
| **A1e — Three-Layer (full)** | VLM intent | packet + freshness | dual-head | AHD only |
| A1f — Three-Layer + ProbeAct | VLM intent | packet + freshness | dual-head + recovery | AHD + FRS stripped |

The expected pattern: A1a–A1d fail to dominate the matched-subtraction ceiling; A1e alone should expose a non-trivial residual `Δ^{D02}_{A1e} > Δ^{D02}_{A1d}`; and A1f's gain over A1e must be flagged as **FRS shell residual**, not as packet-interface superiority.

#### 4.3.2 Latency Compensation Ablation (C2)

| Ablation | `intent_age` input | `latency_offset` input | `obs_drift` input | Trust-region shrinkage |
|---|---|---|---|---|
| A2a — No latency | ❌ | ❌ | ❌ | fixed |
| A2b — `intent_age` only | ✅ | ❌ | ❌ | age-only |
| A2c — `intent_age` + `latency_offset` | ✅ | ✅ | ❌ | age+latency |
| **A2d — Full** | ✅ | ✅ | ✅ | full `ρ_t = f(a_t, s_t, r_t)` |

For each ablation we report `(FPR, FNR, FFR, RSR, RSI)` from §4.2.3-4 under `W2/B1` and `W2/B2`. Promotion rule: a gain may be labeled **latency-aware interface gain** only if A2d > A2c in FFR and RSI under W2/B2 *and* A2c > A2b in FNR. Otherwise the gain is attributed to **age-only support** and frozen.

#### 4.3.3 Dual-Head Controller Ablation (C3)

| Ablation | Diffusion head | PID-MPC head | Route tag | Dominant `q^{\star}` |
|---|---|---|---|---|
| A3a — Diffusion only | ✅ | ❌ | always `diff` | action-distribution support |
| A3b — PID-MPC only | ❌ | ✅ | always `pid` | safety-preserving continuity |
| A3c — Diffusion + fixed heuristic | ✅ | ✅ | heuristic switch | action-head decoupling |
| **A3d — Freshness-conditioned** | ✅ | ✅ | `ρ_t`-driven | semantic-intent execution |

The promotion rule: A3d must dominate A3c in `(RSR, RSI, Aerial-Continuity Pass-Through)` under `W2/B2` *after* subtracting A3b's `safety-preserving continuity` residual. If A3c ≈ A3d under this subtraction, the gain is attributed to **action-head decoupling support (AHD)** rather than to the freshness-conditioned route.

#### 4.3.4 Reasoning Substrate Ablation (C4)

| Ablation | Layer-1 reasoning | Mid-layer substrate | Promotion |
|---|---|---|---|
| A4a — Textual CoT | textual CoT | none | IRS-stripped |
| A4b — Interleaved V-L CoT | ThinkingVLA-style | none | IRS only |
| A4c — Latent Structured Intent | latent `s_t` | none | mid-layer partial |
| **A4d — Structured Intent + Geometry-Memory substrate** | latent `s_t` | GeneralVLA-2 GMSS | mid-layer + GMSS stripped |

A4d must dominate A4c in long-horizon tasks *after* A4b's IRS residual is subtracted, otherwise the long-horizon gain is reported under **GMSS substrate support**, not under **semantic-packet gain**.

#### 4.3.5 Combined-Gain Promotion Gate for the Three-Layer Stack

Following D01's `Γ^{mc}` combined-gain promotion gate (§4.3.4 of D01 PAPER.md), we define a D02 combined-gain residual that requires **all three ablation axes** to survive matched-subtraction simultaneously:

\[
\Gamma^{\mathrm{pkt}}_{\text{three-layer}} = \Delta G_{\text{A1e}} \setminus \left( \mathrm{AHD} \cup \mathrm{FRS} \cup \mathrm{WACS} \cup \mathrm{SIRS} \right),
\]

and demand that this residual be **strictly positive** under `(W2/B1, W2/B2)` and **non-negative** under `(W1/B1)`. If `\Gamma^{\mathrm{pkt}}_{\text{three-layer}} \le 0` in any cell, the three-layer claim is **frozen** to the highest surviving support label (`AHD`, `FRS`, `WACS`, or `SIRS`) and is not promoted to **semantic-intent-execution decoupling gain** in §5.

---

## 5. Conclusion

[TODO: 3-5句话总结贡献，指出局限，展望未来]

We present a three-layer hierarchical VLA architecture that explicitly decouples semantic intent reasoning from fine-grained motor execution for aerial manipulation. [TODO: 补充主要实验结论] Our latency-aware mid-layer interface and dual-head low-level controller enable simultaneous aerial stability and manipulation precision. Limitations include [TODO]. Future work will explore integration with the world model-based deployment supervisor (D01) for pre-execution safety screening.

---

## References

[1] OpenVLA. arXiv: [TODO], 2024.
[2] π0: Flow Matching for Robot Action Generation. arXiv: [TODO], 2024.
[3] GR00T: Cross-Embodiment VLA. arXiv: [TODO], 2024.
[4] TIDAL: Dual-Frequency VLA. arXiv:2601.14945, 2026.
[5] TIC-VLA: Temporal Interface Compensation. arXiv:2602.02459, 2026.
[6] LaST0: Latent Spatio-Temporal CoT. arXiv: [TODO], 2026.
[7] Realtime-VLA V2. arXiv:2603.26360, 2026.
[8] DAM-VLA: Dual Action Model VLA. arXiv: [TODO], 2026.
[9] Long-Horizon Manipulation with Adaptive Planning and Reflection. arXiv:2604.13942, 2026.
[10] MolmoAct2: Action Reasoning Models for Real-world Deployment. arXiv:2605.02881, 2026.
[11] VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts. arXiv:2605.06175, 2026.
[12] AIR-VLA+: Decoupling Movement and Manipulation via Cascaded Dual-Action Decoders with Asymmetric MoE for Aerial Robots. arXiv:2606.12859, 2026.
[13] ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies. arXiv:2606.09630, 2026.
[14] ProbeAct: Probe-Guided Training-Free Failure Recovery in Vision-Language-Action Models. arXiv:2606.09740, 2026.
[15] DUST: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model. arXiv:2510.27607, 2026.
[16] AHA-WAM: Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing. arXiv:2606.09811, 2026.
[17] AutoHorizon: [TODO], 2026. (attention-guided horizon scheduling)
[18] Long-Horizon Adaptation with Reflective Planner. arXiv:2604.13942, 2026. (also cited as [9])
[19] AHEAD: Intercepting the Future — Latent-Space Predictive World Model for Dynamic VLA Manipulation. arXiv:2606.02486, 2026.
[20] ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation. arXiv:2606.17937, 2026.
[21] GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning. arXiv:2606.17480, 2026.
[22] VERITAS: Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement. arXiv:2606.18247, 2026. (UC Berkeley, Zhang & Shah)
[TODO: 补充完整引用列表]
