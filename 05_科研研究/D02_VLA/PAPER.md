# Hierarchical Semantic Decoupling for Aerial Vision-Language-Action Control

> 方向：D02 VLA | 目标会议：ICRA 2027 | 状态：🔴 草稿
> 最后更新：2026-04-22

---

## Abstract

[TODO: 150-250词。核心要点：(1) 端到端VLA在空中操作中的延迟和解耦问题，(2) 三层语义解耦架构，(3) 主要实验结果]

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

[TODO: 描述高层VLM的具体设计。输入：视觉观测+语言指令。输出：语义意图token+任务分解。关键：如何压缩语义意图为结构化中间表示，而不是直接输出动作。]

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

---

## 4. Experiments

### 4.1 Experimental Setup

**Environments**: [TODO: 具体仿真环境和真机平台]

**Baselines**:
| Method | Architecture | Latency | Decoupling |
|---|---|---|---|
| OpenVLA | End-to-end | >900ms | ❌ |
| π0 | End-to-end + flow matching | ~200ms | ❌ |
| TIDAL | Dual-frequency | ~50ms | Partial |
| MolmoAct2 | Reasoning + continuous action expert | medium | Partial |
| Ours | Three-layer hierarchical | ~10ms (low-level) | ✅ |

**Metrics**:
- Task success rate (approach / alignment / contact / grasp)
- End-effector trajectory smoothness (velocity/acceleration/jerk)
- Control jitter rate (chunk-transition instability)
- Semantic latency compensation effectiveness
- Aerial stability during manipulation (attitude deviation)
- Packet freshness preservation under delayed execution
- Route-switch stability between diffusion and PID-MPC heads

### 4.2 Main Results

[TODO: 实验结果表格占位符]

### 4.3 Ablation Study

**A1**: Single-layer end-to-end vs. three-layer hierarchical (C1)
**A2**: Without latency compensation vs. with `intent_age`/`latency_offset` (C2)
**A3**: Single-head controller vs. dual-head (C3)
**A4**: Textual CoT vs. latent structured intent representation

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
[TODO: 补充完整引用列表]
