---
type: index
updated: "2026-05-13 10:13"
---

# 06_知识Wiki 导航首页（重构）

> 目标：从“滚动日志式索引”改为“稳定导航式索引”。

## 1) 快速入口

- 概念总索引：[[concepts/index|concepts/index]]
- 来源总索引：[[sources/index|sources/index]]
- 方向总览：[[overview/方向_世界模型_技术路线图|世界模型]] · [[overview/方向_VLA_技术路线图|VLA]] · [[overview/方向_空中VLN_技术路线图|空中VLN]] · [[overview/方向_跨载体泛化_技术路线图|跨载体泛化]]
- 方法对比：[[comparisons/端到端VLA_vs_层次化VLA|端到端VLA vs 层次化VLA]]
- 报告面板：[[reports/index|reports/index]]

## 2) 概念分组导航（与 concepts 对齐）

- 世界模型：[[concepts/世界模型|世界模型]] / [[concepts/隐空间世界模型|隐空间世界模型]] / [[concepts/物理一致性|物理一致性]]
- VLA 与动作：[[concepts/VLA架构|VLA架构]] / [[concepts/动作生成|动作生成]] / [[concepts/扩散策略|扩散策略]]
- 导航与空中：[[concepts/空中VLN|空中VLN]] / [[concepts/语义导航|语义导航]] / [[concepts/空中操作|空中操作]]
- 数据与迁移：[[concepts/数据飞轮|数据飞轮]] / [[concepts/数据合成|数据合成]] / [[concepts/Sim2Real|Sim2Real]]
- 控制与规划：[[concepts/MPC|MPC]] / [[concepts/任务与运动规划|任务与运动规划]] / [[concepts/运动控制|运动控制]]

## 3) 维护规则（摘要）

- `index.md` 只保留稳定导航，不再堆叠“最新添加流水”。
- 最新来源统一写入 `sources/index.md`。
- 新概念先入 `inbox.md`，审核后再入 `concepts/`。
- 保持概念命名与 `_views/概念关键词字典.md` 一致。

## 4) 变更说明（2026-05-13）

- 已将冗长“最新来源滚动区”从本页下沉到 `sources/index.md`。
- 本页改为长期可维护的目录中枢。