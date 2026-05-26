# World Model × RL 研究机会（主人视角）

## 当前链路里最值得盯的三个切口

### 1. 世界状态模型 + 世界动作模型耦合
- 上游：[[2026-03-19_InSpatio_WorldFM]] / [[2026-03-25_InSpatio-World_开源仓库笔记]]
- 下游：[[2026-03-26_DreamZero_World_Action_Models_are_Zero-shot_Policies]]
- 机会：把 state-anchored 4D world 和 zero-shot action policy 接起来

### 2. 几何锚定 world model for robotics
- 上游：[[2026-03-25_Depth_Anything_3]] / [[2026-03-25_3D_Gaussian_Splatting]]
- 机会：让机器人世界模型不只会“想象视频”，还能维护几何一致世界

### 3. 实时自回归策略生成
- 上游：[[2026-03-25_Self_Forcing]] / [[2026-03-25_Wan_Open_and_Advanced_Large_Scale_Video_Generative_Models]]
- 机会：把流式 rollout 能力迁移到动作预测与闭环控制

## 最值得优先复现的顺序
1. DreamZero（动作策略导向）
2. InSpatio-World（世界状态导向）
3. Self-Forcing（实时 rollout 训练法）
4. DA3 + 3DGS（几何锚定能力）

## 为什么重要
主人当前正处在：
- 零零科技实习
- 3DGS 学习路线
- 世界模型学习路线

这条链正好是主人未来最可能切进去的研究主线之一。
