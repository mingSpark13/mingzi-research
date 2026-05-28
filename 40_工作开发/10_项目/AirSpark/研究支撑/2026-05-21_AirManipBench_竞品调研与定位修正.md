结论先放前面：**你上个月这版没有过时，但“首个全链路 benchmark”的表述需要收窄**。最近 2026 年冒出来一批 UAV-VLN / UAV-VLA / aerial manipulation 工作，你现在更稳的定位应该改成：

> **面向城市低空场景的 Navigate-then-Manipulate benchmark：同时覆盖真实/仿真配对场景、多类接触操作、动力学感知评测、自动化数据采集与 Sim2Real gap 分析。**

这样比“首个导航→操作全链路”更不容易被 AIR-VLA、AirVLA、DroneVLA、HUGE-Bench 这些工作卡住。

---

## 1. 你的竞品表确实需要更新

### A. 导航 / VLN 方向已经很卷

OpenFly 已经是 ICLR 2026，明确集成 Unreal Engine、GTA V、Google Earth、3DGS 四类渲染/场景来源，并用自动化工具链生成 100K aerial VLN 轨迹。它的重点是**大规模空中 VLN 自动生成**，不是操作。([OpenReview](https://openreview.net/forum?id=OKm3w71ymP "OpenFly: A COMPREHENSIVE PLATFORM FOR AERIAL VISION-LANGUAGE NAVIGATION | OpenReview"))

OpenUAV / UAV-Need-Help 是 ICLR 2025，重点是现实化 UAV VLN、12K 左右轨迹、assistant-guided object search，已经把“导航+搜索+助手提示”做成 benchmark。它仍然是纯导航/目标搜索，没有接触操作。([prince687028.github.io](https://prince687028.github.io/OpenUAV/ "OpenUAV"))

AirNav 是 2026 新的强相关补充，它使用真实城市航拍数据，包含 **137K navigation samples**，并用 human–LLM collaborative pipeline 和 10 类 user personas 增强自然语言多样性；还提出 AirVLN-R1，用 SFT + RFT 做 UAV VLN。这个对你“城市低空语言导航数据”构成直接压力。([arXiv](https://arxiv.org/pdf/2601.03707 "AirNav: A Large-Scale UAV Vision-and-Language Navigation Dataset with Natural and Diverse Instructions"))

IndoorUAV 是 AAAI 2026，面向连续室内 UAV VLN，基于 Habitat 的 1000+ 室内场景和 16K+ instruction-trajectory pairs。它提醒你：**室内/半室内复杂结构导航**也可能成为低空 benchmark 的一条支线。([AAAI Publications](https://ojs.aaai.org/index.php/AAAI/article/view/39562?utm_source=chatgpt.com "IndoorUAV: Benchmarking Vision-Language UAV ..."))

AerialVLA 是 AAAI 2026，重点不是操作，而是 **online dialogue**：让 UAV 在导航过程中判断什么时候主动提问，并引入 UNOD benchmark 评测实时问答导航能力。这个可以作为你后续“agent 交互式任务采集”的补充参考。([AAAI Publications](https://ojs.aaai.org/index.php/AAAI/article/view/38878 "AerialVLA: A Vision-Language-Action Model for Aerial Navigation with Online Dialogue
| Proceedings of the AAAI Conference on Artificial Intelligence"))

**判断：** 纯 VLN、城市导航、搜索定位已经不适合作为你的主要创新点。你要把导航定位成“操作前置阶段”和“长链路上下文”，而不是单独和 OpenFly/OpenUAV/AirNav 拼规模。

---

### B. 目标跟踪 / 细粒度控制成为新热点

UAV-Flow 是 NeurIPS 2025 Datasets and Benchmarks 方向，提出 Flying-on-a-Word，把 UAV 任务从“飞到远处目标”转成“根据短语言指令执行细粒度飞行动作”。它包含真实世界语言-视觉-动作轨迹，30K+ real trajectories，并强调 ground-drone collaborative deployment。([arXiv](https://arxiv.org/html/2505.15725v2 "UAV-Flow Colosseo: A Real-World Benchmark for Flying-on-a-Word UAV Imitation Learning"))

CosFly-Track 是 2026 年 5 月刚出的，它非常值得你补进表里：面向城市 UAV visual tracking，包含约 12,000 expert/perturbed trajectories、2.4M timesteps、334 小时数据，通道包括 RGB、metric depth、semantic segmentation、6-DoF drone pose、target state/visibility flag、中英双语指令和 trajectory-pair metadata。它还提出 MuCO，多约束轨迹优化器，直接在连续 3D 空间里约束 visibility、viewpoint quality、collision、smoothness、kinematic feasibility。([arXiv](https://arxiv.org/abs/2605.17776 "[2605.17776] CosFly-Track: A Large-Scale Multi-Modal Dataset for UAV Visual Tracking via Multi-Constraint Trajectory Optimization"))

UAV-Track VLA 是 2026 年 4 月工作，构建了 890K+ frames、176 tasks、85 objects 的 tracking benchmark，并基于 π0.5 做 temporal compression + dual-branch decoder + flow matching action expert，面向语义化 UAV tracking。([arXiv](https://arxiv.org/abs/2604.02241 "[2604.02241] UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models"))

**判断：** 你之前的计划里“搜索与定位”有，但“动态目标跟随/可见性保持/视角质量优化”不够突出。对于城市低空操作，目标接近前的 **tracking-approach-align** 其实是导航和操作之间的关键桥梁，建议加入任务链路。

---

### C. 空中操作方向已经出现“早期竞品”，但都还没完全覆盖你的定位

AIR-VLA 是 2026 年空中操作 benchmark，宣称是第一个专门面向 Aerial Manipulation Systems 的 VLA benchmark，包含 3000 条人工遥操作 demonstrations，覆盖 base manipulation、object/spatial understanding、semantic reasoning、long-horizon planning，并强调 floating-base dynamics 和 UAV-manipulator coupling。([arXiv](https://arxiv.org/html/2601.21602v2 "AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation"))

AirVLA，注意不是 AIR-VLA，是 Stanford/PI 相关的 “π, But Make It Fly”，重点是把 π0 这类 manipulation-pretrained VLA 转到 aerial pick-and-place。它用 Gaussian Splatting 合成导航训练数据，并提出 Payload-Aware Guidance，在推理时把负载约束注入 flow-matching sampling；真实实验里导航 synthetic augmentation 和 payload-aware guidance 都明显提升成功率。([airvla.github.io](https://airvla.github.io/ "AirVLA"))

Flying Hand 是 RSS 2025，重点是 **end-effector-centric aerial manipulation**：全驱六旋翼 + 4-DoF arm + 末端中心 whole-body MPC + 高层 policy，支持 writing、peg-in-hole、pick-and-place、changing light bulbs 等真实操作任务。它对你非常有启发，因为它把“空中操作接口”从机体控制转成了“末端执行器控制”。([arXiv](https://arxiv.org/abs/2504.10334 "[2504.10334] Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning"))

AERMANI-VLM 是 2025 年工作，明确指出直接让 VLM 输出空中操作动作会不安全、幻觉、动力学不可行，所以采用“高层 VLM 推理 + 离散安全技能库 + 底层控制”的分层方式。这个和你现在“RPC 低频控制面、数据面模块化”的系统思想很一致。([arXiv](https://arxiv.org/abs/2511.01472 "[2511.01472] AERMANI-VLM: Structured Prompting and Reasoning for Aerial Manipulation with Vision Language Models"))

**判断：** 你的“6 类接触操作 + 城市场景 + 动力学感知 + Sim2Real 配对”仍然有空间，但不能再说 AIR-VLA 不存在或完全无威胁。你的差异化要从“有没有空中操作”改成“是否有城市低空、真实/仿真配对、多类接触、动力学闭环、可规模化自动采集”。

---

## 2. 新增/修正后的竞品矩阵建议

|类别|代表工作|它强在哪里|你的差异化应怎么写|
|---|---|---|---|
|大规模 UAV VLN|OpenFly|4 引擎、100K 轨迹、自动生成|你不是拼 VLN 规模，而是导航后接触操作与动力学评测|
|现实 UAV 搜索|OpenUAV / UAV-Need-Help|assistant-guided object search，约 12K 轨迹|你要补“搜索→接近→操作”的闭环|
|真实城市 VLN|AirNav|137K 真实城市样本，自然语言多样性，SFT+RFT|你需要强调不是只做离散导航，而是连续控制+操作|
|高层 UAV VLA|HUGE-Bench|3DGS-Mesh，4 个数字孪生场景，8 个高层任务，2.56M 米轨迹|它偏高层过程与安全评测，你偏接触操作和力/力矩|
|UAV 细粒度控制|UAV-Flow|真实世界 language-conditioned fine-grained control|你可以吸收其 atomic instruction/action chunk 设计|
|UAV 跟踪|CosFly-Track / UAV-Track VLA|动态目标跟随、可见性、视角质量、continuous action|你应加入 tracking-approach-align 阶段|
|空中操作 benchmark|AIR-VLA|3000 手动遥操作 demo，Isaac Sim，VLA/VLM 评测|你要强调城市低空、多类接触、Sim2Real 配对、大规模自动采集|
|VLA 转空中操作|AirVLA|π0 transfer、3DGS synthetic data、payload-aware guidance|你应补负载变化、接触扰动、推理期动力学约束|
|末端中心空中操作|Flying Hand|end-effector-centric interface，真实任务丰富|你可以把末端控制接口作为 baseline/系统设计参考|
|分层安全 VLM 操作|AERMANI-VLM|VLM reasoning + safe skill library|你应保留分层/模块化策略，而不是纯端到端一把梭|
|仿真基础设施|CARLA-Air / AirNavigation|单 UE 进程空地统一、UE 多 UAV、半自动场景生成|你的 RPC 控制面、共享内存/本地数据面设计要明确写出来|
|多模态感知数据|UEMM-Air / FlyAwareV2|UE 合成多模态、真实+合成城市理解|可作为你的感知预训练/域随机化补充数据|

---

## 3. 你现在最该补的不是“更多 VLN”，而是 4 个中间环节

你目前的链路写成“导航→操作”是对的，但中间最好细化成：

> **Task instruction → Search / Locate → Track / Approach → Align / Stabilize → Contact-rich Manipulation → Post-contact Recovery / Transport → Evaluation**

其中新增最关键的是：

**1）Track / Approach**  
不只是找到目标，还要在接近过程中保持目标可见、保持合适视角、避免遮挡、控制相对速度。CosFly-Track 和 UAV-Track VLA 都说明这个方向正在升温。([arXiv](https://arxiv.org/abs/2605.17776 "[2605.17776] CosFly-Track: A Large-Scale Multi-Modal Dataset for UAV Visual Tracking via Multi-Constraint Trajectory Optimization"))

**2）Align / Stabilize**  
操作前需要机体-机械臂-末端的对齐，尤其是夹取、按钮、插入、拨动、开合这类任务。这里可以引入末端中心控制、视觉伺服、MPC、action chunking。

**3）Contact / Load Transition**  
接触瞬间、抓取后负载变化、推拉导致的反作用力，是你比 VLN benchmark 更有价值的地方。AirVLA 的 payload-aware guidance 已经明确把“负载变化导致高度下沉”作为关键问题。([airvla.github.io](https://airvla.github.io/ "AirVLA"))

**4）Recovery**  
失败不是只有撞不撞、到没到终点，还包括：抓取失败后重试、接触扰动后恢复悬停、目标丢失后重新搜索、负载晃动后稳定运输。这个可以成为你的 benchmark 很有辨识度的部分。

---

## 4. 数据采集范式需要更新

你之前写“自动化操作数据采集流水线”是对的，但现在建议升级成 **四层数据飞轮**：

### 第一层：程序化场景 + 自动标签

对应 OpenFly / AirNavigation / UEMM-Air 这类方向。OpenFly 的自动工具链包括点云获取、语义分割、轨迹生成、指令生成；AirNavigation 也强调 UE 场景、半自动场景生成、多模态 synthetic training data。([OpenReview](https://openreview.net/forum?id=OKm3w71ymP "OpenFly: A COMPREHENSIVE PLATFORM FOR AERIAL VISION-LANGUAGE NAVIGATION | OpenReview"))

你这里要重点保留 UE5.7 PCG、资产库、语义标签、可达区域、碰撞体、任务点位、操作目标状态。

### 第二层：优化器生成 expert trajectory

不要只靠脚本随机飞。CosFly-Track 的 MuCO 很值得借鉴：把 collision、visibility、viewpoint quality、smoothness、kinematic feasibility 一起放进连续 3D 优化。([arXiv](https://arxiv.org/abs/2605.17776 "[2605.17776] CosFly-Track: A Large-Scale Multi-Modal Dataset for UAV Visual Tracking via Multi-Constraint Trajectory Optimization"))

你可以设计自己的操作版优化器：

> Navigation optimizer + approach optimizer + manipulation pre-contact pose optimizer + post-contact recovery optimizer

### 第三层：少量遥操作 seed demo → 批量变体生成

MimicGen / DexMimicGen 的思想可以迁移：少量高质量 demo，通过对象位置、目标姿态、场景布局、初始状态、扰动采样生成大量可用 episode。MimicGen 用少于 200 条人工 demo 生成 50K+ demonstrations；DexMimicGen 用 60 条 source demos 生成 20K+ 双臂/灵巧操作 demonstrations。([MimicGen](https://mimicgen.github.io/?utm_source=chatgpt.com "MimicGen"))

你可以写成：

> “We combine teleoperation seeds, procedural task randomization, and physics-valid trajectory adaptation to scale contact-rich aerial manipulation episodes.”

### 第四层：Real2Sim / 3DGS-Mesh 配对验证

HUGE-Bench、AirVLA、UAVTwin 都说明 3DGS/3DGS-Mesh 已经从“好看”变成 benchmark 与数据增强的一部分。HUGE-Bench 使用 3DGS-Mesh 表征兼顾 photorealistic rendering 和 collision-aware evaluation；UAVTwin 用 3DGS 重建背景，再加入可控动态人，实现 UAV 视角数据增强。([arXiv](https://arxiv.org/abs/2603.19822 "[2603.19822] HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks"))

你的优势可以是：

> UE 程序化场景负责规模化，3DGS/真实扫描场景负责真实纹理和 Sim2Real 配对，MuJoCo/物理后端负责接触动力学。

---

## 5. 数据格式建议也要补一句

别只写 HDF5。现在机器人数据生态在往 **LeRobot / RLDS / Open X-Embodiment 风格** 靠。LeRobotDataset v3 强调 tabular data、visual data、relational metadata 三部分，并支持直接从 Hugging Face Hub streaming；Open X-Embodiment 聚合了 1M+ real robot trajectories、22 种 robot embodiments，并统一成方便下游使用的数据格式。([Hugging Face](https://huggingface.co/blog/lerobot-datasets-v3?utm_source=chatgpt.com "`LeRobotDataset:v3.0`: Bringing large-scale datasets to ` ..."))

建议你的数据格式写成三层：

1. **Raw logs**：传感器原始流，RGB/depth/segmentation/pose/IMU/force/torque/contact/event。
    
2. **Episode format**：HDF5/Zarr 本地高吞吐训练格式。
    
3. **Release format**：LeRobot / RLDS-compatible metadata，方便别人直接训 ACT、Diffusion Policy、OpenVLA-OFT、π0/π0.5 类模型。
    

每个 episode 至少要有：

```text
observation:
  rgb_front / rgb_down / depth / segmentation
  drone_state: pose, velocity, angular velocity
  arm_state: q, dq, ee_pose
  force_torque / contact_state
  map_context / semantic_target

action:
  low_level_cmd
  waypoint / ee_delta_pose / gripper_cmd
  action_chunk

language:
  high_level_instruction
  subtask_instruction
  atomic_skill_label

metadata:
  scene_id
  task_id
  object_id
  weather/light/domain_randomization
  sim_or_real
  paired_real_episode_id
  success/failure_reason
```

---

## 6. 你的系统架构变更判断是正确的

你这句非常关键：

> 高带宽基础设施不应构建在 RPC 数据面上；RPC 保留为调试、远程控制和低频控制面。

这个判断对。尤其你现在要采 RGB、depth、segmentation、pose、force、contact、map、trajectory，如果还把高频图像/点云/力反馈压到 RPC，会很快变成瓶颈。

建议写成：

> 系统采用“控制面 / 数据面 / 仿真后端”解耦架构：RPC 仅承担调试、远程指令、低频任务控制；高带宽传感器流通过本地共享内存、文件队列、ROS2 topic、ZeroMQ/gRPC streaming 或直接进程内接口传输；MuJoCo 后端、数据采集、建图、规划、VLA 推理模块均可按需启停，避免平台被单一仿真或通信机制绑定。

CARLA-Air 也正好反向支持这个观点：它批评 bridge-based co-simulation 有同步开销和时空一致性问题，并把 CARLA 与 AirSim 放进同一个 UE 进程，共享 physics tick 和 rendering pipeline。([arXiv](https://arxiv.org/abs/2603.28032 "[2603.28032] CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence"))

---

## 7. 你的论文卖点建议改成新版

原来的四点可以升级为：

1. **Navigate-then-Manipulate Benchmark**  
    城市低空任务不止“飞到目标”，而是覆盖搜索、跟踪、接近、对齐、接触操作、负载后恢复的完整链路。
    
2. **Contact-Rich Aerial Operation Taxonomy**  
    提供 6 类以上空中接触操作：抓取/放置、按钮/开关、推/拨/拉、插入/挂载、取样/贴近巡检、交接/运输等。
    
3. **Dynamics-Aware Evaluation**  
    不只评 success rate，还评飞行稳定性、接触力、负载变化、姿态扰动、能耗、控制平滑性、碰撞、可见性、恢复能力。
    
4. **Hybrid Synthetic–Real Data Flywheel**  
    UE 程序化场景 + 真实重建/3DGS-Mesh + 少量遥操作 seed + 自动轨迹优化 + Sim2Real paired validation。
    
5. **Modular Infrastructure for Scalable Collection**  
    RPC 控制面、独立高带宽数据面、MuJoCo/UE/建图/规划/VLA 模块按需启停，支持 benchmark、baseline、主动采样和后续 world model 训练。
    

---

## 8. 最后给你一句更稳的项目定位

建议把 1.1 改成：

> **AirManip-Bench 是一个面向城市低空场景的多模态 Navigate-then-Manipulate benchmark，覆盖语言导航、目标搜索/跟踪、接近对齐、多类接触操作和负载扰动恢复，并提供动力学感知评测、自动化 episode 生成与 Sim2Real 配对验证。**

比“首个同时覆盖导航→操作全链路”稳很多，也更像顶会论文摘要里的贡献句。