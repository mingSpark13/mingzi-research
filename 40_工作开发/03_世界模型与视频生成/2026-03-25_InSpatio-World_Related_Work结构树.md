# InSpatio-World Related Work 结构树

> 目标：直接服务论文/综述写作，把 InSpatio-World 放进一条清晰的技术谱系里。

## 一、几何世界建模（Geometry-grounded World Modeling）

### 1. 静态场景视图合成
- [[2026-03-25_NeRF]]
- [[2026-03-25_3D_Gaussian_Splatting]]

**要点**：
- NeRF 证明了场景可以被连续辐射场建模并从任意视角渲染。
- 3DGS 进一步把质量与实时性交到一起，让“可交互几何世界”更可行。

### 2. 动态场景 / 4D 重建
- [[2026-03-25_Dynamic_View_Synthesis_from_Dynamic_Monocular_Video]]
- [[2026-03-25_DynIBaR]]

**要点**：
- 视频不仅是图像序列，更是时变 4D 场景的投影。
- 这条线强调世界的时空一致性，而不是单帧生成质量。

---

## 二、相机可控视频生成与重渲染（Camera-controlled Video Generation）

### 1. 单视频动态新视角生成
- [[2026-03-25_GCD_Generative_Camera_Dolly]]

### 2. 轨迹级视频控制
- [[2026-03-25_Trajectory_Attention]]

### 3. 3D-aware 视频控制
- [[2026-03-25_Diffusion_as_Shader]]

### 4. 系统化视频重拍框架
- [[2026-03-25_ReCamMaster]]

**要点**：
- 这一阶段的核心转变，是从“生成像视频的内容”走向“生成满足相机轨迹约束的视频”。
- ReCamMaster 已经很接近 InSpatio-World 当前开源实现的表层任务形式。

---

## 三、实时自回归视频基础模型（Autoregressive Real-time Video Models）

### 1. 视频基础模型
- [[2026-03-25_Wan_Open_and_Advanced_Large_Scale_Video_Generative_Models]]

### 2. 训练-推理一致性与流式 rollout
- [[2026-03-25_Self_Forcing]]

**要点**：
- Wan 提供开放视频生成底座。
- Self-Forcing 解决 rollout 时的 train-test gap，使系统更接近实时交互。
- InSpatio-World 在工程血缘上正是“Wan + Self-Forcing”的系统化扩展。

---

## 四、感知辅助模块（Perception Auxiliaries）

### 1. 几何恢复
- [[2026-03-25_Depth_Anything_3]]

### 2. 视觉语义描述
- [[2026-03-25_Florence_2]]

**要点**：
- DA3 为生成模型提供显式几何锚点。
- Florence-2 负责把参考视频语义化、提示化。
- 它们共同说明世界模型不是纯生成问题，而是“语义 + 几何 + 动态”的系统协同问题。

---

## 五、世界模型叙事与评价

- [[2026-03-19_InSpatio_WorldFM]]
- [[2026-03-25_WorldScore]]
- [[2026-03-25_InSpatio-World_开源仓库笔记]]

**要点**：
- InSpatio-World 把前述分散技术线统一叙述成 state-anchored 4D world model。
- WorldScore 则反映了评价目标从“视频质量”转向“世界一致性、动态一致性、交互性”的趋势。

---

## 可直接写进论文的压缩表述

> Existing works on world-oriented video modeling can be roughly organized into four lines: geometry-grounded scene representation, camera-controlled video generation, autoregressive real-time video synthesis, and perception auxiliaries. InSpatio-World lies at the intersection of these lines by combining explicit geometric anchoring, controllable video rerendering, and real-time autoregressive video generation into a unified state-anchored 4D world modeling pipeline.
