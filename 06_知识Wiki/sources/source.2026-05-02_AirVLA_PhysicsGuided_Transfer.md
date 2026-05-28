---
type: "source"
tags: ["VLA架构", "空中操作", "Sim2Real", "运动控制", "多模态统一架构"]
summary: "AirVLA用physics-guided控制适配把机械臂预训练VLA迁移到空中抓放任务，显式分离「可迁移视觉表征」与「须重建飞行动力学控制层」"
origins: ["02_阅读笔记/D02_VLA/2026-04-16_AirVLA_PhysicsGuidedVLA2Aerial_2603.25038", "02_阅读笔记/D02_VLA/2026-04-16_AirVLA_PhysicsGuidedVLA2Aerial_2603.25038", "05_科研研究/D04_跨载体泛化/papers/2026-04-16_AirVLA_PhysicsGuidedVLA2Aerial_2603.25038"]
updated: "2026-05-11"
---

# AirVLA Physics-Guided Transfer (2603.25038)

**核心要点**:
- **问题**: 将固定基座机械臂预训练的 VLA（如 π₀）迁移到空中平台时，视觉表征可迁移，但动力学不兼容（"dynamics gap"：准静态 vs 欠驱动高动态飞行）。
- **方法**: Payload-Aware Guidance（推理时注入载荷约束到 flow-matching 采样过程）+ Gaussian Splatting 数据合成（解决实机数据稀缺）。
- **结果**: 导航任务合成数据从 81%→100%；拾取放置 Payload-Aware Guidance 从 23%→50%；长时序组合任务 62% 成功率。

**原始资料**:
- [[02_阅读笔记/D02_VLA/2026-04-16_AirVLA_PhysicsGuidedVLA2Aerial_2603.25038]]
- [[02_阅读笔记/D02_VLA/2026-04-16_AirVLA_PhysicsGuidedVLA2Aerial_2603.25038]]
- [[05_科研研究/D04_跨载体泛化/papers/2026-04-16_AirVLA_PhysicsGuidedVLA2Aerial_2603.25038]]
