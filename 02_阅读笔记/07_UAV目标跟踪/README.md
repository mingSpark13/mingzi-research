# UAV 端到端/分层目标跟踪 — 研究方向导航

> 整理日期：2026-04-07　　整理人：花火🦊
> 来源：明子实习项目需求 + 论文调研

---

## 方向定义

**核心目标**：无人机端到端或分层端到端的稳定人体运动跟随目标跟踪

**应用场景**：冲浪、滑雪等高动态运动场景下的无人机自主跟随拍摄

---

## 🎯 明确技术路线（三阶段递进）

> 核心原则：小中型自采数据集 → 先 CNN+GRU；大数据强算力 → 再考虑 ViT/VideoMAE

### 阶段一：强前端 + GRU baseline（本周 Demo）

```
[RGB 输入] → [YOLO/RTMDet 检测] → [姿态估计器] → [pose/state 序列] → [GRU] → [控制命令]
```

- 前端：YOLO / RTMDet + pose estimator，输出 bbox、2D/3D joints、人体朝向、速度
- 后端：pose/state sequence → GRU → 预测下一时刻人体状态
- 控制：PID 映射到速度命令
- 仿真：UE5 + AirSim（AirSpark 工程）

### 阶段二：升级时序模型（1-2 周）

```
[pose/state 序列] → [PoseFormerV2 / MotionBERT] → [预测 + 控制]
```

- 用 PoseFormerV2（频域高效）或 MotionBERT（预训练运动编码器）替换 GRU
- 接入 YOPOv2 端到端控制框架
- **对打基线**：GRU vs PoseFormerV2，验证数据规模是否支撑 Transformer

### 阶段三：ViT 视觉前端（数据充足后）

```
[视频帧] → [VideoMAE/ViT backbone] → [temporal head] → [控制命令]
```

- 预训练 ViT backbone（VideoMAE 自监督），再在自采数据上微调
- 仅在数据规模/标注质量/算力充足时考虑
- Domain Randomization + Sim2Real 迁移

---

## 论文库

### 感知端（视觉跟踪）

| 论文 | 核心特点 | arXiv | 笔记 |
|---|---|---|---|
| **ORTrack** | ViT + 遮挡鲁棒表征（Cox随机遮挡） | 2504.09228 | ✅ |
| **SGLATrack** | ViT 动态层选择，高效实时 | 2503.06625 | ✅ |
| **T-SiamTPN** | 时间上下文 Siamese + Transformer | 2509.12913 | ✅ |

### 后端时序建模（人体运动预测）

| 论文 | 核心特点 | 角色 | arXiv | 笔记 |
|---|---|---|---|---|
| **VIBE** | CNN + GRU + 对抗训练，视频人体建模经典 | 基线参考 | 1912.05656 | ✅ |
| **TCMR** | VIBE 升级版，时序一致性更强 | 基线升级 | 2011.08627 | ✅ |
| **PoseFormer** | 纯 Transformer 3D 姿态估计开山之作 | 升级版参考 | 2103.10455 | ✅ |
| **PoseFormerV2** | 频域高效 + 噪声鲁棒 | **推荐首选** | 2303.07425 | ✅ |
| **MotionBERT** | 统一运动表征预训练，DSTformer | 竞争选用 | 2210.06551 | ✅ |

### 视觉前端预训练

| 论文 | 核心特点 | 角色 | arXiv | 笔记 |
|---|---|---|---|---|
| **VideoMAE** | 自监督视频预训练，小数据友好 | 阶段三方案 | 2203.12602 | ✅ |

### 控制端（端到端策略）

| 论文 | 核心特点 | arXiv | 笔记 |
|---|---|---|---|
| **YOPOv2-Tracker** | 端到端感知→控制，motion primitives | 2505.06923 | ✅ |

### 综述

| 论文 | 核心特点 | 来源 | 笔记 |
|---|---|---|---|
| **UAV Moving Target Tracking Review** | 滤波/深度学习/回归三大预测路线 | Defence Tech 2025 | ✅ |

---

## 数据集与评测

| 数据集 | 用途 |
|---|---|
| UAV123 | UAV 跟踪标准基准 |
| UAVDT | UAV 检测+跟踪 |
| VisDrone | 无人机视觉理解 |
| Human3.6M | 3D 人体姿态基准 |
| MPI-INF-3DHP | 3D 姿态 in-the-wild |

---

## 与其他研究方向的联系

- **龙虾项目（D06 空中VLN）**：跟踪框架可复用感知模块
- **D01 世界模型**：3DGS 重建可辅助仿真训练数据生成
- **RAL'26 可微物理**：可微仿真加速跟踪策略训练
- **D03 空地迁移**：人体跟踪策略可迁移到地面机器人

---
**维护**: 花火 · 2026-04-07
