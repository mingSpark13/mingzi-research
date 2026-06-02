---
title: "Nav-R2: Efficient Open-Vocabulary ObjectNav with Single RGB Input"
authors: ""
arxiv: ""
date: 2025/2026
institution: AMAP-EAI
conf: ""
keywords: RGB-only, open-vocabulary, object-goal navigation, 2Hz inference, SFT training
tags: ["D06"]
domain: 语义导航
pdf_path: ""
reading_date: 待补充
reading_status: 已读
summary: "Nav-R2只用第一视角RGB实现开放词汇目标导航，在OVON val-unseen达到44.0% SR / 18.0% SPL，并把高层语义决策接口压成适合对接底层MPC的轻量形态。"
related_concepts: ["Sim2Real", "MPC"]
---

## 🎯 题目

Nav-R2: 高效开放词汇目标导航（RGB单输入）

## 📝 三句摘要

1. **问题背景**：很多视觉语言导航方法依赖深度图、RGB-D 或多传感器融合，输入复杂度高，部署到真实机器人时硬件适配成本大。
2. **核心方法**：仅用第一视角 RGB + SFT 训练，实现 open-vocabulary ObjectNav，推理速度约 2 Hz；在 OVON val-unseen 上达 44.0% SR / 18.0% SPL。
3. **关键结果**：RGB-only 输入即可达到接近多传感器方法的效果，推理速度 2 Hz 适合高层导航决策，对接低层 MPC/locomotion policy 非常方便。

## 💎 价值评估

- **🔬 研究价值**：证明了 RGB-only 语义导航的可行性，为资源受限平台提供了轻量解决方案。
- **🚀 实践价值**：与主人"给龙虾 RGB 图像，输出往哪走"的接口设想高度吻合，是高层语义导航头的最佳候选。
- **📈 扩展潜力**：2 Hz 推理频率配合底层 50-100 Hz 控制，可形成完整的语义决策→运动执行闭环。

## 🎯 可落地实验点

**实验设计**：在真实室内场景验证 RGB-only 语义导航与底层控制器的闭环
- 对比基线：VLFM（多传感器版本）
- 度量指标：SR、SPL、Inference Latency、Perception-to-Action Delay
- 预期结果：Nav-R2 在降低输入复杂度同时保持 SR 不低于 VLFM 90%

## 🔗 知识图谱
- [[RGB单目视觉]]
- [[开放词汇目标检测]]
- [[高效推理]]
- [[视觉语言动作模型]]
- [[Sim2Real]]

## 🔗 相关链接

- [[2024_VLFM_Vision-Language_Frontier_Maps]] - VLFM 是核心对比基线，Nav-R2 专注 RGB-only 轻量化路线
- [[2025_NaVILA_Two-Level_VLA_Navigation]] - NaVILA 同年工作，同样关注高层语义+低层控制分离

## 📌 待探索问题

- 2 Hz 推理在快速避障场景下是否足够？是否有预测模块来弥补决策频率不足？
- RGB-only 方法在光照变化剧烈或暗光环境下鲁棒性如何？是否有数据增强策略？

---
**维护**: 花火 · 2026-04-12
