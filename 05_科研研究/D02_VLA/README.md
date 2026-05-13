# 方向二：用于具身操作的视觉语言动作模型

> VLA：视觉+语言+动作的端到端策略学习

## 研究目标

- 梳理 VLA 发展链条（RT-1 → RT-2 → OpenVLA / π0 / GR00T / UniDex）
- 发现 VLA 在操作领域的核心瓶颈
- 归纳主人可行的 VLA 项目路线

## 核心问题

- VLA 如何支持高频精细操作（vs 导航的低频决策）？
- 开源 VLA（OpenVLA/openpi）在主人硬件上的可行性？
- VLA 与传统控制的结合点？

## 已有知识库论文

- `2026-03-27_OpenVLA.md`
- `2026-03-27_pi0.md`
- `2026-03-27_RT-1.md`
- `2026-03-27_RT-2.md`
- `2026-03-27_OnFly.md`
- `2026-03-28_UniDex.md`
- `2026-03-28_LaST0.md` — 隐式时空CoT+MoT双专家（与Paper A层次化解耦高度相关）
- `2026-03-28_ManualVLA.md` — MoT+ManualCoT多模态手册生成（与Paper A高度相关）
- `2026-03-28_Real2Edit2Real.md` — 3D控制接口数据生成，仅1-5条真机→10-50x数据效率（CVPR 2026）
- `2026-04-24_2604.20472_TD_Calibration_VLA.md` — 用 TD value estimation 做顺序任务中的 VLA 置信度校准，适合作为部署安全护栏/接管触发信号

## 花火研究笔记

### 2026-04-24 R941：Temporal Difference Calibration in Sequential Tasks（VLA 可靠性从后验分数推进到时序价值校准）
- **Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models** (2604.20472)
  - **核心发现**: 把 sequential calibration 明确写成 episodic 任务上的时序置信度估计问题，并证明其风险最优解与 value function 对齐，因此可以直接用 TD estimation 做 VLA 校准。
  - **为什么有价值**: 这不是单纯“再加一个 uncertainty head”，而是把 VLA 的 success confidence 与 RL 价值学习打通，更适合作为真实部署时的 risk signal。
  - **可落地实验点**: 给现有 VLA rollout 增加 confidence head，对比 `原始 action probability`、`temperature scaling`、`TD calibration` 三档，重点看高置信失败率、提前预警能力与人工接管触发质量。
  - **入库判断**: ✅ 入库。更适合作为 D02 的 **deployment reliability / safety wrapper** 锚点，而不是能力提升主线。

### 2026-04-13 R669：SV-VLA + Legato（低层从单一 chunk 调度升级为 verifier + continuation 壳层）
- **SV-VLA / Open-Loop Planning, Closed-Loop Verification** (2604.02965)
  - **核心发现**: 用低频 macro-planner 先生成 action chunks，再让 lightweight verifier 高频闭环校验，必要时触发重规划。
  - **为什么有价值**: 继续坐实 `强动作器 + 轻校验壳层` 是最稳的工程路线，不该只靠裸 chunked/open-loop 执行硬扛 stale observation。
  - **可落地实验点**: 对比 `裸动作器` vs `动作器+verifier` 的 unsafe-action pass-through rate、恢复速度与重规划频率。
- **Legato / Learning Native Continuation for Action Chunking Flow Policies** (2602.12978)
  - **核心发现**: 用 native continuation 减少 chunk 边界的 spurious switching 与轨迹不连续。
  - **为什么有价值**: 说明低层除了调 chunk 和算力，还应预留 **continuation / chunk smoothing** 增强位，专门修正边界拼接不稳。
  - **可落地实验点**: 增加 `动作器+verifier` vs `动作器+verifier+continuation/smoothing` 对照，重点看 chunk stitching stability 与 near-miss 场景误执行。
- **入库判断**: ✅ 低层协议继续收束为 `裸动作器`、`动作器+verifier`、`动作器+verifier+continuation/smoothing` 三档。

