---
type: "source"
id: "source.2408.00415_DriveArena"
pageType: "source"
tags: ["Closed-loop simulation", "Generative model", "Autonomous driving", "World model", "仿真平台", "数据飞轮"]
summary: "驾驶智能体在真实场景中评测缺乏可控、可复现的闭环仿真平台，现有方法难以生成无限自动驾驶场景。 DriveArena 采用模块化架构，Traffic Manager 生成真实交通流，World Dreamer（条件生成模型）生成逼真图像，智能体输出轨迹后被 Traffic Manager 处理，生成新场景布局再传回 World Dreamer，实现闭环迭代。 任意能处理真实图像的驾驶智能体都能在 DriveArena 中导航；支持在不同城市街道图上生成多样化交通流，实现真实感交互。"
origins: ["../../02_阅读笔记/D01_世界模型/2026-04-18_DriveArena.md"]
updated: "2026-06-02"
---

# DriveArena: A Closed-loop Generative Simulation Platform for Autonomous Driving

**核心价值**: 驾驶智能体在真实场景中评测缺乏可控、可复现的闭环仿真平台，现有方法难以生成无限自动驾驶场景。 DriveArena 采用模块化架构，Traffic Manager 生成真实交通流，World Dreamer（条件生成模型）生成逼真图像，智能体输出轨迹后被 Traffic Manager 处理，生成新场景布局再传回 World Dreamer，实现闭环迭代。 任意能处理真实图像的驾驶智能体都能在 DriveArena 中导航；支持在不同城市街道图上生成多样化交通流，实现真实感交互。

**原始资料**:
- [[../../02_阅读笔记/D01_世界模型/2026-04-18_DriveArena.md]]
