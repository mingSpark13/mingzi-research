# D02: VLA 研究报告

> 最后更新：2026-04-17 | 成熟度：🟡中期（R778补上低层部署对照矩阵，开始把Paper A从“架构直觉”压成可测协议）
> 状态：🟡 推进中

## 一、研究背景与动机

VLA（Vision-Language-Action）是具身智能的核心范式，将视觉感知、语言理解和动作生成统一到一个模型中。然而现有 VLA 方法（OpenVLA/π0/GR00T/GO-1）均为纯端到端架构，存在根本性问题：(1) VLM forward 延迟使其无法满足高频控制需求；(2) 无真正的「意图规划↔精细执行」层次化解耦；(3) ACT 的 action chunking 是时序聚合而非意图层解耦，OnFly 的双 agent 是感知频次解耦，均非语义意图层。

## 二、相关工作梳理

### 2.1 纯端到端 VLA
| 方法 | 特点 | 精细操作 | 层次化解耦 |
|------|------|---------|-----------|
| OpenVLA | 开源，action chunking，Jetson Orin 上 >900ms | 一般 | ❌ |
| π0 | Flow matching 动作生成 | 一般 | ❌ |
| GR00T | Cross-embodiment | 一般 | ❌ |
| GO-1 | 大数据驱动 | 一般 | ❌ |

### 2.2 改进型 VLA
- **LILAC** — Flow-based VLA，光流→轨迹，泛化性强
- **TIES** — VLA token 剪枝，78%减少+6%提升
- **LaST0** — 隐式时空 CoT + MoT 双专家
- **ManualVLA** — MoT + ManualCoT 多模态手册生成
- **Fast-dVLA** — 扩散 VLA + CoT，加速推理
- **Xiaomi-Robotics-0** — 异步执行训练 + action chunk 时序对齐，强调消费级 GPU 上的真机实时 rollout
- **Realtime-VLA V2** — 把 fast/smooth/accurate 三指标一起优化，补齐真实部署里的连续执行与轨迹平滑问题
- **TIC-VLA** — 显式建模 delayed semantic-control interface，把语义推理延迟作为控制输入的一部分
- **DAM-VLA** — action routing + 双 diffusion action model（arm/gripper）+ dual-scale weighting，显式拆分不同子动作建模

### 2.3 空中 VLA
- **AIR-VLA** — 空中操纵 VLA 基准
- **UAV-Track VLA** — π₀.₅ 架构空中追踪，temporal compression

### 2.4 核心发现（已确认的架构空白）
**现有 VLA 均无真正的「意图规划↔精细执行」层次化解耦。** 这是论文 A 的核心创新切入点。

### 2.5 🆕 R781 新增：长时序 plan-reflect-execute 证据
- **Long-Horizon Manipulation with Adaptive Planning and Reflection** (2604.13942) — 明确采用 dual-system 结构，把 **VLM planner 的任务分解/记忆管理/验证/反思恢复** 与 **VLA executor 的几何导向执行** 拆开。它对 D02 最重要的价值不是“再来一个长时序系统”，而是再次证明 **planner + verifier + executor** 的三段式闭环在复杂操作里是自然收敛方向，说明 Paper A 的层次化切入并不是少数派假设。

## 三、我们的创新方向（论文 A）

### 3.1 三层语义解耦架构
1. **高层 VLM/LLM** — 输出任务意图（慢思考，秒级）
2. **中层意图解析器** — 意图→操作序列+姿态约束+安全约束
3. **低层精细执行** — ACT/Diffusion Policy/PID-MPC（毫秒级）

### 3.2 低层控制器选项
| 方案 | 优势 | 推理频率 | 适用 |
|------|------|---------|------|
| ACT | 快速、误差累积低 | ~10Hz | 精细操作 |
| Diffusion Policy | 多模态动作分布 | ~3-5Hz | 复杂多峰任务 |
| PID-MPC | 成熟稳定，无模型 | ~100Hz+ | 底层飞行控制 |
| 混合（推荐） | VLM→ACT/DP→PID | 分层频率 | 空中操作 |

### 3.3 关键差异
OpenVLA 的 action chunking 是「预测未来8步」而非「解耦慢快控制」；论文 A 的层次化才是真正的意图-执行解耦。