### 2026-04-12 R663：AutoHorizon + VLA Knows Its Limits（execution horizon 从固定超参升级为可解释自适应）
- **VLA Knows Its Limits / AutoHorizon** (2602.21445)
  - **核心发现**: 固定 execution horizon 会在“响应性 vs 连续性”之间反复失衡，而 flow-based VLA 的 action self-attention 可以直接当作 **predictive limit proxy**，用于 test-time 动态估计每个 chunk 该执行多长。
  - **为什么有价值**: 这让 Paper A 低层的 **adaptive chunk scheduler** 从“经验调参”升级成“可解释、随感知条件变化的在线调度器”，而不是只靠动作熵或手工阈值。
  - **可落地实验点**: 给现有低层执行器补 `fixed horizon` vs `entropy-guided` vs `attention-guided AutoHorizon` 三档对照，重点看恢复速度、chunk stitching stability、near-miss 场景下的误执行长度。
  - **入库判断**: ✅ 作为低层调度协议的重要补强保留。

### 2026-04-12 R648：AAC + SV-VLA + AC^2-VLA + Legato（低层调度/校验协议继续收束）
- **Adaptive Action Chunking at Inference-time for VLA Models** (2604.04161)
  - **核心发现**: action chunk 不该固定写死，而应随当前不确定性与观测变化动态调整，以在响应性和轨迹连续性之间折中。
  - **为什么有价值**: 继续坐实 Paper A 低层需要显式 **adaptive chunk scheduler**，而不是单一固定 chunk。
  - **可落地实验点**: 给现有低层执行器补 `fixed chunk` vs `adaptive chunk` 对照，重点看 jerky behavior、恢复速度与重规划频率。
- **SV-VLA** (2604.02965)
  - **核心发现**: open-loop chunk execution 外侧可加 **lightweight verifier** 做 closed-loop 校验，必要时再触发重规划。
  - **为什么有价值**: 说明“强动作器 + 轻校验壳层”仍是最稳的工程路线。
  - **可落地实验点**: 对比 `裸动作器` vs `动作器+verifier` 的 unsafe-action pass-through rate 与恢复能力。
- **AC^2-VLA** (2601.19634)
  - **核心发现**: 高成本 VLA 推理里的 temporal / spatial / depth 冗余可以做 **budget-aware adaptive computation**。
  - **为什么有价值**: 补强 Paper A 的 **budget-aware compute scheduler** 支线。
  - **可落地实验点**: 增加 `只调 chunk` vs `chunk+compute 双调度` 的延迟与稳定性对照。
- **Legato** (2602.12978)
  - **核心发现**: 用 training-time continuation 减少 chunk 边界的 spurious switching 与轨迹不连续。
  - **为什么有价值**: 提醒低层除了调 chunk 和算力，还应预留 **native continuation / chunk smoothing** 增强位。
  - **可落地实验点**: 后续把 `continuation/smoothing` 作为低层稳定性增强附加实验。


### 2026-03-29 第3轮：新论文扫描
- **LILAC** (2603.25481) ⭐⭐⭐ - Flow-based VLA，光流→轨迹而非直接动作生成，泛化性强。**可落地：Paper A 低层**
- **TIES** (2603.24941) ⭐⭐⭐ - VLA token剪枝，78%减少+6%提升，无需训练。**可落地：Paper A 推理加速**
- **ThermoAct** (2603.25044) ⭐⭐ - 热感VLA，安全增强。**可落地：Paper A 安全层热感反馈**
- **SABER** (2603.24935) ⭐⭐ - VLA对抗攻击，红队测试参考
- **3D-Mix** (2603.24393) ⭐⭐ - 3D信息即插即用VLA模块，**可落地：几何一致性**

### 2026-03-28 第2轮：VLA 全景分析 — 核心空白确认

**背景**：第1轮发现「纯端到端 VLA 不适合空中精细操作」，本轮系统梳理现有 VLA 路线验证这一判断。

#### 现有 VLA 方法分类

