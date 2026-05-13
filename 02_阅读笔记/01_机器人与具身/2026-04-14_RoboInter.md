---
paper_id: RoboInter-2602.09973
arXiv: "2602.09973"
title: "RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation"
authors: ["Hao Li", "Ziqin Wang", "Zi-han Ding", "Shuai Yang", "Yilun Chen", "Yang Tian", "Xiaolin Hu", "Tai Wang", "Dahua Lin", "Feng Zhao", "Si Liu", "Jiangmiao Pang"]
venue: "ICLR 2026"
tags: ["D02", "VLA", "具身智能", "数据合成", "灵巧操作"]
status: "[[已入库]]"
pdf_path: ""
date: 2026-04-14
source: "ICLR 2026 Poster | https://iclr.cc/virtual/2026/poster/10009698"
video: "https://b23.tv/4QH1vAd"
github: ""
reviewer: "[[花火]]"
related_concepts: ["数据合成", "灵巧操作"]
summary: "RoboInter 提出了 **中间表征（Intermediate Representation）** 作为 VLM 通用认知能力与机器人底层操作之间的桥梁，补全了具身智能'规划→执行'链路中最关键的一环 构建了包含 **230k+ episodes、571 场景、10+ 类中间表征密集标注**的大规模数据集，配套 VQA 基准和 VLA 模型 核心贡献：**Plan-then-Execute 框架**，支持模块化和端到端 VLA 变体，通过中间表征同时做高层次规划 + 低层次执行"
---

# RoboInter — 面向机器人操作的完整中间表征体系

## 三句摘要

1. RoboInter 提出了 **中间表征（Intermediate Representation）** 作为 VLM 通用认知能力与机器人底层操作之间的桥梁，补全了具身智能"规划→执行"链路中最关键的一环
2. 构建了包含 **230k+ episodes、571 场景、10+ 类中间表征密集标注**的大规模数据集，配套 VQA 基准和 VLA 模型
3. 核心贡献：**Plan-then-Execute 框架**，支持模块化和端到端 VLA 变体，通过中间表征同时做高层次规划 + 低层次执行

## 核心价值评估

| 维度 | 评分 | 说明 |
|------|------|------|
| **创新性** | ⭐⭐⭐⭐ | 提出"中间表征"作为通用具身智能连接层，填补了从互联网 VLM 到真实机器人操作的空白 |
| **工程完整度** | ⭐⭐⭐⭐⭐ | 完整体系：标注工具 + 数据集 + VQA 基准 + VLA 模型，69 页 40 图 |
| **可复现性** | ⭐⭐⭐⭐ | 数据集和工具已开源，ICLR 2026 Poster |
| **对主人的价值** | ⭐⭐⭐⭐ | 中间表征层直接支撑 Paper A 的"高层语义规划→低层控制执行"架构设计；与龙虾 VLN 任务高度相关 |
| **启发实验点** | ⭐⭐⭐⭐ | Plan-then-Execute 框架可迁移到无人机"语义导航→飞行控制"的层级架构 |

## 可落地实验点

- **无人机层级架构**：将 RoboInter 的 Plan-then-Execute 思想迁移到无人机 VLN，语义层（VLM）规划子目标 + 低层 VLA 执行飞行动作
- **中间表征迁移**：在无人机仿真数据上标注中间表征（位置/速度/任务进度），用于训练模块化 VLA
- **大规模仿真数据采集**：参考 RoboInter-Tool 的半自动标注管线，在 UE 中实现自动化大规模采集标注

---

## 📝 详细笔记

### 背景与问题

**核心痛点**：
- VLM 具备互联网级别的通用认知能力
- 但从 VLM 到真实机器人底层操作，缺少一条**自然、稳定、可扩展**的路径
- 现有 Manipulation 数据集：贵、具身特定、覆盖不足 → VLA 泛化受限

**现有解法及其缺陷**：
- **Plan-then-Execute**：先生成高层规划（子任务/轨迹），再翻译为低层动作
- **问题**：这种范式依赖**额外的中间监督信号**，但现有数据集里根本没有这种标注

### 核心贡献：中间表征体系

```
互联网 VLM（通用认知）
        ↓
   中间表征层（IR）← RoboInter 核心补全
        ↓
机器人底层操作（末端执行器控制）
```

**10+ 类中间表征包括**：
- 空间类：物体位置、相对距离、抓取姿态、空间关系
- 时序类：动作阶段、任务进度、轨迹预测
- 语义类：子任务标签、语言指令嵌入

### RoboInter 三大组件

#### 1. RoboInter-Tool（标注工具）
- 轻量级 GUI，支持**半自动标注**多种中间表征
- 大幅降低标注成本

#### 2. RoboInter-Data（数据集）
- **230k+ episodes**
- **571 场景**
- 覆盖 10+ 类中间表征的密集逐帧标注
- 规模和标注质量均大幅超过现有工作

#### 3. RoboInter-VQA（VQA 基准）
- **9 类空间问题**（Where/How far/Which side...）
- **20 类时序问题**（What next/How many steps...）
- 系统性评估 VLM 的具身推理能力

#### 4. RoboInter-VLA（VLA 模型）
- **Plan-then-Execute 框架**
- 两种变体：
  - **模块化**：语义规划器 + 低层 VLA 分阶段执行
  - **端到端**：通过中间表征监督统一训练
- 中间表征作为桥梁，连接高层规划与低层执行

### 关键洞察

1. **中间表征 = 通用→专用的桥梁**：不需要为每个任务单独训练，用中间表征泛化
2. **数据驱动中间监督**：通过 RoboInter-Data 的密集标注，让 VLA 学习"什么时候该规划、什么时候该执行"
3. **半自动标注可行性**：用工具降低大规模具身数据标注成本

### 作者团队

Hao Li, Ziqin Wang, Zi-han Ding, Shuai Yang, Yilun Chen, Yang Tian, Xiaolin Hu, Tai Wang, Dahua Lin, Feng Zhao, Si Liu, Jiangmiao Pang

**机构**：上海AI Lab / 浙大 / 港科大 / 清华大学（推测）

### 补充信息

- **ICLR 2026 Poster**：https://iclr.cc/virtual/2026/poster/10009698
- **arXiv**：https://arxiv.org/abs/2602.09973
- **论文页数**：69 页，40 张图

## 🏷️ 元信息

- **领域**：VLA / 具身智能 / Manipulation / 中间表征 / 数据集
- **关键词**：#RoboInter #中间表征 #PlanThenExecute #VLA #ICLR2026 #具身数据集
- **相关方向**：Paper A（龙虾 VLN）架构设计、无人机层级规划、Sim2Real 数据管线
