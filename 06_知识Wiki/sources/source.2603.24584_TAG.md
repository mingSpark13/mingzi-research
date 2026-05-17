---
type: "source"
tags: []
summary: "- **问题发现**: VLA 很多失败不是运动不可行，而是 instance-level grounding failure——在杂乱场景中抓取轨迹偏了一点"
origins: ["02_阅读笔记/01_机器人与具身/2603.24584_TAG"]
updated: "2026-04-17"
---

# source.2603.24584_TAG

**核心要点**:
- **问题发现**: VLA 很多失败不是运动不可行，而是 instance-level grounding failure——在杂乱场景中抓取轨迹偏了一点
- **TAG 机制**: 对比原始观测 vs 物体擦除观测的策略预测差异，用残差 steering signal 增强物体证据
- **受 CFG 启发**: 无需修改策略架构，推理时加一个引导信号即可

**原始资料**:
- [[02_阅读笔记/01_机器人与具身/2603.24584_TAG]]