| 方法 | 架构类型 | 精细操作 | 意图规划层 | 层次化解耦 |
|------|---------|---------|-----------|-----------|
| OpenVLA | 纯端到端 | 一般 | 无 | ❌ |
| π0 | 纯端到端（flow matching） | 一般 | 无 | ❌ |
| GR00T | 纯端到端（cross-embodiment） | 一般 | 无 | ❌ |
| GO-1 | 纯端到端（大数据） | 一般 | 无 | ❌ |
| UniDex | 纯端到端（FAAS 动作空间） | 较好（灵巧手） | 无 | ❌ |
| ACT | Action chunking（时序聚合） | 较好 | 无 | ⚠️ 部分（时序，非意图层） |
| OnFly | 双 agent（感知解耦） | 较好（导航） | 有限 | ⚠️ 部分（感知/控制频次解耦） |

#### 核心发现

**现有 VLA 均无真正的「意图规划 ↔ 精细执行」层次化解耦。**

- ACT 的 action chunking 是**时序聚合**而非意图层解耦：同一策略生成一段动作，低层并无独立精细控制
- OnFly 的双 agent 是**感知频次解耦**（高频控制/低频规划），非语义意图层
- 所有 VLA 在灵巧操作/精细控制上均表现一般，无一专门针对「层次化控制」设计

#### 论文构思方向（草案）

**方向X：双模块层次化空中操作 VLA 系统**

- **上层**：VLM（如 Qwen-VL / InternVL）做任务意图规划，输出结构化子目标（抓取点、放置位置、避障路径）
- **下层**：专用精细控制器，接收上层子目标 + 实时传感器反馈，输出高频精细动作
  - 方案A：ACT/action chunking 作为下层（小模型，本地可跑）
  - 方案B：Diffusion Policy 作为下层
  - 方案C：经典 PID-MPC 作为下层（已验证可靠）
- **空中特殊考量**：飞行稳定性约束 → 下层必须包含安全约束模块；高频振动 → 下层需要抗扰动设计

**为什么这是空白**：
1. 现有 VLA 均未在语义层解耦意图与执行
2. 空中精细操作的实时性+安全性要求使纯端到端路线风险过高
3. 双模块层次化架构在地面机械臂有基础（ACT），但未与 VLM 整合

**待验证**：
- [ ] 是否存在 VLM 上层 + 低层精细控制的先驱工作？
- [ ] 低层控制在主人无人机硬件上的可行性（计算资源、延迟要求）？
- [ ] FAAS 动作空间是否可用于无人机+机械爪场景？

### 2026-03-28 第13轮：OnFly 双 agent 架构 × Paper A 深化

**背景**：深化 OnFly 论文（arXiv 2603.10682），聚焦「双 agent 高低频解耦」和「语义-几何验证」两个核心设计，对 Paper A 三层架构的补充价值。

#### 核心发现

**发现1：OnFly 双 agent 架构验证了 Paper A 层次化解耦原则**

OnFly 的双 agent 本质：
- **高频 agent（Fast Agent）**：亚秒级视觉感知 + 实时飞控，响应 <100ms
- **低频 agent（Deliberative Agent）**：秒级 VL推理 + 语义规划 + 任务进度监控

这与 Paper A 的核心主张在架构哲学上一致：
```
Paper A 主张：
VLM意图层（秒级慢思考）→ 中层意图解析器 → 低层精细执行（毫秒级）

OnFly 实现：
低频VL agent（秒级规划）→ 高频飞控agent（亚秒级执行）

共同原则：慢思考语义层与快执行层解耦
```

**关键区别**：OnFly 是「感知频次解耦」，Paper A 是「语义意图层解耦」——OnFly 的低频 agent 仍在输出低层控制动作，而非语义级意图。Paper A 的创新在于把「意图语义层」显式建模出来。

**发现2：语义-几何验证 = Paper A 中层意图验证的雏形**

OnFly 的语义-几何验证策略：
- **语义验证**：VL agent 输出的决策是否符合任务目标语义（"是否朝正确方向飞"）
- **几何验证**：规划路径是否满足几何安全约束（障碍物、禁飞区）
- **滚动时域**：每 1-2 秒做一次全局验证，中间用局部规划填充

→ **Paper A 中层「意图解析器」的验证逻辑与此相同**：解析后的操作序列需同时满足语义正确性（是否符合VLM意图）+ 几何安全性（飞行/操作安全约束）

