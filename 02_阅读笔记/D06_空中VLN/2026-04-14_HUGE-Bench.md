# HUGE-Bench: High-Level UAV Vision-Language-Action Benchmark
> arXiv:2603.19822 | 2026-03 | D06

## 三句摘要
1. 提出 HUGE-Bench，面向高层语义指令（"检查这栋楼"）而非细粒度路由描述的 UAV VLN benchmark，填补"短指令→复杂多阶段行为"评测空白。
2. 基于 3DGS-Mesh 数字孪生（光栅渲染+碰撞几何一体化）构建 4 个真实场景、8 类高层任务、2.56M 米轨迹，支持过程保真度+终端准确率+安全性的综合评估。
3. 在主流 VLA 模型上发现重大差距：高语义完成率与安全执行难以兼得，现有模型在 concise language grounding 上存在根本性缺陷。

## 价值评估
⭐⭐⭐⭐ | D06最强 benchmark 发现！直接对标龙虾项目"语言指令→找到目标"的语义导航任务，且 3DGS-Mesh 数字孪生路线与 UE 仿真体系完全对齐，可作为检查用 demo 的参考框架。

## 可落地实验点
- 用 HUGE-Bench 的任务分类体系（8类高层任务）为龙虾 GoalSearch 设计评测场景库
- 借鉴其"3DGS-Mesh 数字孪生+碰撞感知评估"架构提升 UE 仿真场景的评测真实性
- 以 HUGE-Bench 的"过程+终端+安全"三维度替代单一成功率指标
