---
title: RoboStriker Hierarchical Decision-Making for Autonomous Humanoid Boxing
authors: Kangning Yin, Zhe Cao, Weishuai Dong, Weiran Zeng, Tong Zhang, Jingbo Wang, Jiaxuan Cai, Chen Yao, Qi Wei, Yukai Lin, Song Haoran
arxiv: 2601.22517
date: 2026-01-30
institution: 上海AI实验室, 上海交通大学
conf: arXiv (cs.RO)
keywords: 人形机器人, 分层决策, 博弈强化学习, 对抗任务, 宇树G1
tags: ["D02", "跨载体泛化", "强化学习"]
domain: 腿足机器人
pdf_path: ../../01_论文库/腿足机器人/RoboStriker.pdf
reading_date: 2026-03-17
reading_status: 待读
summary: "在人形机器人上实现类人竞技智能（尤其是拳击等接触密集的高动态任务）仍是挑战；多智能体强化学习直接应用于人形控制受限于高维接触动力学和缺乏强物理先验。"
related_concepts: ["跨载体泛化", "强化学习"]
---

## 🎯 题目

RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing

## 📝 三句摘要

1. **问题背景**：在人形机器人上实现类人竞技智能（尤其是拳击等接触密集的高动态任务）仍是挑战；多智能体强化学习直接应用于人形控制受限于高维接触动力学和缺乏强物理先验。

2. **核心方法**：提出三层分层框架 RoboStriker，将高层策略推理与低层物理执行解耦。(1) 从 mocap 数据训练单智能体动作跟踪器，学习拳击技能库；(2) 将技能蒸馏到结构化潜空间，将高斯参数化分布投影到超球面，约束在物理可行子空间；(3) 引入潜空间神经虚拟自博弈 (LS-NFSP)，在潜空间而非原始电机空间进行对抗训练。

3. **关键结果**：仿真中取得优异对抗性能，成功实现 sim-to-real 迁移（部署到宇树 G1 人形机器人）。

## 💎 价值评估

- **🔬 研究价值**：首次将分层决策+博弈RL用于人形机器人对抗任务，"物理可行性"与"策略竞争力"解耦思路有通用性
- **🚀 实践价值**：可迁移到其他对抗运动（乒乓球、格斗等），为具身智能对抗研究提供基线
- **📈 扩展潜力**：可扩展到双人对战之外的多人场景，加入真实人类对战

## 🎯 可落地实验点

**实验设计**：将 RoboStriker 分层框架迁移到双足机器人武术对练
- 对比基线：端到端 RL、单层策略
- 度量指标：对战胜率、动作多样性、 sim2real 差距
- 预期结果：分层框架应显著优于端到端


## 🔗 知识图谱

- [[腿足机器人]]
- [[强化学习]]
- [[强化学习]]

## 🔗 相关链接

- [[2026-03-17_ASCENT]] - 多楼层导航（同一天入库，上海AI Lab工作）
- [[2026-03-17_AME-2]] - 腿足机器人运动控制（ETH Zurich）
- [[博弈强化学习]] - 关联概念页

## 📌 待探索问题

- 潜空间投影到超球面的物理意义？
- 如何应对人类对手的不规则行为？
- 延迟敏感的真实对战场景如何处理？

---
**维护**: 花火 · 2026-04-12
