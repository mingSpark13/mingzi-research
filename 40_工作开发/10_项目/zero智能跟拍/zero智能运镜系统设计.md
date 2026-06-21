---
tags: [zero, 智能跟拍, 运镜系统, 设计]
created: 2026-06-09
---

# Zero 智能运镜系统设计

> 核心结论：不训练自由轨迹生成模型，而是做**模式库 + 参数化 + 打分选择**。
> 规则提供物理底线，模式提供镜头语言，参数提供变化空间，打分模型提供智能审美，切换机制保证稳定执行。

---

## 一、总体路线

**不生成自由轨迹，而是生成"模式 + 参数 + 切换策略"。**

```
输入（画面 / 目标状态 / 场景信息）
        ↓
生成候选运镜模式
        ↓
为每个模式采样有限参数
        ↓
硬约束 Gate → 规则 Scorer → VLM Scorer → Reward Model
        ↓
选择最高分模式和参数
        ↓
平滑切换 phi_ref / d / h / FOV
        ↓
底层控制执行
```

系统最终输出：

```
mode: orbit / oblique / parallax / reveal / push-in / pull-out ...
params: { phi_ref, distance, height, orbit_speed,
          target_screen_pos, duration, fov, easing_curve }
```

| 阶段         | 输出对象                        | 是否需要大模型        |
| ---------- | --------------------------- | -------------- |
| 当前最小 Demo  | φ_ref                       | 不需要            |
| 实用产品版      | mode + (φ, d, h, v, ω, FOV) | 小模型即可          |
| 高级智能版      | mode + 参数 + 风格 + 后期建议       | 小模型 + VLM/CLIP |
| **不建议初期做** | 任意未来轨迹 / 未来视频               | 参数量和数据需求太大     |

---

## 二、运镜模式库

### 2.1 基础保守模式

| 模式          | 目标            | 适合场景              | 核心参数                            |
| ----------- | ------------- | ----------------- | ------------------------------- |
| **lock**    | 稳定锁定，不追求视觉效果  | 目标剧烈运动、感知不稳、系统刚启动 | phi_ref=当前, screen_pos=center   |
| **oblique** | 斜后方跟拍，兼顾稳定与效果 | 人/船/车移动目标，方向稳定    | phi_ref=120°~150°, leading room |
| **orbit**   | 主动环绕，增强动感     | 目标稳定，空间充足         | ω=5°~25°/s, duration=3~8s       |

### 2.2 热门效果模式

| 模式 | 效果 | 适合场景 | 评分重点 |
|---|---|---|---|
| **parallax slide** | 目标稳定，背景横向运动，高级感 | 主背景有深度差，空间允许横移 | 主体稳定 + 背景视差 + 无遮挡 |
| **reveal** | 目标从遮挡中逐渐露出 | 有前景物（树/柱/门框） | r_vis(0)低 → r_vis(T)高，过渡平滑 |
| **push-in** | 缓慢推近，增强压迫感/情绪感 | 人像、商品、车辆、舞台 | 画面中目标占比变化，稳定性 |
| **pull-out** | 从主体到环境，展示空间感 | 海边、山顶、城市、旅行大片 | 目标最小占比阈值，高度变化 |
| **rise reveal** | 上升揭示大背景 | 海上、城市、山谷、建筑 | 俯仰角曲线，背景占比增长 |
| **leading follow** | 运动方向前方留白 | 船、跑步、骑行、车辆、海上运动 | screen_pos = center - α × motion_dir |

---

## 三、打分器（四层）

最终分数：

```
S_total = S_gate × (w_r·S_rule + w_v·S_vision + w_l·S_learned + w_s·S_style)
```

### 3.1 第一层：硬约束 Gate（直接规则判断）

以下任意触发 → 直接退回 lock：

```
目标出框 / 严重遮挡 / bbox 太小 / 检测不稳定
轨迹碰撞 / 控制加速度超限 / 云台角速度超限 / 模式切换过频
```

