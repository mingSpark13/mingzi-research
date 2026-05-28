---
type: "source"
id: "source.2603.12238_SceneAssistant"
pageType: "source"
tags: ["程序化内容生成", "具身智能", "视觉语言导航", "多模态统一架构"]
summary: "VLM接收渲染反馈后通过Scale/Rotate/FocusOn等action API逐步修改场景，形成「渲染-反馈-修改」视觉反馈循环"
origins: ["../02_阅读笔记/数据合成/2603.12238_SceneAssistant.md"]
updated: "2026-05-28 14:44"
---

# SceneAssistant (2603.12238)

**核心要点**:
- **视觉反馈循环**: VLM接收渲染反馈后通过action API逐步修改场景，迭代提升场景与文本描述的空间一致性
- **迭代修正**: 非一次性生成，而是「渲染-反馈-修改」循环，显著提升open-vocabulary 3D场景生成质量
- **与SAGE互补**: SAGE侧重physics critic，本文侧重visual feedback loop，共同构成「生成-验证-修复」体系

**与我们的关系**:
- D05数据合成方向，程序化内容生成视觉反馈迭代路线
- 主人低空场景调试可借鉴：PCG生成初版→渲染top-down map→VLM反馈→修正的交互式生成界面

**原始资料**:
- [[02_阅读笔记/数据合成/2603.12238_SceneAssistant]]
