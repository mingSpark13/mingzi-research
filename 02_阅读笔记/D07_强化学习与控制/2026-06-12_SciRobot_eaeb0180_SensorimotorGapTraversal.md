---
title: "Precise aggressive aerial maneuvers with sensorimotor policies"
authors: "Tianyue Wu, Guangtong Xu, Zihan Wang, Junxiao Lin, Tianyang Chen, Yuze Wu, Zhichao Han, Zhiyang Liu, Fei Gao"
arxiv: ""
date: 2026-06-10
institution: "浙江大学 (Zhejiang University) · 高飞团队"
conf: "Science Robotics 11, eaeb0180 (2026)"
keywords: ["sensorimotor policy", "aggressive flight", "narrow gap traversal", "SE(3) constraints", "end-to-end RL", "sim-to-real", "domain randomization", "policy distillation"]
tags: ["强化学习", "Sim2Real", "运动控制", "空中操作"]
domain: 强化学习
pdf_path: "../../01_论文库/空中操作/2026_SciRobot_eaeb0180_SensorimotorGapTraversal.pdf"
reading_date: 2026-06-12
reading_status: 已读
related_concepts: ["强化学习", "Sim2Real", "运动控制", "空中操作"]
---

# 📖 花火格式笔记

## 🎯 题目

**Precise aggressive aerial maneuvers with sensorimotor policies**
（基于感运动策略的四旋翼精确激进飞行动作）

浙大高飞团队 · Science Robotics 2026 · eaeb0180

## 📝 三句摘要

1. **问题背景**：四旋翼在受限环境（窄缝 / 建筑窗 / 树枝间 / 洞口）做精确激进飞行时，**窄缝姿态强耦合于 SE(3) 运动学约束**（必须短时倾斜机架、利用非对称几何穿越），传统方案依赖外定位 + 模块化手调（state estimation → 轨迹优化 → 控制），接口处信息损失和累积误差在低容错场景下是致命的。
2. **核心方法**：提出**端到端 sensorimotor 策略**，直接从机载单目视觉 + 本体感知（IMU/姿态）输出底层控制指令（collective thrust + body rate），**不显式做 gap 位姿估计 / 里程计 / 轨迹规划**。训练采用**两阶段**：① 用模型基规划器（微分平坦轨迹优化）生成参考轨迹作为 RL 专家的初始化点，缓解 model-free RL 在窄可行解空间的探索低效；② 通过在线模仿学习做**策略蒸馏**，把低维 oracle MDP 策略蒸馏到高维像素观测的 RNN 学生策略。
3. **关键结果**：20cm × 60cm 矩形窄缝 + 5cm clearance（机体高度 10cm）穿越 100% 成功率；roll 角 ≤ 60° 96.7%（29/30）、> 60° 90%（27/30）；pitch 30°/45°/60° = 100%/80%/73.3%；**未训练过动态 gap** 仍能反应式跟踪移动 gap（水平 ±3m/s、旋转）；连续穿越 2-3 个间隔 0.8m 的窄缝；异形（圆/椭圆/拱形/平行四边形）gap 通用。**100+ 真机试飞验证**。

## 💎 价值评估

- **🔬 研究价值**：把"端到端 sensorimotor 闭环"和"模型基规划器 + 策略蒸馏"两个范式融合，**为 SE(3) 强约束下的精确控制提供了 state estimation-free 的范式**；domain randomization 关键消融揭示了"为何策略能反应式跟踪未训练过模式"的机理；与 Wang et al. (12) 的模块化基线形成清晰对照（SE(3) 感知约束缺失导致的退化）。
- **🚀 实践价值**：38cm × 10cm 平台 + Jetson Orin NX + PX4 飞控 + 单目相机（320×256 下采样），是**完全可复现的工程方案**；4 段配 movie（S1-S4）展示单/动/连/异形 gap；HIL 测试床避免了硬件损耗，方法论可推广到需要 SE(3) 精确控制的其他空中操作任务。
- **📈 扩展潜力**：① 极暗 / 强光 / 透明 gap 下的视觉鲁棒性（当前用 landmark 假设）；② 与 D04 跨载体迁移结合——能不能把该 sensorimotor 模式迁移到带机械臂的空中操作平台（D07 已有的工作）；③ 与 D05 数据飞轮结合——为"激进飞行"这种 corner case 任务自动生成训练分布；④ 与 D06 空中 VLN 互补——VLN 负责长程规划，sensorimotor 负责局部敏捷执行。