### 3.2 第二层：规则指标 Scorer

- **构图分**：目标位置、前方留白、是否贴边/裁切
- **稳定分**：目标抖动、无人机加速度、云台角速度、参数跳变
- **动感分**：`s_motion = |r × v_rel| / |r|²`（相对横向运动越明显越高）
- **环境展示分**：侧向视角、背景深度、前景遮挡、环境占比

### 3.3 第三层：视觉语义 Scorer（VLM/CLIP）

不让 VLM 判断精确几何（直接算），让它判断语义与氛围：

```
背景是否漂亮 / 是否有夕阳侧逆光 / 是否有前景可做 reveal
是否适合旅行大片 / 人物姿态是否自然 / 画面是否杂乱
```

VLM 只输出结构化 JSON，不直接控制轨迹：

```json
{
  "scene_type": "seaside",
  "background_quality": 0.82,
  "foreground_available": true,
  "lighting": "side_backlight",
  "recommended_effects": ["parallax_slide", "pull_out", "orbit"],
  "avoid_effects": ["top_down"]
}
```

### 3.4 第四层：学习型 Reward Model

- **输入**：当前关键帧 + 候选模式/参数 + 规则指标 + VLM 标签 + 短 horizon 预览帧
- **输出**：composition_score / motion_score / style_score / overall_score
- **训练方式**：A/B 偏好排序（不做绝对打分，一致性更高）

---

## 四、在线决策流程（7步）

```
Step 1  感知状态
        bbox / mask / keypoints / 目标速度 / 相对方位角φ / 距离d / 高度h
        → 摄影语义：s_view, s_scale, s_motion, s_stability, s_reveal

Step 2  生成候选模式
        根据状态过滤：
        目标高速转弯 → 只允许 lock/oblique
        稳定且空间大 → 允许 orbit/parallax
        有漂亮环境   → 允许 pull-out/rise
        有前景物     → 允许 reveal

Step 3  参数采样
        每个模式采样有限参数组合（几十~几百个候选）

Step 4  短时预览评估
        1~3s horizon 预测：目标是否出框、控制加速度、遮挡风险、背景视差

Step 5  综合打分
        S = hard_gate × (规则分 + 运动分 + 稳定分 + VLM分 + Reward分 - 切换惩罚)

Step 6  模式切换
        最小驻留时间 + 切换收益阈值Δ + 滞回机制 + 风险回退

Step 7  平滑输出
        phi_ref ← rate_limit(phi_cmd)
        d_ref / h_ref / FOV ← smooth(cmd)
```

---

## 五、端侧小模型：Tiny Shot Advisor

> 大 VLM/CLIP 只做离线老师；端侧只跑 10M–25M 的小模型。

### 模型架构

```
图像 Backbone（MobileNetV3 / TinyViT）
        ↓ image feature

几何/规则特征 MLP
        ↓ state feature

候选模式/参数 Embedding
        ↓ action feature

三者 concat → MLP Head
        ↓
多任务输出
```

**输出结构：**

```json
{
  "mode_scores": { "lock": 0.22, "oblique": 0.76, "parallax": 0.83 },
  "quality": { "composition": 0.74, "lighting": 0.69, "motion_potential": 0.86 },
  "risk": { "recommend_lock": 0.08, "motion_too_aggressive": 0.21 },
  "param_delta": { "distance": 0.5, "height": 0.2, "phi": -8.0 }
}
```

> 参数修正只做 residual：`θ_final = θ_rule + Δθ_model`，不直接输出完整参数。

### 三个档位

| 档位 | Backbone | 参数量 | 适合 |
|---|---|---|---|
| A 极简版 | MobileNetV3-Large | ~5M | 第一版实机 Demo，最稳最快 |
| B 平衡版（推荐） | TinyViT-11M / 21M | 15–25M | 正式版，全局构图/背景/光照更好 |
| C CLIP 风格版 | MobileCLIP-S0 image encoder | ~12M | 保留"电影感/旅行感"文本风格对齐 |

