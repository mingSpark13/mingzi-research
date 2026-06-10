# A World Model-Based Deployment-Time Supervisor for Aerial Manipulation

> 方向：D01 世界模型 | 目标会议：ICRA 2027 | 状态：🔴 草稿
> 最后更新：2026-05-14

---

## Abstract

Aerial manipulation requires deployment-time supervision that goes beyond visually realistic rollout, because packet handoff can fail through bad initial judgment, expired-packet reuse, and downstream consumption mismatch. We propose a world-model-based supervisor that outputs a time-valid safety packet with explicit stage tag, remaining-plan fields, packet expiry, and stage-scoped risk budget for D01→D06 handoff. The method combines dual-dynamics latent prediction, physics/executability alignment, F1/F2 failure triage, and hover-bounded packet repair, while evaluating deployment utility with danger-action release, packet handoff failure, expiry-sensitive repair error, and remaining-plan preservation metrics instead of image realism alone. We further require results to distinguish whether gains come from interface validity, expiry-aware bounded correction, or true cross-stage handoff improvement, preventing local repair wins from being overstated as generic supervision gains. We hypothesize that the strongest contribution of D01 is not a static rollout scorer, but a time-sensitive deployment contract that preserves executable progress continuity under aerial-manipulation constraints.

---

## 1. Introduction

### 1.1 Problem Statement

Aerial manipulation—the combination of unmanned aerial vehicle (UAV) flight dynamics with robotic arm manipulation—presents unique challenges that existing world model approaches fail to address. Current vision-language-action (VLA) systems such as OpenVLA, π0, and GR00T adopt end-to-end architectures where the VLM directly outputs action tokens, suffering from three fundamental bottlenecks: (1) VLM forward latency (200–2000ms) is incompatible with millisecond-level control requirements; (2) purely visual prediction lacks physical consistency guarantees; and (3) existing models do not jointly model aerial flight dynamics and manipulation end-effector dynamics.

World models offer a promising solution by learning environment dynamics in latent space, enabling imagination-based planning and policy optimization. However, existing world model approaches—including DIAL [REF: ], WAM [REF: 2603.28955], RISE [REF: 2602.11075], and WorldEval [REF: 2505.19017]—are designed for ground manipulation and do not account for the dual-dynamics constraint of aerial platforms. Furthermore, deploying world models in safety-critical aerial settings requires not only accurate rollout prediction but also reliable pre-execution verification, failure triage, and stage-aware routing.

This paper addresses the question: *how can a world model serve as a deployment-time supervisor for aerial manipulation, providing pre-execution safety screening, failure classification, and stage-aware action routing?*

### 1.2 Contributions

This paper makes the following contributions:

1. **C1: Dual-Dynamics World Model**: We propose a world model that jointly models aerial flight dynamics and manipulation end-effector dynamics in a shared latent space, enabling planning under the coupled constraints of aerial platforms.
2. **C2: Two-Stage Post-Training Protocol**: We introduce a physics alignment stage (suppressing physically implausible rollouts) followed by an executability alignment stage (enforcing smooth, reachable actions via IDM reward), improving downstream policy success rates.
3. **C3: Deployment-Time Supervisor Interface**: We formalize a `Pre-Execution Safety Packet` interface (`rank_score`, `failure_state`, `route_action`, `stage_tag`, `risk_budget`) that enables the world model to serve as a stage-aware supervisor for downstream navigation and manipulation stacks.
4. **C4: F1/F2 Failure Triage**: We distinguish *known failures* (F1: nameable, recoverable) from *unknown anomalies* (F2: out-of-distribution, requiring human escalation), enabling principled deployment-time decision routing.
5. **C5: Hover-Bounded Recovery**: We demonstrate that world-model-based recovery yields measurable gains specifically within hover/re-anchor windows, and formalize the phase-bounded deployment conditions under which recovery is safe to deploy.

## 2. Related Work

### 2.1 World Models for Robot Manipulation

World models learn environment dynamics in latent space to support planning, policy training, and evaluation. DIAL [REF: ] introduces an intent bottleneck that explicitly separates intent from action, using a latent world model to predict future states. WAM [REF: 2603.28955] extends DreamerV2 with an inverse dynamics loss to produce action-aware latent representations, achieving 92.8% on CALVIN. RISE [REF: 2602.11075] employs a compositional world model with dual branches (dynamics model + progress value model) combined with imagination-based self-improvement, yielding 35–45% improvement on real robot tasks. LeWorldModel [REF: 2603.19312] further shows that stable end-to-end JEPA-style world modeling can be trained directly from pixels with only a next-embedding prediction loss plus SIGReg regularization, dramatically simplifying optimization while preserving physically probeable latent structure and fast planning throughput. These approaches demonstrate the value of world models for ground manipulation but do not address the dual-dynamics constraints of aerial platforms.

### 2.2 World Models as Evaluators and Supervisors

WorldEval [REF: 2505.19017] explicitly positions the world model as a pre-deployment policy evaluator and danger-action filter, showing that while world models tend to underestimate in-distribution and overestimate out-of-distribution performance, they reliably preserve relative policy rankings suitable for pre-deployment screening. Interactive World Simulator [REF: 2603.08546] advances action-conditioned video world models toward interactive simulators, emphasizing long-horizon stability and simulated-real performance correlation. WAV [REF: 2604.01985] decomposes action-conditioned prediction into *state plausibility* and *action reachability* sub-problems, using action-free video and sparse inverse models for self-verification, achieving 2× sample efficiency and 18% downstream policy improvement. These works collectively motivate our deployment-time supervisor design. Recent memory-augmented and tokenized-action models add a complementary lesson: supervisory usefulness improves when the world model carries explicit temporal state rather than collapsing everything into the current frame. MemoryVLA++ [REF: 2606.09827] couples working memory, episodic retrieval, and latent imagination to preserve history-dependent execution context over long horizons, while iMaC [REF: 2606.09813] rewrites action inputs into motion/contact image tokens that retain contact semantics and embodiment-sensitive actuation structure. For D01, neither paper directly solves deployment-time packet contracts, but together they strengthen a concrete design requirement: a supervisor packet should preserve not only feasibility and freshness, but also enough temporal-history trace and contact-aware action semantics to keep downstream bind and consume decisions aligned with the same executable thread.

### 2.3 Physics-Aligned World Models

ABot-PhysWorld [REF: 2603.23376] addresses physically implausible world model outputs (object penetration, anti-gravity, out-of-bounds actions) through physics-aware annotation and DPO post-training, proposing EZSbench to separately evaluate physical realism and action alignment. EVA [REF: 2603.17808] introduces a two-stage post-training protocol: first physics alignment, then executability alignment using an inverse dynamics model (IDM) as a reward model to enforce smooth, reachable motions. For aerial platforms where flight dynamics impose strict velocity, acceleration, and jerk constraints, EVA's IDM reward naturally incorporates trajectory smoothness requirements. Crucially, ABot-PhysWorld also implies that deployment-facing world models should not collapse physical plausibility into a single rollout-quality score: if physical realism and action alignment improve by different amounts, the supervisor must report them separately rather than letting a visually cleaner rollout overclaim executability. This decomposition directly supports our D01 argument that packet release should be justified by physics-accountable evidence, not by perceptual realism alone.

### 2.4 Failure Classification, Feasibility Screening, and Recovery

Dream2Fix [REF: 2603.13528] synthesizes counterfactual failure rollouts by perturbing successful demonstrations within a generative world model, producing failure→correction paired data for training recovery policies. World Model Failure Classification [REF: 2602.16182] proposes distinguishing known failures from anomalies for autonomous inspection, motivating our F1/F2 triage protocol. Recent work on explicit physical feasibility in VLA learning [REF: 2604.17896] further suggests that execution-time supervision should separate semantic correctness from physical feasibility, rather than treating them as a single score. Hi-WM [REF: 2604.21741] pushes world models one step closer to deployment-time corrective infrastructure by showing that failure states inside the learned model can be reused, rolled back, and branched for human corrective supervision, effectively turning the world model into a reusable substrate for failure-targeted post-training rather than only for passive evaluation. Very recent long-horizon VLA evidence also strengthens this decomposition from the planning side: LoHo-Manip [REF: 2604.21924] shows that progress-aware remaining-plan prediction and compact visual traces can implicitly absorb execution errors by repeatedly reissuing local goals instead of relying on brittle monolithic history buffers. Although LoHo-Manip is not a world-model supervisor, it reinforces a design principle highly relevant to D01: recovery and replanning become much more reliable when progress state, remaining intent, and local execution hints are packetized into an explicit intermediate representation. Persistent Robot World Models [REF: 2603.25685] adds a complementary world-model-side signal: stabilizing multi-step rollout trajectories through reinforcement learning can convert failure-prone imagined futures into more reusable supervisory evidence, which matters when cached branches are later reused for packet repair or human correction. OA-WAM [REF: 2605.06481] adds a new identity-preservation perspective by separating persistent object/action addresses from time-varying content, suggesting that delayed-consumption failure is not only about stale timing but also about whether the packet still points to the same executable referent when the downstream stack finally consumes it. Together, these works motivate our decomposition of pre-execution supervision into ranking, feasibility screening, triage, bounded recovery, branchable corrective memory, identity-preserving packet addressing, and explicit remaining-plan preservation.

A further design pressure emerges from recent object-addressable world-action modeling. OA-WAM [REF: 2605.06481] decomposes world prediction into persistent robot/object slots with address vectors separated from time-varying content, allowing action decoding to preserve object identity under scene perturbation. While OA-WAM is proposed for robust manipulation rather than deployment-time supervision, its slot-address separation sharpens an important D01 concern: delayed-consumption failure is often not just a timing problem but an **identity-preservation problem**. A packet can remain geometrically feasible and even controller-bindable while silently drifting to a nearby but different object anchor or clause target. This strengthens our decision to make remaining-plan preservation, clause identity, and downstream consume-honesty first-class supervisory variables instead of treating packet validity as a single scalar confidence.

Recent interface-focused evidence also suggests that the boundary between imagined future quality and executable control quality is still under-specified. MoLA [REF: 2605.12167] proposes a mixture-of-latent-actions interface that inverts imagined multimodal futures into control-oriented latent actions through multiple inverse-dynamics experts, explicitly targeting the gap between perceptually plausible rollout and executable robot behavior. For D01, MoLA reinforces a concrete design pressure: even if packet ranking, expiry handling, and thread preservation are modeled well, the supervisory contract is still vulnerable if the imagined future is decoded through a weak action interface. We therefore treat latent-action mixture quality as complementary evidence for whether a refreshed packet remains not only semantically and temporally valid, but also **decode-honest** with respect to downstream control.

### 2.5 Evaluation Beyond Visual Fidelity

WorldArena [REF: 2602.08971] demonstrates a persistent perception-functionality gap in embodied world models: high-quality video prediction does not necessarily translate into high utility for data generation, policy evaluation, or closed-loop planning. RoboWM-Bench [REF: 2604.19092] further shows that visually plausible rollouts often fail to produce executable manipulation behavior once converted back into action space, with common failure modes including spatial reasoning errors, unstable contact prediction, and non-physical deformation. Mask World Model [REF: 2604.19683] complements these findings by replacing RGB prediction with semantic mask dynamics, introducing a geometric information bottleneck that improves robustness by filtering out nuisance appearance factors such as texture and illumination. ROBOGATE [REF: 2603.22126] adds a deployment-facing perspective by showing that even strong manipulation policies require explicit pre-deployment boundary discovery and failure-focused screening before real execution. Chain of World [REF: 2603.03195] contributes a nearby but distinct lesson: structure-motion factorization can reduce the burden of reconstructing static appearance while keeping temporally useful latent motion chains for downstream action generation. Although it is proposed as a world-model-thinking VLA rather than a deployment-time supervisor, it strengthens the argument that executable downstream value depends on preserving motion-relevant latent structure rather than maximizing pixel realism alone.

Very recent industrial evidence further pushes this argument from benchmark diagnostics toward deployment reliability. Cortex 2.0 [REF: 2604.20246] reports that real-world long-horizon manipulation benefits from explicitly generating and scoring candidate futures before commitment, rather than acting reactively one step at a time. Dream-MPC [REF: 2605.04568] strengthens the planner-side version of this story by showing that latent imagined trajectories can be iteratively optimized rather than passively sampled, while Semantic Latent Space World Models [REF: 2605.06388] suggest that semantically organized latent states can improve what futures are screened as promising in the first place. Yet these newer results also sharpen a caution central to D01: better future scoring and better semantic latent organization are still not equivalent to better delayed-consumption supervision. They may improve candidate quality at proposal time without guaranteeing that the released packet remains fresh, clause-consistent, and consume-honest when finally used downstream. Accordingly, we treat them as evidence that **representation-side screening** and **planner-side refinement** matter, but not as proof that packet-contract failure has been solved.

Although Cortex 2.0 is not designed as a pre-execution safety supervisor, it reinforces a key thesis of this paper: deployment utility emerges when world models are judged by whether their imagined futures help select *reliable executable behavior* under clutter, occlusion, and contact-rich uncertainty, not by whether the generated video merely looks convincing.

A further practical lesson comes from lightweight JEPA-style latent prediction. LeWorldModel [REF: 2603.19312] shows that compact end-to-end joint-embedding predictors can deliver dramatically faster planning loops and physically probeable latent structure with minimal training machinery. For D01, this is useful not because it automatically solves handoff accountability, but because it creates a cleaner experimental separation between **refresh-budget availability** and **refresh-value honesty**. In other words, faster latent refresh makes it easier to test whether more frequent packet regeneration truly improves delayed-consumption survival, rather than merely improving planner-time ranking density.

### 2.6 Limitations of Existing Work

Existing world model approaches share several critical gaps for aerial manipulation deployment:
(1) No existing work jointly models aerial flight dynamics and manipulation dynamics under coupled constraints.
(2) Evaluation metrics often conflate video generation quality with task utility.
(3) Failure handling is typically binary (pass/fail) without distinguishing recoverable known failures from out-of-distribution anomalies.
(4) Recovery mechanisms lack phase-bounded deployment conditions, risking unsafe execution in high-speed flight segments.
(5) Action interface generalization remains weak.
(6) Robustness to nuisance appearance variation is still under-modeled.
(7) Existing deployment-oriented systems provide limited support for stage-aware triage, packetized supervisory handoff, and safety-accountable recovery.
(8) Existing human-in-the-world-model systems stop short of formalizing a stage-aware pre-execution supervisor with explicit routing, packet contracts, and deployment-boundary accounting.
(9) Even strong long-horizon real-world world-model systems still evaluate commitment quality mostly at the moment of candidate selection, leaving **packet freshness, expiry-triggered invalidation, and downstream consumption delay** weakly formalized as first-class deployment variables.
(10) Existing progress-aware replanning systems retain local intent implicitly in memory, traces, or latent plans, but they rarely expose an explicit packet-level contract for **remaining-plan preservation under repair and handoff**.
(11) Existing real-world and industrial world-model pipelines still under-specify a harder deployment question: a packet judged valid at release time can become semantically stale by the time it is actually consumed downstream, yet current evaluation rarely separates **pre-release routing gain**, **hover-window bounded recovery gain**, and **true post-refresh downstream handoff gain** under delayed consumption.
(12) Current world-model evaluation rarely reports whether a refresh event preserves the *same executable thread* or silently swaps to a nearby but semantically shifted local plan, making delayed-consumption gains easy to overclaim when controller-side uptake is not stratified by thread preservation.
(13) Benchmark evidence such as WorldArena further suggests that visually convincing rollouts can still fail to improve downstream screening or execution decisions, so any D01-style supervisor must report deployment-facing packet outcomes rather than relying on aggregate perceptual realism scores as a proxy for supervisory usefulness.
(14) End-to-end JEPA-style world models such as LeWorldModel show that stable compact latent dynamics can be learned with very lightweight objectives, but they still stop short of exposing stage-aware packet contracts, expiry rules, or controller-consumption accountability for deployment-time handoff.
(15) Structure-motion world-model VLA hybrids such as Chain of World reduce representational waste on static appearance and strengthen motion-centric latent prediction, yet they remain optimized for action generation quality rather than for delayed-consumption supervision, thread preservation, or safety-accountable release decisions.
(16) Existing deployment-oriented world-model pipelines still do not expose an explicit notion of **controller-consumption accountability**: a packet may improve planner-side ranking, verifier-side acceptance, or refresh-time freshness, while still failing to preserve the same executable clause when the downstream controller finally binds and consumes it.
(17) Existing packet-level evaluation also under-specifies the distinction between **controller bind** and **local interaction consume**. A packet can survive verifier acceptance and even be successfully attached by the downstream controller, yet still fail when the local interaction stack actually consumes it under execution-time contact, timing, or stage constraints.
(18) More fundamentally, current deployment-facing evaluation rarely measures whether a packet keeps the **same clause identity and remaining-plan compatibility across bind and consume**. As a result, a system can report stronger planner release, verifier acceptance, or controller bind rates while still losing the packet's executable meaning at the final local-interaction consume step.
(19) Existing deployment-time world-model studies also rarely separate **bind-honest** gains from **consume-honest** gains inside the same downstream stage. Without this distinction, local attach success can be misreported as full deployment-time supervisory value, even when the packet only survives long enough to bind but not long enough to preserve executable semantics through actual interaction consumption.
(20) Even when progress fields are retained, current systems seldom preserve an explicit **addressable identity channel** for objects, anchors, or clause targets across refresh and handoff; as a result, delayed-consumption packets can silently drift to a nearby but different referent while still looking feasible under geometric or controller-local checks.
(21) Recent object-addressable world-action models such as OA-WAM [REF: 2605.06481] strengthen identity robustness under manipulation perturbation, but they still do not elevate **consume-time clause/object/address preservation** into a first-class deployment-time supervisory contract with explicit bind-versus-consume honesty separation.
(22) Lightweight JEPA-style latent predictors such as LeWorldModel [REF: 2603.19312] suggest that compact physically probeable latent dynamics may be enough for fast packet scoring, yet existing work still does not show whether higher refresh frequency actually preserves **remaining-plan identity and delayed-consumption honesty** rather than merely planner-side ranking quality.
(23) Recent object-slot world-action modeling further hints that identity disentanglement should be treated not only as a representation robustness issue but also as a **packet-accountability issue**: if slot identity, target clause, and downstream consume address are not explicitly logged together, a refreshed packet can appear safer while actually switching executable referents under the hood.
(24) Lightweight JEPA-style world models also leave unresolved a deployment-facing calibration question: even when compact latent predictors enable faster refresh cycles, current work rarely distinguishes whether the extra refresh budget improves **planner-side proposal quality** or actually improves **bind-honest / consume-honest packet survival** under delayed downstream uptake.
(25) Latent-action interface advances such as mixture-based inverse-dynamics decoding reinforce that identity preservation alone is insufficient; a packet can remain clause-consistent and address-stable while still losing executable meaning if refreshed futures are decoded through a control-weak latent action interface at consume time.
(26) Compact end-to-end latent predictors such as LeWorldModel [REF: 2603.19312] may substantially increase refresh frequency and screening throughput, but existing work still does not report whether this speedup changes **delayed-consumption honesty** or only densifies planner-time rescoring.
(27) Semantics-oriented latent-space selection can improve planner-side screening and policy-relevant prediction, but current work still under-specifies whether a more semantic latent actually preserves **slot identity, clause continuity, and decode-honest packet meaning** through delayed downstream consume.
(28) Asynchronous or speculative refresh pipelines such as DexWorldModel [REF: 2604.16484] further blur a critical boundary: more frequent packet regeneration may improve release-time ranking and controller bind honesty while leaving true consume-time packet survival unchanged, yet current reporting rarely separates these refresh-window regimes into proposal gain, bind gain, and real downstream handoff gain.
(29) Even when semantic latent screening and fast refresh are both available, existing work still does not expose a unified subtraction protocol that removes **semantic ranking gain**, **refresh-density gain**, and **stale-route support** before crediting downstream packet-contract improvement; this makes it too easy to overclaim delayed-consumption progress when the real improvement may live only at proposal time or in interface-side semantic routing.
(30) Recent adaptive world-action models such as HarmoWAM [REF: 2605.10942] show that predictive and reactive experts can be harmonized through stage-sensitive gating, but they still do not formalize whether the gating decision itself preserves packet identity, remaining-plan continuity, or consume-time honesty under delayed downstream uptake.
(31) Semantically grounded planning-oriented world models such as Grounded World Model [REF: 2604.11751] improve cluttered language-conditioned manipulation by coupling latent dynamics with grounding and MPC, yet they evaluate semantic planning quality more than whether grounded packets remain bind-honest and consume-honest once execution is delayed or re-anchored.
(32) Hybrid-task world/ego disentanglement models such as WEM [REF: 2605.19957] clarify long-horizon state organization, but they still stop short of exposing how world/ego separation should translate into a packet contract that audits clause identity, progress-thread continuity, and downstream consume preservation across navigation-manipulation handoff.
(33) Compact JEPA-style latent predictors such as LeWorldModel and LeJEPA-derived training recipes can substantially strengthen representation stability and refresh density, but they still provide little guidance on whether **faster, cleaner latent refresh** merely improves packet rescoring or actually preserves **the same world/ego split, clause identity, and consume-time executable meaning** through delayed downstream uptake.
(34) Even when world/ego separation improves long-horizon prediction quality, current work rarely audits whether the world-side branch and ego-side branch stay aligned to the same downstream thread at bind and consume time; without this audit, a model may look structurally disentangled yet still silently shift the executable subgoal during handoff.
(35) Current deployment-facing world-model evaluation also lacks a direct subtraction protocol between **world/ego thread-preservation gain** and **latency-aware delayed semantic-control gain**. In practice, stronger delayed routing interfaces can make a packet look more stable at consume time even when the world/ego split itself contributes little to preserving the same executable thread.
(36) Recent structured and addressable world-model advances also remain easy to overmerge: **world/ego factorization** can improve long-horizon organization, **object-addressable slots** can reduce referent drift, and **compact JEPA-style refresh** can densify rescoring, but current reporting rarely keeps these as separate bounded support families before asking whether any residual truly improves consume-honest handoff survival.
(37) Recent memory-augmented VLA/world-model hybrids show that long-horizon execution quality often depends on whether the model can explicitly preserve retrieved history and imagined near-future context, yet deployment-oriented supervisors still do not expose this temporal-context preservation as a packet-level accountability field.
(38) Contact-aware action tokenization methods further suggest that downstream handoff failure can arise even when object identity and thread identity are preserved, if the packet loses the local motion/contact semantics needed for consume-time control binding.
(39) Existing deployment-time evaluation therefore still under-specifies whether a refreshed packet preserves the **same temporal episode context** and **same contact-intent semantics** across emit, refresh, bind, and consume, making long-horizon gains from memory or image-action representations easy to misattribute to generic ranking improvements.

