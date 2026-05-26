# OpenVLA 本地实战路线图

> 花火调研 · 2026-03-27
> 目标：帮主人把「会训 policy」升级成「能把 VLA 落到机器人系统里」

---

## 一、项目定位

```
上一代：LeRobot + ACT/DP + 单臂抓取放置
        → "我会训一个 policy"

下一代：OpenVLA + 语言条件 + 机器人平台接入
        → "我会把 VLA 落到机器人系统里"
```

**项目名称建议**：
> "基于 OpenVLA 的语言条件机器人操作部署与轻量微调"

---

## 二、OpenVLA 硬核信息

### 2.1 模型架构

| 项目 | 内容 |
|------|------|
| 参数量 | 7B (7.5B) |
| Vision Backbone | Prismatic: DINOv2 + SigLIP (fused) |
| LLM Base | Llama-2 7B |
| 动作处理 | 256-bin action discretization (每维动作离散化) |
| 预训练数据 | Open X-Embodiment，970K 轨迹 |
| 动作空间 | 7-DoF (可扩展) |
| 推理框架 | Hugging Face `transformers` AutoClasses |

### 2.2 硬件需求

| 场景 | 最低显存 | 推荐配置 |
|------|---------|---------|
| **Zero-shot 推理** | ~14GB | A100 40GB+ |
| **LoRA 微调** | ~27GB (batch=1) | A100 80GB |
| **LoRA 微调 (batch=16)** | ~72GB | 8x A100 或单卡 A100 80GB |
| **全量微调** | 8x A100 | 8x A100 80GB |

> ⚠️ **主人当前硬件**：GTX 1060 6GB
> **结论**：完全无法本地运行 OpenVLA 7B，必须上云。

### 2.3 软件依赖

```python
# 核心依赖 (README 明确要求)
torch==2.2.0
transformers==4.40.1
tokenizers==0.19.1
timm==0.9.10
flash-attn==2.5.5
```

> 注意：README 明确写 `transformers>=4.40` 会因版本更新导致问题，强烈建议用指定版本。

---

## 三、主人现状分析

### 3.1 已有环境

| 环境 | 工具 | 版本 |
|------|------|------|
| aloha conda env | torch | 2.4.1 ✅ |
| aloha conda env | timm | 0.9.7 ✅ |
| aloha conda env | torchvision | 0.19.1 ✅ |
| — | transformers | ❌ 需安装 |
| — | tokenizers | ❌ 需安装 |
| — | flash-attn | ❌ 需安装 |

### 3.2 关键差距

1. **GPU 显存严重不足**：1060 6GB vs 最低需求 14GB（推理）
2. **缺少核心依赖**：transformers、tokenizers 等未安装
3. **没有机器人平台接入代码**：需要写 bridge/ widowX 或自己的机械臂接口

---

## 四、执行路线（两条路径）

### 路径 A ✅ 推荐：云端 GPU + 本地开发调试

**思路**：代码开发在本地，训练/推理上云端 GPU

#### Step 1：本地准备（1-2天）

```bash
# 1. 创建 conda 环境
conda create -n openvla python=3.10 -y
conda activate openvla

# 2. 安装核心依赖（注意版本！）
pip install torch==2.2.0 torchvision==0.17.0 --index-url https://download.pytorch.org/whl/cu121
pip install transformers==4.40.1 tokenizers==0.19.1 timm==0.9.10

# 3. 安装 flash-attn（编译需 Ninja）
pip install packaging ninja
pip install flash-attn==2.5.5 --no-build-isolation

# 4. 克隆仓库
cd ~/openvla   # 或你偏好的目录
git clone https://github.com/openvla/openvla.git
cd openvla && pip install -e .
```

#### Step 2：云端 GPU 准备

推荐平台（按推荐顺序）：

| 平台 | 优点 | 缺点 |
|------|------|------|
| **AutoDL** | 性价比高，A100 80GB 按量计费 | 需要配置网络 |
| **算了_gpu云** | 国内访问快 | 价格稍贵 |
| **Google Colab** | 免费 A100 | 额度有限，会断连 |
| **Lambda Labs** | 支持 A100 80GB | 国际线路 |