**发现3：OnFly 的「感知共享」机制可迁移到 Paper A**

OnFly 中高频 agent 共享低频 agent 的感知结果（节省重复感知计算）：
```
Paper A 可借鉴的感知共享架构：
VLM意图层（慢，共享视觉特征）→ 中层解析器（复用VL特征做意图验证）→ 低层执行（接收解析后的指令）
```

**对 Paper A 的新补充**：
- SafeFlow 的 CBF 安全校正（第1轮发现）可以作为 OnFly「几何验证层」的技术实现方案
- 两者结合：OnFly 的双 agent 频次解耦 + SafeFlow 的 CBF 安全约束 = Paper A 三层架构的完整技术路径

#### 待深挖问题（更新）
- [x] OnFly 双 agent 高低频解耦 → 已确认可迁移为 Paper A 架构原则
- [x] 语义-几何验证 → 已确认为 Paper A 中层验证的参考设计
- [ ] OnFly 的感知共享机制是否可以在 Paper A 中实现「VL特征复用」？需要主人确认硬件平台
- [ ] **新发现**：OnFly 真机验证（已在真实无人机上部署）说明「层次化解耦」路线在工程上完全可行

#### 研究结论
**Paper A 的技术路径已越来越清晰**：
1. 高层：VLM（Qwen-VL/InternVL）输出语义意图（秒级）
2. 中层：意图解析器（参考 OnFly 的语义-几何验证）做意图分解 + SafeFlow 的 CBF 做安全约束
3. 低层：ACT/Diffusion Policy 做精细动作执行（毫秒级）
4. **OnFly 已证明这类架构在真实无人机上可以工作** ✓

---

## 🆕 2026-03-28 第3轮：ST-VLA + Steerable VLA — 层次化VLA新证据

> 青狐深挖轮次 | 20分钟快速扫描

### Paper 1: ST-VLA — 3D-4D时空表示层次化VLA

- **arXiv**: 2603.13788
- **标题**: ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation
- **方向**: 方向1 (UniDex灵巧手VLA)
- **核心发现**: 现有hierarchical VLA框架用2D表示连接高层推理和低层控制，但缺乏深度感知和时间一致性。ST-VLA提出用统一的3D-4D表示（将2D guidance转换为3D轨迹+时空spatial masks）来桥接感知和动作。
- **为什么有价值**: 这是目前最接近Paper A「层次化VLA」构想的学术工作之一。3D-4D表示可以作为Paper A中层的"意图可视化/几何化"的技术实现。
- **可落地实验点**: 在Paper A中层引入ST-VLA的spatial mask机制，将VLM输出的语义意图转换为可执行3D轨迹片段，供低层控制器执行。「可落地实验点」
- **入库判断**: ✅ **入库**（新建 `2026-03-28_ST-VLA.md`）

### Paper 2: Steerable VLA — VLM-VLA接口瓶颈的显式解决

- **arXiv**: 2602.13193
- **标题**: Steerable Vision-Language-Action Policies for Embodied Reasoning and Hierarchical Control
- **方向**: 方向1 (UniDex灵巧手VLA)
- **核心发现**: 核心瓶颈是VLM和VLA之间的接口（通常用自然语言）限制了VLM推理对低层行为的控制力。Steerable Policies训练在多种抽象层次的合成命令上（子任务、运动、像素坐标）。通过改进低层可控性，可以解锁VLM中的预训练知识。
- **为什么有价值**: 直接回答了Paper A的核心问题："VLM意图层→低层控制"的接口应该如何设计？答案是：需要多层次抽象的可控接口，而非纯自然语言。
- **可落地实验点**: Paper A的中层「意图解析器」可以参考Steerable Policies的多层抽象设计（从语义子任务→几何运动→像素坐标），构建VLM意图到低层控制的分层映射。「可落地实验点」
- **入库判断**: ✅ **入库**（新建 `2026-03-28_Steerable-VLA.md`）

### 关键共识（两篇论文交叉验证）

两篇论文共同指向一个结论：