### 3.4 本轮新增启发（R542）
1. **低层验收标准要升级**：Realtime-VLA V2 说明 Paper A 后续不能只看成功率和平均延迟，还要看轨迹平滑度、控制抖动率、chunk 拼接稳定性。
2. **显式建模语义延迟是必要的**：TIC-VLA 说明高层语义推理可以慢，但必须把 stale semantic state 和 latency metadata 显式交给控制层。
3. **Paper A 中层可加 latency-aware 接口**：让中层意图解析器接收“当前观测 + 延迟语义状态 + 时间偏移”，而不是假设语义永远新鲜。
4. **最小可行原型更清晰了**：高层 VLM 输出意图，中层做 routing+约束+latency compensation，低层双头控制器负责平滑连续执行。

### 3.5 本轮新增启发（R574）
1. **统一生成式低层候选更明确了**：MMaDA-VLA 说明未来观测条件化 + diffusion action chunk 的统一骨架，适合作为 Paper A 的低层执行器候选之一。
2. **慢快解耦需要 latent interface，而不只靠文本**：LaST0 证明 latent spatio-temporal CoT + 异频双专家可以同时兼顾推理与控制频率，这比单纯 textual CoT 更贴机器人控制现实。
3. **中层“手册/步骤”接口是可行路线**：ManualVLA 把 multimodal manual 变成 action expert 的显式条件，进一步支撑 Paper A 的中层意图解析器应输出结构化中间表示，而非直接从语义跳动作。
4. **结论不变但更稳**：即便 2026 新 VLA 更强，当前公开路线依旧没有替代 Paper A 的 **显式语义接口 + latency-aware 中层 + 安全约束层** 三件套。

### 3.6 上一轮启发（R570）
1. **统一生成式 VLA 值得作为低层候选，但不能替代层次化解耦**：MMaDA-VLA 说明 diffusion VLA 正在往“统一多模态理解+生成”收敛，低层动作生成能力值得跟踪。
2. **Paper A 的中层价值反而更清楚了**：即便生成能力更强，MMaDA-VLA 仍是原生端到端 VLA 路线，没有直接解决高层语义意图、延迟补偿与安全约束显式接口的问题。
3. **可执行策略**：后续可把 MMaDA-VLA 放进 Paper A 的“低层执行器候选”列表，与 ACT / Diffusion Policy / Xiaomi-Robotics-0 风格实时执行路线并列评估，而不是把它当整套系统替代。

### 3.7 本轮新增启发（R577）
1. **双频控制比单纯 action chunk 更关键**：TIDAL 说明 diffusion VLA 真正的瓶颈是“语义慢, 控制也被拖慢”, 所以要把 **low-frequency semantic loop** 和 **high-frequency micro-control loop** 显式拆开。
2. **stale semantic state 应被显式建模**：TIDAL 的 temporally misaligned training 进一步证明, 高层意图过时不是噪声而是常态, 中层应传递 `intent_age/latency` 之类的时间信息给低层。
3. **开环 chunk 需要闭环校验器兜底**：SV-VLA 说明“重型 VLA 低频规划 + 轻量 verifier 高频监视”是当前很实用的一条工程路线, 很适合作为 Paper A 中层验证器的直接参考。
4. **Paper A 原型更清楚了**：高层 VLM 负责宏意图, 中层做 routing + latency-aware verification, 低层执行器负责高频修正与平滑控制。

### 3.8 上一轮启发（R537）
1. **先解实时性，再解通用性**：Xiaomi-Robotics-0 表明异步执行和 chunk 对齐可以先把 VLA 从“能跑”推进到“能稳定连续跑”。
2. **按动作子空间拆模型是有效的**：DAM-VLA 把 arm / gripper 分头建模，启发 Paper A 可拆成飞行控制头 / 末端操作头。
3. **Paper A 最小可行原型**：高层 VLM 输出意图，中层先简化为 routing+约束模块，低层用双头控制器替代单一动作头。

### 3.9 本轮补记（R584）
1. **MMaDA-VLA 更适合做低层候选，不适合替代三层解耦**：它把 future goal observation 与 action chunk 联合生成，说明 diffusion VLA 在长动作一致性上有潜力。
2. **中层仍然不可省**：即便统一生成更强，MMaDA-VLA 仍没有显式暴露语义接口、延迟状态和安全约束，因此只该作为 Paper A 的低层执行器候选。
3. **下一步实验更清楚**：把 MMaDA-VLA 放进 ACT / Diffusion Policy / Xiaomi-Robotics-0 同一低层对照表，重点比较长时序稳定性、部署延迟和 chunk 拼接误差。

