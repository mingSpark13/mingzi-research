# Layered Transfer of Ground Manipulation Policies to Aerial Platforms

> 方向：D03 空地迁移 | 目标会议：ICRA 2027 | 状态：🔴 草稿
> 最后更新：2026-04-22

---

## Abstract

[TODO: 150-250词]

---

## 1. Introduction

### 1.1 Problem Statement

Ground manipulation methods (ACT, Diffusion Policy, VLA, RL) have accumulated substantial results, but direct transfer to aerial manipulation faces fundamental challenges: (1) vibration and payload disturbances degrade end-effector precision; (2) flight dynamics constraints limit workspace and motion speed; (3) visual and sensor configurations differ significantly; (4) aerial data collection costs far exceed ground collection.

The critical question is not whether ground methods can transfer unchanged, but rather: **which layers can transfer directly, and which layers require aerial-specific adaptation?** Specifically, visual representations, task semantics, action priors, low-level control shells, safety constraints, and sim-to-real components each have different transferability profiles.

### 1.2 Contributions

1. **C1: Dynamics-Aware Policy Transfer Layer**: Explicit modeling of flight dynamics constraints as a policy adaptation layer, injecting payload/jerk/acceleration/safety guidance at inference time.
2. **C2: Layered Transfer Methodology**: Systematic decomposition of what transfers (visual representations, task semantics, goal relations) vs. what must be adapted (control frequency, action space, stability shell, safety constraints).
3. **C3: Navigation-Manipulation Transfer Interface**: Unified interface connecting D06 navigation outputs to aerial manipulation policy inputs.

---

## 2. Related Work

### 2.1 Aerial VLA Transfer

π-Make-It-Fly [REF: ] demonstrates that visual representations transfer but control dynamics do not, proposing Payload-Aware Guidance. AirVLA [REF: ] provides quantitative evidence: visual priors transfer zero-shot, but dynamics constraints must be injected at inference time (pick-and-place: 23% → 50%). Precise Aggressive Aerial Maneuvers [REF: 2604.05828] shows that sim-to-real success depends on smooth action constraints, velocity constraints, and perception distillation/regularization—suggesting aerial transfer requires execution stability shells beyond high-level representation adaptation.

### 2.2 Aerial Manipulation Systems

[TODO: 补充相关工作]

### 2.3 Limitations of Existing Work

(1) π-Make-It-Fly/AirVLA prove visual representations transfer but do not systematize control dynamics transfer.
(2) No reproducible "ground-to-aerial" transfer methodology exists with layered validation.
(3) Aerial manipulation + navigation joint framework is absent.
(4) Deployment-oriented sim-to-real constraint checklists are missing.

---

## 3. Method

### 3.1 Layered Transfer Framework

```
Ground Policy Prior (ACT / Diffusion Policy / VLA / RL)
        │
        ├─ Directly Reusable: visual representations / task semantics / goal relations
        │
        ├─ Transfer Adaptation Layer: action interface mapping + payload-aware guidance
        │                             + dynamics-aware cost
        │
        ├─ Low-Level Execution Shell: smoothness / speed / safety constraints / recovery
        │
        └─ Aerial-Specific Components: flight dynamics model / aerial sensor config
```

### 3.2 Dynamics-Aware Policy Transfer (C1)

[TODO: 具体描述动力学感知的策略迁移层。如何在推理时注入payload/jerk/acceleration/safety guidance？参考π-Make-It-Fly的Payload-Aware Guidance。]

### 3.3 Layered Transfer Validation Protocol (C2)

[TODO: 描述分层迁移验证协议。如何系统地验证哪些层可以迁移，哪些层需要适配？]

---

## 4. Experiments

### 4.1 Setup

[TODO: 实验设置]

### 4.2 Main Results

[TODO: 实验结果]

### 4.3 Ablation

**A1**: Direct transfer vs. + dynamics-aware adaptation layer
**A2**: Without execution shell vs. + stability shell
**A3**: Ground-only training vs. + aerial fine-tuning

---

## 5. Conclusion

[TODO]

---

## References

[1] π-Make-It-Fly. arXiv: [TODO], 2026.
[2] AirVLA. arXiv: [TODO], 2026.
[3] Precise Aggressive Aerial Maneuvers. arXiv:2604.05828, 2026.
[TODO: 补充完整引用列表]
