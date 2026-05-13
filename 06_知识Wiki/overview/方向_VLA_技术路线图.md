---
type: "overview"
id: "overview.方向_VLA_技术路线图"
pageType: "overview"
updated: "2026-05-08"
---

# 总览：VLA 技术路线图

## 一句话结论
VLA 正从“把一切压进单个端到端模型”转向“高层规划、中层校验、低层执行”分工更清晰的部署型系统；对真实机器人尤其是空中平台，层次化和验证壳层已经不是可选增强，而是在成为默认结构件。

## 技术格局
- **端到端 VLA**：OpenVLA、π₀、GR00T 等路线强调统一预训练，但高层语义延迟会直接拖累控制闭环。
- **实时化改造**：[[sources/A1_2604.05672|InternData-A1]]、SD-VLA、Realtime-VLA V2、TIC-VLA 开始把 token 预算、语义延迟与连续执行显式纳入设计。
- **层次化系统**：LaST0、ManualVLA、Long-Horizon Manipulation、SV-VLA 说明 planner, verifier, executor 的分工正在快速收敛。
- **低层动作器分化**：[[concepts/ACT动作分块]]、[[concepts/扩散策略]]、[[concepts/流匹配]] 各自代表速度、稳定性与多模态建模权衡。
- **部署安全壳层**：verifier、geometry critic、chunk/compute scheduler 正从“补丁”升级成低层动作器的标准外壳。 

## 关键 Gap
1. 纯端到端 VLA 仍缺真正的意图规划↔精细执行解耦。
2. stale semantic state 与 compute budget 往往没有被当成一等输入显式建模。
3. 长时序成功率越来越取决于 verifier / recovery loop，而不只是更强动作头。
4. 空中高速控制场景对延迟、安全和恢复速度更敏感，单一 VLM 动作头很难兼顾。

## 我们的切入点
- **三层语义解耦**：高层 VLM/LLM → 中层意图解析与校验 → 低层动作器 / PID-MPC。
- **latency-aware 中层**：显式传递 intent_age、verification result、compute/risk budget。
- **默认 verifier 壳层**：把语义 verifier 与 geometry-aware critic 当成部署标准件，而不是出问题后再补。
- **反思恢复闭环**：高层不只做 task decomposition，还要承担 memory / reflection / recovery trigger。
- **低层可替换**：按任务选 ACT / Diffusion / Flow Matching / predictive world-action model，但统一放进同一验收框架里比较。 

## 相关链接
- 详细报告：[[05_科研研究/D02_VLA/PAPER]]
- 架构对比：[[comparisons/端到端VLA_vs_层次化VLA]]
- 动作头对比：[[comparisons/ACT动作分块_vs_扩散策略_vs_流匹配]]
- 相关概念：[[concepts/VLA架构]] [[concepts/分层规划]] [[concepts/安全护栏]] [[concepts/实时推理]]
- 世界模型配合：[[overview/方向_世界模型_技术路线图]]
- 新近来源：[[sources/source.2604.21391_ResVLA|ResVLA (2604.21391)]] [[sources/source.2026-05-07_2603.03195_Chain_of_World|Chain of World (2603.03195)]] [[sources/AIR-VLA_2601.21602|AIR-VLA (2601.21602)]] [[sources/source.2026-04-01_GigaWorld-Policy|GigaWorld-Policy (2603.17240)]]
