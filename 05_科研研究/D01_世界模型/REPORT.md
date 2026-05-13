# D01: 世界模型 研究报告

> 最后更新:2026-04-18 | 成熟度:🟡中期（R806补入部署前“已知失败 vs 异常”分诊协议，继续把 D01 从世界模型能力讨论压到可执行验收栈）
> 状态：🟡 推进中

## 一、研究背景与动机

现有 VLA 方法(OpenVLA/π0/GR00T)采用端到端架构,VLM 直接输出动作 token。但在空中操作等精细任务中,这种架构面临三大瓶颈:(1) VLM forward 延迟(200-2000ms)无法满足毫秒级控制需求;(2) 纯视觉预测缺乏物理一致性;(3) 缺乏对接触力/物理属性的建模。世界模型通过学习环境动力学,可以在 latent space 进行想象、规划和策略优化,是解决上述瓶颈的关键技术。

## 二、相关工作梳理

### 2.1 隐式 Latent 世界模型
- **DIAL** - Intent bottleneck 显式分离意图与动作,latent world model 预测未来状态
- **LatentPilot** - Latent space 规划,避免像素级预测的计算开销
- **Persistent Robot WM** - RL 后训练稳住 AR rollout 质量

### 2.2 动作感知世界模型
- **WAM** (2603.28955) - DreamerV2 + inverse dynamics loss,action-aware latent 表示,CALVIN 92.8%
- **Fast-WAM** - 测试时是否需要想象?(效率 vs 质量权衡)

### 2.3 多模态世界模型
- **OmniVTA** (2603.19201) - Visuo-tactile 世界模型,21K 轨迹,触觉信号建模接触动力学
- **CMLF** (2604.02108) - 贝叶斯主动推理估计物理属性(惯性/刚度/摩擦),vision↔touch 双向迁移

### 2.4 组合式/分层世界模型
- **RISE** (2602.11075) - Compositional WM(动力学模型+进展价值模型)+ 想象式自我改进,+35%~45% 真机提升
- **Hierarchical Planning** (2604.03208) - 多时序尺度分层规划,pick-place 70% vs 单层 0%

### 2.5 显式物理世界模型
- **Explicit WM + Digital Twin** (2603.13825) - 数字孪生重建 + 仿真探索策略 → zero-shot 部署

### 2.6 Physics-aligned 世界模型
- **ABot-PhysWorld** (2603.23376) - 用 physics-aware annotation + DPO 后训练抑制穿模/反重力等不合理操作,并提出 EZSbench,将评测拆成 physical realism 与 action alignment 两条轴

### 2.7 世界模型作为训练器 / 评测器 / 交互模拟器
- **World-Gymnast** (2602.02454) - 把动作条件视频世界模型直接当作 RL 训练环境,用 VLM 奖励 imagined rollout,对真机任务带来显著提升
- **WoVR** (2602.13977) - 针对 imagined rollout hallucination 问题,引入 keyframe-initialized rollouts 与 world-model-policy co-evolution,提升 world-model RL 的可靠性
- **Evaluating Robot Policies in a World Model / WorldGym** (2506.00613) - 说明 world model 做 policy evaluation 时,虽然会低估 in-distribution、高估 out-of-distribution 的绝对值,但仍能较好保留策略相对排序,适合作为部署前筛选层
- **Interactive World Simulator** (2603.08546) - 把 action-conditioned video world model 往可交互模拟器推进,强调长时稳定交互、world-model-generated data usefulness,以及 simulated-real performance correlation
- **Causal World Modeling for Robot Control / LingBot-VA** (2601.21998) - 用 shared vision-action latent + 闭环 rollout 持续读回真实观测 + 异步推理并行动作预测与执行,提醒 D01 后续应把 **feedback reacquisition** 与 **asynchronous inference latency hiding** 单列成部署导向验收位,而不是只看离线 rollout 质量
- **WorldEval** (2505.19017) - 把 world model 明确拉成部署前 **policy evaluator + danger-action filter**,并强调需要先把 policy/action 映射到更适合视频世界模型跟随的 **latent action interface(如 Policy2Vec)**,提醒后续必须单独验收 ranking correlation、OOD 动作高估风险、安全预筛能力,以及 **原始动作输入 vs latent action adapter** 的接口差异
- **WAV / World Action Verifier** (2604.01985) - 把 action-conditioned prediction 显式拆成 **state plausibility + action reachability** 两个更易验证的子问题,并利用 **action-free video + sparse inverse model + cycle consistency** 做自校验,在 9 个任务上实现 **2x 样本效率** 与 **18% 下游策略提升**。它直接强化了 D01 里 verifier / self-check 这条支线,说明 deployment 前不能只看 rollout reward,还要单列 reachability 验证层
- **OpenWorldLib** (2604.04707) - 给 advanced world model 提供统一定义与推理框架,提醒后续应把"能力清单/统一接口"与"真实任务效用"分开验收,避免把框架完备性误当成下游有效性
- **Event-Centric World Modeling with Memory-Augmented Retrieval** (2604.07392) - 不走纯 rollout 生成,而是把环境压成 **semantic events**,再从历史经验库里检索对应 maneuver,并用 physics-informed retrieval 保证机动选择与动力学一致。它更像可解释的 **retrieval planner / experience bank**,对 UAV 场景尤其贴近,但当前更适合作为 D01 的 planner 外围增强,而不是替代 verifier/evaluator 主线
- **Grounded World Model for Semantically Generalizable Planning** (2604.11751) - 用 training-free、embodiment-agnostic 的 rendering-based action encoder 把动作/状态接口做成跨载体统一 tokenizer,并在新载体 xArm6 上给出 zero-shot 泛化。它直接强化了 D01 的 **policy-to-latent action interface** 主线,说明接口层不一定要靠 learnable encoder 才能泛化。
- **GigaWorld-Policy** (2603.17240) - 强调 **action-centered world-action model** 不只是做视频预测器,而是直接把世界模型压成可服务策略学习、测试时规划与闭环执行的动作中心骨架。它对 D01 的提醒很直接:后续基线不该只放 `video-WM / geometry-WM / evaluator-WM`,还应单列一类 **action-centered WAM baseline**，专门比较“世界模型是否真的服务动作决策”而不只是生成看起来更真的未来。
- **PlayWorld** (2603.09030) - 用 **autonomous play + overnight unattended collection** 训练 action-conditioned video WM,证明 interaction-rich play data 不只是“多一点数据”,而是能显著提升 **contact-rich dynamics fidelity / failure prediction / fine-grained policy evaluation**,并支持 world-model RL fine-tuning 在真机上带来 **最高 65% 成功率提升**。它直接提醒 D01:世界模型上限未必先卡在骨架,更可能先卡在 **交互覆盖度与数据来源结构**。
- **Dream2Fix** (2603.13528) - 不再把 world model 只当 evaluator 或 trainer,而是直接在生成式 world model 里对成功演示做动作扰动,合成 **counterfactual failure rollouts**，再经任务有效性、视觉连贯性与运动学安全三重校验,产出可用于学习“失败类型 → 恢复轨迹”的高价值配对数据。它对 D01 的关键提醒是: `known failure triage` 之后不该只停在回退或人工接管,还应显式比较 **triage-only** 与 **triage+actionable recovery synthesis** 的增益。

### 2.8 共同缺陷 / Gap
1. 隐式 WM(DIAL/WAM)缺乏物理一致性保证
2. 多模态 WM(OmniVTA)数据采集成本高
3. **无一专门针对空中操作场景设计**--飞行动力学+操作动力学的双重约束未被建模
4. 想象式训练(RISE)在高维+长时序场景的稳定性未验证
5. **评测与真实功能脱节**--WorldArena 表明高视频质量与高任务效用并不强相关,单看生成指标容易误判路线价值
6. **缺少"动作对齐"和"物理可执行"解耦验收**--ABot-PhysWorld 证明只看视频观感不够,必须把物理合理性单独验收
7. **世界模型做 RL 训练器时仍有 hallucination 污染风险**--World-Gymnast 证明路线有效,但 WoVR 进一步提醒 imagined rollout 的可靠深度必须被显式约束
8. **缺少对欠覆盖动作区间的可达性自校验**--WAV 说明 under-explored / suboptimal actions 才是部署前最危险的盲区,仅靠 forward rollout 很容易误判,需要单列 inverse-check / reachability verifier
9. **动作接口泛化仍薄弱**--Grounded World Model 表明 training-free rendering-based action encoder 就可能显著提升跨载体泛化,说明当前 D01 若继续把接口层绑死在特定 embodiment 的 learnable action encoder 上,后续很容易在新平台上重训成本过高
10. **数据覆盖结构经常被低估**--PlayWorld 说明 contact-rich world model 的瓶颈不一定先是主干建模能力,而常常先是 **autonomous play / failure-heavy interaction coverage** 是否足够；若数据仍以 success-biased demo 为主,评测相关性和 imagined RL 收益都可能被提前卡死
11. **部署前缺少“已知失败 vs 未知异常”分诊层**--现有 D01 验收大多只问策略该不该放行,却很少进一步区分“这是可预期、可命名、可修复的已知失败”,还是“超出训练覆盖、需要升级人工接管级别的异常”。若不把两者拆开,world model evaluator 很容易把低置信度异常误当成普通失败继续自动执行,或把可修复已知失败过度升级成全面停机
12. **已知失败后的恢复 supervision 仍薄弱**--即使完成 F1/F2 分诊,系统通常也只会 `stop / retry / fallback`，缺少从失败视觉状态直接映射到 **可执行修正轨迹** 的数据与训练协议。Dream2Fix 说明这类 supervision 可以通过 world-model-based counterfactual synthesis 低成本补齐,否则 D01 很容易停在“会拦不会救”。

## 三、我们的创新方向

### 3.1 核心创新点

1. **C1: 飞行-操作双动力学世界模型** - 在 latent space 同时建模飞行平台动力学和操作末端动力学,支持空中操作规划
2. **C2: 组合式 WM + 安全层** - RISE 风格双分支(动力学+价值)+ SafeFlow CBF 安全约束,保证空中操作安全
3. **C3: 触觉增强 latent 表示** - 在 DIAL/WAM 的 latent state 中融入触觉/力觉信号,提升接触丰富任务预测精度
4. **C4: Physics alignment 后训练层** - 在 WM 主训练完成后增加"物理偏好校正"阶段,专门压制穿模、反重力、越界等不合理行为
5. **C5: 解耦验收协议** - 借鉴 WorldArena + EZSbench,把世界模型输出拆成"任务效用 / 动作对齐 / 物理一致性 / 安全约束"四类指标统一验收
6. **C6: 语义接地动作接口** - 在 policy-to-latent interface 层尝试 embodiment-agnostic 的 rendering-based action encoding,优先把语义接地与跨载体泛化前移到接口层,而不是把泛化压力全部留给世界模型主干
7. **C7: 几何接地动作状态主干** - 不再默认世界模型必须联合预测 2D 视频,而是显式比较 `action+video` 与 `action+3D geometry` 两类主干,验证几何先验是否更适合承载接触一致性、跨视角稳定性与可达性判断

### 3.2 两阶段后训练路线(新增)
结合 **EVA (2603.17808)** 最新发现,D01 的 C4 Physics alignment 后训练可升级为两阶段路线:
1. **第一阶段:Physics Alignment**(ABot-PhysWorld路线)-- physics-aware annotation + DPO 后训练,显式压制穿模/反重力/越界等物理不合理行为,输出物理合理但动作未必可达的 rollout
2. **第二阶段:Executability Alignment**(EVA路线)-- 用真实机器人轨迹训练 IDM,再用 IDM 作为 reward 模型评估第一阶段生成的视频,鼓励平滑运动(速度/加速度/jerk约束),惩罚违反 embodiment 约束的动作
3. **关键价值**:两阶段分离比单阶段更清晰--第一阶段解决"看起来物理真",第二阶段解决"做出来可执行"。在 RoboTwin 和真实双手机器人上验证,下游任务成功率显著提升。
4. **对空中操作的特殊意义**:无人机高速运动下,动作可达性和动力学约束比地面机器人更严苛,EVA 的 IDM reward 还能自然引入速度/加速度/jerk 平滑约束,直接对应飞行控制的平滑轨迹需求。

### 3.3 C6 接口层设计草案（R785 新增）

> 目标：不再把 `policy-to-latent action interface` 只写成一句口号，而是把它压成可直接验收的接口层方案。

| 接口路线 | 代表思路 | 优点 | 风险 | D01 中的定位 |
|---|---|---|---|---|
| **A. Learnable action encoder** | DIAL / 常规 latent adapter | 易和现有 WM 主干联合训练 | 强依赖 embodiment，换载体常要重训 | 作为基础基线 |
| **B. Rendering-based tokenizer** | Grounded World Model | training-free、语义接地、跨载体零样本潜力强 | 可能受视觉基础模型上限约束 | 作为 C6 主实验轴 |
| **C. Interface + verifier 联合** | B + WAV/self-check | 同时比较“能否表达”与“是否可达” | 误杀率可能升高 | 作为部署前安全接口 |

**当前判断**：D01 不该默认接口层只是“把动作塞进 world model”的前处理，而应把它当成单独方法位。因为一旦接口层本身就具备语义接地和跨载体泛化，后面的主干世界模型就不必承担全部迁移压力。

### 3.4 C7 几何接地主干假设（R788 新增）

> 目标：把 `video-WM` 与 `geometry-grounded WM` 的分歧从抽象争论压成可证伪实验。

