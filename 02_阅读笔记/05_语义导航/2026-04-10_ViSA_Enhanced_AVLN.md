# ViSA-Enhanced Aerial Vision-Language Navigation

- **标题**: A Visual-Spatial Reasoning Enhanced Framework for Aerial Vision-Language Navigation
- **arXiv**: 2603.08007
- **日期**: 2026-03-09
- **定位**: D06 空中视觉语言导航，适合作为轻量前端推理增强层，而非主骨架替代

## 这篇在做什么
作者指出，现有 aerial VLN 常把开放词汇检测结果转成离散文本场景图，但这样会丢空间关系且容易产生语言歧义。ViSA 提出一个 **triple-phase collaborative architecture**，通过 **structured visual prompting** 让 VLM 直接在图像平面上做视觉-空间推理，不依赖额外训练，也不强依赖复杂中间表示。

## 核心贡献
1. **直接图像平面推理**：不先压成离散 scene graph，而是保留视觉几何关系给 VLM 直接判断。
2. **结构化视觉提示**：把目标、候选区域、空间关系组织成 prompt，增强空间定位能力。
3. **训练自由（training-free）增强**：更像给现有 aerial VLN/explorer 补一个 reasoning 前端，而不是重训整套控制器。
4. **CityNav 上显著提升**：摘要声称相对已训练 SOTA 方法成功率提升 70.3%。

## 与本方向的关系
它补的是 **“看懂当前画面里哪里更像目标、空间关系是否成立”** 这一层，适合作为 D06 里显式 explorer / frontier 主线的前端增强模块。

## 可借鉴技术点
- 把 **structured visual prompting** 作为龙虾 GoalSearch 当前 VLM 前端的可插拔增强层
- 用于比较 **image-plane reasoning** 与 **显式 3D 前沿图 / 语义地图** 哪种更稳
- 可作为 **低改造成本 baseline**，验证“不改控制器，只补 reasoning 前端”能拿到多少增益

## 局限 / 不足
- 重点仍在 **视觉-空间推理增强**，对开放式长程搜索、显式记忆、重规划恢复覆盖有限
- 训练自由意味着工程接入轻，但通常也受限于 VLM 前端稳定性与 prompt 设计
- 摘要里的大幅增益来自 CityNav，是否能迁移到主人当前 **开放词汇目标搜索 + 连续飞行控制** 场景，还得单独验收

## 对龙虾 GoalSearch 的直接启发
优先把它放在 **“显式 explorer 不变，只在候选视图打分前加一层视觉空间推理”** 的实验位，而不是替换 APEX + AirNav 主骨架。

## 建议实验位
1. Baseline: 现有 explorer + 原始 VLM 打分
2. ViSA-lite: explorer + structured visual prompting
3. Full map route: explorer + 3D VL-frontier map
4. 对比指标：开放式搜索成功率、误检率、重规划恢复率、推理时延
