# Aerial Manipulation Data Factory: Scalable Synthetic Data Generation via World Model Simulation

> 方向：D05 数据飞轮 | 目标会议：CoRL 2027 | 状态：🔴 草稿
> 最后更新：2026-04-22

---

## Abstract

[TODO: 150-250词]

---

## 1. Introduction

### 1.1 Problem Statement

Aerial manipulation data collection is prohibitively expensive: real UAV flights require safety operators, controlled environments, and significant time per trajectory. Existing simulation-to-real approaches for ground manipulation (RoboAgent, RoboGen, etc.) do not account for aerial dynamics, making direct application infeasible.

The key question is: **can a world model serve as a scalable aerial manipulation data factory, generating physically plausible and dynamically consistent synthetic trajectories that improve downstream policy performance?**

### 1.2 Contributions

1. **C1: Aerial Manipulation Data Factory**: World model-based synthetic data generation pipeline for aerial manipulation, incorporating flight dynamics constraints.
2. **C2: Dynamics-Consistent Trajectory Synthesis**: Physics-aligned trajectory generation ensuring velocity, acceleration, and jerk consistency with real UAV platforms.
3. **C3: Sim-to-Real Transfer Protocol**: Systematic protocol for validating synthetic data quality and measuring downstream policy improvement.

---

## 2. Related Work

### 2.1 Synthetic Data for Robot Learning

Recent robot data generation pipelines increasingly treat data production as a first-class systems problem rather than a by-product of policy training. ComSim [REF: 2604.11386] shows that a compositional real-sim-real loop, combining classical simulation with neural simulation, can improve the realism-cost trade-off of synthetic robot data. ShapeGen [REF: 2604.15569] further isolates object-shape diversity as an independent scaling axis, suggesting that category-level manipulation performance often saturates because geometric coverage is narrow rather than because policies are under-parameterized. CRAFT [REF: 2604.03552] complements these lines by using video diffusion to augment action-conditioned demonstrations, indicating that trajectory-view coverage can also be scaled without rerunning expensive simulation.

### 2.2 World Models as Data Generators

PlayWorld [REF: 2603.09030] demonstrates that interaction-rich autonomous play data significantly improves contact-rich dynamics fidelity and failure prediction, with up to 65% success rate improvement on real robot tasks. This suggests data coverage structure is often the binding constraint rather than model architecture. More broadly, these results motivate using a world model not merely as a predictor, but as a controllable generator that can roll out rare contact events, recovery behaviors, and long-horizon state transitions that are costly to capture in real flights.

### 2.3 Data Organization and Flywheel Dynamics

F-ACIL [REF: 2603.25583] argues that robotic data should be explicitly factorized along object, action, and environment axes, and that iterative collection should focus on under-covered compositional corners rather than uniformly adding more demonstrations. This perspective is especially relevant for aerial manipulation, where the same semantic task can fail for very different reasons: target geometry mismatch, aerodynamic disturbance, poor approach angle, or unstable contact timing. Therefore, a useful aerial data flywheel must scale not only the number of trajectories, but also the coverage accounting over disturbance regime, contact phase, and reset/recovery outcomes.

### 2.4 Limitations of Existing Work

Existing synthetic data pipelines are still centered on ground robots, rigid workspaces, or offline augmentation stages. They rarely model aerial dynamics constraints explicitly, they do not define quality metrics for manipulation-ready flight trajectories, and they under-specify how recovery data, near-failure data, and disturbance-conditioned data should be promoted back into the training set. As a result, current pipelines can generate more samples, but they cannot yet guarantee that those samples improve downstream aerial deployment robustness in a measurable and accountable way.

A second limitation is that current flywheel pipelines usually collapse heterogeneous supervision into a single replay buffer. Robot-Powered Data Flywheel [REF: 2511.19647] makes clear that real deployment naturally produces different supervisory value types, while F-ACIL [REF: 2603.25583] argues that coverage should be accounted for structurally rather than volumetrically. However, existing systems still under-specify when a weakly auto-labeled trace, a near-failure trace, or a recovery trace is mature enough to be promoted into the main corpus. This leaves a methodological gap between “data growth” and “accountable data growth,” especially for aerial manipulation where disturbance, contact timing, and reset cost are tightly coupled.

