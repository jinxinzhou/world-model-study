# Abstract 写作模板与拆解

**🌐 Language**: 🇨🇳 **中文** · [🇬🇧 English](Abstract-Writing-EN.md)

> 本文从 PlaNet (Hafner et al., ICML 2019) 的 abstract 中提炼出一套**通用的"5 步走"写作模板**,并附上原文逐句拆解。

---

## 一、为什么 Abstract 这么重要

- **审稿人的第一印象 80% 来自 abstract**。绝大多数审稿人会先扫 abstract + 图,再决定要不要细读
- **arXiv 浏览者**只会看 abstract 决定是否点 PDF
- **搜索引擎 + Google Scholar**索引,abstract 决定召回率
- **未来读者**(包括自己 1 年后回看)第一眼看的就是 abstract

→ **abstract 不是"摘要",而是"全文最重要的 8 句话"**。

---

## 二、5 步走结构(从 PlaNet 提炼的通用模板)

| 步骤 | 角色 | 句数 | 关键问题 |
|:----:|------|:---:|---------|
| **① 问题铺垫** | Hook —— 建立 context | 2–3 | 「这个领域有什么长期挑战?为什么旧方法不够?」|
| **② 提出方法** | 给方法命名 + 一句定位 | 1 | 「我们做了什么?用一句话说清。」|
| **③ 技术贡献** | 列 1–2 个关键技术创新 | 1–2 | 「为什么我们能 work?核心 trick 是什么?」|
| **④ 实验设定** | 强调任务难度 | 1 | 「在多难的场景上验证?」|
| **⑤ 结果对比** | 数字 + 与 SOTA 对比 | 1 | 「比 baseline 强多少?用了多少数据/算力?」|

**总长度**:8–10 句话最佳(约 150–250 词)。

---

## 三、通用模板(可直接套用)

```
[1] [领域] 在 [已知条件下] 已经很成功。
[2] 但要把 [方法/能力] 扩展到 [未知条件],需要解决 [核心难点]。
[3] 然而 [更具体的挑战] 一直是长期问题,尤其是在 [极端条件] 下。

[4] 我们提出 [方法名](缩写),一个 [定位] 的 [方法类型],
    它 [核心机制] 来解决 [目标]。

[5] 要达到 [关键性能指标],必须解决 [子问题]。
[6] 我们用 [技术 1] 和 [技术 2] 来处理。

[7] 仅使用 [输入限制],我们的方法解决了具有 [难点 a, b, c] 的任务,
    这些难度超过了 [前人能解决的范围]。

[8] [方法名] 用 [N 倍少的资源] 达到 [接近 / 超过] 强基线 [SOTA] 的性能。
```

---

## 四、案例:PlaNet 摘要逐句拆解

### 原文

> [1] Planning has been very successful for control tasks with known environment dynamics.
> [2] To leverage planning in unknown environments, the agent needs to learn the dynamics from interactions with the world.
> [3] However, learning dynamics models that are accurate enough for planning has been a long-standing challenge, especially in image-based domains.
> [4] We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning in latent space.
> [5] To achieve high performance, the dynamics model must accurately predict the rewards ahead for multiple time steps.
> [6] We approach this using a latent dynamics model with both deterministic and stochastic transition components.
> [7] Moreover, we propose a multi-step variational inference objective that we name latent overshooting.
> [8] Using only pixel observations, our agent solves continuous control tasks with contact dynamics, partial observability, and sparse rewards, which exceed the difficulty of tasks that were previously solved by planning with learned models.
> [9] PlaNet uses substantially fewer episodes and reaches final performance close to and sometimes higher than strong model-free algorithms.

### 中文翻译

> [1] 对于环境动力学已知的控制任务,规划方法已经非常成功。
> [2] 而要把规划用于未知环境,agent 需要通过与世界的交互来学习动力学。
> [3] 然而,学到一个精度足以支持规划的动力学模型一直是个长期挑战 —— 尤其在基于图像的领域。
> [4] 我们提出 **Deep Planning Network(PlaNet)**—— 一个纯 model-based 的 agent,它直接从图像中学习环境动力学,并通过在 latent 空间中快速在线规划来选择动作。
> [5] 要达到高性能,动力学模型必须能准确预测未来多步的奖励。
> [6] 为此,我们使用一个**同时包含确定性和随机性转移分量**的 latent 动力学模型。
> [7] 此外,我们提出了一种**多步变分推断目标**,将其命名为 **latent overshooting**。
> [8] 仅使用像素观察,我们的 agent 就能解决具有**接触动力学**、**部分可观测性**和**稀疏奖励**的连续控制任务 —— 这些任务的难度超过了以往用学到的模型做规划所能解决的范围。
> [9] PlaNet 使用的 episode 数大幅减少,最终性能接近、有时甚至超过强大的 model-free 算法。

### 逐句对应模板

| 原句 | 模板步骤 | 该句的作用 |
|:----:|:--------:|----------|
| [1] | ① Hook 起点 | 建立「规划已知动力学」这个共识 |
| [2] | ① 痛点过渡 | 引出「未知动力学」这个 gap |
| [3] | ① 具体化 | 把痛点窄化到「图像域、精度不够」 |
| [4] | ② **提出方法 + 命名** | 给名字 (PlaNet) + 一句定位:**纯 model-based + 像素输入 + latent 规划** |
| [5] | ③ 引出技术挑战 | 关键问题:多步精准预测 |
| [6] | ③ **技术贡献 1** | 双路 latent(deterministic + stochastic) |
| [7] | ③ **技术贡献 2** | latent overshooting(命名 + 简介) |
| [8] | ④ **实验难度** | 强调三大难点(contact / partial obs / sparse rewards) |
| [9] | ⑤ **结果对比** | 数字省略但点明「样本少 + 性能 ≥ model-free SOTA」 |

