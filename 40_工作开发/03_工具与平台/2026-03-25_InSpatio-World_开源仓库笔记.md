# InSpatio-World 开源仓库笔记

- Repo: https://github.com/inspatio/inspatio-world
- 定位：reference-video-based real-time interactive 4D world model 的工程化开源实现
- 技术链路：Florence-2 → DA3 → point cloud → InSpatio-World v2v inference
- 底座致谢：Self-Forcing、Wan2.1、Depth-Anything-3、Florence-2、ReCamMaster

## 关键结论
1. 当前开源仓库更像“几何锚定 + 生成式视频重渲染”的系统落地版。
2. README 中 world model / state-anchored 叙事更偏研究目标，而现实现以 novel-view video pipeline 为主。
3. 其重要性在于把多条分散路线真正串成了一个可运行工程。

## 环境要求
- Python 3.10
- CUDA 12.1
- torch 2.5.1 + cu121
- 14B 模型建议 24GB+ 显存；1.3B 更适合轻量实验

## 为什么重要
它不是单篇论文自然延伸，而是多路线融合节点：几何恢复、相机控制视频、视频基础模型、实时自回归训练法在这里汇合。