## 3. Method

### 3.1 Overview

We propose an aerial manipulation data factory in which a world model serves as a deployment-accountable synthetic data generator rather than a purely generative simulator. The pipeline starts from a small set of real anchored trajectories, augments them with structured perturbations over object, action, and environment factors, rolls them forward in a dynamics-aware world model, and retains only those synthetic segments that satisfy manipulation-readiness checks. The resulting dataset is not a monolithic replay buffer: it is indexed by disturbance regime, contact phase, reset outcome, and recovery value, so that downstream policy training can target the failure modes that most often block real-world deployment.

### 3.2 Factorized Scenario and Trajectory Synthesis

Following the factor-aware view of F-ACIL [REF: 2603.25583], we model each synthetic sample as a tuple of object state, task/action specification, environment context, and flight-disturbance condition. Instead of sampling these factors independently at random, the generator prioritizes sparse or brittle compositional regions, such as crosswind-plus-thin-handle grasps or visually ambiguous approach corridors with delayed contact windows. This design turns data generation into coverage balancing: the goal is not to maximize sample count, but to raise support over task-relevant but underrepresented combinations that dominate aerial failure cases.

### 3.3 Promotion Rules for World-Model-Generated Data

A central requirement of our framework is that synthetic data must earn its place in training. We therefore introduce promotion rules that separate (i) kinematically plausible but manipulation-irrelevant flight segments, (ii) task-completing yet disturbance-fragile behaviors, and (iii) genuinely valuable samples that preserve handoff quality to the downstream controller. A synthetic rollout is promoted only when it improves at least one deployment-facing criterion: successful contact timing, stable post-contact state evolution, recovery from near-failure, or improved robustness under a specified disturbance bucket. In this sense, the world model is not judged by visual realism alone, but by whether its generated trajectories change downstream policy behavior in the regimes that matter.

### 3.4 Recovery-Centric Data Flywheel

Unlike conventional pipelines that mostly retain successful demonstrations, our data factory explicitly treats near-failure and recovery segments as high-value supervision. Rollouts that miss grasp timing, drift during approach, or destabilize after contact are not discarded if they expose a recoverable strategy boundary. Instead, they are relabeled into recovery buckets and reintroduced as targeted training material for disturbance-aware policy improvement. This closes the loop between real failures, world-model expansion, and retraining: each deployment round updates the coverage map, and the next synthetic generation round focuses on the unrecovered corners rather than repeating already-solved cases.

Concretely, we adopt a seed-demo-to-self-improvement loop inspired by recent data-flywheel systems such as Robot-Powered Data Flywheel and DexFlyWheel [REF: 2511.19647; REF: 2509.23829]. A small set of operator-verified anchor trajectories is used only to initialize the policy and world-model conditioner; subsequent data growth is dominated by autonomous rollouts, quality filtering, and failure-bucket replay. This framing is important for aerial systems because the bottleneck is rarely one-shot dataset construction, but rather whether the system can keep harvesting new supervision from drift, mistimed contact, occluded targets, and aborted recovery attempts without requiring a human pilot to relabel every iteration.

### 3.5 Disturbance-Bucketed Promotion with Wind-Aware Filtering

For aerial manipulation, disturbance is not a nuisance variable but a first-class indexing axis. Motivated by onboard wind estimation for small UAVs [REF: 2604.20290], we partition both real-anchor and synthetic rollouts into disturbance buckets defined by estimated wind magnitude, wind-direction change rate, and approach-phase attitude correction demand. A sample is not promoted merely because it succeeds nominally; it must also be labeled with the disturbance regime under which it remains executable, such as calm-hover grasping, crosswind approach correction, or post-contact rejection under slow gust accumulation. This design makes downstream policy training accountable to the exact environmental regime it is expected to survive.

