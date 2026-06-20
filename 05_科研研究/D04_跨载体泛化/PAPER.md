# Unified Cross-Embodiment Policy Transfer via Shared Geometry and Latent Action Interfaces

> 方向：D04 跨载体泛化 | 目标会议：CoRL 2027 | 状态：🔴 草稿
> 最后更新：2026-06-17 03:56

---

## Abstract

Cross-embodiment transfer is often reported as a single end-task success number, which obscures whether the real gain comes from shared task geometry, a reusable latent transition interface, or embodiment-specific residual recovery. We study this problem in the setting most relevant to mixed ground–aerial manipulation, where policies may inherit semantic and geometric structure across platforms but still fail under morphology mismatch, viewpoint drift, or aerial dynamics. Our central claim is that cross-embodiment transfer should be evaluated as a staged decision process: shared geometry must be verified before latent transfer can be credited, and shared latent must be exhausted before morphology-aware or dynamics-aware adaptation is promoted to the main explanation.

To this end, we propose a geometry-first transfer protocol built around a shared geometry packet, geometry-conditioned latent action retargeting, optional in-context embodiment residual modeling, and an explicit escalation rule that separates embodiment-conditioned compensation from dynamics-residual recovery. The framework is paired with a pre-registered evaluation tuple `(TR, IGS, LTS, MCG, DRB, VGS-xEmb, CIG, CSC, TSG, TSR, PTL, GRS, OC)` and a weakest-honest reporting discipline for mixed ground–aerial transfer. In particular, we require first-pass gains to be routed through **terrain-state completion**, **contact-interface enrichment**, and **coordination-state completion** before any upgrade to latent/policy-interface transfer or embodiment residual recovery is allowed. This design lets strong heterogeneous-pretraining baselines such as JoyAI-RA, compact geometry-grounded priors such as PokeVLA, and low-data lock-in probes such as Breaking Lock-In function not only as baselines, but as decision tests for whether additional transfer structure is scientifically necessary. We expect this protocol to provide a cleaner account of what truly transfers across embodiments, especially when moving from ground manipulation to aerial manipulation where low-frequency task intent may transfer while high-frequency stabilization remains platform-specific.


---

## 1. Introduction

### 1.1 Problem Statement

Existing robot policies are typically trained for specific hardware, requiring full retraining when the platform changes. For researchers with both UAV and robotic arm platforms, cross-embodiment generalization is essential. Current approaches span four paradigms: action space unification, functional alignment, world model routes, and data-policy strategies—but no unified framework exists.

The key question is: **given shared geometry representations and latent action interfaces, how much cross-embodiment transfer is possible without embodiment-specific retraining?**

### 1.2 Contributions

This paper makes the following contributions:
1. **C1: Geometry-first cross-embodiment transfer protocol.** We formalize cross-embodiment transfer as a staged decision process in which shared geometry must be verified before latent transfer is credited, and latent transfer must be exhausted before embodiment-specific or dynamics-specific explanations are promoted.
2. **C2: State-completion-aware attribution for mixed ground--aerial transfer.** We introduce a reviewer-facing routing discipline that explicitly separates terrain-state completion, contact-interface enrichment, coordination-state completion, and contact-capable embodiment parameterization from stronger policy-interface or embodiment-residual claims.
3. **C3: Consumption-time claim serialization.** We propose a weakest-honest reporting protocol that ties every gain to its creation stage, first positive window, last honest consumption boundary, and matched-budget explanation tag, preventing early packet improvements from being overclaimed as full cross-embodiment success.
4. **C4: Lock-in- and prior-aware transfer auditing.** We integrate heterogeneous-pretraining saturation tests and low-data post-training lock-in controls, so that foundation-scale priors, compact geometry-grounded priors, and scarce target-side adaptation are treated as scientific decision tests rather than narrative shortcuts.

---

## 2. Related Work

### 2.1 Action Space Unification

CEI achieves 82.4% transfer ratio through unified interface/representation alignment. FAAS, MOTIF, ROI-Driven approaches provide complementary perspectives on action space normalization.

### 2.2 Data Organization and Demonstration Analogies

Data Analogies [REF: 2603.06450] shows that structured paired demonstrations can outperform large unpaired heterogeneous corpora by 22.5% in real cross-embodiment transfer, indicating that embodiment shift is not only a representation problem but also a data alignment problem. This matters for our setting because a shared geometry or latent interface is only useful when demonstrations expose task-consistent correspondences across embodiments. Human-to-robot geometry anchors and simulation-generated paired trajectories should therefore be viewed as structured supervision for interface formation, rather than merely as cheap extra data.

### 2.3 Morphology-Aware Approaches

Embedding Morphology into Transformers [REF: 2603.00182] injects kinematic tokens, topology attention bias, and joint attribute conditioning, showing that explicit morphology structure improves cross-embodiment robustness. UniMorphGrasp [REF: 2602.00915] uses morphology as diffusion generator conditioning for cross-hand-type grasping. DexFormer [REF: 2502.11147] adds a particularly relevant dynamic variant: instead of relying only on static morphology descriptors, it uses history-conditioned transformers to infer embodiment-specific kinematics and dynamics online, suggesting that part of the residual transfer burden may come from time-varying embodiment constraints rather than from morphology labels alone. However, these morphology-aware gains should not be interpreted too early as proof that embodiment-specific structure is the primary transfer bottleneck. Unified Latent Space [REF: 2601.15419] is a useful counterweight here: it shows that adversarial latent projection plus cycle-consistent decoding can already support zero-shot transfer without paired data or target-domain rewards, implying that some apparent morphology gap may instead reflect the absence of a sufficiently shared latent transition space.

A complementary non-arXiv but high-value signal comes from *Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer* (Science Robotics, 2026). Rather than learning embodiment invariance only from data scale or latent compression, it argues that cross-robot transfer can be unlocked by explicitly factorizing manipulator topology and feasible kinematic branches, so that a single demonstrated skill is lifted into a morphology-aware but analytically structured execution rule. For D04, this paper is important because it sharpens a missing boundary in current morphology-aware work: some transfer gains may come from **kinematic feasibility priors** that are neither generic shared latent structure nor online residual adaptation. We therefore treat kinematic-intelligence-style topology priors as a separate explanatory candidate that should be tested before attributing all post-geometry gains either to latent sufficiency or to history-conditioned embodiment residuals.

### 2.4 Latent Action Interfaces

LAD [REF: 2506.14608] uses diffusion models to unify latent action spaces, achieving cross-embodiment manipulation generalization. Unified Latent Space for Humanoid [REF: 2601.15419] validates shared latent representations for multi-DOF complex platforms. LAC-WM [REF: ICLR 2026] demonstrates +46.7% gain from latent action alignment at scale. More recently, UniT [REF: 2604.19734] pushes the latent-interface view one step further by learning a unified physical language across human and humanoid data through visual anchoring and cross-reconstruction, suggesting that embodiment-agnostic intent tokens can simultaneously support policy learning and world modeling. AdaTracker [REF: 2604.20305] provides an important counterexample: if embodiment context inferred from rollout history still contributes large gains after geometry stabilization, then latent interfaces alone are not yet sufficient. PokeVLA [REF: 2604.20834], while not framed as a cross-embodiment paper, strengthens the same interface thesis from the manipulation-foundation-model side: multi-view geometry alignment and action-expert injection imply that compact action learning benefits from spatially grounded intermediate semantics before embodiment-specific execution is resolved. Together, these works suggest a default D04 interpretation rule: once shared geometry is stable, the next hypothesis should be latent-transition sufficiency, but that claim must be stress-tested against online embodiment-context baselines rather than assumed from shared latent structure alone.

### 2.5 Geometry-Centric Shared Interfaces

Point Bridge [REF: 2601.16212] shows that 3D point-based representations can serve as a cross-domain policy bridge by decoupling appearance variation from geometry-sensitive control cues. DeFM [REF: 2601.18923] further argues that depth-centric, noise-invariant representations reduce visual domain gaps and provide a more stable substrate for cross-platform transfer than RGB-only priors. OPFA / One-Policy-Fits-All [REF: 2603.14522] sharpens this line by explicitly coupling geometry-aware action latents with cross-embodiment manipulation, suggesting that shared geometry should not be treated as perception-only preprocessing, but as part of the transferable action abstraction itself. GaussFly [REF: 2604.05062] complements this line from the aerial side: 3D Gaussian field reconstruction plus contrastive visuomotor pretraining suggests that geometry-first representation learning can preserve transferable control structure before embodiment-specific compensation is introduced. XEmbodied [REF: 2604.18484], although not designed specifically for cross-embodiment transfer, reinforces the same thesis from the foundation-model side: injecting 3D geometric and physical cues into the backbone improves spatial reasoning and OOD robustness, implying that geometry-rich intermediate states are a stronger substrate for embodiment-agnostic transfer than pure 2D semantic tokens.

### 2.6 Grounded World Model Interface

Grounded World Model [REF: 2604.11751] uses training-free rendering-based action encoding for embodiment-agnostic tokenization, achieving zero-shot generalization to new platforms (xArm6) without interface retraining.

### 2.7 In-Context Embodiment Adaptation

AdaTracker [REF: 2604.20305] adds a useful variant to the D04 design space: instead of enforcing a single globally shared embodiment-invariant controller, it conditions policy execution on an inferred embodiment context extracted from trajectory history. Its embodiment context encoder and context-aware policy suggest that part of the remaining transfer gap may be recoverable through online inference of embodiment constraints rather than only through static morphology tokens. This matters for our paper because it gives a sharper falsification baseline for the shared-geometry-plus-latent thesis: if an in-context embodiment encoder still provides substantial gains after geometry stabilization and latent retargeting, then residual embodiment information has not yet been fully absorbed by the shared interface; if not, AdaTracker can be reinterpreted as a transient substitute for a more explicit geometry-conditioned latent interface.

### 2.8 Dynamics Residual and Physics Adaptation

RAFL [REF: 2603.22039] provides an important counterpoint to purely representational accounts of transfer. By learning a residual acceleration field that generalizes across soft-robot morphologies, it suggests that some transfer failures should be attributed to shared residual dynamics rather than missing semantic alignment. For D04, this motivates our escalation rule: when geometry and latent interfaces are already stable, persistent residual error should be tested against morphology- or dynamics-conditioned adapters instead of being prematurely interpreted as failure of the shared interface itself.

### 2.9 Real-to-Sim Geometry Anchors from Human Video

X-Sim [REF: 2505.07096] shows that cross-embodiment transfer can be bootstrapped from human videos without action labels by projecting observations into a shared latent space, relabeling actions in simulation, and then distilling robot policies back into real deployment. The important lesson for D04 is not only data efficiency, but also that human demonstrations can contribute transferable supervision at the level of task geometry, subgoal ordering, and contact preparation before embodiment-specific action realization is recovered. This supports our decision to treat human geometry anchors as structured interface-formation data rather than merely as cheap augmentation.

### 2.10 Shared Human-Robot Physical Intent Tokens

