# WorldEval — World Model as Real-World Robot Policies Evaluator

- **日期**: 2026-04-10
- **论文**: WorldEval: World Model as Real-World Robot Policies Evaluator
- **链接**: https://arxiv.org/abs/2505.19017
- **方向**: D01 世界模型
- **标签**: policy evaluation, world simulator, ranking correlation, safety filter

## 一句话结论
WorldEval 的核心价值不是“再做一个更像真的视频模型”，而是把 world model 明确拉成 **部署前策略评测器 + 危险动作筛查层**，强调与真实表现的排序相关性。

## 核心贡献
1. 提出 **Policy2Vec**，让视频生成模型更稳定地跟随策略动作，提升 action-following world simulation 的可用性。
2. 构建 **WorldEval** 在线评测流程，用 world model rollout 直接比较不同 policy / checkpoint 的优劣。
3. 显示 world-model-based evaluation 与真实环境表现具有较强相关性，并可用于危险动作预筛。

## 对当前主线的启发
- D01 应继续把验收重点放在 **policy ranking correlation**，而不是只看视频逼真度。
- 对龙虾 / 空中系统，WorldEval 更适合作为 **上线前筛选器**，先筛掉明显危险或低价值策略，再进 AirSim/真机。
- 这条路线和 **WAV / WorldGym / Interactive World Simulator** 是同一支线：world model 不只是 planner，还可以是 evaluator / safety gate。

## 可落地实验点
- 做一版轻量 `WM evaluator → AirSim → 真机` 三层对照，比较策略排序是否一致。
- 单独测 **OOD 动作高估 / ID 动作低估** 问题，避免把 world model 评分直接当绝对分数。
- 给龙虾导航策略加一个“危险动作预筛”接口，先在 imagined rollout 里拦截高碰撞风险策略。

## 当前判断
适合纳入 D01 的 **评测器 / 安全筛选层** 主线，不替代 planner 或 trainer，但非常适合作为部署闭环的一环。
