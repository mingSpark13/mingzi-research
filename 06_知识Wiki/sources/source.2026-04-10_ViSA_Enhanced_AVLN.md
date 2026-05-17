---
type: "source"
tags: []
summary: "**原始资料**:"
origins: ["02_阅读笔记/05_语义导航/2026-04-10_ViSA_Enhanced_AVLN"]
updated: "2026-04-17"
---

# source.2026-04-10_ViSA_Enhanced_AVLN

**核心要点**:
- **直接图像平面推理**: 不先压成离散 scene graph，而是保留视觉几何关系给 VLM 直接判断。
- **结构化视觉提示**: 把目标、候选区域、空间关系组织成 prompt，增强空间定位能力。
- **训练自由（training-free）增强**: 更像给现有 aerial VLN/explorer 补一个 reasoning 前端，而不是重训整套控制器。

**与我们的关系**:
- 它补的是 **“看懂当前画面里哪里更像目标、空间关系是否成立”** 这一层，适合作为 D06 里显式 explorer / frontier 主线的前端增强模块。

**原始资料**:
- [[02_阅读笔记/05_语义导航/2026-04-10_ViSA_Enhanced_AVLN]]
