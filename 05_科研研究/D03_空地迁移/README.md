# 方向三:借鉴地面机械臂方法,低成本迁移到空中操作

> 核心问题:地面机械臂的好方法,如何迁移到无人机/空中机械臂

## 研究目标

- 梳理地面机械臂操作的前沿方法(模仿学习/强化学习/VLA)
- 分析迁移到空中操作的关键挑战(振动、负载、视野、动态环境)
- 归纳低成本迁移路径

## 核心问题

- 地面方法(如 ACT/Diffusion Policy)在无人机上的适配成本?
- 空中操作 vs 地面操作的核心差异?
- 主人已有的无人机控制经验如何与操作结合?

## 已有知识库论文

- `2026-03-27_OnFly.md` - 无人机VLA导航
- `2026-03-28_UniDex.md` - 灵巧手迁移
- `2026-05-22_2605.21414_PointACT.md` - 3D点云驱动的VLA动作解码
- `2026-05-22_2605.20752_GaussianDream.md` - 训练期3DGS世界模型监督 manipulation policy

## 花火研究笔记

- 2026-04-12 R658: 本轮按轮换切到 **D03 + D01**。D03 轻量回扫 **AIR-VLA** 与 **DroneVLA** 一线，没有出现比既有 **AirVLA / UMI-on-Air / FlyAware** 更强的"低成本迁移骨架"，但一个判断更稳了：当前最值得写实的不是再扩方法名录，而是把 **ground-policy prior reuse / inference-time dynamics guidance / onboard contact-awareness / deployment cost** 固定成统一验收表，专门比较"视觉先验能否直接迁移"与"动力学补偿是否必须外置"。也就是说，D03 近期默认路线应继续坚持 **复用地面先验 + 推理时载体修正**，而不是把 aerial 任务重新当成从零训练问题。

- 2026-04-15 R715: 新增 **AirVLA** (2603.25038) 定量强证据：
  - **视觉先验**：π0 视觉表征可零样本迁移到飞行平台（确认）
  - **动力学 gap**：飞行动力学不可自动迁移（确认，定量）
  - **Payload-Aware Guidance**（推理时注入载荷/动力学约束，不重训 foundation model）：pick-and-place 23%→50%（+27pp）
  - **Gaussian Splatting 合成导航数据**：navigation 81%→100%（+19pp）
  - **综合长程任务**：62% 成功率
  - **关键结论**：推理时物理引导 + 合成数据增广 = 低成本迁移的最优路线，而非大规模重训。

---

## 🆕 2026-03-28 第1轮补充:空中机械臂论文扫描

> 青狐深挖轮次 | 20分钟快速扫描


| **Higher-Order Lie Dynamics for Aerial Manipulators** | 2605.06498 | 高阶Lie群递推动力学，支持空中机械臂实时轨迹优化与MPC | 🆕 候选-R20260510 |

### Paper 1: Aerial Manipulator RL - 空中机械臂端到端RL控制

- **arXiv**: 2512.21085
- **标题**: Global End-Effector Pose Control of an Underactuated Aerial Manipulator via Reinforcement Learning
- **方向**: 方向2 (空中机械臂操作)
- **核心发现**: 空中机械臂(quadrotor + 2-DoF轻量机械臂)面临重量和复杂度约束。用PPO在仿真中训练,产生前馈加速度和机体角速率命令+关节角度目标,由INDI姿态控制器和PID关节控制器跟踪。实现了厘米级位置精度和degree级姿态精度,能处理重负载和推动任务。
- **为什么有价值**: 空中精细操作的"轻量化+精确控制"挑战与主人的空中操作需求直接相关。展示了学习-based控制+经典控制器的组合是可行的工程路线。
- **可落地实验点**: Paper A的低层执行层可以参考"RL策略+经典控制器"的组合,RL负责产生高层运动指令,INDI/PID负责跟踪执行。「可落地实验点」
- **入库判断**: ✅ **入库**(新建 `2026-03-28_Aerial-Manipulator-RL.md`)

### Paper 2: GroundedPlanBench - 空间接地长程任务规划

