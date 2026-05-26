---

summary: "GET 通过结构化LLM推理与经验概率图协同，提升大尺度未知环境中的目标搜索效率与稳定性。"
title: "GET: Goal-directed Exploration and Targeting for Large-Scale Unknown Environments"
authors: 待从论文首页补全
arxiv: ""
date: 2025-11-24
institution: 待补
conf: 未知（当前 PDF 为论文稿件格式）
keywords: object search, large language models, exploration, unknown environments, embodied intelligence
tags: ["D02", "具身智能"]
domain: 通用操作
pdf_path: ../../01_论文库/通用操作/GET_Goal-directed_Exploration_and_Targeting_for_Large-Scale_Unknown_Environments.pdf
reading_date: 2026-04-01
reading_status: 已读
related_concepts: ["LLM驱动机器人", "主动感知", "长程任务规划", "Sim2Real"]
---

## 🎯 题目

GET: Goal-directed Exploration and Targeting for Large-Scale Unknown Environments

## 📝 三句摘要

1. **问题背景**：在大尺度未知环境里做目标物搜索时，LLM 虽然有语义理解和推理能力，但在 3D 空间感知、决策一致性和多目标历史信息利用上都很容易翻车。
2. **核心方法**：论文提出 **GET** 框架，把 LLM 用于环境全景分析和目标位置推断；其中 **DoUT**（Diagram of Unified Thought）负责用“提议者-评估者”双角色加反馈循环增强推理稳定性，另用 **GMM 多层任务概率图** 显式记录和更新历史搜索经验。
3. **关键结果**：真实机器人实验表明，GET 在复杂大尺度未知环境中的搜索效率明显优于现有方法，说明“结构化 LLM 推理 + 显式经验地图”这条路线对目标搜索很有效。

## 💎 价值评估

- **🔬 研究价值**：这篇的亮点不是单纯把 LLM 塞进机器人，而是很认真地正视了 LLM 在空间感知和记忆上的缺陷，然后用外部结构（DoUT + 概率图）去补，属于比较扎实的 embodied LLM 系统设计。
- **🚀 实践价值**：如果主人后面要做开放环境探索、搜索定位、甚至空地协同中的目标发现，这篇方法论很有借鉴意义——尤其是“LLM 负责语义推断，外部模块负责空间一致性与经验累积”这套分工。
- **📈 扩展潜力**：可以继续往多目标、多机器人、空地协同搜索扩展；也可以把 GMM 经验图替换成更强的 world model / memory map / active sampling 机制。

## 🎯 可落地实验点

**实验设计**：做一个“语义搜索 + 空间经验图”的无人机/地面机器人搜索 baseline，验证 LLM 与显式地图记忆结合的收益。
- 对比基线：纯规则搜索 / 纯 LLM 开环搜索 / 无历史经验图的语义搜索
- 度量指标：目标找到率、平均搜索时间、路径长度、重复探索率、多目标切换效率
- 预期结果：加入结构化反馈推理与经验概率图后，搜索效率和多轮任务稳定性都会明显提升

## 🔗 知识图谱
- [[具身智能]] - 目标搜索任务属于典型 embodied decision-making 场景
- [[LLM驱动机器人]] - 用 LLM 做语义推断与任务决策
- [[主动感知]] - 搜索过程本质上是主动选择观测与移动策略
- [[长程任务规划]] - 大尺度未知环境中的搜索具有长时序决策特征
- [[Sim2Real]] - 论文使用真实机器人实验验证搜索策略有效性

## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- [[2026-04-01_MolmoSpaces]] - 都关注大尺度复杂环境中的 embodied task，但 MolmoSpaces 偏 benchmark 基建，GET 偏 LLM 搜索框架
- [[2026-04-01_See_Point_Fly]] - 都在做“语言/视觉理解到行动”的闭环，只是 GET 偏地面目标搜索，SPF 偏无人机导航
- [[2026-04-01_Explainable_DRL_UAV_Path_Planning]] - 一个是结构化 LLM 搜索路线，一个是经典 DRL 路径规划路线，可作为两类不同范式对照

## 📌 待探索问题

- DoUT 这种“提议者-评估者”结构，能不能迁移到主人后面更关心的空中操作与空地协同任务里？
- GMM 任务概率图在更大规模、更动态的环境里是否会出现表达瓶颈，是否需要换成更强的记忆图或世界模型？
- 如果把 GET 与主动采样结合，能否让机器人在失败区域自动补采并持续提升搜索策略？

---
**维护**: 花火 · 2026-04-12