UniT [REF: 2604.19734] further suggests that cross-embodiment transfer can be framed as a unified physical-language problem rather than only a robot-to-robot retargeting problem. By aligning human and humanoid behavior through visual anchoring and latent intent reconstruction, it implies that transferable structure may live at the level of physical intent tokens before embodiment-specific actuation is resolved. For D04, this matters because it strengthens the case that shared latent interfaces should absorb human demonstrations as structured supervision, not as loose pretraining noise. It also sharpens the distinction between transferable intent and embodiment-specific recovery: if a token remains predictive across human, ground-robot, and aerial-manipulation settings, then later morphology or dynamics modules should be interpreted as residual execution layers rather than as the primary source of generalization.

### 2.11 Foundation VLA Priors and Negative Controls for Embodiment Bridging

JoyAI-RA 0.1 [REF: 2604.20100] is relevant to D04 not because it fully solves cross-embodiment transfer, but because it bundles explicit action-space unification with heterogeneous human, simulation, and robot data at foundation-model scale. This makes it a strong prior against which our layered interpretation should be tested: if large-scale heterogeneous pretraining plus unified action formatting already explains most transfer, then D04 should emphasize structured interface verification over inventing yet another adapter family. Conversely, if JoyAI-RA still leaves clear morphology- or dynamics-dependent residuals, it supports our decision to separate shared geometry, latent transfer, and residual recovery into distinct explanation layers.

Breaking Lock-In [REF: 2604.23121] adds a complementary but strategically important signal: even when a strong generalist VLA prior exists, low-data post-training can destroy steerability and collapse the policy onto seen objects or spatial targets. Its DeLock recipe—preserving visual grounding during post-training and adding test-time contrastive prompt guidance—suggests that some apparent cross-embodiment failure may actually be **post-training lock-in** rather than missing geometry, latent structure, or embodiment-specific compensation. For D04, this matters because small target-platform adaptation sets are exactly where such failure is most likely. We therefore treat lock-in as a distinct negative control: if transfer degrades mainly after low-data adaptation while geometry stability remains acceptable, the correct interpretation may be *steerability collapse under post-training* rather than *shared interface insufficiency*.

PokeVLA [REF: 2604.20834] strengthens this argument from a compact-manipulation foundation-model angle. Although it is not explicitly formulated as a cross-embodiment paper, its two-stage recipe—multi-view goal-aware semantics learning, geometry alignment, and action-expert injection before downstream manipulation decoding—suggests that spatially grounded intermediate semantics can absorb a large fraction of transferable structure before embodiment-specific execution is resolved. For D04, this makes PokeVLA more than a generic strong baseline: it becomes a probe for whether better geometry-conditioned compact priors can raise latent-transition sufficiency without paying the full cost of morphology-aware or dynamics-aware adaptation.

VistaBot [REF: 2604.21914] adds a fresh but highly relevant adjacent signal from view-robust manipulation. Its combination of 4D geometry estimation, view-synthesis latent extraction, and latent action learning shows that geometry-grounded latent interfaces can remain stable even when viewpoint changes substantially at test time. For D04, the value of VistaBot is not that it directly solves embodiment transfer, but that it sharpens a hidden prerequisite in our argument: if the shared geometry packet is fragile to camera relocation or observation geometry drift, then later latent-transfer gains are hard to interpret as embodiment transfer rather than merely view robustness. VistaBot therefore strengthens the decision to treat `IGS` as a first-class gate and suggests that geometry-conditioned latent interfaces should be stress-tested under viewpoint perturbation before morphology-conditioned recovery is invoked.

Grounding Sim-to-Real VLA [REF: 2603.22876] provides an orthogonal but highly practical caution for D04: once a VLA policy is trained or adapted in simulation, the strength of a claimed cross-embodiment interface still depends on whether the sim-side grounding protocol survives real-world variation. Its evidence that **fine-grained randomization**, **structured rendering realism**, and **post-training RL refinement** materially change zero-shot transfer implies that some gains attributed to embodiment transfer may actually come from better sim-grounding hygiene. For our paper, this means sim-to-real grounding quality should be audited before we conclude that a geometry packet or latent interface is inherently transferable across embodiments.

A newer signal comes from ResVLA [REF: 2604.21391], which reframes generative VLA control as refinement from an intent anchor rather than generation from pure noise. Its low-frequency intent plus high-frequency residual decomposition is not yet a direct cross-embodiment solution, but it sharpens an important D04 hypothesis: transferable structure may first emerge as a geometry- and intent-stabilized coarse transition, while embodiment-specific residuals are deferred to a later refinement stage. This is conceptually aligned with our staged interpretation rule—shared geometry first, latent transition sufficiency second, and only then embodiment- or dynamics-specific residual recovery.

LoHo-Manip [REF: 2604.21924] offers a complementary warning from long-horizon manipulation. By emphasizing trace-conditioned planning and subgoal-consistent execution over many steps, it suggests that strong multi-step rescue can improve end-task success without necessarily improving the underlying cross-embodiment interface. For D04, this matters because progress-trace quality and replanning competence should not be conflated with shared geometry or latent-transfer sufficiency. We therefore treat LoHo-Manip-style long-horizon traces as an orthogonal evaluation guard: if gains appear mainly through better multi-step repair while the embodiment interface remains fragile, the paper must report that improvement as planning rescue rather than cross-embodiment transfer.

### 2.12 Touch-Centric Embodiment Interfaces

FlexiTac [REF: 2604.28156] brings an under-discussed but potentially decisive modality into D04: a reusable tactile interface that can be mounted across different robotic embodiments and tied into both visuo-tactile learning and real-to-sim-to-real fine-tuning. While it is primarily a sensing-system paper rather than a transfer algorithm, its relevance is conceptual and infrastructural. If contact-rich transfer fails only when execution reaches touch-sensitive stages, then a shared visual geometry packet may be necessary but insufficient; a platform-reusable tactile packet may be the missing interface layer that stabilizes contact semantics across embodiments.

This matters especially for the ground-to-aerial manipulation setting, where the policy may inherit coarse intent and geometry from shared latent interfaces but still fail under contact uncertainty, slip, or payload-induced micro-instability. FlexiTac therefore suggests a new D04 reading rule: when gains appear mainly after adding standardized tactile observations, they should not be lumped into generic morphology compensation. Instead, they should be recorded as **contact-interface enrichment**, i.e., the shared interface was incomplete because it lacked a transferable contact state, not because embodiment-specific adaptation was fundamentally unavoidable.

A new local retrieval signal sharpens the same point from the knowledge side. The recent haptics survey *Haptic Sensing for Robot Manipulation: Kinesthetic and Tactile Perception* [REF: 2508.11261] indicates that contact-rich manipulation performance is often bottlenecked by the availability and quality of transferable tactile state variables rather than by arm-specific policy structure alone. For D04, we therefore treat tactile packet design as a first-class interface question: if a cross-embodiment route only improves after touch, slip, force, or kinesthetic traces are exposed, the gain should be frozen at **contact-state completion** before any stronger embodiment-aware story is allowed.

A newer local signal sharpens the same point from the design side. HandCDO [REF: 2604.27557] shows that cross-embodiment performance can also depend on whether the embodiment descriptor itself is parameterized richly enough to expose contact geometry, fingertip shape, and kinematic structure as transferable conditions. In other words, some apparent “morphology-aware gain” may actually come from giving the transfer stack a better **contact-capable embodiment parameterization**, rather than from adding a heavier adaptation module. For D04, this means tactile packetization and embodiment parameterization should be treated as two halves of the same interface question: one specifies transferable contact state at execution time, and the other specifies transferable contact affordance structure before execution begins.

### 2.13 Shared World State as a Cross-Embodiment Coordination Substrate

OmniRobotHome [REF: 2604.28197] is not a direct transfer algorithm, but it provides an important systems-level reminder for D04: some cross-embodiment failures are actually failures of **shared world-state maintenance** rather than failures of action retargeting. Its room-scale multi-camera platform stabilizes human, object, and multi-robot state inside one synchronized coordinate frame, enabling anticipatory assistance and safer shared-space interaction. For our setting, this suggests that when multiple embodiments participate in a task pipeline, a transferable policy may still look weak if the shared state packet drifts under occlusion, camera relocation, or asynchronous observation updates.

This matters because D04 increasingly interacts with multi-robot and mixed ground–aerial deployment scenarios. If transfer gains only emerge once a stable shared world frame is restored, the improvement should not be over-credited to latent action alignment or morphology compensation. Instead, it should be logged as **coordination-state completion**: the transfer stack required a stronger cross-agent state substrate before embodiment-conditioned execution could even be evaluated fairly. This gives D04 another disciplined interpretation guard, adjacent to but distinct from cross-view geometry stability and contact-interface enrichment.

### 2.14 Terrain-State Completion Before Policy-Interface Promotion

GA3T [REF: 2605.06478] sharpens an even more specific confound for mixed ground--aerial transfer: heterogeneous teams may improve not because the policy interface becomes more transferable, but because the aerial platform exposes traversability evidence, obstacle topology, and overhead terrain context that the ground embodiment never observed. In that case, the gain is best interpreted as **terrain-state completion** rather than latent-transfer or embodiment-residual improvement. This distinction is especially important for D04 because our target setting mixes cross-view perception with cross-embodiment execution; without an explicit guard, overhead scene completion can be misreported as stronger transfer.

We therefore treat terrain completion as a first-pass explanation that must be exhausted before any promotion to policy-interface transfer is allowed. Concretely, if the main gain appears after restoring overhead traversability cues, line-of-sight disambiguation, or map-level support-region visibility, the paper must first freeze that gain under **terrain-state completion**. Only after terrain completion, contact-interface enrichment, and coordination-state completion fail to explain the result do we allow upgrades to latent-transition sufficiency, policy-interface transfer, or embodiment residual recovery. This makes D04 more honest in mixed ground--aerial settings where the UAV may contribute scene-state evidence rather than a stronger transferable controller.

### 2.15 Demonstration-Translation Completion as an Upstream Confound

Recent cross-embodiment video-editing work adds an upstream confound that is easy to over-credit as transfer. Bridging the Embodiment Gap [REF: 2605.03637] shows that disentangling task latent from embodiment latent can generate embodiment-matched robot demonstration videos from human demonstrations without requiring paired cross-embodiment data. This is highly relevant to D04 because it means a route may improve not because the downstream geometry packet, latent transition interface, or embodiment-conditioned controller becomes stronger, but because the supervision presented to policy learning has already been cleaned, re-rendered, or embodiment-matched in observation space.

For our paper, this evidence motivates a strict distinction between **demonstration-translation completion** and **policy-interface sufficiency**. If a route only becomes competitive after relabeling, reenactment, simulation replay, or embodiment-specific video translation makes demonstrations more kinematically plausible, temporally coherent, or contact-aligned for the target platform, then the first honest claim is that better supervision has been created. Only after matched toggles show that the same gain survives without cleaner translated demonstrations may the route be promoted to latent-interface transfer, policy-interface transfer, or embodiment residual recovery. In other words, cross-embodiment video generation is an important bridge for D04, but it should initially be treated as an upstream data-completion mechanism rather than automatic evidence that the transfer interface itself has improved.

