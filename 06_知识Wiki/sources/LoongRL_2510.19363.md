---
type: "source"
id: "source.LoongRL_2510.19363"
pageType: "source"
tags: ["reinforcement learning", "long-context reasoning", "multi-hop QA", "retrieval-augmented reasoning", "强化学习"]
summary: "现有RL方法通过CoT提升短上下文推理，但长上下文推理需要同时具备检索和推理能力，且高质量的RL训练数据极度稀缺，导致长上下文推理仍是未解难题。 提出KeyChain数据合成框架，通过UUID链将短多跳QA转换为高难度长上下文任务——在海量干扰文档中隐藏真实问题，要求模型逐步追踪正确链条、识别问题、检索事实并推理作答。 RL训练在KeyChain数据上诱发了plan-retrieve-reason-recheck推理模式，该模式可泛化到远超训练长度（16K训练的模型可解决128K任务），大幅降低全长度rollout的计算成本。"
origins: ["../../02_阅读笔记/D04_跨载体泛化/2026-03-14_LoongRL.md", "02_阅读笔记/D04_跨载体泛化/2026-03-14_LoongRL.md"]
updated: "2026-06-02"
---

# LoongRL_2510.19363

**核心价值**: 现有RL方法通过CoT提升短上下文推理，但长上下文推理需要同时具备检索和推理能力，且高质量的RL训练数据极度稀缺，导致长上下文推理仍是未解难题。 提出KeyChain数据合成框架，通过UUID链将短多跳QA转换为高难度长上下文任务——在海量干扰文档中隐藏真实问题，要求模型逐步追踪正确链条、识别问题、检索事实并推理作答。 RL训练在KeyChain数据上诱发了plan-retrieve-reason-recheck推理模式，该模式可泛化到远超训练长度（16K训练的模型可解决128K任务），大幅降低全长度rollout的计算成本。

**原始资料**:
- [[../../02_阅读笔记/D04_跨载体泛化/2026-03-14_LoongRL.md]]
- [[02_阅读笔记/D04_跨载体泛化/2026-03-14_LoongRL.md]]
