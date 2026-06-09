---
type: "source"
id: "source.2601.20668_GPO"
pageType: "source"
tags: ["legged robot", "whole-body control", "reinforcement learning", "torque control", "zero-shot deployment", "强化学习"]
summary: "腿足机器人在 torque-based control 下做强化学习很难，动作维度高、探索信号弱，而且传统 reward shaping 和课程设计往往强依赖具体环境。 GPO 提出一种随训练时间变化的动作变换，先在早期收缩有效动作空间提升采样效率，再逐步放开动作范围，让 PPO 在保持稳定梯度的同时获得更强探索能力。 论文在四足和六足平台上都取得更好性能，并完成 sim-to-real zero-shot 上机，说明它更像一种环境无关的优化框架，而不只是某个任务特化技巧。"
origins: ["../../02_阅读笔记/D07_强化学习与控制/2026-04-21_2601.20668_GPO.md", "02_阅读笔记/D07_强化学习与控制/2026-04-21_2601.20668_GPO.md"]
updated: "2026-06-02"
---

# source.2601.20668_GPO

**核心价值**: 腿足机器人在 torque-based control 下做强化学习很难，动作维度高、探索信号弱，而且传统 reward shaping 和课程设计往往强依赖具体环境。 GPO 提出一种随训练时间变化的动作变换，先在早期收缩有效动作空间提升采样效率，再逐步放开动作范围，让 PPO 在保持稳定梯度的同时获得更强探索能力。 论文在四足和六足平台上都取得更好性能，并完成 sim-to-real zero-shot 上机，说明它更像一种环境无关的优化框架，而不只是某个任务特化技巧。

**原始资料**:
- [[../../02_阅读笔记/D07_强化学习与控制/2026-04-21_2601.20668_GPO.md]]
- [[02_阅读笔记/D07_强化学习与控制/2026-04-21_2601.20668_GPO.md]]