### 2.16 Unified Embodied Priors as a Saturation Test rather than Direct Transfer Evidence

Pelican-Unified 1.0 [REF: 2605.15153] sharpens a decision boundary that D04 has only recently started to make explicit. A sufficiently strong unified embodied foundation model may already absorb understanding, reasoning, future imagination, and action grounding across heterogeneous embodiments inside one checkpoint. If so, then some gains that appear after adding geometry-first transfer modules, latent retargeting, or specialist residual heads may no longer reflect new transfer structure at all; they may simply reflect that the backbone prior had not yet saturated.

For this reason, we treat unified embodied priors as a **saturation-test family** rather than as direct evidence for cross-embodiment transfer. Their role is to ask a harder reviewer-facing question: after a strong unified prior is installed, does a proposed D04 module still explain residual gain that cannot be routed to generic foundation-scale understanding, geometry-rich representation exposure, or demonstration-side cleanup? If not, the honest interpretation ceiling should remain **prior saturation** instead of being upgraded to shared-interface necessity or embodiment-specific structural evidence.

This distinction is especially important for mixed ground--aerial transfer. A unified prior may already encode broad scene semantics, coarse task decomposition, and long-horizon action regularities that make a weak transfer stack look deceptively capable. In our paper, any D04 module that only helps before this saturation test is passed must be frozen as **pre-saturation support** rather than claimed as core transfer structure.

### 2.17 Shared Interface Necessity after Unified Prior Saturation

The practical implication of Pelican-Unified-style models is that D04 can no longer ask only whether a module improves transfer; it must ask **whether the module is still scientifically necessary once a strong unified prior is present**. We therefore define a stricter route for interpretation: `foundation-scale embodied prior → geometry/interface exposure → latent retargeting sufficiency → residual embodiment structure`. Only gains that survive earlier routes under matched budget, matched context length, and matched observation support are allowed to promote later explanations.

Concretely, if a route improves success mainly by restoring coarse scene semantics or task-level action regularity that a weak backbone was missing, we freeze the gain at **foundation-prior completion**. If stronger geometry packets or latent interfaces only expose a cleaner transfer surface on top of that prior, we freeze the gain at **interface exposure**. Only if substantial residual error remains after both tests do we allow D04 to escalate toward **shared-interface necessity** or **remaining embodiment-structure evidence**. This route-closure rule keeps the paper honest in the face of rapidly strengthening embodied foundation models.

### 2.18 Prior-Preserving Low-Data Adaptation as a Bounded Assistance Route rather than Direct Transfer Evidence

D-CLING [REF: 2605.19690] adds a useful but easy-to-overclaim route for D04. Its depth-conditioned residual branch preserves the action prior of a navigation foundation model while absorbing new-scene geometry through a zero-initialized side adapter. The important lesson is not that low-data target adaptation suddenly proves a stronger cross-embodiment interface; rather, it shows that some gains may come from **prior-preserving bounded adaptation** that keeps a large shared backbone usable under shifted camera geometry or environment statistics.

For our paper, this means low-data adaptation routes should initially be treated as **bounded assistance / prior-preservation support** rather than as direct evidence that the geometry packet or latent transfer interface has become stronger. If a gain appears only after a depth-conditioned side branch, lightweight adapter, or similarly constrained target-side patch is enabled, the first honest explanation is that the transfer stack needed a carefully bounded adaptation route to avoid overwriting shared priors. Only after matched tests show that the same gain survives against weaker explanations such as representation exposure, demonstration-side cleanup, and bounded supervision support do we allow it to promote toward stronger embodiment-structure claims.

### 2.19 Bounded Supervision and Copilot Routes as Residual Support rather than Embodiment Structure

Human-Robot Copilot [REF: 2604.03613] sharpens a second route that D04 must separate from direct transfer evidence. By inserting intermittent human assistance and sparse corrective scaling during execution, it can raise low-data imitation performance across multiple robotic embodiments without necessarily strengthening the shared geometry packet, latent interface, or embodiment-conditioned controller itself. In other words, some apparent transfer gain may simply come from **bounded supervision-side completion**: the system remains fragile, but sparse human correction prevents that fragility from surfacing as hard failure.

We therefore treat copilot-style methods as a family-matched weak explanation that must be defeated before stronger D04 narratives are allowed. If a route only becomes competitive once bounded intervention, sparse correction, or human-in-the-loop patching is available, the honest ceiling is **supervision-side support** or **bounded residual assistance**. Only if gains persist under matched no-copilot controls, and after representation exposure plus prior-preserving adaptation have already been exhausted, may the paper escalate toward latent-interface sufficiency or remaining embodiment-structure evidence.

### 2.20 Specialist Distillation as a Last-Stage Residual Test

Embodiment-Aware Generalist Specialist Distillation [REF: 2602.02960] is important for D04 not because it automatically validates embodiment-aware structure, but because it provides a **last-stage residual test**. If a generalist backbone plus shared geometry and latent retargeting still leaves a stable residual that only specialist heads can absorb, then D04 gains evidence that some embodiment-specific structure remains scientifically necessary. But if specialist branches mainly clean up optimization noise, narrow contact timing, or sparse failure tails already explainable by weaker routes, then their gains should remain frozen as residual support rather than upgraded into a broad transfer headline.

This gives us a stricter interpretation order. Representation exposure, prior-preserving bounded adaptation, copilot-style supervision support, shared latent sufficiency, and terrain/contact/coordination completion must all be exhausted before specialist distillation is credited as remaining embodiment structure. In short, specialist branches should be read as a **promotion blocker test**: they reveal whether a residual still survives after all cheaper and weaker explanations have already been consumed.

### 2.22 Geometry-Predictive Action Models as a Strong Shared-Interface Counterfactual

Geometric Action Model (GAM) [REF: 2606.17046] adds a particularly sharp counterfactual for D04 because it combines a geometric foundation backbone, a causal future predictor, and action decoding inside one geometry-first policy stack. Unlike routes that only standardize robot I/O or add lightweight adaptation after a generalist policy is already formed, GAM suggests that a large portion of cross-platform robustness may come from **future geometry prediction embedded directly in the action model**. If this is true, then some gains that D04 might otherwise attribute to explicit latent retargeting or embodiment-conditioned residual recovery could instead be explained by a stronger geometry-predictive backbone that already stabilizes camera perturbation, contact approach, and pre-contact pose evolution before embodiment-specific execution begins.

For our paper, GAM therefore functions as a **shared-interface counterfactual** rather than as immediate evidence that cross-embodiment transfer is solved. The correct reviewer-facing question is not simply whether a geometry-rich action model performs better, but whether it eliminates the scientific need for D04's staged transfer decomposition. If a geometry-predictive backbone already absorbs most of the transferable structure under matched observation support and matched embodiment budget, then later D04 modules should be frozen as **geometry-predictive support** rather than promoted directly to shared-latent necessity or remaining embodiment structure.

### 2.23 Intervention-Value Recovery as Bounded Supervision Support

ROVE [REF: 2606.17011] highlights a different but equally important confound for D04: a cross-embodiment route may improve not because its shared interface is stronger, but because it gets better at **filtering and reusing imperfect human recovery behaviors** during post-training. Its optimistic value estimation over rollout-intervention tuples shows that low-quality human takeovers do not need to be fully imitated to improve whole-body manipulation; instead, a critic can select the subset of intervention experience that genuinely rescues failure-prone states. For D04, this matters because mixed ground--aerial or humanoid transfer stacks are likely to rely on the same kind of sparse recovery data once zero-shot transfer leaves a long tail of near-failure states.

We therefore treat ROVE-style gains as a **bounded supervision and recovery-selection family** rather than as direct embodiment-structure evidence. If a route becomes competitive mainly after it learns to identify which human interventions are worth absorbing, the first honest explanation ceiling should remain **recovery-value support**: the system is still leaning on filtered supervision-side rescue rather than proving that the shared geometry packet, latent interface, or embodiment-conditioned controller already explains the transfer. Only if the gain survives after subtracting intervention-value selection under matched rollout budgets should D04 promote the result to stronger latent or residual structure claims.

### 2.24 Limitations of Existing Work

