---
type: "source"
tags: []
summary: "- **Training-free agent system**: 不重新训练整套导航模型，而是把 foundation model 与低层控制网络编排成可执行系统。"
origins: ["02_阅读笔记/05_语义导航/2026-04-09_QuadAgent"]
updated: "2026-04-17"
---

# QuadAgent_2604.02786

**核心要点**:
- **Training-free agent system**: 不重新训练整套导航模型，而是把 foundation model 与低层控制网络编排成可执行系统。
- **异步多 agent 架构**: Foreground Workflow Agents 负责当前任务与用户指令，Background Agents 负责 look-ahead reasoning。
- **Impression Graph**: 用稀疏关键帧维护轻量拓扑场景记忆，支持环境推理与响应式导航。

**与我们的关系**:
- 1. **异步执行栈**：把“现在要做什么”和“下一步可能发生什么”拆开，对空中平台很适合降低高层推理阻塞。
- 2. **关键帧拓扑记忆**：比全量 dense map 更轻，适合机载计算受限场景。
- 3. **系统工程价值大于新 backbone 价值**：对主人现在的 GoalSearch，更像运行时编排参考，而不是替换 APEX/AirNav 主线的论文骨架。

**原始资料**:
- [[02_阅读笔记/05_语义导航/2026-04-09_QuadAgent]]
