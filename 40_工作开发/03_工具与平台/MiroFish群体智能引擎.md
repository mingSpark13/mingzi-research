---
title: MiroFish - 群体智能预测引擎
description: 基于多智能体的AI预测引擎，支持舆情推演、金融预测、故事推演
tags: [多智能体, LLM, 群体智能, 预测, GraphRAG, OASIS, 盛大集团]
repo: https://github.com/666ghj/MiroFish
stars: 39419
forks: 5319
license: AGPL-3.0
created: 2025-11-26
updated: 2026-03-22
institution: 盛大集团
domain: AI工具/多智能体仿真
local_path: /home/muyin/文档/MiroFish
reading_date: 2026-03-23
reading_status: 已入库
---

# MiroFish — 群体智能预测引擎

## 🎯 是什么

> **A Simple and Universal Swarm Intelligence Engine, Predicting Anything**
> 简洁通用的群体智能引擎，预测万物

MiroFish 是一款基于多智能体技术的新一代 AI 预测引擎。通过提取现实世界的种子信息（突发新闻、政策草案、金融信号、小说故事等），自动构建出**高保真的平行数字世界**。在此空间内，成千上万个具备独立人格、长期记忆与行为逻辑的智能体进行自由交互与社会演化。

通过"上帝视角"动态注入变量，精准推演未来走向——**让未来在数字沙盘中预演，助决策在百战模拟后胜出**。

驱动引擎基于 **OASIS**（CAMEL-AI 开源项目）。

---

## 📊 核心数据

| 指标 | 数值 |
|------|------|
| GitHub Stars | ⭐ 39,419 |
| Forks | 5,319 |
| License | AGPL-3.0 |
| 创建时间 | 2025-11-26 |
| 最近更新 | 2026-03-22 |
| 语言 | Python + Node.js |
| 赞助商 | 盛大集团 |

---

## 🔧 技术架构

### 后端结构 (`backend/app/`)

```
backend/app/
├── api/
│   ├── graph.py       # 图谱构建 API
│   ├── report.py      # 报告生成 API
│   └── simulation.py  # 仿真运行 API
├── services/
│   ├── graph_builder.py              # 图谱构建服务
│   ├── ontology_generator.py         # 本体生成（人设/实体关系）
│   ├── oasis_profile_generator.py   # OASIS 智能体配置生成
│   ├── simulation_config_generator.py # 仿真参数配置生成
│   ├── simulation_runner.py          # 仿真运行器
│   ├── simulation_manager.py        # 仿真管理器
│   ├── simulation_ipc.py            # 仿真进程间通信
│   ├── report_agent.py              # ReportAgent（报告生成）
│   ├── text_processor.py           # 文本处理
│   ├── zep_graph_memory_updater.py  # Zep 记忆层更新
│   ├── zep_entity_reader.py         # Zep 实体读取
│   └── zep_tools.py                # Zep 工具集
├── models/           # 数据模型
├── utils/           # 工具函数
├── config.py        # 配置
└── run.py           # 入口
```

### 前端结构 (`frontend/`)

- **框架**: Vue.js + Vite
- **端口**: `localhost:3000`
- **功能**: 交互界面、仿真控制、报告展示

### 后端 API

- **端口**: `localhost:5001`
- **框架**: Python
- **API 路由**: `/api/graph`, `/api/simulation`, `/api/report`

---

## 🌟 核心功能

### 1. 舆情推演
输入突发事件/新闻，模拟社会各群体的反应、观点演化、信息传播路径。输出舆情发展报告和可交互的数字分身。

### 2. 金融预测
模拟市场参与者（散户、机构、政策制定者等）的行为逻辑和博弈，预测金融信号走向。

### 3. 故事推演
输入小说前 N 回，让 Agent 模拟后续剧情发展。比如《红楼梦》前80回预测后40回结局。

### 4. 政策预演
模拟政策在不同人群（官员/企业/居民/媒体）中的反应、博弈和连锁效应。

### 5. 高保真数字世界
每个 Agent 具备：
- **独立人格**（价值观、性格、背景）
- **长期记忆**（Zep 记忆层）
- **行为逻辑**（OASIS 驱动）
- **社会关系**（GraphRAG 构建关系图谱）

---

## ⚙️ 核心技术栈

| 组件 | 技术 |
|------|------|
| **Agent 驱动** | OASIS (CAMEL-AI) |
| **记忆层** | Zep (长期记忆 + 检索) |
| **知识图谱** | GraphRAG (图检索增强生成) |
| **LLM 后端** | OpenAI SDK 兼容（推荐 qwen-plus） |
| **前端** | Vue.js + Vite |
| **后端** | Python + FastAPI (推测) |
| **部署** | Docker Compose |

---

## 🚀 快速开始

### 环境要求
- Node.js 18+
- Python 3.11-3.12
- uv (Python 包管理器)

### 源码部署

```bash
# 1. 克隆
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env:
# LLM_API_KEY=your_api_key
# LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
# LLM_MODEL_NAME=qwen-plus
# ZEP_API_KEY=your_zep_api_key

# 3. 安装依赖
npm run setup:all

# 4. 启动
npm run dev
# 前端: http://localhost:3000
# 后端: http://localhost:5001
```

### Docker 部署

```bash
docker compose up -d
```

### 在线 Demo
> https://666ghj.github.io/mirofish-demo/

---

## 💰 成本参考

- 推荐使用**阿里百炼 qwen-plus** 模型
- 官方提醒：消耗较大，建议先做 **<40轮** 小规模模拟

---

## 🔗 关联链接

- **官网**: https://mirofish.ai
- **GitHub**: https://github.com/666ghj/MiroFish
- **在线 Demo**: https://666ghj.github.io/mirofish-demo/
- **Bilibili 演示**: 武大舆情推演（BV1VYBsBHEMY）、红楼梦推演（BV1cPk3BBExq）
- **OASIS 引擎**: https://github.com/camel-ai/oasis

---

## 💡 潜在应用场景

### 🛸 机器人/具身智能
- **多机器人协同策略推演**：输入任务目标，让多个机器人 Agent 在仿真环境中自由交互、涌现协同行为
- **社会交互仿真**：训练机器人在复杂社会场景中的社交能力

### 🦊 花火相关
- **花火记忆系统增强**：Zep 记忆层架构值得借鉴，可用于花火的三层记忆系统升级
- **OASIS 驱动架构**：花火的行为逻辑可参考 OASIS 的 Agent profile 生成机制

### 🌐 世界模型
- **行为仿真层**：作为世界模型（World Model）的行为预测层
- **Sim2Real**：在 MiroFish 中仿真机器人群体行为，再迁移到真实硬件

---

## 📌 待探索

- [ ] 研究 OASIS Agent profile 生成机制与花火行为逻辑的结合
- [ ] 探索 MiroFish 用于多机器人协同策略仿真的可行性
- [ ] Zep 记忆层是否可以集成到花火的三层记忆系统中
- [ ] 本地部署测试（需配置 ZEP_API_KEY + LLM_API_KEY）

---
**维护**: 花火 · 2026-03-23
