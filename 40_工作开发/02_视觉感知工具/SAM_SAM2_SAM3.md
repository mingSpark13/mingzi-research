# SAM / SAM 2 / SAM 3

> Meta 的 Segment Anything Model 系列

## 📋 基本信息

| 项目 | 版本 | 发布机构 | 时间 |
|------|------|----------|------|
| SAM | 初代 | Meta AI | 2023 |
| SAM 2 | 图像+视频 | Meta AI | 2024 |
| SAM 3 | 检测+分割+跟踪统一版 | Meta AI | 2025 |

## 🎯 定位

SAM 系列不是端到端机器人 policy，而是**感知层组件**，主要用于：
- 交互式数据标注
- open-world mask proposal
- 检测/跟踪/分割一体前端

## 🔗 核心链接

- SAM 2 官方: https://ai.meta.com/research/sam2/
- SAM 3 官方博客: https://ai.meta.com/blog/segment-anything-model-3/

## 📝 主人提供的技术定位

> SAM3: Meta 2025 公布，升级成「检测+分割+跟踪的统一模型」，支持基于 concept prompt 的 Promptable Concept Segmentation，并开源了 SAM 3 和新 benchmark。

## 💡 在机器人项目中的用法

SAM 系列通常和以下模块串联：
1. **Grounding DINO** → 文本定位目标物体
2. **SAM** → 分割出精确 mask
3. **FoundationPose / GraspNet** → 6D pose 或抓取候选
4. **ACT / Diffusion Policy** → 动作执行

```
文本指令 → Grounding DINO(检测) → SAM(分割) → 抓取/位姿估计 → 机械臂执行
```

## ⚠️ 注意事项

- SAM 系列本身不输出动作，是感知层工具
- 实际部署时通常和 YOLO、Grounding DINO 配合使用
- SAM 3 的 promptable concept segmentation 是新特性，值得关注

---
**维护**: 花火 · 2026-03-27