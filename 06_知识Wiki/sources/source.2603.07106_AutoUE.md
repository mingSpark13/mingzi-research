---
type: "source"
id: "source.2603.07106_AutoUE"
pageType: "source"
tags: ["程序化内容生成", "多智能体系统", "仿真平台"]
summary: "多Agent协作框架（检索+场景生成+代码+playtesting），从自然语言生成可玩游戏关卡，端到端自动化生成"
origins: ["../02_阅读笔记/数据合成/2603.07106_AutoUE.md"]
updated: "2026-05-28 14:44"
---

# AutoUE (2603.07106)

**核心要点**:
- **四Agent流水线**: 检索Agent（858K 3D模型库选资产）→场景生成Agent（UE PCG layout graph）→代码Agent（玩法逻辑）→playtesting Agent（验证）
- **多Agent协作**: 验证了多Agent在复杂工程系统（UE）中的可行性，分离设计模式可迁移
- **端到端生成**: 从自然语言描述→可玩游戏关卡，完整验证了生成式工程系统的可行性

**与我们的关系**:
- D05数据合成方向，多Agent生成流水线的工程化参考
- 可扩展为「低空场景检索+PCG生成+飞控验证+轨迹采集」四Agent流水线

**原始资料**:
- [[02_阅读笔记/数据合成/2603.07106_AutoUE]]
