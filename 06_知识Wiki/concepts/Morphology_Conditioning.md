---
type: concept
id: concept.Morphology_Conditioning
pageType: concept
updated: "2026-05-14"
---

# Morphology Conditioning

**别名**：形态条件化、morphology adapter、physics adapter

## 定义

Morphology Conditioning 是一种让机器人策略或世界模型感知自身形态参数（肢长、质量、关节刚度、执行器动力学等）的技术，通过将形态参数作为条件输入，使同一模型可适配不同硬件平台，而无需为每个新平台重新训练。

## 核心思想

- **问题**：传统世界模型/策略过拟合特定硬件形态，跨平台迁移失败
- **方案**：将形态参数编码为条件向量，注入模型的 dynamics-to-latent 层
- **效果**：frozen 基础模型 + 轻量 morphology adapter = 跨载体零样本/少样本迁移

## 典型实现

- Frozen world model + morphology parameter vector → physics adapter
- 形态参数：肢长比例、质量分布、关节 DOF、执行器力矩曲线
- 注入位置：latent dynamics 层（而非 policy 层），保留通用运动先验

## 与相关概念的关系

- [[concepts/跨载体泛化]] - Morphology Conditioning 是实现跨载体泛化的核心技术手段
- [[concepts/世界模型]] - 通常作为 frozen world model 的 adapter 层使用
- [[concepts/Sim2Real]] - 形态参数可桥接 sim-to-real 的动力学 gap
- [[concepts/动作空间统一]] - 形态条件化常与统一动作表示共同出现

## 代表论文

- [[2026-04-09_HardwareAgnostic_QuadWM]] - 首次将 morphology conditioning 用于四足世界模型跨载体迁移

---
**维护**: 花火 · 2026-04-17
