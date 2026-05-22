---
title: "ViT（Vision Transformer）基础知识"
date: "2026-03-28"
tags: [ViT, Vision_Transformer, 多模态, 视觉 backbone, 基础知识]
source: "明子学习笔记整理"
context: "VLA/VLM 视觉前端核心组件"
---

# ViT（Vision Transformer）基础知识

## 一句话定义

> **ViT = 把图像切成 patch，当成 token 序列送进 Transformer 的视觉模型。**

---

## 核心流程

```
输入图像（224×224×3）
    ↓ 切 patch（16×16）
196 个 patch 序列
    ↓ 展平 + 线性映射
patch embedding（每个 768 维）
    ↓ 加位置编码
加入 [CLS] token
    ↓
多层 Transformer Encoder
（Multi-Head Self-Attention + FFN + LayerNorm + Residual）
    ↓
输出视觉特征（[CLS] token 或全部 patch tokens）
```

---

## 关键设计

### Patch Embedding
- 把每个 patch 展平成向量，经线性层映射为固定维度 embedding
- 相当于 NLP 里的「词向量」

### 位置编码（Positional Encoding）
- Transformer 本身不知道 token 顺序，必须显式加上位置信息
- 让模型区分「天在上、草在下」和「草在上、天在下」

### [CLS] Token
- 放在序列最前面的特殊 token
- 经过多层 attention 后，聚合全图信息
- 用于分类任务（类似 BERT 的 [CLS]）

---

## ViT vs CNN

| 维度 | ViT | CNN |
|------|------|-----|
| 归纳偏置 | 弱（更依赖数据）| 强（局部感受野、平移不变性）|
| 长距离依赖 | 强（self-attention 全局建模）| 弱（多层卷积堆叠）|
| 大数据/大模型 | 很强 | 相对受限 |
| 小数据 | 不如 CNN 稳定 | 更稳 |
| 与 LLM 接驳 | 自然（token 序列）| 需要额外设计 |
| 局部细节建模 | 不如 CNN 强 | 天然优势 |

**一句话**：CNN 像逐层扫描提炼，ViT 像全局关系建模。

---

## ViT 为什么适合 VLA/VLM

### 1. 全局关系建模
- 直接建模图像任意位置之间的关系
- 适合空间 grounding、导航、物体关系推理

### 2. 与语言模型天然接驳
- 输出 = token 序列，和 LLM 输入格式一致
- 视觉 token + 文本 token → 一起送入多模态模型

### 3. 适合大模型化
- Scaling law：数据↑ + 参数↑ + 算力↑ → 性能↑
- 成为大视觉模型的基础模块

### 4. 多模态融合方便
- 当前图像 + 历史图像 + 文本指令 + 状态向量 → 统一 token 序列

---

## ViT 在 VLA 系统里的角色

```
RGB Image
    ↓
ViT（视觉编码器）→ 提取视觉语义特征（场景布局、物体位置、空间关系）
    ↓
Projector（模态对齐）→ 映射到 LLM 的 embedding 空间
    ↓
LLM（语言/推理）→ 结合文本指令做高层规划
    ↓
Action Module（动作解码）→ 输出控制指令/轨迹意图
```

**ViT 的角色**：视觉大脑前端，负责「看见什么、场景是什么结构、目标在哪里」，不直接负责控制执行。

---

## 常见 ViT 变体

| 名称 | 特点 |
|------|------|
| 原始 ViT | 经典版本，直接 patchify + Transformer |
| DeiT | Data-efficient Image Transformer，更高效的数据利用和蒸馏 |
| Swin Transformer | 层次结构 + 局部窗口 attention，更像 CNN 金字塔结构 |
| CLIP ViT | CLIP 的视觉编码器，很多 VLM/VLA 的视觉前端 |
| DINO / DINOv2 | 自监督学习，提取通用视觉特征能力强 |

---

## 在机器人/无人机场景的直观类比

**CNN 的感知方式**：
- 先看边缘 → 再看纹理 → 再看局部目标 → 一层层往上堆

**ViT 的感知方式**：
- 把画面切成很多区域 → 让每个区域彼此交流
- 哪块是门、哪块是墙、哪块是目标
- 区域之间的关系一起被建模
- 最后形成整张图的全局理解

对于「导航、空间 grounding、长时任务、语言条件控制」，ViT 往往更顺手。

---

## 核心优缺点

### ✅ 优点
- 全局关系建模能力强
- 适合大规模预训练
- 和多模态系统兼容性好（视觉 + 语言）
- 结构统一，NLP/Vision 共享 Transformer 范式

### ❌ 缺点
- 小数据场景不如 CNN 稳定
- 计算量随 token 数量增长（attention O(N²)）
- 局部细节建模不如 CNN（需要额外设计弥补）

---

## 关联概念

- [[多模态大模型]] — ViT 是视觉编码器的标准选择
- [[VLA]] — ViT 作为视觉前端
- [[CLIP]] — CLIP ViT 是很多 VLM 的视觉 backbone
- [[CNN vs Transformer]] — 两者在机器人任务中的选型对比

---

**关联笔记**：
- [[SFT_RLHF_RFT_后训练方法]] — 大模型后训练方法笔记
- [[VLA_相关论文]] — 具身智能 VLA 论文汇总