**C 档关键**：离线预计算 text prompt embedding，端侧只跑 image encoder，不部署完整 CLIP。

---

## 六、训练策略：大模型离线蒸馏小模型

### 离线标签来源

| 来源 | 标签内容 |
|---|---|
| 大 VLM | scene_type / background_quality / recommended_shots / avoid_shots |
| 大 CLIP/SigLIP | cinematic_score / travel_score / sports_score / bad_composition_score |
| 规则系统 | 构图位置 / 目标尺度 / 视觉动感 / 稳定性 / 控制压力（最可靠） |
| 人工 A/B | 少量偏好修正审美方向 |

### 训练任务

1. **语义蒸馏**：小模型预测 VLM 的结构化标签（cross entropy / BCE）
2. **CLIP 风格蒸馏**：MSE 拟合 CLIP 风格分数
3. **规则评分拟合**：MSE 拟合规则 scorer 输出
4. **候选排序**：pairwise ranking，`P(A>B) = σ(R_A - R_B)`
5. **风险回退**：二分类，是否应该退回 lock

---

## 七、系统模块总览

```
1. Perception Parser
   目标 / 人体 / 背景 / 深度 / 光照 / 前景 / 运动状态

2. Cinematic Semantic Encoder
   s_view / s_scale / s_motion / s_stability / s_reveal

3. Shot Primitive Library
   lock / oblique / orbit / parallax / reveal /
   push-in / pull-out / rise / leading-follow

4. Candidate Generator
   每个模式采样有限参数

5. Hybrid Scorer
   规则分 + VLM分 + CLIP风格分 + Reward Model分

6. Mode Switch Manager
   滞回 / 驻留时间 / 风险回退 / 平滑过渡

7. Reference Generator
   phi_ref / d_ref / h_ref / FOV_ref / screen_pos_ref

8. Controller
   位置控制 / 云台控制 / 速度加速度限制

9. Post-processing（后期）
   自动裁切 / 稳定 / 调色 / 慢动作 / 音乐卡点 / 封面选择
```

---

## 八、研发阶段

| 阶段 | 目标 | 内容 |
|---|---|---|
| **第一阶段** | 先能稳定跑 | lock / oblique / orbit / parallax / pull-out + 纯规则打分 |
| **第二阶段** | 从"会跟拍"到"会推荐" | 接入 VLM/CLIP 场景判断（背景/前景/逆光/适合人像） |
| **第三阶段** | 真正有"审美偏好" | 收集 A/B 偏好数据，训练 Reward Model |
| **第四阶段** | 热门效果 + 生成式预览 | AI preview / 风格预设 / 一键电影感 / 旅行大片 |

---

## 九、保留 & 扩展建议

**原有文档中应保留：**
语义空间建模 / 模式决策 / lock-oblique-orbit 最小模式 / 滑窗平滑 / 风险回退 / 滞回机制 / 最小驻留时间 / 方位角平滑过渡

**需要扩展的模式：**
parallax / push-in / pull-out / rise reveal / foreground reveal / leading follow / hero shot

**评分升级方向：**
纯几何语义距离 → 几何规则 + 场景语义 + 审美偏好 + 热门风格

**不建议现在做：**
直接训练未来轨迹生成器 / 完全依赖 VLM 判断运动参数 / 每种风格一个 LoRA 控制无人机

---

## 十、核心公式

```
(m*, θ*) = argmax_{m∈M, θ∈Θ_m} S(m, θ | o_t, s_t, z_t, style)

S = S_gate × (α·S_comp + β·S_motion + γ·S_style + δ·S_aesthetic + η·S_feas - λ·S_switch)
```

- `S_gate`：硬约束（出框/碰撞/超限 → 0）
- `S_comp`：构图分
- `S_motion`：动感分
- `S_style`：风格匹配分
- `S_aesthetic`：学习型审美分（Reward Model）
- `S_feas`：可执行性分
- `S_switch`：切换惩罚
