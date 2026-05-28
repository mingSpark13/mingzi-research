---

title: "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation"
authors: Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang, Xintao Chao, Shiyuan Dong, Fang Chen
arxiv: 2605.06481
date: 2026-05-07
institution: 未知
conf: arXiv
keywords: [World Action Model, robot manipulation, slot state, object addressability, flow matching]
tags: [VLA架构, 流匹配, 多模态统一架构, 具身智能]
domain: 具身智能
pdf_path: "../../01_论文库/具身智能/2605.06481_OA-WAM.pdf"
reading_date: 2026-05-11
reading_status: 已读
related_concepts: ["VLA架构", "流匹配", "多模态统一架构", "具身智能"]
---

# 📖 花火格式笔记

## 🎯 题目

OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation

## 📝 三句摘要

1. **问题背景**：现有 World Action Model 往往用整体图像或全局 latent 表征未来世界，遇到指令绑定具体目标物体、且场景发生扰动时，动作解码器很难稳定地“找对对象”。
2. **核心方法**：论文提出 OA-WAM，把场景拆成机器人槽位和多个物体槽位，每个槽位分成持久 address 向量与时变 content 向量，并在 block-causal Transformer 中联合文本、图像、本体感觉与历史动作做下一帧世界预测和 16-step flow-matching 动作解码。
3. **关键结果**：OA-WAM 在 LIBERO 达到 97.8%、在 SimplerEnv 达到 79.3%，同时在 causal slot intervention 中 swap-binding cosine 达到 0.87，显著优于整体式 baseline，说明“对象可寻址”确实提升了场景扰动下的稳健操作。

## 💎 价值评估

- **🔬 研究价值**：它把 WAM 里的“世界预测”从整体视觉生成推进到对象级可绑定接口，这对主人正在关心的 controllable handoff / honest packet 类问题很有启发。
- **🚀 实践价值**：若后续要做多物体操作、场景变化下的稳健抓取或语言条件 pick-place，slot address 机制比纯全局 latent 更容易排查错误归因。
- **📈 扩展潜力**：可以继续往跨视角、多机器人共享 object slots、或空地协同操作中的“对象级世界状态接口”扩展。

## 🎯 可落地实验点

**实验设计**：把 OA-WAM 的 object-addressable slot 接口迁移到主人现有具身操作/空中操作 world model 设定里，验证“地址-内容分离”是否能提升扰动场景下的任务成功率。
- 对比基线：holistic latent WAM、video-token WAM、无 address reset 的 slot 版本
- 度量指标：任务成功率、目标绑定准确率、scene perturbation 后的恢复率、intervention consistency score
- 预期结果：对象级 address 设计会在多物体干扰和目标切换任务中显著降低绑错对象的问题

## 🔗 知识图谱

- [[VLA架构]] - 统一动作与世界预测的主体框架
- [[流匹配]] - 动作头采用 flow-matching 解码连续动作 chunk
- [[多模态统一架构]] - 融合文本、图像、本体感觉与动作历史
- [[具身智能]] - 面向真实机器人操作稳健性的核心问题

## 🔗 相关链接

- [[2026-05-11_BioProVLA_A_Biologically_Plausible_Vision-Language-Action_Model_for_Robotic_Manipulation]] - 同样关注操作任务中的视觉-语言-动作统一建模
- [[2026-05-11_Failure_Demonstration_Data_Improves_Robot_Learning]] - 都在研究如何提高扰动和失败场景下的机器人稳健性
- [[2026-05-11_RoboInter_A_Holistic_Intermediate_Representation_Suite_Towards_Robotic_Manipulation]] - 对比“整体中间表征”与“对象可寻址表征”两条路线

## 📌 待探索问题

- 这种 address/content 分离如果迁移到空中操作场景，地址是否还能在强视角变化和遮挡下稳定维持？
- object slots 数量与实际场景物体数量不匹配时，会不会出现 address collision 或无效槽位干扰？

---
**维护**: 花火 · 2026-05-11
