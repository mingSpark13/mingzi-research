# Transformer Decoder vs MLP Head 学习笔记

## 学习背景
这次重点理解的是：
- `4 层 Decoder` 在视觉/多模态网络里到底是什么意思
- 它和“最后接几层全连接”不是一回事
- Decoder head 与普通 MLP / 回归头相比，多了什么、什么时候值得保留、什么时候可能是浪费
- 对当前单目标 `(u, v, d)` 回归 + 时序任务，什么结构更划算

---

## 一、4 层 Decoder 到底是什么意思

这里的 `4 层 Decoder` 不是：
- 最后接了 4 层全连接层

而是：
- **堆了 4 个 Transformer Decoder block**

每一个 decoder block 一般都包含：
1. Query 之间的 **self-attention**
2. Query 对 encoder memory 的 **cross-attention**
3. **FFN 前馈网络**

如果当前结构是：
- Encoder 输出 memory: `(301, bs, 256)`
- Decoder queries: `3 learned embeddings -> (3, bs, 256)`

那它的真实含义是：
- 有 3 个 query token
- 它们连续经过 4 个 decoder block
- 每一层都在反复做：

```math
Q \leftarrow SelfAttn(Q)
Q \leftarrow CrossAttn(Q, memory)
Q \leftarrow FFN(Q)
```

所以 **4 层 Decoder 的本质**就是：
> 让这 3 个 query 连续 4 轮去读 encoder 提供的图像/状态特征，并不断 refine 自己。

---

## 二、Decoder 的作用是什么

### 直观理解
- **Encoder** 更像：把整张图和状态编码成全局特征记忆
- **Decoder** 更像：带着“问题”去 memory 里捞需要的信息

可以把 learned queries 理解成一组“提问向量”：
- query 0：偏向“人在哪”
- query 1：偏向“距离是多少”
- query 2：偏向“辅助信息是什么”

当然这些不是手工指定，而是训练过程中自己学出来的。

### 所以 Decoder 在做什么
它是在做一种：
- **查询式读图 / 检索式读特征**
而不是简单的：
- **整图压缩后直接回归**

---

## 三、普通尾部网络 vs Decoder 式输出头

### 1. 普通尾部网络
常见写法：

```math
f = Backbone(I)
z = GAP(f)
\hat{y} = MLP(z)
```

流程是：
- backbone 提特征
- pooling / flatten
- MLP
- 直接回归 `(u, v, d)`

#### 特点
- 简单
- 快
- 参数少
- 非常适合单目标回归

#### 问题
- 整个特征图会被压成一个向量
- 缺少“按问题去读图”的显式机制
- 多输出头之间共享 backbone，但交互较弱

---

### 2. Decoder 式输出头
流程是：
- 不直接把整张图压成一个向量
- 保留空间 token / memory
- 让 query 去和这些 token 交互
- 最后输出查询式的 token，再丢给 head

#### 优势
- 更适合结构化输出
- 更适合多目标 / 多 query / 多槽位问题
- 更适合“从整张图里找证据”

这也是为什么 DETR 一类检测器会用 decoder：
- 每个 query 对应一个候选目标
- query 去 image memory 里找自己负责的那个物体

---

## 四、为什么当前任务里 Decoder 可能有点浪费

如果任务只是：
- 单目标
- 一张图回归一个 `(u, v, d)`
- 后续还要上时序模块

那 decoder 的“查询能力”很可能已经强于任务需求。

因为当前并不是：
- 多目标检测
- 多实例匹配
- 文本条件 grounding
- 动作序列 token 解码

而只是：
> 从一张图里回归一个目标的位置和距离

所以很多时候，更直接的结构可能更划算：
- Encoder / CNN 提特征
- GAP 或 attention pooling 得到紧凑表示
- 拼状态
- 接 GRU 做时序
- 最后用 MLP 输出 `(u, v, d)`

---

## 五、Decoder 比普通 MLP head 多了什么

### 普通 MLP head
可以理解成：
> “我把整张图总结成一句话，然后直接回答。”

### Transformer Decoder head
可以理解成：
> “我先准备几个问题，然后拿着问题去翻整张图的特征笔记，找到答案后再回答。”

所以：
- **MLP** 更像整体压缩式读图
- **Decoder** 更像检索式读图

---

## 六、4 层是不是越多越好

不一定。

4 层 decoder 的含义是：
- query 进行多轮 refinement

但对于当前这类单目标回归任务：
- 1 层可能已经够用
- 2 层通常也够了
- 4 层未必比 2 层明显更强
- 反而更慢、更难训、参数更多

如果后面还要加时序模块，算力预算通常更应该优先给：
- **时间维建模**
而不是给：
- **过深的 decoder 深度**

---

## 七、什么时候 Decoder 很值

Decoder 更适合这些场景：

### 1. 多目标
例如画面里有多个人、多物体，需要多个 query 分别负责不同目标。

### 2. 条件查询
例如：
- 找红衣服的人
- 找左边那个目标
- 找指定类别物体

这时 query 可以带条件信息。

### 3. 多槽位输出
例如同时输出：
- 当前目标
- 障碍物
- 可通行区域
- 未来落脚点

### 4. 动作序列 / 轨迹 token 化
像 ACT 一类结构中，decoder 更适合解码结构化输出序列。

---

## 八、对当前模型更合适的替代

### 方案 A：去掉 decoder
直接用：
- ResNet18
- Conv投影
- spatial pooling / attention pooling
- 拼状态
- GRU
- MLP heads

### 方案 B：保留 encoder，不保留 decoder
- 把 encoder 当成空间建模器
- 把输出池化成全局表示
- 再做时序建模

这通常会比：
- `encoder + 4层 decoder + 后续再加 GRU`
更干净，也更适合当前单目标 + 时序任务。

---

## 九、最短结论

当前这里的 `4 层 Decoder` 指的是：
> 3 个 learned queries 经过 4 个 Transformer decoder block，反复通过 self-attention 和 cross-attention 从 encoder memory 中读信息，再输出给 position head / distance head。

它和普通尾部 MLP 的主要区别是：
- **MLP head**：整体压缩后直接回归，简单高效
- **Decoder head**：query 式地从空间特征里检索信息，更适合多目标与结构化输出

而对于当前这个：
- 单目标 `(u, v, d)` 回归
- 后续还要加时序建模

很多情况下，decoder 确实不是最划算的部分，**完全可以考虑砍掉或显著简化**。

---

## 十、一句话记忆
> Decoder 更像“带着问题去查特征”，MLP 更像“把整图压缩后直接回答”。

对当前单目标 + 时序任务，通常 **简单 encoder/pooling + GRU + MLP heads** 会更划算。
