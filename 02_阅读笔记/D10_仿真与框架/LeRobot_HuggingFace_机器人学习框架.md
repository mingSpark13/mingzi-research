---
title: "LeRobot: Hugging Face 机器人学习开源框架 (v0.5)"
authors: ["Hugging Face"]
arxiv: 待补充
date: 待补充
institution: 待补充
conf: 待补充
keywords: 待补充
tags: []
domain: 通用操作
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["遥操作"]
---

## 🎯 题目

"LeRobot: Hugging Face 机器人学习开源框架 (v0.5)"

## 📝 三句摘要

1. **定位**：Hugging Face 出品的首个机器人学习开源框架，主打"硬件无关、标准数据集、前沿模型、开源生态有机统一"，v0.5.1 版本包含 321 个源文件、9 万行代码。
2. **核心架构**：六层代码架构（CLI → 策略模型 → 数据管线 → 机器人抽象 → 硬件驱动 → 基础设施），统一了 11 种机器人 + 13 种遥操作设备的接口。
3. **支持的模型**：15 种 AI 策略模型（ACT / Diffusion / Pi0 / GR00T / SmolVLA 等），支持模仿学习、RL、VLA 三大范式。

## 💎 价值评估

**与主人研究方向的相关度**：⭐⭐⭐⭐⭐
主人研究空中机械臂+具身智能，LeRobot 是**最容易上手的机器人学习框架**，HuggingFace 生态集成度高，和 Paper A 的低层执行层完全对齐。

**核心亮点**：
- **硬件抽象层**：一行代码切换不同机器人（Franka/Unitree/ALOHA等）
- **数据集 v3.0**：HuggingFace 生态，直接用 Hub 上的机器人数据集
- **15 种策略模型**：ACT/Diffusion/Pi0/GR00T/SmolVLA 等前沿模型全覆盖
- **16 个命令行工具**：覆盖数据采集、训练、评估、部署全流程

## 核心内容（来自视频解读）

### 六层代码架构

| 层级 | 功能 |
|------|------|
| **CLI** | 命令行工具，16 个完整工作流命令 |
| **策略模型** | 15 种模型：ACT / Diffusion / Pi0 / GR00T / SmolVLA 等 |
| **数据管线** | LeRobot Dataset v3.0，HuggingFace Hub 集成 |
| **机器人抽象** | 统一接口，11 种机器人 + 13 种遥操作设备 |
| **硬件驱动** | 硬件无关，支持多种传感器 |
| **基础设施** | 日志、可视化、配置系统 |

### 支持的 15 种 AI 策略模型
- ACT (Action Chunking Transformer)
- Diffusion Policy
- Pi0 (Physical Intelligence)
- GR00T (NVIDIA)
- SmolVLA
- 及其他 10 种

### 三大范式对比

| 范式 | 适用场景 | LeRobot 支持 |
|------|---------|------------|
| **模仿学习 (IL)** | 有专家演示数据 | ✅ BC, ACT |
| **强化学习 (RL)** | 无演示，需要探索 | ✅ PPO 等 |
| **VLA (视觉-语言-动作)** | 大模型 + 机器人 | ✅ GR00T, Pi0, SmolVLA |

### 硬件抽象层支持的机器人
- Franka Emika Panda
- Unitree 系列
- ALOHA 双手臂
- Humanoid 人形
- 等 11 种

### 遥操作设备
- 13 种，包括：键盘/手柄/遥操作臂/VR设备等

## 与主人研究的关联

1. **Paper A 低层执行层**：LeRobot 的 ACT/Diffusion Policy 实现可以直接作为 Paper A 的低层控制器
2. **数据采集**：LeRobot 的标准化数据采集流程可用于采集空中机械臂的演示数据
3. **VLA 集成**：GR00T/SmolVLA 可以作为 Paper A 高层 VLM 意图层的视觉-语言主干

## 🔗 知识图谱
- 相关方向：02_VLA / 03_空地迁移 / 05_仿真工具
- 关联框架：IsaacLab（仿真层）+ LeRobot（学习层）+ HuggingFace（生态）
- 技术路线：模仿学习 → 强化学习 → VLA 端到端


## 🎯 可落地实验点

**实验设计**：待补充
- 对比基线：待补充
- 度量指标：待补充
- 预期结果：待补充


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