## 🎯 可落地实验点

**实验设计 A（推荐·短期可做）**：在 AirSpark 中复现 sensorimotor 窄缝穿越
- 对比基线：① 模块化方案（VIO 状态估计 + MPC 轨迹跟踪 + handcrafted features）② OpenVLA 风格 end-to-end 但不加规划器初始化 ③ 本方法（end-to-end + 规划器初始化 + 策略蒸馏）
- 度量指标：穿越成功率（按 gap orientation 0°/30°/60°/90° 分桶）、最小 clearance、平均穿越时间、控制平滑度（jerk/control rate）
- 预期结果：本方法在低 clearance + 极端 orientation 上显著领先，端到端优势在"模块接口误差"维度被放大

**实验设计 B（中期）**：把 sensorimotor 模式迁移到**敏捷空中操作**
- 改造点：把"窄缝"换成"目标抓取点"，policy 输出从"thrust+body rate"扩展到"thrust+body rate+机械臂末端位姿增量"
- 训练范式：参考本文"模型基规划器初始化 RL 专家"思路，用轨迹优化生成抓取 reference trajectory 作为 RL 起点
- 度量：抓取成功率、操作精度、对动态目标的反应能力

**实验设计 C（探索性）**：对"动态 gap"反应能力做形式化分析
- 想法：本文用 domain randomization 实现了"未训练过的反应能力"，值得做系统性消融（不同 DR 强度对动态目标跟踪上限的影响）
- 可落地于 AirSpark 的任意一个 reactive control 子模块

## 🔗 知识图谱

> 链接本文涉及的核心概念（4 个），全部使用字典 v1.1 二级规范名。
> 字典真源：`06_知识Wiki/_views/概念关键词字典.md`

- [[concepts/强化学习]] - 本文核心训练范式（RL + 模仿学习蒸馏）
- [[concepts/Sim2Real]] - 本文核心迁移挑战（域随机化是关键消融）
- [[concepts/运动控制]] - 本文输出空间（collective thrust + body rate 底层控制）
- [[concepts/空中操作]] - 本文任务域（空中平台 + SE(3) 约束下的精确动作）

## 🔗 相关链接

> 链接本文核心引用的论文（baseline / SOTA / 基础工作），通常 2-5 篇。

- [[2026-04-07_RAL26_DiffPhys_GapTraversal]] - 主人已有同主题笔记：DiffPhys 窄缝穿越的 differentiable physics 路线
- [[2026-06-02_公众号视频_浙大高飞团队_FlyMirage_天空之城]] - 浙大高飞团队 FlyMirage 数据合成平台（同一团队 3 周前 B 站视频）
- [[2026-05-12_AutonomousAerialManipulation_SE3]] - 主人已有 SE(3) 空中操作相关笔记
- [[2025-05-28_LaDiWM]] - 主人笔记库中的空中 VLA 基础工作（可作为端到端架构对比）
- [[2026-03-27_pi0]] - 端到端 VLA 经典基线（虽然本文不直接对比，但端到端范式相同）

> 论文中核心对比的 Wang et al. (12) 暂未入库，文中将其作为模块化基线引用。

## 📌 待探索问题

- **问题 1**：本文的"端到端 sensorimotor 闭环"是否能在**空中机械臂操作**任务上复现？D07_Isaac强化学习机械臂控制 是否可以借鉴"规划器初始化 + 策略蒸馏"两阶段？
- **问题 2**：domain randomization 让策略"未训练就反应式跟踪动态 gap"是个有意思的涌现能力——是否可以做形式化分析（DR 强度 vs 涌现能力 vs 训练稳定性的 Pareto 曲线）？
- **问题 3**：本文用 landmark（binarized observation）简化视觉输入，回到真正的端到端 raw image 输入会损失多少性能？这是该范式能否扩展到"无先验 landmark"场景的关键。
- **问题 4**：SE(3) 约束在窄缝中体现为"机架倾斜 + 空气动力学扰动"，与 D03 空地迁移中"地面操作策略迁移到空中"的 SE(3) 泛化问题有什么联系？

---
**维护**: 花火 · 2026-06-12 · 浙大高飞团队 Science Robotics 2026 经典 sensorimotor 工作
