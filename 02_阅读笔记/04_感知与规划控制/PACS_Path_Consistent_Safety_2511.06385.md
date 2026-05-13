---
title: "From Demonstrations to Safe Deployment: Path-Consistent Safety Filtering for Diffusion Policies"
authors: ["Ralf Römer", "Julian Balletshofer", "Jakob Thumm", "Marco Pavone", "Angela P. Schoellig", "Matthias Althoff"]
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
tags: []
domain: 运动控制
pdf_path: "Notebook/30_论文研究/01_论文库/PACS_Path_Consistent_Safety_2511.06385.pdf"
reading_date: 待补充
reading_status: 已读
related_concepts: ["空中操作", "扩散策略", "运动控制"]
---

## 🎯 题目

"From Demonstrations to Safe Deployment: Path-Consistent Safety Filtering for Diffusion Policies"

# PACS: Path-Consistent Safety Filtering

## 📝 三句摘要

1. **核心问题**：Diffusion Policy 无法保证安全，外部安全机制会破坏训练分布导致性能下降
2. **核心贡献**：PACS — 在轨迹层面做路径一致性刹车（path-consistent braking），保持训练分布一致性
3. **关键保证**：提供形式化安全证明 + 集合可达性分析实时部署 + 在动态环境中保持任务成功率

## 核心创新

### 问题诊断

| 现有方法的局限 | PACS 的解决 |
|--------------|-----------|
| 扩散模型不能保证安全 | 外部安全过滤 |
| 安全过滤破坏训练分布 | 路径一致的刹车 |
| 动作级别安全过滤 | 轨迹级别刹车 |
| 延迟高 | 集合可达性分析实时验证 |

### 技术方案：Path-Consistent Braking

**核心思想**：不是修改单个 action，而是对一段轨迹整体做刹车校正

```
扩散策略生成的轨迹 → 在轨迹层面做路径一致的刹车 → 保持训练分布一致性
```

**关键机制**：
- **路径一致性**：刹车后的轨迹仍然在策略的训练分布空间内
- **集合可达性分析**：实时验证安全性，处理不确定性
- **形式化安全保证**：提供数学证明的安全边界

## 与 SafeFlow 的对比

| 维度 | SafeFlow (CBF) | PACS |
|------|---------------|------|
| 基础框架 | Control Barrier Functions | Path-consistent braking |
| 安全类型 | 硬安全约束（数学证明）| 轨迹级安全过滤 |
| 计算量 | QP（1-5ms）| 轨迹优化 |
| 实时性 | ✅ 毫秒级 | ✅ 实时部署 |
| 训练分布保持 | ❌ 可能偏离 | ✅ 路径一致 |

**结论**：SafeFlow 和 PACS 是互补的。SafeFlow 提供硬安全约束，PACS 提供训练分布一致性保证。Paper A 的安全层可以两者结合。

## 待探索问题

1. PACS 的轨迹级刹车与 SafeFlow 的 QP 校正能否叠加？
2. PACS 的计算复杂度在 Jetson 级别硬件上的表现？
3. PACS 在空中机器人（飞行器）上的适用性？


## 💎 价值评估

- **🔬 研究价值**：待补充
- **🚀 实践价值**：待补充
- **📈 扩展潜力**：待补充


## 🎯 可落地实验点

**实验设计**：待补充
- 对比基线：待补充
- 度量指标：待补充
- 预期结果：待补充


## 🔗 知识图谱
- [[空中操作]]
- [[扩散策略]]
- [[运动控制]]


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
