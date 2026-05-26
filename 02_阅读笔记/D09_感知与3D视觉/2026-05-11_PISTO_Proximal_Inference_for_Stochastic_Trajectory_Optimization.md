---

title: "PISTO: Proximal Inference for Stochastic Trajectory Optimization"
authors: Hongzhe Yu, Zinuo Chang, Yongxin Chen
arxiv: 2605.07215
date: 2026-05-08
institution: Georgia Tech
conf: arXiv
keywords: [trajectory optimization, STOMP, variational inference, proximal update, robot planning]
tags: [最优控制, 任务与运动规划, 强化学习, 运动控制]
domain: 规划与控制
pdf_path: "../../01_论文库/规划与控制/2605.07215_PISTO.pdf"
reading_date: 2026-05-11
reading_status: 已读
related_concepts: ["最优控制", "任务与运动规划", "强化学习", "运动控制"]
---

# 📖 花火格式笔记

## 🎯 题目

PISTO: Proximal Inference for Stochastic Trajectory Optimization

## 📝 三句摘要

1. **问题背景**：STOMP 这类随机轨迹优化虽然能处理不可微和不连续代价，但更新不够稳定，常在样本效率和轨迹质量上吃亏。
2. **核心方法**：论文把 STOMP 重新解释为对 Boltzmann 轨迹分布做变分推断，并进一步提出带相邻 proposal KL 正则的 PISTO，用 proximal / trust-region 形式稳定 Gaussian proposal 更新。
3. **关键结果**：PISTO 在机械臂运动规划上达到 89% 成功率，优于 CHOMP 的 63% 和 STOMP 的 68%，同时路径更短更平滑，且在接触丰富的 locomotion 与 manipulation 任务中也持续胜过 CEM、MPPI。

## 💎 价值评估

- **🔬 研究价值**：它把经典随机轨迹优化和变分推断连接起来，给 STOMP 一条更“可解释且可扩展”的理论升级路线。
- **🚀 实践价值**：主人若做非光滑代价、接触丰富任务或需要快速替换 reward/cost 定义，PISTO 这种 derivative-free 但更稳的 planner 很实用。
- **📈 扩展潜力**：能往 MPC、task-motion planning，甚至和 learned world model 结合成 planning-time trust-region 更新继续推。

## 🎯 可落地实验点

**实验设计**：把 PISTO 接到现有接触丰富操作/导航环境里，比较其在不可微惩罚和障碍约束下对规划成功率与轨迹平滑性的提升。
- 对比基线：STOMP、MPPI、CEM、梯度型 trajectory optimizer
- 度量指标：规划成功率、轨迹长度、平滑度、单次规划时间、对代价函数不连续性的鲁棒性
- 预期结果：PISTO 会在非光滑代价和接触场景里表现得更稳，尤其适合需要快速切换任务成本定义的实验

## 🔗 知识图谱

- [[最优控制]] - 把随机轨迹优化与变分推断统一到优化视角下
- [[任务与运动规划]] - 直接服务于机器人 motion planning 任务
- [[强化学习]] - 在 locomotion/manipulation reward 优化实验中与采样型 RL 基线相邻
- [[运动控制]] - 结果可直接影响控制可执行轨迹质量

## 🔗 相关链接

- [[2026-05-11_Dream-MPC]] - 都在讨论 planning-time optimization 与可执行控制之间的接口
- [[2026-05-11_CineMPC]] - 同属 MPC / trajectory optimization 路线，可对比实时性与代价建模能力
- [[2026-05-11_OA-WAM_Object-Addressable_World_Action_Model_for_Robust_Robot_Manipulation]] - 可作为 learned world model + classical planner 的潜在组合方向

## 📌 待探索问题

- PISTO 的 proximal KL 约束在高维长时域 planning 里是否仍然稳定，还是会出现 proposal 过早收缩？
- 如果把 learned world model 的 rollout uncertainty 纳入 surrogate distribution，PISTO 能否自然升级成 uncertainty-aware planner？

---
**维护**: 花火 · 2026-05-11
