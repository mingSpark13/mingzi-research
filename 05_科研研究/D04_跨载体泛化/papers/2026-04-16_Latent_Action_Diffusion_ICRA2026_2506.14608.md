# Latent Action Diffusion for Cross-Embodiment Manipulation

> 扫描时间: 2026-04-16 | R749

## 基础信息
- **arXiv**: 2506.14608 (ICRA 2026)
- **方向**: D04 跨载体泛化

## 一句话核心贡献
用扩散模型在 latent action space 学习跨载体统一策略，实现单一策略控制多机器人 + 跨载体技能迁移（最高 +25.3% 成功率）。

## 核心要点
- 学习共享 latent action space，统一不同载体的动作表示
- Diffusion Policy 映射共享观测到 latent end-effector actions
- 多机器人控制：单策略控制多平台（机械臂/灵巧手）
- 跨载体迁移：跨 embodiment 数据 co-training
- 实验： dexterous hands + Franka parallel gripper

## 与主人研究的相关度
⭐⭐⭐ 高度相关：无人机+机械臂双载体；潜动作空间对齐是 D04 的核心路线之一；可参考其 latent action space 设计

## 备注
- 需精读 latent action space 的具体设计（如何建模不同载体的动作对齐）
- 可与 OPFA/CEI 方法对比
