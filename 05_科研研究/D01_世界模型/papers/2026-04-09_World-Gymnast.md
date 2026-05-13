# World-Gymnast — Training Robots with Reinforcement Learning in a World Model

- **论文**: World-Gymnast: Training Robots with Reinforcement Learning in a World Model
- **arXiv**: 2602.02454
- **日期**: 2026-04-09
- **方向**: D01_世界模型
- **状态**: 已深挖

## 这篇在讲什么
它把动作条件视频世界模型直接当成 RL 训练环境来用。策略不在软件模拟器里训，而是在 learned world model 里 rollout，再由 VLM 对 imagined video 打分，最后反向更新 VLA policy。

## 方法与实验要点
1. **训练闭环**
   - VLA policy 输出动作。
   - 动作送进 action-conditioned video world model，生成 imagined rollout。
   - VLM 根据任务指令判断 rollout 是否成功，给奖励。
   - 用 **GRPO** 做 policy update。
2. **不是只在分布内微调**
   - 支持 novel instruction、novel scene、test-time training。
   - 还能把真实机器人新 rollout 继续回灌 world model，形成 online iterative improvement。
3. **关键结果**
   - 真机 AutoEval 上，`put eggplant into blue sink` 从 **4% → 72%**。
   - `put eggplant into yellow basket` 从 **8% → 78%**。
   - 对比 SIMPLER 软件模拟器，4 个任务里 3 个明显更强。
   - 说明 world model 不只是“辅助看视频”，而是真能承担策略训练器角色。

## 与本方向的关系
这篇把 D01 从“世界模型做预测 / 做规划”进一步推进到“世界模型做训练器”。它直接回答了一个很关键的问题, 即 learned world model 能不能替代部分真实交互和传统 simulator 来优化策略。

## 可借鉴的技术点
1. **world model as trainer**
   - 后续主人做 D01 / D06，不必只把世界模型当 planner，也可以把它当 RL 训练环境。
2. **VLM reward 很适合语义任务**
   - 对“找目标、放到指定位置、语义导航”这类任务，VLM judge 比手写 reward 更快起步。
3. **真实 rollout 回灌 world model**
   - 这和 D05 数据飞轮天然闭环，意味着训练器本身也能持续变强。

## 局限 / 不足
1. 依赖 imagined rollout 质量，如果世界模型 hallucination 严重，RL 可能学会利用模型漏洞。
2. 奖励来自 VLM judge，仍可能存在误判与 reward hacking 风险。
3. 当前验证集中在 Bridge 桌面操作，尚未覆盖主人更关心的空中长程导航与空中操作。

## 对主人的启发
1. 龙虾项目后续可以尝试“世界模型小步 RL 微调”而不是只靠 imitation learning。
2. 如果 D01 要继续往论文方向推，世界模型的角色可以从 planner 扩成 **planner + trainer**。
3. 真正的关键不只是 world model 能不能生成像样视频，而是它能不能提升真实任务成功率。World-Gymnast 给了很强的正例。

## 可落地实验点
- 先做一个轻量原型：
  1. 用现有导航 / 操作 policy 生成 imagined rollout。
  2. 用 VLM 或成功判别器给奖励。
  3. 小步 RL finetune。
  4. 对比“纯 SFT / 纯仿真 RL / world-model RL”三条线。
- 若 rollout 漂移明显，再补 WoVR 式关键帧回锚机制。