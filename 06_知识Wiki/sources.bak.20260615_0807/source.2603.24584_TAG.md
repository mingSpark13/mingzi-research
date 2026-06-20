---
type: "source"
id: "source.2603.24584_TAG"
pageType: "source"
tags: ["待补充", "D02", "通用操作"]
summary: "TAG 通过比较原始观测与目标擦除观测的策略差异生成 steering signal，增强 VLA 在杂乱场景中的物体级 grounding 稳定性。"
origins: ["../../02_阅读笔记/D02_VLA/2603.24584_TAG.md", "02_阅读笔记/D02_VLA/2603.24584_TAG.md"]
updated: "2026-06-02"
---

# source.2603.24584_TAG

**核心要点**:
- **问题发现**: VLA 很多失败不是运动不可行，而是 instance-level grounding failure——在杂乱场景中抓取轨迹偏了一点
- **TAG 机制**: 对比原始观测 vs 物体擦除观测的策略预测差异，用残差 steering signal 增强物体证据
- **受 CFG 启发**: 无需修改策略架构，推理时加一个引导信号即可

**原始资料**:
- [[../../02_阅读笔记/D02_VLA/2603.24584_TAG.md]]
- [[02_阅读笔记/D02_VLA/2603.24584_TAG.md]]
