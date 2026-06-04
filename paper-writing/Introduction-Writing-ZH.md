# Introduction 写作模板与拆解

**🌐 Language**: 🇨🇳 **中文** · [🇬🇧 English](Introduction-Writing-EN.md)

> 本文从 PlaNet (Hafner et al., ICML 2019) 的 Introduction 章节中提炼出一套**通用的"5–6 段叙事弧线"模板**。

---

## 一、Introduction 的核心任务

Abstract 是「广告」,Introduction 则是「说服书」—— 用 1–2 页让审稿人接受 4 件事:

1. **这个问题存在**(且重要)
2. **解决它有价值**
3. **前人没解决好**(但他们做的也不能轻视)
4. **我们的方法值得一看**

→ Introduction 没说服力,审稿人后面看实验数据再好也会半信半疑。

---

## 二、标准 5–6 段叙事弧线

| 段 | 角色 | 字数 | 关键问题 |
|:--:|------|------|---------|
| **① What's the problem** | 打地基 + 列痛点 | 较长 | 这个领域的长期挑战是什么? |
| **② Why it matters** | 价值主张 | 中等 | 解决了能带来什么好处? |
| **③ What others did** | 缩小 gap | 中等 | 前人做到哪步了?哪里还没解决? |
| **④ What we propose** | 提出方法 | 短 | 我们的方法是什么?一句话定位 |
| **⑤ Concrete contributions** | bullet 列表 | 中等 | 1–3 个具体技术贡献(对应 abstract) |
| **⑥ Figure / Table 引用**(可选) | 视觉锚点 | 极短 | 引向首图,让读者建立直觉 |

---

## 三、各段的"句子模板"

### ① What's the problem(打地基 + 列痛点)

```
[领域] is a natural / powerful / important approach for [scope where it works well].
To extend this to [unknown / harder condition], the agent needs to [necessary capability].
However, [specific challenge] has been a long-standing challenge.
Key difficulties include [pain 1], [pain 2], [pain 3], and [pain 4].
```

🔑 **关键技巧**:**列 3–4 个具体痛点**(不是泛泛而谈"很难"),向审稿人展示"我们真懂这个 domain"。

### ② Why it matters(价值主张)

```
[Our approach class] offers several benefits over [alternative class]:

First, [benefit 1 with reason] — [optional citation].
Moreover, [benefit 2 with future implication] — as shown by [citation].
Finally, [benefit 3, often transferability / generality].
```

🔑 **关键技巧**:
- **3 个独立卖点**(First / Moreover / Finally)
- 每个卖点配 1 个引用,显得有根据
- 不要超过 3 条(4+ 显得啰嗦)

### ③ What others did(给前人 credit,然后缩小 gap)

```
Recent work has shown promise in [narrow setting] ([citations]).
However, these approaches typically assume [strong assumption] / are limited to [narrow scope].
In [our setting], we would like to [extension goal].
The success of such methods has previously been limited to [explicit limitation],
e.g., [concrete example].
```

🔑 **关键技巧**:
- **先承认前人贡献,再点 gap** —— 不要直接踩前人(审稿人可能是前人)
- 把"前人做到 X,我们要做 X+1"具体化 —— 比"prior work is limited" 强 100 倍

### ④ What we propose(提出方法)

```
In this paper, we propose [Method Name] ([abbreviation]),
a [positioning] that [core mechanism] to [accomplish goal].
To achieve [key property], we use [Technique 1] and propose [Technique 2 — your own].
[Method] solves [hard setting] that [exceeds prior work's scope].
```

🔑 **关键技巧**:
- 方法名 + 全称 + 缩写**第一次出现就一次性给全**
- **直接回应段 ③ 的 gap** —— 形成「问题 → 方法」的精确对应
- 结尾给"难度承诺"(比前人 setting 难)

### ⑤ Concrete contributions(bullet 列表)

```
Key contributions of this work are summarized as follows:

• [Contribution 1 name]:  [1–2 sentences with concrete number or claim]
• [Contribution 2 name]:  [1–2 sentences]
• [Contribution 3 name]:  [1–2 sentences with claim of generality]
```