### 3.33 World/Ego Thread Preservation versus Latency-Aware Delayed Control

Recent local evidence from WEM [REF: 2605.19957], LeJEPA [REF: 2511.08544], and OA-WAM [REF: 2605.06481] suggests that D01 needs a sharper distinction between **structural thread preservation** and **latency-tolerant delayed semantic routing**. WEM factorizes long-horizon embodied behavior into world-side and ego-side latent structure, clarifying how task progress may remain coherent even when embodiment-specific execution details drift. LeJEPA strengthens the representation side by showing that a compact JEPA-style predictor can preserve semantically meaningful latent organization with much cheaper refresh and cleaner dynamics modeling. OA-WAM complements both by preserving object/action addresses under perturbation. However, our local QMD retrieval for `world model delayed consumption slot identity refresh semantics LeWorldModel OA-WAM` primarily returns TIC-VLA-style delayed semantic-control interface evidence rather than a pure D01 family, which is a warning sign: better world/ego structure can be easily confused with merely stronger controller-side tolerance to stale semantic packets.

We therefore introduce a matched subtraction tuple

\[
\kappa_t = (q_t^{\text{world/ego-thread}},\; q_t^{\text{latency-aware-route}},\; q_t^{\text{stale-semantic-support}},\; q_t^{\text{bind-honest}},\; q_t^{\text{consume-honest}}),
\]

where `world/ego-thread` measures whether the factored latent state truly preserves the same executable thread across refresh and reroute, `latency-aware-route` measures how much gain can already be explained by a delayed semantic-control interface that exposes slow semantics to a fast controller, `stale-semantic-support` measures whether the packet still benefits from stale-but-still-useful high-level cues, and the last two terms keep the usual downstream accountability split. A positive `world/ego-thread` score is only meaningful if it survives subtraction against `latency-aware-route` and `stale-semantic-support`; otherwise the gain is frozen below packet-contract promotion as **world/ego structuring support** rather than true delayed-consumption supervisory progress.

Operationally, this gives D01 a more honest interpretation boundary for structured world models. If WEM-style factorization improves bind and consume metrics only because the downstream controller becomes better at tolerating old semantics, then the gain should remain attributed to a **latency-aware routing interface**, not to the world model's packet contract. If LeJEPA-style compact refresh merely densifies rescoring while the same stale semantic route remains viable, the gain should freeze as **refresh-stable latent support**. Only when a structured world model still improves consume-honest packet survival after subtracting delayed-route tolerance do we credit it as **world/ego thread-preserving handoff gain**.

### 3.34 Current Evidence-Consistent Freeze after WEM / LeJEPA / OA-WAM Re-read

After re-reading the strongest recent local anchors, the most honest current freeze for D01 is to keep three bounded support families separate rather than merging them into an oversized “structured world model solves deployment-time supervision” narrative. **WEM** [REF: 2605.19957] currently supports a **world/ego thread-structuring** subclaim: it helps explain how world-side and ego-side trajectories can stay better organized over long horizons, but this is still weaker than proving delayed consume-time packet honesty. **OA-WAM** [REF: 2605.06481] currently supports an **identity-preserving slot** subclaim: it reduces referent drift and sharpens object/clause address stability, but this is still weaker than proving that the same address remains executable through downstream bind and consume. **LeJEPA / LeWorldModel-style compact JEPA predictors** [REF: 2511.08544, 2603.19312] currently support a **refresh-stable latent** subclaim: they plausibly make refresh cheaper, denser, and semantically cleaner, but this is still weaker than proving that more refresh actually changes consume-honest handoff outcomes.

This freeze is intentionally conservative. It means D01 should not yet claim that recent structured or addressable world models have solved the deployment-time supervisor problem. At the current evidence level, the strongest honest narrative is that they provide three complementary supports—thread structuring, identity preservation, and refresh stability—that may make a packet supervisor *more diagnosable* and *more auditable*, while the decisive unresolved question remains whether those supports survive subtraction against delayed semantic-control interfaces and still improve true consume-honest packet survival.

### 3.35 Bind-Honest versus Consume-Honest Accountability Matrix

To prevent controller-side overclaim, we make downstream handoff accountability explicitly two-layered. A packet that survives verifier acceptance and reaches the controller still passes through two different tests: **bind** and **consume**. **Bind** means the downstream controller can attach the packet to its current execution context without immediate envelope, syntax, or timing rejection. **Consume** is stricter: the local interaction stack must actually execute the packet while preserving the same executable clause, remaining-plan relation, and stage-consistent interaction value. In practice, many false positives live in the gap between these two moments.

We therefore record two separate downstream horizons for every released packet: the **last honest bind window** and the **last honest consume window**. A packet is *bind-honest* if it still preserves stage tag, clause identity, and remaining-plan compatibility at controller attachment time; it is *consume-honest* only if those properties remain valid when the local interaction stack actually uses the packet under contact, timing, and execution-pressure conditions. This yields a downstream accountability tuple

\[
\beta_t = (w_t^{\text{first+}},\; w_t^{\text{bind}},\; w_t^{\text{consume}},\; \upsilon_t,\; \rho_t,\; \chi_t),
\]

where \(w_t^{\text{first+}}\) is the first positive window, \(w_t^{\text{bind}}\) is the last bind-honest window, \(w_t^{\text{consume}}\) is the last consume-honest window, \(\upsilon_t\) is the consumption-time thread label, \(\rho_t\) is the compressed remaining-plan field, and \(\chi_t\) is the clause-compatibility score seen by the downstream consumer.

The reporting rule is intentionally conservative. If a result is positive only through \(W0\), it may support at most **planner-side semantic gain**. If it survives to \(W1\), it may support **runtime continuity gain**. If it reaches controller bind but not true consume, it is frozen at **controller-bind gain** even when attachment appears stable. Only when the packet remains honest through actual consume—while simultaneously preserving `SOR`, `CCH`, `MRP`, `T12`, `B2`, and `CTTPR`—may the paper escalate the claim to **full deployment-time handoff-value gain**. This rule ensures that controller attachment success is never allowed to borrow explanation power from genuine local interaction consumption.

## 3.25 Identity-Preserving Packet Addressing

Delayed-consumption supervision is not only about whether a packet stays fresh long enough to be consumed; it is also about whether the packet still points to the **same executable referent** when consumption finally happens. We therefore augment the safety packet with an explicit addressable identity layer that separates *who/what the packet is about* from *the time-varying execution content attached to it*. Concretely, each packet carries an identity tuple

\[
\alpha_t = (a_t^{\text{obj}},\; a_t^{\text{anchor}},\; a_t^{\text{clause}},\; a_t^{\text{thread}}),
\]

where `obj` denotes the manipulated object slot, `anchor` denotes the local spatial/relational anchor, `clause` denotes the next executable subgoal clause, and `thread` denotes the running progress thread expected by the downstream consumer. The supervisor is allowed to refresh timing margins, feasibility scores, or local geometric corrections only if the address tuple remains stable or the change is explicitly reported as a controlled reroute.

This design is inspired by OA-WAM [REF: 2605.06481], which preserves robot/object identity through address vectors separated from mutable slot content. Our use is different: we do not adopt object-addressable slots merely to improve manipulation robustness, but to prevent a more subtle deployment error in aerial supervision. A packet may remain rank-positive, feasibility-positive, and even bind-honest while quietly shifting from one nearby object or clause target to another. In that case, the failure is neither pure freshness loss nor pure controller failure; it is an **identity drift under delayed consumption**. MoLA [REF: 2605.12167] adds a complementary constraint on the action side: even when object/clause identity is preserved, downstream execution can still fail if the imagined future is decoded into a semantically correct but control-weak latent action. We therefore treat identity preservation and latent-action decode honesty as two coupled conditions for trustworthy packet reuse.

We therefore define an identity-preservation predicate

\[
\iota_t = \mathbb{I}[d(\alpha_t, \alpha_t^{\downarrow}) \leq \epsilon_{\alpha}],
\]

where \(\alpha_t^{\downarrow}\) is the downstream consumer's expected address tuple and \(d\) compares object identity, anchor relation, clause continuity, and thread continuity. A packet can only be counted as truly consume-honest if both clause-compatibility and identity preservation remain positive at consume time. If identity fails but feasibility remains positive, the event is frozen as **address-drifted bind gain** rather than full handoff gain. This gives D01 a stricter route for honest reporting: surviving delayed consumption now requires not just executable timing validity, but also stable object/anchor/clause reference across refresh, bind, and consume.

### 3.26 Refresh-Budget Attribution: Proposal Gain versus Handoff Gain

Fast latent predictors are attractive for D01 because they can increase how often the supervisor refreshes packet validity before downstream execution. However, a higher refresh rate is not automatically equivalent to stronger deployment-time supervision. We therefore introduce an attribution rule that separates **proposal-side refresh gain** from **true downstream handoff gain**. Let a refresh sequence produce packets \(\mathcal{P}_{t}^{(0)}, \mathcal{P}_{t}^{(1)}, \dots, \mathcal{P}_{t}^{(K)}\) before final controller use. For each refresh index \(k\), we separately record whether the update improved (i) planner-side ranking and feasibility discrimination, (ii) controller-side bind honesty, and (iii) local consume-time honesty:

\[
\Delta^{(k)} = (\Delta r^{\text{rank}}_k,\; \Delta h^{\text{bind}}_k,\; \Delta h^{\text{consume}}_k).
\]

This decomposition matters because lightweight JEPA-style predictors such as LeWorldModel [REF: 2603.19312] mainly promise **faster latent refresh and cheaper planning throughput**, whereas latent-action mixture interfaces such as MoLA [REF: 2605.12167] mainly promise **more executable decoding of imagined futures**. In D01, neither improvement is allowed to directly upgrade the paper's main claim unless it survives delayed downstream use. A refresh loop that repeatedly raises ranking quality but leaves \(\Delta h^{\text{consume}}_k \approx 0\) is credited only as **proposal-side semantic gain**; a loop that improves bind honesty but not consume honesty is frozen as **controller-attachment gain**. Only refresh updates that measurably increase consume-honest packet survival while preserving clause identity, thread continuity, and remaining-plan compatibility may be counted as **refresh-enabled handoff gain**.

Operationally, this lets D01 use fast world-model refresh as a controlled experimental variable rather than a vague systems advantage. We can now ask whether more frequent packet regeneration truly rescues delayed consumption, or merely makes the supervisor look sharper at release time.

### 3.27 Slot-to-Consume Identity Audit and Decode-Honesty Coupling

Recent local evidence from OA-WAM [REF: 2605.06481] and LeWorldModel [REF: 2603.19312] sharpens a deployment-time distinction that D01 should make explicit. OA-WAM shows that persistent object-address vectors can stabilize **which entity** a manipulation model is acting on under perturbation, while LeWorldModel shows that compact JEPA-style latent dynamics can make packet refresh dramatically cheaper and more frequent. Put together, these results imply a subtle but important supervisory risk: faster refresh may regenerate packets more often, and object-addressable slots may preserve representation-level identity better, yet the downstream stack can still lose the packet's executable meaning if **emitted slot identity**, **refreshed slot identity**, **bound slot identity**, and **consumed slot identity** are not audited under the same clause and decode interface.

We therefore extend the D01 packet contract with a slot-to-consume identity audit tuple

\[
\eta_t = (s_t^{\text{emit}},\; s_t^{\text{refresh}},\; s_t^{\text{bind}},\; s_t^{\text{consume}},\; q_t^{\text{decode}}),
\]

where the first four fields denote the object-addressable slot selected at packet release, after refresh, at downstream bind, and at final local consume, respectively, and \(q_t^{\text{decode}}\) denotes a decode-honesty score measuring whether the latent action interface still maps the refreshed packet to the same executable operational meaning. The first four terms audit *referent preservation*; the fifth audits whether the action-side interface silently weakens or shifts the packet even when the referent remains stable.

This audit gives D01 a more honest interpretation boundary for fast-refresh world models. A LeWorldModel-style predictor may improve refresh density and planner-time rescoring, and an OA-WAM-style address space may reduce slot drift under perturbation, but neither should be credited as delayed-consumption progress unless the slot lineage remains aligned through consume and the latent action interface remains decode-honest at use time. Accordingly, if slot lineage is preserved through bind but breaks at consume, we freeze the gain as **address-stable bind support**. If slot lineage remains stable but decode honesty collapses, we freeze the gain as **identity-preserved decode-fragile support**. Only when both slot lineage and decode honesty survive consume do we allow the evidence to promote a stronger **consume-honest identity-preserving handoff** claim.

### 3.28 Semantics-Aware Slot Screening versus Consume-Time Preservation

Recent evidence on robotic latent-space selection suggests that semantically useful representations can substantially improve world-model utility even when they do not maximize pixel reconstruction fidelity. Semantic Latent Space World Models [REF: 2605.06388] shows that semantically oriented encoders such as V-JEPA-style or DINO-style representations can outperform reconstruction-heavy latents on policy-relevant evaluation, which is highly relevant for D01 because our supervisor must rank and screen packets according to executable downstream value rather than visual realism alone. However, this gain should be interpreted carefully: a more semantic latent can improve planner-side discrimination, retrieval of the correct action-relevant object manifold, and stage-local scoring, while still failing to preserve the same packet meaning at delayed downstream consume.

We therefore introduce a semantics-aware screening tuple

\[
\sigma_t = (q_t^{\text{sem-rank}},\; q_t^{\text{slot-match}},\; q_t^{\text{clause-link}},\; q_t^{\text{decode-honest}},\; q_t^{\text{consume-honest}}),
\]

where `sem-rank` measures whether the latent supports better policy-relevant ranking, `slot-match` measures whether the semantic latent still points to the intended object/anchor slot, `clause-link` measures whether the selected latent state preserves the same executable subgoal clause, `decode-honest` measures whether the downstream action interface still maps the latent packet to the intended control semantics, and `consume-honest` measures whether all of the above survive actual local consume. This tuple lets D01 separate **semantic screening gain** from **semantic consume-time preservation**. A stronger semantic latent may correctly re-rank futures and improve early-stage filtering, yet if `slot-match` or `clause-link` breaks after refresh, or if the downstream action interface weakens at consume time, the gain must remain frozen below full handoff credit.

This section sharpens the paper's core argument in a way that is especially useful for aerial manipulation. The real question is not whether semantic latent spaces are better in general, but whether they help the supervisor preserve the same executable packet across refresh, bind, and consume under time pressure. Accordingly, D01 only upgrades semantic-latent improvements to packet-contract evidence when they jointly improve ranking, slot stability, clause continuity, and delayed-consumption honesty. Otherwise, they are reported conservatively as **planner-side semantic screening gain** or **identity-helpful but consume-fragile support**, rather than being overstated as full deployment-time supervisory progress.

### 3.29 Consume-Time Semantics Audit under Delayed Semantic-Control Interfaces

The latest local retrieval signal also suggests a concrete cross-direction caution for D01. QMD recall for `world model semantic latent consume honest packet delayed consumption` primarily returns **TIC-VLA** and other delayed semantic-control interface evidence instead of a clean D01-only world-model family, reinforcing that semantically stronger latent states are easy to confuse with merely better *late semantic routing*. For D01, this means a semantic latent should not be credited just because it improves planner-side matching, route selection, or stage-local action plausibility under a delayed-control stack. It must still survive the same delayed downstream consume boundary that TIC-VLA-style interface work explicitly warns about.

We therefore add a consume-time semantics audit tuple

\[
\zeta_t = (q_t^{\text{sem-rank}},\; q_t^{\text{route-stale}},\; q_t^{\text{slot-stable}},\; q_t^{\text{decode-honest}},\; q_t^{\text{consume-honest}}),
\]

where `route-stale` measures whether a semantic latent's apparent gain can already be explained by a delayed semantic-control interface that exposes stale-but-still-useful routing information, rather than by a genuinely stronger packet contract. The reporting rule is deliberately conservative. If a semantic latent only improves `sem-rank` while leaving `route-stale` high, the gain is frozen as **planner-side semantic routing support**. If `slot-stable` and `decode-honest` improve but `consume-honest` still collapses under delayed uptake, the result is frozen as **address-stable semantic support** rather than full handoff progress. Only when the semantic latent simultaneously reduces stale-route dependence and improves true consume-time honesty may D01 promote it to **packet-contract evidence**.

This addition matters because D01 increasingly sits next to D02-style latency-aware semantic-control interfaces in the local knowledge base. By explicitly auditing `route-stale` against consume-time honesty, we keep the paper honest about a subtle but important boundary: **better semantic latents may help choose a packet, but they do not automatically prove that the packet remains executable when the downstream controller finally consumes it**.

### 3.30 Slot-Lineage Preservation versus Refresh-Frequency Gain

Two recent local anchors sharpen a second reporting boundary that D01 should make explicit. **OA-WAM** [REF: 2605.06481] shows that object-addressable slots can preserve referent identity under perturbation, while **LeWorldModel** [REF: 2603.19312] shows that compact JEPA-style latent predictors can make refresh dramatically cheaper and denser. Put together, these results create a tempting but potentially misleading narrative: if slot identity is better preserved and packets can be refreshed much more often, then delayed-consumption supervision must be better. Our local evidence suggests this implication is too strong. Better slot identity may only improve *who the packet refers to*, and faster refresh may only improve *how often the packet is rescored*; neither automatically proves that the same executable clause survives all the way to downstream consume.

We therefore introduce a slot-lineage preservation tuple

\[
\lambda_t = (s_t^{\text{emit}},\; s_t^{\text{refresh}},\; s_t^{\text{bind}},\; s_t^{\text{consume}},\; f_t^{\text{refresh-gap}},\; h_t^{\text{consume}}),
\]

where the first four terms track the object-addressable slot lineage across release, refresh, controller bind, and final local consume; `refresh-gap` records how much the packet's apparent gain can already be explained by denser refresh opportunities alone; and `consume` records whether the final slot lineage still preserves executable meaning at actual use time. This tuple lets D01 distinguish **slot-lineage preservation gain** from **refresh-frequency gain**. If slot lineage remains stable through bind but consume honesty still collapses, the improvement is frozen as **address-stable bind support**. If denser refresh improves ranking and bind success but the residual disappears once refresh-gap is subtracted, the effect is frozen as **refresh-density support**. Only when stable slot lineage and residual consume honesty remain positive after subtracting refresh-frequency gain do we allow the result to count as **consume-honest slot-preserving handoff gain**.

This distinction is especially important for our deployment-time supervisor framing. D01 is not merely asking whether a world model can maintain identity or refresh cheaply in isolation; it asks whether those properties survive the full packet contract under delayed downstream uptake. By separating slot-lineage preservation from refresh-density gain, the paper stays honest about what has actually improved: referent robustness, rescoring throughput, or true handoff survival.

### 3.31 Semantic-Screening, Refresh-Density, and Stale-Route Subtraction before Packet-Contract Promotion

The latest local re-read makes one failure mode especially clear: D01 now has strong evidence that **semantic latent screening** can improve policy-relevant ranking [REF: 2605.06388], that **compact JEPA-style predictors** can make refresh much cheaper [REF: 2603.19312], and that **asynchronous refresh pipelines** can hide a meaningful portion of inference latency behind execution [REF: 2604.16484]. However, these three gains live at different layers of the stack, and none of them should be allowed to directly promote a result to packet-contract progress. A stronger semantic latent may only improve which proposal is chosen; a faster predictor may only increase how often rescoring happens; an async refresh loop may only preserve stale-but-still-useful route hints at bind time. If these gains are not explicitly subtracted, delayed-consumption supervision becomes easy to overclaim.

We therefore define a promotion-subtraction tuple

\[
\psi_t = (\Delta q_t^{\text{sem-rank}},\; \Delta r_t^{\text{refresh-density}},\; \Delta s_t^{\text{stale-route}},\; \Delta h_t^{\text{bind}},\; \Delta h_t^{\text{consume}}),
\]

where `sem-rank` measures improvement in semantic ranking quality, `refresh-density` measures how much extra proposal opportunity comes purely from faster or more frequent refresh, `stale-route` measures how much of the apparent downstream gain can already be explained by better delayed semantic routing without a stronger packet contract, `bind` measures controller-attachment honesty, and `consume` measures true delayed-consumption honesty. The interpretation rule is intentionally asymmetric: positive gains in `sem-rank`, `refresh-density`, or stale-route reduction are treated as **supporting upstream evidence**, while only the residual that survives after subtracting those gains may be credited to packet-contract progress.