(1) No unified framework systematically determines when shared geometry suffices vs. when dynamics adaptation is required.
(2) Geometry-centric representation bridges are often treated as perception-only improvements, rather than as the prerequisite gate for cross-embodiment transfer claims.
(3) Morphology injection and latent alignment are treated as competing approaches rather than complementary layers.
(4) Cross-embodiment transfer for aerial platforms (UAV + arm) remains unvalidated.
(5) Human-to-robot and robot-to-robot transfer are still frequently discussed in separate literatures, leaving open whether a single geometry-and-latent interface can bridge both sources without collapsing task-feasible physical intent.
(6) Recent in-context adaptation and large-scale VLA pretraining results suggest strong embodiment-aware priors, but they still do not tell us when those priors can be replaced by a verified shared geometry-plus-latent interface.
(7) Recent intent-anchored generative control results indicate that stable low-frequency intent and high-frequency embodiment recovery may separate naturally, but existing cross-embodiment work rarely distinguishes latent-transition sufficiency from intent-stable residual refinement.
(8) Existing evaluations usually report final transfer success after scaling data or adaptation modules, but they seldom ask whether heterogeneous-pretraining gains saturate the value of a staged transfer explanation, i.e., whether geometry verification and latent sufficiency still provide explanatory leverage once unified-action foundation models become strong enough.
(9) Current cross-embodiment evaluations still under-specify whether residual gains come from stabilized shared intent or merely from stronger high-frequency repair policies, which makes it easy to overclaim latent sufficiency when the real gain is intent-anchored residual refinement.
(10) Recent cross-view manipulation evidence suggests that geometry packets can look stable under a fixed training camera while remaining brittle under observation relocation; without explicit view-robustness checks, later gains may be misread as embodiment transfer rather than geometry packet repair.
(11) New long-horizon VLA planning results further indicate that progress-aware trace planning can rescue multi-step execution without solving embodiment transfer itself, so current evaluations still conflate long-horizon replanning competence with genuine cross-embodiment interface quality.
(12) Even within morphology-aware methods, most evaluations under-specify whether gains come from static embodiment descriptors or from online history-conditioned inference of morphology and dynamics, leaving the boundary between embodiment labels and temporal residual adaptation insufficiently tested.
(13) Existing morphology-aware comparisons rarely isolate whether the gain comes from embodiment information that is available once per platform or from history-conditioned temporal clues that only emerge online, making it difficult to compare static morphology-token methods against context-adaptive policies under a common attribution rule.
(14) Existing sim-to-real VLA evaluations rarely distinguish failures caused by weak simulation grounding hygiene from failures caused by truly missing cross-embodiment structure, which can inflate transfer claims when randomization and rendering choices are under-controlled.
(15) Contact-rich transfer remains under-instrumented: most current cross-embodiment studies assume vision-dominant interfaces, leaving it unclear when a reusable tactile packet is the missing shared state rather than morphology-aware adaptation itself.
(16) Existing cross-robot transfer studies also under-separate **kinematic feasibility priors** from generic morphology conditioning: when a policy succeeds after swapping embodiments, it is still unclear whether the gain came from a shared latent interface, from topology-aware kinematic branch selection, or from rollout-conditioned residual correction.
(17) Current evaluations also under-specify whether topology-aware gains are confined to **pre-contact feasible-branch selection** or remain beneficial after contact and under view perturbation, which makes it easy to over-promote branch-feasibility priors into broad embodiment-adaptation claims.
(18) Current cross-embodiment evaluations also under-separate failures of action/interface transfer from failures of **shared world-state maintenance** in multi-agent or occlusion-heavy settings, making coordination-state drift an unmeasured confound.
(19) Existing morphology-aware narratives still under-specify when better embodiment descriptors are merely exposing transferable contact affordance structure, rather than proving that heavier embodiment-specific adaptation is fundamentally required.
(20) Existing evaluations also rarely separate **contact-interface enrichment** from **coordination-state completion**: success can improve either because a transferable tactile/contact packet finally makes local interaction observable, or because a synchronized shared world frame prevents cross-agent or cross-view state drift, yet both are often over-credited as generic cross-embodiment adaptation gains.
(21) Existing studies rarely separate **low-data post-training lock-in** from true embodiment gaps: a policy can preserve coarse geometry stability while losing object- and spatial-steerability after tiny target-platform adaptation, so apparent transfer failure may reflect steerability collapse rather than insufficient shared geometry, latent structure, or embodiment priors.
(22) Current evaluations still under-separate **contact-capable embodiment parameterization** from heavier adaptation itself: richer hand or end-effector descriptors may improve transfer simply by exposing transferable contact affordance structure before execution begins, not because the policy has learned a deeper embodiment-specific controller.
(23) A rapidly growing line of cross-embodiment video editing and generation now shows that embodiment shift can sometimes be repaired in observation space before policy learning even begins, yet current transfer evaluations rarely ask whether later policy gains come from a stronger control interface or simply from better **demonstration translation quality**. In particular, disentangling task latent from embodiment latent may create high-quality robot demonstrations from human video without solving low-level transfer at execution time.
(24) Existing benchmarks also under-separate **demonstration-translation completion** from **policy-interface sufficiency**: a route may improve because cross-embodiment video generation supplies cleaner embodiment-matched supervision, while the downstream geometry, latent, contact, and residual stack remains unchanged. Without this distinction, D04 risks over-crediting data-generation bridges as if they were direct evidence that the shared transfer interface itself has become stronger.
(25) Current cross-embodiment evaluations also under-separate **terrain-state completion** from policy transfer itself: in heterogeneous ground–aerial teams, gains may arise because the aerial view fills blind terrain or traversability state that the ground robot never observed, rather than because the action or latent interface became more transferable. Without this distinction, cross-view terrain completion can be over-credited as embodiment adaptation.
(26) Existing multi-robot transfer studies also rarely separate **coordination-state completion** from **terrain-state completion**. A shared world frame may be synchronized, yet the joint team still lacks a task-sufficient traversability map; conversely, better terrain coverage may improve success even when the policy interface is unchanged. This boundary becomes especially important for mixed ground–aerial deployment where the UAV contributes overhead terrain disambiguation rather than direct action retargeting.
(27) Current first-pass result readouts still under-specify the **priority order between terrain-state completion and policy-interface transfer**: a route may improve because the aerial platform exposes missing traversability evidence, while geometry packets, latent interfaces, and embodiment residual modules remain functionally unchanged. Without an explicit priority rule, D04 risks over-promoting scene-state completion into a stronger transfer headline.
(28) Even when an upstream packet or prior creates a measurable gain, current evaluations rarely audit **when that gain is actually consumed** by the target embodiment; without a consumption-time boundary, early packet readiness can be overclaimed as full cross-embodiment success even when decisive uplift arrives only through later contact, coordination, or aerial residual rescue.
(29) Recent unified embodied foundation models such as Pelican-Unified suggest that shared understanding, reasoning, future imagination, and action grounding can already absorb a large portion of cross-platform variance inside one checkpoint. Current D04-style evaluations still rarely test whether a proposed geometry-first or morphology-aware transfer interface remains scientifically necessary once such unified priors are used, making it easy to overclaim new transfer structure when the real effect is prior saturation.
(30) Existing evaluations rarely separate **prior-preserving bounded adaptation** from stronger transfer structure. A lightweight depth-conditioned side branch or constrained adapter may preserve a useful shared prior under new geometry or sensor statistics, but that does not by itself prove that the shared geometry packet or latent interface has become more transferable across embodiments.
(31) Current low-data cross-embodiment studies also under-separate **bounded supervision-side completion** from direct policy-interface gains: intermittent human correction or sparse copilot assistance can rescue execution tails while leaving the underlying transfer interface unchanged.
(32) Even when specialist distillation improves whole-body or cross-platform control, current evaluations rarely test whether specialist gains survive after representation exposure, bounded adaptation, supervision support, and shared latent sufficiency have all been exhausted. Without this ordering, specialist branches can be over-promoted from residual cleanup to broad embodiment-structure evidence.
(33) Recent geometry-predictive action models such as GAM suggest that much of the apparent cross-platform gain may come from a stronger future-geometry backbone rather than from an explicitly auditable staged transfer interface, yet existing evaluations rarely test whether geometry prediction alone already saturates a large fraction of D04's claimed latent or residual structure.
(34) Current cross-embodiment evaluations also under-separate **intervention-value recovery** from direct interface improvement: sparse human rescue can raise deployment success simply because a critic learns which near-failure interventions are worth absorbing, while the shared geometry packet, latent interface, and embodiment-conditioned controller remain unchanged.

---

## 3. Method

### 3.1 Transfer Decision Protocol

We formalize cross-embodiment transfer as a staged verification-and-escalation procedure over a shared geometry packet. For each rollout segment, the interface state is represented as
\[
\mathcal{G}_t = \{P_t^{\text{obj}},\; M_t^{\text{scene}},\; A_t^{\text{contact}},\; \phi_t,\; E,\; T_t,\; C_t,\; W_t\},
\]
where \(P_t^{\text{obj}}\) denotes object-relative pose hypotheses, \(M_t^{\text{scene}}\) the geometry-rich scene substrate (depth / point / Gaussian / occupancy state), \(A_t^{\text{contact}}\) the contact-affordance packet, \(\phi_t\) the task-phase token, \(E\) the embodiment descriptor, \(T_t\) the terrain-state slot, \(C_t\) the coordination-state slot, and \(W_t\) the view/world-frame consistency traces. The packet is considered valid only when it supports stable pre-contact geometry, contact-candidate consistency, and cross-view state persistence under matched perturbations.

We use an explicit geometry-verification score
\[
S_{\text{geo}} = \alpha_1 S_{\text{pose}} + \alpha_2 S_{\text{view}} + \alpha_3 S_{\text{contact}} + \alpha_4 S_{\text{coord}} + \alpha_5 S_{\text{terrain}},
\]
with nonnegative weights \(\alpha_i\) summing to 1. Here \(S_{\text{pose}}\) measures object/goal pose agreement across source-target reconstructions, \(S_{\text{view}}\) measures cross-view latent stability, \(S_{\text{contact}}\) measures consistency of contact-affordance prediction, \(S_{\text{coord}}\) measures synchronized shared-state agreement, and \(S_{\text{terrain}}\) measures whether traversability / support-region evidence is already task-sufficient. A transfer route is allowed to leave the geometry stage only if
\[
S_{\text{geo}} \ge \tau_{\text{geo}} \quad \text{and} \quad \Delta_{\text{view}},\Delta_{\text{coord}},\Delta_{\text{terrain}} \le \varepsilon_{\text{geo}},
\]
meaning that geometry remains stable under matched viewpoint, coordination, and terrain-completion perturbations.

This verification-first formulation prevents D04 from treating cross-embodiment transfer as a monolithic success number. If the score increases mainly because a UAV reveals missing terrain layout, because a synchronized world frame repairs stale shared state, or because a reusable tactile/contact packet finally exposes interaction state, then the first honest explanation remains **terrain-state completion**, **coordination-state completion**, or **contact-interface enrichment** rather than latent transfer. Only after these geometry-side confounds are controlled do we allow the method to escalate toward latent retargeting, embodiment residual inference, or dynamics-aware adaptation.

### 3.2 Shared Geometry Interface (C1)

We instantiate C1 as a geometry-first transfer gate rather than a direct action decoder. Given multi-view RGB-D observations or geometry-recoverable monocular streams, the source platform is mapped into a shared scene-centric representation that preserves target-object geometry, pre-contact pose candidates, and admissible contact regions. Concretely, the interface packet contains a task geometry state, contact affordance tags, a phase token, and embodiment capability bounds, so that downstream transfer decisions are made on a verified geometric substrate instead of raw appearance features.

This design is motivated by three complementary observations in prior work. Point Bridge [REF: 2601.16212] shows that 3D geometric representations can bridge cross-domain policy transfer better than appearance-coupled features. DeFM [REF: 2601.18923] indicates that depth-centric representations reduce spurious visual variation and improve sim-to-real stability. OPFA [REF: 2603.14522] adds a crucial control-facing lesson: geometry-aware latent actions can already absorb a meaningful fraction of embodiment variation before any explicit morphology compensation is enabled, implying that geometry verification should be treated as part of action-interface formation rather than as a perception-only front-end. GaussFly [REF: 2604.05062] further suggests that geometry-preserving scene reconstruction can retain transferable control structure for aerial visuomotor policies. VistaBot [REF: 2604.21914] now makes the gate even more concrete: if 4D geometry estimation and synthesized latent views are required to maintain manipulation robustness under camera displacement, then any D04 claim about embodiment transfer should first verify that its geometry packet survives cross-view perturbation rather than only nominal embodiment swaps. Therefore, our protocol treats shared geometry as a prerequisite gate: if the geometry packet is unstable under viewpoint, morphology, or sensor perturbation, later gains from latent alignment or morphology compensation cannot be credited as true cross-embodiment transfer.

We further refine the packet with a **contact-interface slot**, a paired **coordination-state slot**, an explicit **terrain-state slot**, and an explicit **contact-capable embodiment-parameterization slot**. In addition to pose- and phase-level geometry, the shared state may optionally contain platform-reusable tactile or contact summaries such as pressure onset, slip likelihood, and contact persistence. This extension is motivated by FlexiTac [REF: 2604.28156], which suggests that a low-cost standardized tactile layer can be mounted across embodiments and reused in real-to-sim-to-real learning pipelines. For D04, the implication is sharp: when cross-embodiment transfer fails primarily after contact, the missing ingredient may be an incomplete shared interface rather than insufficient morphology-aware adaptation. We therefore treat tactile/contact packetization as an optional completion of C1, not as a late-stage embodiment-specific patch.

