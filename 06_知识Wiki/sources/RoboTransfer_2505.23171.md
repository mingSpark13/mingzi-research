---
type: "source"
id: "source.RoboTransfer_2505.23171"
pageType: "source"
tags: ["video diffusion", "geometry consistency", "policy transfer", "data augmentation", "数据合成", "视频生成"]
summary: "用几何一致性视频扩散把机器人操作视频做成可控可编辑的数据增强层，并在策略迁移中带来显著真实泛化增益。"
origins: ["../../02_阅读笔记/D04_跨载体泛化/2026-04-09_RoboTransfer.md", "../../02_阅读笔记/D04_跨载体泛化/2026-04-09_RoboTransfer.md"]
updated: "2026-06-02"
---

# RoboTransfer_2505.23171

**核心价值**: 用几何一致性视频扩散把机器人操作视频做成可控可编辑的数据增强层，并在策略迁移中带来显著真实泛化增益。

**与我们的关系**:
- 这篇正好补 D05 现在最缺的一环：不是再问“能不能生成机器人视频”，而是问**生成出来的视频能不能保持多视角几何一致、还能被策略真正用起来**。对主人后续 UE/AirSim 数据工厂尤其关键，因为空中平台视角变化更剧烈，若几何不稳，合成数据很容易训练出只会看表面纹理的假本事。

**原始资料**:
- [[../../02_阅读笔记/D04_跨载体泛化/2026-04-09_RoboTransfer.md]]
- [[02_阅读笔记/D04_跨载体泛化/2026-04-09_RoboTransfer.md]]
