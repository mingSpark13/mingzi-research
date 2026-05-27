---
title: "π, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation"
authors: 未在笔记中记录
arxiv: 2603.25038
date: 2026-03-31
institution: 未在笔记中记录
conf: arXiv
keywords: [aerial manipulation, VLA, transfer learning, diffusion policy, gaussian splatting]
tags: [空地迁移, VLA架构, 数据合成, 动力学约束]
domain: 空地迁移
pdf_path: ""
reading_date: 2026-04-05
reading_status: 已读
summary: "将地面VLA迁移到空中操作时，视觉表征可复用但动力学失配明显，论文提出Payload-Aware Guidance与Gaussian Splatting数据增强来弥合这一gap。"
related_concepts: ["空地迁移", "VLA架构", "数据合成", "动力学约束"]
---

# π, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation

- **arXiv**: 2603.25038
- **方向**: 方向03（空地迁移）
- **入库时间**: 2026-04-05
- **研究轮次**: R459

## 一句话摘要
研究如何将固定基座VLA模型（π₀）迁移到空中平台，发现视觉表征可迁移但控制动力学无法迁移，提出Payload-Aware Guidance机制在diffusion采样中注入有效载荷约束，并结合Gaussian Splatting合成数据，在460次真机实验中验证100%成功率。

## 核心贡献
1. **发现 dynamics gap**：VLA视觉表征能泛化，但动作输出因基座不同（固定→飞行）而完全失效
2. **Payload-Aware Guidance**：无需重训练基础模型，在diffusion sampling中注入payload约束，使VLA适应空中平台动力学
3. **Gaussian Splatting合成数据**：解决空中训练数据稀缺问题
4. **460次真机实验验证**

## 为什么有价值
- 主人正在做无人机+机械臂VLA迁移，这是目前最直接的"地面VLA→空中平台"迁移路线
- Payload-Aware Guidance不依赖重训练，对主人的快速验证场景很有价值
- Gaussian Splatting数据合成路线与主人实习的3DGS方向高度契合

## 可落地实验点
- Payload-Aware Guidance机制可直接迁移到主人的空中机械臂控制——在diffusion策略的采样过程中注入无人机动力学约束，而不是重训练整个VLA
- Gaussian Splatting合成数据路线可作为主人龙虾项目的数据增强方案——用3DGS重建室内场景+合成语言指令数据