- **假设 H1**：对 manipulation 尤其是 contact-rich 场景，`joint action + 3D geometry prediction` 比 `joint action + 2D video prediction` 更能保留结构约束，因此更适合作为动作可达性和接触一致性的底座。
- **假设 H2**：video-WM 仍更适合承担长时时序与语义外观预测，但 geometry-WM 更可能在 **cross-view consistency / contact plausibility / pose-sensitive planning** 上占优。
- **系统定位**：C7 不替代 C6。更合理的组合是 **C6 负责接口层语义接地，C7 负责主干层几何接地**，两者共同减轻世界模型对纯 2D 像素时序的依赖。

### 3.5 与论文 A(层次化空中 VLA)的关系
世界模型作为论文 A 中层意图解析器的核心组件:VLM 输出语义意图 → 世界模型在 latent space 规划安全可行轨迹 → 低层控制器执行

## 四、实验设计(待主人确认后细化)

### 4.1 验证路线
1. DIAL/WAM baseline → 加入飞行动力学约束 → 空中操作仿真验证
2. RISE 想象式训练 → 空中抓取任务 → 真机对比
3. 触觉融合 ablation → 有/无触觉信号的 latent WM 预测精度
4. 参照 WorldArena 增加**功能性验收**:
   - 生成数据是否提升下游策略成功率
   - 世界模型评估结果与仿真/真机结果相关性
   - 世界模型闭环规划能否完成任务
5. 参照 ABot-PhysWorld 增加**物理一致性验收**:
   - 是否出现穿模、反重力、非因果接触
   - 动作条件与视频轨迹是否一致
   - 安全约束(禁飞区/碰撞/关节极限)是否被满足
6. 增加**评测相关性验收**:
   - world model 内 policy evaluation 与仿真/真机结果的相关性
   - strategy ranking 是否在 WM / AirSim / 真机之间保持一致
   - interactive simulator fidelity 是否足够支撑策略筛选
   - world-model-generated data 是否真能提升下游策略
   - **将 simulator fidelity / ranking correlation / generated-data usefulness 拆成三张独立验收表**,避免把"有用"混成单指标
   - imagined rollout 的有效深度与关键帧回锚收益
   - danger-action filter 是否能在进入 AirSim / 真机前稳定拦截高风险策略
   - **policy-to-latent action adapter** 是否明显优于直接输入原始动作,尤其在 action-following fidelity、危险动作预筛和 OOD 高估抑制上
   - **training-free rendering-based action encoder** 是否能在新载体上保留 ranking correlation 与 safety filtering 能力,并显著降低接口重训成本
   - **geometry-grounded backbone** 是否能在 cross-view consistency、contact plausibility、pose-sensitive planning 上优于 video-WM,同时不显著损伤长时 rollout 价值
   - **reachability verifier / sparse inverse check** 接入后,是否能显著降低 under-explored 动作区间的高估与错误排序
   - **closed-loop feedback reacquisition** 是否明显提升长时序回稳与重规划后再收敛
   - **asynchronous inference latency hiding** 是否真的换来可用墙钟时延,而不只是把延迟转移到控制链其他位置

#### 4.1+ 任务阶梯与数据集选择（R790 推进）

| 阶段 | 任务族 | 推荐环境/数据 | 目标 | 为什么先做它 |
|---|---|---|---|---|
| **S1 短程语义导航** | 语言到局部目标点/视角调整 | AirSim / Unreal Robotics Lab / 自建室内航点场景 | 验证 `policy ranking correlation` 与 `danger-action filter` | 先把长程导航和接触误差拆开 |
| **S2 接近-对位** | UAV 末端接近物体、稳定悬停、预抓取位姿对齐 | AirSim + 简化机械臂末端，或固定底座末端替代实验 | 验证 `geometry-grounded backbone` 与 `executability alignment` | 直接测可达性与位姿一致性 |
| **S3 短程接触操作** | 按钮按压 / 轻触 / 抓取前接触 | UE5/Isaac Sim 接触丰富场景 + 触觉/力信号可选 | 验证 `physics alignment + tactile fusion` | 这里最容易暴露穿模、反重力、非法接触 |
| **S4 空中抓取闭环** | 导航→接近→抓取→退出 | AirSim/UE5 联合场景，后续接龙虾平台 | 评估 D01 作为 trainer/planner/evaluator 的完整价值 | 只在前 3 阶段过门槛后再上，避免一次把误差混在一起 |

**数据优先级**：先用 `仿真可控任务 + 少量真实回放片段` 建最小闭环，再补 `真实 UAV 视频/轨迹`。对 D01 来说，首轮最值钱的不是大数据量，而是能同时覆盖 **安全约束、动作可达性、几何位姿误差** 的可诊断任务。

#### 4.1++ baseline 家族与对照位（R790 推进）

| baseline 家族 | 代表方法 | 在 D01 中承担的对照角色 |
|---|---|---|
| **Planner-first** | Hierarchical Planning / VISTA-WM | 对照“世界模型做高层规划器”是否真比纯策略更稳 |
| **Trainer-first** | World-Gymnast / WoVR / RISE | 对照 imagined rollout 能否带来稳定策略增益 |
| **Evaluator-first** | WorldEval / Interactive World Simulator / Ctrl-World | 对照 ranking correlation 与危险动作预筛 |
| **Verifier-first** | WAV / inverse-check | 对照 self-check 是否真能降低 under-explored 动作高估 |
| **Interface-first** | Grounded WM / Policy2Vec-style adapter | 对照动作接口设计本身是否决定跨载体与排序稳定性 |
| **Geometry-first** | f(v)→G / Mirage2Matter | 对照几何接地主干是否比 video-WM 更适合接触与位姿任务 |

**建议首轮 baseline 组合**：`WorldEval/Interactive WM + WAV + Grounded WM tokenizer`。这一组最贴近主人当前需求，因为它能先回答“能不能在不上真机前筛掉危险策略”，而不是一开始就追求最强 end-to-end 成功率。

#### 4.1+++ 数据来源 sanity 轴（R802 新增）

> 目的：先确认 D01 的收益到底来自“骨架更强”，还是其实主要来自 **interaction-rich data**。

| 数据设置 | 代表来源 | 主要回答的问题 | 关键指标 |
|---|---|---|---|
| **D0 success-biased demos** | 常规人类示教 / 成功轨迹 | 只靠干净 demo，world model 能学到多少可达性与接触动力学 | contact plausibility、ranking correlation |
| **D1 demo + autonomous play** | PlayWorld-style unattended play | 增加失败与边界交互后，评测与 imagined RL 是否显著变稳 | failure prediction、OOD 动作过滤、下游成功率 |
| **D2 demo + play + 少量真实回放** | 仿真/真机混合 | 对空中平台而言，少量真实回放是否足以校正动力学与安全门 | danger-action 漏放率、短程回稳 |

**建议用法**：所有 Tier-1/Tier-2 baseline 至少都在 `D0 vs D1` 上跑一次。若 D1 带来的增益大于主干差异，就说明 D01 下一阶段应优先补 **交互数据飞轮**，而不是继续扩 backbone。

#### 4.1++++ 已知失败 vs 异常分诊协议（R806 新增）

> 来自 **World Model Failure Classification and Anomaly Detection for Autonomous Inspection** (2602.16182) 的直接启发。D01 后续不该只输出一个“放行/拦截”分数，还应把失败进一步拆成 **已知失败** 与 **未知异常**，决定是自动修补、回退策略，还是立刻升级人工接管。

| 分诊层 | 定义 | 典型来源 | 推荐处置 | 关键指标 |
|---|---|---|---|---|
| **F1 已知失败** | 模型见过或可命名的失败模式，能归到稳定类别 | 目标误读、抓取位姿偏移、局部碰撞、短程重规划失败 | 允许自动 recovery / fallback policy / 重试 | failure classification accuracy、已知失败恢复成功率 |
| **F2 未知异常** | 明显超出训练分布，world model 自己也不该自信解释 | 新障碍、极端视角、异常光照、传感器失真、动力学失配 | 直接升级 human review / hard stop / 更保守策略 | anomaly recall、OOD 漏放率、异常升级时延 |
| **F3 误判成本层** | 把 F1/F2 混错后的系统代价 | 把异常当已知失败继续执行，或把可恢复失败误升级停机 | 单独统计风险成本，不与成功率混算 | risk-weighted false accept / false escalate |

**使用规则**：
1. **Tier-1 安全预筛之后，必须立刻接 F1/F2 分诊**，不能只做“危险动作是否拦截”。
2. evaluator/verifier 的输出至少包含三项：`pass score`、`known-failure class`、`anomaly score`。
3. 对主人当前空中平台，`动力学失配 / 视觉失锁 / 新障碍物` 优先归入 F2，不让系统在高风险场景里假装“只是普通失败”。
4. 后续若 D01 要服务 D06/D07，优先比较 **有无异常分诊层** 对 `危险动作漏放率、误升级率、人工接管频率` 的影响。

#### 4.1+++++ 已知失败恢复闭环（R809 新增）

> 受 **Dream2Fix: Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis** (2603.13528) 启发。D01 不该把 F1 已知失败只处理成“允许重试”这种粗粒度回退，而应继续比较系统有没有能力从失败状态直接生成 **可执行修正动作/轨迹**。

| 恢复层 | 定义 | 数据来源 | 推荐处置 | 关键指标 |
|---|---|---|---|---|
| **R1 规则回退** | 固定 retry / backoff / return-to-safe-pose | 人工规则、控制器先验 | 成本最低，作为最低保底层 | 恢复成功率、额外耗时 |
| **R2 检索式恢复** | 按失败类型检索相似历史 case 或 maneuver | 历史失败库、经验回放 | 适合高频已知失败 | case hit rate、恢复时延 |
| **R3 反事实恢复合成** | 用生成式 WM 扰动成功轨迹，合成 failure→correction 配对样本后训练恢复器 | Dream2Fix-style counterfactual synthesis | 直接输出修正轨迹，最贴近 D01 主线 | correction accuracy、闭环恢复率、运动学违规率 |

**当前判断**：
1. D01 的 `F1 known-failure` 不应默认终点是 `retry/fallback`，而应把 **R3 反事实恢复器** 正式列成候选方法位。
2. 对空中平台最现实的做法不是先采大量真实故障，而是先从成功轨迹 + world model rollout 里合成 `接近位姿偏移 / 局部碰撞 / 抓取落空 / 退出路径错误` 等已知失败样本。
3. 只有当 `triage + recovery` 明显优于 `triage-only`，D01 才算真正具备“会拦也会救”的部署前价值。

#### 4.1++++++ 分诊-恢复统一记账协议（R829 新增）

> 来自本轮对 **Dream2Fix** 与现有 `F1/F2 + P6` 主线的本地复核。D01 现在不该只继续追“恢复成功率有没有提升”，而要正式回答：**这条 recovery 线值不值得上线、值不值得占论文主表位置**。因此需要把恢复收益、异常漏放、人工负担和恢复债务统一记账，避免系统用更激进的恢复把风险偷偷转嫁掉。

| 指标 | 含义 | 为什么单列 |
|---|---|---|
| **SRY** (Safe Recovery Yield) | 在不触发新增安全违规前提下，恢复链真正带回的有效成功增益 | 防止把“勉强继续执行”误算成恢复收益 |
| **AER** (Anomaly Escape Rate) | 未知异常被误送进 recovery 或继续执行的比例 | Dream2Fix 线最危险的代价不是恢复失败，而是把异常硬救下去 |
| **HHB** (Human Handoff Burden) | 每 100 次任务需要的人工确认/接管次数与平均介入时长 | 防止系统把复杂度转嫁给主人或操作员 |
| **RDR** (Recovery Debt Ratio) | 恢复后新增的额外路径、时延、能耗或二次修复成本 | 恢复成功但代价过高时，不该和直接成功等价计分 |
| **RCS** (Recovery Calibration Score) | 恢复器置信度与真实恢复成功率的一致性 | 决定 recovery 能否升到在线闭环，而不只是离线建议 |

**统一记账规则**：
1. 所有 `R1/R2/R3` 恢复实验，默认都要同时报 `SRY/AER/HHB/RDR/RCS`，不再接受只报 recovery success rate。
2. 若某方法仅提升 `SRY`，但显著恶化 `AER` 或 `HHB`，则默认降级为候选，不升主线。
3. `R3 Dream2Fix-style recovery` 只有在 `SRY` 提升且 `RCS` 可校准时，才允许进入在线 gated recovery 讨论。
4. 对 D01 而言，`RDR` 高于规则回退过多时，应优先把 recovery 写成 **offline recommendation / hover-bounded recovery**，而不是通用在线恢复器。

#### 4.1+++++++ 首轮读数判定表（R829 新增）

> 目的：把 D01 的恢复线从“概念上可行”继续压成 **12h 级首轮实验一出来就知道该收缩、转向还是暂停** 的判线表，避免反复加模块却没有 go/no-go 依据。

| 观察信号 | 若出现该结果，优先判断 | 推荐动作 |
|---|---|---|
| `B1/B2` 相比 `B0` 几乎不降 danger-action 漏放率 | evaluator / WAV / triage 还没站住，recovery 讨论过早 | 回退到接口层与 verifier，自停 R3 线 |
| `SRY` 提升但 `AER` 同时上升明显 | recovery 只是把异常硬往下执行 | 保留离线建议位，不进在线闭环 |
| `SRY` 与 `AER` 都改善，但 `HHB` 明显升高 | 系统在把复杂度转移给人工 | 缩回 hover-bounded 或 recommendation-only |
| `RCS` 长期失准 | recovery 置信度不可信 | 禁止默认自动执行，只保留人工确认 |
| `RDR` 很高，即使恢复成功也拖慢链路 | recovery 更像昂贵补丁而非主收益 | 仅保留在高价值任务或停悬阶段 |
| `P1/P2` 成立而 `P3` 明显恶化 | recovery 甜区只在停悬/低速窗口 | 主叙事明确写成 phase-bounded recovery |

