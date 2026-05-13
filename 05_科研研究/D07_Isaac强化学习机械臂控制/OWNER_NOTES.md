# D07_Isaac强化学习机械臂控制 — 主人批注 (Owner Notes)

> 📌 **花火必读**：每次推进 D07_Isaac强化学习机械臂控制 研究前，先读此文件，按最新批注调整 PAPER.md 方向。
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

> 目前暂无批注，等待主人添加。

---

## 📊 花火执行记录

> 花火每次读取此文件后，在此记录已响应的批注（避免重复执行）。

| 日期 | 响应的批注 | 执行动作 |
|------|-----------|---------|
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（KG-M3PO / DiSCo / Reactive Dexterous Grasping / ARM）补写 PAPER.md 4.66，新增 disturbance-disambiguation overlay 规则，明确 semantic-state 与 sequence-copilot 只能在四行核心 bundle、reward-retention-projection 冲突裁决、sim2sim 一致性与 fixed-flight→coupled-base 晋级通过后，作为 support-side overlay 解锁 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（RL vs Optimal Control / Squint / Reactive Dexterous Grasping）补写 PAPER.md 4.65，新增 RL-versus-optimal-control routing 规则，要求后续 RL/最优控制对照继续服从同一套 W2/W3、sim2sim、一致性与 coupled-base promotion 闸门 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（DiSCo / KG-M3PO / ARM / Reactive Dexterous Grasping）补写 PAPER.md 4.64，新增 sim2sim-consistent deployment ladder，明确 semantic/shared-autonomy 只能在四行核心 bundle 通过 reward-retention-projection 冲突裁决、Sim2Sim 一致性与 fixed-flight→coupled-base 晋级后再介入 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（KG-M3PO / DiSCo / ARM / Reactive Dexterous Grasping）补写 PAPER.md 4.62-4.63，新增 semantic/shared-autonomy deferred-promotion 与 reward-retention-projection conflict-resolution 规则，继续锁死首轮标题路由边界 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（DiSCo / KG-M3PO / Reactive Dexterous Grasping / Squint）补写 PAPER.md 4.59-4.61，把四行最小实验包、S1→S3 串行协议、smoke-test 完整性门槛正式写进论文实验节，和 experiments.md 执行工作流对齐 |
| 2026-05-13 | 无新增批注 | 按默认轮换推进 D07，基于本地锚点（Q2RL / Reactive Dexterous Grasping / ARM / RL sim-real co-training）补写 PAPER.md 4.57-4.58，新增 retention-versus-projection route freeze 与 dominant-credit freeze，进一步锁死首轮真实 bundle 的标题路由边界 |
| 2026-05-12 | 无新增批注 | 按默认轮换推进 D07，补写 PAPER.md Section 4.8-4.12（semantic-state ablation 后续平台锁定解释规则 / platform-vs-controller 分离模板 / first real bundle 结论冻结） |
| 2026-05-09 | 无新增批注 | 按默认轮换推进 D07，补写 PAPER.md Section 4.8-4.11（semantic-state ablation / window-localized table / first-round go-no-go / reward-origin accountability） |


---

## 🧭 论文研究引导建议（新增通用机制，2026-05-13）

### A. 每轮必须产出 1 条「可验证主结论」
- 结论格式固定：`在[任务/窗口]下，[方法A] 相对 [方法B] 在 [指标] 上 [提升/无显著差异]`。
- 结论后必须加证据等级：`L0想法 / L1离线单次 / L2多seed复现 / L3真机复核`。
- 没有等级标签的结论，不允许进入 `REPORT.md` 的主结论区。

### B. 写作与实验配额绑定（防止“写作替代实验”）
- 每新增 1 段 route/freeze/gate 叙事，必须对应新增至少 1 个可执行实验项（命令、输入、输出指标、判停条件）。
- 若当轮没有新增实验执行证据，只允许更新 `rounds/`，不更新 `PAPER.md` 主方法与主结论。

### C. Source 页与 Wiki 的质量门（Claw 定时代理专用）
- 每篇新论文至少保留 3 个 source 证据点：`问题定义`、`核心方法`、`关键结果`。
- 禁止 wiki-to-wiki 循环引用：必须至少有 1 条原始 source（arXiv/官方项目页）支撑关键 claim。
- 若 source 缺失结果表/设置细节，标记为 `证据不完整`，不得提升为“方向锚点论文”。

### D. 阅读笔记目录格式统一（索引质量）
- 文件名统一：`YYYY-MM-DD_arXivID_英文短名.md`（无 arXiv 则用机构+标题短名）。
- 每篇笔记顶部固定 6 字段：`主题标签 / 任务类型 / 贡献类型 / 关键指标 / 可复现性 / 与本方向关系`。
- 每个方向 `README.md` 必须维护「Top 10 锚点论文」和「近 14 天新增」两个表，避免目录无序增长。

### E. 每周一次结构化清理
- 删除/归档超过 14 天且未进入任何实验设计的“弱相关笔记”。
- 对重复题材笔记做 `merge note`，保留一篇主笔记与交叉引用，降低索引噪声。