### 3.10 本轮补记（R590）
1. **低层 chunk 应改成自适应，而非固定超参**：AAC 说明 inference-time chunk size 可以跟随动作熵动态调整，这比固定 8/10/16 步更符合真实部署。
2. **Paper A 低层验收需要再补 3 个指标**：除了成功率与平均延迟，还应单独看 **mode-jumping、chunk stitching stability、语义延迟场景下的恢复能力**。
3. **落地原型更明确了**：高层 VLM 输出意图，中层继续负责 latency-aware routing，低层执行器则增加一个 **entropy-guided chunk scheduler**，按当前不确定性决定开环执行长度。

### 3.11 本轮补记（R594）
1. **MMaDA-VLA 仍应定位为低层执行器候选，而不是系统替代**：它用 native discrete diffusion 统一生成 future goal observation 与 action chunk，说明低层可以把视觉前瞻直接塞进动作生成，但这并没有替代 Paper A 的显式语义接口与 latency-aware 中层。
2. **低层候选表需要再补 2 个硬指标**：除已有成功率、延迟、轨迹平滑度外，后续还应单独比较 **long-horizon consistency** 和 **future-observation conditioning 对恢复能力的增益**。
3. **实验分工更清楚了**：MMaDA-VLA 适合放进 ACT / Diffusion Policy / Xiaomi-Robotics-0 同一低层对照表，重点看它在长动作一致性上是否真能换来比显式中层更大的收益。

### 3.12 本轮补记（R599）
1. **低层执行器不只要调动作长度，还要动态调算力深度**：A1 和 AC^2-VLA 说明 VLA 实时化正在从固定压缩转向 **上下文感知 + 预算感知** 的自适应计算。
2. **Paper A 可新增双调度结构**：在已有 `entropy-guided chunk scheduler` 之外，再补一个 **action-consistency early-exit / compute scheduler**，按当前风险和一致性决定是否继续深层推理或更多 denoising。
3. **中层接口可再加 1 个输入**：除了 intent / latency metadata，还应传递 **compute budget / risk budget**，让低层在高负载或高风险时选择“更快但保守”或“更慢但更稳”的执行模式。
4. **验收指标需要再补 2 项**：后续除成功率、延迟、平滑度外，还应单独记录 **单位 episode 计算开销** 与 **early-exit 触发率下的性能退化曲线**。

### 3.13 本轮补记（R602）
1. **MMaDA-VLA 的价值更明确地落在低层 diffusion 执行器**：它把 **future goal observation + action chunk** 放进统一 discrete diffusion 骨架并行生成，用 iterative denoising 改善长时序一致性，这对 Paper A 的低层候选很有吸引力。
2. **统一生成不等于中层可省**：MMaDA-VLA 依旧没有显式暴露语义接口、延迟状态与安全约束，因此最多替代“动作器”，不能替代 **显式语义接口 + latency-aware 中层 + 安全约束层**。
3. **低层对照表应再补 1 个维度**：后续除了成功率、延迟、平滑度、chunk 拼接误差外，还应单独比较 **future-observation conditioning 对长时序恢复能力的增益**。
4. **下一步实验建议**：把 MMaDA-VLA 与 ACT / Diffusion Policy / Xiaomi-Robotics-0 放进同一低层对照表，重点看它是否真的能用视觉前瞻换来更稳的长动作执行，而不是只在离线 benchmark 上更好看。

### 3.14 本轮补记（R605）
1. **MMaDA-VLA 的工程定位更清楚了**：结合公开代码，它明显走的是 **Open-X Embodiment 预训练 → CALVIN / LIBERO 微调** 的大规模统一训练路线，常用 `action_chunk_size` 为 5/10，更像“强离线低层动作器平台”而不是直接可部署的小模型。
2. **低层候选表要再补 1 个现实维度**：后续除了成功率、延迟、平滑度、恢复能力，还应单独比较 **训练资源需求 / 微调成本 / 推理服务化复杂度**，否则容易高估统一 diffusion 路线的落地性价比。
3. **Paper A 的中层价值反而更稳了**：即便 MMaDA-VLA 在离线 benchmark 上很强，它仍没有消掉显式语义接口、latency-aware routing 和安全约束层的必要性，说明三层解耦不是“性能不够时的妥协”，而是部署导向系统设计本身需要。