> **Paper A的「VLM意图层→中层意图解析器→低层执行」三层架构是正确的方向**，且：
> 1. 中层需要显式的「表示转换」（ST-VLA的3D-4D表示）
> 2. 中层需要多层次抽象接口（Steerable VLA的分层可控命令）
> 3. 现有VLA均未完整解决这两点 → 仍是研究空白

### 与主人研究的相关性
- 主人说「VLM给出模糊意图→其他模块优化为安全精细高频操作」= Paper A三层架构
- ST-VLA验证了「3D-4D表示」作为中层接口的可行性
- Steerable VLA验证了「多层次抽象」作为VLM-VLA接口的必要性

### 2026-04-10 R574：MMaDA-VLA + LaST0 + ManualVLA（统一生成低层候选 × 显式中间接口再确认）
- **MMaDA-VLA** (2603.25406)
  - **核心发现**: 用 native discrete diffusion 把语言、图像和连续控制统一进单一离散 token 空间，并并行生成 **future goal observation + action chunk**，说明生成式 VLA 正在往“动作器 + 未来观测条件化”一体化骨架收敛。
  - **为什么有价值**: 适合作为 Paper A 的低层执行器候选，因为它补强了复杂长时序动作的一致性；但它仍是端到端路线，没有替代 **显式语义接口 / latency-aware 中层 / 安全约束层**。
  - **可落地实验点**: 后续把它放进 ACT / Diffusion Policy / Xiaomi-Robotics-0 同一低层对照表，重点比较长动作一致性、部署延迟与 action chunk 稳定性。
  - **入库判断**: ✅ 继续保留为低层重点候选。
- **LaST0** (2601.05248)
  - **核心发现**: 用 latent spatio-temporal CoT + MoT 双专家，把 **低频 reasoning expert** 与 **高频 acting expert** 显式拆开，还通过 heterogeneous operation frequencies 解决部署时频率不一致问题。
  - **为什么有价值**: 它给 Paper A 的“慢语义层 + 快执行层”提供了更强正例，尤其说明 **latent reasoning** 比纯文本 CoT 更适合机器人时空控制。
  - **可落地实验点**: 主人的中层意图解析器后续可以尝试输出 latent trajectory / structural hints，而不只输出文本子任务。
  - **入库判断**: ✅ 高优先级支撑证据。
- **ManualVLA** (2512.02013)
  - **核心发现**: 先生成包含图像、位置提示、文本说明的 multimodal manual，再通过 ManualCoT 驱动 action expert 执行，等于把“中间手册/操作说明”作为显式控制条件。
  - **为什么有价值**: 它非常贴近 Paper A 的中层接口设想，证明“先把 what 变成 how 的可执行中间表示”是有效路线。
  - **可落地实验点**: 可把主人后续中层输出设计成 **waypoint + ROI + textual step** 的轻量 manual，而不是直接逼低层从语义跳动作。
  - **入库判断**: ✅ 继续作为中层接口核心参考。

### 2026-04-11 R616：LaST0 + SV-VLA（latent 中层接口 × 外置 verifier 壳层继续收束）
- **LaST0** (2601.05248)
  - **核心发现**: 通过 **latent spatio-temporal CoT** 建模未来视觉、3D 结构与 proprioceptive state，再用 **低频 reasoning expert + 高频 acting expert** 的 MoT 双专家协同执行，且训练时显式覆盖异频运行比。
  - **为什么有价值**: 它进一步证明主人要的不是 textual CoT，而是 **更物理化的中间表示 + 显式慢快分频**；尤其说明中层接口可以输出 latent hint，而不是只输出文字子任务。
  - **可落地实验点**: Paper A 的中层后续可尝试输出 `semantic intent + latent dynamics hint + latency metadata` 三元接口，并让低层显式接收 stale semantic state。
  - **入库判断**: ✅ 已完成深挖，转入 Paper A 高优先级支撑证据。