Operationally, this means D01 uses a stricter promotion ladder. If a method improves `sem-rank` and refresh density but leaves `consume-honest` unchanged, the result freezes at **proposal-side semantic-refresh support**. If it improves bind honesty after async refresh, but the effect disappears once stale-route support is subtracted, the result freezes at **interface-side delayed-routing support**. Only when a method still improves delayed consume honesty after removing semantic ranking gain, refresh-density gain, and stale-route support may D01 promote it as **true packet-contract evidence**. This rule is especially important for the current D01 draft because LeWorldModel, Semantic Latent Space World Models, and DexWorldModel together create a highly tempting but potentially misleading story: that sharper semantics plus faster refresh must imply better delayed-consumption supervision. Our paper argues that this implication is false unless the residual survives actual downstream consume.

### 3.32 Unified World-Language-Action Backbone versus Deployment-Time Packet Contract

A very recent local anchor, **WLA-0** [REF: 2606.05979], strengthens an adjacent but non-identical explanation for D01-style gains. WLA-0 unifies world modeling, language reasoning, and action synthesis inside one autoregressive backbone, and further allows test-time world prediction to be switched on for stronger multi-step reasoning. This is highly relevant because such a unified backbone can improve subtask decomposition, proposal quality, and local action continuity without explicitly solving the harder deployment question that motivates D01: whether a released packet stays **identity-consistent, expiry-honest, and consume-honest** when it is delayed, rebound, or locally repaired before actual downstream use.

We therefore introduce a matched subtraction tuple

\[
\omega_t = (q_t^{\text{unified-backbone}},\; q_t^{\text{world-prediction-scale}},\; q_t^{\text{subgoal-consistency}},\; q_t^{\text{bind-honest}},\; q_t^{\text{consume-honest}}),
\]

where `unified-backbone` measures gains that can already be explained by jointly modeling language, world, and action inside one shared transformer, `world-prediction-scale` measures improvements attributable to enabling extra test-time world rollout or reasoning depth, `subgoal-consistency` measures whether the model preserves coherent local subgoal structure across long horizons, and the final two terms keep the D01 downstream accountability split. The key reporting rule is conservative: if a method mainly improves `unified-backbone`, `world-prediction-scale`, or `subgoal-consistency`, then its gain is frozen as **integrated reasoning-and-action support** unless a positive residual remains at true delayed consume.

Operationally, this prevents D01 from borrowing explanatory power from WLA-style integrated architectures too early. A WLA-like model may look better because it emits cleaner subtask text, more coherent subgoal images, or more stable action continuations, yet these strengths can still live entirely on the proposal side. If a packet remains vulnerable to delayed expiry, referent drift, or consume-time semantic collapse, the result should not be promoted to deployment-time packet-contract progress. Only when a unified world-language-action backbone still improves `consume-honest` survival after subtracting proposal-side reasoning and subgoal-coherence gains do we credit it as evidence for a stronger supervisor.

### 3.33 World/Task-Factored Packet Contract

A fresh external scan also surfaced **World-Task Factorization for Robot Learning** [REF: 2606.02027], which argues that one of the most fundamental decompositions in robotics is to separate *world factors*—embodiment and environment properties that exist independently of intent—from *task factors*—logic imposed by the current objective. For D01, this is interesting not as a replacement for world models, but as a clean way to sharpen our deployment-time packet contract. Much of the current delayed-consumption ambiguity comes from mixing these two sources of change: some packet failures happen because the world state truly drifted, while others happen because the task-side clause, priority, or local logic shifted even though the world-side estimate remained stable.

We therefore refine the safety packet into a factored tuple

\[
\pi_t = (z_t^{\text{world}},\; z_t^{\text{task}},\; a_t^{\text{addr}},\; b_t^{\text{budget}},\; e_t^{\text{expiry}}),
\]

where `world` summarizes flight/manipulation dynamics and environment state, `task` summarizes the currently valid executable clause and remaining-plan logic, `addr` is the identity-preserving address tuple introduced earlier, `budget` is the stage-scoped risk budget, and `expiry` records time-validity. This decomposition lets the supervisor report a more honest failure mode at handoff time: a packet may fail because the world-side latent has become stale, because the task-side clause has been rerouted, or because the world/task split remains individually valid but their coupling no longer supports the same executable thread.

This distinction matters for aerial manipulation because delayed-consumption repair can otherwise hide behind aggregate confidence. A refresh may improve world-state prediction without preserving the same task clause, or a clause-preserving reroute may still bind to a world state whose contact geometry or flight envelope has drifted. Under the factored packet contract, D01 only credits a refresh as **progress-preserving handoff gain** when both `z^{world}` and `z^{task}` remain jointly honest through bind and consume. If only the world factor is rescued, the gain freezes as **world-state refresh support**; if only the task factor is preserved, the gain freezes as **task-clause continuity support**. This gives the PAPER a cleaner method-level explanation for why some refresh loops help ranking or short-window repair but still fail to protect the same executable packet at true downstream consume.

### 4.2.8 World-Factor versus Task-Factor Handoff Attribution

To test the world/task-factored packet contract, we introduce an attribution benchmark that perturbs delayed-consumption packets along two orthogonal axes: (i) **world drift**, including object pose changes, contact-state perturbation, and aerial envelope drift; and (ii) **task drift**, including clause reroute, local-goal substitution, and remaining-plan compression mismatch. For each packet, we measure whether a refresh rescues the world factor only, the task factor only, both jointly, or neither. The key metrics are world-honest bind rate, task-honest bind rate, joint consume-honest rate, and factor-specific false-promotion rate.

This experiment is designed to prevent a common overclaim in D01-style supervision. A system can look strong if it repeatedly repairs geometry while silently changing the task clause, or if it preserves clause continuity while relying on stale world estimates. We therefore only allow a result to count as **full handoff preservation** when the refreshed packet remains jointly honest in both factors at consume time. Otherwise, the gain is reported conservatively as world-side rescue or task-side continuity support. This attribution study complements the earlier bind-versus-consume and semantic-subtraction analyses by showing *which side of the packet contract actually survived*.

### 3.33 Grounded Semantics versus Latency-Aware Delayed Control

A second local convergence point is that **stronger semantic grounding** and **latency-aware delayed control** are adjacent but not equivalent explanations for downstream success. Grounded World Model [REF: 2604.11751] shows that cluttered language-guided manipulation becomes more stable when semantic relations are embedded directly into latent dynamics and then queried through imagined rollout and MPC. TIC-VLA [REF: 2602.02459], by contrast, demonstrates that much of deployment robustness can come from explicitly exposing delayed semantic state and latency metadata to the controller, even without a world-model-style packet contract. For D01, this creates a real attribution risk: a packet may look more semantically correct simply because the control stack became more delay-aware, or more delay-tolerant simply because the world model grounded the clause better before release.

We therefore add a grounding-versus-latency audit tuple

\[
\phi_t = (q_t^{\text{ground}},\; q_t^{\text{latency}},\; q_t^{\text{stale-route}},\; q_t^{\text{thread}},\; h_t^{\text{consume}}),
\]

where `ground` measures whether the world model preserves the intended semantic relation and object/anchor clause before release, `latency` measures how much of the downstream gain can already be explained by a delayed semantic-control interface, `stale-route` measures whether the packet remains merely useful as a stale routing hint, `thread` measures whether the same remaining-plan thread is preserved across refresh and uptake, and `consume` records whether those advantages survive actual local consume. This tuple prevents D01 from conflating semantically grounded world-state prediction with delayed-control robustness.

The reporting rule is conservative. If a method improves semantic grounding but most of the downstream gain disappears once latency-aware control is matched, the result freezes as **grounding support under delayed control**. If a method improves delay tolerance but clause and anchor identity remain fragile, the result freezes as **latency-aware routing support**. Only when semantically grounded latent prediction continues to improve consume-honest packet survival *after* delayed-control benefits have been subtracted may D01 promote the gain to **grounded packet-contract evidence**. This is especially important for our deployment-time supervisor framing, because D01 increasingly sits beside D02-style latency-aware interfaces in the local knowledge base: stronger grounding and stronger delay tolerance are both valuable, but they should enter the paper through distinct explanatory ceilings.

### 3.35 World/Ego Thread Preservation versus Latency-Aware Delayed Control

Recent local evidence makes a final D01 attribution boundary more explicit. **WEM** [REF: 2605.19957] argues that long-horizon hybrid embodied tasks become easier when the model explicitly separates *world evolution* from *ego evolution*, while **TIC-VLA** [REF: 2602.02459] shows that much of delayed-control robustness can come from exposing semantic latency and stale-control state directly to the controller. These two gains are adjacent but not equivalent. A packet may survive delayed downstream use because the world/ego decomposition preserves the correct execution thread, or because a latency-aware semantic-control interface simply helps the controller interpret stale information more gracefully. Without subtracting the second explanation, D01 risks over-crediting world/ego structuring for gains that are really delayed-interface gains.

We therefore define a world/ego-versus-latency attribution tuple

\[
\kappa_t = (q_t^{\text{world/ego-thread}},\; q_t^{\text{latency-aware-route}},\; q_t^{\text{stale-semantic-support}},\; q_t^{\text{bind-honest}},\; q_t^{\text{consume-honest}}),
\]

where `world/ego-thread` measures whether the packet preserves the same executable thread after separating world-side and ego-side evolution, `latency-aware-route` measures how much of the downstream gain can already be explained by a delayed semantic-control interface, `stale-semantic-support` measures whether the packet remains merely useful as a stale routing hint, and the final two terms record bind-honest and consume-honest survival. This tuple lets D01 ask a sharper question: does world/ego disentanglement really preserve the same downstream thread, or does it only look better because the control stack has become more delay-aware?

The promotion rule is intentionally conservative. If world/ego separation mainly improves planner-side prediction or bind-time stability while `latency-aware-route` remains high, the gain is frozen as **world/ego structuring support under delayed control**. If `bind-honest` improves but `consume-honest` does not survive once latency-aware support is matched, the result is frozen as **thread-shaped bind support**. Only when world/ego separation still improves consume-honest packet survival after subtracting latency-aware delayed-control gain may D01 promote the result to **world/ego thread-preserving packet-contract evidence**. This section sharpens the paper's core claim: faster refresh, cleaner semantics, and better delayed routing are all useful, but the D01 thesis only truly advances when the same executable thread survives through actual downstream consume.

### 3.36 Current Evidence-Consistent Freeze after WEM / LeJEPA / OA-WAM Re-read

After re-reading the recent local anchors **WEM** [REF: 2605.19957], **LeJEPA** [REF: 2511.08544], and **OA-WAM** [REF: 2605.06481], the most defensible D01 freeze is now clearer. **WEM** strengthens the need to audit whether world-side and ego-side evolution remain aligned to the same downstream execution thread in hybrid embodied tasks. **OA-WAM** sharpens the identity side of that audit by showing that slot-address preservation can stabilize object-level referents under perturbation, but does not by itself prove consume-honest packet survival. **LeJEPA** strengthens a third, complementary point: compact JEPA-style latent predictors may reduce heuristic burden and increase refresh stability, yet they still do not directly show whether faster or cleaner latent refresh preserves bind-honest and consume-honest packet meaning.

Accordingly, D01 should not yet promote these lines as direct proof of a solved deployment-time supervisor. Instead, they currently support three bounded subclaims: **world/ego thread-structuring support** (WEM), **identity-preserving slot support** (OA-WAM), and **refresh-stable latent support** (LeJEPA). Any result that can already be explained by one of these families must be matched and subtracted before being credited as full packet-contract progress. In practical writing terms, this means the current D01 headline should remain centered on a **time-sensitive deployment contract** rather than drifting into a broader "structured world models are better" story. The real contribution remains the same stricter one: a packet should only be counted as valuable when it survives refresh, bind, and consume while preserving executable thread, clause identity, and remaining-plan continuity under delayed downstream uptake.

where `world` and `ego` denote the separated latent branches used for environment evolution and agent evolution, `refresh` measures how much apparent gain is attributable merely to denser JEPA-style refresh, `thread` measures whether the same executable progress thread is preserved across release/refresh/bind/consume, and `consume` records whether the packet still carries the same usable meaning when locally consumed. This tuple lets D01 distinguish **structural disentanglement gain** from **refresh-density gain** and from **true thread-preserving handoff gain**.

The rule is again strict. If world/ego separation improves planner-side prediction quality but the same downstream thread is not preserved, the result freezes as **structure-aware screening support**. If fast JEPA refresh improves rescoring density but not consume-honest thread preservation, it freezes as **refresh-density support**. Only when world/ego separation remains aligned to the same thread *and* survives actual consume after subtracting refresh-density gain may D01 promote the result to **thread-preserving world/ego packet-contract evidence**. This gives the paper a sharper next-step contribution boundary: D01 is not just about faster latent world models or cleaner structural decomposition, but about whether those advantages survive the delayed-consumption boundary as an honest deployment-time supervisory contract.

## 4. Experiments

### 3.32 Adaptive Gating and World/Ego Separation as Packet-Contract Priors

Recent local anchors suggest that two seemingly separate lines—**adaptive expert gating** and **world/ego disentanglement**—should be treated as priors for packet-contract design rather than merely as model-side performance tricks. HarmoWAM [REF: 2605.10942] shows that predictive and reactive experts can be switched online according to interaction phase, yielding stronger zero-shot generalization without sacrificing precise contact behavior. WEM [REF: 2605.19957] separately argues that long-horizon hybrid tasks become easier to model when environment evolution and agent evolution are disentangled into distinct but coupled latent streams. For D01, these results jointly imply that packet honesty may depend not only on *what future is predicted*, but also on **which expert family is authorized to speak for which stage**, and on whether the packet preserves a clean separation between world-side state change and ego-side execution commitment.

We therefore introduce a stage-gating/world-ego audit tuple

\[
\omega_t = (g_t^{\text{stage}},\; e_t^{\text{expert}},\; q_t^{\text{world}},\; q_t^{\text{ego}},\; h_t^{\text{consume}}),
\]

where `stage` records the current deployment phase, `expert` records whether the packet was produced or refreshed under predictive, reactive, or hybrid gating, `world` measures whether world-side latent evolution remains clause-consistent, `ego` measures whether the executor-side progress thread remains compatible with the same remaining plan, and `consume` records whether both survive actual downstream use. This tuple gives D01 a sharper explanation boundary. A HarmoWAM-style gate may improve local precision simply because the reactive expert is better at contact-rich finishing; a WEM-style separation may improve long-horizon prediction by clarifying navigation-versus-manipulation evolution; yet neither effect should be promoted to supervisory gain unless the packet still preserves the same clause identity and consume-time executable meaning under delayed uptake.

Operationally, we treat adaptive gating and world/ego separation as **contract priors**: they can justify why a packet should be refreshed differently across search, hover, re-anchor, approach, and inspect stages, but they do not automatically justify packet release. If a stage-specific gate improves bind honesty but not consume honesty, the gain freezes at **stage-local expert support**. If world/ego separation improves planner stability but the downstream executor still drifts off-thread, the gain freezes at **state-organization support**. Only when stage-aware gating and world/ego separation jointly improve delayed-consumption honesty may D01 promote them to true packet-contract evidence.

### 3.1 System Overview

We propose a world model-based deployment-time supervisor for aerial manipulation. The system operates between the high-level planner and the low-level controller, providing pre-execution safety screening and stage-aware action routing. Given a candidate action packet from the planner, the supervisor outputs a `Pre-Execution Safety Packet` containing: `rank_score` (deployment confidence), `failure_state` ∈ {pass, F1_known_failure, F2_anomaly}, `route_action` ∈ {continue, hover_hold, packet_repair, fallback, human_review}, `stage_tag` ∈ {search, hover, re-anchor, approach, inspect}, and `risk_budget`.

### 3.2 Dual-Dynamics World Model (C1)

We treat aerial manipulation as a **coupled dual-dynamics prediction problem** rather than a standard single-body manipulation problem. The world model maintains a shared latent state

\[
\mathbf{z}_t = [\mathbf{z}^{\text{scene}}_t,\; \mathbf{z}^{\text{flight}}_t,\; \mathbf{z}^{\text{ee}}_t,\; \mathbf{z}^{\text{contact}}_t,\; \mathbf{z}^{\text{intent}}_t],
\]

where scene, flight, end-effector, contact, and intent are explicitly factorized. The transition model receives packet actions and stage tags, and predicts latent evolution with dynamics, progress, feasibility, and reachability heads. Training combines forward prediction, inverse consistency, progress consistency, executability-aware feasibility losses, and a horizon-matched reachability objective that teaches the model to distinguish futures that merely end near the target in latent space from futures that are actually reachable under the allotted execution horizon.

Recent evidence from semantic-latent world modeling and latent-model-predictive control sharpens an important boundary for D01. Semantic Latent Space World Models [REF: 2605.06388] suggest that higher-level semantic latent structure can improve screening and imagined future discrimination under partial observability, while Dream-MPC [REF: 2605.04568] shows that gradient-based latent planning can refine candidate action sequences more effectively than simpler proposal mechanisms. TRM [REF: 2605.22164] adds an equally important planner-interface lesson: even with a usable latent dynamics model, the deployment stack can still fail if terminal ranking is based on Euclidean latent proximity rather than horizon-conditioned reachability. For D01, this means candidate scoring must be treated as its own contract surface rather than as a transparent readout of latent quality. However, neither stronger semantic representation, stronger latent planning, nor stronger reachability-aware reranking should be counted as deployment-time packet-contract progress by default. In D01, all three are treated as **upstream evidence generators** whose gains must still survive packet expiry, remaining-plan preservation, delayed downstream bind, and local consume-time honesty before they can be credited as true supervisory value.

Concretely, we separate four sources of improvement already at the model level: **representation gain** (better latent state organization and semantic screening), **planner gain** (better candidate optimization in imagination), **ranking-interface gain** (better horizon-matched future selection), and **packet-contract gain** (better preservation of executable meaning through release, refresh, bind, and consume). This separation is central to our aerial setting because a system can become much better at ranking futures or proposing recoverable trajectories while still failing to preserve the same clause identity once the downstream controller actually consumes the packet.

We intentionally keep the planner-side interpretation narrow. Dream-MPC [REF: 2605.04568] is therefore used in D01 as evidence for **proposal refinement under fixed packet semantics**, not as evidence that packet handoff itself has improved. Likewise, TRM [REF: 2605.22164] is used as evidence for **ranking-interface repair under fixed latent dynamics**, not as proof that better endpoint selection alone solves delayed-consumption supervision. A planner that optimizes latent trajectories more effectively, or a reachability head that reorders terminal futures more honestly, may reduce obviously bad proposals and increase rank quality; but unless the resulting packet also survives stage-scoped expiry, slot identity audit, and consume-time decode honesty, the gain remains frozen at planner-side or ranking-interface support.

### 3.3 Two-Stage Post-Training (C2)

Following EVA [REF: 2603.17808] and ABot-PhysWorld [REF: 2603.23376], we adopt a two-stage post-training protocol:

**Stage 1 — Physics Alignment**: We annotate training rollouts with physics plausibility labels and apply DPO post-training to suppress physically implausible predictions. Inspired by ABot-PhysWorld, these labels are not limited to generic realism judgments; they explicitly tag penetration, unsupported contact, anti-gravity motion, envelope-violating flight transitions, and other packet-relevant failure modes that can later explain why a candidate packet should be blocked, repaired, or escalated.

**Stage 2 — Executability Alignment**: We train an inverse dynamics model (IDM) on real UAV trajectories and use it as a reward model to evaluate Stage 1 outputs. The IDM reward penalizes velocity, acceleration, and jerk violations specific to the aerial platform. [TODO: 补充具体训练细节和损失函数]

A practical consequence of this design is that D01 does not treat physics alignment as a cosmetic regularizer. Instead, physics alignment provides packet-facing evidence for deployment-time release decisions. In particular, we require the supervisor to preserve a separation between **physical plausibility** and **action executability** at both training time and evaluation time, mirroring ABot-PhysWorld's EZSbench decomposition. A packet may look smoother after post-training yet still remain weakly executable under the current flight envelope; conversely, a packet may remain executable while drifting toward physically suspicious contact or pose transitions. By keeping these two signals decoupled, D01 avoids overstating physics-cleaned imagination as deployment-ready supervision.

### 3.4 Deployment-Time Supervisor Interface (C3)

We define a `Pre-Execution Safety Packet` as

\[
\mathcal{P}_t = \{s_t,\; \hat{\tau}_{t:t+H},\; r_t^{\text{rank}},\; f_t^{\text{feas}},\; a_t^{\text{anom}},\; g_t^{\text{stage}},\; b_t^{\text{risk}}\},
\]

where ranking, feasibility, anomaly, stage, and risk are explicitly separated. This design allows D01 to act as a deployment-time *supervisory packet generator* rather than a monolithic planner.

### 3.5 F1/F2 Failure Triage (C4)

We decompose failed candidate packets into two deployment-relevant categories. **F1 known failures** are nameable and recoverable errors that resemble patterns covered by training or synthetic counterfactual augmentation. **F2 anomalies** are out-of-distribution events whose causal explanation is unreliable under the current model. Packets with low rank but low anomaly are routed to F1 and remain eligible for bounded repair; packets with high anomaly are routed to F2 and escalated.

### 3.6 Hover-Bounded Recovery (C5)

We only activate recovery inside low-speed windows where the platform can safely pause, re-anchor, or make a short corrective maneuver. The recovery policy is trained using Dream2Fix-style counterfactual failure synthesis [REF: 2603.13528]. During search or cruise, the supervisor may still downgrade the route or request hover hold, but it does not execute aggressive online repair.

### 3.7 Stage-Consistent Packet Calibration

Packet routing should preserve **stage consistency** rather than only maximize an aggregate confidence score. A candidate packet can appear semantically promising while still being poorly timed for the current execution phase. We therefore calibrate packets using a stage-consistency term that combines intended stage transition, phase-envelope divergence, and anticipated downstream handoff mismatch.

