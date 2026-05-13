---
title: 'D(R, O) Grasp: A Unified Representation for Cross-Embodiment Dexterous Grasping'
authors: Zhenyu Wei, Zhixuan Xu, Jingxiang Guo, Yiwen Hou, Chongkai Gao, Zhehao Cai,
  Jiayu Luo, Lin Shao (NUS)
arxiv: 2410.01702
date: 2024-10
institution: National University of Singapore
conf: arXiv
keywords: Cross-Embodiment, Dexterous Grasping, Unified Representation, D(R,O), Interaction-Centric,
  Point Cloud
tags:
- D02
- 跨载体泛化
domain: 机器人与具身
summary: 灵巧抓取（dexterous grasping）因高自由度、复杂接触而困难；现有 robot-centric 方法（UniDexGrasp++）效果好但泛化差，object-centric
  方法（Contact Map）泛化强但需要额外IK优化、速度慢。
pdf_path: ../../01_论文库/具身智能/2410_D_RO_Grasp.pdf
reading_date: 待补充
reading_status: 已读
related_concepts:
- 跨载体泛化
---

## 🎯 题目

D(R, O) Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping

## 📝 三句摘要

1. **问题背景**：灵巧抓取（dexterous grasping）因高自由度、复杂接触而困难；现有 robot-centric 方法（UniDexGrasp++）效果好但泛化差，object-centric 方法（Contact Map）泛化强但需要额外IK优化、速度慢。
2. **核心方法**：提出 **D(R, O)** = 统一交互表征，编码"机器人手在抓取pose下点云"与"物体点云"之间的相对距离矩阵；输入是 open hand 点云 + 物体点云，输出是 D(R,O) 矩阵，再用 multilateration 恢复 hand link 6D pose → 算关节角。提出 **configuration-invariant pretraining**（对比学习）来建立不同手构型间的对齐。
3. **关键结果**：仿真成功率 87.53%（3种灵巧手，<1秒），真实世界 LeapHand 实验成功率 89%。

## 💎 价值评估

- **🔬 研究价值**：D(R,O) 是"交互中心"表征，超越了传统的 robot-centric / object-centric 二分法；configuration-invariant pretraining 为跨躯体特征对齐提供了新思路。
- **🚀 实践价值**：支持任意灵巧手（LeapHand、Shadow Hand、Inspire Hand）从点云直接预测，无需针对特定手训练。
- **📈 扩展潜力**：D(R,O) 表征可作为主人 PMI 框架中"身体使用层"的抓取能力基础——D(R,O) 编码了"手-物"交互关系，可以直接为 Body-Usage Adapter 提供接触稳定性估计。

## 🎯 可落地实验点

**实验设计**：以 D(R,O) Grasp 为抓取底层，接入主人的 Body-Usage Adapter
- 对比基线：D(R,O) 直接输出（无身体使用参数调节）
- 度量指标：抓取成功率、接触力分配合理性、跨手迁移率
- 预期结果：Body-Usage Adapter 应能在不同手、不同物体上更稳定地分配接触力

## 🔗 知识图谱

- [[灵巧操作]] - D(R,O) 是灵巧抓取的统一表征
- [[具身智能]] - 跨躯体泛化是具身智能的核心挑战

## 📌 待探索问题

- D(R,O) 表征是否可以扩展到非抓取任务（如插入、装配）？
- configuration-invariant pretraining 的对比学习信号从何而来——是否需要大规模跨手数据？

---
**维护**: 花火 · 2026-04-12


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作