### 3.3 Geometry-Conditioned Latent Action Retargeting (C2)

Once the shared geometry packet is validated, we do not decode actions directly from raw observations. Instead, we factor transfer into a reusable **core transition latent** and an embodiment-facing **formatting layer**. The core latent is supposed to explain task-phase-consistent subgoal motion, contact timing, and intent progression, while the formatting layer only converts that latent into embodiment-feasible actuation. This separation is important for D04: if transfer fails before the formatting layer is stressed, the honest diagnosis is still geometry or latent insufficiency rather than morphology-aware residuals.

Let the verified packet from Section 3.1 be serialized into
\[
x_t = [M_t^{\text{scene}},\; P_t^{\text{obj}},\; A_t^{\text{contact}},\; T_t,\; C_t,\; W_t,\; \phi_t],
\]
and let `E^s`, `E^\tau` denote the source and target embodiment descriptors with capability bounds `B^s`, `B^\tau`. We encode a shared transition latent
\[
z_t^{core} = f_{core}(x_t),
\]
and derive embodiment-facing formatter states
\[
q_t^{s} = g_{fmt}(z_t^{core}, E^s, B^s), \qquad
q_t^{\tau} = g_{fmt}(z_t^{core}, E^\tau, B^\tau).
\]
The retargeted target action is then
\[
\hat a_t^{\tau} = D_{\tau}(z_t^{core}, q_t^{\tau}),
\]
where `D_\tau` is intentionally lightweight: it is allowed to express actuator range, control frequency, and end-effector feasibility, but it is not allowed to invent new task semantics that are absent from `z_t^{core}`.

We train this factorization with a geometry- and phase-aware objective
\[
\mathcal{L}_{lat} =
\lambda_{bc}\mathcal{L}_{bc}
+ \lambda_{align}\mathcal{L}_{align}
+ \lambda_{cycle}\mathcal{L}_{cycle}
+ \lambda_{cap}\mathcal{L}_{cap}
+ \lambda_{contact}\mathcal{L}_{contact},
\]
where `\mathcal{L}_{bc}` matches retargeted actions to target demonstrations, `\mathcal{L}_{align}` contrastively pulls same-phase source-target segments together, `\mathcal{L}_{cycle}` enforces source-target-source consistency, `\mathcal{L}_{cap}` penalizes capability-violating outputs, and `\mathcal{L}_{contact}` preserves contact onset and persistence semantics across embodiments. In practice, the important constraint is that `\mathcal{L}_{align}` operates on subgoal-consistent windows rather than raw joint traces; otherwise the model can appear to align actions while actually memorizing morphology-specific timing.

This section gives D04 a concrete latent-transfer object rather than an abstract “shared action space” claim. The paper can now ask a clean question: after geometry is fixed, does `z_t^{core}` already explain target-side subgoal transitions under matched controls, or does the route still need context inference, bounded adaptation, or later specialist rescue? That distinction is what later promotion blockers will audit.

### 3.4 In-Context Embodiment Residual Modeling

Even when `z_t^{core}` is well formed, some transfer failures only appear after several closed-loop steps because morphology, payload, view drift, or contact timing are only partially observable at a single time step. Following the intuition of AdaTracker [REF: 2604.20305], we therefore model embodiment residuals as a **history-conditioned correction path** rather than as a replacement for the shared latent interface. The critical discipline is that this residual path starts from zero and is promoted only after the base latent route from Section 3.3 has been tested on its own.

Let a rollout window `H_{t-k:t}` contain recent observations, actions, contact outcomes, and state errors. We encode a context state
\[
h_t^{ctx} = f_{ctx}(H_{t-k:t}, E^\tau),
\]
and split the correction into a slow embodiment branch and a fast execution branch
\[
r_t^{slow} = g_{slow}(h_t^{ctx}), \qquad
r_t^{fast} = g_{fast}(h_t^{ctx}, \delta_t^{pose}, \delta_t^{contact}, \delta_t^{stab}),
\]
where `\delta_t^{pose}`, `\delta_t^{contact}`, and `\delta_t^{stab}` summarize pre-contact pose error, contact mismatch, and stabilization error. The final control proposal becomes
\[
u_t = \hat a_t^{\tau} + m_t \odot (r_t^{slow} + r_t^{fast}),
\qquad
m_t = \sigma(W_m[h_t^{ctx}, \phi_t]),
\]
so the gate `m_t` decides whether residual support is actually needed at the current task phase.

We train the residual path with a constrained objective
\[
\mathcal{L}_{ctx} =
\mathcal{L}_{task}
+ \beta_{sp}\|m_t\|_1
+ \beta_{res}\|r_t^{slow} + r_t^{fast}\|_2^2
+ \beta_{sm}\mathcal{L}_{smooth},
\]
where `\mathcal{L}_{task}` is the downstream control loss, the sparsity term keeps residual use minimal, the residual norm discourages the context branch from overwriting the latent route, and `\mathcal{L}_{smooth}` regularizes adjacent-window corrections to avoid oscillatory patching. For mixed ground--aerial transfer, this branch is where payload shift, wind-induced bias, delayed contact realization, or morphology-specific stabilization can be absorbed without pretending that the shared latent itself already solved them.

This makes the embodiment-context story measurable rather than rhetorical. If the route only becomes competitive once `h_t^{ctx}` is enabled, the honest interpretation ceiling is **context-conditioned embodiment support**, not shared latent sufficiency. Only gains that survive after subtracting this residual family are allowed to promote further.

### 3.4 In-Context Embodiment Residual Modeling (C3)

After geometry verification and latent retargeting, we allow a bounded embodiment-conditioned residual path whose role is not to replace the shared interface, but to explain only the error that survives it. Let the verified packet be `\mathcal{G}_t`, the retargeted latent action be `\tilde z_t`, and the target rollout history be `H_t=(o_{t-k:t}, a_{t-k:t-1}, q_{t-k:t}, c_{t-k:t})`, where `q` denotes proprioceptive state and `c` denotes contact/tactile summaries when available. We define a context encoder
\[
\mathbf{h}_t = f_{ctx}(H_t, E, \mathcal{G}_t),
\]
which summarizes embodiment-specific residual cues that are not already consumed by shared geometry or latent-transition structure.

We explicitly split this residual context into three sources:
\[
\mathbf{h}_t = [\mathbf{r}^{dyn}_t,\; \mathbf{r}^{self}_t,\; \mathbf{r}^{steer}_t],
\]
where `\mathbf{r}^{dyn}_t` captures online embodiment/dynamics mismatch, `\mathbf{r}^{self}_t` captures self-other distinction and self-occupancy grounding cues, and `\mathbf{r}^{steer}_t` captures action-entry repair cues introduced by steering modules such as flow-reversal control. The self-grounding term is motivated by proprioceptive-visual correspondence work [REF: 2606.13222]: if a platform first improves because it can tell which body in the scene is itself, or because it can stabilize a predictive self-occupancy model, the honest explanation ceiling is **shared-space grounding support**, not immediate latent-interface superiority. The steering term is motivated by Flow Reversal Steering [REF: 2606.13675]: if a route becomes effective only after coarse candidate actions are reversed into the flow-policy prior and pulled toward executable modes, the first honest explanation is **action-entry steering support**, not stronger embodiment invariance.

The residual branch therefore predicts an additive correction
\[
\Delta z_t = g_{res}(\tilde z_t, \mathbf{h}_t),
\qquad
z_t^{final} = \tilde z_t + \gamma_t^{ctx} \odot \Delta z_t,
\]
where `\gamma_t^{ctx} \in [0,1]^d` is a gated activation that is allowed to turn on only after geometry and latent checks are passed. We further decompose the gate into source-specific scalars
\[
\gamma_t^{ctx} = [\omega_t^{dyn},\; \omega_t^{self},\; \omega_t^{steer}],
\]
with the conservative activation rule
\[
\omega_t^{self} > 0 \Rightarrow S_{geo} \ge \tau_{geo},
\qquad
\omega_t^{steer} > 0 \Rightarrow S_{geo} \ge \tau_{geo} \land LTS_t = 1,
\]
meaning that self-grounding support can only refine an already verified shared space, and action-entry steering can only refine a route that already survives the latent-transition gate.

To prevent this residual path from silently swallowing upstream gains, we report a residual attribution tuple
\[
\mathcal{R}_t^{ctx}=(IEC, SGS^{self}, AES, DRS, CW, PC),
\]
where `IEC` denotes generic in-context embodiment cue usage, `SGS^{self}` denotes self-grounding support, `AES` denotes action-entry steering support, `DRS` denotes remaining dynamics residual support, `CW` is the first positive context window, and `PC` is the last honest consumption boundary. The weakest-honest escalation rule is then:
\[
HRS_t^{ctx} = \Delta_{row} \setminus (IEC \cup SGS^{self} \cup AES).
\]
Only residual gain that remains after context-conditioned embodiment inference, self-grounding support, and action-entry steering support are all consumed may be promoted to **remaining embodiment structure**. In particular, if uplift is concentrated in shared-space disambiguation, collision-aware self-occupancy grounding, or coarse-action repair before executable refinement, then D04 must freeze the explanation at `SGS^{self}` or `AES` rather than upgrading it to shared latent sufficiency or embodiment-conditioned transfer.

### 3.5 Weakest-Honest Escalation Rule

The base D04 protocol must decide whether a gain should stop at geometry completion, context-conditioned support, bounded adaptation, or shared latent sufficiency. We therefore use an explicit ordered claim audit rather than a single best-score selection. The point is simple: the paper should stop at the weakest explanation that still survives matched controls, because stronger narratives are only scientifically justified when weaker families have already failed.

For each evaluated route we maintain
\[
\Pi_t = (IGS,\; IEC,\; BPA,\; BSC,\; LTS,\; SRS,\; CW,\; PC),
\]
where `IGS` is interface-geometry stability, `IEC` is in-context embodiment contribution, `BPA` is bounded prior-preserving adaptation gain, `BSC` is bounded supervision/copilot gain, `LTS` is latent-transition sufficiency under residual-off controls, `SRS` is specialist-residual survival after family subtraction, `CW` is the decisive consumption window, and `PC` is the current promotion ceiling. The ordered base claim set is
\[
\mathcal{C}_{base} =
\{\text{terrain},\text{coordination},\text{contact},\text{IEC},\text{BPA},\text{BSC},\text{LTS},\text{SRS}\}.
\]
A route is assigned the first claim in `\mathcal{C}_{base}` whose residual remains positive under matched context length, adaptation budget, and sensory support.

