---
title: "Training data-efficient image transformers & distillation through attention"
authors: Hugo Touvron, Matthieu Cord, Matthijs Douze, Francisco Massa, Alexandre Sablayrolles, Hervé Jégou
arxiv: 2012.12877
date: 2020-12-23
institution: Facebook AI
conf: ICML 2021
keywords: [Vision Transformer, knowledge distillation, image classification, DeiT, teacher-student]
tags: [多模态统一架构, 模仿学习, 数据合成]
summary: "DeiT 证明 Vision Transformer 可在 ImageNet 级数据上高效训练，并用 distillation token 把 CNN 教师知识稳定蒸馏进 Transformer。"
domain: 多模态学习
pdf_path: "../../01_论文库/多模态学习/2012.12877_DeiT.pdf"
reading_date: 2026-05-20
reading_status: 已读
related_concepts: ["多模态统一架构", "模仿学习", "数据合成"]
---

# 🎯 题目

Training data-efficient image transformers & distillation through attention（数据高效图像Transformer与注意力蒸馏）

# 📝 三句摘要

1. **问题背景**：原始 ViT 需要在 JFT-300M 等超大规模数据集上预训练才能达到 SOTA，训练成本极高，限制了其在实际场景中的应用。
2. **核心方法**：提出 DeiT（Data-efficient image Transformers），仅用 ImageNet 训练即可达到竞争性性能；创新性地引入 distillation token，使 student Transformer 通过注意力机制从 CNN 教师模型学习。
3. **关键结果**：DeiT-B（86M 参数）仅用 ImageNet 达到 83.1% top-1 精度，结合 CNN 教师蒸馏可达 85.2%，训练时间仅需 3 天单卡。

# 💎 价值评估

- **🔬 研究价值**：首次证明 Transformer 可在中等规模数据集（ImageNet 1.2M）上高效训练无需外部数据；蒸馏token设计为 Transformer 知识蒸馏提供了新范式，推动了 ViT 在资源受限场景的普及。
- **🚀 实践价值**：单卡 3 天训练成本可控；HuggingFace transformers 已有官方支持；CNN 作为教师的蒸馏策略可直接迁移到其他 ViT 变体训练。
- **📈 扩展潜力**：蒸馏token设计可与 ViT-S/DeiT-III/MAE 等后续工作结合；可探索用更大 ViT 作为教师进一步提升学生模型性能。

# 🎯 可落地实验点

**实验设计**：将 DeiT 蒸馏策略应用于无人机图像分类任务

- 对比基线：直接用 ImageNet 预训练 ViT-B/16（无蒸馏）；CNN（RegNetY）教师
- 度量指标：top-1 accuracy、FLOPS/参数量效率
- 预期结果：在自有无人机数据集（~10K 图）上，DeiT 蒸馏策略应比直接训练 ViT 提升 3-5% 精度

**核心蒸馏实现要点**：
```python
# 1. 添加 distillation token（与 cls token 并行）
distillation_token = nn.Parameter(...)  # 可学习

# 2. 双重损失函数
loss_ce = F.cross_entropy(student_logits, labels)
loss_distill = F.cross_entropy(
    student_soft_logits, teacher_soft_logits
) / T**2  # 温度蒸馏
total_loss = loss_ce + lambda * loss_distill

# 3. 学生从教师的 attention map 学习（可选）
# 通过 attention 损失强迫学生 attention pattern 接近教师
```

# 🔗 知识图谱

- [[多模态统一架构]] - 本文核心架构 Vision Transformer，属于多模态统一架构
- [[模仿学习]] - 蒸馏本质是 teacher-student 策略，属于知识蒸馏型模仿学习
- [[数据合成]] - 通过蒸馏弥补小数据集不足，本质是数据增强型知识迁移

# 🔗 相关链接

- [[2020_ViT]] - Vision Transformer 奠基工作，本文在其基础上解决数据效率问题
- [[2021-06_如何通过蒸馏提到ViT模型的准确率]] - 本文核心方法论补充

# 📌 待探索问题

- DeiT 的 distillation token 设计是否可迁移到多模态 VLM（如 LLaVA）的训练中？
- 使用更大的 ViT（如 ViT-L）作为学生模型、ConvNeXt 作为教师，是否能在保持效率的同时进一步提升性能？

---
**维护**: 花火 · 2026-05-20
