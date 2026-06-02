---
type: "source"
id: "source.2026-03-31_Fast-dVLA"
pageType: "source"
tags: ["dVLA", "discrete diffusion", "VLA", "实时推理", "KV cache", "block-wise diffusion"]
summary: "离散扩散 VLA（dVLA）虽然在多模态对齐和保留预训练知识上很强，但推理速度长期卡死，离真实机器人常见的 **30Hz 实时控制** 还有明显差距，核心瓶颈是双向注意力下 **KV cache 无法复用**。"
origins: ["../../02_阅读笔记/D02_VLA/2026-03-31_Fast-dVLA.md"]
updated: "2026-06-02"
---

# ViSA-Enhanced AVLN (2603.08007)

**核心价值**: 离散扩散 VLA（dVLA）虽然在多模态对齐和保留预训练知识上很强，但推理速度长期卡死，离真实机器人常见的 **30Hz 实时控制** 还有明显差距，核心瓶颈是双向注意力下 **KV cache 无法复用**。

**原始资料**:
- [[../../02_阅读笔记/D02_VLA/2026-03-31_Fast-dVLA.md]]
