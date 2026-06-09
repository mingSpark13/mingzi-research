---
type: "source"
id: "source.2605.02739_Latent_Bridge"
pageType: "source"
tags: ["VLA inference", "dual-system VLA", "feature delta prediction", "DAgger", "VLA架构", "实时推理"]
summary: "双系统 VLA 虽然效果强，但每个控制步都跑一次大 VLM 太贵，时序上还存在大量冗余特征计算。 论文提出 Latent Bridge 预测相邻时刻的 VLM feature delta，让 action head 在预测特征上运行，只周期性调用昂贵 backbone，并用 task-agnostic DAgger 管线训练这座“时序桥”。 在 GR00T-N1.6 与 π0.5 两类架构上都保留 95-100% 性能，同时减少 50-75% VLM 调用，带来 1.65-1.73x episode 级加速。"
origins: ["../../02_阅读笔记/D05_数据飞轮/2026-05-06_2605.02739_Latent_Bridge.md", "02_阅读笔记/D05_数据飞轮/2026-05-06_2605.02739_Latent_Bridge.md"]
updated: "2026-06-02"
---

# source.2605.02739_Latent_Bridge

**核心价值**: 双系统 VLA 虽然效果强，但每个控制步都跑一次大 VLM 太贵，时序上还存在大量冗余特征计算。 论文提出 Latent Bridge 预测相邻时刻的 VLM feature delta，让 action head 在预测特征上运行，只周期性调用昂贵 backbone，并用 task-agnostic DAgger 管线训练这座“时序桥”。 在 GR00T-N1.6 与 π0.5 两类架构上都保留 95-100% 性能，同时减少 50-75% VLM 调用，带来 1.65-1.73x episode 级加速。

**原始资料**:
- [[../../02_阅读笔记/D05_数据飞轮/2026-05-06_2605.02739_Latent_Bridge.md]]
- [[02_阅读笔记/D05_数据飞轮/2026-05-06_2605.02739_Latent_Bridge.md]]