**当前主张**：D01 后续不该再用“恢复率又涨了 X%”这种单轴表述，而应优先回答 **这条 recovery 线值不值得上线、应该上线在哪个阶段**。这会让 REPORT 从“会恢复”进一步收束成“恢复值不值得部署”。

### 4.13 执行阶段恢复部署判线表（R830 新增）

> R829 已经把 recovery 从“会不会恢复”推进到“值不值得部署”；这一轮继续把它压成 **执行阶段级 go / no-go 表**。目的不是再增加指标，而是让首轮实验结果一出来，就能直接回答：**该把 recovery 留在离线建议、停悬窗口、低速接近窗口，还是根本不该部署。**

| 首轮读数组合 | 优先判断 | 部署结论 | 推荐后继动作 |
|---|---|---|---|
| `SRY` 无明显提升，且 `RDR` 偏高 | recovery 只是昂贵补丁，没有主收益 | **不部署** | 回退到 `Y0/Y1`，只保留 triage + rule fallback |
| `SRY↑`，但 `AER` 也明显上升 | recovery 在把异常硬往前推 | **仅离线建议** | 固定为 `Y2 offline recommendation`，禁止在线自动执行 |
| `SRY↑`，`AER` 稳定，但 `HHB` 明显升高 | 系统在把决策压力转嫁给人工 | **仅人工确认后执行** | 收缩到 `recommendation + human confirm`，不上默认自动恢复 |
| `SRY↑`，`AER/HHB/RDR` 都可控，且 `Y3 >> Y2` | recovery 甜区主要在停悬/回锚阶段 | **仅 P1 停悬/回锚部署** | 主叙事写成 `hover-bounded recovery` |
| `Y4 ≈ Y3` 且 `AER/RCS` 不恶化 | recovery 可扩到低速接近窗口 | **P1+P2 部署** | 允许 `low-speed window recovery`，但仍禁止 P3 默认放开 |
| `Y5` 才有收益，但 `AER` 或 `RCS` 波动明显 | 运动中恢复依赖高风险放行 | **不部署 P3** | 保留 `P1/P2` 方案，明确拒绝 unrestricted online |
| `RCS` 长期失准，即便 `SRY` 不错 | recovery 对自己成功概率没有可靠认知 | **仅人工确认或离线建议** | 优先修 calibration，不继续扩 recovery 能力 |

**主结论规则**：
1. D01 后续主表不再接受“恢复率更高所以更好”的单轴结论，必须先经过这张判线表。
2. 对空中平台，`AER` 与 `RCS` 优先级高于 `SRY`；只要异常漏放或置信失准明显，就不允许把 recovery 升成默认在线能力。
3. 若 `Y3` 成立而 `Y4/Y5` 不成立，论文主叙事就明确写成 **phase-bounded / hover-bounded recovery**，这不是妥协，而是部署边界被清楚证明。
4. 只有当 `SRY↑` 且 `AER/HHB/RDR/RCS` 同时不过度恶化时，recovery 才有资格从“有趣模块”升级成“值得部署的主线机制”。

### 4.21 实验主表优先级冻结规则（R885 新增）

> 目的：把 D01 从“标题/摘要该如何冻结”再往前压一层，直接固定 **首轮实验主表与正文第一结果段** 的解释顺序，防止后续被局部 recovery 指标重新带偏。

| 首轮读数模式 | 默认解释顺序 | 主叙事结论 | 禁止的误读 |
|---|---|---|---|
| `danger-action 漏放率 / late stop / misroute` 未同步改善，但 `packet repair` 漂亮 | 先判安全主收益未成立 | **不允许 recovery 抢主叙事** | 不能把补件成功率包装成部署前 supervisor 成立 |
| `rank-score gate` 单独收益最大，`triage+route_action` 增益有限 | 先收束接口层价值 | **interface-first execution supervisor** | 不能提前写成 stage-aware route supervisor |
| `triage+route_action` 稳定同步拉低前三项核心安全指标 | 先确认 route-aware 收益成立 | **stage-aware route supervisor** | 不能再把 route 增益降格成只是 packet filtering 附庸 |
| `hover-bounded recovery` 只改善 `packet repair 成功率`，未拉低前三项核心指标 | recovery 只记 supporting evidence | **hover-window supporting evidence** | 不能把 hover-window 局部补救写成通用在线恢复能力 |
| `hover-bounded recovery` 也同步改善前三项核心安全指标 | 才允许 recovery 进入主叙事竞争 | **phase-bounded recovery** 候选保留 | 不能跳过 AER/RCS/RDR 直接升格为默认部署能力 |

**解释铁律**：
1. D01 首轮主表默认按 `danger-action 漏放率 → late stop → misroute → packet repair 成功率 → 时延` 的顺序解释，不接受局部 recovery 指标倒灌主结论。
2. 只要前三项核心安全指标没有同步改善，D01 论文正文第一结果段就默认写成“supervisor 主收益未成立”，其余增益一律降级为 supporting evidence。
3. `route supervisor` 与 `interface-first supervisor` 只能二选一占主标题；`hover-bounded recovery` 只有在同时改善核心安全指标时，才保留竞争位。
4. 这张表的作用不是否定 recovery，而是强制 D01 先证明“值不值得部署前放行链采用”，再讨论“能不能顺手补救”。

### 4.22 首轮跨方向收束映射（R889 新增）

> 目的：把 D01 首轮实验结果与 **D01→D06** 的跨方向定位直接绑定，避免首轮读数一出来又把 `interface-first / route supervisor / hover-bounded recovery` 三条线同时挂到 D06 接口层上。

| 首轮信号组合 | D01 默认收束 | 对 D06 的默认输出定位 | 下一轮唯一优先动作 |
|---|---|---|---|
| `rank-score gate` 明显降低 `danger-action 漏放率`，但 `triage+route_action` 对 `late stop / misroute` 增益有限 | **interface-first execution supervisor** | 只承担 **packet pre-screen / safety gate**，不主张 route-level intervention | 优先修 packet schema / verifier 输入质量 |
| `triage+route_action` 同步拉低 `danger-action 漏放率 / late stop / misroute` | **stage-aware route supervisor** | 升格为 **execution-time route supervisor**，可影响 D06 的 reject / reroute 选择 | 优先补 route_action 与 handoff 接口联动 |
| `hover-bounded recovery` 主要改善 `packet repair 成功率`，核心安全指标无净改善 | **hover-window supporting evidence** | 只允许作为 **D06 停悬窗口补件能力**，不得抢 packet / handoff 主叙事 | 回退到 packet / handoff 两线，不继续扩通用 recovery |
| `hover-bounded recovery` 也稳定改善前三项核心安全指标，且 `AER/RCS/RDR` 可控 | **phase-bounded recovery** 候选保留 | 可作为 **D06 的 bounded online recovery** 分支，但仍晚于 packet / handoff 判线 | 仅在停悬/低速窗口继续扩 recovery |
| `rank-score gate / triage+route_action / recovery` 三者都没有站稳 | **supervisor 主收益未成立** | D01 暂不向 D06 输出主接口主张 | 回退 D01 内部 verifier / interface 设计，不做跨方向耦合 |

**跨方向约束**：
1. D01 首轮结果出来后，对 D06 只能输出 **1 条默认接口主张**，禁止同时维持 packet gate、route supervisor、online recovery 三条主叙事竞争位。
2. 若 `interface-first` 成立，D06 默认继续把主问题收在 `packet schema / verifier-gated execution`；若 `stage-aware route supervisor` 成立，才允许 D06 把 handoff / reroute 提升到核心接口位。
3. 若 recovery 只在 hover-window 有效，D06 论文口径必须写成 **bounded recovery**，而不是“online recovery 普遍有效”。
4. 这张映射表优先级低于 D01 内部安全主收益判定，高于所有跨方向叙事包装。

| `rank-score gate` 单独贡献最大，`triage+route_action` 增益有限 | 先收成接口层收益 | **interface-first execution supervisor** | 不能提前宣称 route supervisor 已站稳 |
| `triage+route_action` 同步拉低 `漏放率 / late stop / misroute` | 先收成阶段感知路由收益 | **stage-aware route supervisor** | 不能再让 interface-first 与 recovery 并列抢标题 |
| `hover-bounded recovery` 只改善 `packet repair` 或局部停悬窗口 | 只记 supporting evidence | **supporting evidence only** | 不能把 hover-window 局部收益升格为跨方向主贡献 |
| `hover-bounded recovery` 也同步改善前三项核心安全指标 | 才允许进入主叙事竞争 | **phase-bounded recovery（候选）** | 仍不得绕过核心安全指标直接升格 |

**固定规则**：
1. D01 首轮结果一律按 `漏放率 → late stop → misroute → packet repair → 时延/代价` 的顺序写主表。
2. 只要前三项核心安全指标没同时站稳，`packet repair` 与 `hover-window` 读数默认只能进附录或 supporting 段。
3. 因此 D01 的正文第一段默认不是“recovery 好不好用”，而是“D01 是否已经形成 **部署前 interface-first / stage-aware supervisor** 的净安全收益”。

### 4.17 恢复线资源冻结与主叙事收束规则（R836 新增）

> 目的：D01 现在已经把 `triage / verifier / recovery / route supervisor` 都铺开了，但首轮实验预算有限，不能让 recovery 线无限吞资源。这一节把 **执行阶段部署判线** 继续往前压成 **资源冻结规则 + 主叙事映射**，确保首轮结果一出来，就知道 recovery 是该升成论文主贡献，还是只保留成 supporting evidence。

| 首轮主要读数 | 优先结论 | 论文主叙事 | 资源动作 |
|---|---|---|---|
| `B1/B2` 稳定提升，`R3` 额外增益很弱 | verifier / triage 已足够解释大部分收益 | **部署前 evaluator + triage** | recovery 线冻结为 supporting evidence |
| `SRY↑`，但主要集中在 `Y3`，`Y4/Y5` 不成立 | recovery 甜区只在停悬/回锚阶段 | **hover-bounded recovery** | 只保留 P1/P2 资源，不扩 unrestricted online |
| `SRY↑`，但 `AER` 或 `RCS` 不稳 | recovery 置信与异常边界没站住 | **offline recommendation / human-confirmed recovery** | 停止扩大自动恢复，优先修 calibration |
| `SRY↑` 且 `AER/HHB/RDR/RCS` 都可控 | recovery 具备部署价值 | **triage + calibrated recovery** | 保留 recovery 主线，减少对额外新 baseline 的投入 |
| `RDR` 长期偏高，即使 `SRY` 尚可 | recovery 更像昂贵补丁 | **phase-bounded recommendation** | 转为建议层，不再烧主实验预算 |

**冻结原则**：
1. D01 后续不再接受“每条线都再加一点实验”的推进方式，必须按这张表决定 recovery 是否继续吃主预算。
2. 对空中平台，`AER` 与 `RCS` 的优先级高于“恢复率多涨一点”；只要异常漏放或置信失准明显，就不允许 recovery 升主线。
3. 若 recovery 主收益只出现在 `hover / low-speed window`，论文就明确写成 **phase-bounded / hover-bounded recovery**，而不是把它包装成通用在线恢复器。
4. 只有当 recovery 在线收益与风险边界同时成立时，它才值得从“有趣模块”升级成“值得投稿强调的贡献点”。

| `B2` 显著降低异常漏放，且 `F1/F2` 代价可控 | **已知失败 vs 未知异常分诊层** | WAV / route_action | 激进 recovery 冻结 |
| `Y3` 成立而 `Y4/Y5` 不成立 | **phase-bounded / hover-bounded recovery** | evaluator / triage 作为前置层 | broad online recovery 冻结 |
| `route_action` 显著降低 late stop / misroute | **跨方向 route supervisor** | 本地方向 fallback | D01 内部单点 recovery 叙事降级 |
| `Grounded tokenizer / geometry backbone` 收益最大 | **接口层/主干层设计决定部署上限** | WAV / triage 作为验收配件 | recovery 与 route supervisor 暂停扩张 |

**冻结规则**：
1. 首轮只允许 **1 条主叙事** 占论文标题与摘要；其余一律降为 supporting evidence。
2. 若 `AER` 或 `RCS` 不稳，默认先冻结 recovery 线，优先保 evaluator / verifier / triage。
3. 若 `route_action` 只在单方向自洽、不具跨方向稳定性，就不升成主贡献，只保留为系统工程细节。
4. 若接口层（C6）或几何主干（C7）解释了大部分增益，论文主线应转回“世界模型部署上限由接口/主干决定”，不要硬保 recovery 叙事。

### 4.17 恢复线资源冻结与主叙事收束规则（R836 新增）

> 目的：D01 现在已经把 `triage / verifier / recovery / route supervisor` 都铺开了，但首轮实验预算有限，不能让 recovery 线无限吞资源。这一节把 **执行阶段部署判线** 继续往前压成 **资源冻结规则 + 主叙事映射**，确保首轮结果一出来，就知道 recovery 是该升成论文主贡献，还是只保留成 supporting evidence。

