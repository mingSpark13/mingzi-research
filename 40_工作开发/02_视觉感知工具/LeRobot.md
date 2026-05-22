# LeRobot — Hugging Face 机器人学习框架

> 官方文档: https://huggingface.co/docs/lerobot

## 📋 基本信息

| 项目 | 说明 |
|------|------|
| 类型 | 机器人模仿学习框架 |
| 机构 | Hugging Face |
| 官方文档 | https://huggingface.co/docs/lerobot |
| 核心 Policy | ACT (新手首推) |

## 🎯 定位

LeRobot 是**完整机器人操作框架**，包含：

- **数据格式标准化**：统一的 robot data format
- **Policy 训练**：ACT、Diffusion Policy 等
- **仿真/实机部署**：支持多种机器人平台
- **开源复现**：降低了机器人学习门槛

## 📝 主人提供的技术定位

> LeRobot 现在仍把 ACT 当成新手起步的首推 policy。能把「数据采集—训练—评测—部署」全讲清楚的完整闭环。

## 💡 主人建议的项目路线

```
数据采集（示教/VR/键鼠）
    ↓
LeRobot 数据格式标准化
    ↓
ACT / Diffusion Policy 训练
    ↓
仿真评测 (MuJoCo / Isaac Sim)
    ↓
实机部署
```

## 🎯 项目卖点

主人建议的项目可以强调：
1. 我懂 imitation policy（ACT / DP）
2. 我懂数据流和部署
3. 我能接仿真和实机
4. 我能做 benchmark 对比（ACT vs DP）

## ⚠️ 注意事项

- LeRobot 的 ACT 是官方新手首推，但这不意味着它是 SOTA，而是最适合入门
- 数据格式统一是其核心价值之一
- 建议与主人已有经验结合（ACT、DP 实践经验）

---
**维护**: 花火 · 2026-03-27