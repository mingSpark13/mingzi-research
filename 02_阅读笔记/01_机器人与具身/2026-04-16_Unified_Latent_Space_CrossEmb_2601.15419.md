# Learning a Unified Latent Space for Cross-Embodiment Robot Control

> 扫描时间: 2026-04-16 | R749

## 基础信息
- **arXiv**: 2601.15419
- **方向**: D04 跨载体泛化

## 一句话核心贡献
学习统一 latent space 实现跨载体机器人控制的零样本迁移，无需重训练。

## 核心要点
- 核心需求：开发可跨载体无缝迁移的控制策略，无需为每个新机器人重新训练
- 统一 latent space 作为不同 embodiment 的共享表示空间
- 关键技术：projection of diverse state-action spaces to shared latent spaces
- 对齐机制：adversarially trained decoders + cycle-consistency regularizers
- 无需 paired data 或目标域 reward labels

## 与主人研究的相关度
⭐⭐⭐ 高度相关：主人有无人机+机械臂双平台；Latent Action Diffusion 和 OPFA 已覆盖同类路线；本文方法与它们的差异点需精读

## 备注
- 需对比与 OPFA(2603.14522) 和 CEI(2601.09163) 的方法差异
- 关注 latent space 对齐的具体数学框架
