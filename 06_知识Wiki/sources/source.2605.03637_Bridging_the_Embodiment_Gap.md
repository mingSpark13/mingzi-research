---
type: "source"
id: "source.2605.03637_Bridging_the_Embodiment_Gap"
pageType: "source"
tags: ["cross-embodiment", "video diffusion", "robot learning", "human-to-robot transfer", "跨载体泛化", "多模态统一架构"]
summary: "人类示范视频很容易拿到，但人和机器人在运动学与外形上的分布差异，会让直接迁移到机器人学习时严重失真。 论文把任务信息与 embodiment 信息显式解耦到两个正交 latent space，再用参数高效适配器把它们注入冻结的视频扩散模型，实现从单条人类演示生成机器人执行视频。 方法不需要成对 cross-embodiment 数据，就能生成时序一致、形态合理的机器人演示视频，适合作为互联网人类视频转机器人训练数据的桥接层。"
origins: ["../../02_阅读笔记/D04_跨载体泛化/2026-05-06_2605.03637_Bridging_the_Embodiment_Gap.md", "../../02_阅读笔记/D04_跨载体泛化/2026-05-06_2605.03637_Bridging_the_Embodiment_Gap.md"]
updated: "2026-06-02"
---

# source.2605.03637_Bridging_the_Embodiment_Gap

**核心价值**: 人类示范视频很容易拿到，但人和机器人在运动学与外形上的分布差异，会让直接迁移到机器人学习时严重失真。 论文把任务信息与 embodiment 信息显式解耦到两个正交 latent space，再用参数高效适配器把它们注入冻结的视频扩散模型，实现从单条人类演示生成机器人执行视频。 方法不需要成对 cross-embodiment 数据，就能生成时序一致、形态合理的机器人演示视频，适合作为互联网人类视频转机器人训练数据的桥接层。

**原始资料**:
- [[../../02_阅读笔记/D04_跨载体泛化/2026-05-06_2605.03637_Bridging_the_Embodiment_Gap.md]]
- [[02_阅读笔记/D04_跨载体泛化/2026-05-06_2605.03637_Bridging_the_Embodiment_Gap.md]]