🔑 **关键技巧**:
- **3 条最佳**(不要 5+ 条,会被读者忘)
- 每条给一个**「关键词」名字**(便于全文/讨论里引用),用粗体
- 至少 1 条带**具体数字**(N×、+M 分)
- 至少 1 条暗示**通用性 / 可迁移**(显得贡献不是 hack)
- **与 abstract 的 3 个贡献一一对应**,但 intro 这里可以多一点具体细节

---

## 四、6 段叙事的"逻辑齿轮"

```
段 ① 痛点 ──── 引出 ────► 段 ② 价值
   │                          │
   └────────问题大,值得解决────┘
                              │
段 ③ 前人 ◄─── 但他们没解决 ──┘
   │
   └──── 留下具体 gap ──► 段 ④ 提出方法
                              │
                              └──── 一一对应 gap ──► 段 ⑤ 贡献清单
                                                            │
                                                            └──► 段 ⑥ 看图
```

**关键检查**:段 ③ 的 gap 和段 ④ 的方法**必须一一对应**。如果段 ③ 列了 3 个 gap,段 ④ 也要明确点出方法怎么解决这 3 个。

---

## 五、自检 8 问

写完 Introduction 之后过一遍:

- [ ] 第一段是否列了 **3–4 个具体痛点**,而非泛泛说"难"?
- [ ] 是否有「**Why it matters**」段,给出 2–3 个**独立**价值?
- [ ] 是否给了前人 **credit + citation**,而非直接踩?
- [ ] 前人的 **gap 是否具体**(可以指着说"他们这点没做")?
- [ ] 方法是否**直接回应**前人的 gap(每个 gap 对应一个 contribution)?
- [ ] **方法名 + 缩写**是否在第 4 段就出现?
- [ ] **Contributions bullets** 是否 3 条以内,每条带关键词名字?
- [ ] Bullets 里至少 1 条是否有**具体数字**?

通过 8 条 → 合格的 Introduction。

---

## 六、案例:PlaNet 的 Introduction 是范本

PlaNet 的 Section 1 严格遵守这个 6 段模板:

| 段 | PlaNet 实例 | 提炼出的技巧 |
|:--:|------------|-------------|
| ① | 列了 model accuracy / 多步误差 / 多模态 / 过度自信 **4 个痛点** | 立刻展示 domain expertise |
| ② | First (样本效率) / Moreover (越算越强) / Finally (任务迁移) | 三段式价值主张 |
| ③ | 先肯定 Deisenroth 2011 等;但他们假设知道 state;高维只解过 cartpole | 给 credit + 具体化 gap |
| ④ | "We propose PlaNet, a model-based agent that..." 一句定位 | 命名 + 全称 + 缩写 + 定位四合一 |
| ⑤ | **3 个 bullets**:Latent planning / RSSM / Latent overshooting | 一一对应 abstract,各带具体数字 (200× / both crucial / compatible) |
| ⑥ | Figure 1 展示 6 个 DMC 任务 | 让读者看到"我们要解决的任务长这样" |

详细原文 + 中文翻译见:[World Models 学习笔记 §4.2 PlaNet](../World-Model-学习笔记.md#42-planet-2019)。

---

## 七、可借鉴的其他经典 Introduction

| 论文 | Introduction 的特色 |
|------|--------------------|
| **AlphaGo** (Nature 2016) | 第一段就给震撼数字:战胜专业棋手 |
| **Transformer** (2017) | Intro 极简 5 段,迅速进入"attention is all you need" |
| **GPT-3** (2020) | 大量引用 scaling laws,把"为什么做大"作为整篇主线 |
| **Sora 技术报告** (2024) | 不走标准 ML 范式,改用 "vision-first" 叙事 |

---

## 八、一句话总结

> **Introduction 是「问题 → 价值 → 前人 gap → 我们的方法 → 贡献清单」的 6 段叙事。每一段都有具体职责,段 ③ 的 gap 必须和段 ④ 的方法一一对应,这是审稿人最看重的逻辑齿轮。** PlaNet 的 Section 1 是教科书级别的范例。

---

_提炼自:[PlaNet (Hafner et al., 2019)](https://arxiv.org/abs/1811.04551) Section 1 · 最后更新:2026-06_