| 首轮主要读数 | 优先结论 | 论文主叙事 | 资源动作 |
|---|---|---|---|
| `B1/B2` 稳定提升，`R3` 额外增益很弱 | verifier / triage 已足够解释大部分收益 | **部署前 evaluator + triage** | recovery 线冻结为 supporting evidence |
| `B2` 成立，且 `route_action` 明显降低 late stop / misroute | D01 更像统一阶段化 supervisor | **stage-aware route supervisor** | recovery 只保留 hover-bounded 候选 |
| `Y3` 成立而 `Y4/Y5` 不成立 | 恢复收益只在停悬/回锚窗口成立 | **phase-bounded / hover-bounded recovery** | 冻结 broad online recovery |
| `SRY↑`，且 `AER/HHB/RDR/RCS` 同时不过线风险 | recovery 具备真实部署价值 | **triage + calibrated recovery** | 保留 recovery 主线，压缩额外 baseline 扩张 |
| `Grounded tokenizer / geometry backbone` 解释了大部分增益 | 世界模型部署上限主要由接口/主干决定 | **interface-first / geometry-first WM** | triage 保留为验收层，冻结 recovery 扩张 |

**冻结规则**：
1. 首轮结果出来后，D01 只允许保留 **1 条主叙事** 占摘要与主图；其余路线一律降级为 supporting evidence。
2. 若 `AER` 或 `RCS` 持续不过线，默认先冻结自动 recovery，优先保留 evaluator / verifier / triage。
3. 若 recovery 收益只集中在 `hover / low-speed window`，论文就明确写成 **phase-bounded recovery**，不要硬包装成通用在线恢复器。
4. 若接口层（C6）或几何主干（C7）解释了主要增益，主线应转回“部署上限由接口/主干决定”，而不是继续让 recovery 吞主预算。

### 4.20 D01 首轮 no-go → 主叙事冻结映射（R872 新增）

> 目的：把 `local-only / rank-score gate / triage+route_action / hover-bounded recovery` 四档首轮结果，直接映射到论文标题层，避免实验里已经知道 recovery 该降级，写作时又把 `supervisor / interface-first / recovery` 三条一起挂回主叙事。

| 首轮结果模式 | 默认主叙事 | 必须降级的项 | 下轮唯一动作 |
|---|---|---|---|
| `rank-score gate` 已明显降低危险放行，但 route_action 增益一般 | **interface-first execution supervisor** | hover-bounded recovery 主叙事 | 继续补 `packet schema / verifier_features` 接口质量 |
| `triage+route_action` 同时稳定降低 `danger-action 漏放率 / late stop / misroute` | **stage-aware route supervisor** | 单纯 evaluator-first / hover-only 叙事 | 固化 triage 路由协议并补跨方向接口 |
| hover-bounded recovery 主要只改善 `packet repair 成功率`，未同步改善前三项核心安全指标 | **supervisor 主线 + recovery supporting evidence** | `phase-bounded recovery` 主标题竞争位 | 把 recovery 收缩到停悬窗口或离线建议位 |
| recovery 对核心安全指标也出现净正增益，且不过度放大时延/风险 | **phase-bounded recovery**（仅保留竞争位） | 纯 hover-window 配角口径 | 继续做阶段边界与上线窗口验证 |

**硬规则**：
1. 只要 `danger-action 漏放率 / late stop / misroute` 没有同步改善，recovery 一律不能抢 D01 主标题。
2. `packet repair` 属于 supporting 级指标，优先级永远低于前三项核心安全指标。
3. 若首轮结果显示 supervisor 已解释大部分净收益，则 D01 标题默认收束为 `interface-first` 或 `stage-aware route supervisor`，不再把 hover-bounded recovery 与之并列。

### 4.21 D01 首轮 no-go 后的标题默认收束规则（R873 新增）

> 目的：继续把 D01 从“知道哪条线该降级”推进到 **一旦某条线判 no-go，标题默认该怎么诚实收束**。否则首轮结果虽然已经说明 recovery 或 route_action 不值得抢主叙事，写作时仍容易把 `interface-first / route supervisor / hover-bounded recovery` 三条一起保留在摘要竞争位。

| no-go 触发模式 | 默认标题收束 | 不再允许并列竞争的项 | 默认后续动作 |
|---|---|---|---|
| `rank-score gate` 已明显降低危险放行，但 `route_action` 对 `late stop / misroute` 增益不稳定 | **interface-first execution supervisor** | `stage-aware route supervisor`、`phase-bounded recovery` 主标题位 | 继续压实 `packet schema / verifier_features / rank_score` 接口质量 |
| `triage+route_action` 已稳定降低 `danger-action 漏放率 / late stop / misroute`，而 recovery 主要只改善 `packet repair 成功率` | **stage-aware route supervisor** | `phase-bounded recovery` 主标题位 | recovery 明确降为停悬窗口 supporting evidence |
| recovery 只在 `hover / low-speed window` 局部成立，且对前三项核心安全指标没有额外净收益 | **supervisor 主线 + hover-window evidence** | `hover-bounded recovery` 作为独立标题叙事 | 固定为 `offline recommendation / hover-only`，不再扩 online |
| recovery 对前三项核心安全指标也给出净增益，且 `AER / RCS / 时延` 不恶化 | **phase-bounded recovery**（仅此时保留竞争位） | 纯 `packet repair` 或单点 repair 成功率叙事 | 继续验证阶段边界，不扩 unrestricted online |

**默认收束规则**：
1. 只要 `danger-action 漏放率 / late stop / misroute` 的主增益已经能被 `rank-score` 或 `triage+route_action` 解释，标题默认先收成 **interface-first** 或 **stage-aware route supervisor**。
2. recovery 若主要只改善 `packet repair 成功率`，默认只能留在 supporting evidence，不能再与 supervisor 并列抢摘要第一句。
3. 只有 recovery 同时改善前三项核心安全指标，且没有明显放大 `AER / RCS / 额外时延`，才允许它保留 **phase-bounded recovery** 的标题竞争位。
4. 一旦某条线在首轮被判 no-go，后续汇报与写作都不得再把它包装成“只是还差一点数据/调参”的并列主线。

### 4.21 D01 首轮摘要句式冻结卡（R876 新增）

> 目的：在 4.20 已经把标题级主叙事冻结后，继续把 **摘要与跨方向汇报口径** 也压成默认句式，避免首轮结果出来后又把 `interface-first / route supervisor / hover-bounded recovery` 三条线同时塞进摘要。

| 首轮主要读数 | 摘要默认主句 | 禁止越级写法 |
|---|---|---|
| `rank-score gate` 先稳住 `danger-action 漏放率`，但 `triage+route_action` 对 `late stop / misroute` 增益一般 | **An interface-first execution supervisor improves packet pre-screening safety before execution.** | 不得提前写成 `stage-aware route supervision` |
| `triage+route_action` 同时稳定降低 `danger-action 漏放率 / late stop / misroute` | **A stage-aware route supervisor reduces unsafe release, late stop, and misroute in packet execution.** | 不得把 recovery 一并抬成并列主贡献 |
| hover-bounded recovery 主要只改善 `packet repair 成功率`，而前三项核心安全指标未同步改善 | **Hover-bounded recovery provides supporting repair evidence but is not the main source of safety gain.** | 不得写成 `deployable recovery policy` 或 `general online recovery` |
| hover-bounded recovery 也对前三项核心安全指标给出净增益 | **Phase-bounded recovery complements the route supervisor with measurable net safety gain.** | 仍不得盖过 interface / route supervisor 的主语位，除非前三项收益主要来自 recovery |

**默认规则**：
1. 摘要第一句只允许出现 **1 条主叙事**，按 `interface-first → stage-aware route supervisor → phase-bounded recovery` 的顺序竞争。
2. recovery 若只修 `packet repair`，默认只能进第二句或结果补充句，不能占摘要主句。
3. 面向 D06 的跨方向汇报也必须沿用这张冻结卡，避免把 D01 重新说成“既是 evaluator、又是 supervisor、又是 recovery policy”。

### 4.18 与 D06 的最小接口绑定（R836 新增）

> 目的：把 D01 和龙虾项目的对齐关系再压实一层。D01 首轮最现实的价值不是替 D06 做规划，而是做 **执行前预筛 + 阶段化处置 supervisor**。

| D01 输出 | D06 中的对应位置 | 首轮用途 | 不该越级承担的事 |
|---|---|---|---|
| `rank_score` | planner packet 进入机载执行前的预筛 | 拦高风险 packet / 比较候选轨迹 | 不直接替代 D06 planner |
| `failure_state (F1/F2)` | 停悬修补 vs 直接接管分流 | 区分可修补局部失败与未知异常 | 不代替 D06 全局任务重规划 |
| `route_action` | `continue / hover / fallback / human review` | 统一执行阶段默认动作 | 不直接下发具体控制量 |
| `hover-bounded recovery` | 停悬窗口内的小范围修补 | 只在低速/停悬阶段验证收益 | 不进入高速运动段默认闭环 |

**当前主张**：D01 若要在龙虾项目首轮落地，最该证明的是 `verifier + triage + route_action` 这套接口能否稳定降低危险放行与误路由，而不是急着让 world model 越级做长程 planner。

### 4.19 D01→D06 packet 预筛接口烟测（R849 新增收束规则）

> 在 `local-only / rank-score gate / triage+route_action / hover-bounded recovery` 四档对照下，D01 首轮主叙事**默认只允许从 evaluator-first / route-supervisor / hover-bounded recovery 三者中选一条**。判定优先级固定为：
> `danger-action 漏放率` → `late stop rate` → `misroute rate` → `packet repair 成功率` → `额外时延`。
>
> **收束规则**：
> 1. 若 `rank-score gate` 已显著降低危险放行，而 `triage+route_action` 进一步降低 late stop / misroute，则 D01 主叙事默认收束为 **pre-execution route supervisor**。
> 2. 若前三项核心指标未同时改善，则 recovery 不得抢主叙事；即便 `packet repair 成功率` 上升，也只能降级为 **supporting evidence**。
> 3. 若 `hover-bounded recovery` 仅在停悬窗口改善 repair 成功率，但对 `danger-action / late stop / misroute` 净收益有限，则论文只允许写成 **阶段性补件**，不得写成通用在线恢复器。
> 4. 只有在 `rank-score / triage / route_action` 三层都已站稳后，recovery 才有资格进入第二阶段扩展讨论。

### 4.20 D01 首轮主叙事冻结规则（R855 新增）

> 目的：把 R849 的收束判断进一步压成**标题 / 主图 / 摘要**的冻结协议，避免首轮结果出来后又让 recovery、evaluator、route supervisor 三条线同时抢叙事。

- 首轮结果出来后，**只允许**在以下三条叙事中保留 1 条主线：
  1. `部署前 evaluator`
  2. `pre-execution route supervisor`
  3. `hover-bounded recovery`
- 默认判线：
  - 若 `rank-score gate` 已明显降低 `danger-action 漏放率`，且 `triage+route_action` 继续降低 `late stop / misroute`，则标题、主表与摘要统一收束为 **pre-execution route supervisor**。
  - 若 hover-bounded recovery 主要只提升 `packet repair 成功率`，但前三项核心指标未同步改善，则 recovery 明确降级为 **补件/附录证据**。
  - 若 evaluator 线已经显著降低危险放行，而 route supervisor 对 `late stop / misroute` 无额外帮助，则主叙事回收为 **部署前 evaluator**。
- 解释优先级禁止改写：后续一律先解释 `danger-action 漏放率`，再解释 `late stop / misroute`，最后才允许讨论 recovery 增益与时延成本。

### 4.19 与 D06 的最小接口绑定（R839 新增）

> 目的：把 D01 从“自己的部署前验收栈”继续压成 **D06 执行前 packet supervisor** 的最小可复用接口，而不是泛泛而谈“未来可服务导航方向”。这一节只绑定最小闭环：`packet rank → F1/F2 triage → route_action → hover-bounded recovery`。

| D01 输出 | 在 D06 中的角色 | 何时触发 | 默认处置 |
|---|---|---|---|
| `rank_score` | 执行前预筛分数 | planner 产出 `Semantic Waypoint Packet` 后 | 低于阈值先不进 controller |
| `failure_state=F1` | 已知失败 | packet 语义/几何问题可命名、可修 | 允许 `repair / hover / bounded retry` |
| `failure_state=F2` | 未知异常 | 新障碍、视角失锁、动力学失配 | 默认 `human review / hard stop / escalate` |
| `route_action` | 阶段感知 supervisor 动作 | `rank_score` 低或 triage 触发后 | `continue / hover / fallback / human review` |
| `hover-bounded recovery` | 仅停悬窗口恢复器 | 已进入停悬/回锚窗口且 F1 成立 | 允许短窗恢复，不扩到 in-motion |

**绑定规则**：
1. D01 不接管 D06 planner；它只在 `planner → verifier / controller` 之间做 **执行前预筛与路由**。
2. D06 若已能稳定执行 shared packet，D01 首轮最值钱的增益是 **降低 late stop / misroute**，而不是提高规划上限。
3. `hover-bounded recovery` 只在 D06 的 `search / hover / re-anchor` 窗口可用；进入 `approach / manipulate-ready` 后默认降级为 `recommendation-only` 或 `hard stop`。
4. 若首轮实验显示 `rank_score + route_action` 对 D06 几乎不降 danger-action 漏放率，则 D01 不再宣传跨方向 supervisor 价值，退回本方向内部验收栈。

### 4.19 与 D06 的最小接口绑定（R839 新增）

