# D04_跨载体泛化 — 主人批注 (Owner Notes)

> 📌 **花火必读**：每次推进 D04_跨载体泛化 研究前，先读此文件，按最新批注调整 PAPER.md 方向。
> 主人可随时在此添加批注，花火下次 Heartbeat 时自动生效。

---

## 📋 批注格式说明

每条批注请按以下格式添加（花火会按时间倒序读取，最新的优先级最高）：

```
### [YYYY-MM-DD] 批注标题
**类型**: 方向调整 / 创新点 / 实验要求 / 写作风格 / 其他
**优先级**: 🔴 立即执行 / 🟡 下轮执行 / 🟢 长期参考

内容...
```

---

## 📝 主人批注区

### [2026-05-27] 推进 Method 3.x 具体技术描述
**类型**: 写作风格
**优先级**: 🟡 下轮执行

D04 的 Related Work 结构健康（真实的方法分类，不是路由规则堆积），核心贡献（geometry-first 跨载体迁移协议）独立有价值。主要问题是 Method 的具体技术描述还不够完整。

**执行要求**：
1. **禁止**在 Related Work 下继续新增子章节，现有 2.1-2.11 已足够
2. 本轮及后续轮次的 80% 精力集中在 **Method 3.x**：
   - **3.1 Geometry-First Transfer Protocol**：具体写出 shared geometry packet 的数据结构定义，以及 geometry verification 的判断条件（公式层面）
   - **3.2 Geometry-Conditioned Latent Action Retargeting**：具体写出 latent action 重定向的网络架构和训练目标
   - **3.3 In-Context Embodiment Residual Modeling**：具体写出在线载体上下文推断的机制
   - **3.4 Escalation Rule**：将现有文字描述的升级规则转化为可执行的算法步骤
3. 当 Method 各子章节完成后，再写 Abstract
4. 每轮推进后同步更新头部 `最后更新` 字段

---

## 📊 花火执行记录

> 花火每次读取此文件后，在此记录已响应的批注（避免重复执行）。

| 日期 | 响应的批注 | 执行动作 |
|------|-----------|---------|
| 2026-06-01 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：在 3.8 specialist promotion blocker 之后新增 shared-latent promotion blocker `Ω_t=(KAG,DAG,RIG,LTS,HRS,CW,PC,PB_lat)`，用 Any2Any / RIO / 轻量 PEFT 适配三类证据把“kinematic alignment + tiny adaptation”与真正的 shared latent sufficiency 分开；同步更新 PAPER 头部时间戳 |
| 2026-06-01 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：在 3.7 后新增 family-matched specialist promotion blocker，形式化 `Ξ_t=(RIG,BPA,BSC,LTS,SRS,CW,PC,PB)` 与 `SRS > max(BPA,BSC)+τ_spec` 的晋升条件，把 D-CLING / Human-Robot Copilot / specialist distillation 三类本地锚点压成可执行的 weakest-honest subtraction 规则；同步更新 PAPER 头部时间戳 |

| 2026-05-28 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 本轮继续主推进 D04 Method 3.x：细化 3.3 latent retargeting 的 token 化架构与训练目标，补写 3.5 in-context residual 的双分支机制与路由损失，重写 3.7 escalation 为可执行 shortest-honest algorithm，并同步更新时间戳；本轮本地扫描命中 RIO / Human-Robot Copilot / D-CLING / Any2Any / OPFA，无新增正式入库 |
| 2026-05-28 | [2026-05-27] 推进 Method 3.x 具体技术描述 | 主推进 D04 Method 3.x：重写 3.1 几何包与验证判据、3.3 latent retargeting 架构与目标、3.5 context residual 机制、3.7 escalation algorithm；同步更新 PAPER 头部日期 |
