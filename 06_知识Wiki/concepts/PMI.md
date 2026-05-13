---

type: "concept"
level: "secondary"
parent: "跨载体泛化"
tags: ["PMI"]
summary: "Perceptual-Motor Interface，主人明子原创的可验证意图接口理论"
updated: "2026-04-17"
id: "concept.PMI"
pageType: "concept"
---


# 概念：PMI (Perceptual-Motor Interface)

> Perceptual-Motor Interface，用于跨躯体具身操作的可验证意图接口。是主人提出的核心理论贡献，2026-03-26 已升级为"四层闭环 + 双状态系统"。

## 背景

现有多 VLA / generalist policy 与 embodiment、动作空间、控制接口绑得很紧，跨躯体泛化是核心难题。

## 理论升级：从三层静态分层 → 四层闭环

### 四层架构

| 层级 | 功能 | 关键能力 |
|------|------|---------|
| 1. 世界感知层 | 视觉+触觉+力觉+本体感知+历史记忆 | 包含身体自感知（body schema在线观测） |
| 2. 意图与心理模拟层 | 目标对象/关系、当前子任务、操作风格、风险偏好、预期结果 | 意识/想象/规划 |
| 3. **身体使用与适配层 ⭐** | 实时回答"这副身体能做什么、哪些部件更可靠、如何分配接触力" | Body-Usage Adaptation |
| 4. 反射与执行层 | IK/MPC/RL/impedance/torque/skill primitive | 高频低延迟 |

### 双状态系统

系统状态：
$$z_t = (z_t^{\text{intent}}, z_t^{\text{body}})$$

更新方程：
$$(z_{t+1}^{\text{intent}}, z_{t+1}^{\text{body}}) = F(z_t, o_t, a_t, o_{t+1})$$
$$a_t = \pi(z_t^{\text{intent}}, z_t^{\text{body}}, o_t)$$

**两个闭环回路：**
- **回路A（外部世界闭环）**：动作改变环境 → 更新任务判断
- **回路B（身体自我闭环）**：动作暴露能力局限 → 更新"如何用身体"参数

## 三个推荐研究方向

| 方向 | 说明 | 推荐度 |
|------|------|--------|
| A1：Body-Usage Adapter | 高层意图 + 视觉/触觉反馈 → 实时调节身体使用参数 | ⭐⭐⭐ |
| A2：PMI + Capability Verification | 意图 → Body-Usage Adapter → 可行性验证 → 执行 | ⭐⭐ |
| A3：触觉驱动的意图修正 | 触觉显示接触不稳 → 自动修正意图参数 | ⭐⭐ |

## 相关子概念

- [[concepts/VLA架构|VLA]] - VLM-based 高层策略
- [[concepts/具身智能|具身智能]] - 跨躯体迁移
- [[concepts/力-触融合|力-触融合]] - 触觉感知是身体使用参数更新的关键输入
- [[concepts/任务与运动规划|任务与运动规划]] - 高层规划与低层执行的接口

---
**通过 Obsidian Backlinks 自动建立双向链接，无需手动维护。**