> 目的：把 D01 从“自己的部署前验收栈”继续压成 **D06 执行前 packet supervisor** 的最小可复用接口，而不是泛泛而谈“未来可服务导航方向”。这一节只绑定最小闭环：`packet rank → F1/F2 triage → route_action → hover-bounded recovery`。

| D01 输出 | 在 D06 中的角色 | 何时触发 | 默认处置 |
|---|---|---|---|
| `rank_score` | 执行前预筛分数 | planner 产出 `Semantic Waypoint Packet` 后 | 低于阈值先不进 controller |
| `failure_state=F1` | 已知失败 | packet 语义/几何问题可命名、可修 | 允许 `repair / hover / bounded retry` |
| `failure_state=F2` | 未知异常 | 新障碍、视角失锁、动力学失配 | 默认 `human review / hard stop / escalate` |
| `route_action` | 阶段感知 supervisor 动作 | `rank_score` 低或 triage 触发后 | `continue / hover / fallback / human review` |
| `hover-bounded recovery` | 仅停悬窗口恢复器 | 已进入停悬/回锚窗口且 F1 成立 | 允许短窗恢复，不扩到 in-motion |

**绑定规则**：
1. D01 不接管 D06 planner；它只在 `planner → verifier / controller` 之间做 **执行前预筛与路由**。
2. D06 若已能稳定执行 shared packet，D01 首轮最值钱的增益是 **降低 late stop / misroute**，而不是提高规划上限。
3. `hover-bounded recovery` 只在 D06 的 `search / hover / re-anchor` 窗口可用；进入 `approach / manipulate-ready` 后默认降级为 `recommendation-only` 或 `hard stop`。
4. 若首轮实验显示 `rank_score + route_action` 对 D06 几乎不降 danger-action 漏放率，则 D01 不再宣传跨方向 supervisor 价值，退回本方向内部验收栈。

### 4.20 恢复线资源冻结与主叙事收束规则（R839 新增）

> 目的：D01 现在已有 `evaluator / verifier / triage / route supervisor / recovery` 五条子线，不能让首轮实验把每条都写成贡献。这里明确 **一轮实验后只允许保留一条主叙事**，其余全部降级为 supporting evidence 或接口补件。

| 首轮主要读数 | 优先结论 | 论文主叙事 | 资源动作 |
|---|---|---|---|
| `rank_score + WAV` 已显著降漏放，`triage/recovery` 增益弱 | 预筛比恢复更值钱 | **部署前 evaluator + verifier** | recovery 冻结为 supporting evidence |
| `F1/F2` 显著降低异常漏放，`route_action` 进一步降低 late stop | 分诊/路由层最值钱 | **stage-aware triage supervisor** | recovery 只保留 hover-bounded 候选 |
| `hover-bounded recovery` 只在停悬阶段稳，运动段风险高 | recovery 甜区明确但边界窄 | **phase-bounded recovery** | 禁止继续投资源到 in-motion |
| `D01→D06` 接口显著降低 misroute / late stop | 跨方向 packet supervisor 成立 | **interface-first execution supervisor** | D01 主叙事向跨方向接口倾斜 |
| `recovery` 提升来自高代价或高人工负担 | recovery 在拖慢失败 | 不升主线 | 预算转回 verifier / triage / interface |

**冻结规则**：
1. 首轮只允许一条主叙事进摘要和主表；其它收益只能作为解释层或补充实验。
2. 若 `hover-bounded recovery` 与 `route_action` 同时有效，优先保留 **route supervisor / interface**，因为它更容易跨 D06/D07 复用。
3. 若 `recovery` 只在局部窗口有效，必须明确写成 **bounded mechanism**，不能包装成通用在线恢复器。
4. 任何需要持续高人工确认才能成立的子线，默认不占主贡献位。

### 4.21 首轮结论→主图/摘要映射表（R840 新增）

> 目的：继续把 D01 从“结果出来后再解释”压成“结果一出来就知道论文首页该怎么写”。这一节不再新增方法，而是把 **首轮读数** 直接映射到 **主图、摘要一句话、贡献点排序**，避免 verifier / route supervisor / hover-bounded recovery 三条线同时抢主叙事。

| 首轮最强信号 | 论文首页主图 | 摘要第一句该怎么写 | 贡献点排序 |
|---|---|---|---|
| `B1/B2` 稳定压低 danger-action 漏放，且 `F1/F2` 明显减少误升级 | **执行前 evaluator + triage 流程图** | 我们提出一个面向空中执行前放行的 world-model-based evaluator，能在不进入控制环的前提下稳定降低危险 packet 放行 | `C5 解耦验收协议 → triage/verifier → 其余降级 supporting` |
| `route_action` 明显降低 late stop / misroute，且跨 packet 阶段最稳 | **stage-aware route supervisor 状态机图** | 我们把 world model 从“打分器”推进成阶段感知 supervisor，在执行前统一输出 continue/hover/fallback/human-review 路由 | `route supervisor → triage/verifier → hover-bounded recovery` |
| `Y3` 成立而 `Y4/Y5` 不成立，`SRY` 提升且 `AER/RCS` 可控 | **hover-bounded recovery sweet-spot 图** | 我们证明 world-model recovery 的真实甜区不在 unrestricted online，而在停悬/回锚窗口的阶段化恢复 | `hover-bounded recovery → triage → verifier` |
| `Grounded tokenizer / geometry backbone` 解释大部分增益 | **interface-first / geometry-first 对照图** | 我们发现部署前 world model 的上限首先由接口层与几何主干决定，而非恢复器本身 | `C6/C7 → verifier/triage → recovery 降级` |

**执行规则**：
1. 首轮结果出来后，D01 只允许从上表中选 **1 个首页主图**；其余路线全部转为 supporting evidence 或 appendix。
2. 若 `AER`、`RCS`、跨阶段稳定性三者里任一不过线，就不能让 recovery 或 route supervisor 抢摘要第一句。
3. 若接口层/主干层解释了大部分增益，必须主动把 recovery 线降级，避免论文叙事失焦。
4. 对龙虾项目对齐来说，默认优先级仍是 **evaluator/triage → route supervisor → hover-bounded recovery**；除非 recovery 的证据最干净，否则不抢首页主图。

### 4.22 D01→D06 packet 预筛接口契约（R844 新增）

> 目的：把 D01 从“自己的部署前验收栈”继续压成 **D06 可直接消费的执行前 packet supervisor**。这一节只保留最小闭环：`rank_score → F1/F2 triage → route_action → hover-bounded recovery`，不再泛泛谈“未来可服务导航方向”。

#### D06 输入到 D01 的最小字段
- `packet_id`
- `stage_tag ∈ {search, hover, re-anchor, approach, inspect}`
- `semantic_waypoint_packet`
- `planner_confidence`
- `verifier_features`（几何可达性、语义一致性、障碍余量、历史 reject 次数）

#### D01 返回字段
- `rank_score`
- `failure_state ∈ {pass, F1_known_failure, F2_anomaly}`
- `route_action ∈ {continue, hover_hold, packet_repair, fallback, human_review}`
- `recovery_scope ∈ {none, hover_only}`
- `risk_budget`

| D01 输出组合 | D06 默认动作 | 解释 |
|---|---|---|
| `pass + continue` | 直接执行 packet | 正常放行 |
| `F1 + packet_repair` | 先做 packet repair，再次过 verifier | 已知失败优先本地修补 |
| `F1 + hover_hold` | 进入停悬窗口后再恢复 | recovery 只允许在低风险阶段发生 |
| `F2 + fallback` | 回退到更保守 packet / 历史锚点 | 未知异常不允许继续向 controller 下沉 |
| `F2 + human_review` | 触发人工确认 | 高风险异常直接升级 |

**为什么这层接口值钱**：
1. **WorldEval** 这条线已经说明 D01 当前最稳的是 `部署前 evaluator`，不是替 D06 接管长程 planner。
2. **Dream2Fix** 这条线说明恢复不是不能做，而是更适合先锁在 `hover-bounded` 窗口，而不是一上来就在高速运动段全放开。
3. 对 D06 来说，真正省事的不是多一个抽象分数，而是少发明一整套 `什么时候 repair / 什么时候 fallback / 什么时候必须人工确认` 的规则。

**当前主张**：
- D01→D06 首轮只验证 **执行前预筛 + 阶段化处置 supervisor**，不争论谁来做长程 planner。
- 若 `rank_score + route_action` 已能明显降低 `danger-action 漏放 / late stop / misroute`，就足够支撑 D01 先作为跨方向接口层成立。
- 只有这层接口站稳后，才值得再讨论 D01 是否上升为更深的 planner/trainer 主干。


### 4.1+++ Gate-G0~G4 放行门与失败回查协议（R798 新增）

> 这轮继续把 D01 的 recovery 主线往实验可执行层压。前面已经有 `F1/F2 分诊`、`R1/R2/R3 恢复层`、`SRY/AER/HHB/RDR/RCS` 统一记账，也有按执行阶段的部署判线；但还差一张 **首轮实验拿到结果后就能马上判断 go / no-go 的阶段化读数表**。它解决的问题是：恢复收益到底发生在哪个阶段，值不值得把系统从 recommendation-only 升级到 gated online recovery。

| 阶段 | 典型场景 | 首要观察信号 | 过线条件 | 未过线时的默认结论 |
|---|---|---|---|---|
| **P0 离线建议** | 仅输出恢复建议，不自动执行 | `RCS`、建议命中率、异常误建议率 | 建议命中率稳定，且异常误建议低 | 继续只做离线分析，不接控制环 |
| **P1 停悬/回锚恢复** | hover、接近前停顿、回到安全位姿 | `SRY`、`AER`、恢复后新增碰撞率 | `SRY` 明显优于规则回退，且 `AER` 不恶化 | 保留 triage + fallback，不放 recovery |
| **P2 低速接近窗口** | 末端缓慢接近、预抓取对位 | `RDR`、`HHB`、恢复时延 | 额外时延/人工负担可控，且 `Y4≈Y3` | recovery 只允许停悬阶段 |
| **P3 运动中恢复** | 飞行中连续修正、不中断控制链 | `AER`、`RCS`、运动学违规率 | 只有当 `AER/RCS` 也稳定时才考虑 | 默认禁止，除非结果非常干净 |

**阶段化主张**：
1. D01 首轮 recovery 实验默认按 `P0 → P1 → P2 → P3` 串行推进，**不允许跳级**。
2. 只要 `P1` 都站不住，就不再讨论低速窗口和在线恢复，把资源退回 verifier / triage / interface 层。
3. 若 `P1` 成立、`P2` 边际收益很小，则主叙事明确写成 **hover-bounded recovery**，这已经足够构成论文卖点，不必强冲 `P3`。
4. 对主人当前空中平台，`P3` 不是默认目标，而是只有在 `AER` 与 `RCS` 同时过线时才保留的 bonus path。

### 4.16 首轮预算冻结协议（R833 新增）

> 这轮继续把 D01 从“阶段化首轮判线”再往前压一步：不只回答 **recovery 该不该部署**，还要回答 **首轮结果出来后，哪条线还配继续烧 GPU / 标注 / 人工确认预算**。否则就会出现 triage、route_action、Dream2Fix-style recovery 三条线同时续命，实验账面上都“有一点点收益”，但没有一条真正被收束成主线。

| 首轮读数组合 | 优先判断 | 预算动作 | 主线结论 |
|---|---|---|---|
| `B1/B2` 对 `B0` 仍无稳定预筛收益 | evaluator / WAV / triage 还没站住，recovery 讨论过早 | **冻结 R3 recovery**，预算退回接口层与 verifier | D01 暂不谈“会救”，先确保“会拦” |
| `AER` 居高或 `F2` 异常仍频繁误送入 recovery | 系统在高风险区过度自信 | **冻结 online recovery 与跨方向路由**，只保留 offline recommendation | D01 保持 deployment-time evaluator，不升 route supervisor |
| `SRY↑`，但 `HHB` 或 `RDR` 明显偏高 | recovery 只是把复杂度或成本转嫁出去 | **冻结 P2/P3 扩展**，只保留 `P1 hover-bounded` 预算 | 主叙事明确写成阶段性恢复器 |
| `Route Precision↑` 且 `Late Stop Rate↓`，但 recovery 增益有限 | 阶段感知路由比恢复器本身更值钱 | **冻结 R3 扩展，保留 route_action 线** | D01 主线切向 `route supervisor` |
| `RCS` 长期失准，即便 `SRY` 不错 | recovery 对自身成功概率认知不可靠 | **冻结自动执行权**，只允许 recommendation + human confirm | recovery 不升在线主线 |
| `Y3` 成立，`Y4/Y5` 不成立 | 甜区只在停悬/回锚窗口 | **冻结运动中恢复预算**，集中打磨 hover-bounded 证据包 | phase-bounded recovery 足以成稿 |
| `X1` 跨方向接口在 D06/D07 上也稳定降低 `Late Stop Rate` | D01 已具备跨方向统一安全路由价值 | **冻结各方向重复 verifier/shield 扩展**，集中预算到统一接口 | D01 可升为跨方向 route supervisor |

**执行规则**：
1. 首轮实验后，D01 默认只保留 **一条继续扩预算的主线**：`verifier-first`、`route supervisor`、或 `hover-bounded recovery` 三选一，禁止三条并行长期烧资源。
2. 若 `AER` 与 `RCS` 任一持续不过线，自动恢复相关预算全部降级为 **offline recommendation / human-in-the-loop**，不再争夺主实验槽位。
3. 若 `route_action` 的收益显著早于 `R3 recovery` 收敛，D01 论文主叙事应优先转向 **阶段感知安全路由接口**，而不是执着把 recovery 写成最大卖点。
4. 对主人当前空中平台，预算优先级固定为：**先会拦（verifier/triage）→ 再会路由（stage-aware route_action）→ 最后才是会救（recovery）**。

