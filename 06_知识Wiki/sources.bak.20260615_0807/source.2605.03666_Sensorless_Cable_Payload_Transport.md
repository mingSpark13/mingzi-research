---
type: "source"
id: "source.2605.03666_Sensorless_Cable_Payload_Transport"
pageType: "source"
tags: ["aerial manipulation", "cable-suspended payload", "quadrotor", "NMPC", "state estimation", "空中操作"]
summary: "四旋翼吊运绳悬载荷时常依赖额外载荷传感器或不完整动力学模型，导致真实部署复杂、误差大、难以做激进机动运输。 论文用 Udwadia-Kalaba 约束动力学显式建模缆绳几何约束，把张力直接并入 NMPC 预测模型，并基于同一几何约束提出无载荷传感器的状态估计器。 真实机器人实验表明，显式纳入载荷动力学与 sensorless state estimation 后，轨迹跟踪误差和整体运输性能都优于不完整模型策略。"
origins: ["../../02_阅读笔记/D03_空地迁移/2026-05-06_2605.03666_Sensorless_Cable_Payload_Transport.md", "02_阅读笔记/D03_空地迁移/2026-05-06_2605.03666_Sensorless_Cable_Payload_Transport.md"]
updated: "2026-06-02"
---

# source.2605.03666_Sensorless_Cable_Payload_Transport

**核心价值**: 四旋翼吊运绳悬载荷时常依赖额外载荷传感器或不完整动力学模型，导致真实部署复杂、误差大、难以做激进机动运输。 论文用 Udwadia-Kalaba 约束动力学显式建模缆绳几何约束，把张力直接并入 NMPC 预测模型，并基于同一几何约束提出无载荷传感器的状态估计器。 真实机器人实验表明，显式纳入载荷动力学与 sensorless state estimation 后，轨迹跟踪误差和整体运输性能都优于不完整模型策略。

**原始资料**:
- [[../../02_阅读笔记/D03_空地迁移/2026-05-06_2605.03666_Sensorless_Cable_Payload_Transport.md]]
- [[02_阅读笔记/D03_空地迁移/2026-05-06_2605.03666_Sensorless_Cable_Payload_Transport.md]]