**推荐配置**：
- 机型：A100 80GB
- 系统：Ubuntu 22.04
- 镜像：PyTorch 2.2 + CUDA 12.1

#### Step 3：下载模型和数据集（云端做）

```bash
# 从 HuggingFace 下载预训练模型（约 15GB）
from transformers import AutoModelForVision2Seq, AutoProcessor
model = AutoModelForVision2Seq.from_pretrained("openvla/openvla-7b")
processor = AutoProcessor.from_pretrained("openvla/openvla-7b")

# 下载 BridgeData V2 数据集（约 124GB）
cd <DATA_ROOT>
wget -r -nH --cut-dirs=4 --reject="index.html*" \
  https://rail.eecs.berkeley.edu/datasets/bridge_release/data/tfds/bridge_dataset/
mv bridge_dataset bridge_orig
```

#### Step 4：跑通 Zero-shot 推理

在云端先跑通官方 demo，验证环境：

```python
# test_inference.py
from transformers import AutoModelForVision2Seq, AutoProcessor
from PIL import Image
import torch

processor = AutoProcessor.from_pretrained("openvla/openvla-7b", trust_remote_code=True)
vla = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b",
    attn_implementation="flash_attention_2",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True
).to("cuda:0")

# 模拟相机输入
image = Image.open("test_image.jpg")
prompt = "In: What action should the robot take to pick up the red cup?\nOut:"
inputs = processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)
action = vla.predict_action(**inputs, unnorm_key="bridge_orig", do_sample=False)
print("Action:", action)
```

#### Step 5：LoRA 微调实验

```bash
# 在云端 A100 上运行
torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path "openvla/openvla-7b" \
  --data_root_dir <PATH TO DATA> \
  --dataset_name bridge_orig \
  --run_root_dir <PATH TO LOGS> \
  --adapter_tmp_dir <PATH TO ADAPTER> \
  --lora_rank 32 \
  --batch_size 16 \
  --grad_accumulation_steps 1 \
  --learning_rate 5e-4 \
  --image_aug True \
  --wandb_project openvla-finetune \
  --save_steps 500
```

**显存不够时**（< 80GB）：减小 batch_size，增加 grad_accumulation_steps

```bash
# 27GB 显存可行配置（实测）
--batch_size 1 \
--grad_accumulation_steps 16 \
```

#### Step 6：对接主人自己的机器人平台

把 OpenVLA 的 action 输出接到主人自己的机械臂控制：

```python
# robot_deploy.py
import numpy as np

class OpenVLADeployer:
    def __init__(self, checkpoint_path, robot_config):
        self.processor = AutoProcessor.from_pretrained(checkpoint_path, trust_remote_code=True)
        self.vla = AutoModelForVision2Seq.from_pretrained(
            checkpoint_path,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True
        ).to("cuda:0")
        self.robot_config = robot_config

    def predict_and_execute(self, image, language_instruction):
        prompt = f"In: What action should the robot take to {language_instruction}?\nOut:"
        inputs = self.processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)
        action = self.vla.predict_action(**inputs, unnorm_key=self.robot_config["unnorm_key"])
        
        # 动作去归一化后发送给机械臂
        normalized_action = action[0]  # shape: (7,)
        real_action = self.denormalize_action(normalized_action)
        self.robot.execute(real_action)
        return real_action

    def denormalize_action(self, normalized_action):
        # 根据具体机器人的 action normalization 方案
        bounds = self.robot_config["action_bounds"]
        return normalized_action * (bounds["max"] - bounds["min"]) / 2 + (bounds["max"] + bounds["min"]) / 2
```

---

### 路径 B：本地先跑 LeRobot + 现有 ACT/DP，对比 VLA 概念理解

**思路**：在 1060 上继续做 ACT/DP 项目，但加上 VLA 的认知和系统设计

这个路径更适合"先把项目讲出去"，之后再补 VLA 实操。

#### 本地可完成的事：

