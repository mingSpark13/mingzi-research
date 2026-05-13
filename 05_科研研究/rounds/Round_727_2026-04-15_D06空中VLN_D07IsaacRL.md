# R727 | 2026-04-15 18:05 | D06_空中VLN + D07_Isaac强化学习

## 执行方向
- D06 空中视觉语言导航
- D07 Isaac强化学习机械臂控制

---

## Phase 1: 文献扫描（≤10min）

### D06 空中VLN
**扫描结果：**
- AerialVLA (2603.14363) 已在论文地图 ✅（ICLR 2026，极简端到端 VLA，3-DoF+降落信号，模糊方向提示无需oracle，SOTA）
- 新扫结果 AIR-VLA (2601.21602) 已在地图 ✅
- 本轮 Tavily 高位结果回流到 AerialVLA / UAV-VLA 一线，未发现新主骨架
- **判断**：主线骨架仍稳定为 **APEX + AirNav**，近期不应继续扩图，应固化四层验收表

### D07 Isaac RL
**扫描结果：**
- WheelArm-Sim (2601.21129) 已在地图 ✅（Isaac Sim + Kinova Gen3 + 导航+操作联合数据平台）
- **新候选 Squint** (2602.21203)：Fast Visual RL for Sim-to-Real，5-DoF SO-101机械臂，ManiSkill3 8任务基准 → 适合作为 D07 低成本硬件平台对照
- **新候选 Grounding Sim-to-Real** (2603.22876)：域随机化+渲染保真度+RL微调，dexterous manipulation
- **判断**：D07 方向成熟度仍为 🔴 初期，新候选入库待确认，基础设施层（Isaac Lab / WheelArm-Sim）已较完整

---

## Phase 2: 深挖推进
- 深挖队列优先：**AerialVLA**（D06）/ **Real-to-Sim-to-Real**（D07）
- 本轮未执行精读，主要做新候选识别

---

## Phase 3: 产出推进
- D06 成熟度 🟡：主骨架稳定，验收表已收束，本轮无新推进
- D07 成熟度 🔴：新增 Squint / Grounding Sim-to-Real 候选，待确认入库

---

## 本轮汇报（≤5句）
R727·D06+D07。**D06** AerialVLA 本轮复核仍无新主骨架替代，APEX+AirNav 主线继续稳定，**建议近期把三路验收表固化写完**。**D07** 新增 Squint (Isaac-free 低成本平台) + Grounding Sim-to-Real (域随机化链路) 候选，待归档入库；Isaac Lab 基础设施层已基本确认，下一步推进 sim-to-real 协议写实。**龙**

---

## 下轮建议方向
- D06 继续稳定主骨架，推进验收表写实
- D07 归档 Squint + Grounding Sim-to-Real，启动 REPORT.md 框架起草
