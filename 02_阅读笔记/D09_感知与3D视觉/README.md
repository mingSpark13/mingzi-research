# VR & 3D 场景生成资源导航

> 整理日期：2026-04-07　　整理人：花火🦊
> 来源：明子提供的资源清单

---

## 一、工程项目

### WorldGen — 文本/图像 → 3D 场景（秒级生成）
- **GitHub**: https://github.com/ZiYang-xie/WorldGen
- **官网**: https://worldgen.github.io/
- **核心**：text-to-scene + image-to-scene，360° 一致性探索，低显存（~10GB），输出可导入 Unity/Unreal
- **状态**：⭐ 活跃维护（v0.2.0，2026.04 更新）
- **笔记**: `2026-04-07_WorldGen.md`

### GenAI-3D-Virtual-Reality-Augmented
- **GitHub**: https://github.com/ruslanmv/GenAI-3D-Virtual-Reality-Augmented
- **核心**：LLM + Diffusion 生成 360° VR 图像，集成 Unreal Engine + NPC AI + VR headset
- **状态**：工程示例，非严肃研究项目
- **用途**：VR 内容生成 pipeline 参考

### Awesome-3D-Scene-Generation
- **GitHub**: https://github.com/hzxie/Awesome-3D-Scene-Generation
- **核心**：300+ 论文/模型导航库，覆盖规则驱动/LLM+规划/体积场/neural representation 等全方向
- **状态**：⭐ 持续更新，方向导航价值高
- **用途**：快速定位 3D 生成各类方法

---

## 二、学术论文

### AgentWorld (CoRL 2025)
- **arXiv**: 2508.07770
- **核心**：自动化场景构建 + 双模式遥操作的家庭移动操作仿真平台
- **亮点**：支持轮式+人形机器人，sim-to-real 验证，代码+数据集将开源
- **PDF**: `../01_论文库/VR与3D场景生成/AgentWorld_2508.07770.pdf`
- **笔记**: `AgentWorld.md`
- **对主人价值**：⭐⭐⭐ 场景自动构建 → 龙虾仿真数据扩增

### EyeNavGS (2025)
- **arXiv**: 2506.02380
- **核心**：首个 3DGS VR 6-DoF 导航数据集（46人，12场景，头部姿态+眼动）
- **亮点**：开源 SIBR viewer fork with record-and-replay，眼动数据支持 foveated rendering
- **PDF**: `../01_论文库/VR与3D场景生成/EyeNavGS_2506.02380.pdf`
- **笔记**: `EyeNavGS.md`
- **对主人价值**：⭐⭐ 3DGS VR replay 工具链，空中场景渲染优化参考

### SpaceBlender (AVI 2025)
- **arXiv**: 2409.13926
- **核心**：真实物理环境 2D 图像 → 3D VR 协作空间（深度估计+网格对齐+diffusion补全）
- **亮点**：物理+虚拟混合空间生成范式，协作 VR 用户研究
- **PDF**: `../01_论文库/VR与3D场景生成/SpaceBlender_2409.13926.pdf`
- **笔记**: `SpaceBlender.md`
- **对主人价值**：⭐⭐ 真实场景+空中仿真的混合场景构建思路

---

## 三、VR 交互引擎（辅助工具）

| 工具 | 用途 | 地址 |
|---|---|---|
| A-Frame | Web VR 框架，Three.js + WebXR | https://aframe.io |
| OpenSpace3D | 跨平台 XR 引擎，免费 | http://www.openspace3d.com/ |
| Unity XR / Unreal XR | 成熟 VR 交互 + world building | 商业软件 |
| Omniverse Isaac Sim | AI + 3D 仿真，可生成世界数据 | NVIDIA 官方 |
| NVIDIA fVDB | 生成真实 3D 数据集（world model 输入） | NVIDIA 开发者 |

---

## 四、资源聚合

### Awesome-3D-Scene-Generation 重点子方向摘录
（完整列表见 GitHub 仓库）

| 方向 | 代表工作 | 关键特点 |
|---|---|---|
| 规则驱动 Procedural | CityEngine 等 | 可控但需人工设计 |
| LLM + Scene Planning | SceneLLM, LLMS3 | 语义理解强，物理合理性弱 |
| 体积场 Neural Fields | NeRF, 3DGS, Diffusion | 质量高但计算重 |
| 面向游戏/VR 生成 | WorldGen, BuilderBot | 实时性 + 可探索 |

---

## 五、对主人研究的价值总结

### 🔥 最高价值链路
```
WorldGen（场景生成）
    ↓
AgentWorld（任务定义 + 遥操作数据采集）
    ↓
龙虾仿真平台（sim-to-real 训练）
    ↓
EyeNavGS（SIBR replay 验证可视化）
```

### ⭐ 论文产出方向
1. **WorldGen × 龙虾仿真**：空中场景批量自动化生成（novelty：空中场景 × WorldGen）
2. **AgentWorld × 空中操作**：从室内家庭机器人迁移到空中机器人任务定义
3. **EyeNavGS × 自适应渲染**：3DGS 的 foveated rendering 在空中场景的应用

---

## 六、DDL 提醒
- 龙虾 DDL **4/10**（剩余约 3 天），这些资源优先级低于龙虾论文写作
- 建议：龙虾提交后再深入研究本清单中的资源

---
**维护**: 花火 · 2026-04-07