1. **系统架构设计**：画完整的 VLA 部署流程图
2. **数据格式转换**：把主人的数据转成 RLDS 格式（适配 OpenVLA）
3. **对比实验设计**：规划 OpenVLA vs ACT/DP 的评测方案
4. **代码框架准备**：写好 robot_deploy.py 的骨架，等云端 GPU

---

## 五、项目里程碑

| 阶段 | 内容 | 产出 |
|------|------|------|
| **Week 1** | 本地环境搭建 + 云端 GPU 准备 + 模型下载 | 能跑通官方 demo |
| **Week 2** | Zero-shot 推理 + 评测 benchmark | 跑通 LIBERO 或 BridgeData 评测 |
| **Week 3** | LoRA 微调自己的任务（pick-place/ drawer） | 微调后模型 checkpoint |
| **Week 4** | 对接自己机械臂/仿真器 + 端到端测试 | 可演示的完整 pipeline |
| **Week 5-6** | ACT/DP 对比实验 + 项目文档 + GitHub 整理 | 简历项目完成 |

---

## 六、简历项目包装

### 项目标题
> "基于 OpenVLA 的语言条件机器人操作：预训练 VLA 的部署、微调与实机验证"

### 项目描述模板
```
本项目聚焦将开源 7B VLA（OpenVLA）落地到真实机器人操作平台。

主要工作：
1. 在云端 GPU 环境下完成 OpenVLA 预训练模型的推理部署，验证 zero-shot 指令执行能力
2. 使用 LoRA 高效微调技术，将模型适配到具体的 pick-place / drawer 操作任务
3. 设计并实现 OpenVLA 与自研机械臂控制系统的接口对接，完成端到端闭环验证
4. 与经典 imitation learning 方法（ACT/Diffusion Policy）进行系统级对比分析

技术栈：OpenVLA / PyTorch FSDP / LoRA / Hugging Face Transformers / LIBERO / BridgeData V2 / RLDS

亮点：从「会训 policy」升级为「能把 foundation model 接入机器人系统」，理解 VLA 预训练-
微调范式，掌握从云端训练到边缘部署的完整流程。
```

### GitHub 仓库结构建议

```
openvla-robot-project/
├── README.md
├── requirements.txt
├── scripts/
│   ├── inference_demo.py        # 推理 demo
│   ├── finetune_lora.sh        # LoRA 微调脚本
│   ├── evaluate_benchmark.py    # 评测脚本
│   └── robot_deploy.py         # 机器人部署接口
├── configs/
│   └── robot_config.yaml        # 机器人参数配置
├── data/
│   └── README.md                # 数据集说明
├── evaluation/
│   ├── results/                 # 评测结果
│   └── logs/                    # WandB logs
└── comparisons/
    └── act_dp_comparison/       # 与 ACT/DP 对比实验
```

---

## 七、备选参考：OFT（最新微调方法）

> README 最新更新 [2025-03-03] 提到 OFT（Optimized Fine-Tuning recipe for VLAs）

OFT 对比 vanilla LoRA 的优势：
- 推理速度提升 25-50x
- 任务成功率更高
- 支持多输入图像
- 支持高频双臂机器人控制
- 使用连续动作（vs 离散动作）

**项目网站**：https://openvla-oft.github.io/

> 💡 这个方法值得在 Week 4+ 关注，如果主人在微调阶段遇到瓶颈，可以切换到 OFT。

---

## 八、主人硬件补充建议

| 方案 | 成本 | 适用场景 |
|------|------|---------|
| **AutoDL A100 80GB** | ~15元/小时 | LoRA 微调 + 实机部署调试 |
| **Lambda Labs A100** | ~0.80$/h | 临时跑实验 |
| **升级本地显卡到 RTX 4090 24GB** | ~1.2万 | 本地可跑推理+小规模 LoRA |
| **MacBook M3 Pro** | — | 只能跑小模型，不推荐 |

**花火建议**：先白嫖 Colab A100 熟悉流程，再上 AutoDL 按量付费。

---

**维护**: 花火 · 2026-03-27