### 3.8 Human-Corrective World-Model Branching

Inspired by Hi-WM [REF: 2604.21741], we attach a lightweight corrective branch to the supervisor packet interface. When a packet is classified as F1 and routed to `packet_repair` or `hover_hold`, the system stores the latent state, packet fields, imagined rollout, and failure annotation as a reusable correction anchor.

### 3.9 Stage-Bounded Corrective Memory and Branch Reuse

We further operationalize corrective branching with a **stage-bounded corrective memory** indexed by packet type and failure regime. Retrieval is gated by stage consistency and risk budget, so a correction remembered from a hover shell is not allowed to fire during high-speed search or under a different dynamics envelope.

### 3.10 Progress-Conditioned Remaining-Plan Compression

We augment the supervisory packet with a compressed remaining-plan field

\[
\rho_t = h_\psi(\mathbf{z}_t, g_t, \mathcal{I}_t, \mathcal{H}_t),
\]

which summarizes the next executable subgoal clause, expected local progress state, and minimal recovery-relevant context needed for packet repair or handoff. Instead of caching a long opaque history buffer, \(\rho_t\) keeps only the progress variables that matter for downstream continuity: local anchor identity, subgoal completion state, short-horizon trace hint, and repair-relevant stage context. This design is motivated by LoHo-Manip [REF: 2604.21924], which shows that long-horizon robustness improves when the system repeatedly refreshes an explicit remaining-plan representation rather than trusting stale hidden context.


### 3.11 Recovery-Aware Packet Repair Objective

We define packet repair as a constrained correction problem over both feasibility and progress continuity:

