---

summary: "2026-04-10_OpenFly_A_Comprehensive_Platform_for_Aerial_Vision-Language_Navigation"
title: "OpenFly: A Comprehensive Platform for Aerial Vision-Language Navigation"
authors: Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan Chen, Qizhi Chen, Zhonghan Tang, Liansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Xuelong Li, Zhigang Wang, Bin Zhao
arxiv: 2502.18041
date: 2025-02-25
institution: 暂未统一标注
conf: ICLR 2026
keywords: aerial vision-language navigation, aerial VLN, benchmark, 3D Gaussian Splatting, keyframe selection, real-to-sim
tags: ["D06", "空中VLN", "跨载体泛化"]
domain: 空中操作
pdf_path: ../../01_论文库/空中操作/2502.18041_OpenFly_A_Comprehensive_Platform_for_Aerial_Vision-Language_Navigation.pdf
reading_date: 2026-04-10
reading_status: 已读
related_concepts: ["空中VLN", "跨载体泛化"]
---

## 🎯 题目

OpenFly: A Comprehensive Platform for Aerial Vision-Language Navigation

## 📝 三句摘要

1. **问题背景**：空中视觉语言导航比室内 VLN 更缺数据和基准，因为外场航拍视角覆盖范围大、采集成本高、真实环境构建困难。
2. **核心方法**：论文提出 OpenFly 平台，统一整合 Unreal Engine、GTA V、Google Earth、3D Gaussian Splatting 等多种渲染源，并配套自动化工具链生成轨迹、语义信息和指令，同时提出 keyframe-aware 的 OpenFly-Agent。
3. **关键结果**：基于该工具链构建了覆盖 18 个场景、10 万条轨迹的 AVLN 基准，实验表明 OpenFly 平台与 OpenFly-Agent 在 seen / unseen 设定下都优于多种近期 VLN 方法。

## 💎 价值评估

- **🔬 研究价值**：这篇工作把“空中 VLN 缺 benchmark、缺数据工厂、缺统一平台”三个瓶颈一起补上，意义不只是出一个新模型，而是给整个方向搭了基础设施。
- **🚀 实践价值**：对无人机具身导航项目很实用，尤其适合借鉴它的多引擎统一接口、自动轨迹生成、自动指令生成和 keyframe 压缩链路。
- **📈 扩展潜力**：后续很适合作为 D06 的数据底座，与 AirNav 的真实基准、APEX 的解耦 explorer 主线拼接，形成更完整的训练,评测,部署闭环。

## 🎯 可落地实验点

**实验设计**：把 OpenFly 的关键帧筛选与 visual token merging 思路接到现有龙虾 VLM 前端，验证在开放式目标搜索中是否能降低推理延迟并保持导航成功率。
- 对比基线：不做关键帧筛选的原始多帧输入；固定间隔抽帧；OpenFly 风格关键帧选择
- 度量指标：目标搜索成功率、平均轨迹长度、单步推理延迟、token 数量、重规划恢复率
- 预期结果：关键帧策略在几乎不损失成功率的前提下，降低前端时序冗余与延迟开销

## 🔗 知识图谱
- [[VLA]] - OpenFly-Agent 属于视觉语言动作导航模型路线
- [[具身智能]] - 空中 VLN 是具身智能在无人机平台上的关键子方向
- [[空中操作]] - 该工作可作为无人机导航到后续空中操作的前置基础设施
- [[3D高斯溅射]] - 论文把 3DGS 引入真实到仿真的场景构建链路
- [[Sim2Real]] - 通过 3DGS 与真实外场验证增强 sim-to-real 相关性
- [[主动感知]] - OpenFly-Agent 的关键帧选择本质上是在做任务相关观测压缩

## 🔗 相关链接

链接本文核心引用的论文（baseline/SOTA/基础工作）：

- [[2026-04-08_AerialVLA_Vision_Language_Action_Model_for_UAV_Navigation]] - 空中 VLN / VLA 主线代表方法，适合作为轻量端到端基线对照
- [[2026-04-09_AirNav_真实城市空中视觉语言导航基准]] - 提供真实城市空中 VLN benchmark，与 OpenFly 的合成平台路线互补
- [[2026-04-09_APEX_解耦式空中目标导航框架]] - 提供动态语义建图与目标引导探索主骨架，可与 OpenFly 数据平台结合
- [[2025-04-09_HUGE-Bench_Holistic_UAV_Generalization_Evaluation_Benchmark]] - 同样强调空中具身评测基础设施，适合做 benchmark 维度上的横向对照

## 📌 待探索问题

- OpenFly 的 4-DoF 离散动作设定迁移到更真实的 6-DoF 无人机控制时，关键帧策略是否仍然稳定有效？
- 多引擎统一接口虽然强大，但不同引擎间视觉统计分布差异会不会给策略学习带来额外 domain gap？
- OpenFly-Agent 更偏历史压缩和轻量 VLN，若接到开放式语义搜索任务中，是否需要和显式 explorer / frontier map 结合？
- 3DGS real-to-sim 场景对真实外场泛化到底带来多少增益，是否值得单独做 ablation？

---
**维护**: 花火 · 2026-04-12