Operationally, the world model receives a disturbance token together with task and embodiment state, and generates trajectories conditioned on regime-specific perturbation envelopes rather than globally randomized noise. Low-cost onboard sensing does not need to perfectly reconstruct the full flow field; it only needs to provide a sufficiently stable partition of deployment conditions so that hard examples are replayed into the correct bucket instead of being mixed into a single undifferentiated failure pool. As a result, the data flywheel can ask a more meaningful question than “did the rollout work”: it can ask whether a trajectory remains promotable under the same disturbance class that will later appear in real deployment.

### 3.7 Heterogeneous Supervision Contracts and Promotion Gates

To prevent synthetic scale from becoming supervision noise, we formalize each collected segment with a supervision contract rather than treating all data as interchangeable. Concretely, every segment is routed into one of four bucket families: successful task-completing traces, near-failure traces with actionable failure phases, recovery traces that cross the failure boundary back to success, and weak-label traces derived from environment metadata or low-confidence automatic annotation. This routing is motivated by Robot-Powered Data Flywheel [REF: 2511.19647], which highlights that deployment naturally produces heterogeneous supervision, and by F-ACIL [REF: 2603.25583], which implies that data quality must be tracked jointly with factor coverage.

A segment is promoted only if it satisfies a small set of accountable gates. First, it must be replayable under matched initialization, so that its supervisory value is not a one-off artifact. Second, it must preserve at least the object, action, environment, and outcome fields required for factor-aware reuse. Third, if it is a failure-derived sample, its failure phase and last safe state must be explicit enough to support recovery-oriented learning rather than merely increasing dataset volume. Finally, at least one downstream use must be identifiable: cross-embodiment transfer support for D04, navigation-recovery support for D06, or disturbance-survival support for D07-style control tasks. These gates convert the flywheel objective from maximizing synthetic volume into maximizing reusable, diagnosable, and transfer-linked supervision.

## 4. Experiments

### 4.1 Setup

We evaluate the proposed data factory on aerial manipulation tasks with a small set of real-anchor demonstrations and a larger pool of world-model-generated synthetic rollouts. The benchmark should include at least three task families: contact-free approach, single-contact grasp/attach, and post-contact transport or stabilization. For each task, we define factor labels over object type, action template, environment layout, disturbance bucket, and bucket-specific outcome type, and compare policies trained with different promotion strategies under a fixed real-data budget.

We consider three training protocols: (i) real-anchor-only training, (ii) synthetic expansion without promotion control, and (iii) our disturbance-bucketed promotion pipeline. To isolate the contribution of replayability-gated supervision, we additionally compare whether near-failure segments are discarded, naively retained, or routed into explicit recovery buckets, and whether weakly auto-labeled segments are mixed directly into the main corpus or held as auxiliary supervision. Evaluation is performed both in held-out simulation regimes and in real or high-fidelity replay settings with matched disturbance annotations.

### 4.2 Main Results

The primary hypothesis is that downstream performance is limited less by raw sample count than by whether synthetic data is promoted with disturbance accountability. We therefore expect the strongest gains to appear not in nominal success rate alone, but in regime-conditioned robustness: crosswind grasp completion, post-contact stabilization success, and recovery probability after timing mismatch. A method that generates many visually plausible trajectories but fails to improve these disturbance-conditioned metrics should be treated as an inadequate data generator even if its aggregate success rate looks competitive.

We will report results by disturbance bucket rather than only in aggregate. This is important because a policy that improves in calm settings while regressing under moderate crosswind should not be mistaken for a better deployment policy. Tables should therefore separate nominal buckets from hard buckets and include sample-efficiency views showing how much real-anchor data is saved by world-model expansion.

### 4.3 Ablation Study