- **SV-VLA** (2604.02965)
  - **核心发现**: 采用 **重型 VLA 低频 macro-plan + 轻量 verifier 高频在线校验**，在 action chunk 开环执行期间持续根据最新观测判断当前计划是否失配，必要时再触发重规划。
  - **为什么有价值**: 这正好补强了 Paper A 里“强低层动作器外面再包一层轻校验壳”的工程路径，说明 chunked/open-loop 不一定只能硬吃 stale observation。
  - **可落地实验点**: 后续可把主人现有低层候选统一放进 `裸动作器` vs `动作器 + lightweight verifier` 对照表，重点看 unsafe-action pass-through rate、重规划频率和恢复能力。
  - **入库判断**: ✅ 新增重点候选，适合作为中层 verifier 直接参考。

### 2026-04-12 R632：ADV + VGAS（draft-and-verify × geometry-aware chunk critic）
- **ADV** (2603.18091)
  - **核心发现**: 用 diffusion 动作器先生成多个 candidate chunks，再让 VLM 用单次 forward 的 perplexity-style 评分做 rerank，形成 **Action-Draft-and-Verify** 闭环。
  - **为什么有价值**: 它把“强生成器 + 轻校验壳层”做成了更明确的工程结构，直接支持 Paper A 的 `动作器 + verifier` 路线，而不需要一开始就堆更重的统一模型。
  - **可落地实验点**: 把 MMaDA-VLA / ACT / Xiaomi-Robotics-0 这类低层候选统一接进 `裸动作器` vs `动作器+ADV式 verifier` 对照表，重点看 **unsafe-action pass-through rate、rerank overhead、恢复速度**。
  - **入库判断**: ✅ 新增 verifier 支撑证据，适合和 SV-VLA 并列参考。
- **VGAS** (2602.07399)
  - **核心发现**: 用 **best-of-N generation-selection + Q-Chunk-Former critic + Explicit Geometric Regularization** 处理 few-shot 适配里的几何歧义，专门拉开 near-miss 候选的 value ranking。
  - **为什么有价值**: 它说明中层/低层之间不一定只靠语义 verifier，还可以单列 **geometry-aware chunk critic**，专门筛掉“语义对但几何上会出事”的动作片段。
  - **可落地实验点**: Paper A 后续可增加一条 **near-miss 几何判别** 支线，重点比较 `语义 verifier`、`几何 critic`、`双层校验` 三档对复杂操作失败率的影响。
  - **入库判断**: ✅ 新增 geometry-aware verifier 证据。

### 2026-04-10 R584：MMaDA-VLA 摘要级补记（低层 diffusion 执行器定位继续收束）
- **MMaDA-VLA** (2603.25406)
  - **核心发现**: 用 native discrete diffusion 把语言、图像和连续控制统一进单一离散 token 空间，并并行生成 **future goal observation + action chunk**，强化长时序动作的一致性。
  - **为什么有价值**: 它更适合作为 Paper A 的 **低层 diffusion 执行器候选**，因为能把视觉前瞻直接绑定到动作生成；但它仍没有替代 **显式语义接口 / latency-aware 中层 / 安全约束层**。
  - **可落地实验点**: 后续和 ACT / Diffusion Policy / Xiaomi-Robotics-0 放进同一低层对照表，重点比较 **长动作一致性、部署延迟、chunk 稳定性**。
  - **入库判断**: ✅ 已补摘要级速记，待全文 method 复核。

### 2026-04-09 R542：Realtime-VLA V2 + TIC-VLA（部署链路与延迟建模补强）
- **Realtime-VLA V2** (2603.26360)
  - **核心发现**: 不再只优化 GPU 上的单次 VLA 推理，而是把真实部署里的校准、规划控制、轨迹连续执行一起纳入优化目标，强调 fast + smooth + accurate 三指标并重。
  - **为什么有价值**: 这说明主人后续空中 VLA 评估不能只看成功率和平均延迟，还要把 **轨迹平滑度 / control jitter / chunk stitching stability** 当成一等公民。
  - **可落地实验点**: 在 AirSim 给现有原型补上轨迹平滑度、姿态抖动率、chunk 拼接误差三个指标，先把“能跑”升级成“跑得稳”。
  - **入库判断**: ✅ 已深挖速记，建议作为 Paper A 的低层执行验收参考。
