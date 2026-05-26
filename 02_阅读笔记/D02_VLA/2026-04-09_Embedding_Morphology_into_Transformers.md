# Embedding Morphology into Transformers for Cross-Robot Policy Learning

> **arXiv**: 2603.00182 | **方向**: D04_跨载体泛化 | **深挖时间**: 2026-04-09 R564 | **状态**: ✅ 摘要级入库

## 一句话与本方向关系
这篇工作把 morphology 从“后处理补偿项”前移成 transformer 结构里的显式条件，说明跨载体策略不该一味追求 embodiment-agnostic，而应把本体先验直接写进 backbone。

## 核心贡献
1. **Morphology token / attribute conditioning**：将关节属性、运动学结构等形态信息作为条件输入策略模型。
2. **Topology-aware attention bias**：把机器人拓扑关系编码进注意力偏置，减轻模型从原始观测里硬猜本体结构的负担。
3. **Single-policy cross-robot learning**：目标是在多个 embodiment 上训练一套统一策略，而不是每个机器人各训一套。
4. **Robustness gain across embodiments**：搜索结果与摘要都指向一个结论，显式 morphology prior 能提升跨机器人鲁棒性与泛化稳定性。

## 技术路线
```text
观测序列 + 任务条件
  + morphology attributes / kinematic structure
  + topology-aware attention bias
  → transformer policy
  → embodiment-aware action output
```

## 可借鉴的技术点
1. **形态先验前置**：本体差异应尽早进入 backbone，而不是只留给 retargeting。
2. **结构偏置可解释**：相比纯黑盒隐式适配，topology-aware attention 更方便做误差归因。
3. **适合作为 D04 主线对照**：后续可与 CEI/SoftAct 的功能接口路线、DexFormer 的隐式本体推断路线做三线对照。

## 局限 / 不足
1. **仍需结构元数据**：如果真实系统里 morphology 描述不完整，落地成本会上升。
2. **更偏同任务跨本体**：跨任务泛化能力可能仍受限于训练分布。
3. **摘要级结论为主**：当前 heartbeat 受抓取限制，后续需全文复核实验设定与指标。

## 对主人的落地启发
- D04 当前判断进一步收敛为：**接口层与 morphology-aware backbone 应并行设计**。
- 若主人后续做空中机械臂 / 异构末端执行器共享策略，这篇很适合作为“显式形态先验”基线。
- 和 DexFormer 配对后，刚好形成“显式 morphology conditioning vs 隐式 history inference”的强对照框架。