---

## 五、关键写作技巧(从 PlaNet 摘要学到的)

### 1. 第一句要建立"已知 vs 未知"的张力

```
✅ "Planning has been very successful for control tasks with known environment dynamics."
   → 立刻让读者明白:这里要把规划从「已知」推到「未知」
```

**反例**:
```
❌ "Reinforcement learning is an important field with many applications."
   → 空泛,没建立 gap
```

### 2. 方法命名要有"标识度"

PlaNet 的命名做得很好:
- **PlaNet** = **Pla**nning **Net**work → 中文可叫「行星网络」(双关地球/规划)
- 短(2 个音节)、好记、和功能直接相关

**对比常见反例**:
- ❌ `DLLDMRL`(Deep Latent-Logic Dynamics Model with RL)→ 没人记得住
- ✅ Dreamer / GATO / Sora / PaLM → 简单的英文单词最容易传播

### 3. "命名 + 简介"放在同一句

```
✅ "We propose the Deep Planning Network (PlaNet), a purely model-based agent that ..."
```

- 名字 + 全称 + 缩写**一次性给出**
- 紧跟一个**「a ...」同位语**,一句话定位
- 比起分两句写「We propose X. X is ...」更紧凑

### 4. 用"数字 + 对比"代替"提升 / 改进"

PlaNet 摘要里没用具体数字,但论文 Table 1 给出了:
- PlaNet 用 **2,000 episodes** 达到 D4PG **100,000 episodes** 的性能

**写到 abstract 里就是**:
```
✅ "PlaNet uses 50× fewer episodes than D4PG to reach competitive performance."
```

**反例**:
```
❌ "PlaNet significantly improves sample efficiency."
   → 「显著提升」是空话,审稿人最讨厌
```

### 5. 实验难度堆叠(强化贡献)

```
✅ "...solves continuous control tasks with contact dynamics, partial observability, and sparse rewards"
   → 一口气列了 3 个难点,显示方法的鲁棒性
```

**反例**:
```
❌ "...solves several control tasks"
   → 模糊,审稿人会怀疑是 cherry-picked easy tasks
```

### 6. 不要在 abstract 里讲 limitation 或 future work

abstract 是**让人想读全文的"广告"**,不是"完整的总结"。把局限留到 discussion section。

---

## 六、反模式 / 应避免的写法

| ❌ 反模式 | 为什么不好 | ✅ 改进 |
|----------|----------|--------|
| "We propose a novel framework that..." | "novel" 是空话,审稿人最反感 | 直接说做了什么:"We propose X, which does Y" |
| "Extensive experiments show..." | 套话,信息量为零 | 列具体数字 + 具体 benchmark 名 |
| 缩写满天飞(VAE, MDN, RSSM, ELBO 一行 4 个) | 阅读门槛高,读者不耐烦 | 第一次用先展开,后续才缩写 |
| 一句话超过 30 词 | 难读 | 拆成两句 |
| 用大词("paradigm-shift", "revolutionary") | 显得不自信 | 让数字和实验说话 |
| 完全不提 baseline | 读者无法判断价值 | 必须有「vs SOTA」的明确对比 |

---

## 七、清单(写完 abstract 自检 6 问)

- [ ] 第一句是否在 30 秒内让外行明白「这个领域有什么问题」?
- [ ] 方法名是否短、好记、有标识度?
- [ ] 是否在前 4 句就给出了方法名?
- [ ] 技术贡献是 **1–2 个**,而不是 5–6 个堆砌?
- [ ] 是否有**具体的数字**(N× / N M 帧 / +X 分)?
- [ ] 是否明确点出**对比的 baseline 名字**(不是模糊的 "prior work")?

通过 6 条 → 这是一份合格的 abstract。

---

## 八、可借鉴的其他经典 abstract

| 论文 | abstract 值得学的点 |
|------|-------------------|
| **AlphaGo** (Nature 2016) | 第一句直接给震撼数字(战胜专业棋手)|
| **Transformer** (Vaswani 2017) | 极致简洁:"based solely on attention mechanisms" |
| **BERT** (2018) | 在结果句直接给 11 个 task 上的具体提升 |
| **GPT-3** (Brown 2020) | 用"175B parameters"作为 hook |
| **DreamerV3** (2023) | 强调"single set of hyperparameters" 作为核心卖点 |

→ 后续读这些论文时,可以专门精读 abstract,继续完善这份模板。

---

## 九、一句话总结

> **一份好的 abstract = 用 8–10 句话讲清楚「问题 → 方法 → 技术贡献 → 实验难度 → 结果对比」,每一句都有信息量,没有套话,有具体数字和 baseline 名字。** PlaNet 的 abstract 是教科书级别的范例,值得反复读、逐句拆。

---

_提炼自:[PlaNet (Hafner et al., 2019)](https://arxiv.org/abs/1811.04551) · 最后更新:2026-06_