Operationally, let `\tilde a_t^\tau` denote the action proposal emitted by the geometry-conditioned latent route before any deployment-time steering. We define a target-side executable correction operator
\[
\bar a_t^\tau = \mathcal{E}_{js}(\tilde a_t^\tau, E^\tau, B^\tau, \mathcal{K}^\tau, \mathcal{C}^\tau),
\]
where `E^\tau` is the target embodiment descriptor, `B^\tau` the capability bounds, `\mathcal{K}^\tau` the kinematic/Jacobian structure, and `\mathcal{C}^\tau` the collision-and-limit constraint set. The key reporting rule is that any gain obtained after replacing `\tilde a_t^\tau` with `\bar a_t^\tau` must first be frozen as **post-latent executability support**. In matched-control form,
\[
HRS^{js}=\Delta_{row}\setminus(JGS\cup CAS\cup LLS),
\]
and only when `HRS^{js}>\tau_{js}` under the same decisive window `CW` may the route preserve its stronger `LTS` or `SRS` claim. If the uplift disappears after removing joint-space guidance, the honest ceiling is that the route needed a deployment-time embodiment-specific steering layer; it is not yet evidence that the shared latent packet itself was sufficient.

This distinction is especially important for the paper's central thesis. D04 argues for a geometry-first transfer protocol with staged promotion from shared geometry to shared latent and only then to residual embodiment structure. EmbodiSteer shows that there is still a narrower layer after latent transfer but before embodiment-structure claims: a route may already encode the right coarse intent and contact progression, yet still depend on **inference-time joint-space recourse** to stay executable. By formalizing `\Theta_t`, we prevent deployment patches from being misreported as representational breakthroughs. In practical terms, this also gives future mixed ground--aerial or arm-to-arm experiments a new control family: if a policy only becomes stable when target-side joint-space steering is active, the paper must report **deployment-time executability support** before promoting any stronger cross-embodiment narrative.

### 3.6 Scene-Graph, Context-Encoding, and Aerial Structuring Supports after the Executability Gate

Even after geometry verification, latent retargeting, context residual modeling, and post-latent executability checks are fixed, a mixed ground--aerial route can still look stronger simply because the aerial side contributes better **scene decomposition**, **multi-scale context encoding**, or **future-world structuring**. The key D04 discipline is that these supports must be consumed before any upgrade to embodiment-agnostic interface claims. Otherwise, gains produced by stronger aerial organization of the world are misreported as stronger cross-embodiment transfer.

We therefore define an aerial-structuring support tuple
\[
\Phi_t^{struct}=(SGS,\; CES,\; WPS,\; GGS,\; LTS,\; HRS^{js},\; CW,\; PC),
\]
where `SGS` denotes scene-graph structuring support, `CES` denotes context-encoder support, `WPS` denotes world-prediction support, `GGS` denotes grounding/generalization support, `LTS` is the latent-transition sufficiency that remains after upstream subtraction, `HRS^{js}` is the post-executability residual survival, `CW` is the decisive consumption window, and `PC` is the promotion ceiling. In this paper, **scene-graph support** means that a route succeeds because it can organize landmarks, objects, traversable corridors, and interaction affordances into a more stable symbolic or graph-like world substrate before transfer is tested. **Context-encoder support** means that a route succeeds because it accumulates longer multi-scale history, route state, or neighborhood context into a more informative aerial planning state, even if the embodiment interface itself is unchanged.

Matched subtraction then extends the base promotion rule from Section 3.5 into
\[
\mathcal{C}_{ext}=
\{\text{terrain},\text{coordination},\text{contact},\text{IEC},\text{BPA},\text{BSC},\text{JGS/CAS/LLS},\text{SGS},\text{CES},\text{WPS},\text{GGS},\text{LTS},\text{SRS}\},
\]
with the additional requirement that a route may only keep a strong `LTS` or `SRS` claim if its residual remains positive after removing the aerial structuring families under the same context length, same prediction horizon, same grounding budget, and same decisive window. Concretely, let `\Delta_{row}` denote the end-task gain of a candidate route relative to the weakest geometry-valid baseline. Then the transferable residual after aerial structuring subtraction is
\[
HRS^{struct}=\Delta_{row}\setminus(SGS\cup CES\cup WPS\cup GGS),
\]
and only if `HRS^{struct}>\tau_{struct}` together with `HRS^{js}>\tau_{js}` do we allow promotion beyond aerial support explanations. This ensures that a route which only wins because it can build a better scene graph, hold better route context, imagine better futures, or cover grounding more broadly is frozen at those support families rather than upgraded to shared-interface necessity.

This extension matters because D04 increasingly interacts with aerial-manipulation and mixed-platform settings where the strongest adjacent systems are not necessarily better at embodiment transfer, but are often better at **organizing the world before transfer is asked to work**. WorldFly-style future imagination, FLIGHT-style pilot reasoning, WildRoadBench-style grounding, and D06-style scene-graph/context-encoder families all sharpen the same warning: planner-side world structuring gains are real and valuable, but they are not yet evidence that the same geometry packet, latent transition, and embodiment-facing interface truly survive across platforms. By placing `SGS/CES/WPS/GGS` after executability but before latent or specialist promotion, D04 stays honest about what kind of competence is actually being verified.


### 3.6 Geometry-Predictive Backbone Support before Embodiment Promotion

A geometry-first transfer stack can still look artificially strong if most of its gain is actually provided by a powerful **future-geometry action backbone** rather than by a reusable cross-embodiment interface. Geometric Action Model (GAM) [REF: 2606.17046] is the clearest current example: by combining a geometric foundation encoder, a causal future predictor, and action decoding in one network, it may stabilize viewpoint changes, pre-contact pose drift, and approach geometry before D04's staged retargeting logic is ever meaningfully stressed. We therefore introduce a dedicated geometry-predictive support family that must be consumed before a result can be promoted to shared latent sufficiency or remaining embodiment structure.

We define a geometry-predictive tuple
\[
\Gamma_t^{geo}=(GPS,\; FGS,\; ACS,\; LTS,\; HRS^{struct},\; CW,\; PC),
\]
where `GPS` denotes geometry-predictive backbone support, `FGS` denotes future-geometry stabilization support, `ACS` denotes action-coupled geometry support, `LTS` is latent-transition sufficiency after earlier subtraction, `HRS^{struct}` is the residual that survives planner-side structuring subtraction, `CW` is the decisive consumption window, and `PC` is the promotion ceiling. Intuitively, `GPS` asks whether a stronger geometric encoder alone already makes target-side pre-contact geometry more transferable, `FGS` asks whether explicit future geometry prediction explains the observed uplift, and `ACS` asks whether tightly coupling geometry and action heads already absorbs the transition structure that D04 would otherwise credit to explicit latent retargeting.

Matched subtraction then extends the promotion chain once more:
\[
\mathcal{C}_{geo}=
\{\text{terrain},\text{coordination},\text{contact},\text{IEC},\text{BPA},\text{BSC},\text{JGS/CAS/LLS},\text{SGS},\text{CES},\text{WPS},\text{GGS},\text{GPS},\text{FGS},\text{ACS},\text{LTS},\text{SRS}\}.
\]
For an evaluated route with gain `\Delta_{row}`, the residual after geometry-predictive subtraction is
\[
HRS^{geo}=\Delta_{row}\setminus(GPS\cup FGS\cup ACS),
\]
and only when `HRS^{geo}>\tau_{geo-pred}` together with `HRS^{struct}>\tau_{struct}` and `HRS^{js}>\tau_{js}` do we allow promotion beyond geometry-predictive support explanations. In plain terms, if a route only wins because its backbone already predicts cleaner future geometry, or because action generation is fused with geometry forecasting more effectively, then the honest ceiling remains **geometry-predictive support** rather than reusable embodiment interface evidence.

This addition is important because D04 increasingly sits between pure representation-transfer papers and stronger integrated geometric policy models. Without an explicit `GPS/FGS/ACS` blocker, the paper could overclaim staged transfer structure when the real gain is that a geometry-rich backbone has already solved much of the hard pre-contact and approach-phase prediction problem. By placing this family after planner-side structuring support but before latent or specialist promotion, D04 keeps its central claim honest: a reusable cross-embodiment interface should only be credited after stronger geometry-predictive backbones have already been matched and consumed.

### 3.7 Intervention-Value Recovery Support before Specialist Promotion

Even after geometry-predictive support is subtracted, a route can still improve because it has become better at **selecting which human recovery interventions to learn from**. ROVE [REF: 2606.17011] makes this explicit: deployment rollouts plus imperfect human interventions can raise manipulation performance when a value estimator filters out low-value takeovers and only feeds high-value recovery behaviors back into policy improvement. For D04, this means a route may succeed not because its shared interface is intrinsically stronger, but because it has acquired a better supervision-side mechanism for absorbing sparse near-failure rescue data.

We therefore add an intervention-value support tuple
\[
\Gamma_t^{rove}=(RVS,\; HIS,\; OVS,\; LTS,\; HRS^{geo},\; CW,\; PC),
\]
where `RVS` denotes recovery-value support, `HIS` denotes human-intervention selection support, `OVS` denotes optimistic value-selection support, `LTS` is latent-transition sufficiency after earlier subtraction, `HRS^{geo}` is the residual that survives geometry-predictive subtraction, `CW` is the decisive consumption window, and `PC` is the promotion ceiling. Conceptually, `RVS` asks whether the gain is dominated by better recovery-data curation, `HIS` asks whether sparse intervention examples themselves are doing the decisive work, and `OVS` asks whether value-based screening of those interventions is the real source of improvement.

The ordered claim set is then extended to
\[
\mathcal{C}_{rove}=
\{\text{terrain},\text{coordination},\text{contact},\text{IEC},\text{BPA},\text{BSC},\text{JGS/CAS/LLS},\text{SGS},\text{CES},\text{WPS},\text{GGS},\text{GPS},\text{FGS},\text{ACS},\text{RVS},\text{HIS},\text{OVS},\text{LTS},\text{SRS}\}.
\]
For a measured gain `\Delta_{row}`, the residual after intervention-value subtraction is
\[
HRS^{rove}=\Delta_{row}\setminus(RVS\cup HIS\cup OVS).
\]
Only if `HRS^{rove}>\tau_{rove}` together with `HRS^{geo}>\tau_{geo-pred}` do we allow promotion beyond recovery-value explanations. In practical terms, if a cross-embodiment route only becomes stable after it learns which human takeovers are worth imitating and which should be ignored, then the correct ceiling is **recovery-value support** rather than shared latent sufficiency or remaining embodiment structure.

This gate matters because near-failure rescue is likely to become common once D04 moves from static retargeting to difficult whole-body or mixed ground--aerial deployment. By formalizing `RVS/HIS/OVS`, we prevent the paper from overclaiming a stronger transfer interface when the real gain is a better filter over scarce human corrections. That keeps specialist promotion honest: specialist residuals should only be credited after both stronger geometry-predictive backbones and better intervention-value selection have already been matched and consumed.

### 4.1 Setup