### 3.15 本轮补记（R607）
1. **预测型低层动作器需要外置校验壳层**：MMaDA-VLA 把 future observation 与 action chunk 绑得很紧，这对长动作一致性有吸引力，但它仍没有显式暴露 verifier / risk-aware scheduler 接口。
2. **Paper A 的更优接法清楚了**：如果后续采用这类统一 diffusion 动作器，更合理的方式不是让它吞掉更多高层语义，而是把它包在 **中层校验器 + chunk/compute 调度器** 外面，当成“预测型低层执行器”。
3. **实验表要再补 1 个问题**：除了看恢复能力和推理成本，还应单独比较 **外置 verifier 后的收益**，验证“强生成器 + 轻校验壳层”是否比单独堆大模型更划算。

### 3.16 本轮补记（R611）
1. **MMaDA-VLA 的下一步不该只停在“是否更强”**：当前真正缺的不是再抄一轮 benchmark，而是把它放进 **裸动作器 vs 外置 verifier + chunk/compute scheduler 壳层** 的成体系对照里。
2. **Paper A 的实验优先级更明确了**：后续若深挖 MMaDA-VLA method，首先要验证它在加入轻量校验壳层后，是否能用更少额外计算换来更稳的长时序恢复与更低的危险动作放行率。
3. **低层验收表还要补 1 个部署指标**：除了成功率、延迟、平滑度、恢复能力、推理成本，建议再单列 **unsafe-action pass-through rate**，直接衡量“强生成器 + 轻校验壳层”是否真比纯生成更值得上线。

### 3.17 本轮补记（R616）
1. **中层接口应更物理化，而不只文本化**：LaST0 说明更有效的“reason before act”不一定是 textual CoT，而可以是同时编码 **未来视觉、3D 结构、proprioception** 的 latent hint，这很适合主人后续空中平台的中层设计。
2. **异频协同最好在训练期就显式建模**：LaST0 的 heterogeneous operation frequencies 说明，低频语义层与高频控制层的关系不该只靠部署时拼装，后续原型至少要显式暴露 `intent_age / latency` 一类时间信息。
3. **轻量 verifier 壳层路线更稳了**：SV-VLA 进一步验证了 `重型低频 planner + 高频 verifier` 是现实可落地的工程结构，Paper A 的中层除意图解析外还应承担 **在线校验 / 失配检测 / 重规划触发**。
4. **下一步对照实验更清楚**：把低层候选统一放进 `裸动作器`、`动作器+verifier`、`动作器+verifier+chunk/compute scheduler` 三档实验，重点看 **unsafe-action pass-through rate、replan frequency、长时序恢复能力**。

### 3.18 本轮补记（R627）
1. **低层实时化应从“调动作长度”升级为“调动作长度+调算力深度”**：A1 说明真正高性价比的实时 VLA 不只是少预测几步，而是根据 action consistency 动态决定是否继续深层推理和更多 denoising。
2. **Paper A 可正式补一层 budget-aware compute scheduler**：除了已有 `entropy-guided chunk scheduler`，后续可新增 `compute/risk budget` 输入，让低层按场景风险在“更快但保守”和“更慢但更稳”之间切换。
3. **低层对照表需要再补 2 个部署指标**：后续除成功率、延迟、平滑度、unsafe-action pass-through rate 外，还应单独记录 **单位 episode 计算开销** 与 **early-exit 触发率下的性能退化曲线**。

### 3.19 本轮补记（R631）
1. **MMaDA-VLA 的实验价值应从“单点分数”改成“三档部署对照”**：当前更值得测的是 **裸动作器 vs 动作器+verifier vs 动作器+verifier+chunk/compute scheduler**，而不是再单独追一次 benchmark 榜单。
2. **future-observation conditioning 要单独验恢复收益**：MMaDA-VLA 把 future goal observation 直接塞进低层生成器，这个优点不能只用离线成功率判断，后续应单列 **长时序恢复增益 / 重规划后回稳速度**。
3. **部署验收再补 1 个现实指标**：除成功率、延迟、平滑度、unsafe-action pass-through rate、单位 episode 计算开销外，还应单独记录 **future-observation 带来的恢复收益是否值得额外算力**，避免“更会想象但不更划算”。

