---
title: "Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer"
authors: Sthithpragya Gupta, Durgesh Haribhau Salunkhe, Aude Billard
arxiv: ""
date: 2026-04-15
institution: EPFL LASA Lab
conf: Science Robotics
keywords: ["Kinematic Intelligence", "Cross-robot Skill Transfer", "LfD", "7-DoF Manipulator"]
tags: [跨载体泛化, 运动控制, 逆运动学]
domain: 具身智能
pdf_path: ""
reading_date: 2026-05-03
reading_status: 已读
related_concepts: ["跨载体泛化", "运动控制", "逆运动学"]
---

# 📖 花火格式笔记

## 🎯 题目

**Demonstrate once, execute on many: Kinematic intelligence for cross-robot skill transfer**

## 📝 三句摘要

1. **问题背景**：示教学习（LfD）的技能与机器人本体强绑定，换一台臂需要重新训练，导致工业场景换臂成本极高。
2. **核心方法**：提出**运动学智能（Kinematic Intelligence）**框架，将人类示教的任务在运动学层面抽象为拓扑级通用策略，使不同构型的协作臂都能安全执行。
3. **关键结果**：三个完全不同构型的 7-DoF 商用协作臂成功复现同一示教任务（推块、放置、投篮），换臂无需重训练。

## 💎 价值评估

- **🔬 研究价值**：首次从运动学拓扑本质出发解决跨机器人迁移问题，提出可解析、可验证的框架，填补了示教学习"本体约束建模"的空白。
- **🚀 实践价值**：工业产线换臂可复用已有示教技能，降低部署成本；运动学先验替代数据蛮力，计算可负担。
- **📈 扩展潜力**：可扩展到人形机器人、多指灵巧手；与 VLA/世界模型结合可能产生新范式；非尖点假设可进一步放松。

## 🎯 可落地实验点

**实验设计**：在双机械臂协作场景验证跨臂迁移
- 对比基线：传统同构复刻方法（不经运动学抽象的轨迹复制）、π₀ 等 VLA 方法
- 度量指标：任务成功率、关节限位违反率、奇异规避抖动次数
- 预期结果：运动学智能框架在换臂场景下成功率显著高于基线，且无奇异抖动

## 🔗 知识图谱

> 链接本文涉及的核心概念（3-5个），必须使用字典 v1.1 二级规范名。

- [[跨载体泛化]] - 核心问题：不同构型机器人之间的技能迁移
- [[运动控制]] - 底层执行：关节空间的安全轨迹执行与奇异规避
- [[运动学建模]] - 关键技术：7R→4R+3R 降维锚点，全局拓扑与可行域确定

## 🔗 相关链接

> 链接本文核心引用的论文（baseline/SOTA/基础工作）。

- 待补充：本文尚未入库核心对比 baseline（待下载 Science Robotics 原文后补充）

## 📌 待探索问题

- 框架假设"非尖点（noncuspidal）"机器人，对尖点型机器人（如某些 6-DoF 臂）如何扩展？
- 运动学智能与近期 VLA 端到端方法（如 π₀、OpenVLA）如何融合？能否用 VLM 理解任务语义，运动学智能保证安全性？
- 实验仅验证 7-DoF 协作臂，迁移到人形机器人（27+ DoF）时拓扑分类复杂度如何控制？

---
**维护**: 花火 · 2026-05-03