- **TIC-VLA** (2602.02459)
  - **核心发现**: 提出 latency-aware 的 Think-in-Control 框架，用 delayed semantic-control interface 显式建模“慢语义推理”和“快实时控制”之间的时间错位。
  - **为什么有价值**: 它几乎正面回答了主人 Paper A 里的关键矛盾，说明高层语义不是不能慢，而是必须把延迟显式暴露给控制层。
  - **可落地实验点**: 给主人后续中层意图解析器补一个 latency token / stale semantic state 输入，验证高延迟下是否更稳。
  - **入库判断**: 🆕 候选，值得后续补读 method 细节。

### 2026-04-09 R537：Xiaomi-Robotics-0 + DAM-VLA（实时VLA路线补强）
- **Xiaomi-Robotics-0** (2602.12684)
  - **核心发现**: 从大规模跨载体轨迹 + 视觉语言数据预训练，再通过异步执行训练和 action chunk 对齐策略，解决真机 rollout 的推理延迟问题；可在消费级 GPU 上实现平滑实时执行。
  - **为什么有价值**: 这不是单纯追求大模型效果，而是把**实时部署**当成一等公民，正好击中主人空中 VLA 的延迟瓶颈。
  - **可落地实验点**: 以 π₀.₅/OpenVLA 为基座，单独复现实机异步执行 + action chunk 对齐，先验证延迟改善，再考虑接入空中平台。
  - **入库判断**: ✅ 已转正，建议作为 Paper A 的工程基座候选。
- **DAM-VLA** (2603.00926)
  - **核心发现**: 用任务相关视觉/语言线索做 action routing，把机械臂运动和夹爪操作分给不同 diffusion action model，再用 dual-scale weighting 动态融合。
  - **为什么有价值**: 它证明了**按动作子空间拆头**是有效路线，和主人设想的“高层意图→中层解析→低层专控”非常贴。
  - **可落地实验点**: 空中操作可改写为“飞行姿态/轨迹头 + 末端执行器头”双分支，避免单一动作头同时背负飞行与操作两种动力学。
  - **入库判断**: ✅ 候选转重点关注。

### 2026-04-06 R498：新候选 — Xiaomi-Robotics-0（小米开源VLA）
- **arXiv**: 2602.12684
- **标题**: Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model
- **方向**: 方向2 (空中VLA)
- **核心发现**: 小米开源端到端 VLA，输入观测图像+语言指令+机器人本体状态，输出连续动作；基于标准 VLA 架构，强调开源可复现性。
- **为什么有价值**: 这是目前少有的国内团队开源 VLA，具体架构和性能数据需补读确认；可能与主人现有的 π₀.₅/OpenVLA 基座形成互补或竞争对比。
- **可落地实验点**: 补读摘要后评估是否可作为 Paper A 的候选基座之一，与 π₀.₅/OpenVLA 做架构对比。「待评估」
- **入库判断**: 候选待确认（HALO/GeneralVLA 同样待确认，建议合并评估）

### 2026-04-05 R443：新方向 — UAV-Track VLA（空中追踪VLA）
- **arXiv**: 2604.02241
- **标题**: UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models
- **方向**: 方向2 (空中VLA)
- **核心发现**: 基于 π₀.₅ 架构的空中追踪VLA，专为无人机视觉追踪任务设计。提出 temporal compression net 解决帧间冗余 + parallel dual-branch decoder（含 spatial-aware grounding head + flow matching action expert）解耦跨模态特征，直接生成细粒度连续动作。在 CARLA 模拟器中，追踪成功率达 61.76%，单步推理延迟降至 0.0571s（比 π₀.₅ 快 33.4%）。
- **为什么有价值**: 这是目前最接近主人「空中VLA动作生成」主线的具体实现。π₀.₅ 架构本身值得参考，而 temporal compression + dual-branch decoder 思路可以直接迁移到空中操作的 VLA 微调 Pipeline。对主人最有价值的点：它展示了「架构改进（π₀.₅基座）+ 时序建模（compression net）+ 多分支解码（spatial+action 解耦）」三合一优化路线，是可以借鉴的空中 VLA 调优范式。
- **可落地实验点**: 以 π₀.₅ 或 OpenVLA 为基座，引入 temporal compression net 解决视频序列冗余，参考 dual-branch decoder 思路设计空中操作的动作生成分支。「可落地实验点」
- **入库判断**: ✅ **入库**（新建 `2026-04-05_UAV-Track-VLA.md`）

