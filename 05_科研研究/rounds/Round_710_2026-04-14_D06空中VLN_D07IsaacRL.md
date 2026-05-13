# R710 · D06空中VLN + D07Isaac强化学习机械臂

**时间**: 2026-04-14 21:50 (周二晚)
**轮换**: D06 + D07（上次R709为D01+D04，本轮D06优先）
**方向成熟度**: D06 ≥ 🟢（已建立论文地图，候选丰富），D07 ≥ 🔴（刚建方向，基础设施调研阶段）

---

## D06 空中视觉语言导航 — 扫描

### 新候选发现

**GRAD-NAV++** (2604.07705) — 已有记录，确认为新扫描
- **标题**: GRAD-NAV++: Vision-Language Navigation for Aerial Robots
- **作者**: Schwager 等, 2026
- **核心**: VL模型 + Gaussian Radiance Fields + 可微动力学结合，实现空中机器人导航
- **判断**: 值得关注。Gaussian radiance fields 提供 scene prior，与 AerialVLA/OnFly 的纯学习路线形成对比；可微动力学则对应 D01 的 simulator-as-physics-engine 路线。对龙虾项目的启发：可以探索"场景先验 + 轻量VL"作为 onboard VLN 的折中方案。
- **归档**: ✅ 确认入库，REPORT 可补充为「场景先验派」代表

**AerialVLN Survey** (2604.07705 同源) — 确认为新 Survey
- **核心**: 系统梳理 Aerial VLN 领域进展，重点关注 Large Vision-Language Models 集成
- **判断**: 有利于快速建立 Aerial VLN 全貌，补全 D06 论文地图的 survey 层
- **归档**: 候选，待补充摘要

### 主线判断
D06 论文地图已较完整，两个技术路线清晰：
- **路线A（纯学习派）**: AerialVLA / OnFly / UAV-Track VLA → 端到端 VLN
- **路线B（场景先验派）**: GRAD-NAV++ / UMBRELLA → scene prior + VL

本周龙虾 Demo 可重点参考路线A（OnFly onboard VLN 最成熟），路线B可作为后续鲁棒性增强备选。

---

## D07 Isaac 强化学习机械臂 — 扫描

### 新候选发现

**Zero-Shot Sim2Real RL for Occlusion-Aware Plant Manipulation** (2505.16547v3) — 🆕 新增
- **核心**: 在 Isaac Lab 环境中训练，实现零样本 sim-to-real 迁移的植物操作（嫁接/修剪）
- **判断**: 与 D07 直接相关，Isaac Lab 的标志性成果之一。核心价值：
  1. Isaac Lab 环境配置参考（task specification / reward shaping）
  2. sim-to-real gap 的实际处理方法（domain randomization / UV mapping）
- **归档**: 🆕 候选入库，重点深挖对象

**Deep RL for Robotic Manipulation under Occlusion** (2604.01142) — 🆕 新增
- **核心**: 针对遮挡场景的深度 RL 机械臂操作，强调在部分可见情况下的策略鲁棒性
- **判断**: 遮挡是无人机+机械臂联合操作的核心问题（机体遮挡 + 目标自遮挡），可作为 D07 的泛化场景设计参考
- **归档**: 🆕 候选入库

### 主线判断
D07 目前主要缺：
1. Isaac Lab 具体任务配置案例（缺乏实际 task 设计参考）
2. Isaac Lab 中 RL 算法对比（PPO vs SAC vs ACT 效果）
3. 空中机械臂的 domain gap 特殊点（飞行扰动 + 机械臂协调）

建议下一步（R711-R713）重点扫描：
- Isaac Lab 官方 benchmark 任务设计
- ACT (Action Chunking with Transformers) 在 Isaac Lab 的实现
- 空中机械臂/无人机+机械臂联合操作的 RL 研究

---

## 汇报主人（≤5句）

🦊 **R710·D06+D07轮换完成。** D06 新确认 **GRAD-NAV++**（Gaussian radiance fields + VL + 可微动力学，场景先验派代表），与 AerialVLA/OnFly 纯学习路线形成技术分支，可为龙虾 onboard VLN 提供鲁棒性备选方案。D07 方向扫描发现 **2505.16547**（Isaac Lab sim-to-real 植物操作）和 **2604.01142**（遮挡场景 RL 操纵），均为 Isaac Lab RL 的实操参考，建议优先深挖 2505.16547 的任务配置与 domain randomization 方法。🐙
