---
type: "source"
id: "source.2605.28615_PrimitiveVLA"
pageType: "source"
tags: ["VLA架构", "ACT动作分块", "模仿学习", "长程任务规划", "多模态统一架构"]
summary: "PrimitiveVLA 用 Multimodal Canonical Representation 把示范拆成可复用动作原语，再由 VLM planner + LLM switch 动态组装执行，显著提升数据效率与长程/未见任务泛化。"
origins: ["../02_阅读笔记/01_机器人与具身/2026-05-28_2605.28615_PrimitiveVLA.md"]
updated: "2026-05-28 14:20"
---

# PrimitiveVLA (2605.28615)

**核心要点**:
- **动作原语拆解**: 用 Multimodal Canonical Representation 把示范轨迹自动拆成可复用动作原语，而非整段轨迹记忆
- **动态组装执行**: VLM planner + LLM switch 模块在推理时闭环组装原语，支撑长程任务执行与纠错重规划
- **数据效率提升**: primitive-centric 范式显著优于直接 instruction-to-control VLA，适合数据有限场景

**与我们的关系**:
- D02 VLA架构方向，primitive 库思路可与主人关注的 ACT/动作分块路线结合
- 可落地实验：动作原语库 + planner-switch 组装 vs 整轨迹模仿，在未见组合任务上验证泛化提升

**原始资料**:
- [[02_阅读笔记/01_机器人与具身/2026-05-28_2605.28615_PrimitiveVLA]]