- **arXiv**: 2603.13433
- **标题**: Spatially Grounded Long-Horizon Task Planning in the Wild
- **方向**: 方向2 (空中机械臂操作,跨域参考)
- **核心发现**: 当前VLM做任务规划时,缺少对"精确空间位置"(在哪里操作)的评估。提出GroundedPlanBench基准测试,评估VLM的分层子动作规划和空间接地能力。V2GP框架利用真实机器人视频演示自动生成空间接地规划数据。
- **为什么有价值**: 空中机械臂操作同样需要精确的空间接地(末端执行器位置+姿态),且当前瓶颈与地面操作类似--VLM规划缺乏几何精确性。
- **可落地实验点**: V2GP的自动数据生成框架可用于创建Paper A所需的「VLM意图+空间接地」训练数据。「可落地实验点」
- **入库判断**: ✅ **入库**(新建 `2026-03-28_GroundedPlanBench.md`)

### 关键发现总结

1. **空中机械臂的核心挑战**:轻量化 + 精确控制 + 抗干扰。RL+经典控制组合是可行路线。
2. **跨域迁移的关键发现**:VLM规划缺乏几何精确性是空中和地面操作的共同瓶颈。空间接地技术(GroundedPlanBench)可以迁移到空中场景。
3. **与Paper A的关联**:Paper A的三层架构(VLM意图→中层解析→低层执行)可以应用于空中机械臂,其中中层解析器需要输出几何精确的空间目标。

---

## 🆕 2026-04-01 第2轮补充:AirVLA 低成本迁移路线

### Paper 3: AirVLA - 把地面 manipulation VLA 迁到空中操作

- **arXiv**: 2603.25038
- **标题**: $\pi$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation
- **方向**: 方向3(借鉴地面机械臂方法,低成本迁移到空中操作)
- **核心发现**: 直接把固定基座机械臂 VLA(如 $\pi_0$)迁到飞行平台时,视觉表征能迁,但飞行动力学不会自动迁。论文提出 **Payload-Aware Guidance**,在推理阶段往 flow-matching 采样里注入载荷/动力学约束,不重训 foundation model;同时用 **Gaussian Splatting** 合成导航训练数据,460 次真实实验里把 pick-and-place 成功率从 **23% 提到 50%**,导航成功率从 **81% 提到 100%**。
- **为什么有价值**: 这条线非常贴合主人的主问题--不是从零做空中 VLA,而是把地面已有 manipulation prior 尽量"低成本改造"到空中平台。它证明了 **视觉先验可直接复用,动力学差异可通过 inference-time physics guidance 补偿**。
- **可落地实验点**: 主人后续可把地面机械臂 VLA / diffusion policy 当作上层操作先验,再单独设计一个空中平台的 **动力学约束引导层**(payload / thrust / attitude envelope / safety filter),优先走"推理时修正"而非"大规模重训"。同时可把 3DGS 场景重建接进导航数据合成链路。「可落地实验点」
- **入库判断**: ✅ **入库**(建议后续单独建 `2026-04-01_AirVLA.md`)

### Paper 4: AeroGrab - 空中抓取的一体化闭环管线

- **arXiv**: 2603.15097
- **标题**: AeroGrab: A Unified Framework for Aerial Grasping in Cluttered Environments
- **方向**: 方向3(借鉴地面抓取/主动感知方法迁到空中操作)
- **核心发现**: 不再只做"看到目标 → 直接抓"的 centroid 式空中抓取,而是把 **语言指定目标 + 主动探索补视角 + 多个 6-DoF grasp 候选 + collision-aware 可行性筛选 + 执行控制** 串成完整闭环。重点不在单个 grasp 网络,而在把地面机械臂里常见的主动感知与抓取评估流程整体搬到空中平台。
- **为什么有价值**: 它提醒主人一个很实用的低成本迁移方向--空中操作未必先追超强端到端 VLA,先把地面成熟的 **active perception + grasp ranking + feasibility filtering** 组合过去,往往更快形成可用系统。
- **可落地实验点**: 可先给无人机抓取实验加一个"补视角观察 + 候选抓取排序"中间层:利用主动绕目标飞行获得多视角,再用碰撞约束/姿态可达性对候选末端位姿打分,最后交给已有控制器执行。「可落地实验点」
- **入库判断**: ✅ **补记到本 README**(先作为系统级 pipeline 参考,不急着单独深挖)

