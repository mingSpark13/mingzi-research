# Self-Forcing 开源仓库笔记

- Repo: https://github.com/guandeh17/Self-Forcing
- 核心论文：[[2026-03-25_Self_Forcing]]
- 定位：训练时模拟推理 rollout 的自回归视频扩散训练框架

## 仓库价值
- 给 InSpatio-World 提供实时自回归推理范式
- 提供 KV caching、rollout 训练、streaming video generation 的工程实现
- 证明单卡 4090 也能接近实时流式视频生成