### 4.17 与 D06 / D07 的主从关系收束（R833 新增）

> 这一步是为了避免 D01 后续继续“什么都想管”。既然 D06 负责空中语义导航壳层，D07 负责 Isaac RL/机械臂控制壳层，那么 D01 最应该证明的不是自己能端到端替代它们，而是 **能否作为统一的前置验收与风险路由层**。

| 方向 | D01 应提供什么 | D01 不该抢什么 |
|---|---|---|
| **D06 空中视觉语言导航** | `rank_score / failure_state / route_action / stage_tag`，用于 packet 执行前验收、hover stop、packet repair 触发 | 不直接替代 planner 本身，不负责长程搜索策略设计 |
| **D07 Isaac RL 机械臂控制** | `pass vs anomaly`、已知失败分诊、低速窗口恢复准入 | 不直接替代 RL policy / shield / residual controller |

**当前收束判断**：
1. D01 最有论文味道的主线，不是“最强世界模型”，而是 **world-model-based deployment-time verifier + stage-aware route supervisor**。
2. `Dream2Fix-style recovery` 更适合作为 D01 的加分项，而不是默认的唯一主卖点；只有当 `SRY/AER/RCS` 同时过线，它才配升到标题级贡献。
3. 这也解释了为什么本轮无需继续外扩新论文：D01 当前最缺的不是再多一个世界模型名词，而是把已有 verifier / triage / recovery / route_action 之间的主从关系彻底写实。

### 4.1+++ Gate-G0~G4 放行门与失败回查协议（R798 新增）

> 目的：把 D01 从“有很多实验矩阵”继续压成一条真正可执行的推进顺序，避免 evaluator、trainer、geometry 主干同时开工，最后谁也说不清是哪层先坏了。

| Gate | 先过什么 | 最小证据包 | 没过时优先回查 | 通过后才允许做什么 |
|---|---|---|---|---|
| **G0 接口可用门** | C6 接口层先站住 | I1/I2 至少一组成立，短程 ranking correlation 稳定 | action tokenizer、接口重训成本、语义接地失败 | 进入 verifier / evaluator 联调 |
| **G1 预筛可靠门** | evaluator-first 路线能稳定筛危险动作 | P4 + Tier-1：漏放率下降，误杀率可控 | WAV reachability、自校验阈值、OOD 动作分布 | 进入 trainer-first 或 action-centered 主干比较 |
| **G2 短程增益门** | world model 不只会筛，还能带来短程任务收益 | S1/S2 上成功率或回稳性提升，且 compute 可接受 | feedback reacquisition、异步推理、短程几何误差 | 进入长时 imagined rollout / trainer-first 实验 |
| **G3 长程稳定门** | imagined rollout 或 action-centered WM 的收益不是幻觉 | 长时 consistency、policy gain、hallucination 深度可控 | keyframe 回锚、world-model-policy co-evolution、action-centered 主干 | 进入 geometry-grounded / contact-heavy 子任务 |
| **G4 部署候选门** | 已具备真机前 smoke test 价值 | S3/S4 上危险动作预筛、位姿误差、延迟预算都过线 | 安全门、执行平滑度、真机前回放诊断 | 才允许升为 D01 主线候选 |

**执行规则**：
1. **先 G0/G1，后 G2/G3**。若连接口和危险动作预筛都站不住，不该直接追 imagined RL 提升。
2. **G2 只看短程、可诊断任务**，不把长航程导航和接触误差混在一起。
3. **G3 允许 action-centered WAM、trainer-first、geometry-WM 三路竞争**，但都必须继承同一套 G0/G1 安全前置门。
4. **只要 G4 没过，D01 默认仍是“部署前验收栈”而不是“真机主控器”**，避免研究叙事过度承诺。

### 4.1++++ 首轮 baseline 梯队与证伪顺序（R794 新增）

> 目的：避免 D01 后续实验一上来同时比较过多世界模型角色，先用最少 3 组 baseline 回答“哪一层最值得继续投资源”。

| 梯队 | baseline 组合 | 要回答的问题 | 关键指标 | 判停条件 |
|---|---|---|---|---|
| **Tier-1 安全预筛** | `WorldEval/Interactive WM + WAV + Grounded tokenizer` | 不上真机前，能否先稳定筛掉危险策略 | ranking correlation、danger-action 漏放率、误杀率 | 若 ranking correlation 不稳定或误杀率过高，则先停在 evaluator/verifier 层修接口 |
| **Tier-2 动作中心主干** | `GigaWorld-Policy / WAM-style action-centered WM` | 世界模型若直接服务动作决策，是否比 evaluator-first 路线更值 | 长时执行回稳、action-following fidelity、closed-loop usefulness | 若动作中心主干在安全预筛和回稳上都不占优，则不作为主线，只保留为对照 |
| **Tier-3 几何接地主干** | `f(v)→G / geometry-grounded WM` | 接触与位姿任务里，几何主干是否比视频主干更适合 | contact plausibility、pose error、cross-view consistency | 若几何指标不显著更优，则退回 video-WM + verifier 组合 |

**建议执行顺序**：
1. 先跑 **Tier-1**，确认 evaluator / verifier / interface 三层能否独立成立。
2. 只有当 Tier-1 站住后，再比较 **Tier-2**，回答“action-centered WAM 值不值得替代 evaluator-first 主线”。
3. 最后跑 **Tier-3**，决定 geometry-grounded 主干是成为主线，还是只保留给 contact-heavy 子任务。

**当前研究判断**：D01 最可能成立的路线不是“单一超大 world model 通吃”，而是 **Tier-1 先做安全预筛主线，Tier-2/Tier-3 再按任务类型做增益模块**。这会让 D01 更像一套可部署验收栈，而不是继续扩文献综述。

### 4.2 两阶段后训练最小验收矩阵（R776 新增）

> 目的：把 C4 的“physics alignment + executability alignment”变成能一眼判断是否值得继续投资源的最小实验，而不是停在概念层。

| 实验 | 对比设置 | 关键指标 | 通过门槛 |
|------|---------|---------|---------|
| **P1 物理校正有效性** | Base WM vs +Physics Alignment | 穿模率、反重力率、非法接触率 | 三项至少两项下降 ≥30% |
| **P2 可执行对齐有效性** | Physics-only vs Physics+EVA(IDM reward) | 动作可达率、速度/加速度/jerk 平滑度、下游成功率 | 可达率提升 ≥10%，且平滑度不退化 |
| **P3 评测相关性** | WM policy ranking vs AirSim/真机 ranking | Kendall/Spearman 相关性 | 相关性显著高于 physics-only |
| **P4 安全门收益** | 无 verifier vs +WAV/self-check | 高风险动作漏放率、误杀率 | 漏放率显著下降，误杀率可接受 |
| **P5 分诊层收益** | 只有放行分数 vs 放行分数+F1/F2分诊 | 已知失败恢复成功率、异常漏放率、误升级率 | 异常漏放显著下降，且已知失败不过度升级 |
| **P6 恢复层收益（R809新增）** | `F1/F2 分诊` vs `分诊+Dream2Fix-style recovery` | correction accuracy、闭环恢复率、额外碰撞率、恢复时延 | 已知失败恢复率显著提升，且异常场景不明显增大误恢复 |
| **P7 统一记账门（R829新增）** | `P6 + unified accounting` | SRY、AER、HHB、RDR、RCS | 至少 `SRY↑` 且 `AER/HHB/RDR` 不明显恶化，`RCS` 可校准 |

**首轮建议任务**：优先选空中导航到位后的短程精细动作，避免一开始把长程导航误差和操作误差混在一起。

### 4.3 C6 接口层最小实验矩阵（R785 新增）

> 目的：把 `Grounded World Model / rendering-based tokenizer` 的价值从“看起来有意思”压成能否保留为 D01 主线的最小实验。

| 实验 | 对比设置 | 关键指标 | 通过门槛 |
|---|---|---|---|
| **I1 接口泛化** | Learnable adapter vs Rendering-based tokenizer | 新载体零样本成功率、接口重训成本 | 零样本更优，且无需或几乎无需重训 |
| **I2 排序稳定性** | 两类接口下的 WM policy ranking | Kendall/Spearman 相关性 | Rendering-based 不低于 learnable，最好更稳 |
| **I3 危险动作预筛** | Interface-only vs Interface+WAV | 漏放率、误杀率 | 漏放率显著下降，误杀率可控 |
| **I4 语义接地收益** | 无 referring expression vs 有复杂 referring expression | novel referring expression 成功率 | 复杂语义目标下保持明显优势 |

**建议顺序**：先跑 I1/I2，确认接口层确实值得单列；只有当泛化和排序稳定性同时成立时，再继续做 I3/I4。

### 4.4 C7 几何接地主干最小实验矩阵（R788 新增）

| 实验 | 对比设置 | 关键指标 | 通过门槛 |
|---|---|---|---|
| **G1 主干对照** | Video-WM vs Geometry-WM | cross-view consistency、接触可解释性、位姿误差 | Geometry-WM 在至少两项结构指标上更优 |
| **G2 规划可用性** | 两类主干接同一 planner / evaluator | pose-sensitive task 成功率、ranking correlation | Geometry-WM 在精细操作任务不弱于 Video-WM |
| **G3 时序代价** | 两类主干长时 rollout | 长时一致性、compute / memory 开销 | 若 Geometry-WM 时序退化明显,则转为“局部精细段专用主干” |
| **G4 组合收益** | C6-only vs C6+C7 | 新载体零样本泛化、危险动作预筛 | C6+C7 同时提升泛化与预筛,否则不保留组合路线 |

**建议顺序**：先跑 G1/G2，确认几何接地主干对 manipulation 确实有独立收益；若成立，再决定它是替代 video-WM 主干，还是只服务局部 contact-heavy 子模块。

### 4.5 硬件/服务器需求（R790 推进）

| 模块 | 最低配置 | 推荐配置 | 用途 |
|---|---|---|---|
| **世界模型训练/后训练** | 1×24GB GPU | 1×48GB 或 2×24GB | 跑 physics alignment / EVA 风格后训练与小规模 imagined rollout |
| **仿真与数据生成** | 1×RTX 3090 本地 | 1×4090 或远端更高显存 | UE5 / AirSim / Isaac Sim 联合场景、生成多视角轨迹 |
| **评测与可视化** | 16 核 CPU + 64GB RAM | 24 核 + 128GB RAM | 生成 ranking correlation、穿模率、可达性诊断报表 |
| **真机前 smoke test** | 单卡即可 | 单卡 + 独立日志机 | 跑短程 evaluator / danger-action filter，不要求大吞吐 |

**资源建议**：D01 首轮不必追大模型训练，先优先保障 `仿真可回放 + 多指标自动验收 + 短程 world-model evaluator` 这三件事。只要这套闭环稳住，后面再决定是否值得投更大 GPU 做 trainer-first 路线。

### 4.6 四周执行排期与判停规则（R812 新增）

> 目标：把 D01 从“实验矩阵很多”进一步压成一个 4 周内能跑出 go / no-go 结论的最小推进计划，避免继续堆论文名录却没有第一轮证据。

| 周次 | 目标 | 必做产物 | 放行条件 | 判停条件 |
|---|---|---|---|---|
| **W1 接口与预筛周** | 跑通 `Grounded tokenizer + evaluator + WAV` 的 Tier-1 闭环 | ranking correlation 报表、危险动作预筛日志、F1/F2 分诊标签样例 | G0/G1 过线，漏放率开始下降 | 若接口层排序不稳或误杀率过高，暂停 trainer-first，先只修接口/阈值 |
| **W2 分诊与恢复周** | 在已知失败上加入 `triage + rule fallback + Dream2Fix-style recovery` 对照 | P5/P6 首轮结果、失败类型统计、恢复轨迹可视化 | 已知失败恢复率显著优于 triage-only | 若 recovery 带来明显额外碰撞或异常误恢复，冻结 R3，只保留 R1/R2 |
| **W3 几何与执行周** | 对比 `video-WM` vs `geometry-grounded WM` 在短程接近-对位任务上的收益 | G1/G2 对照表、位姿误差曲线、executability 平滑度统计 | geometry 或 executability 至少一条轴有明确增益 | 若两条轴都不增益，D01 暂不扩主干，只保留 evaluator-first 主线 |
| **W4 长程放行周** | 只让通过前 3 周门槛的方法进入短程 imagined rollout / trainer-first 小验证 | G2/G3 smoke test、关键帧回锚收益、计算预算评估 | 至少一条路线进入 G3 且收益真实 | 若长程收益不稳定或计算代价过高，D01 本阶段收束为“部署前验收栈”，不升主控器 |

**执行约束**：
1. 每周只允许 1 条主线过门，其余路线留作对照，不并行扩成大项目。
2. 任何路线只要连续两次触发判停条件，就降级为 README 候选，不再占用主实验槽位。
3. 若 W1 都没过，不得直接跳到 imagined RL 或大规模后训练。

### 4.7 论文主叙事选择器（R812 新增）

> 用来避免 D01 后续“什么都想讲”，最后论文主线发散。

