---
type: "source"
id: "source.2026-03-26_DreamZero_World_Action_Models_are_Zero-shot_Policies"
pageType: "source"
tags: ["DreamZero", "World Action Model", "Zero-shot Policy", "Video Model", "Robot Policy", "D01"]
summary: "DreamZero 把机器人策略学习重新表述为 **World Action Model (WAM)**：模型同时预测未来视频和动作，而不是只输出动作 token。 核心观点是：如果视频生成骨干已经学会了世界动态，那么在动作条件下它天然可以承担零样本策略的角色，从而在未见任务上直接执行。 论文与开源项目都强调 DreamZero 在 DROID 等基准上具有很强 zero-shot 表现，并说明视频模型骨干不只是“会生成视频”，而是可以转化为可执行机器人策略。"
origins: ["../../02_阅读笔记/D01_世界模型/2026-03-26_DreamZero_World_Action_Models_are_Zero-shot_Policies.md"]
updated: "2026-06-02"
---

# ViSA-Enhanced AVLN (2603.08007)

**核心价值**: DreamZero 把机器人策略学习重新表述为 **World Action Model (WAM)**：模型同时预测未来视频和动作，而不是只输出动作 token。 核心观点是：如果视频生成骨干已经学会了世界动态，那么在动作条件下它天然可以承担零样本策略的角色，从而在未见任务上直接执行。 论文与开源项目都强调 DreamZero 在 DROID 等基准上具有很强 zero-shot 表现，并说明视频模型骨干不只是“会生成视频”，而是可以转化为可执行机器人策略。

**原始资料**:
- [[../../02_阅读笔记/D01_世界模型/2026-03-26_DreamZero_World_Action_Models_are_Zero-shot_Policies.md]]
