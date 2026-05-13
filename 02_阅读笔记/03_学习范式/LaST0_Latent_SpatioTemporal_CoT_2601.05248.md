---
title: "LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model"
authors: ["Zhuoyang Liu", "Jiaming Liu", "Hao Chen", "Jiale Yu", "Ziyu Guo", "Chengkai Hou", "Chenyang Gu", "Xiangju Mi", "Renrui Zhang", "Kun Wu", "Zhengping Che", "Jian Tang", "Pheng-Ann Heng", "Shanghang Zhang"]
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
tags: []
domain: 强化学习
pdf_path: "Notebook/30_论文研究/01_论文库/LaST0_Latent_SpatioTemporal_CoT_2601.05248.pdf"
reading_date: 待补充
reading_status: 已读
related_concepts: ["VLA架构", "强化学习", "模仿学习"]
---

## 🎯 题目

"LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model"

# LaST0: Latent Spatio-Temporal Chain-of-Thought

## 📝 三句摘要

1. **核心问题**：现有 VLA 的显式 CoT 在语言空间推理，有推理延迟瓶颈，且语言无法捕捉"不可言说"的物理属性（力反馈、触觉、精细动力学）
2. **核心贡献**：提出 LaST0——在**连续隐空间**进行时空 CoT 推理，建模未来视觉动力学、3D结构信息、机器人本体感知状态，实现 token 高效的隐式推理轨迹
3. **核心架构**：双系统 MoT（Mixture-of-Transformers）——推理专家低频做隐式推理，动作专家高频生成动作，支持推理频率与动作频率的自适应切换

## 核心创新

### 问题诊断

| 现有方法的局限 | LaST0 的解决 |
|--------------|------------|
| 语言空间 CoT 推理延迟高 | 隐空间推理，token 高效 |
| 语言无法捕捉物理属性 | 建模视觉动力学+3D结构+本体感知 |
| 推理和动作同频，浪费算力 | 异构操作频率，推理低频、动作高频 |

### 架构：双系统 MoT

```
观察输入(Observation)
    ↓
[推理专家] ──低频隐式推理──→ 隐式推理轨迹（未来视觉+3D结构+本体感知）
    ↓
[动作专家] ──高频动作生成──→ 机器人动作（action）
```

- **推理专家（Reasoning Expert）**：低频，做隐式时空 CoT，不输出语言，只输出隐状态
- **动作专家（Acting Expert）**：高频，基于推理专家的隐式表征生成 action
- **异构频率训练**：推理专家和动作专家以不同频率运作，推理频率远低于动作频率

### 隐式 CoT 空间建模内容

1. **未来视觉动力学**：预测未来几帧的视觉观察
2. **3D 结构信息**：空间几何结构
3. **机器人本体感知状态**：关节角度、末端执行器位置等

## 实验结果

| 场景 | 改进幅度 |
|------|---------|
| 10 个仿真任务 | +8% 成功率 |
| 6 个真实世界任务 | +13% 成功率 |
| 长时域任务最终步骤 | 5× 更高成功率 |

## 与 Paper A 的关系

**高度相关！**

Paper A 的三层架构：
```
高层 VLM（秒级慢思考，语义层）→ 中层意图解析器 → 低层执行控制器（毫秒级）
```

LaST0 的双专家 MoT 架构与 Paper A 层次化解耦哲学完全一致：
- 推理专家 ≈ Paper A 的高层 VLM 意图层
- 动作专家 ≈ Paper A 的低层执行控制器
- **LaST0 缺失的中层** = Paper A 的 SafeFlow 安全层（CBF 约束）

**关键区别**：
- LaST0 的推理专家在**隐空间**进行 CoT（token 高效）
- LaST0 没有显式的安全约束层
- LaST0 没有专门的中层「意图解析」模块

**可借鉴点**：
1. LaST0 的隐式 CoT 空间可作为 Paper A 高层 VLM 的输出形式
2. MoT 双专家频率解耦的设计值得参考
3. LaST0 的异构频率训练方法

## 待探索问题

1. LaST0 的隐式推理轨迹如何在 Paper A 中与 SafeFlow 安全层衔接？
2. LaST0 没有安全约束——Paper A 的 CBF 层能否直接叠加？
3. LaST0 的 3D 结构信息建模方式是否适用于空中机械臂？

## 🔗 相关链接

- [Project Website](https://sites.google.com/view/last0)
- [Authors - Jiaming Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+J) — 主人之前分享的「至简动力」演讲者贾鹏团队


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
- [[VLA]]
- [[强化学习]]
- [[模仿学习]]


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
