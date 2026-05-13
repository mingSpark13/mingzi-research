---
title: DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations
authors: Qingtao Liu, Zhengnan Sun, Yu Cui, Haoming Li, Gaofeng Li, Lin Shao, Jiming Chen, Qi Ye
arxiv: 2602.21811
date: 2026-02-25
institution: Zhejiang University等
conf: IEEE Transactions on Robotics (T-RO 2026)
keywords: [dexterous manipulation, hand-object representation, reinforcement learning, sim2real]
tags: [灵巧操作, 强化学习, Sim2Real, 零样本泛化]
domain: 灵巧操作
pdf_path: "../../01_论文库/灵巧操作/2602.21811_DexRepNet++.pdf"
reading_date: 2026-04-20
reading_status: 已读
related_concepts: ["灵巧操作", "强化学习", "Sim2Real", "零样本泛化"]
---

# 📖 花火格式笔记

## 🎯 题目

DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations

## 📝 三句摘要

1. **问题背景**：多指灵巧手操作受高自由度动作空间和复杂接触关系影响，现有DRL方法常忽视手-物交互表征对泛化能力的决定作用。
2. **核心方法**：论文提出DexRep手物交互表征，同时编码物体表面几何与手-物空间关系，并用于抓取、手内重定向、双手交接三类灵巧任务策略学习。
3. **关键结果**：在仅40个训练物体下，抓取策略对5000+未见物体达到87.9%成功率，多个任务较既有表征提升20%-40%，且实机部署显示较小sim2real gap。

## 💎 价值评估

- **🔬 研究价值**：把“表征”而非单纯“策略网络”拉回灵巧操作核心矛盾，适合作为手-物几何关系建模的重要基线。
- **🚀 实践价值**：对主人关注的高泛化操作策略很有参考意义，尤其适合抓取到更复杂灵巧操作之间的过渡研究。
- **📈 扩展潜力**：后续可继续接入触觉、多视角视觉或VLA高层语义条件，验证表征是否能支撑更复杂指令驱动操作。

## 🎯 可落地实验点

**实验设计**：把DexRep式几何+空间表征迁移到现有灵巧抓取/双臂交接任务中，对比纯点云编码与手工状态拼接方案。
- 对比基线：PointNet状态编码、仅物体表征、仅相对位姿编码
- 度量指标：未见物体成功率、样本效率、sim2real性能下降幅度
- 预期结果：几何+空间联合表征在跨对象泛化和真实部署稳定性上更优

## 🔗 知识图谱

- [[灵巧操作]] - 多指手精细接触与手内操作核心任务
- [[强化学习]] - 主要策略学习范式
- [[Sim2Real]] - 实机迁移效果是论文亮点之一
- [[零样本泛化]] - 对大规模未见物体的泛化能力突出

## 🔗 相关链接

- [[2026-04-18_HRDexDB]] - 同样关注灵巧手与跨形态数据基础，但这篇更偏表征学习
- [[2024-10_pi0]] - 可作为通用操作/VLA路线对照，比较表征驱动与大模型驱动范式

## 📌 待探索问题

- DexRep若加入触觉或力反馈，能否进一步提升手内重定向与双手交接稳定性？
- 该表征是否能与语言条件策略结合，支撑开放词汇灵巧操作任务？

---
**维护**: 花火 · 2026-04-20
