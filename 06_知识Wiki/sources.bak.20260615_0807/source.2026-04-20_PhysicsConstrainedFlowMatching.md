---
type: "source"
id: "source.2026-04-20_PhysicsConstrainedFlowMatching"
pageType: "source"
tags: ["流匹配", "物理约束", "反问题", "PDE", "AI for Science", "无监督微调"]
summary: "DFKI 联合帝国理工提出物理约束的流匹配微调框架，**无需成对训练数据**，通过引入弱形式 PDE 残差作为引导信号，让生成模型在采样过程中严格遵守物理法则。框架同时解决正问题（生成物理一致样本）和反问题（从观测逆推隐藏物理参数），在单张 NVIDIA L40S 上微调仅需 **15 分钟**。物理残差断崖式下降，精度和样本多样性全面碾压传统基线，为 AI for Science 方向提供了无标"
origins: ["../../02_阅读笔记/D01_世界模型/2026-04-20_PhysicsConstrainedFlowMatching.md"]
updated: "2026-06-02"
---

# **Physics-Constrained Fine-Tuning of Flow-Matching Models for Generation and Inverse Problems**

**核心价值**: DFKI 联合帝国理工提出物理约束的流匹配微调框架，**无需成对训练数据**，通过引入弱形式 PDE 残差作为引导信号，让生成模型在采样过程中严格遵守物理法则。框架同时解决正问题（生成物理一致样本）和反问题（从观测逆推隐藏物理参数），在单张 NVIDIA L40S 上微调仅需 **15 分钟**。物理残差断崖式下降，精度和样本多样性全面碾压传统基线，为 AI for Science 方向提供了无标

**原始资料**:
- [[../../02_阅读笔记/D01_世界模型/2026-04-20_PhysicsConstrainedFlowMatching.md]]
