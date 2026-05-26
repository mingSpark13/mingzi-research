# AirManip-Bench: A Navigate-then-Manipulate Benchmark for Contact-Rich Aerial Tasks in Urban Environments

> 方向：D06 空中视觉语言导航 | 论文类型：数据集 / Benchmark | 目标会议：CoRL 2027 / ICRA 2027 | 状态：🔴 草稿
> 依托平台：AirSpark（UE5.7 + AirSim + MuJoCo）
> 最后更新：2026-05-26

---

## Abstract

[TODO: 150-250词]

核心主张：现有空中 VLN/VLA benchmark 要么只覆盖导航阶段（OpenFly、AirNav），要么只覆盖实验室场景下的操作（AIR-VLA），缺少城市低空场景下从语言指令到接触操作的完整链路评测。AirManip-Bench 填补这一空白，提供 Search→Track→Approach→Align→Contact→Recovery 六阶段完整任务链路，覆盖多类接触操作、动力学感知评测与 Sim2Real 配对验证。

---

## 1. Introduction

### 1.1 Problem Statement

空中机器人正从"飞行"走向"操作"，但现有 benchmark 仍停留在导航阶段。OpenFly、AirNav 等工作提供了大规模空中 VLN 数据，却在目标到达后戛然而止；AIR-VLA 首次引入空中操作评测，但局限于实验室场景，缺少城市低空的动力学复杂性与多类接触操作。

真实城市低空任务的挑战不只是"飞到目标"，而是完整的：**找到目标 → 接近对齐 → 接触操作 → 扰动恢复**。这条链路中每个阶段的失败模式都不同，现有单阶段 benchmark 无法系统暴露。

### 1.2 Contributions

1. **C1: 城市低空 NtM 任务体系**：定义 Search→Track→Approach→Align→Contact→Recovery 六阶段任务链路，覆盖 6 类接触操作（抓取/放置、按钮/开关、推拨拉、插入/挂载、取样/巡检、交接/运输）。

2. **C2: 动力学感知评测协议**：不只评 success rate，还评飞行稳定性、接触力、负载变化、姿态扰动、能耗、控制平滑性、碰撞率、可见性保持、恢复能力，提供首个系统性动力学感知评测框架。

3. **C3: 自动化 Episode 生成与 Sim2Real 配对**：基于 AirSpark 平台的 BatchControllerSubsystem，支持程序化城市场景 + 3DGS-Mesh 真实重建配对，提供可规模化的 episode 自动生成与 Sim2Real gap 分析工具链。

4. **C4: 基线评测**：在 AirManip-Bench 上评测现有主流方法（OnFly、APEX、AerialVLA、AIR-VLA 风格），系统暴露各阶段失败模式，为后续方法研究提供可靠对照。

---

## 2. Related Work

### 2.1 空中 VLN Benchmark

| Benchmark | 场景 | 操作 | 动力学 | Sim2Real |
|-----------|------|------|--------|---------|
| OpenFly | 城市导航 | ❌ | ❌ | 部分 |
| AirNav | 真实城市 | ❌ | ❌ | ✅ |
| OpenUAV | 室外搜索 | ❌ | ❌ | ❌ |
| HUGE-Bench | 数字孪生 | ❌ | 碰撞 | ❌ |
| AIR-VLA | 实验室 | ✅ 部分 | 部分 | ❌ |
| **AirManip-Bench** | **城市低空** | **✅ 6类** | **✅ 完整** | **✅** |

### 2.2 空中操作系统

AIR-VLA [REF] 是首个空中操作 VLA benchmark，3000 条遥操作 demo，但局限于实验室场景。AirVLA [REF] 把 π0 迁移到空中 pick-and-place，提出 Payload-Aware Guidance，但无城市场景与多类接触。Flying Hand [REF] 提出末端中心空中操作框架，对本工作的操作接口设计有参考价值。

### 2.3 仿真平台

AirSpark（本工作依托平台）采用 UE5.7 + AirSim + MuJoCo 统一进程设计，避免 CARLA-Air [REF] 式跨进程 bridge 的时间戳漂移问题，为高带宽多模态数据采集提供基础。

---

## 3. AirManip-Bench

### 3.1 任务链路定义

```
语言指令
    ↓
Search / Locate     ← 开放词汇目标搜索，3D 语义前沿探索
    ↓
Track / Approach    ← 动态目标跟随，可见性保持，接近对齐
    ↓
Align / Stabilize   ← 末端对齐，姿态稳定，接触前准备
    ↓
Contact Operation   ← 6 类接触操作（抓取/按钮/推拨/插入/取样/交接）
    ↓
Recovery / Transport← 负载扰动恢复，任务完成或重导航
```

### 3.2 接触操作分类

[TODO: 6 类操作的具体定义与示例场景]

### 3.3 动力学感知评测指标

[TODO: 各阶段指标定义]

### 3.4 Episode 生成流程

基于 AirSpark BatchControllerSubsystem：
- SceneSpec 版本化城市场景资产
- 任务 profile 驱动 episode 自动生成
- JSONL writer + manifest 落盘
- 离线 validator + LeRobot v3 converter

### 3.5 Sim2Real 配对验证

[TODO: 3DGS-Mesh 真实重建配对方案]

---

## 4. Experiments

### 4.1 基线方法

[TODO: OnFly / APEX / AerialVLA / AIR-VLA 风格基线]

### 4.2 各阶段失败模式分析

[TODO: 系统暴露现有方法在哪个阶段失败]

---

## 5. Conclusion

[TODO]

---

## References

[TODO]