### 3.20 本轮补记（R632）
1. **draft-and-verify 路线值得正式纳入低层默认结构**：ADV 说明 diffusion 动作器先提多个 chunk，再由单次 forward verifier 重排，是一条比“无脑重规划”更省算力的低层稳健化路径。
2. **几何 critic 应单列成中层/低层之间的独立校验轴**：VGAS 证明 few-shot 和 near-miss 场景下，单靠语义 plausibility 不够，后续应补 `geometry-aware chunk critic` 来筛掉几何失配动作。
3. **Paper A 的三档实验可以升级成四档**：`裸动作器`、`动作器+语义 verifier`、`动作器+几何 critic`、`动作器+双层校验`，重点比较 **unsafe-action pass-through rate、near-miss failure rate、rerank overhead**。

### 3.21 本轮补记（R640）
1. **MMaDA-VLA 的最准定位仍是“预测型低层动作器”**：从最新摘要再确认，它的核心不是替代层次化架构，而是把 **future goal observation + action chunk** 放进同一 discrete diffusion 骨架里并行去噪，提升长时序一致性。
2. **未来观测条件化值得单列成低层实验轴**：后续不该只看 LIBERO/CALVIN 分数，而应单独比较 **future-observation conditioning 对恢复速度、长时序回稳、重规划后再收敛** 的真实收益。
3. **Paper A 的默认接法更清楚了**：把 MMaDA-VLA 放进 `动作器` 位置，外面套 **语义 verifier / geometry critic / chunk+compute scheduler**，而不是让统一 diffusion 模型直接吞掉中层语义接口与风险控制。

### 3.22 本轮补记（R657）
1. **open-loop chunk + closed-loop verification 已经成为更明确的新主线**：`Open-Loop Planning, Closed-Loop Verification` 与 `A Self-Verifying Framework for Vision-Language-Action` 都在强化同一件事，说明 Paper A 不能只把 verifier 当补丁，而应把它视为默认结构件。
2. **双层校验壳更值得继续收紧**：新结果继续支持 `语义 verifier + geometry-aware critic` 的拆层设计，后续不该只测“有没有 verifier”，还要单独比较 near-miss 失效率、rerank 开销和危险动作放行率。
3. **对主人当前原型的直接启发**：低层动作器可以继续开环吐 chunk，但必须让轻量闭环校验器高频盯住 drift / mismatch / unsafe action，并把重规划触发频率写进部署验收表。

### 3.23 本轮补记（R663）
1. **execution horizon 应从固定超参升级成在线可解释变量**：AutoHorizon 说明 flow-based VLA 的 action self-attention 可以直接近似模型当前的 predictive limit，用来决定每个 chunk 该执行多长。
2. **Paper A 的低层调度器可以再细化一层**：后续不只比较 `fixed chunk` 与 `entropy-guided chunk`，还应补 `attention-guided horizon`，单独看它是否更稳地平衡 reactivity 与 temporal smoothness。
3. **验收指标要再补 1 个更贴部署的问题**：除成功率、延迟、平滑度、unsafe-action pass-through rate 外，后续还应单列 **horizon misallocation cost**，直接量化“执行过长导致反应迟缓”与“执行过短导致抖动/拼接失稳”的代价。

### 3.24 本轮补记（R781）
1. **Paper A 的高层不该只做 task decomposition, 还应内置 reflection/recovery loop**：2604.13942 说明真正长时序稳定的关键不只是拆步骤,而是让 planner 负责记忆管理、失败校验与反思恢复。
2. **中层价值更稳了**：当 planner 与 executor 分开后, 中层就不只是 routing, 还应承担 `plan state / verification result / recovery trigger` 的状态转发,把高层反思真正落到低层执行切换上。
3. **实验表应再补 1 个闭环指标**：除成功率、延迟、安全性外, 后续还应单列 **recovery success rate**，专门衡量 verifier 发现偏航后, 系统是否能在不整局重开的情况下回到任务轨道。