\[
\tilde{\mathcal{P}}_t = \arg\min_{\mathcal{P}' \in \Omega(g_t, b_t^{\text{risk}})}
\; \lambda_f \mathcal{L}_{\text{feas}}(\mathcal{P}')
+ \lambda_p \mathcal{L}_{\text{prog}}(\mathcal{P}', \rho_t)
+ \lambda_h \mathcal{L}_{\text{handoff}}(\mathcal{P}').
\]

A valid repair is not simply a safer packet; it is a safer packet that still preserves the intended local execution thread.

### 3.12 Stage-Scoped Risk Budgeting and Packet Expiry

We attach two additional control-facing variables to every packet: a **stage-scoped risk budget** and a **packet expiry rule**. Rather than treating `risk_budget` as a single abstract confidence field, we decompose it into

\[
b_t^{\text{risk}} = \{m_t^{\text{vel}},\; m_t^{\text{att}},\; m_t^{\text{pose}},\; w_t^{\text{corr}},\; \eta_t^{\text{esc}}\},
\]

where velocity margin, attitude excursion, pose tolerance, correction window, and escalation threshold are stage-dependent.

We also define a packet expiry condition so that stale supervisor outputs are not reused beyond their valid operating envelope. A packet expires when timeout, envelope drift, or stage mismatch is triggered. This turns D01 from a one-shot packet scorer into a **time-sensitive supervisory contract**.

### 3.13 Expiry-Aware Packet Handoff and Repair Gating

We define an expiry-aware handoff gate

\[
\pi_t^{\text{handoff}} = \mathbb{I}[r_t^{\text{rank}} > \delta_r] \cdot \mathbb{I}[f_t^{\text{feas}} > \delta_f] \cdot \mathbb{I}[\text{valid}(\mathcal{P}_t)=1],
\]

so that downstream release requires ranking, feasibility, and freshness to be jointly satisfied. If freshness alone fails, the event is routed to an **expiry-sensitive branch** that regenerates, re-ranks, or invalidates the packet before downstream consumption.

### 3.14 Expiry-Aware Packet Handoff Contract

We formalize packet handoff as an **expiry-aware supervisory contract** rather than a timeless confidence score. Each packet carries an explicit validity tuple containing stage, remaining-plan state, risk budget, timeout, drift threshold, and local anchor signature. D01 therefore guarantees that the packet it releases is still valid **for this stage, this envelope, and this local progress anchor**.

### 3.15 Progress-Consistent Commit Semantics

A packet should not be committed solely because it is individually feasible and fresh. It must also remain **progress-consistent** with the current execution thread. We therefore define a commit predicate

\[
\kappa_t = \mathbb{I}[\pi_t^{\text{handoff}} = 1] \cdot \mathbb{I}[\chi(\rho_t, \rho_t^{\downarrow}) > \delta_c],
\]

where \(\rho_t\) is the packet's compressed remaining-plan state and \(\rho_t^{\downarrow}\) is the downstream executor's expected local thread signature. The compatibility score \(\chi\) measures whether the released packet preserves the next executable clause, anchor relation, and short-horizon progress semantics expected by the consumer.

This extra commit layer matters because a packet may be feasible, high-ranked, and still fresh, yet remain **semantically off-thread** after refresh or reroute. By making commit explicitly depend on progress consistency, D01 supervises not only *whether a packet can still be executed*, but also *whether executing it would silently abandon the intended local plan*.

### 3.16 Thread-Safe Refresh and Downstream Commit Guard

We further refine deployment-time packet usage with a **thread-safe refresh guard** that sits between packet regeneration and downstream consumption. The key idea is that refresh alone is not enough: a regenerated packet can satisfy feasibility and freshness checks while still drifting away from the local execution thread that the downstream controller is already following. We therefore distinguish three states after refresh: **thread-preserving refresh**, **thread-shifting refresh**, and **off-thread commit**.

A thread-preserving refresh updates timeout, envelope margins, or local geometric details while keeping the next executable clause and anchor semantics aligned with the prior packet thread. A thread-shifting refresh produces a packet that is individually executable but changes the local subgoal interpretation or progress anchor. An off-thread commit occurs when such a refreshed packet is released without explicit acknowledgment that the downstream thread has changed. In aerial manipulation, this failure is especially dangerous because stage transitions are short and tightly coupled: even a small semantic shift during hover-to-approach or approach-to-inspect handoff may look safe in isolation while quietly breaking the intended manipulation sequence.

To capture this phenomenon, we define a refresh classification variable

\[
\omega_t \in \{\text{preserve},\; \text{shift},\; \text{off-thread}\},
\]

where classification depends jointly on packet freshness, remaining-plan compatibility, and consumer-side thread expectation. Operationally, D01 is only allowed to auto-release packets with \(\omega_t = \text{preserve}\). If \(\omega_t = \text{shift}\), the supervisor must either regenerate a packet closer to the current thread or explicitly relabel the downstream handoff as a controlled reroute event. If \(\omega_t = \text{off-thread}\), the packet is treated as a deployment error rather than a successful refresh. This turns refresh from a purely timing-aware update into a **thread-accountable supervisory action**.

The purpose of this guard is to prevent a common evaluation mistake in deployment-oriented world models: counting a packet as successfully repaired or refreshed just because it remains executable. For D01, a refreshed packet only counts as useful when it preserves both safety validity and local progress semantics. This keeps the paper's main claim anchored to a stronger supervisory contract—**freshness plus thread consistency**—instead of a weaker notion of packet validity that ignores silent local-plan abandonment.

### 3.17 Route-Window Decomposition for Delayed Consumption

To make delayed-consumption effects measurable, we decompose every packet event into three mutually exclusive **route windows**. **W0 pre-release reroute** captures cases where the supervisor blocks or reroutes a packet before any downstream consumer sees it. **W1 hover-window bounded recovery** captures cases where a packet becomes invalid or questionable, but can still be repaired inside a low-speed hover or re-anchor shell without changing the intended local execution thread. **W2 post-refresh downstream consumption** captures the hardest regime: the packet has been refreshed or regenerated and is then actually consumed by the downstream controller under a potentially shifted local state.

This decomposition matters because prior recovery-oriented narratives can easily overclaim. A method may appear strong simply because it succeeds often in W1, where the platform is stationary and the controller is tolerant to small refresh delays, while offering little real benefit in W2 where the corrected packet must survive actual downstream use. We therefore require all deployment-facing gains to be attributed to one of these windows rather than being reported as a single undifferentiated supervision improvement.

Formally, for every packet event we assign a route-window label

\[
\zeta_t \in \{W0, W1, W2\},
\]

and report packet outcomes separately by window. In particular, the key packet metrics—Safety Release Yield (SRY), Refresh-to-Post-Plan Retention (RPPR), Packet Handoff Continuity (PHC), and thread-preserving Effective Aerial Handoff Rate (EAHR)—must be stratified by \(\zeta_t\). This makes it impossible to hide a weak W2 handoff story behind a strong W1 recovery story.

### 3.18 Latency-Exposed Semantic Staleness Tokens

Recent latency-aware VLA evidence suggests that delayed control failure is not only a world-model freshness problem but also an interface problem between slow semantic reasoning and fast execution. TIC-VLA [REF: 2602.02459] explicitly models the delayed semantic-control interface and shows that high-level semantic outputs should expose their latency to downstream control rather than pretending to be instantaneous. We adopt this lesson in D01 by attaching a compact **semantic staleness token** to every safety packet.

Concretely, besides rank, feasibility, and expiry fields, the packet carries

\[
\sigma_t = (\delta_t^{\text{sem}},\; \delta_t^{\text{bind}},\; \delta_t^{\text{consume}},\; \phi_t^{\text{stage}}),
\]

where \(\delta_t^{\text{sem}}\) is the elapsed semantic age since the packet's clause-level reasoning was produced, \(\delta_t^{\text{bind}}\) and \(\delta_t^{\text{consume}}\) are expected lag budgets up to downstream bind and final local consume, and \(\phi_t^{\text{stage}}\) encodes whether the current stage tolerates stale semantics or requires forced refresh. The purpose is not to turn D01 into a semantic planner, but to make semantic staleness visible to the same deployment-time contract that already tracks expiry and thread preservation.

This extension gives D01 a cleaner bridge to future D02 and D06 handoff experiments. A packet may remain dynamically feasible while its clause interpretation has become stale because the downstream controller will only consume it after an additional delay. In that case, the correct explanation is neither pure anomaly nor pure route failure: it is **latency-exposed semantic staleness**. We therefore treat positive gains from stale-semantic exposure as support for **freshness-accountable invalidation** or **latency-aware reroute discipline** unless they also survive \(W2\) post-refresh consume. In other words, exposing semantic age can justify earlier invalidation or safer reroute, but by itself it is still not evidence of full delayed-consumption handoff preservation.

### 3.30 Interface-Staleness-Corrected Semantic Promotion Rule

The previous sections separate semantic screening gain, identity preservation, and delayed-consumption honesty, but one more reviewer-facing rule is needed: **how should D01 decide whether a semantic-latent improvement is a world-model gain or merely a delayed-interface gain in disguise?** The local retrieval pattern is informative here. When our D01-targeted query repeatedly recalls TIC-VLA-style delayed semantic-control interface material before new D01 world-model evidence, the burden of proof should shift: any semantic gain must first defeat the weaker explanation that the system simply exposed stale semantic routing information more gracefully.

We therefore define an interface-staleness-corrected promotion tuple

\[
\kappa_t = (q_t^{\text{sem-rank}},\; q_t^{\text{route-stale}},\; q_t^{\text{bind-honest}},\; q_t^{\text{consume-honest}},\; q_t^{\text{promotion-gap}}),
\]

where `promotion-gap` measures how much semantic-latent improvement remains after subtracting the best delayed-interface explanation. Concretely, D01 may only upgrade a semantic-latent result above **planner-side semantic routing support** if two conditions hold simultaneously: (i) `route-stale` decreases relative to an interface-only control, and (ii) the remaining gain still survives at both bind and consume time. If either condition fails, the result must be frozen below full packet-contract credit even when planner-side routing, ranking, or early-stage feasibility improves.

This rule gives D01 a more honest promotion ladder. A semantic latent that helps the system pick cleaner packets but still depends on stale delayed-interface exposure is reported as **semantic-routing support**. A semantic latent that survives delayed bind but not consume is reported as **bind-honest semantic support**. Only a latent that reduces interface staleness dependence *and* improves consume-honest packet survival is allowed to support a stronger **deployment-time packet-contract** claim. In short, D01 should not claim that semantic latents solved delayed-consumption supervision until they outperform the best stale-interface explanation under the same downstream consume boundary.

### 3.19 Route-Freezing Rule for Deployment Claims

We finally impose a **route-freezing rule** on the paper's top-level claim. D01 is only allowed to claim a **progress-preserving supervisory contract** if gains remain positive under delayed consumption specifically in the **W2 post-refresh downstream consumption** window and those gains are attributable to **thread-preserving** commits rather than merely executable refreshes.

If improvements concentrate in W0, the correct interpretation is that D01 behaves primarily as a **freshness-accountable invalidation and rerouting layer**. If improvements concentrate in W1, the correct interpretation is that D01 provides a **phase-bounded recovery interface** that is useful during hover or re-anchor shells but does not yet solve general downstream handoff. Only if W2 also improves with positive thread-preserving commit statistics may the paper escalate its claim to full deployment-time progress preservation.

This rule is intentionally conservative. Its purpose is to force the narrative to freeze at the strongest level truly supported by evidence, preventing local repair success from being overstated as a generic world-model supervision win.

### 3.19 Consumption-Time Thread Preservation Readout

We further add an explicit controller-side uptake readout, because delayed-consumption failure often emerges *after* refresh has already passed freshness and feasibility checks. For every packet that reaches a downstream consumer, we annotate whether the packet is executed under the same local progress thread, under an explicitly acknowledged controlled reroute, under a silent semantic thread shift, or rejected after refresh. Formally, we define

\[
\upsilon_t \in \{\text{same-thread consume},\; \text{controlled reroute consume},\; \text{silent thread-shift consume},\; \text{reject after refresh}\}.
\]

This variable complements route-window labels by answering a stricter question: even if a packet survives refresh and is actually consumed, does the downstream controller still interpret it as the same executable clause? A system can look strong on freshness and feasibility alone while still failing on true deployment continuity if many refreshed packets are consumed under **silent thread shift**, because those events preserve local motion continuity but discard the intended remaining-plan semantics.

### 3.36 Temporal-Context and Contact-Semantics Preservation

Recent local additions from MemoryVLA++ [REF: 2606.09827] and iMaC [REF: 2606.09813] suggest that D01 should make one more accountability split explicit. MemoryVLA++ shows that long-horizon embodied execution benefits from preserving retrieved episodic context and imagined future state inside the control pipeline, rather than repeatedly acting from a shallow current-frame summary. iMaC shows that action representation itself can be lifted into motion/contact image tokens, preserving contact-rich actuation semantics that are often lost in low-dimensional action vectors. For D01, these two signals point to a deployment-time question that current packet-contract language has only implicitly covered: even if object identity, clause identity, and thread identity survive refresh, can the packet still preserve the **same temporal episode context** and **same contact-intent semantics** when the downstream stack finally consumes it?

We therefore introduce a temporal-contact preservation tuple

\[
\tau_t = (c_t^{\text{episode}},\; c_t^{\text{imagined-future}},\; a_t^{\text{contact-sem}},\; h_t^{\text{bind}},\; h_t^{\text{consume}}),
\]

where `episode` measures whether the packet still points to the same retrieved execution context, `imagined-future` measures whether the near-future latent state remains aligned with the intended remaining plan, `contact-sem` measures whether the packet preserves the same contact/motion semantics expected by the downstream controller, and the last two terms keep the usual downstream honesty split. A packet that preserves only thread identity but not `episode` or `contact-sem` is frozen below full handoff credit as **context-thin bind support** or **contact-fragile consume support**. Only when temporal context and contact semantics both survive delayed consume do we allow these newer world-model gains to count as true packet-contract progress.

This addition gives D01 a cleaner way to absorb recent long-horizon world-model evidence without overclaiming. MemoryVLA++ should currently be treated as strong support for **temporal-context preservation**, not automatic proof of deployment-time supervisory honesty. iMaC should currently be treated as strong support for **contact-semantic packetization**, not automatic proof of consume-honest handoff. The paper's main claim therefore remains conservative: memory-rich and contact-aware world models are valuable precisely because they may make delayed-consumption packets more auditable, but they still need explicit packet-level accounting before being credited as deployment-time supervision gains.

### 3.25 Identity-Preserving Packet Addressing

Beyond freshness and thread continuity, deployment-time supervision must preserve **what the packet is about**. We therefore augment the packet with an explicit identity-preserving address tuple

\[
\alpha_t = (a_t^{\text{obj}},\; a_t^{\text{anchor}},\; a_t^{\text{clause}},\; a_t^{\text{thread}}),
\]

where \(a_t^{\text{obj}}\) denotes the primary object slot, \(a_t^{\text{anchor}}\) the local spatial or relational anchor, \(a_t^{\text{clause}}\) the executable clause identity, and \(a_t^{\text{thread}}\) the expected progress thread. The key motivation comes from object-addressable world-action modeling such as OA-WAM [REF: 2605.06481], which shows that persistent address vectors can decouple *which entity is being acted on* from *what its current appearance or mutable content is*. We borrow this principle at the supervisory layer rather than the generative layer.

Concretely, D01 does not require a refreshed packet to preserve pixel-level scene reconstruction or a globally identical latent state. It requires the packet to preserve the same **addressable execution referent** across rerank, refresh, bind, and local interaction consume. A packet therefore fails identity preservation if, after refresh, it attaches to a nearby but different object, swaps a local clause from “inspect valve A” to “inspect adjacent handle,” or reuses the correct stage tag with a shifted anchor relation that no longer matches the remaining-plan field.

We operationalize this through an identity-preservation predicate

\[
\iota_t = \mathbb{I}[d(\alpha_t, \alpha_t^{\downarrow}) \leq \epsilon_{\alpha}],
\]

where \(\alpha_t^{\downarrow}\) is the controller-side expected address state at bind or consume time, and \(d\) compares object identity, anchor relation, clause continuity, and thread continuity. A refreshed packet may only count as **consume-honest** if both thread consistency and identity preservation remain above threshold. If identity fails but feasibility remains positive, the event must be frozen as **address-drifted bind gain** rather than full handoff gain. This prevents a common failure mode in aerial manipulation handoff: a packet appears feasible, fresh, and locally smooth, yet its executable meaning has drifted because the target referent silently changed under viewpoint shift, contact evolution, or hover-window replanning.

We further add an explicit **slot-to-consume audit** for object-slot style world models. For each packet we log whether the emitted slot identity, refreshed slot identity, and consumed slot identity remain aligned under the same clause and anchor relation. This matters because recent object-slot world-action modeling suggests that identity disentanglement can stay stable in representation space while still drifting at the packet-consumption interface. We therefore treat slot alignment as a first-class packet audit signal rather than assuming representational disentanglement automatically implies downstream consume honesty.

We therefore derive a **Consumption-Time Thread Preservation Rate (CTTPR)** that fully credits `same-thread consume`, partially credits `controlled reroute consume`, and penalizes silent shifts or post-refresh rejects. CTTPR is reported jointly with RPPR and PHC so that D01 distinguishes a packet that merely survives until consumption from a packet that preserves the intended executable thread *and referent* through consumption.

### 3.26 Refresh-Budget Attribution: Proposal Gain versus Handoff Gain

Fast latent predictors are attractive for D01 because they can increase how often the supervisor refreshes packet validity before downstream execution. However, a higher refresh rate is not automatically equivalent to stronger deployment-time supervision. We therefore introduce an attribution rule that separates **proposal-side refresh gain** from **true downstream handoff gain**. Let a refresh sequence produce packets \(\mathcal{P}_{t}^{(0)}, \mathcal{P}_{t}^{(1)}, \dots, \mathcal{P}_{t}^{(K)}\) before final controller use. For each refresh index \(k\), we separately record whether the update improved (i) planner-side ranking and feasibility discrimination, (ii) controller-side bind honesty, and (iii) local consume-time honesty:

\[
\Delta^{(k)} = (\Delta r^{\text{rank}}_k,\; \Delta h^{\text{bind}}_k,\; \Delta h^{\text{consume}}_k).
\]

This decomposition matters because lightweight JEPA-style predictors such as LeWorldModel [REF: 2603.19312] mainly promise **faster latent refresh and cheaper planning throughput**, whereas latent-action mixture interfaces such as MoLA [REF: 2605.12167] mainly promise **more executable decoding of imagined futures**. In D01, neither improvement is allowed to directly upgrade the paper's main claim unless it survives delayed downstream use. A refresh loop that repeatedly raises ranking quality but leaves \(\Delta h^{\text{consume}}_k \approx 0\) is credited only as **proposal-side semantic gain**; a loop that improves bind honesty but not consume honesty is frozen as **controller-attachment gain**. Only refresh updates that measurably increase consume-honest packet survival while preserving clause identity, thread continuity, and remaining-plan compatibility may be counted as **refresh-enabled handoff gain**.

Operationally, this lets D01 use fast world-model refresh as a controlled experimental variable rather than a vague systems advantage. We can now ask whether more frequent packet regeneration truly rescues delayed consumption, or merely makes the supervisor look sharper at release time.

### 3.20 Retention-Aware Packet Refresh Scheduling

A second deployment ambiguity is that refresh frequency itself can create misleading gains. If refresh is too sparse, packets expire before downstream use; if refresh is too aggressive, the system may repeatedly improve local freshness while silently rewriting the remaining-plan thread, inflating apparent supervision gains without preserving executable continuity. We therefore model packet refresh as a retention-aware scheduling problem rather than a free timing knob.

For each live packet, the supervisor estimates a refresh utility

\[
U_t^{\text{refresh}} = \gamma_1 \Delta F_t^{\text{fresh}} + \gamma_2 \Delta E_t^{\text{exec}} - \gamma_3 \Delta S_t^{\text{shift}} - \gamma_4 \Delta C_t^{\text{consume}},
\]

where \(\Delta F_t^{\text{fresh}}\) measures expected freshness gain, \(\Delta E_t^{\text{exec}}\) measures executability recovery, \(\Delta S_t^{\text{shift}}\) measures increased risk of thread shift, and \(\Delta C_t^{\text{consume}}\) measures expected disruption to downstream consumption continuity. Refresh is triggered only when the anticipated freshness/executability gain outweighs both semantic thread-shift risk and controller-side uptake disruption.

This scheduling rule is motivated by a simple deployment fact reinforced by WorldArena and Cortex 2.0: candidate quality at proposal time is not enough unless the resulting packet remains useful for commitment under real consumption delay. WorldArena shows that visually or perceptually stronger rollouts need not improve downstream functional utility, while Cortex 2.0 suggests that candidate scoring only matters when it survives commitment in cluttered long-horizon execution. In our setting, that means refresh should be judged by whether it preserves *retained executable value*, not merely by whether it updates packet content.

Operationally, retention-aware refresh scheduling gives D01 a stricter interpretation boundary. If gains come primarily from invalidating stale packets before use, the method is best described as a freshness-aware rerouting layer. If gains remain after accounting for thread-shift risk and consumer disruption, then refresh behaves as a true continuity-preserving supervisory mechanism.

### 3.21 Controller-Bind Versus Local-Consume Separation

We further separate two downstream events that are often collapsed into a single “handoff success” label: **controller bind** and **local interaction consume**. A packet may pass verifier checks and be successfully attached to the downstream controller, yet still fail when the local interaction stack actually consumes it under contact, timing, or stage-specific constraints. This distinction became increasingly important after revisiting LoHo-Manip [REF: 2604.21924], Chain of World [REF: 2603.03195], and the broader delayed-consumption discussion in our local notes: compact progress traces and motion-centric latent structure can help preserve executable intent, but neither by itself guarantees that a packet surviving bind will remain correct at true consume time.

We therefore annotate every post-refresh downstream event with two binary gates,

\[
\beta_t^{\text{bind}} \in \{0,1\}, \qquad \beta_t^{\text{consume}} \in \{0,1\},
\]

where \(\beta_t^{\text{bind}}=1\) means the downstream controller accepts and attaches the packet to its active execution thread, while \(\beta_t^{\text{consume}}=1\) means the local interaction routine actually consumes the packet without breaking stage semantics, remaining-plan intent, or contact-time feasibility. The second gate is strictly stronger than the first.

This lets D01 avoid a common overclaim: a refreshed packet that survives controller bind may still only provide **binding-time continuity**, not true **consumption-time continuity**. Accordingly, we define a **Bind-to-Consume Integrity Rate (BCIR)** that measures the fraction of bound packets which remain valid through local consume, and we require BCIR to be reported jointly with CTTPR and PHC. If gains are positive at bind time but collapse at consume time, the honest interpretation is that D01 improves controller attachment stability but has not yet solved full downstream execution preservation.

### 3.22 Lightweight Latent Packet Scoring with Physics-Probeable Dynamics

The recent LeWorldModel result suggests that deployment-time supervision does not necessarily require a large generative model with many auxiliary stabilizers. A compact JEPA-style latent dynamics model can already preserve physically probeable structure while remaining fast enough for repeated scoring and replanning. Motivated by this observation, we instantiate D01's packet scorer as a lightweight latent predictor whose primary job is **not** to reconstruct visually rich futures, but to preserve the subset of dynamics needed to judge packet freshness, stage compatibility, and downstream executability.

Concretely, the latent packet scorer receives the current observation embedding, action-conditioned packet proposal, remaining-plan summary, and stage tag, then predicts a short-horizon latent continuation together with packet-facing heads for freshness risk, execution feasibility, and thread-preservation compatibility. We intentionally keep this predictor lightweight so that refresh and re-evaluation can occur at deployment cadence without relying on heavyweight video synthesis. This design is also consistent with Chain of World's structure-motion separation lesson: for deployment-time supervision, preserving motion-relevant latent structure is often more valuable than reconstructing static appearance in pixel space.

This module therefore serves two roles. First, it gives D01 a practical path toward low-latency packet scoring and repeated use-time auditing. Second, it sharpens the paper's scientific boundary: we are not claiming that richer visual generation is unnecessary in all embodied settings, but rather that **for packet supervision**, a compact latent dynamics core may be the better abstraction because it exposes physically meaningful variation, refresh-time uncertainty, and thread-sensitive motion evolution at the timescale where downstream release decisions are made.

### 3.23 Promotion Discipline for Deployment Claims

Given the expanded downstream accounting, we impose a final promotion discipline on top-level claims. D01 evidence is only allowed to escalate through four increasingly strong levels: **L0 freshness-accountable invalidation**, **L1 hover-window bounded recovery**, **L2 controller-bind continuity**, and **L3 full consume-time thread preservation**. Promotion to a higher level requires positive gains not only in the matching route window but also in the stronger downstream readout associated with that level.

Concretely, improvements concentrated in W0 only support L0 claims; improvements concentrated in W1 with stable hover-shell repair support at most L1 claims; positive W2 refresh results that survive controller bind but not local consume support L2 claims; and only positive W2 results that also preserve same-thread local consume support L3 claims. This promotion ladder turns our delayed-consumption honesty rule into an explicit paper-writing protocol: the narrative must freeze at the strongest level actually supported by controller-side evidence, rather than being informally promoted from packet freshness or bounded repair alone.

### 3.24 Bind-versus-Consume Honest Escalation Rule

The controller-accountability matrix still admits one final overclaim risk: evidence can look strong up to controller bind while quietly collapsing at the moment of local interaction consume. We therefore add a bind-versus-consume escalation rule on top of the existing `W0/W1/W2` promotion matrix.

For each positive packet outcome, we record two downstream checkpoints: the **last honest bind window** and the **last honest consume window**. A packet that survives to controller bind but loses clause identity, remaining-plan compatibility, or local interaction value at actual consume time is not allowed to inherit a full deployment-time handoff interpretation. Instead, it must be frozen at the weaker controller-bind level.

Operationally, the final escalation rule is:
- if evidence is only honest through verifier acceptance, the gain is frozen as **planner-side semantic or runtime continuity gain**;
- if evidence is honest through controller bind but not local consume, the gain is frozen as **controller-bind gain**;
- only if evidence remains honest through local-interaction consume, while preserving `SOR`, `CCH`, `MRP`, `T12`, `B2`, and positive `CTTPR`, may the result be escalated to **full deployment-time handoff-value gain**.

This rule matters because many deployment-time world-model systems are naturally strongest at early screening and provisional binding, while the hardest failure often appears later when the packet is finally consumed under contact-rich or stage-shifted execution. By separating bind-time honesty from consume-time honesty, D01 keeps its top-level claim aligned with the latest checkpoint at which the packet still preserves the intended executable thread.

### 3.23 Bind-versus-Consume Honest Escalation Rule

We add a final escalation guard that explicitly separates **controller bind** from **local interaction consume** when interpreting positive results. For every packet that reaches the controller side, the system records two final checkpoints: the **last honest bind window** and the **last honest consume window**. The bind window answers whether the packet can still be attached to the downstream controller while preserving stage tag, clause identity, and remaining-plan compatibility. The consume window asks the harder question: when the local interaction stack actually consumes the packet under contact, timing, and execution-stage constraints, does the same executable clause still survive?

Formally, we log

\[
\beta_t^{\text{bind}} \in \{W0, W1, W2, \varnothing\}, \qquad
\beta_t^{\text{consume}} \in \{W0, W1, W2, \varnothing\},
\]

where \(\varnothing\) means the packet fails before that checkpoint is reached. A result is only allowed to inherit the strongest claim supported by the **later** of these two honest checkpoints. If evidence remains honest only through bind, the gain must be frozen as a **controller-bind gain** even if planner release, verifier acceptance, and bind-time continuity all improve. Only when the packet remains honest through consume—while also preserving `SOR`, `CCH`, `MRP`, `T12`, `B2`, and `CTTPR`—may the result be escalated to a **full deployment-time handoff-value gain**.

This rule prevents a subtle but important overclaiming pattern: a method may make the packet easier to rank, validate, refresh, and even attach to the controller, yet still lose the same clause identity when the local interaction stack executes under real contact and timing stress. D01 therefore treats **bind-honest** and **consume-honest** as different evidence levels rather than as interchangeable late-stage success.

### 3.25 Clause-Identity and Remaining-Plan Preservation at Use Time

A remaining ambiguity is that late-stage packet success is often reported at the level of controller attachment or local completion, without checking whether the **same executable clause** survives all the way to use time. In aerial manipulation this is dangerous because a packet may keep looking locally executable while silently drifting away from the intended clause, anchor relation, or remaining-plan semantics during refresh, bind, or contact-time consume.

We therefore explicitly track a use-time preservation tuple

\[
\psi_t = (\iota_t^{\text{clause}},\; \rho_t^{\text{remain}},\; \sigma_t^{\text{stage}},\; \kappa_t^{\text{contact}}),
\]

where \(\iota_t^{\text{clause}}\) measures clause-identity preservation, \(\rho_t^{\text{remain}}\) measures remaining-plan compatibility, \(\sigma_t^{\text{stage}}\) measures stage-tag consistency, and \(\kappa_t^{\text{contact}}\) measures whether the packet remains valid under local interaction/contact-time constraints. A packet is considered **use-time honest** only when all four components remain positive at the actual consume timestamp.

This tuple gives D01 a sharper deployment boundary. A packet can be release-honest, verifier-honest, and even bind-honest while no longer being use-time honest if the local interaction stack consumes a semantically shifted clause or a packet whose remaining-plan meaning has drifted. By elevating clause identity and remaining-plan compatibility to first-class use-time variables, we ensure that late-stage gains are credited only when the same intended executable meaning survives to actual local consume.

## 3.23 Bind-versus-Consume Honest Escalation Rule

Controller-side accountability still leaves one final ambiguity: a packet may survive verifier acceptance and even controller bind, yet fail when the local interaction stack actually consumes it under contact, timing, or stage constraints. To prevent this last ambiguity from leaking into inflated deployment claims, we explicitly distinguish the **last honest bind window** from the **last honest consume window** for every positive result. Intuitively, bind asks whether the downstream controller can attach the packet without immediately rejecting it, while consume asks whether the same packet still preserves clause identity, remaining-plan compatibility, and local interaction value when it is actually used.

For each packet event, we therefore log a pair

\[
\xi_t = (w_t^{\text{bind}},\; w_t^{\text{consume}}),
\]

where each element takes values in \(\{W0, W1, W2, \varnothing\}\). Here \(w_t^{\text{bind}}\) is the latest window in which controller bind remains honest, and \(w_t^{\text{consume}}\) is the latest window in which local interaction consume remains honest. A result is only allowed to inherit the stronger of these two interpretations when both windows agree. If evidence only remains honest up to bind but not consume, the result must freeze at the bind-level interpretation rather than being promoted to full downstream value.

Concretely, we impose the following escalation rule. A packet whose positive evidence stops at \(W0\) can only support **planner-side semantic gain**. If it survives to \(W1\) and preserves verifier acceptance continuity, it may be promoted to **runtime continuity gain**. If it survives controller bind at \(W1\) or \(W2\) but loses honesty at local consume, it can at most be reported as **controller-bind gain**. Only packets that preserve `SOR / CCH / MRP / T12 / B2 / CTTPR` and remain honest through the actual consume window are allowed to be promoted to **full deployment-time handoff-value gain**.

This rule is intentionally stricter than controller-accountability alone. Its purpose is to stop a common overclaim pattern in deployment-oriented world-model systems: treating successful downstream attachment as evidence that the packet's executable meaning was preserved all the way to local interaction. In D01, successful bind is useful but not sufficient. The strongest claim is reserved only for packets whose clause identity and remaining-plan semantics survive until real consume time.

## 4. Experiments

### 3.17 Address-Preserving Consume-Time Handoff Gate

Freshness and thread consistency are still insufficient to certify a packet for downstream use if the packet no longer points to the same executable referent at consume time. In aerial manipulation, the downstream stack may receive a packet that is still geometrically feasible and still locally bindable, yet the object anchor, clause target, or latent action interpretation has already drifted. We therefore extend the deployment-time contract from **freshness + thread consistency** to **freshness + thread consistency + address preservation + decode honesty**.

Let the consume-time handoff tuple be

\[
\zeta_t = (f_t,\; h_t,\; a_t,\; d_t),
\]

where \(f_t\) denotes freshness validity, \(h_t\) denotes thread compatibility, \(a_t\) denotes address preservation, and \(d_t\) denotes decode honesty. Here, **address preservation** asks whether the packet still refers to the same target object / waypoint anchor / instruction clause that justified its release, while **decode honesty** asks whether the packet can still be decoded into a downstream action interface without silently changing its effective operational meaning.

Concretely, we define an address-preservation score

\[
\alpha_t = \mathrm{sim}(\eta_t^{\text{emit}}, \eta_t^{\text{consume}}),
\]

where \(\eta_t\) is an address signature that includes target identity, local anchor relation, clause pointer, and stage-scoped subgoal token. A packet is address-preserving only if \(\alpha_t > \delta_a\). This design is motivated by object-addressable world action modeling: a packet can remain executable after refresh while silently drifting to a nearby but different referent, which should count as a supervisory failure rather than a successful bounded repair.

We also define a decode-honesty score

\[
\beta_t = \mathrm{compat}(u_t^{\text{latent}}, u_t^{\downarrow}),
\]

where \(u_t^{\text{latent}}\) is the latent action or packet content intended by the supervisor and \(u_t^{\downarrow}\) is the control-facing action interpretation induced at consume time. If \(\beta_t \leq \delta_d\), the packet may still be locally executable but no longer honestly supports the original semantic or control claim. This failure mode is especially important when a refreshed packet only preserves low-level continuation while losing clause-level or manipulation-ready meaning.

The final consume-time release gate is therefore

\[
\kappa_t^{+} = \mathbb{I}[f_t = 1] \cdot \mathbb{I}[h_t = 1] \cdot \mathbb{I}[\alpha_t > \delta_a] \cdot \mathbb{I}[\beta_t > \delta_d].
\]

Only packets satisfying \(\kappa_t^{+}=1\) are allowed to support the strongest reviewer-facing claim of **progress-preserving, address-stable, consume-honest handoff**. If freshness and thread consistency hold but address preservation fails, the result must be frozen to a weaker **freshness-accountable reroute** or **bindable-but-drifted packet** interpretation. If address preservation holds but decode honesty fails, the packet can support at most a **decode-fragile bind support** claim. This rule prevents D01 from overstating hover-window recovery or packet refresh gains as full downstream handoff preservation when the packet has already lost referential or interface honesty.

### 3.18 Minimal Logging Contract for Consume-Time Address and Decode Audits

To make the above gate experimentally auditable, we attach two additional log fields to the existing delayed-consumption protocol: `addr_match` and `decode_match`. The first records whether the emitted packet and consumed packet still share the same object / waypoint / clause address signature; the second records whether the latent packet content and downstream interpreted action remain compatible under the same local execution thread. Together with the existing freshness and thread fields, D01 now logs a minimal consume-time contract

\[
\Lambda_{D01}^{+} = (\texttt{fresh},\; \texttt{thread},\; \texttt{consume},\; \texttt{addr\_match},\; \texttt{decode\_match}).
\]

This compact tuple is intentionally reviewer-facing. It forces every late-window gain to declare whether it survives only as freshness recovery, as thread-preserving bounded repair, or as the stronger address-stable and decode-honest downstream handoff. In this way, the method section and the experiment section share the same boundary language, reducing the risk that a packet is counted as successful merely because it remained executable after refresh.

### 4.1 Experimental Setup

**Environments**:
- **S1 Short-range Semantic Navigation**: Language-conditioned local waypoint navigation in AirSim/Unreal Robotics Lab
- **S2 Approach and Alignment**: UAV end-effector approach, stable hover, pre-grasp pose alignment
- **S3 Short-range Contact Manipulation**: Button pressing, light touch, pre-grasp contact in UE5/Isaac Sim
- **S4 Aerial Grasping Closed-Loop**: Navigate → approach → grasp → exit

**Baselines**:
| Baseline Family | Representative Methods | Role |
|---|---|---|
| Planner-first | Hierarchical Planning | World model as high-level planner |
| Trainer-first | World-Gymnast, WoVR, RISE | Imagined rollout for policy training |
| Evaluator-first | WorldEval, Interactive WM, Cortex 2.0 candidate scoring | Ranking correlation and commitment-quality evaluation |
| Verifier-first | WAV, inverse-check | Self-check for under-explored action regions |
| Interface-first | Grounded WM, Policy2Vec | Action interface design for cross-platform generalization |
| Boundary-first | ROBOGATE | Pre-deployment failure boundary discovery and risk-focused screening |

**Metrics**:
- `danger-action release rate`
- `late stop rate`
- `misroute rate`
- `packet repair success rate`
- `anomaly escape rate (AER)`
- `Safe Recovery Yield (SRY)`
- `Recovery Calibration Score (RCS)`
- `Packet Handoff Failure Rate (PHFR)`
- `Boundary Discovery Yield (BDY)`
- `Corrective Branch Reuse Rate (CBR)`
- `Failure-to-Correction Latency (FCL)`
- `Remaining-Plan Preservation Rate (RPPR)`
- `Progress-to-Handoff Consistency (PHC)`
- `Expired-Packet Reuse Rate (EPRR)`
- `Expiry-Aware Handoff Recovery (EAHR)`
- `thread-preserving EAHR`
- `Consumption-Time Thread Preservation Rate (CTTPR)`
- `Bind-to-Consume Integrity Rate (BCIR)`
- `Address Preservation Rate at Consume (APR-C)`
- `Address-Drifted Bind Rate (ADBR)`
- `Remaining-Plan Drift at Use Time (Δplan)`
- `Physical Plausibility Preservation Rate (PPPR)`
- `Executable Packet Validity Rate (EPVR)`
- `Decode-Honest Latent Action Rate (DHLR)`
- `window-conditioned delayed-consumption matrix` over `W0/W1/W2 × B0/B1/B2`

**Physics-accountable interpretation rule**:
- `PPPR` reports whether a released or repaired packet remains free of penetration, unsupported contact, anti-gravity transition, and flight-envelope inconsistency after post-training.
- `EPVR` reports whether a physically plausible packet is still reachable, smooth, and controller-consumable under the current dynamics budget.
- `DHLR` reports whether the packet's imagined future can still be decoded into a control-oriented latent action without silent loss of clause identity, temporal consistency, or downstream inverse-dynamics support; this metric is motivated by MoLA-style multi-expert latent-action decoding.
- A result that improves only `PPPR` should be read as stronger physical sanitization; a result that improves only `EPVR` should be read as stronger controller-facing executability; only joint gains may support stronger deployment-time supervision claims.
- A result that improves `EPVR` but not `DHLR` should be interpreted as controller-bindable yet decode-fragile packet quality, not full consume-honest action-interface improvement.

### 4.2 Main Results

We evaluate the proposed supervisor in a staged aerial-manipulation benchmark that couples language-conditioned navigation with short-horizon manipulation packets. Each trial is decomposed into stage tags \(\{\text{search}, \text{hover}, \text{re-anchor}, \text{approach}, \text{inspect}\}\), and candidate packets are produced by an upstream planner or aerial VLN stack before being screened by D01. The world model is trained on a mixture of action-conditioned rollouts, failure-tagged execution traces, and synthetic counterfactual perturbations for F1 recovery. [TODO: 补充具体数据来源、仿真平台和真实平台配置]

We compare four deployment settings corresponding to the proposed ladder: **Rank-Only**, **Reject-Only**, **Stage-Aware Routing**, and **Bounded Packet Repair**. The baseline set includes (i) direct planner execution without supervision, (ii) a rollout-ranking-only evaluator in the style of WorldEval, (iii) a verifier-style reachability check without stage-aware packet routing, and (iv) an ablated version of our method without F1/F2 triage. We additionally reserve a MoLA-style latent-action decoding ablation that replaces the packet's default action interface with a multi-expert inverse-dynamics latent-action mixture, allowing us to test whether stronger decode-honesty survives delayed consumption better than direct future-to-action decoding. This setup allows us to isolate whether gains come from ranking, feasibility screening, routing, bounded repair, or control-oriented action-interface design.

#### 4.2.1 Primary Readout and Submission-Ready Table Contract

The main result table should be organized around three deployment-facing failure surfaces rather than a single aggregate success number:

1. **Initial screening quality**: `DAR`, `MR`, `AER`
2. **Expiry-sensitive handoff quality**: `PHFR`, `EPRR`, `EAHR`
3. **Progress continuity after reroute/repair**: `RPPR`, `PHC`, `SRY`

In the submission-ready result table, we therefore require every method to report the tuple

\[
(\text{DAR},\; \text{MR},\; \text{AER}) \rightarrow (\text{PHFR},\; \text{EPRR},\; \text{EAHR}) \rightarrow (\text{RPPR},\; \text{PHC},\; \text{SRY}).
\]

#### 4.2.2 Expiry-Aware Interpretation Protocol

We explicitly separate three visually similar but scientifically different handoff failures:
- **Bad initial judgment**
- **Expired-packet reuse**
- **Downstream consumption mismatch**

This separation is directly motivated by the local literature sweep. Cortex 2.0 suggests that imagined futures help only when they remain grounded at commitment time; Hi-WM suggests that failure-local branches are useful only when their anchors remain valid; LoHo-Manip suggests that preserving the remaining local thread matters as much as immediate feasibility. LeWorldModel [REF: 2603.19312] further sharpens the deployment boundary from the systems side: a lightweight latent predictor may make packet rescoring cheaper and more frequent, but higher refresh cadence alone still does not prove that the released packet remains clause-consistent when the downstream controller finally consumes it. OA-WAM [REF: 2605.06481] adds a complementary warning that delayed-consumption failure is often an address drift problem rather than a pure freshness problem; a packet can remain geometrically feasible while silently reattaching to a nearby but different object, anchor, or executable clause. MoLA [REF: 2605.12167] then exposes the last interface gap: even when freshness and identity look preserved, the imagined future may still decode into a control-weak latent action, so bind-time executability can overstate true consume-time honesty.

To make this separation operational rather than rhetorical, every failed handoff is assigned a minimal diagnostic tuple

\[
\upsilon_t = (e_t^{\text{fresh}},\; c_t^{\text{thread}},\; u_t^{\text{consume}},\; a_t^{\text{addr}},\; d_t^{\text{decode}}),
\]

where `fresh` indicates whether the packet remained within its expiry envelope at the instant of downstream use, `thread` measures whether the packet still matches the current remaining-plan thread, `consume` records whether the downstream controller interpreted the packet consistently with its released stage/action semantics, `addr` records whether object-anchor-clause identity still matches the controller-side expected address tuple, and `decode` records whether the refreshed future still maps to a consume-honest latent action interface. In particular, a packet can fail after release in at least five distinct ways: it may be wrong **before** release (`bad initial judgment`), become wrong **between** release and use (`expired-packet reuse`), remain fresh but be consumed against a shifted local thread (`downstream consumption mismatch`), stay executable while drifting to a different addressable referent (`address drift under delayed consumption`), or stay bindable while losing decode-honest action support (`latent-action decode mismatch`). We therefore require all delayed-consumption experiments to log packet age, envelope drift, thread-compatibility, address preservation, and decode-honesty at the actual consumption timestamp rather than only at release.

This extended tuple also determines the strongest honest explanation class. If only `e_t^{\text{fresh}}` improves, the gain is frozen as freshness-accountable invalidation. If freshness and executability improve but `a_t^{\text{addr}}` or `d_t^{\text{decode}}` collapse, the gain is frozen as address-stable reroute support or decode-fragile bind support rather than full delayed-consumption handoff preservation. Only joint gains across freshness, thread, address, and decode-honesty are allowed to support the stronger `progress-preserving supervisory contract` reading.

#### 4.2.3 Refresh-Thread Attribution and Honest Route Freezing

The main-results interpretation must explicitly distinguish **refresh success** from **thread-preserving success**. A packet that remains executable after refresh but no longer preserves the intended local clause should not be counted as a full supervisory win. We therefore require every refresh-mediated handoff event to be assigned to one of three bins: **thread-preserving refresh**, **thread-shifting reroute**, or **off-thread commit failure**. Only the first bin contributes directly to claims about robust packet supervision.

This distinction is motivated by the local evidence chain synthesized in Section 2. Cortex 2.0 suggests that candidate-future scoring matters at commitment time; Hi-WM suggests that branch reuse is only reliable when failure anchors remain semantically reusable; and LoHo-Manip suggests that preserving remaining-plan structure matters as much as immediate feasibility. In other words, the world-model supervisor must not only ask whether a refreshed packet can still be executed, but also whether it still belongs to the same local execution thread.

For route freezing, this means D01 may only claim **cross-stage handoff improvement** when gains appear jointly in `PHFR`, `EPRR`, `PHC`, and the thread-preserving subset of `EAHR`. If improvements are concentrated only in repair success while off-thread commit events remain high, the narrative must be downgraded to **bounded corrective support** rather than promoted to a broader interface or handoff-improvement claim. Likewise, if freshness improves but thread compatibility does not, the correct conclusion is that D01 learned a better expiry-aware invalidation rule, not a stronger progress-preserving supervisory contract.

#### 4.2.4 Window-Stratified Benchmark Protocol and Quantitative Placeholder

Following WorldArena's perception-functionality warning and Interactive World Simulator's correlation-oriented evaluation logic, we define the first-round benchmark around a **window-stratified delayed-consumption matrix** rather than a single aggregate success number. Every packet event is indexed by route window `W0/W1/W2` and lag bin `B0/B1/B2`, where `W0` denotes pre-release reroute, `W1` denotes hover/re-anchor bounded recovery, and `W2` denotes post-refresh downstream consumption; `B0`, `B1`, and `B2` denote immediate use, bounded delay, and stale use respectively. The minimal quantitative report for each cell is `(PHFR, EPRR, PHC, thread-preserving EAHR, Δplan)`, with `SRY` and `RPPR` additionally attached for recovery-dominant windows.

This protocol directly encodes the paper's honesty constraint: gains in `W0` support a **freshness-accountable invalidation layer**, gains in `W1` support a **phase-bounded recovery interface**, and only gains that survive in `W2` under `B1/B2` while keeping `PHC` positive and `Δplan` bounded support the stronger **progress-preserving supervisory contract**. In practice, the expected first submission table should include four method rows—Rank-Only, Reject-Only, Stage-Aware Routing, and Full D01 Supervisor—and reserve dedicated columns for `W2/B1` and `W2/B2` because those are the reviewer-facing stress cells most likely to falsify an over-strong claim.

Before full end-to-end numbers are available, we pre-register the expected qualitative ordering as follows: Rank-Only should help mostly in `W0/B0`; Reject-Only should reduce stale misuse but remain weak on `PHC`; Stage-Aware Routing should improve `W1/B1` by reducing stage-mismatch handoff; and the Full D01 Supervisor should be the only variant that materially preserves thread-preserving `EAHR` in `W2/B1`. If `W2/B2` still collapses while `W1` remains strong, the manuscript must freeze its abstract and title around bounded freshness-aware repair rather than general handoff preservation. This gives Section 4 a clearer quantitative skeleton and aligns the paper with the evidence already accumulated from WorldArena, Interactive World Simulator, Dream2Fix, and the recent D01 local synthesis.

#### 4.2.5 Delayed-Consumption Contract and Freshness Accountability

A deployment-time supervisor should be judged at the **actual packet consumption timestamp**, not only at release. This point is reinforced by both our local D01 evidence chain and a nearby latency-aware control literature signal surfaced by QMD. Recent delayed semantic-control interfaces in VLA systems suggest that the real failure surface is often the mismatch between *when a high-level packet was generated* and *when the low-level controller actually consumes it*. For D01, this means freshness must be evaluated jointly with packet age, envelope drift, and downstream stage timing, rather than treated as a binary release-time flag.

We therefore extend the main-results contract with a delayed-consumption accountability tuple

\[
\zeta_t = (\Delta t_t^{\text{age}},\; d_t^{\text{env}},\; s_t^{\downarrow},\; \upsilon_t),
\]

where \(\Delta t_t^{\text{age}}\) is packet age at actual downstream use, \(d_t^{\text{env}}\) is envelope drift accumulated after release, \(s_t^{\downarrow}\) records consumer-side stage at use time, and \(\upsilon_t\) is the freshness-thread-consumption diagnostic defined above. A packet only counts as a valid handoff if it remains fresh **at use time**, still matches the intended local thread, and is consumed under a stage-consistent downstream context. This makes D01 explicitly robust to delayed packet usage rather than only to delayed packet generation.

Operationally, all delayed-consumption experiments should report age-binned `PHFR`, `EPRR`, and `PHC`, e.g., `0-1 step`, `1-3 steps`, and `>3 steps after release`. If gains vanish once consumption delay exceeds the nominal hover/re-anchor correction window, D01 should be described as a **short-horizon freshness contract** rather than a generic handoff supervisor. If gains persist under moderate delay while thread-preserving EAHR remains positive, we can more credibly claim that packet freshness and progress consistency were jointly learned rather than accidentally aligned at release.

### 4.2.6 Latency-Aware Handoff Binning and Stale-Consumption Stress Test

To make the delayed-consumption claim measurable, we add a stress-test protocol that explicitly varies **planner-to-consumer lag** while holding upstream packet quality fixed. The protocol is inspired by nearby latency-aware semantic-control interfaces such as TIC-VLA, but reinterpreted through the D01 packet contract: the question is not whether semantic reasoning is slow in general, but whether a world-model packet remains valid after the real downstream controller consumes it late.

Concretely, each candidate packet is replayed under three lag bins: **B0 immediate use**, **B1 bounded delay within nominal hover/re-anchor window**, and **B2 stale use beyond the intended correction window**. For each bin, we report `PHFR`, `EPRR`, `PHC`, and thread-preserving `EAHR`, while also tagging whether failure is dominated by **expiry-triggered invalidation**, **stale-but-still-released misuse**, or **fresh-but-off-thread consumption**. This turns delayed packet usage into a first-class experimental axis rather than an implementation caveat.

The expected interpretation is as follows. If D01 only improves B0 while collapsing in B1/B2, then the correct conclusion is that the supervisor learned a **release-time screening heuristic** rather than a deployable handoff contract. If B1 remains strong but B2 degrades sharply, then D01 should be framed as a **bounded-delay freshness-aware interface**. Only if B1 remains stable and B2 still shows materially reduced stale-consumption failures relative to rank-only or verifier-only baselines do we allow stronger claims about delayed-consumption robustness.

### 4.2.7 Hover-Window Recovery Versus General Handoff Gain

Our local paper sweep suggests that bounded recovery, branch reuse, and progress-thread preservation are easy to conflate unless the result table explicitly separates them. Dream2Fix demonstrates that counterfactual recovery can strongly improve recoverable failures, while WorldEval and WorldArena warn that local imagined gains do not automatically transfer to robust downstream deployment. We therefore add a dedicated readout that asks whether improvement comes from **hover-window recoverability** or from a more general **handoff-quality improvement**.

Concretely, all repair-mediated events are partitioned into three route windows: **W0 pre-release rejection/reroute**, **W1 hover/re-anchor bounded recovery**, and **W2 post-refresh downstream consumption**. For each window we report `(SRY, RPPR, PHC, thread-preserving EAHR)` together with the share of failures that were still attributable to bad initial judgment, expiry-triggered invalidation, or off-thread commit. A method is only allowed to claim broad handoff gains if improvements persist beyond W1 and remain visible in W2 under delayed consumption. If gains are concentrated in W1, then the correct scientific reading is not “the supervisor fixed handoff,” but rather “the supervisor learned a **phase-bounded recovery prior** that is useful only inside hover/re-anchor correction shells.”

This additional split is important for D01 because aerial manipulation naturally contains a short safe correction window that can make recovery look stronger than it actually is. By forcing the paper to say **where** the gain appears, we reduce the risk of overstating a Dream2Fix-style bounded recovery benefit as a full packet-handoff contract improvement.

### 4.2.8 Refresh-Thread Attribution and Honest Route Freezing

A refreshed packet should only count as a true supervisory success when it remains both fresh and aligned with the current local execution thread. We therefore require every main-results paragraph to attribute gains using the joint readout set `(PHFR, EPRR, PHC, thread-preserving EAHR)` together with route-window labels `(W0, W1, W2)`. Improvements that mainly arise from blocking stale packets (`PHFR`) or from bounded local repair (`RPPR`) must not be rewritten as generic handoff gains unless `PHC` and thread-preserving `EAHR` also improve in the `W2` regime.

This leads to an explicit **honest route-freezing rule**. If the dominant improvement appears in stale suppression, the result is frozen to **freshness-accountable invalidation layer**. If the dominant improvement appears in hover-shell correction but not downstream use, the result is frozen to **phase-bounded recovery interface**. Only when delayed-consumption bins and `W2` handoff readouts remain jointly positive is the paper allowed to claim a stronger **progress-preserving supervisory contract**. This rule prevents local repair wins from being overstated as general deployment-time supervision gains.

### 4.2.9 Window-Stratified Main-Results Table Template

To prevent local recovery gains from being merged into a single flattering headline, the main table should be **window-stratified**. Each method is reported not only by global averages, but also by route window `W0/W1/W2` and lag bin `B0/B1/B2`. A minimal submission-ready table therefore has the form

| Method | W0: PHFR↓ | W0: EPRR↓ | W1: SRY↑ | W1: RPPR↑ | W2: PHC↑ | W2: thread-preserving EAHR↑ | B0 PHFR↓ | B1 PHC↑ | B2 CTTPR↑ | Weakest Honest Claim |
|--------|-----------|-----------|----------|-----------|----------|------------------------------|----------|----------|------------|----------------------|
| Ours | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| w/o expiry gate | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| w/o thread check | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| recovery-only | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

The last column is deliberately semantic rather than numeric. It records the **strongest claim the evidence is honestly allowed to support** after window and lag stratification. This forces every apparent gain to route to one of three scientifically distinct readings: freshness-accountable invalidation, phase-bounded recovery, or progress-preserving handoff. The table is therefore not merely a presentation convenience; it is the mechanism that keeps D01 from over-claiming bounded-recovery improvements as general deployment-time supervision.

### 4.2.10 JEPA-Style Representation Gain versus Packet-Contract Gain

Recent lightweight world models such as LeWorldModel [REF: 2603.19312] show that stable compact latent prediction can dramatically improve planning throughput and preserve physically meaningful state structure even without complex generative objectives. This is highly relevant to D01 because a lighter latent model can reduce planner-side latency and make packet refresh more frequent. However, faster or cleaner latent prediction should not be confused with better deployment-time supervision. A JEPA-style gain may improve `rank_score`, branch reuse efficiency, or refresh latency while still failing to preserve clause identity, packet freshness, or thread-consistent downstream consumption.

We therefore treat LeWorldModel-style advances as **representation-side throughput gain** unless they survive the same delayed-consumption accounting as our supervisory contract. In practice, a compact end-to-end latent model may help in three places: (i) more frequent re-ranking before release, (ii) lower-latency expiry-aware regeneration, and (iii) more stable branch retrieval for bounded repair. But unless these gains remain visible in `W2` and the long-lag bins while preserving `PHC`, `CTTPR`, and identity-consistent consume honesty, the paper freezes them to **refresh-efficiency gain** rather than promoting them to handoff-value gain. This distinction matters because D01 aims to argue for a deployment-time contract, not merely a faster world model.

TRM [REF: 2605.22164] adds a second interpretation axis that is especially important for D01: some improvements may come from **repairing the planner-facing ranking interface** rather than from improving the latent world model or the packet contract itself. We therefore include a reachability-aware reranking variant that replaces terminal Euclidean latent distance with a horizon-matched trajectory reachability head under the same frozen dynamics model. If this change mainly improves `W0` reroute quality, early danger-action suppression, or terminal-score calibration while leaving `PHC`, `CTTPR`, and delayed `W2/B1-B2` consume honesty largely unchanged, the gain must be reported as **ranking-interface gain** rather than packet-contract gain. Only if reachability-aware reranking also survives downstream bind and consume, while preserving remaining-plan and address consistency, may it support a stronger D01 supervisory interpretation.

### 4.2.11 Identity-Drift Audit under Delayed Consumption

OA-WAM [REF: 2605.06481] suggests that robust action generation benefits from preserving explicit object-address separation. For D01, the analogous deployment-time question is whether a packet still refers to the **same object, anchor, and executable clause** when the downstream stack finally consumes it. We therefore add an identity-drift audit that reports three complementary failure rates: object-slot drift, anchor drift, and clause drift after refresh. These are measured both at controller bind and at true local consume time.

This audit serves two purposes. First, it prevents a packet from being counted as a success merely because it remained geometrically feasible while silently changing referent. Second, it makes delayed-consumption errors scientifically legible: a packet can fail due to expiry, due to off-thread commit, or due to identity drift despite otherwise positive feasibility signals. In the submission-ready narrative, any method whose gains disappear after identity-drift filtering is frozen to **address-preserving bind gain** at best, not full supervisory handoff gain. This gives D01 a stricter and more honest reading rule for late-stage packet success.

### 4.2.12 Window-Conditioned Delayed-Consumption Summary Table

To make the paper easier to read without sacrificing diagnostic sharpness, we summarize the full result contract with a compact **window-conditioned delayed-consumption table** that aggregates the most decision-relevant cells. Instead of showing only one overall average, the summary table reports three route windows (`W0` pre-release reroute, `W1` hover-window bounded recovery, `W2` post-refresh downstream consumption) crossed with three lag bins (`B0` immediate use, `B1` bounded delay, `B2` stale use). The minimal per-cell readout is `PHFR`, `EPRR`, `PHC`, thread-preserving `EAHR`, and `Δplan` at use time. Recovery-focused cells in `W1` additionally report `SRY` and `RPPR`.

| Method | W0: PHFR↓ | W0: EPRR↓ | W1: SRY↑ | W1: RPPR↑ | W2: PHC↑ | W2: thread-preserving EAHR↑ | B0 PHFR↓ | B1 PHC↑ | B2 CTTPR↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rank-Only |  |  |  |  |  |  |  |  |  |
| Reject-Only |  |  |  |  |  |  |  |  |  |
| Stage-Aware Routing |  |  |  |  |  |  |  |  |  |
| Full D01 Supervisor |  |  |  |  |  |  |  |  |  |

The scientific role of this table is not cosmetic. `W0` isolates **freshness-accountable invalidation and rerouting**, `W1` isolates **hover-shell bounded repair**, and `W2` isolates the only regime that truly supports a **progress-preserving supervisory contract**. Likewise, `B0/B1/B2` reveal whether the claimed gain survives planner-to-consumer lag. If a method looks strong in aggregate but collapses once results are stratified by `W2` or `B2`, the paper must freeze the claim at a weaker route label rather than averaging away the failure.

### 4.2.10 Conditional Abstract Claim Template

To keep the eventual abstract honest, we predefine a conditional claim template tied to the result strata above. If gains are concentrated in `W0` and stale suppression metrics, the abstract should say that D01 provides a **freshness-accountable invalidation and rerouting layer** for aerial-manipulation packets. If gains are concentrated in `W1` with weak `W2` continuity, the abstract should instead say that D01 offers a **phase-bounded recovery interface** that is useful inside hover/re-anchor correction shells. Only when `W2` and delayed-consumption bins remain positive in `PHC` and thread-preserving `EAHR` may the abstract escalate to a **progress-preserving deployment-time supervisory contract**.

This conditional template matters because D01 sits at a particularly high risk of overclaiming: bounded hover repair is naturally easier than robust downstream handoff, and stale-packet suppression is naturally easier than preserving the intended remaining-plan thread. By deciding the abstract language *before* seeing numbers, we force the final narrative to follow the strongest route actually supported by evidence instead of retrofitting a generic success story.

### 4.2.11 Window-Conditioned Delayed-Consumption Matrix and Claim Escalation Rule

The current result contract can be made more submission-ready by collapsing route windows and lag bins into a single **window-conditioned delayed-consumption matrix**. Instead of only reporting global averages, each method should be evaluated over the Cartesian split `(W0/W1/W2) × (B0/B1/B2)`, where `W0/W1/W2` denote pre-release reroute, hover-window bounded recovery, and post-refresh downstream consumption, and `B0/B1/B2` denote immediate use, bounded delay, and stale use. This gives a compact but honest way to read whether the supervisor merely blocks stale packets, only helps inside hover shells, or genuinely preserves thread-consistent downstream handoff under delayed use.

For each cell, the minimal report should include `PHFR`, `EPRR`, `PHC`, and thread-preserving `EAHR`; for the recovery-dominant windows, `SRY` and `RPPR` should also be attached. The key interpretation rule is simple: if improvements remain confined to `(W0, B0/B1)` or `(W1, B0/B1)`, then D01 should be described as a **freshness-accountable rerouting layer** or **phase-bounded recovery interface**. Only if the `(W2, B1/B2)` cells also remain positive in `PHC` and thread-preserving `EAHR` may the paper escalate to a **progress-preserving delayed-consumption supervisory contract**. This matrix therefore operationalizes the paper's honesty constraint at the exact point where world-model deployment papers most often overclaim.

### 4.2.12 Remaining-Plan Drift Readout for Downstream Use-Time Validity

A second missing piece in the main-results section is a direct readout of **remaining-plan drift at the downstream use timestamp**. The current tuple `(fresh, thread, consume)` tells us whether a packet stayed valid, but it does not yet quantify *how far* the packet's intended local clause drifted relative to the downstream executor's active thread. We therefore introduce a use-time drift score

\[
\Delta^{\text{plan}}_t = d(\rho_t^{\text{release}},\; \rho_t^{\downarrow@use}),
\]

where `\rho_t^{release}` is the packet's released remaining-plan signature and `\rho_t^{downarrow@use}` is the consumer's actual active local thread at the moment of use. This scalar should be logged together with packet age and envelope drift for every delayed-consumption event.

The reason this matters is that D01's current thesis is no longer just about expiry-aware invalidation; it is about preserving executable progress continuity after reroute and refresh. If `PHFR` drops but `\Delta^{plan}` still grows sharply in `W2/B2`, the scientifically honest conclusion is that D01 learned to suppress stale packets better than the baseline, but has not yet learned a robust progress-preserving handoff contract. Conversely, if `\Delta^{plan}` remains bounded while `PHC` and thread-preserving `EAHR` stay positive under delayed use, that would materially strengthen the paper's central claim. In short, `\Delta^{plan}` turns qualitative discussion about “remaining-plan preservation” into a measurable downstream-use-time quantity.

### 4.2.13 Expected D01 Narrative Freeze for the Current Evidence State

Based on the current local evidence chain—WorldEval for deployment-time ranking, Dream2Fix for bounded corrective recovery, Cortex 2.0 for commitment-time future scoring, and nearby latency-aware control signals surfaced by QMD—the most defensible near-term expectation is that D01 will first succeed in `W0/W1` before it fully succeeds in `W2`, especially under `B2` stale-consumption stress. We therefore pre-register the likely narrative freeze as follows: unless the future results show positive `PHC`, bounded `\Delta^{plan}`, and positive thread-preserving `EAHR` in `W2` under delayed consumption, the default paper framing should remain **freshness-accountable invalidation plus phase-bounded recovery**, not full delayed-consumption progress preservation.

This pre-registration is useful even before experiments exist, because it shapes the writing of the introduction, related-work contrast, and abstract toward a tighter first submission target. Concretely, it suggests that the strongest immediate win condition for D01 is not “the world model solved packet handoff in general,” but “the world model learned when to invalidate, when to locally repair, and when not to over-trust refreshed packets under delayed downstream use.” If later experiments beat this expectation, the paper can escalate its claim. If not, the manuscript is already phrased around the strongest result likely to survive review scrutiny.

### 4.2.14 Window-Conditioned Delayed-Consumption Summary Table

To make the paper easier to read without sacrificing diagnostic sharpness, we summarize the full result contract with a compact **window-conditioned delayed-consumption table** that aggregates the most decision-relevant cells. Instead of showing only one overall average, the summary table reports three route windows (`W0` pre-release reroute, `W1` hover-window bounded recovery, `W2` post-refresh downstream consumption) crossed with three lag bins (`B0` immediate use, `B1` bounded delay, `B2` stale use). The minimal per-cell readout is `PHFR`, `EPRR`, `PHC`, thread-preserving `EAHR`, and `Δplan` at use time. Recovery-focused cells in `W1` additionally report `SRY` and `RPPR`.

This summary table has a very specific scientific role. If the gains mostly live in `W0`, the result should be interpreted as **freshness-accountable invalidation and rerouting**. If the gains mostly live in `W1`, the result should be interpreted as a **phase-bounded recovery interface**. Only if `W2` remains positive under `B1/B2` for `PHC`, thread-preserving `EAHR`, and bounded `Δplan` may the paper escalate to a **progress-preserving delayed-consumption supervisory contract**. By tying claim escalation to a fixed table layout, we reduce the risk of averaging away the exact failure mode that matters most in aerial deployment: a packet that was once valid, later refreshed, and finally consumed off-thread.

### 4.2.15 Bind-Honest versus Consume-Honest Reading Path

The delayed-consumption matrix should also be read with a second late-stage split: **bind-honest** versus **consume-honest** evidence. A method may improve planner release, verifier acceptance, and even controller attachment while still failing when the local interaction stack actually consumes the packet. We therefore require every positive `W2` result to report both the **last honest bind window** and the **last honest consume window**, together with `CTTPR` and `BCIR`.

The reading rule is intentionally strict. If evidence remains honest only through controller bind, then the strongest valid interpretation is **controller-bind continuity gain**. If evidence remains honest through local consume while preserving `SOR`, `CCH`, `MRP`, `T12`, `B2`, and `CTTPR`, then the result may be escalated to **full deployment-time handoff-value gain**. This prevents D01 from overclaiming late-stage success when the packet still loses executable meaning at actual use time.

### 4.2.16 Clause-Identity and Remaining-Plan Audit at Use Time

To make the previous rule actionable, we add a use-time audit over four late-stage preservation variables: clause identity, remaining-plan compatibility, stage consistency, and contact-time validity. For every packet that reaches local consume, we log

\[
\psi_t = (\iota_t^{\text{clause}},\; \rho_t^{\text{remain}},\; \sigma_t^{\text{stage}},\; \kappa_t^{\text{contact}}),
\]

and only count a packet as **consume-honest** when all four remain positive at the actual use timestamp. This audit distinguishes a packet that merely survives long enough to be consumed from a packet that still preserves the same intended executable meaning when consumed.

In practice, this means that a method can no longer claim strong downstream continuity simply because `BCIR` or `CTTPR` improved in aggregate. If clause identity or remaining-plan compatibility collapses at use time, the gain must be downgraded to a weaker bind-time or refresh-time interpretation. The purpose of this audit is to ensure that D01's strongest claims remain tied to the survival of the **same executable clause** rather than to superficial late-stage attachment success.

### 4.2.17 First-Pass Honest Summary Template

Given the expanded late-stage accounting, the first-pass summary paragraph for D01 results should follow a fixed order: **where the gain first appears**, **whether it survives bind**, **whether it survives consume**, and **which honest claim level remains after downgrading**. Concretely, every first-pass paragraph should answer four questions in order: (i) does the gain arise mainly in `W0`, `W1`, or `W2`; (ii) is the gain bind-honest; (iii) is it consume-honest under the `\psi_t` audit; and (iv) after applying the promotion discipline, is the strongest valid label freshness-accountable invalidation, phase-bounded recovery, controller-bind continuity, or full deployment-time handoff-value preservation?

This template matters because D01 is especially prone to flattering late-stage summaries. By freezing the reading path up front, we force the paper to distinguish release-time, bind-time, and consume-time evidence before any broad deployment conclusion is written.

### 4.2.23 Identity-Preservation Gate before Consume-Time Promotion

Bind-honest and consume-honest evidence still leave one final loophole: a packet may survive delayed consume while no longer pointing to the same executable referent. We therefore add an **identity-preservation gate** before any late-stage positive result is promoted to a full deployment-time handoff claim. Concretely, every `W2/B1-B2` positive event must log the address tuple

\[
\alpha_t = (a_t^{\text{obj}},\; a_t^{\text{anchor}},\; a_t^{\text{clause}},\; a_t^{\text{thread}}),
\]

and the use-time audit tuple

\[
\psi_t = (\iota_t^{\text{clause}},\; \rho_t^{\text{remain}},\; \sigma_t^{\text{stage}},\; \kappa_t^{\text{contact}}).
\]

A packet is only allowed to support a **full deployment-time handoff-value gain** if it is simultaneously freshness-positive, bind-honest, consume-honest, and identity-preserving at use time. If freshness and controller attachment remain positive but object/anchor/clause identity drifts, the event must be frozen as **address-drifted bind gain** rather than being promoted to a genuine handoff win. This rule prevents a particularly dangerous overclaim in aerial manipulation supervision: a refreshed packet looks executable, remains locally smooth, and even gets consumed, yet the executable meaning has silently shifted to a nearby referent or a different local clause.

Operationally, the reviewer-facing reading order now becomes: `window/lag cell → bind-honest vs consume-honest → address preservation α → use-time audit ψ → weakest honest claim`. Any result missing `α` or `ψ` logging is not allowed to upgrade beyond **freshness-accountable invalidation**, **phase-bounded recovery**, or **controller-bind continuity**, regardless of aggregate success.

### 4.2.24 Current Evidence-Consistent Freeze after Identity-Aware Delayed-Consumption Audit

Given the current D01 evidence chain, the most defensible near-term expectation is still that the method will first become reliably strong in `W0/W1`, partially stabilize `W2/B1`, and remain fragile in `W2/B2` once identity-preservation and use-time audit constraints are enforced. We therefore explicitly freeze the manuscript's strongest default interpretation as follows.

If gains live mainly in stale suppression or release-time filtering, D01 should be described as a **freshness-accountable invalidation and rerouting layer**. If gains extend into hover/re-anchor repair but weaken once `\alpha` or `\psi` is checked at downstream use time, D01 should be described as a **phase-bounded recovery interface with identity-aware delayed-consumption auditing**. If gains survive controller bind but not identity-preserving consume, the strongest valid interpretation is **address-aware controller-bind continuity**. Only if `W2/B1-B2` remains positive in `PHC`, `CTTPR`, bounded `\Delta^{plan}`, and identity-preserving `\alpha/\psi` audit may the manuscript escalate to a **full progress-preserving deployment-time supervisory contract**.

This freeze matters because the new address layer makes D01 more honest about what late-stage success actually means. A method that improves packet age, suppresses stale reuse, and even raises consume counts can still fail the harder deployment test if those packets no longer preserve the same object/anchor/clause/thread semantics when finally used. D01 should therefore win first by knowing when **not** to over-promote late positive events.

### 4.2.18 Expected Qualitative Trend

**Reject-Only** should already reduce `DAR` and `AER` relative to direct execution. **Stage-Aware Routing** should reduce `MR` and `PHFR`. **Bounded Packet Repair** should improve `SRY`, `RPPR`, and `PHC` specifically inside hover and re-anchor windows, but only if expiry handling suppresses stale-packet reuse and corrective memory remains stage-compatible. Under explicit delayed-consumption bins, we expect naive ranking-only baselines to degrade sharply as packet age increases, while D01 should preserve a larger fraction of its benefit in the `1-3 step` regime by coupling expiry invalidation with thread-consistent handoff guards.

### 4.2.19 Identity-Preserving Address Audit for Delayed-Consumption Packets

Recent local evidence from OA-WAM [REF: 2605.06481] suggests that address-content separation is not only useful for robust manipulation, but also clarifies a hidden D01 failure mode: a packet may remain executable while silently drifting to a nearby but different object, anchor, or clause target. We therefore extend the delayed-consumption evaluation with an identity-preservation audit. For every packet that reaches bind or consume, we log whether the released object slot, anchor relation, clause identity, and progress-thread address remain aligned with the downstream expectation.

Concretely, we report an address audit tuple
\[
\mathcal{A}_t = (A_t^{\text{obj}},\; A_t^{\text{anchor}},\; A_t^{\text{clause}},\; A_t^{\text{thread}}),
\]
where each field measures preservation at the actual downstream checkpoint rather than at planner release time. A packet is only counted as identity-honest if all four remain positive through the claimed window. If a packet survives delayed consume but loses object or clause address, the event is frozen as **address-drifted bind/consume gain** rather than being promoted to a true progress-preserving handoff gain. This prevents D01 from mistaking local executability for preserved executable meaning.

### 4.2.20 Lightweight-Latent Refresh Efficiency versus Contract Preservation

LeWorldModel [REF: 2603.19312] motivates a second ablation axis: some improvements may come from **faster latent refresh and rescoring**, not from a stronger packet contract. To separate these effects, we compare a compact JEPA-style scorer against the full supervisor under matched delayed-consumption bins. The compact scorer is expected to improve refresh cadence and ranking throughput, but unless its gains also survive `W2/B1-B2` with positive `PHC`, `CTTPR`, bounded `Δplan`, and positive address audit tuple `\mathcal{A}_t`, the result should be interpreted only as **refresh-efficiency gain**.

This ablation is important because D01's thesis is about deployment-time supervisory contracts, not merely about making world-model scoring cheaper. If the lightweight latent scorer only improves release-time screening or short-horizon freshness, the paper should explicitly freeze that result to a weaker route label rather than borrowing the full packet-contract narrative.

### 4.2.21 Current Evidence-Consistent Freeze after Address Audit

Given the current local evidence chain, the most defensible near-term expectation remains that D01 will first be strongest in `W0/W1`, partially stabilize `W2/B1`, and still be fragile in `W2/B2` after identity-preserving address audit is enforced. We therefore pre-freeze the strongest default interpretation as follows.

If gains mainly appear in stale suppression or pre-release filtering, D01 should be described as a **freshness-accountable invalidation and rerouting layer**. If gains extend into hover/re-anchor correction but weaken after bind-versus-consume or address audit, D01 should be described as a **phase-bounded recovery interface with delayed-consumption auditing**. If gains survive bind but fail address-preserving consume, the strongest honest interpretation is **address-aware controller-bind continuity**. Only when `W2/B1-B2` remains positive in `PHC`, `CTTPR`, bounded `Δplan`, and full address audit may the paper escalate to a **progress-preserving deployment-time supervisory contract**.

### 4.2.16 Consumer-Side Uptake Table and NtM-Style Boundary Readout

A remaining weakness in the current evaluation story is that most metrics are still packet-centric. To make the D01 claim line up more tightly with downstream navigation-to-manipulation (NtM) handoff, we add a **consumer-side uptake table** that records what the downstream controller actually did after a packet was released. For every consumed packet, the controller-side event is labeled as `same-thread consume`, `controlled reroute consume`, `silent thread-shift consume`, or `reject after refresh`, matching the consumption-time thread variable introduced in Section 3.19. This table should be reported jointly with `CTTPR`, `PHC`, and `Δplan`, because a packet that remains fresh but is repeatedly consumed under silent thread shift is not a successful deployment-time handoff.

This readout matters especially for the D01→D06 boundary. D01 is no longer only trying to predict whether a packet is locally executable; it is trying to preserve a usable packet at the navigation-to-manipulation boundary where hover, re-anchor, approach, and inspect stages become tightly coupled. We therefore require a compact **NtM-style boundary summary** over four event types: `(i)` boundary-correct handoff, `(ii)` freshness-correct but thread-wrong handoff, `(iii)` recovery-correct inside hover shell but not reusable downstream, and `(iv)` stale packet correctly invalidated before downstream use. If the full D01 supervisor mainly improves `(iv)` and partially improves `(iii)` but remains weak on `(i)`, then the honest manuscript framing remains “freshness-accountable invalidation + phase-bounded recovery.” If `(i)` also rises with bounded `Δplan` and positive `CTTPR`, the paper earns a stronger D01→D06 interface claim.

### 4.2.17 Representation-Side Gain versus Packet-Contract Gain

The latest local D01 sweep adds four nearby anchors that sharpen how this paper should interpret its own gains. **LeWorldModel** shows that a compact JEPA-style world model can be trained stably from pixels with only a next-embedding objective plus SIGReg regularization while still exposing latent structure that remains linearly probeable by physical state. **Physically Native World Models** further argues that world models should be judged as control-facing dynamical systems rather than as visually pleasing predictors, reinforcing our decision to keep `PPPR` and `EPVR` separate. **Failure Detection World Model** adds a complementary safety-side lesson: uncertainty-aware future prediction can already detect imminent manipulation failure, so D01's extra value is not merely failure anticipation but converting those predicted failures into a stage-scoped contract that decides whether to invalidate, reroute, repair, or escalate. Finally, **HarmoWAM** [REF: 2605.10942] provides a fresh 2026 anchor from the WAM side: its adaptive coordination between predictive and reactive experts suggests that some world-model gains are fundamentally about *where* predictive control should hand over to reactive control, not about delayed-consumption packet honesty itself.

Together, these anchors tighten the paper's interpretation boundary. LeWorldModel supports the feasibility of lightweight, physically structured latent prediction; Physically Native World Models supports a control- and physics-facing evaluation axis; Failure Detection World Model supports deployment-time uncertainty as a first-class safety signal; and HarmoWAM supports the usefulness of process-adaptive predictive/reactive switching for combining generalizable transit with precise interaction. However, none of them alone justifies a blanket claim that delayed downstream consumption is solved. For D01, these advances must therefore be read as **representation-side gain**, **physics-accountable gain**, **uncertainty-aware gain**, or **process-adaptive control gain** unless they survive the stricter packet-contract readout in `W2/B1-B2` with positive `PHC`, `CTTPR`, bounded `Δplan`, and identity-preserving use-time honesty. What D01 must prove beyond them is narrower and clearer: not merely that a world model can be stable, physically meaningful, failure-aware, or adaptively predictive/reactive, but that these properties can be converted into a **consumption-time-valid packet interface** whose value survives delayed downstream use.

### 4.2.18 Chain-of-World as a Latent-Motion Compression Counterpoint

The newly added **Chain of World** line also gives D01 a useful counterpoint from the VLA side. Its core lesson is that world-model supervision does not have to spend most of its capacity reconstructing static appearance; instead, it can push structure-motion factorization and let the model reason over compact latent motion chains. For D01, this matters less as a direct baseline replacement and more as an interpretation guardrail: if a lighter latent-motion representation already carries enough temporal semantics for downstream action reasoning, then a packet supervisor should avoid claiming that full-frame generative richness is necessary for deployment-time utility.

This counterpoint strengthens the paper's current writing freeze. D01 is not trying to win by generating the most photorealistic future, nor even by carrying the richest latent movie. It is trying to release the *right* packet at the *right* time with the *right* remaining-thread semantics. Chain-of-World therefore functions as supportive contrast: it reinforces the broader trend that compact latent dynamic representations can be enough when the evaluation target is action-facing continuity. In the final manuscript, it should be cited not as proof of our packet contract, but as evidence that the field is already moving away from raw visual reconstruction toward **task-aligned latent dynamics**, which makes D01's contract-centric evaluation philosophy more plausible.

### 4.2.19 Present-Round Writing Freeze

Given the present local evidence state, the most defensible immediate writing freeze is to emphasize **consumer-safe packet invalidation, bounded hover-shell repair, and explicit downstream uptake auditing**, while keeping the strongest cross-stage progress-preservation claim conditional on future `W2/B1-B2` evidence. This keeps the paper aligned with what the local D01 synthesis already supports: world models help most reliably when they know when **not** to release, when they can still perform a bounded correction, and when a refreshed packet should be demoted because the downstream consumer is no longer on the same executable thread.

### 4.2.20 Refresh Is Only Useful When It Preserves Handoff Value

A final ambiguity in deployment-time evaluation is that packet refresh can improve **local freshness** while still degrading **handoff value**. This is especially likely in aerial manipulation because the packet often lives across short but semantically dense transitions such as `hover → re-anchor → approach → inspect`. A refreshed packet may look strictly better under release-time checks—newer timestamp, lower envelope drift, and even improved feasibility margin—yet still become less useful at the downstream boundary if it no longer preserves the target identity, the intended local clause, or the manipulation-ready shell expected by the consumer.

We therefore introduce a **handoff-value-first interpretation rule**. Let the downstream value of a refreshed packet be summarized by three consumer-facing properties: **target identity stability**, **controller-consumability**, and **manipulation-ready shell validity**. A refresh event counts as deployment-positive only if these three properties are preserved jointly with freshness. In practice, this means that refresh-mediated gains must be interpreted through the tuple `(CTTPR, PHC, Δplan, manipulation-ready validity)` rather than through freshness metrics alone. If packet age decreases but `CTTPR` or `PHC` drops, the result must not be described as a stronger handoff mechanism; it should instead be frozen to **refresh-positive but handoff-negative**, indicating that the system learned to update packets without preserving their downstream task value.

This rule strengthens the paper's honesty boundary in a way consistent with both the local D01 evidence chain and the nearby delayed semantic-control literature surfaced by QMD. The deployment question is no longer “did refresh make the packet newer?” but rather “did refresh keep the packet valuable at the exact navigation-to-manipulation takeover point?” If not, D01 should only claim a better **freshness-accountable maintenance rule**. Only when freshness improvement is accompanied by stable target identity, bounded remaining-plan drift, and positive consumer-side thread preservation may the manuscript escalate refresh into evidence for a broader **handoff-value-preserving supervisory contract**.

### 4.2.21 ELVIS-Inspired Uncertainty-Calibrated Packet Release

The latest local D01 note on **ELVIS** adds a missing interpretation axis for this paper: even a packet that is fresh, thread-compatible, and physically plausible can remain dangerous if the imagined futures supporting it collapse into a single overconfident mode. ELVIS shows that long-horizon latent control becomes materially more reliable when planning preserves **multi-hypothesis futures** and calibrates return estimates with ensemble uncertainty rather than trusting a single latent rollout path. For D01, this suggests that packet release should not depend only on feasibility and delayed-consumption validity, but also on whether the supporting imagined branch family remains uncertainty-calibrated at the moment of commitment.

We therefore add an **uncertainty-calibrated packet release** clause to the main-results interpretation. In addition to freshness, thread preservation, and handoff-value retention, every released packet should carry a lightweight uncertainty summary over the supporting latent futures, for example branch disagreement, ensemble return dispersion, or route-level confidence spread. A packet that looks executable but is supported only by a sharply collapsed, disagreement-heavy imagined branch should be interpreted as a **fragile release candidate**, not as a robust supervisory success. This matters especially in aerial manipulation because delayed consumption already amplifies small semantic drift; if the upstream imagination is itself epistemically unstable, the downstream handoff contract becomes easy to overclaim.

Operationally, the first-round D01 story does not need to become a full MPC paper. Instead, ELVIS should be absorbed as a **calibration guardrail**: if refresh or reroute gains are strongest only under low branch disagreement, then D01 should state that its packet contract currently works best under **uncertainty-bounded release regimes**. If future experiments show that `W2/B1-B2` gains remain positive even under moderate ensemble disagreement, that would materially strengthen the claim that D01 is learning a real deployment-time supervisory contract rather than merely exploiting easy low-uncertainty windows. This addition also sharpens the difference between D01 and simpler evaluator-first baselines: D01 is not only deciding *whether* to release a packet, but also *how much imagined-future uncertainty is still acceptable* before release becomes scientifically and operationally dishonest.

### 4.2.22 Current Claim Freeze After the ELVIS Counterpoint

With ELVIS added as a local counterpoint, the current D01 writing freeze becomes slightly sharper. The near-term strongest defensible claim is no longer just “freshness-accountable invalidation plus phase-bounded recovery,” but more precisely: **a delayed-consumption-aware, uncertainty-calibrated supervisory packet contract that knows when to invalidate, when bounded hover-shell repair is still safe, and when imagined-future uncertainty is too high to justify downstream release**. This keeps the paper narrow enough to be honest, but still more substantial than a simple stale-packet filter.


The first ablation block focuses on whether expiry awareness is a true deployment variable or merely an implementation detail. We compare `(a)` no explicit expiry semantics, `(b)` temporal TTL only, `(c)` TTL + envelope-drift expiry, and `(d)` full expiry-aware contract with stage validity. This ablation should be read against `PHFR`, `EPRR`, and `EAHR`, not only overall success rate.

A second ablation isolates how much of D01’s gain comes from preserving progress continuity versus restoring local feasibility. Here we compare packet repair with and without the compressed remaining-plan field \(\rho_t\), and with versus without branch-reuse priors from stage-bounded corrective memory. Inspired by LoHo-Manip [REF: 2604.21924], this block explicitly asks whether compact progress-state serialization is what allows a repaired packet to resume the correct local thread instead of merely producing a safer but task-drifting correction. We therefore require the pair `(RPPR, PHC)` to be reported together with repair success, so that a method cannot claim progress-preserving recovery when it only improves local feasibility while silently dropping the remaining clause sequence.

A third ablation targets the supervisory contract itself: decomposed stage-scoped risk budget versus a single scalar risk score. Here the design is motivated by recent real-world world-model evidence such as Cortex 2.0 [REF: 2604.20246], which suggests that imagined futures are deployment-useful only when commitment remains grounded in the current local envelope rather than in a globally optimistic score. Accordingly, we compare whether decomposed margins over velocity, attitude, pose, and correction window reduce stale but high-score packet release relative to a monolithic confidence value.

We further add two deployment-oriented ablations: **A3 (no explicit packet expiry, route-aware only)** and **A4 (expiry without decomposed stage-scoped risk budget)**.

Finally, we include a packet-structure attribution ablation that decomposes first-round failures into bad initial judgment, expired-packet reuse, downstream consumption mismatch, and **off-thread commit after refresh**. This last attribution is read jointly with `PHC`, making it possible to tell whether a seemingly successful handoff merely stayed executable while drifting away from the intended remaining local plan.

In addition, we introduce two thread-specific contract ablations that are newly motivated by this round’s synthesis. **A5 (no progress-consistent commit)** removes the compatibility check between the packet’s remaining-plan state and the downstream executor’s active local thread, allowing any fresh and feasible packet to be released. **A6 (refresh without off-thread guard)** keeps expiry-aware refresh active but disables explicit detection of thread-shifting refreshes, thereby testing whether apparent handoff gains are actually coming from silent local-plan abandonment.

These two ablations are important because they separate three non-equivalent phenomena: better freshness control, safer local feasibility repair, and true thread-preserving supervisory handoff. If A5 or A6 sharply worsens `PHC`, `RPPR`, or the thread-preserving subset of `EAHR` without dramatically changing raw repair success, then D01 earns the stronger claim that its key contribution is not merely expiry-aware invalidation but **freshness plus progress-thread consistency**. If these ablations do not matter, then thread-accountable commit should be demoted from a main mechanism to an analysis aid.

#### 4.2.9 Controller-Bind versus Controller-Consume Attribution Protocol

The main result table must also prevent a late-stage accounting error: **controller bind success is not yet controller consume success**. A packet can pass ranking, freshness, verifier checks, and even be accepted by the downstream controller, yet still lose clause identity or remaining-plan compatibility when the local interaction stack actually consumes it under contact-time constraints. We therefore require every positive event in `W1/W2` to be decomposed into a downstream pair

\[
lpha_t = (b_t^{	ext{bind}},\; c_t^{	ext{consume}}),
\]

where `bind` records whether the controller successfully attaches the packet to its active execution context, and `consume` records whether the same executable clause survives actual local use. In the submission-ready main table, `EAHR` must be accompanied by both **bind-honest** and **consume-honest** columns, and any gain that remains positive only in the bind-honest column must be interpreted as **controller-bind continuity** rather than full deployment-time handoff preservation.

This protocol matters because D01 currently derives many intermediate gains from better invalidation, better refresh timing, and cleaner controller attachment. Those are useful, but they do not yet prove that the same packet meaning survives to local consume. Accordingly, the recommended table layout is:

\[
(W0/W1/W2) 	imes (	ext{first positive},\; 	ext{last bind-honest},\; 	ext{last consume-honest})
\]

with supporting rows for `PHFR`, `EPRR`, `PHC`, `EAHR_bind`, `EAHR_consume`, and `CTTPR`. If a method improves `EAHR_bind` but not `EAHR_consume`, the honest narrative must freeze at **bind-time continuity gain**. Only joint improvements in `PHC`, `CTTPR`, and `EAHR_consume` under `W2/B1-B2` justify the stronger claim that D01 preserves executable packet value through real downstream consumption.

#### 4.2.10 Window-Indexed Results Paragraph Template

To keep the manuscript honest at write time, every main-results paragraph should follow a fixed window-indexed template instead of jumping directly from aggregate task success to a broad supervisory headline. The default sentence order is:

1. **Earliest gain creation**: state whether the first positive signal appears in `W0`, `W1`, or `W2`.
2. **Latest honest bind horizon**: state the last window in which controller bind remains honest.
3. **Latest honest consume horizon**: state the last window in which local consume remains honest.
4. **Claim freeze**: assign the weakest honest tag among `planner-side semantic gain`, `runtime continuity gain`, `controller-bind gain`, or `full deployment-time handoff-value gain`.

A canonical paragraph template is therefore:

> *The proposed supervisor first becomes positive in `W?`, remains bind-honest through `W?`, and remains consume-honest through `W?`. Consequently, the strongest honest interpretation is `[...]`, because gains in `PHFR/EPRR/PHC` are [or are not] matched by positive `EAHR_consume` and `CTTPR` under delayed downstream use.*

This template prevents two recurring overclaims. First, it stops `W0/W1` improvements from being silently rewritten as general handoff gains. Second, it stops controller attach improvements from being borrowed as evidence for true local interaction preservation. In other words, Section 4 should now read results in the same discipline already imposed by Section 3: **first positive window, last bind-honest window, last consume-honest window, then claim strength**.

#### 4.2.11 Minimal Main-Table Schema for First Submission

For the first submission-ready version, we recommend freezing the core main table to the following minimum schema rather than continuing to expand unrelated metrics:

| Method | First + Window | Last Bind-Honest Window | Last Consume-Honest Window | EAHR_bind ↑ | EAHR_consume ↑ | CTTPR ↑ | PHC ↑ | Claim Tag |
|---|---|---|---|---:|---:|---:|---:|---|
| Direct Execution |  |  |  |  |  |  |  |  |
| WorldEval-style Rank-Only |  |  |  |  |  |  |  |  |
| Verifier-Only |  |  |  |  |  |  |  |  |
| Stage-Aware Routing |  |  |  |  |  |  |  |  |
| Full D01 Supervisor |  |  |  |  |  |  |  |  |

This schema is intentionally narrow. `First + Window` tells the reader where the gain is first created; `Last Bind-Honest Window` and `Last Consume-Honest Window` prevent controller attachment from being conflated with true local-interaction preservation; `EAHR_bind` and `EAHR_consume` quantify that split directly; and `CTTPR` plus `PHC` ensure that downstream uptake and thread preservation remain visible. The final `Claim Tag` must be assigned conservatively from the route-freezing ladder, so that every row is explicitly frozen to one of `planner-side semantic gain`, `runtime continuity gain`, `controller-bind gain`, or `full deployment-time handoff-value gain`.

#### 4.2.12 Family-Matched Reading Order for First-Pass D01 Comparisons

The first-pass reading order should also be **family-matched** rather than headline-first. Direct execution should only establish the raw failure floor. A WorldEval-style rank-only baseline should then be used to test whether D01 is gaining merely from better **policy ranking and dangerous-action suppression** at release time. Verifier-only variants should test whether the observed benefit is only **feasibility/accountability filtering**. Dream2Fix-style bounded-repair variants should then test whether gains are limited to **hover-window recoverability**. Finally, lightweight JEPA/latent-dynamics evidence such as LeWorldModel and real-world commitment-time scoring evidence such as Cortex 2.0 should be used as interpretation anchors: the former supports the plausibility of stable compact deployment latents, while the latter supports commitment-time future scoring, but neither alone licenses delayed-consumption handoff claims.

This family-matched order matters because D01 currently sits at the intersection of evaluator, verifier, recovery, and world-model-planning narratives. If the result is read headline-first, a reviewer can easily misread a rank-only gain as a handoff gain, or a bounded-repair gain as a general delayed-consumption contract. By reading `rank-only → verifier-only → bounded repair → full D01 supervisor`, the manuscript makes the burden of proof explicit: every stronger claim must first defeat the weakest same-family explanation.

#### 4.2.13 Current Evidence-Consistent Freeze After Local L1 Re-Read

After re-reading the local L1 anchors **WorldEval**, **Dream2Fix**, **LeWorldModel**, **Semantic Latent Space World Models**, **Dream-MPC**, **Hi-WM**, and **Cortex 2.0**, the most evidence-consistent freeze for D01 is sharper than a generic “world model as supervisor” claim. WorldEval supports **release-time ranking and danger filtering**; Dream2Fix and Hi-WM support **bounded recoverability and corrective branching for known failures**; LeWorldModel and Semantic Latent Space World Models support the feasibility of **stable, compact, control-relevant latent prediction**; Dream-MPC supports **stronger planner-side candidate refinement inside latent imagination**; and Cortex 2.0 supports **commitment-time future scoring under real deployment pressure**. None of these anchors, by themselves, justify a blanket claim that delayed downstream consumption is solved.

Accordingly, the strongest honest near-term D01 framing is: **a world-model-based deployment-time packet supervisor that combines release-time ranking, verifier-gated invalidation, bounded hover-shell repair, semantic-latent representation choice, planner-side latent refinement, and bind-versus-consume accountability under delayed use**. The paper may only escalate beyond this if future `W2/B1-B2` evidence remains positive in `EAHR_consume`, `CTTPR`, and bounded `Δplan`. Until then, all abstract and results writing should default to this narrower but more defensible contract-centric framing.

This freeze also clarifies how to read future wins from the two newly re-read 2026 anchors. If a semantic latent encoder improves policy screening, robustness to nuisance variation, or candidate calibration without materially moving `w^{consume}` or `CTTPR`, the gain should be interpreted as **representation-side screening gain** rather than packet-contract gain. If Dream-MPC-style gradient refinement improves candidate quality or early ranking but the packet still expires, drifts in clause identity, or loses thread continuity under delayed use, the gain should be interpreted as **planner-side proposal gain** rather than deployment-time supervisory value. In other words, D01 now explicitly separates **better world-model internals** from **better delayed-consumption handoff honesty**.

| Method | First + Window | Last Bind-Honest | Last Consume-Honest | PHFR ↓ | EPRR ↓ | PHC ↑ | EAHR_bind ↑ | EAHR_consume ↑ | CTTPR ↑ | Claim Tag |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Rank-Only | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| Reject-Only | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| Stage-Aware Routing | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| Full D01 Supervisor | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

The point of this schema is not completeness but epistemic discipline. If the full D01 row only improves `Last Bind-Honest` and `EAHR_bind`, then the abstract and title must stop at **controller-bind continuity**. If it also improves `Last Consume-Honest`, `EAHR_consume`, and `CTTPR` in `W2/B1-B2`, then the paper earns the stronger deployment-time handoff claim. This gives D01 a concrete reviewer-facing reporting contract and turns the existing theory of bind-versus-consume honesty into a table that can actually be filled.

### 4.3.1 Minimal Delayed-Consumption Experiment Matrix

To make the above ablations executable rather than rhetorical, we define a smallest useful experiment matrix over **route window**, **consumption lag**, and **thread-preservation supervision**. Concretely, the first-round study should run three route windows `W0/W1/W2`, three lag bins `B0/B1/B2`, and three supervision variants `{Reject-Only, Stage-Aware Routing, Full D01}`; A5 and A6 are then inserted only into the stress cells `W1/B1`, `W2/B1`, and `W2/B2`, where silent thread shift is most likely to be hidden by superficially successful refresh.

The practical reason for this restriction is efficiency. D01 does not need an exhaustive factorial sweep to falsify its central claim; it only needs to show whether the claimed gains survive when delayed use and downstream thread continuity become adversarial. We therefore recommend the following minimal matrix: `(W0,B0)`, `(W1,B1)`, `(W2,B1)`, and `(W2,B2)` as the four primary reporting cells. `W0/B0` tests whether D01 is at least a competent freshness-accountable invalidation layer. `W1/B1` tests whether bounded hover-shell repair adds value beyond rejection. `W2/B1` is the first real handoff cell, and `W2/B2` is the decisive stress cell for whether the paper may escalate beyond bounded-delay supervision.

For each primary cell, the mandatory readout is `(PHFR, EPRR, PHC, thread-preserving EAHR, CTTPR, Δplan)`, with `SRY` and `RPPR` additionally reported in `W1/B1`. The experimental decision rule is intentionally hard-edged: if A5 or A6 causes a large drop in `PHC`, `CTTPR`, or bounded `Δplan` specifically in `W2/B1` or `W2/B2`, then the paper has concrete evidence that thread-accountable commit is a core mechanism rather than a cosmetic logging choice. If not, D01 should stop over-investing in commit semantics and instead freeze the contribution at expiry-aware invalidation plus phase-bounded repair.

### 4.3.2 Submission-Facing Falsification Criteria

We further pre-register a falsification-oriented reading of the experiment matrix. D01 is **not** considered to have established a progress-preserving supervisory contract if any of the following holds: `(i)` `W2/B1` remains below the Stage-Aware Routing baseline on `PHC`, `(ii)` `W2/B2` shows positive freshness but negative `CTTPR`, indicating that refreshed packets are still consumed off-thread, or `(iii)` `Δplan` grows monotonically with lag while thread-preserving `EAHR` remains flat. Any of these outcomes means the supervisor helps locally but does not yet preserve downstream executable intent under delayed use.

By contrast, a stronger claim becomes acceptable only when `W2/B1` and at least one hard stress cell in `W2/B2` remain positive relative to all lighter baselines on `PHC`, `CTTPR`, and bounded `Δplan`, while A5/A6 materially hurt the same cells. This criterion gives the paper a reviewer-resistant promotion rule: the manuscript may only move from **freshness-accountable invalidation** or **phase-bounded recovery** to **progress-preserving delayed-consumption supervision** when the exact cells most likely to reveal semantic thread breakage remain positive under ablation.

A dedicated falsification branch also targets the TRM-style ranking-interface hypothesis [REF: 2605.22164]. If a horizon-matched reachability head substantially improves candidate ordering, terminal-score calibration, or `W0/W1` route choice while leaving `PHC`, `CTTPR`, and use-time clause preservation unchanged in `W2/B1-B2`, then D01 must explicitly report that the improvement is **planner-facing ranking repair** rather than packet-contract progress. This guard is important because it prevents us from confusing better latent future selection with better delayed-consumption supervision.

### 4.4 Cross-Direction Interface Validation

Since D01 is intended to hand off supervisory packets to D06-style aerial VLN and local manipulation stacks, we evaluate not only whether a packet is internally well ranked, but whether it remains consumable across subsystem boundaries. The evaluation therefore treats D01→D06 interaction as a contract test over three layers: `(i)` interface validity at release time, `(ii)` freshness at downstream consumption time, and `(iii)` preservation of local progress anchors after reroute or repair. This protocol is consistent with LoHo-Manip’s progress-conditioned replanning intuition and with Cortex 2.0’s deployment-grounded future scoring, but turns both ideas into a packet-facing handoff benchmark rather than a generic planning comparison.

Concretely, we report `PHFR`, `EPRR`, `EAHR`, `RPPR`, and `PHC` under two execution regimes: **same-cycle consumption** and **delayed downstream consumption**. The delayed regime intentionally inserts realistic latency and envelope drift between D01 release and D06 execution, making it possible to distinguish three cases that would otherwise be conflated: a packet that was wrong from the beginning, a packet that was locally correct but became stale before use, and a packet that remained fresh yet was consumed inconsistently by the downstream stack. We expect the full expiry-aware contract to matter most under this delayed regime.

To avoid over-claiming handoff robustness, the delayed regime also includes an explicit **off-thread commit** audit. After any refresh, reroute, or bounded repair, we compare the packet’s released remaining-plan signature against the downstream executor’s currently active clause/anchor thread. A packet that stays feasible and fresh but silently switches to the wrong local clause is counted as a contract failure rather than a benign execution variant. This audit is directly aligned with WorldArena’s perception-functionality warning: a locally plausible packet should not be credited as a successful handoff if it preserves short-horizon executability while losing the intended task thread.

### 4.5 Deployment-Boundary Discovery and Failure-Focused Screening

Beyond average task success, we evaluate whether the supervisor can expose hazardous pre-execution regions before live deployment. Following ROBOGATE [REF: 2603.22126], we construct a boundary-discovery protocol in which candidate packets are sampled around known weak regions. We report `Boundary Discovery Yield (BDY)`, `danger-action release rate`, and the fraction of surfaced hazards that are correctly routed into `hover_hold`, `fallback`, or `human_review`.

### 4.6 Stage-Aware Triage and Recovery Accounting

We evaluate whether F1/F2 triage and hover-bounded recovery improve safety-accountable execution rather than merely increasing intervention frequency. The ablation compares three routing regimes: `rank_score` gating only, `rank_score + triage`, and the full `rank_score + triage + hover-bounded recovery` system. For each regime, we track `Safe Recovery Yield (SRY)`, `Recovery Calibration Score (RCS)`, `anomaly escape rate (AER)`, and `late stop rate`, with results broken down by stage.

### 4.7 Packet Calibration, Remaining-Plan Preservation, Human-Corrective Branch Reuse, and Progress-Localized Repair Attribution

We evaluate whether F1 failure states can be reused as correction anchors instead of being discarded after one failed rollout, and whether the repaired packet still preserves the **right remaining local intent**. We compare `(i)` no-memory fallback, `(ii)` bounded repair without remaining-plan compression, and `(iii)` corrective memory + remaining-plan compression, and track whether reuse improves `CBR` without collapsing `RPPR` or `PHC`.

We further add a progress-localized attribution analysis: every successful or failed repair is tagged by whether its gain is concentrated in **pre-handoff alignment**, **subgoal-preserving transition**, or **post-repair handoff stabilization**. This yields a localized readout over `(Δfeasibility, Δremaining-plan, Δhandoff)`.

To connect this analysis back to delayed handoff, we introduce a final attribution bucket called **refresh-induced off-thread commit**. This bucket captures cases where refresh or repair restores feasibility and freshness, but the packet is recommitted onto a clause/anchor thread that no longer matches the downstream executor’s active local objective. Reporting this bucket alongside `PHC` prevents bounded repair from being overrated as progress-preserving simply because it kept the platform safe for a few more steps.

### 4.8 Minimal Sanity-Check Ladder

Before any expensive end-to-end campaign, we validate the system through a staged sanity ladder that increases coupling only after the previous rung is stable. **L1** tests packet ranking and feasibility scoring on short-horizon synthetic packet candidates. **L2** adds stage-conditioned routing. **L3** introduces bounded F1 packet repair. **L4** evaluates cross-direction packet handoff to a downstream D06-style executor. **L5** runs a short closed-loop staged task from search to local manipulation under disturbance.

A rung is considered passed only if danger-action release, packet handoff failure, and anomaly escape all remain below stage-specific thresholds.

## 5. Conclusion

This paper presents a world model-based deployment-time supervisor for aerial manipulation that reframes the role of a world model from passive rollout generator to **supervisory packet generator** for coupled flight-manipulation execution. Instead of evaluating success by visual realism alone, our formulation binds rollout ranking, feasibility screening, F1/F2 triage, hover-bounded recovery, and correction-aware branch caching into a stage-aware packet interface that can be handed to downstream aerial navigation and manipulation modules.

The current experimental design is intentionally deployment-facing: it asks whether the world model can surface hazardous packets before execution, preserve interpretable stage-consistent handoff, improve safety-accountable correction only inside bounded hover/re-anchor windows, and retain reusable corrective branch states for later post-training. This makes the contribution narrower but more actionable than generic world-model planning claims.

Our current limitations are equally clear. The paper still lacks first-round quantitative results, and the proposed supervisor has only been specified for short-horizon packetized interaction rather than for full long-horizon autonomous mission execution.

Future work will therefore focus on four directions: (1) implementing the minimal sanity ladder and boundary-discovery protocol in simulation, (2) testing D01→D06 packet handoff under nuisance appearance and disturbance shifts, (3) measuring whether branch-level corrective memory reduces repeated F1 failures in bounded hover windows, and (4) extending bounded recovery into a human-in-the-loop corrective branch only for phases whose geometric anchor and risk budget are explicitly verified.

---

## References

[1] WAM: Action-Aware World Model. arXiv:2603.28955, 2026.
[2] RISE: Compositional World Model with Imagination-Based Self-Improvement. arXiv:2602.11075, 2026.
[3] WorldEval: World Model as Policy Evaluator. arXiv:2505.19017, 2025.
[4] ABot-PhysWorld: Physics-Aware World Model Post-Training. arXiv:2603.23376, 2026.
[5] EVA: Executability Alignment via IDM Reward. arXiv:2603.17808, 2026.
[6] WAV: World Action Verifier. arXiv:2604.01985, 2026.
[7] Dream2Fix: Counterfactual Failure Synthesis for Recovery. arXiv:2603.13528, 2026.
[8] World Model Failure Classification. arXiv:2602.16182, 2026.
[9] Interactive World Simulator. arXiv:2603.08546, 2026.
[10] Can Explicit Physical Feasibility Benefit VLA Learning? arXiv:2604.17896, 2026.
[11] Mask World Model: Predicting What Matters for Robust Robot Policy Learning. arXiv:2604.19683, 2026.
[12] ROBOGATE: Risk-Boundary Discovery for Deployment-Time Screening of Manipulation Policies. arXiv:2603.22126, 2026.
[13] Cortex 2.0: Grounding World Models in Real-World Industrial Deployment. arXiv:2604.20246, 2026.
[14] Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training. arXiv:2604.21741, 2026.
[15] LoHo-Manip: Long-Horizon Manipulation via Trace-Conditioned VLA Planning. arXiv:2604.21924, 2026.
[16] Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning. arXiv:2603.25685, 2026.
[TODO: 补充完整引用列表]
