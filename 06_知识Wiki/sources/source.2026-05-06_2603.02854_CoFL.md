---
type: "source"
id: "source.2026-05-06_2603.02854_CoFL"
pageType: "source"
tags: ["language-conditioned navigation", "flow field", "BEV", "real-time policy", "semantic maps", "语义导航"]
summary: "传统语言导航常把指令转成单条轨迹或离散 waypoint，监督稀疏、泛化差，还容易牺牲实时性与安全性。 CoFL 把导航改写成条件连续流场学习，用 BEV 观察和语言指令直接预测任意位置的局部运动向量，让单条示例变成稠密空间控制监督。 在未见场景上，CoFL 相比模块化 VLM planner 和轨迹生成策略，在导航精度、安全性和实时性上都更强。"
origins: ["../../02_阅读笔记/D06_空中VLN/2026-05-06_2603.02854_CoFL.md", "../../02_阅读笔记/D06_空中VLN/2026-05-06_2603.02854_CoFL.md"]
updated: "2026-06-02"
---

# CoFL: Continuous Flow Fields for Language-Conditioned Navigation (2603.02854)

**核心价值**: 传统语言导航常把指令转成单条轨迹或离散 waypoint，监督稀疏、泛化差，还容易牺牲实时性与安全性。 CoFL 把导航改写成条件连续流场学习，用 BEV 观察和语言指令直接预测任意位置的局部运动向量，让单条示例变成稠密空间控制监督。 在未见场景上，CoFL 相比模块化 VLM planner 和轨迹生成策略，在导航精度、安全性和实时性上都更强。

**原始资料**:
- [[../../02_阅读笔记/D06_空中VLN/2026-05-06_2603.02854_CoFL.md]]
- [[02_阅读笔记/D06_空中VLN/2026-05-06_2603.02854_CoFL.md]]
