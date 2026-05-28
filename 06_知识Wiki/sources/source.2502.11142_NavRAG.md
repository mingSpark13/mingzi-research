---
type: "source"
id: "source.2502.11142_NavRAG"
pageType: "source"
tags: ["语义导航", "具身智能", "检索增强生成", "视觉语言导航"]
summary: "RAG-LLM基于scene tree和用户画像生成多样化导航指令，861场景200万+标注，支持不同user persona的差异化需求表达"
origins: ["../02_阅读笔记/数据合成/2502.11142_NavRAG.md"]
updated: "2026-05-28 14:44"
---

# NavRAG (2502.11142)

**核心要点**:
- **scene description tree**: 自动构建场景描述树结构，支撑RAG-LLM生成多样化导航指令
- **RAG增强生成**: 利用检索增强LLM根据用户画像和场景上下文生成导航指令，比模板句更贴近真实用户需求
- **大规模标注**: 861个3D场景，200万+条导航指令，支持security/delivery/emergency/maintenance等差异化persona

**与我们的关系**:
- D06空中VLN方向，RAG增强的指令生成路线
- 主人的低空任务指令可从「模板句」升级为「场景树+用户画像+RAG生成」的自然语言规格

**原始资料**:
- [[02_阅读笔记/数据合成/2502.11142_NavRAG]]
