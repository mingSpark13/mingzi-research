# RoboAgent / RoboAgent Paper

> 多任务机器人操作的数据集与框架

## 📋 基本信息

| 项目 | 说明 |
|------|------|
| 类型 | 多任务机器人操作基准 |
| 机构 | CMU / RoboAgent Team |
| 关键工作 | MT-ACT (Multi-Task ACT) |

## 📝 核心内容

RoboAgent 项目提出了：
1. **多任务操作数据集**：38 种技能，覆盖多种任务
2. **MT-ACT**：作为多任务基线方法
3. **benchmark**：用于评估新模型在多任务场景下的性能

## 🔗 主人提供的技术定位

> MT-ACT 本质上不是一个像 RT/π0 那样"超级大系列品牌"，更像是 multi-task 版本的 ACT/常见 baseline 名称，在多任务 manipulation benchmark 里经常被当成基线拿来比较。

## 💡 与其他工作的关系

```
RoboAgent / MT-ACT
    ↓
多任务模仿学习基线
    ↓
对比更复杂的 VLA (RT-2 / π0 / GR00T)
```

## ⚠️ 注意事项

- MT-ACT 不要想成神秘大山头，它更像「ACT 的多任务化用法/benchmark baseline」
- RoboAgent 的数据规模比 RT 系列小，但更适合作为「入门多任务」的研究起点

---
**维护**: 花火 · 2026-03-27