We target mixed cross-embodiment transfer settings in which source and target platforms differ in morphology, kinematic tree, sensing layout, contact regime, and in some cases mobility carrier, but still share task-level geometric intent. The evaluation should cover eight matched control families: **human-to-humanoid retargeting without paired demonstrations** (Human2Humanoid [REF: 2606.03476]), **humanoid-to-humanoid transfer with explicit kinematic alignment and lightweight PEFT adaptation** (Any2Any [REF: 2605.23733]), **cross-platform policy deployment through a unified robot I/O substrate** (RIO [REF: 2605.11564]), **aerial future-prediction support** (WorldFly [REF: 2606.06147]), **long-horizon pilot-reasoning support** (FLIGHT [REF: 2606.06836]), **open-vocabulary aerial grounding support** (WildRoadBench [REF: 2605.20306]), **geometry-predictive backbone support** (GAM [REF: 2606.17046]), and **intervention-value recovery support** (ROVE [REF: 2606.17011]). This combination is intentional: the first three families test whether transfer was created upstream by supervision organization, alignment, or infrastructure cleanup, the next three test whether apparent mixed ground--aerial transfer is actually coming from stronger aerial prediction, reasoning, or grounding rather than from a reusable embodiment interface, the seventh tests whether a geometry-rich future-predictive backbone already absorbs the pre-contact and approach-phase structure that D04 might otherwise attribute to explicit latent retargeting, and the eighth tests whether deployment success is being driven by better filtering of sparse human recovery interventions rather than by a stronger shared interface.

For each family, we construct matched source-target tuples `(source embodiment, target embodiment, observation support, contact support, adaptation budget)` and require the same backbone scale, context length, training horizon, and target-side data fraction across ablations. The decisive comparison is not only end-task success, but whether the claimed gain is still visible after subtracting easier explanations from earlier sections: `terrain-state completion`, `coordination-state completion`, `contact-interface enrichment`, `kinematic-alignment gain`, `representation/infrastructure exposure`, `bounded prior-preserving adaptation`, `world-prediction support`, `pilot-reasoning support`, `grounding-side support`, `geometry-predictive support`, and `intervention-value recovery support`. Concretely, Human2Humanoid-style routes instantiate the **unpaired geometry-anchor** regime, Any2Any-style routes instantiate the **explicit alignment + tiny dynamics patch** regime, RIO-style routes instantiate the **representation/infrastructure exposure** regime, WorldFly-style routes instantiate the **aerial future-imagination** regime, FLIGHT-style routes instantiate the **frequency-decoupled pilot-policy** regime, WildRoadBench-style routes instantiate the **wild grounding coverage** regime, and GAM-style routes instantiate the **future-geometry action-backbone** regime, and ROVE-style routes instantiate the **critic-filtered intervention-reuse** regime. A proposed D04 method is only considered scientifically strong if it survives these matched comparisons under the same budget.

We therefore define the core evaluation bundle as
\[
\mathcal{B}^{D04}=\big(\mathcal{E}_{hum},\;\mathcal{E}_{align},\;\mathcal{E}_{rio},\;\mathcal{E}_{wm},\;\mathcal{E}_{pilot},\;\mathcal{E}_{ground},\;\mathcal{E}_{gam},\;\mathcal{E}_{rove},\;\mathcal{C}_{view},\;\mathcal{C}_{contact},\;\mathcal{C}_{budget}\big),
\]
where `\mathcal{E}_{hum}` denotes the Human2Humanoid-style unpaired transfer benchmark, `\mathcal{E}_{align}` the Any2Any-style aligned transfer benchmark, `\mathcal{E}_{rio}` the RIO-mediated deployment benchmark, `\mathcal{E}_{wm}` the WorldFly-style future-prediction control, `\mathcal{E}_{pilot}` the FLIGHT-style long-horizon pilot control, `\mathcal{E}_{ground}` the WildRoadBench-style grounding control, `\mathcal{E}_{gam}` the GAM-style geometry-predictive control, `\mathcal{E}_{rove}` the ROVE-style intervention-value recovery control, `\mathcal{C}_{view}` the cross-view perturbation control, `\mathcal{C}_{contact}` the contact/tactile support control, and `\mathcal{C}_{budget}` the matched adaptation-budget control. This setup turns the experiments into a true promotion audit: if a route only wins when explicit kinematic alignment is present, the honest ceiling is **alignment-support**; if it only wins when a tiny PEFT patch is enabled, the honest ceiling is **bounded-adaptation support**; if it only wins once unified I/O packaging is restored, the honest ceiling is **representation/infrastructure exposure**; if it only wins after aerial future prediction or pilot reasoning is strengthened, the honest ceiling remains an aerial-side support family; if it only wins after installing a geometry-predictive future-action backbone, the honest ceiling remains **geometry-predictive support**; and if it only wins after a critic starts filtering which human interventions are worth learning, the honest ceiling remains **intervention-value recovery support**.

### 4.2 Main Results

A reviewer-facing first-pass table should be organized around the same weakest-honest routing used in Section 3 rather than around a single end-task success number. For each route, we report whether the decisive gain is first consumed as terrain-state completion, coordination-state completion, contact-interface enrichment, kinematic-alignment gain, bounded dynamics-adaptation gain, representation/infrastructure exposure, prior-preserving bounded adaptation, bounded supervision/copilot support, world-prediction support, pilot-reasoning support, grounding-side support, geometry-predictive backbone support, shared latent sufficiency, joint-space executability support, self-model distinction support, or specialist residual survival. This forces Any2Any-style routes to declare whether they win because `K_t^{align}` and `G_t^{map}` already make the task structurally admissible, it forces Human-Robot-Copilot- or D-CLING-style routes to declare whether low-data uplift is still mainly coming from sparse human rescue or prior-preserving side adaptation, it forces mixed ground--aerial routes to declare whether they win because the aerial side simply became better at imagining, planning, or grounding before the embodiment interface itself was tested, it forces GAM-style routes to declare whether a geometry-predictive future-action backbone already explains the gain before explicit staged transfer logic is needed, it forces EmbodiSteer-style routes to declare whether target-side executable steering is still doing the last-mile work after latent transfer is nominally in place, and it now also forces self-model routes to declare whether the gain is coming from better **self-other separation and body-state grounding** rather than from a stronger reusable interface.

Concretely, every main-result row should at minimum log
\[
\Upsilon_{row}^{D04} = (TR,\; IGS,\; LTS,\; KAG,\; DAG,\; RIG,\; BPA,\; BSC,\; WPS,\; PRS^{air},\; GGS,\; GPS,\; FGS,\; ACS,\; RVS,\; HIS,\; OVS,\; JGS,\; CAS,\; LLS,\; SMS,\; OGS,\; HRS^{geo},\; HRS^{rove},\; HRS^{self},\; HRS^{js},\; SRS,\; CW,\; PC),
\]
where `TR` is end-task transfer rate, `IGS` is interface-geometry stability, `LTS` is latent-transition sufficiency after matched controls, `KAG` is kinematic-alignment gain, `DAG` is bounded dynamics-adaptation gain, `RIG` is representation/infrastructure exposure gain, `BPA` is prior-preserving bounded-adaptation gain, `BSC` is bounded supervision/copilot support gain, `WPS` is WorldFly-style world-prediction support, `PRS^{air}` is FLIGHT-style pilot-reasoning support, `GGS` is WildRoadBench-style grounding/generalization support, `GPS` is GAM-style geometry-predictive backbone support, `FGS` is future-geometry stabilization support, `ACS` is action-coupled geometry support, `RVS` is recovery-value support, `HIS` is human-intervention selection support, `OVS` is optimistic value-selection support, `JGS` is joint-space-guidance gain, `CAS` is collision-aware steering gain, `LLS` is limit-aware stabilization gain, `SMS` is self-modeling support, `OGS` is occupancy-grounding support, `HRS^{geo}` is the residual survival after subtracting geometry-predictive support, `HRS^{rove}` is the residual survival after subtracting intervention-value recovery support, `HRS^{self}` is the residual survival after subtracting self/other-distinction support, `HRS^{js}` is the residual survival after subtracting executable steering support, `SRS` is specialist-residual survival, `CW` is the decisive consumption window, and `PC` is the current promotion ceiling. A row is not allowed to promote beyond **alignment-support** if `KAG` dominates and `LTS` collapses under matched no-alignment controls; similarly, it cannot promote beyond **bounded-adaptation support** if `BPA` remains the only stable explanation after geometry and latent reuse are fixed, nor beyond **bounded supervision support** if the decisive rescue still comes from sparse human intervention. It also cannot promote beyond an aerial-side support ceiling if `WPS`, `PRS^{air}`, or `GGS` remains the only stable explanation after geometry and alignment are fixed. It cannot promote beyond **geometry-predictive support** if `HRS^{geo}` disappears once `GPS`, `FGS`, or `ACS` is removed under the same `CW`. It cannot promote beyond **intervention-value recovery support** if `HRS^{rove}` disappears once `RVS`, `HIS`, or `OVS` is removed under the same rollout-intervention budget. It cannot promote beyond **self-model distinction support** if `HRS^{self}` disappears once self-other separation or occupancy-grounding is removed under the same `CW`. Finally, it cannot promote beyond **joint-space executability support** if `HRS^{js}` disappears once `JGS`, `CAS`, and `LLS` are removed under the same `CW`.

This setup is especially important for future mixed ground--aerial transfer experiments. A UAV-to-arm route may look transferable simply because overhead geometry plus hand-designed kinematic remapping removes the hardest mismatch before execution starts, because low-data target adaptation quietly preserves a strong prior through a side branch, because sparse copilot intervention keeps the policy inside recoverable regions, because the aerial side is already much better at future prediction and language grounding, because a geometry-predictive future-action backbone has already absorbed the difficult pre-contact evolution, because a critic has learned which human interventions are worth retaining and which should be discarded, because a self-model resolves who the acting body actually is in cluttered shared space, or because a deployment-stage executable steering layer silently rescues the rollout once latent intent is decoded. Our table structure therefore requires the paper to say whether the observed gain was consumed pre-contact as a cleaner aligned packet, during adaptation as a prior-preserving patch, mid-rollout as a supervision-side rescue or aerial reasoning/prediction aid, at the geometry-action backbone level as future-geometry support, in the rollout-intervention loop as recovery-value support, during embodiment grounding as a self/other clarification layer, late in execution as target-side executable steering support, or only after all of those as true latent or specialist survival. In practice, this gives D04 a submission-ready experiment contract: **alignment, bounded adaptation, bounded supervision, world prediction, pilot reasoning, wild grounding, geometry-predictive backbones, intervention-value recovery, self-model distinction, and joint-space executable steering are all valid supports, but none are allowed to impersonate embodiment-agnostic interface verification.**

