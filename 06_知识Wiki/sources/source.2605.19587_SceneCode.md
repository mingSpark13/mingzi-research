---
type: "source"
id: "source.2605.19587_SceneCode"
pageType: "source"
tags: ["程序化内容生成", "具身智能", "世界模型", "仿真平台"]
summary: "将NLP prompt编译为可执行Blender Python program生成SDF场景，实现「场景即代码」范式，支持可交互性查询和批量变体生成"
origins: ["../02_阅读笔记/数据合成/2605.19587_SceneCode.md"]
updated: "2026-05-28 14:44"
---

# SceneCode (2605.19587)

**核心要点**:
- **场景即代码**: NLP prompt编译为可执行Blender Python program，导出SDF给物理仿真器，场景可编辑、可复用、可批量变体生成
- **scene-state registry**: 维护object request→可执行程序→渲染几何→仿真资产的完整映射，支持物理仿真器的关节/碰撞/抓取查询
- **程序化生成**: part-wise Blender Python程序导出SDF，实现关节类物体（门/抽屉）的可交互性查询

**与我们的关系**:
- D05数据合成方向，「程序化世界代码」代表工作
- 主人低空SceneSpec/TaskSpec中间格式的路线参考：保存可执行规范而非一次性资产文件
- 可扩展到低空TaskSpec设计（巡检路线/覆盖区域/避障约束）

**原始资料**:
- [[02_阅读笔记/数据合成/2605.19587_SceneCode]]