### 2026-04-08 R527：**E-VLA — Event-Augmented VLA for Dark and Blurred Scenes** (2604.04834) 【新增入库】

**核心贡献**：解决传统VLA在极端视觉条件（低光/运动模糊/过曝）下完全失效的问题。提出E-VLA，将事件相机流直接注入VLA（而非先重建图像），在D435i等深度相机失效的低光条件下从0%→90%成功率提升。

**对主人的价值**：
1. **龙虾项目直接相关**：实机测试中D435i在动态飞行/低光条件下RGB通道易失效，E-VLA的事件流注入路线可作为感知增强模块直接叠加，无需重新训练VLA
2. **零训练成本集成**：E-VLA不需要对现有VLA做架构修改或重训练，只需要在输入层融合事件流，可即插即用
3. **极端条件保障**：龙虾项目目标4/10 DDL，实机测试时如果遇到低光/运动模糊，E-VLA路线提供了可靠的备用感知方案

**可落地实验点**：在龙虾VLA pipeline的输入端叠加事件相机数据流，验证在低光/动态飞行条件下的感知鲁棒性提升

**归档**：方向 02，已正式入库

### 2026-04-09 R537：阶段结论
- **实时 VLA 两条可用路线已更清楚**：
  1. **工程路线**：Xiaomi-Robotics-0 的异步执行 + action chunk 对齐，优先解决推理时延；
  2. **结构路线**：DAM-VLA 的动作路由 + 双尺度融合，优先解决不同子动作的建模冲突。
- **对 Paper A 的启发**：主人不必一开始就做完整三层巨系统，可以先做“VLM意图层 + 双头低层控制器”的轻量版原型，把飞行控制和末端操作拆开验证。

### 2026-04-09 R548：LaMP 新候选（3D scene flow 作为低层运动先验）
- **arXiv**: 2603.25399
- **标题**: LaMP: Learning Vision-Language-Action Policies with 3D Scene Flow as Motion Priors
- **核心发现**: 把 dense 3D scene flow 显式注入 VLA，不再让模型只靠 2D 语义特征硬学空间动力学，属于“给低层执行器补几何运动先验”的路线。
- **为什么有价值**: 这条线和主人 Paper A 很贴，因为它说明中低层之间不一定只能传自然语言或 action token，还可以传更几何化的运动表征，尤其适合空中平台这种动态更强的场景。
- **可落地实验点**: 后续可尝试把主人中层意图解析器输出改成 waypoint / flow hint / 局部速度场，而不是只给低层一个抽象文本子任务。
- **入库判断**: 🆕 候选，建议后续与 ST-VLA、TIC-VLA 一起补读 method。

### 2026-04-10 R570：MMaDA-VLA 摘要级入库（统一多模态理解+生成的 diffusion VLA）
- **arXiv**: 2603.25406
- **标题**: MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation
- **核心发现**: 从可访问摘要与项目页片段看，MMaDA-VLA 主打 **fully native pre-trained large diffusion VLA**，尝试把多模态理解与生成统一到同一框架里，说明 diffusion VLA 正在从“单纯动作生成器”往更统一的条件生成骨架收敛。
- **为什么有价值**: 它适合作为 Paper A 的低层执行器候选参考，因为统一生成式骨架可能提升复杂动作序列建模能力；但它仍属于原生端到端 VLA 路线，没有直接回答主人最关心的 **高层语义意图接口 / 延迟补偿 / 安全约束显式建模**。
- **可落地实验点**: 后续可把 MMaDA-VLA 放进低层候选对照，与 ACT / Diffusion Policy / Xiaomi-Robotics-0 异步执行路线并列，重点比较复杂动作表达能力与实时部署代价。
- **入库判断**: ✅ 摘要级入库，已新建速记，后续值得补读 method 与部署细节。