| 主叙事 | 核心问题 | 最强证据需求 | 风险 | 当前优先级 |
|---|---|---|---|---|
| **S1 部署前验收栈** | world model 能否在真机前先筛掉危险策略并分诊失败 | ranking correlation + danger-action filter + F1/F2/P6 恢复收益 | 论文更像系统评测，方法新颖性要靠 triage/recovery 结构撑住 | **最高** |
| **S2 双动力学主干** | 飞行-操作双动力学 WM 是否比通用 WM 更适合空中任务 | 空中接近/抓取上的明确增益 | 实验门槛高，容易被平台进度卡住 | 中 |
| **S3 trainer-first 闭环** | world model 是否能稳定产出 imagined RL 收益 | G3 长程稳定 + WoVR-style 回锚 + 真机前后对比 | 最容易被 hallucination 和算力拖慢 | 中低 |
| **S4 几何接地主干** | geometry-WM 是否该替代 video-WM 成为主干 | 位姿/接触任务上显著领先 | 可能更适合做子模块而非整篇主线 | 中低 |

**当前建议**：D01 论文主叙事优先锁 **S1 部署前验收栈**，把 Dream2Fix 提供的恢复层、WAV 提供的 verifier 层、2602.16182 提供的异常分诊层压成一条完整方法线。只有当 W3/W4 明确证明双动力学或 trainer-first 路线收益更大，再升级主叙事。

### 4.8 分诊-恢复统一记账协议（R813 新增）

> 目的：既然 D01 当前主叙事锁在 **部署前验收栈**，就不能只报 `恢复成功率`。后续论文主表需要同时回答“救回来了多少”“为此多冒了多少风险”“给主人多加了多少接管负担”。

| 指标 | 定义 | 直觉解释 | 希望趋势 |
|---|---|---|---|
| **SRY（Safe Recovery Yield）** | `已知失败被安全救回的比例` | 真正有价值的恢复收益，不把带来额外碰撞的“伪恢复”算成功 | 越高越好 |
| **AER（Anomaly Escape Rate）** | `未知异常被误当已知失败继续执行的比例` | recovery 线最危险的漏放指标 | 越低越好 |
| **HHB（Human Handoff Burden）** | `每100次任务需要的人类接管次数与平均接管时长` | 系统是不是把压力重新甩回人工 | 越低越好 |
| **RDR（Recovery Debt Ratio）** | `恢复额外耗时 / 原任务正常执行时长` | 即使能救回来，代价是不是已经大到不值得 | 越低越好 |
| **RCS（Recovery Calibration Score）** | `恢复置信度与真实恢复成功率的一致性` | system 会不会对自己“能救回来”过度自信 | 越高越好 |

**用法规则**：
1. **P6 不再只报 recovery success rate**，必须至少同时报 `SRY + AER + HHB`。
2. 若某路线 `恢复率更高` 但 `AER/HHB` 明显恶化，则默认不升主线，只保留为候选补件。
3. 对空中平台，`AER` 权重高于 `RDR`，因为“把异常当普通失败继续飞”比“恢复慢一点”危险得多。
4. 论文主表建议采用 **安全优先排序**：先比 `AER`，再比 `SRY`，最后才比 `RDR` 和 `HHB`。

**当前判断**：Dream2Fix 这类反事实恢复器最可能提升的是 `SRY`，而 WAV + F1/F2 分诊最可能压低的是 `AER`。因此 D01 的真正完整主线不是“恢复器单独变强”，而是 **verifier → triage → recovery** 三段联合优化。

### 4.9 恢复上线放行门（R816 新增）

> 目的：D01 现在已经不缺“恢复率”故事，真正缺的是一句更硬的话, 即 **什么时候 recovery 只配做离线建议，什么时候才配进在线闭环**。

| 放行门 | 必须回答的问题 | 主指标 | 默认结论 |
|---|---|---|---|
| **RG0 建议有效门** | recovery 至少比 `rule fallback` 更有帮助吗 | `SRY / RDR` | 过不了就只保留规则回退 |
| **RG1 异常隔离门** | recovery 会不会把 F2 异常硬当成 F1 继续执行 | `AER / anomaly recall` | 过不了就禁止在线执行，只允许离线建议 |
| **RG2 置信校准门** | system 知道自己什么时候“救不回来”吗 | `RCS / HHB` | 过不了就必须人工确认后才能执行 |
| **RG3 时延预算门** | 恢复决策是否压在短程控制可接受预算内 | `决策时延 / RDR` | 过不了就只允许在低速或停悬阶段触发 |

**执行规则**：
1. `Dream2Fix-style recovery` 默认先以 **offline recommendation** 进入系统，不直接接管在线动作。
2. 只有同时满足 `RG1 + RG2`，才允许从“建议恢复”升为“自动恢复”。
3. 对空中平台，`RG1` 权重大于 `RG0`，因为“救回一点已知失败”不值得交换“把未知异常继续往前飞”。
4. 若 `RG3` 不过线，不代表 recovery 无价值，而是把它降级到 **停悬/回锚后再执行** 的阶段性恢复器。

**当前判断**：D01 下一步最值得证明的，不是 `R3 recovery` 本身更聪明，而是 **online recovery 的准入边界可被清楚写出来**。这会让 D01 的论文主叙事从“会恢复”升级成“知道何时该恢复、何时不该恢复”。

### 4.10 分阶段恢复触发包线（R819 新增）

> 来自本地回扫 **Dream2Fix / WorldEval** 与现有 `RG0~RG3` 的直接收束。D01 现在不该再把 recovery 写成统一开关，而要明确 **不同飞行阶段允许的恢复类型不同**。

| 阶段 | 典型状态 | 允许恢复动作 | 默认门槛 | 不允许做什么 |
|---|---|---|---|---|
| **P0 静止评测** | 离线回放 / rollout ranking / 不控真机 | `offline recommendation`、反事实恢复打分 | 只需过 `RG0` | 不得把建议直接当在线控制 |
| **P1 停悬/回锚** | 低速、姿态稳定、允许短暂停顿 | `R1 rule fallback`、`R3 gated recovery` | 必须过 `RG1 + RG2`，时延可略宽 | 不得跨越 anomaly gate 强行继续任务 |
| **P2 接近段** | 低速逼近目标、局部几何敏感 | 仅允许短窗修正、保守回退、局部重规划 | 必须额外过 `RCS` 与 jerk/碰撞预算 | 不得做长轨迹恢复或高幅度机动 |
| **P3 运动中执行** | 正在飞行、速度较高、控制预算紧 | 默认只允许 `R1` 或 hard stop | 需同时过 `RG1 + RG2 + RG3` 才能开放自动恢复 | 不得默认放开 Dream2Fix-style 长程 recovery |

**核心判断**：
1. **Dream2Fix-style recovery 默认先绑定 `P1 停悬/回锚` 场景**，不再假设它天生适合运动中在线接管。
2. 若 `P1` 成立而 `P3` 不成立，D01 论文也仍然成立，因为它回答的是 **phase-bounded recovery**，不是“任意时刻都能自动救”。
3. 后续主表应单列 `阶段 × 放行门 × 指标`，避免把停悬恢复的收益误写成通用在线恢复收益。

### 4.11 阶段感知分诊-恢复路由表（R820 新增）

> 这一步把 **WorldEval 的部署前排序器** 与 **Dream2Fix 的恢复器** 真正接上。D01 后续不该只输出 `pass / fail / anomaly`，而要给出 **当前阶段允许的动作路由**，否则 evaluator、triage、recovery 仍然是三套各说各话的模块。

| 输入条件 | P0 静止评测 | P1 停悬/回锚 | P2 接近段 | P3 运动中执行 |
|---|---|---|---|---|
| **高 pass 分 + 低 anomaly** | 允许通过，仅记日志 | 通过 | 通过 | 通过 |
| **低 pass + 已知失败 F1** | 输出 `offline recovery recommendation` | 允许 `R1/R3 gated recovery` | 只允许 `短窗修正 or 回退` | 默认降级到 `R1 / hard stop` |
| **高 anomaly F2** | 标为高风险样本，不执行 | `hard stop / human review` | `hard stop / retreat` | `hard stop` |
| **低 pass + 低 anomaly,但置信度差** | 保留作回放复查 | `re-evaluate after hover` | `减速后重评估` | `延后到下一个稳定窗口` |

**推荐输出接口**：
1. `rank_score`：来自 WorldEval-style evaluator，回答“这条动作值不值得继续”。
2. `failure_state`：`pass / F1 / F2 / uncertain`，回答“它属于哪类风险”。
3. `route_action`：`pass / recommend / fallback / gated_recovery / hard_stop`，回答“当前阶段到底该做什么”。

**为什么重要**：
- 这样 D01 就不再只是“会打分的世界模型”，而是具备了 **阶段感知决策路由**。
- 后续 D06/D07 接入时，也能直接继承 `route_action`，避免每条链路自己发明恢复规则。
- 若 `route_action` 在 P1 成立、P3 不成立，论文主叙事也依然完整，因为我们证明的是 **阶段感知安全路由**，不是“统一在线恢复万能开关”。

### 4.12 D01→D06/D07 下游接口契约（R824 新增）

> R820 把 D01 内部路由写清后，本轮继续往前推进一步：把 `route_action` 正式定义成 **可被 D06 导航栈与 D07 控制栈直接消费的统一接口**。这样 D01 才不只是“自己的评测器”，而是上游安全路由层。

| 字段 | 含义 | D06 空中VLN 消费方式 | D07 Isaac RL 机械臂 消费方式 |
|---|---|---|---|
| `rank_score` | 当前动作/子目标的部署前可信度 | 决定 planner packet 是直接下发还是降级重规划 | 决定 policy rollout 是继续执行还是切回 shield / fallback |
| `failure_state` | `pass / F1 / F2 / uncertain` | 把失败归到 `可修复导航偏差 / 未知环境异常` | 把失败归到 `可修复接触偏差 / 未知动力学异常` |
| `route_action` | `pass / recommend / fallback / gated_recovery / hard_stop` | 映射到 `继续飞 / packet repair / local replan / hover-recovery / stop` | 映射到 `继续执行 / action patch / shield fallback / gated recovery / emergency stop` |
| `stage_tag` | `P0/P1/P2/P3` 当前阶段标签 | 对应 `离线评测 / 停悬 / 接近 / 飞行中` | 对应 `离线回放 / 静止对位 / 接触接近 / 动态执行中` |
| `risk_budget` | 当前允许的时延/碰撞/jerk 预算 | 限制 D06 只在预算内做局部修复 | 限制 D07 只在预算内做 recovery 或 residual correction |

**接口规则**：
1. **D01 不直接替 D06/D07 做规划或控制**，只输出部署前路由建议，避免职责混叠。
2. **D06 默认只消费 `pass / fallback / hard_stop` 三档**，`gated_recovery` 仅在 `P1/P2` 低速窗口开放。
3. **D07 默认比 D06 更保守**，`F2` 一律直接映射到 `emergency stop / human review`，不允许在高接触不确定区间自动放大动作。
4. 后续若 D06/D07 论文要共享一套安全叙事，可直接把 D01 描述成 **world-model-based route supervisor**，而非额外再发明一层 verifier。

**当前判断**：
- 对 **D06**，D01 最值钱的输出不是“更会找路”，而是 **什么时候该把 planner 输出降级成 packet repair / local replan**。
- 对 **D07**，D01 最值钱的输出不是“替代控制器”，而是 **什么时候该把 RL policy 交还给 shield / fallback / emergency stop**。
- 因此 D01 的论文主叙事又更稳了一点，它不需要证明自己能通吃下游，只需要证明 **同一套 route supervisor 能稳定服务导航与控制两条链**。

### 4.17 恢复线资源冻结与主叙事收束规则（R836 新增）

> 目的：D01 现在已经把 `triage / verifier / recovery / route supervisor` 都铺开了，但首轮实验预算有限，不能让 recovery 线无限吞资源。这一节把 **执行阶段部署判线** 继续往前压成 **资源冻结规则 + 主叙事映射**，确保首轮结果一出来，就知道 recovery 是该升成论文主贡献，还是只保留成 supporting evidence。

| 首轮主要读数 | 优先结论 | 论文主叙事 | 资源动作 |
|---|---|---|---|
| `B1/B2` 稳定提升，`R3` 额外增益很弱 | verifier / triage 已足够解释大部分收益 | **部署前 evaluator + triage** | recovery 线冻结为 supporting evidence |
| `P1/P2` 与 `R1/R2` 有收益，但 `R3` 成本高、`RCS` 不稳 | recovery 只在保守阶段有局部价值 | **stage-aware route supervisor** | 仅保留 hover / low-speed recovery，小步继续 |
| `R3` 明显提升 `SRY` 且 `AER/HHB/RDR/RCS` 都不过界 | 已知失败恢复真正带来部署收益 | **hover-bounded recovery** | 保留 recovery 主线，但冻结更激进扩展 |
| `E6` 表现最好，跨方向接口收益强于单方向恢复收益 | D01 更像上游统一 supervisor，而非单独 recovery 论文 | **interface-first safety supervisor** | 资源转向 D01→D06 接口与统一验收 |
| `Y4/Y5` 才有增益，且 `AER` 或 `RCS` 波动大 | recovery 依赖高风险在线放行 | **不把 recovery 作为主贡献** | 冻结 online recovery 扩展，回退为离线建议 |

**收束规则**：
1. D01 首轮只允许 **一条主叙事** 占据主表，其余全部降为 supporting evidence，不允许 verifier / triage / recovery / interface 四线并行抢主位。
2. 若 `E6 D01→D06` 接口实验收益清晰，而 recovery 只在局部窗口成立，则主叙事优先改写为 **统一 route supervisor**，避免把论文写成过窄的恢复器工作。
3. 只要 `AER` 或 `RCS` 明显失控，recovery 就不得再扩到更激进阶段；预算优先回流到 triage / interface / deployability 证据补强。
4. 对龙虾项目当前落点，D01 最现实的第一论文位仍是 **部署前 evaluator + stage-aware supervisor**，不是长程 planner，也不是无边界通用 recovery 引擎。

