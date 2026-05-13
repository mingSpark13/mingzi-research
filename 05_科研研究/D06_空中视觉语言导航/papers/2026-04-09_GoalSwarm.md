# GoalSwarm: Multi-UAV Semantic Coordination for Open-Vocabulary Object Navigation

- **arXiv**: 2603.12908
- **方向**: D06 空中视觉语言导航
- **阅读深度**: 摘要级深挖（待全文复核）
- **时间**: 2026-04-09 R545

## 与本方向的关系
这篇更像龙虾 GoalSearch 的“多机协同扩展版”。它关注的不是传统封闭类别导航，而是 **open-vocabulary object-goal navigation**，并且把多无人机协同搜索、轻量语义建图和不确定性探索放到同一套去中心化框架里，对后续多机搜索、协同巡检、分布式语义探索都有直接参考价值。

## 摘要级核心结论
1. GoalSwarm 用 **轻量 2D top-down semantic occupancy map** 代替完整 3D 表示，降低多机协同搜索的机载计算压力。
2. 它把多视角检测置信度融合成 **Bayesian Value Map**，再用 **UCB frontier exploration** 做前沿评分，兼顾目标相关性与探索不确定性。
3. 任务分配上采用 **去中心化 coordination + cost-utility bidding + spatial separation penalty**，减少多机重复搜索。

## 可借鉴的技术点
- **Bayesian Value Map**：适合接到主人现有目标搜索链路后，作为“发现概率热图”中层表示，而不是只靠单帧检测结果决定移动。
- **UCB frontier scoring**：能把“看起来像目标的地方”和“信息增益高的地方”统一到一个探索分数，适合长时搜索任务。
- **多机协同接口**：虽然主人当前重点是单机龙虾，但这篇可提前定义未来多机版本的消息接口和区域分工逻辑。

## 局限 / 不足
- 当前框架核心仍是 **2D 俯视语义地图**，对 6-DoF 空中机动、俯仰视角变化和动力学约束处理不够强。
- 更偏 **semantic object-goal navigation**，语言长程推理链条没有 AirNav / APEX 那么完整。
- 多机协同价值很高，但对当前单机 DDL 4/10 的龙虾项目只是次主线参考，不是最直接可落地主骨架。

## 对主人的落地启发
1. 单机版本可先借它的 **Bayesian Value Map + frontier scoring**，把“检测到目标”和“值得继续探索”分开建模。
2. 若后续做多龙虾协同，可把 GoalSwarm 的 **bidding + spatial separation** 直接改成任务分区和去重搜索机制。
3. 对当前项目，最现实的吸收方式不是整套照搬，而是先把 **热图记忆 + 不确定性探索** 抽成中层模块。 
