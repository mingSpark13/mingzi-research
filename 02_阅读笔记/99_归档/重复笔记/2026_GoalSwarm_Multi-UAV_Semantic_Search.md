---
title: "GoalSwarm: Multi-UAV Open-Vocabulary Object Search in Unknown Environments"
authors: ""
arxiv: "2603.12908"
date: 2026-03
institution: ""
conf: arXiv 2026
keywords: multi-UAV, open-vocabulary detection, decentralized coordination, Bayesian value map, aerial robotics
tags: ["空中VLN", "多机器人协调", "语义导航"]
summary: "GoalSwarm 将开放词汇感知、Bayesian value map 与去中心化协同结合，面向未知环境下的多 UAV 语义搜索。"
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["空中VLN", "多机器人协调", "语义导航"]
---

## 🎯 题目

GoalSwarm: 多无人机未知环境开放词汇目标搜索

## 📝 三句摘要

1. **问题背景**：单无人机语义搜索在复杂城区/建筑物内效率低，多 UAV 协同搜索是提升覆盖率和效率的关键方向，但现有方法多为已知目标或几何搜索。
2. **核心方法**：提出轻量 2D 语义占据图 + 基础模型 open-vocabulary detection/segmentation + Bayesian Value Map + 去中心化协同探索，实现多 UAV 开放词汇目标搜索。
3. **关键结果**：在多 UAV 仿真中验证了协同搜索的覆盖率优势，是目前最直接涉及空中机器人 open-vocabulary navigation 的论文之一。

## 💎 价值评估

- **🔬 研究价值**：首次将 open-vocabulary detection 引入多 UAV 协同搜索，为空中机器人语义搜索开辟了新方向。
- **🚀 实践价值**：多 UAV 协同搜索在园区/城市搜索场景有实际价值；其 Bayesian Value Map 可启发单无人机"智能探索方向"决策。
- **📈 扩展潜力**：去中心化协同框架可扩展到异构无人机群（大小机搭配）；2D 语义地图可升级为 3D 以适应空中立体搜索。

## 🎯 可落地实验点

**实验设计**：在仿真环境中验证 GoalSwarm 的协同搜索覆盖率 vs 单机语义搜索
- 对比基线：单机 VLFM、独立搜索多 UAV
- 度量指标：Search Coverage Rate、平均任务完成时间、通信开销
- 预期结果：多机协同覆盖率提升 >30%，平均完成时间减少 >25%

## 🔗 知识图谱
- [[多智能体协同]]
- [[去中心化规划]]
- [[贝叶斯价值图]]
- [[空中操作]]
- [[抓取检测]]

## 🔗 相关链接

- [[2024_VLFM_Vision-Language_Frontier_Maps]] - VLFM 提供了单机语义探索基础，GoalSwarm 将其扩展到多机协同
- [[2026_DRIVE-Nav_Directional_Reasoning_Navigation]] - DRIVE-Nav 的 directional reasoning 与 GoalSwarm 的价值地图探索方向相似

## 📌 待探索问题

- 去中心化协同在通信受限或中断时的鲁棒性如何？是否有通信降级策略？
- 2D 语义占据图在无人机高度变化时的适用性如何？是否需要扩展到 3D 表示？

---
**维护**: 花火 · 2026-04-12