### 4.18 与 D06 的最小接口绑定（R836 新增）

### 4.19 首轮主叙事结果解释顺序冻结（R862 新增）

> R861 已把 D01 的五个候选叙事槽位（`evaluator-first / triage-first / route-first / hover-recovery-first / interface-first`）拉到同一张烟测表上；这一轮继续把它压成 **结果解释顺序不可逆规则**。目的不是再增加指标，而是防止首轮结果出来后，因为某个局部 recovery 数字好看，就把整篇论文标题和主表重新改写掉。

**统一解释顺序（必须按此顺序，不得跳步）**：
1. **Core Safety Gain**：先看 `danger-action 漏放率 / late stop / misroute` 是否形成净改善。只要这三项没有同时站住，任何 recovery 或 packet repair 增益都不得升格为主标题。
2. **Narrative Exclusivity**：再看收益是否主要由某一叙事独占解释。若 route-first 与 interface-first 共享同一批主收益，则默认优先保留更跨方向可复用的那条，不允许同时保两条并列标题。
3. **Cross-Direction Utility**：再看这条叙事是否能自然服务 D06/D07，而不只是 D01 内部自洽。若某条线只能解释 D01 本地实验，却不能外接 packet 执行前验收链，则默认降级。
4. **Budget-to-Gain Ratio**：再看这条线是否值得继续烧算力/篇幅。若收益只靠高恢复债务、高人工确认或高时延换来，则最多保留为附录或 supporting evidence。
5. **Risk Inflation**：最后看是否伴随 `异常漏放 / 人工负担 / 恢复债务 / 置信失准` 上升。只要风险膨胀明显，即便局部成功率漂亮，也不得争主叙事。

**直接冻结规则**：
- 若净收益主要来自 `danger-action 漏放率 + late stop + misroute` 的同步下降，D01 主线默认优先收束为 **stage-aware route supervisor**；若同一收益更明显依赖统一 packet 前验收接口，则改收束为 **interface-first execution supervisor**。
- `hover-bounded recovery` 只有在**不恶化前三项核心安全指标**的前提下，还额外带来跨阶段、低风险、可校准的净收益，才允许保留为次主线；否则统一降级为 hover-window supporting evidence。
- 若 `triage-first` 的主要价值只是把已知失败与异常分开，但没有继续转化为执行前路由收益，则它默认并入 route/interface 叙事，不单独占标题。
- 首轮之后禁止用单一 `packet repair 成功率 / recovery success rate / hover window gain` 反向改写主标题；所有标题调整都必须先通过上述五级顺序。
- **R883 补充冻结**：只要 `rank-score gate + triage+route_action` 还没有在 `danger-action 漏放率 / misroute / late stop` 三项上同时形成净改善，recovery 线一律不得升级为主标题；D01 的实验预算优先继续投向 pre-screen / route decision / safe reject，而不是扩在线补救。


> 目的：把 D01 从“自己内部会分诊、会恢复”继续推进到“能不能给 D06 一个真正可接的执行前安全接口”。这一步不扩新模块，只把已有 `rank_score / known-failure vs anomaly / route_action / hover-bounded recovery` 收成最小跨方向契约。

**最小输出包 `Pre-Execution Safety Packet`**：
- `rank_score`: 当前 planner / packet 是否值得执行的综合分数
- `failure_state`: `pass / known-failure / anomaly`
- `route_action`: `allow / recommendation-only / human-confirm / hover-bounded-recovery / reject`
- `stage_tag`: `search / approach / inspect / manipulate-ready`
- `risk_budget`: 允许的速度、爬升率、恢复窗口与人工介入阈值

**为什么只先做这一层**：
1. D06 当前最缺的不是再多一个 planner，而是 **执行前准入与阶段化处置** 的统一 supervisor。
2. D01 的 `F1/F2 + R1/R2/R3 + Y3/Y4/Y5` 已经足够产生可复用的 `route_action`，没必要等到 world model 主干更大再接。
3. 这层接口一旦稳定，D06 的 `Semantic Waypoint Packet` 就能在执行前统一经过 D01 安全筛查，而不是各自发明 reject / fallback 规则。

**当前接口主张**：
- D01 不替 D06 做长程规划；它只负责 **执行前预筛 + 阶段化处置建议**。
- `anomaly` 默认高于 `known-failure`；只要触发异常，就优先 `reject / human-confirm`，不让 D06 在高风险 OOD 场景里把异常假装成普通 packet repair。
- 只有当 `stage_tag ∈ {search, approach}` 且 `failure_state = known-failure` 时，才允许进入 `hover-bounded-recovery` 或 recommendation-first 恢复。
- 这会让 D01 的首轮真实价值更贴近主人当前工程链：**危险放行过滤、误路由拦截、停悬窗口恢复建议**。

### 4.18 与 D06 的最小接口绑定（R840 新增）

> 目的：把 D01 从“自方向内部的部署前验收栈”继续压成 **可被 D06 直接消费的执行前 supervisor**，但严格限制在低风险、低耦合的 packet 预筛层，不越权替代 D06 planner。

#### 接口最小包
D06 向 D01 暴露的首轮字段只保留：
- `stage_tag`：`search / hover / re-anchor / approach`
- `goal_repr`：目标语义与局部几何摘要
- `route_candidates`：候选 packet 或局部动作分支
- `state_snapshot`：执行前平台状态（姿态、速度、相对位姿、近邻障碍摘要）

D01 返回的首轮输出固定为：
- `rank_score`
- `failure_state ∈ {pass, F1_known_failure, F2_anomaly}`
- `route_action ∈ {continue, hover, fallback, human_review}`
- `recovery_hint`（仅在 `stage_tag=hover` 时可非空）

#### 为什么只绑到这里
1. **不抢 D06 planner 主权**：D01 只回答“这包该不该放、该进哪条处置分支”，不生成长程 waypoint。
2. **先守住最值钱的三件事**：危险放行、误路由、停悬窗口恢复。
3. **便于跨方向复用**：同样接口未来也能接 D07 的 rollout gate / shield fallback。

#### 首轮主张
- 若 `rank_score + triage` 已显著降低 `danger-action 漏放率`，D01 主叙事优先写成 **pre-execution evaluator**。
- 若 `route_action` 对 `late stop / misroute` 改善最稳，主叙事升级为 **stage-aware supervisor**。
- 若收益主要来自 `hover` 阶段的 `recovery_hint`，则 recovery 明确降为 **phase-bounded supporting evidence**，不与 evaluator / supervisor 抢主叙事。

### 4.19 D01→D06 packet 预筛接口烟测（R848 新增）

> 目标：把 `WorldEval + F1/F2 triage + hover-bounded recovery` 收成一组最小跨方向烟测，验证 D01 是否真能在 D06 的 `Semantic Waypoint Packet` 执行前承担统一 supervisor，而不是只在 D01 自己报告里好看。

| 实验 | 对比设置 | 关键指标 | 通过门槛 |
|---|---|---|---|
| **E6a local-only** | D06 packet 直接执行（无 D01 预筛） | task success、danger-action 漏放率、late stop | 作为基线，不设门槛 |
| **E6b rank-score gate** | `rank_score` 低于阈值即阻断执行 | 漏放率、误杀率、packet latency overhead | 漏放率明显下降，误杀可控 |
| **E6c triage + route_action** | D01 输出 `pass / fallback / human_review` | misroute、late stop、fallback 成功率 | 至少一项 routing 指标显著改善 |
| **E6d hover-bounded recovery** | 仅在 `hover / re-anchor` 阶段启用 `recovery_hint` | packet repair 成功率、Recovery Debt Ratio、anomaly escape | repair 有效且不显著抬高 anomaly escape |

**记录要求**：
1. 统一记录 `danger-action 漏放率 / late stop / misroute / packet repair 成功率`，不接受只报总成功率。
2. `hover-bounded recovery` 只允许在 `search / hover / re-anchor` 三类窗口启用，不得默认扩到高速 approach。
3. 若 `rank-score gate` 已能解释大部分收益，则 recovery 自动降级为 supporting evidence，优先保 evaluator / triage 主线。
4. 若 `triage + route_action` 的收益强于 `hover-bounded recovery`，则 D01 主叙事进一步收束为 **pre-execution route supervisor**。

## 五、论文写作计划

### 目标会议
| 会议 | 投稿截止 | 审稿周期 | 备注 |
|------|---------|---------|------|
| **ICRA 2027**（Primary） | ~2026-09 | 3个月 | 机器人领域顶会，具身智能录稿多，偏好系统级工作 |
| **CoRL 2027**（Secondary） | ~2026-11 | 3个月 | 具身智能专会，偏好学习+系统结合，ICRA被拒后可转投 |
| **IROS 2027**（备选） | ~2027-01 | 3个月 | 机器人应用偏多，接收率较高 |

> **推荐主投 ICRA 2027**：理由——①飞行-操作双动力学世界模型属具身智能+无人机交叉创新，适合 ICRA 的 robotics 轨道；②两阶段后训练路线（physics alignment + executability alignment）是可验证的系统工作；③实习项目（UE 数据采集）可直接提供实验支撑

### 论文标题（候选）
- *"A Dual-Dynamics World Model for Aerial Manipulation: Physics-Aligned Training meets Executability Verification"*
- *"WorldGym: A Hierarchical World Model for UAV Vision-Language Navigation with Safety-Guaranteed Planning"*

### 时间线
| 阶段 | 目标 | 截止日期 |
|------|------|---------|
| **文献收尾** | 完成 Section 2 相关工作，扫完 D01/D06/D07 剩余候选论文 | 2026-05-10 |
| **方法定型** | C1-C5 创新点收敛，接口定义冻结，与 D04/D06 创新点解耦明确 | 2026-05-31 |
| **实验启动** | 选定主实验（physics alignment ablation + executability verification），完成 UE/AirSim 实验环境 | 2026-06-15 |
| **实验完成** | 核心实验出结果（成功率/物理穿模率/ranking correlation） | 2026-07-31 |
| **论文初稿** | 完成全文初稿（背景→相关工作→方法→实验→讨论） | 2026-08-31 |
| **论文打磨** | 格式规范、图表美化、补充实验、rebuttal 预判 | 2026-09-15 |
| **投稿 ICRA 2027** | Submit | ~2026-09-20 |

### 论文结构（目标版）
1. **Introduction**：空中操作的世界模型需求（6-DoF 运动+接触动力学双重约束）
2. **Related Work**：地面世界模型→空中世界模型差距，C1-C5 各创新点对齐的相关工作
3. **Method**：C1 飞行-操作双动力学世界模型 + C2 组合式架构 + C3 两阶段后训练
4. **Experiments**：UE5/AirSim 仿真 + 空中操作任务 + ablation + 跨载体迁移验证
5. **Conclusion & Future Work**：限制+下一步

### 关键里程碑检查点
- [ ] **M1（2026-05-10）**：Section 2 相关工作全部归类，创新点与已有工作的增量明确
- [ ] **M2（2026-05-31）**：方法框架接口冻结，不在随意增删创新点
- [ ] **M3（2026-06-15）**：实验环境可跑通，baseline 对比方案确认
- [ ] **M4（2026-07-15）**：核心结果数字到手（不用完美，但要有趋势）
- [ ] **M5（2026-08-15）**：全文草稿完成，导师/同事第一轮review
- [ ] **M6（2026-09-15）**：终稿提交

---

## 六、后续 TODO
- [ ] **M1（2026-05-10）**：Section 2 相关工作全部归类，创新点与已有工作的增量明确
- [ ] RISE 想象训练在 AirSim 环境的可行性验证
- [ ] WAM 的 action-aware latent 与 D04 跨载体 force latent 的融合方案
- [ ] 把 WorldArena + EZSbench 思路改造成“空中 WorldArena mini”，作为主人后续实验统一验收表
- [ ] 增加一版"policy evaluation correlation"实验，验证 world model 评分和仿真/真机成功率是否一致
- [ ] 设计轻量版 physics alignment 后训练实验，验证是否能降低穿模/碰撞类失败
- [ ] 设计一版 WoVR 风格的关键帧回锚 imagined rollout，对比纯 imagined rollout 在空中导航 / 空中操作中的稳定性
- [ ] 补一张 OpenWorldLib 风格 capability taxonomy，对照 D01 当前 trainer / planner / evaluator / safety alignment 四类能力
- [ ] 把 C6 接口层实验正式落成 `learnable adapter vs rendering-based tokenizer vs +WAV` 三组对照
- [ ] 新增一组 `pass-only vs pass+known-failure/anomaly triage` 对照,验证 F1/F2 分诊层是否真的降低异常漏放
- [ ] 把 4.12 的 `route supervisor` 契约映射到 D06 packet planner 与 D07 shield/fallback 接口，形成跨方向统一安全层图
- [ ] **新增**：HY-Embodied-0.5 (2604.07430) 作为 related work 对标基线入 Section 2
- [ ] **新增**：EmbodiedClaw (2604.13800) 与 D05 数据飞轮的交叉点补入 Section 2.5（研究自动化）
- [x] **R776**: 新增 4.2「两阶段后训练最小验收矩阵」，把 Physics Alignment / EVA / WAV 三层关系压成 P1-P4 四组最小实验