To make the table operational, we recommend eleven canonical row families. **Row A (Human2Humanoid control)** asks whether unpaired geometry anchors plus physics-aware feasibility already recover most transfer without explicit latent reuse; if yes, the gain stays at `UGA/PEC/MIE`-style support. **Row B (Any2Any control)** asks whether explicit kinematic alignment plus a tiny PEFT dynamics branch already explains the remaining uplift; if yes, the gain stays at `KAG/DAG`. **Row C (RIO control)** asks whether a route only becomes stable after robot I/O standardization and deployment cleanup; if yes, the gain stays at `RIG`. **Row D (D-CLING control)** asks whether a depth- or geometry-conditioned prior-preserving side branch already explains the low-data target uplift; if yes, the gain stays at `BPA`. **Row E (Human-Robot Copilot / ROVE control)** asks whether sparse intervention and bounded human rescue already explain the gain, and whether critic-filtered recovery-value selection is the decisive ingredient; if yes, the gain stays at `BSC/RVS/HIS/OVS`. **Row F (WorldFly control)** asks whether future-world imagination already explains the aerial uplift; if yes, the gain stays at `WPS`. **Row G (FLIGHT control)** asks whether low-frequency pilot reasoning plus high-frequency control already explains the long-horizon uplift; if yes, the gain stays at `PRS^{air}`. **Row H (WildRoadBench control)** asks whether broader aerial grounding coverage already explains the result; if yes, the gain stays at `GGS`. **Row I (GAM control)** asks whether a geometry-predictive future-action backbone already explains the pre-contact and approach-phase uplift; if yes, the gain stays at `GPS/FGS/ACS`. **Row J (Self-other distinction control)** asks whether proprioceptive-visual self-modeling and occupancy grounding are still required before cross-embodiment execution is stable in shared space; if yes, the gain stays at `SMS/OGS`-style self-model support. **Row K (EmbodiSteer control)** asks whether target-side joint-space guidance, collision-aware steering, and limit-aware stabilization are still needed after latent transfer and context support are fixed; if yes, the gain stays at `JGS/CAS/LLS`-style executability support. Only rows whose `LTS`, `HRS^{rove}`, `HRS^{self}`, and `HRS^{js}` survive all relevant control families under the same `CW` may be promoted to **shared latent sufficiency** or beyond.

### 4.3 Ablation Study

The ablation section should be written as a matched subtraction audit rather than as a flat list of modules. At minimum, we require toggles for `(i)` no geometry-anchor supervision, `(ii)` no explicit kinematic alignment, `(iii)` no lightweight PEFT dynamics patch, `(iv)` no unified robot I/O substrate, `(v)` no prior-preserving side adaptation, `(vi)` no bounded supervision/copilot intervention, `(vii)` no aerial future-prediction branch, `(viii)` no low-frequency pilot-reasoning branch, `(ix)` no aerial grounding support, and `(x)` no specialist residual branch. These toggles directly correspond to the local high-value anchors Human2Humanoid, Any2Any, RIO, D-CLING, Human-Robot Copilot, WorldFly, FLIGHT, and WildRoadBench, and they let the paper answer a harder question than “does our full model win?”—namely, *which weaker family still explains the win once the full stack is decomposed?*

We therefore recommend the following canonical matched ablations:
\[
\mathcal{A}^{D04}=\{A_{-hum},\; A_{-align},\; A_{-peft},\; A_{-rio},\; A_{-bpa},\; A_{-bsc},\; A_{-world},\; A_{-pilot},\; A_{-ground},\; A_{-gam},\; A_{-spec}\},
\]
where `A_{-hum}` removes unpaired geometry-anchor and physics-feasibility supervision, `A_{-align}` removes explicit kinematic alignment, `A_{-peft}` removes the tiny dynamics-sensitive adapter, `A_{-rio}` removes the unified I/O and deployment abstraction, `A_{-bpa}` removes the prior-preserving bounded-adaptation branch, `A_{-bsc}` removes bounded supervision/copilot rescue, `A_{-world}` removes WorldFly-style future prediction support, `A_{-pilot}` removes FLIGHT-style low-frequency pilot reasoning, `A_{-ground}` removes WildRoadBench-style aerial grounding support, `A_{-gam}` removes GAM-style geometry-predictive future-action support, and `A_{-spec}` removes the final specialist residual cleanup branch. The interpretation rule is strict: if performance collapses mainly under `A_{-align}` but remains stable under `A_{-world}`, `A_{-pilot}`, `A_{-ground}`, and `A_{-gam}`, the route is still best explained as **alignment-support**; if it collapses mainly under `A_{-bpa}`, the route remains **prior-preserving bounded-adaptation support**; if it collapses mainly under `A_{-bsc}`, the route remains **bounded supervision support**; if it collapses mainly under `A_{-world}`, the route remains **world-prediction support**; if it collapses mainly under `A_{-pilot}`, the route remains **pilot-reasoning support**; if it collapses mainly under `A_{-ground}`, the route remains **grounding-side support**; if it collapses mainly under `A_{-gam}`, the route remains **geometry-predictive support**; if only `A_{-spec}` matters after all earlier families are exhausted, then the gain can be promoted to **remaining embodiment structure**.

A small but critical detail is that each ablation must be reported with the same decisive window `CW` and the same adaptation budget. Without this constraint, a route could appear to survive subtraction merely because it consumed more context, more demonstrations, more target-side optimization, more sparse human intervention, or more aerial-side reasoning frequency than the control. For that reason, every ablation row should be paired with a budget witness tuple `(data fraction, update steps, context length, sensor support, prediction horizon, reasoning frequency, intervention budget)` and a weakest-honest tag from `{terrain, contact, coordination, alignment, infrastructure, bounded-adaptation, bounded-supervision, world-prediction, pilot, grounding, joint-space-executability, latent, specialist}`. This keeps D04 aligned with the core thesis of the paper: cross-embodiment success should be promoted only after all easier families have been exhausted under matched evidence.

A final deployment-stage ablation should explicitly test the new EmbodiSteer-style control family. We therefore add `A_{-js}` to the canonical control bank, where the shared geometry packet, latent-transition state, context branch, and all upstream support families are held fixed, but the target-side joint-space executable correction `\mathcal{E}_{js}` is removed. The corresponding report row should extend `\mathcal{A}^{D04}` to
\[
\mathcal{A}^{D04,+js}=\{A_{-hum},\; A_{-align},\; A_{-peft},\; A_{-rio},\; A_{-bpa},\; A_{-bsc},\; A_{-world},\; A_{-pilot},\; A_{-ground},\; A_{-js},\; A_{-spec}\},
\]
and log the deployment tuple `(JGS, CAS, LLS, HRS^{js}, CW, PC)`. The interpretation rule is again weakest-honest: if performance drops mainly under `A_{-js}` while latent-transition statistics remain otherwise intact, the route must stop at **joint-space executability support** rather than being promoted to shared-latent sufficiency or remaining embodiment structure. This gives the experiments section a clean final guardrail: even after upstream supervision, alignment, infrastructure, bounded adaptation, bounded supervision, prediction, and reasoning families have all been exhausted, a zero-shot route may still be winning only because a target-specific executable correction layer kept the rollout inside safe and feasible joint-space trajectories.

A second final-stage audit should explicitly test the newly separated **planner-side world-structuring** families. We therefore extend the control bank once more with
\[
\mathcal{A}^{D04,+struct}=\{A_{-hum},\; A_{-align},\; A_{-peft},\; A_{-rio},\; A_{-bpa},\; A_{-bsc},\; A_{-world},\; A_{-pilot},\; A_{-ground},\; A_{-js},\; A_{-sg},\; A_{-ctxenc},\; A_{-wps},\; A_{-ggs},\; A_{-spec}\},
\]
where `A_{-sg}` removes scene-graph structuring support, `A_{-ctxenc}` removes context-encoder support, `A_{-wps}` removes future-world prediction support when it is used as a planner-side structuring aid rather than a pure rollout model, and `A_{-ggs}` removes grounding/generalization support. Every such row should report the structuring tuple
\[
\Xi_{row}^{struct}=(SGS,\; CES,\; WPS,\; GGS,\; HRS^{struct},\; HRS^{js},\; CW,\; PC),
\]
under the same context length, same prediction horizon, same grounding budget, and same decisive window as the full route. The interpretation rule is again conservative: if a route collapses mainly under `A_{-sg}` or `A_{-ctxenc}`, the honest ceiling remains **planner-side structuring support** rather than shared-interface evidence; if it collapses mainly under `A_{-wps}` or `A_{-ggs}`, the route remains **future-world support** or **grounding/generalization support**. Only if `HRS^{struct}` and `HRS^{js}` both remain positive after these removals may the result continue to support shared latent sufficiency or remaining embodiment structure. This gives D04 a last reviewer-facing guardrail: a mixed ground--aerial route is not allowed to claim cross-embodiment interface strength merely because it became better at organizing landmarks, preserving multi-scale route context, imagining the next world segment, or widening aerial grounding coverage before execution.

A third final-stage audit should now explicitly separate **aerial support-side world structuring** from **cross-view cross-embodiment geometry survival** inside the same reviewer-facing protocol. WorldFly [REF: 2606.06147], FLIGHT [REF: 2606.06836], and WildRoadBench [REF: 2605.20306] together suggest that a mixed ground--aerial route can improve for at least three weaker reasons before the paper is allowed to claim reusable embodiment transfer: `(i)` the aerial side imagines the next traversable world segment more accurately, `(ii)` the aerial side carries a stronger low-frequency pilot/planner state over long horizons, or `(iii)` the aerial side simply grounds open-vocabulary landmarks and road-level targets more reliably. We therefore recommend an explicit control bundle in which the same shared geometry packet is replayed under `matched future horizon`, `matched pilot reasoning frequency`, and `matched grounding coverage` so that the D04 claim is only promoted when residual uplift is still visible after these three aerial supports are removed.

Formally, for every row that uses aerial assistance we additionally report
\[
\mathcal{S}_{row}^{air}=(Q^{wm}_{air},\; Q^{pilot}_{air},\; Q^{ground}_{air},\; HRS^{air-struct},\; CW,\; PC),
\]
where `Q^{wm}_{air}` denotes the gain attributable to aerial future-world imagination, `Q^{pilot}_{air}` denotes the gain attributable to low-frequency pilot reasoning or multi-stage route carrying, and `Q^{ground}_{air}` denotes the gain attributable to broader grounding/generalization coverage. The residual
\[
HRS^{air-struct}=\Delta_{row}\setminus(Q^{wm}_{air}\cup Q^{pilot}_{air}\cup Q^{ground}_{air})
\]
must remain positive under the same view perturbation, same adaptation budget, and same decisive window before the paper is allowed to keep a stronger `LTS`, `HRS^{js}`, or `SRS` reading. In plain terms, if the result disappears once WorldFly-style future prediction, FLIGHT-style pilot reasoning, or WildRoadBench-style grounding coverage is matched away, then the honest ceiling is still **aerial-side structuring support** rather than geometry-conditioned latent transfer.

This extra audit matters because D04 is no longer only competing against robot-to-robot retargeting papers; it is increasingly competing against aerial systems that organize the world better before transfer is even asked to work. By forcing `\mathcal{S}_{row}^{air}` into the same table as `\Upsilon_{row}^{D04}` and `\Xi_{row}^{struct}`, we make the final reviewer-facing readout much harder to game: a route is not allowed to claim cross-embodiment strength merely because it sees farther into the future, keeps a cleaner long-horizon pilot state, or names aerial targets more reliably. It must still show that the **same transferable packet remains useful after those aerial supports are honestly consumed**.

## References

[TODO: keep existing references list and renumber after Method stabilization]
