---
title: "From Code to Action: Hierarchical Learning of Diffusion-VLM Policies"
authors: ["Markus Peschl", "Pietro Mazzaglia", "Daniel Dijkman"]
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
tags: ["D02"]
domain: 通用操作
pdf_path: "Notebook/30_论文研究/01_论文库/From_Code_to_Action_Hierarchical_VLM_2509.24917.pdf"
reading_date: 待补充
reading_status: 已读
related_concepts: ["模仿学习", "VLA架构"]
---

## 🎯 题目

"From Code to Action: Hierarchical Learning of Diffusion-VLM Policies"

# From Code to Action: Hierarchical VLM + Diffusion Policy

## 📝 三句摘要

1. **核心问题**：模仿学习在复杂长时域任务上泛化差、数据稀缺
2. **核心贡献**：层次化框架 — 代码生成 VLM 做高层规划 + 低层 Diffusion Policy 做动作执行
3. **关键洞察**：开源机器人 API 不仅作为执行接口，也是结构化监督的来源（subtask function 作为语义标签）

## 核心创新

### 架构：VLM 高层规划 + Diffusion 低层执行

```
语言任务描述
    ↓
[VLM: 代码生成 + 任务分解] → 分解为可执行子程序（subroutines）
    ↓
[Memory Mechanism] → 维护子程序上下文（处理非马尔可夫任务，如物体交换）
    ↓
[Diffusion Policy] → 根据子程序生成具体动作
```

**关键设计**：
1. **VLM 做任务分解**：把「把红色积木放到蓝色积木上面」分解为「抓红色积木→移到蓝色积木上方→放下」
2. **Subtask functions 作为语义标签**：每个子程序有明确的语义含义
3. **Memory 机制**：跨时间维护子程序上下文，处理非马尔可夫性

### 与 Paper A 的对应关系

**Paper A 的完整技术参考！**

| Paper A 分层 | From Code to Action |
|------------|------------------|
| 高层 VLM 意图 | VLM 代码生成 + 任务分解 |
| 中层意图解析 | Subtask function grounding（语义标签→具体子程序）|
| 低层执行 | Diffusion Policy（生成具体动作）|

**创新性**：
- Paper A 的「中层」在这里是「subtask function grounding」，有明确的语义意义
- Memory 机制处理非马尔可夫性 → 对应 Paper A 的「意图解析器」在长时域任务中的状态维护

## 待探索问题

1. VLM 代码生成是否能在边缘设备（Jetson）上实时运行？
2. Memory 机制的计算开销能否满足 50-100Hz 控制频率？
3. 此框架能否迁移到空中机械臂的长时域任务？


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
- [[模仿学习]]
- [[具身智能]]
- [[VLA]]


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