Ablations focus on which indexing and promotion components are truly necessary. First, we remove factorized coverage accounting and replace it with uniform synthetic sampling to test whether compositional under-coverage, rather than model capacity, is the bottleneck. Second, we remove disturbance bucketing and train on a pooled dataset to test whether wind-aware regime labels are essential for aerial robustness. Third, we drop recovery relabeling and keep only successful demonstrations to quantify the value of near-failure supervision.

A final ablation tests the source of disturbance labels. We compare oracle disturbance annotations, onboard low-cost estimation [REF: 2604.20290], and no explicit disturbance estimate. If low-cost onboard estimation is already sufficient to preserve promotion quality, then the data factory becomes practical for field deployment because it avoids requiring expensive instrumentation while still keeping the synthetic replay loop aligned with real environmental regimes.

We further include a flywheel-growth ablation that compares three data accumulation regimes under the same real-anchor budget: static one-shot augmentation, autonomous rollout expansion without failure replay, and autonomous rollout expansion with hard-bucket replay. This ablation is designed to isolate whether iterative self-improvement, rather than raw synthetic volume, is what drives policy gains. If the full loop consistently improves recovery success and hard-regime robustness with fewer human demonstrations, it would provide direct evidence that the proposed system behaves like a true aerial data flywheel rather than a conventional offline simulator.

### 4.4 Replayability and Bucket-Purity Audits

Because D05 makes stronger claims about data organization than about raw generation scale, we add explicit audits that measure whether the flywheel remains honest about what kind of supervision it is accumulating. We therefore report bucket-purity statistics: the fraction of samples in each bucket whose labels remain stable under replay, the proportion of near-failure samples with actionable failure-phase annotations, and the promotion rate of weak-label traces after confidence auditing. These metrics are complementary to task success because a system that improves briefly by flooding the corpus with noisy weak labels is not a trustworthy data factory.

We also define a replayability audit under matched reset conditions. For each promoted sample, we check whether the trajectory can be replayed with sufficiently small deviation in contact timing, post-contact stabilization, and termination label. Samples that fail this audit are demoted or isolated from the main training pool even if they looked successful once. This makes the experimental section consistent with the methodological claim of Section 3.6: data-flywheel growth is only meaningful when dataset expansion preserves reusable supervision structure instead of silently accumulating irreproducible traces.

### 4.5 Minimal Promotion-Gate Audit for First Deployment

Before scaling the full flywheel, we propose a first-deployment audit that asks a simpler question: does the system produce samples that are not only numerous, but eligible for honest reuse? The audit reports four operational rates under a fixed real-anchor budget: replay pass rate, actionable-failure rate, weak-label promotion rate, and transfer-linked usage rate. These statistics are computed per disturbance bucket so that the flywheel cannot hide poor hard-regime behavior behind nominal-condition abundance.

This first-deployment audit is intentionally narrow. It does not claim that the world model has solved aerial data generation end to end; instead, it tests whether the pipeline has crossed the minimum threshold for accountable growth. A data factory that produces many nominal successes but low replay pass rate, low actionable-failure density, or negligible downstream reuse should be interpreted as a buffer-expansion system rather than a true flywheel. By contrast, if promotion-gated samples consistently survive replay, preserve bucket purity, and improve at least one downstream regime-specific metric, then the system has earned the stronger claim of reusable synthetic supervision.

---

## 5. Conclusion

[TODO]

---

## References

[1] PlayWorld. arXiv:2603.09030, 2026.
[2] ComSim. arXiv:2604.11386, 2026.
[3] ShapeGen. arXiv:2604.15569, 2026.
[4] CRAFT. arXiv:2604.03552, 2026.
[5] F-ACIL. arXiv:2603.25583, 2026.
[6] Robot-Powered Data Flywheel. arXiv:2511.19647, 2025.
[7] DexFlyWheel. arXiv:2509.23829, 2025.
[8] Wind Disturbance Estimation for Small Unmanned Aerial Vehicles. arXiv:2604.20290, 2026.
[TODO: 补充完整作者、会议信息与其余引用列表]