### Paper 5: FlyAware - 抓取前惯量估计 + 抓取后自适应控制

- **arXiv**: 2601.22686
- **标题**: FlyAware: Inertia-Aware Aerial Manipulation via Vision-Based Estimation and Post-Grasp Adaptation
- **方向**: 方向3(借鉴地面感知/控制协同思路迁到空中操作)
- **核心发现**: 论文把空中抓取最麻烦的 **载荷惯量突变** 拆成两段处理:抓取前用 **RGB-D + 文本目标指定** 先估目标物体质量/惯量,抓取后再结合板载力传感做 **在线参数修正**,最后通过 **gain scheduling 的 inertia-aware adaptive control** 实时补偿负载变化。它不是单纯做识别或单纯做控制,而是把"视觉先验估计 → 抓取后快速自适应"串成闭环。
- **为什么有价值**: 这条线很适合主人后续空中机械臂路线,因为真实任务里最常见的问题不是不会抓,而是 **抓到之后动力学立刻变了**。FlyAware 说明可以先借鉴地面抓取里的目标感知/属性估计,再把结果喂给空中平台控制器,减少纯后验辨识带来的几十秒收敛延迟。
- **可落地实验点**: 主人可以先做一个轻量版两阶段管线:抓取前由视觉模块估计目标类别/大致质量区间/质心偏置,抓取后用 IMU/推力/末端力传感快速修正,再驱动一个 **payload-aware 控制增益调度层**。这能和 AirVLA 的 physics guidance 路线形成互补:AirVLA 负责高层操作先验,FlyAware 负责抓取后动力学稳态恢复。「可落地实验点」
- **入库判断**: ✅ **补记到本 README**(建议后续单独建 `2026-04-02_FlyAware.md`)

---

## 🆕 2026-04-05 第3轮补充:UMI-on-Air - 跨载体迁移的 embodiment-aware diffusion 新路线

### Paper 6: UMI-on-Air - 把 handheld gripper 操作策略迁移到空中机械臂

- **arXiv**: 2510.02614(v3 更新 2026-03-13)
- **标题**: UMI-on-Air: Embodiment-Aware Guidance for Embodiment-Agnostic Visuomotor Policies
- **方向**: 方向3(借鉴地面/手持式灵巧操作方法,低成本迁移到空中操作)
- **核心发现**: 核心问题是把 UMI(handheld gripper)收集的通用操作策略迁移到空中机械臂时的「控制与动力学失配」。提出 **EADP(Embodiment-Aware Diffusion Policy)**:在推理时把高层 UMI 策略与低层 embodiment-specific 控制器耦合,通过把控制器的跟踪代价梯度注入 diffusion 采样过程,引导轨迹生成朝向部署载体的动力学可行模式。这是「推理时 adaptation」而非「重训练」,实现即插即用。
- **为什么有价值**: 这条路与 AirVLA 的「physics guidance at inference time」思路高度一致,但更具体地处理了 **载体差异(handheld → aerial)**。对于主人最有参考价值的是:不需要为每个目标载体重训 policy,只需要设计一个「载体适配层」在推理时修正 diffusion 轨迹。这与 AirVLA 的 Payload-Aware Guidance 是同一范式的不同实现。
- **可落地实验点**: 主人可以把 UMI-on-Air 的 EADP 思路与 AirVLA 结合:用地面机械臂或手持 gripper 收集操作 demonstrations,训练一个 embodiment-agnostic diffusion policy,然后设计一个无人机专用的 embodiment-aware correction layer 在推理时注入,实现「一份策略 + 多载体即插即用」。「可落地实验点」
- **入库判断**: ✅ **补记到本 README**(建议后续单独建 `2026-04-05_UMI-on-Air.md`)

