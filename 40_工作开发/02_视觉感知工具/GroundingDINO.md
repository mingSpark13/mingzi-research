# Grounding DINO / Grounding DINO 1.5

> 开放词汇目标检测器，常与 SAM 组合成「Grounded SAM」

## 📋 基本信息

| 项目 | 说明 |
|------|------|
| 类型 | 开放词汇目标检测 (Open-vocabulary Detection) |
| 机构 | IDEA Research |
| GitHub | https://github.com/idea-research/groundingdino |

## 🎯 定位

Grounding DINO 是**感知层组件**，专为机器人设计：

- **核心能力**：用文本提示检测任意类别物体（不需预先定义类别）
- **典型用法**：`"red mug"` / `"blue screwdriver"` 等自然语言定位目标
- **组合用法**：常与 SAM 组合成 Grounded SAM（检测→分割）

## 🔗 与 SAM 的组合

```
Grounding DINO (文本检测) → SAM (精确分割) → 下游任务
```

## 📝 主人提供的技术定位

> 开放词汇/开放世界检测选 Grounding DINO / Grounding DINO 1.5。适合机器人，因为你经常不想把所有类别写死，而是想用文字提示找"red mug""blue screwdriver"这种目标。

## 💡 在机器人项目中的用法

1. **开放词汇抓取**：`"the blue cup"` → Grounding DINO 检测 → SAM 分割 → GraspNet 抓取
2. **文本指定操作对象**：语言指令中的目标物体定位
3. **场景理解**：用自然语言描述场景中的物体

## ⚠️ 注意事项

- Grounding DINO 是检测器，SAM 是分割器，两者职责不同
- 在机器人上部署时需考虑推理延迟
- 适合「不知道所有物体类别」的真实世界场景

---
**维护**: 花火 · 2026-03-27