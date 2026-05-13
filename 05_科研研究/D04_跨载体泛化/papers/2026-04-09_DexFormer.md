# DexFormer: Cross-Embodied Dexterous Manipulation via History-Conditioned Transformer

> **arXiv**: 2602.08278 | **方向**: D04_跨载体泛化 | **深挖时间**: 2026-04-09 R562 | **状态**: ✅ 摘要级入库

## 一句话与本方向关系
DexFormer 证明跨载体策略不一定非要显式输入 morphology id，也可以依靠历史观测在时序 transformer 中在线推断不同手型/动力学差异，实现零样本跨灵巧手泛化。

## 核心贡献
1. **History-conditioned transformer**：利用历史观测而非单帧输入，在线推断 embodiment 差异
2. **Dynamics-aware cross-embodiment policy**：同时适配不同灵巧手的运动学与动力学，不依赖每个本体单独 decoder head
3. **Procedural dexterous-hand assets**：在多种程序化手型资产上训练，获得可迁移的 manipulation prior
4. **Zero-shot transfer**：对 Leap Hand、Allegro Hand、Rapid Hand 展现零样本迁移能力

## 技术路线
```text
历史观测序列
  → transformer 编码时序上下文
  → 隐式推断 morphology + dynamics
  → 输出 embodiment-appropriate control
```

## 可借鉴的技术点
1. **隐式本体识别**：不一定要显式输入 morphology token，可把“识别当前本体”交给时序模型自己完成
2. **history as embodiment signal**：跨载体差异不只在结构参数，也体现在同一动作下的动态响应轨迹中
3. **适合作为对照基线**：后续主人做异构末端执行器/空中机械臂共享策略时，可把它作为“implicit inference”路线，对照 CEI/SoftAct/Embedding Morphology 这类显式结构先验路线

## 局限/不足
1. **偏灵巧手场景**：当前验证更集中在高自由度手部操作，离空中机械臂/跨平台移动操作还有距离
2. **依赖历史窗口**：如果实时约束很紧，长历史输入会增加时延和工程复杂度
3. **隐式推断可解释性弱**：相比显式 morphology token，难分析模型到底学到了什么 embodiment 结构

## 对主人当前课题的启发
- D04 后续不应只比较“统一接口”与“显式 morphology-aware backbone”，还可以补一条 **history-conditioned implicit embodiment inference** 路线
- 若主人后续做空中机械臂/异构夹爪共享策略，可先用 DexFormer 式思路做 baseline，再决定是否需要显式 morphology token 或功能接口层