## 四、实验设计
- **Baseline**: OpenVLA / π0 端到端
- **我们的方法**: 三层解耦架构
- **验证任务**: 空中抓取/放置（AirSim + 真机）
- **核心指标**: 成功率 + 延迟 + 安全违规率 + 轨迹平滑度 + 控制抖动率 + chunk 拼接误差

### 4.1 低层部署对照矩阵（R778新增）

| 档位 | 结构 | 对应参考 | 主要验证问题 |
|------|------|---------|-------------|
| **L0 裸动作器** | ACT / Diffusion / MMaDA-VLA 直接输出 chunk | OpenVLA, π0, MMaDA-VLA | 只靠强动作器能否稳住长时序执行 |
| **L1 动作器+语义 verifier** | 低频规划 + 高频语义校验 | SV-VLA, ADV | stale semantic state 下是否更少跑偏 |
| **L2 动作器+几何 critic** | 动作器外接 geometry-aware critic | VGAS | near-miss / 几何失配动作能否提前拦截 |
| **L3 动作器+双层校验+双调度** | verifier + critic + AAC/compute scheduler | AAC, A1, AutoHorizon | 在算力受限时能否兼顾实时性、平滑度、安全性 |

### 4.2 最小可验证实验

1. **E1, latency-aware 中层是否必要**
   - 对比：无 `intent_age/latency` 输入 vs 显式 latency-aware 中层
   - 指标：语义过时场景成功率、重规划触发频率、恢复时间
   - 通过门槛：高延迟场景成功率提升 ≥10%，且额外延迟可接受
2. **E2, verifier 壳层是否真能降风险**
   - 对比：L0 vs L1
   - 指标：unsafe-action pass-through rate、replan frequency、成功率
   - 通过门槛：危险动作漏放率显著下降，成功率不退化
3. **E3, geometry critic 是否值得单独保留**
   - 对比：L1 vs L2 vs L3
   - 指标：near-miss failure rate、chunk stitching stability、rerank overhead
   - 通过门槛：near-miss 失败率下降 ≥15%，且 rerank 开销不过度拉高墙钟时延
4. **E4, 自适应 chunk/compute 调度是否真比固定超参更划算**
   - 对比：固定 chunk vs AAC vs AAC+compute scheduler
   - 指标：平均延迟、轨迹平滑度、horizon misallocation cost、单位 episode 计算开销
   - 通过门槛：延迟或算力开销下降明显，且平滑度/成功率不退化
5. **E5, planner reflection 是否值得保留**
   - 对比：纯 planner→executor vs planner+reflection/recovery→executor
   - 指标：recovery success rate、重规划后回稳时间、长时序成功率
   - 通过门槛：恢复成功率显著提升，且 planner 额外开销不把整体时延拖垮

### 4.3 当前最推荐原型
- **高层**：VLM 输出任务意图与目标约束
- **中层**：latency-aware routing + 语义 verifier + 重规划触发
- **低层**：ACT / MMaDA-VLA 二选一，外接 geometry critic 与 AAC 调度器
- **底层控制**：PID/MPC 保证飞行稳定与安全约束执行

## 五、后续 TODO
- [ ] 论文 A 实验框架搭建（AirSim + VLM + 低层控制器）
- [ ] 确定 VLM backbone（Qwen-VL vs InternVL）
- [ ] 中层意图解析器的具体架构设计
- [ ] 复现 Xiaomi-Robotics-0 的异步执行 + chunk 对齐思路，评估在主人硬件上的延迟收益
- [ ] 补读 MMaDA-VLA method，判断它更适合作为低层 diffusion 执行器，还是只适合作为端到端对照基线
- [ ] 把 DAM-VLA 的 action routing 改写成“飞行头/操作头”双分支原型
- [ ] 给中层加 latency-aware 接口，验证 stale semantic state 是否能提升高延迟稳定性
- [ ] 补一层 lightweight verifier，验证“低频规划 + 高频校验”是否比纯开环 chunk 更稳
- [ ] 在 AirSim 建立轨迹平滑度 / 抖动率 / chunk 拼接误差三项验收
- [ ] 深挖队列中 MMaDA-VLA/LaST0/ManualVLA/FASTER/AIR-VLA/TIC-VLA 以及 SV-VLA 补完
- [ ] 补做 ADV / VGAS 对照，验证 `语义 verifier` 与 `geometry critic` 是否应该拆成两层校验
