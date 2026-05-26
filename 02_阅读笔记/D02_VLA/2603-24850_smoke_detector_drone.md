---
title: "Towards automatic smoke detector inspection: Recognition of the smoke detectors in industrial facilities and preparation for future drone integration"
authors: ["Lukas Kratochvila", "Jakub Stefansky", "Simon Bilik", "Robert Rous", "Tomas Zemcik", "Michal Wolny", "Frantisek Rusnak", "Ondrej Cech", "Karel Horak"]
arxiv: 待补充
date: "2026-03-27"
institution: 待补充
conf: 待补充
keywords: 待补充
tags: ["D02"]
domain: 通用操作
pdf_path: ""
reading_date: 待补充
reading_status: 已读
related_concepts: ["空中操作"]
---

## 🎯 题目

"Towards automatic smoke detector inspection: Recognition of the smoke detectors in industrial facilities and preparation for future drone integration"

## 📝 三句摘要
提出面向工业设施烟雾探测器的自动检测系统，对比 YOLOv11 和 RT-DETRv2 在工业场景下的性能，为未来无人机巡检奠定基础。

## 📝 三句摘要
1. 工业消防烟雾探测器因安装位置高、难以接近，自动检测系统可显著提升巡检效率、降低人员风险；
2. 论文对比了 CNN-based 检测器（YOLOv11、SSD）和 Transformer-based RT-DETRv2 在真实/半合成数据上的表现，并探索了多种训练策略；
3. 最优模型 YOLOv11n 在 mAP@0.5 达到 0.884，同时提出可集成到无人机系统的 pipeline 方案。

## 💎 价值评估
⭐⭐⭐（中等）
- 工业检测 + 无人机方向，与主人无人机背景契合
- 论文质量中等偏下，非顶会，方法较常规
- 工程参考价值高于学术创新价值，适合作为应用场景参考

## 🎯 可落地实验点
借鉴其半合成数据增强策略，结合主人无人机平台设计一套高空设施检测的 data engine pipeline。

## 🔗 知识图谱
- 相关方向：[[03_空地迁移]]
- 关联工具：YOLOv11, RT-DETRv2


## 🔗 相关链接

- [[待补充相关论文]] - 待补充核心基线 / 相关工作


## 📌 待探索问题

- 该工作的关键假设在真实场景中是否成立？
- 如果接到当前研究主线里，最先需要补哪一块实验验证？

---
**维护**: 花火 · 2026-04-12
