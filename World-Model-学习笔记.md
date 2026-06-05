# World Model 学习笔记

**🌐 Language**: **中文** · [English](World-Model-Study-Notes.md)

> 整理自 2026 年 4–5 月的学习讨论。按「是什么 → 为什么重要 → 流派对比 → 怎么入门」的逻辑组织。
>
> 💡 每章使用可折叠区块,点击 ▶ 标题即可展开/收起。

---

## 目录

- [一、World Model 是什么](#一world-model-是什么)
- [二、为什么 World Model 火?实际价值在哪?](#二为什么-world-model-火实际价值在哪)
- [三、三大流派深入对比](#三三大流派深入对比)
- [四、必读论文](#四必读论文)
- [五、参考资料汇总](#五参考资料汇总)

---

## 一、World Model 是什么

<details>
<summary><b>展开 / 收起</b></summary>

World Model(世界模型)是 AI agent 领域的热门方向,核心思想是让模型学会**预测环境未来状态**,从而支持规划、决策和想象式推理。

目前主要分三大流派(详见 [§3](#三三大流派深入对比)):

| 流派 | 代表 | 预测对象 |
|------|------|---------|
| **生成式 / 视频派** | Sora、Genie、GAIA | 像素 / 视频帧 |
| **Latent Dynamics(RL 派)** | Dreamer v1/v2/v3、PlaNet | latent state(带像素重建) |
| **JEPA(预测式表征派)** | I-JEPA、V-JEPA、V-JEPA 2 | 抽象 embedding(无重建) |

先明确所关心的流派,学习路径差别很大。

</details>

---

## 二、为什么 World Model 火?实际价值在哪?

<details>
<summary><b>2.1 为什么突然火起来</b></summary>

**1. LLM 撞墙了,需要新叙事**
纯语言模型在物理推理、长程规划、具身任务上表现差。业界共识:**光靠文本预测下一个 token,学不到真正的物理常识**。LeCun 带头喊「LLM 是死胡同」,JEPA / World Model 成了替代路线的旗帜。

**2. Sora 出圈(2024 初)**
OpenAI 把 Sora 定位为 "world simulator" 而不是视频生成器,直接把这个概念推成顶流。资本和媒体迅速跟进。

**3. 具身智能 / 机器人 / 自动驾驶爆发**
特斯拉 FSD、Wayve、1X、Figure、Physical Intelligence 都需要一个东西:**在部署前大规模、低成本地模拟真实世界**。真机采数据太贵太慢,world model 是唯一可扩展方案。

**4. 技术条件成熟**
- Diffusion + Transformer 让视频生成质量跨过可用门槛
- Dreamer v3 首次证明**同一套超参**能解 150+ 任务,包括 Minecraft 钻石(纯 model-based,世界首次)
- 算力和数据规模起来了

**5. Scaling Law 需要新战场**
文本数据快用完了,视频/交互数据是下一个金矿,world model 是消化这些数据的自然架构。

</details>

<details>
<summary><b>2.2 实际价值(按落地成熟度排序)</b></summary>

#### ✅ 已经在赚钱 / 明确有用

**1. 自动驾驶仿真**
- [Wayve GAIA-1](https://wayve.ai/thinking/scaling-gaia-1/) / [GAIA-2](https://wayve.ai/thinking/gaia-2/)、[英伟达 Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)、特斯拉内部模型
- 价值:生成海量 corner case(暴雨、突然冲出的行人),**把单公里测试成本从几美元降到几分钱**
- 解决真实路测**长尾数据**采不到的根本问题

**2. Model-based RL(机器人控制)**
- [Dreamer 系](https://danijar.com/project/dreamerv3/)在真实机器人上已经能做到**几小时真机数据学会新技能**(传统 model-free 要几天)
- Google DeepMind、[1X](https://www.1x.tech/discover/1x-world-model)、[Physical Intelligence](https://www.physicalintelligence.company/) 都在用
- 价值:**样本效率提升 1–2 个数量级**,真机训练才可行

**3. 游戏 / 内容生成**
- [Genie 2](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/)、[Oasis](https://oasis-model.github.io/)(Minecraft 实时生成)、[DIAMOND](https://github.com/eloialonso/diamond)
- 价值:**无需游戏引擎**就能生成可交互世界,长期看可能颠覆游戏开发流程

#### 🟡 有潜力但尚未规模化

**4. Agent 规划 / 推理**
- 给 LLM agent 一个 world model,让它"在脑子里"试错再行动
- 类似人类的"想象力",是通往 AGI 的关键拼图之一

**5. 科学仿真**
- 流体、天气、材料、蛋白动力学
- [GraphCast](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/)、[AlphaFold](https://alphafold.ebi.ac.uk/) 某种意义上就是领域专用 world model
- 价值:比传统数值模拟快 1000–10000 倍

**6. 视频生成 / 影视**
- [Sora](https://openai.com/sora/)、[可灵 Kling](https://kling.kuaishou.com/)、[Runway](https://runwayml.com/)
- 价值:内容生产力工具,但"物理真实"仍不达标

#### 🔴 还在画饼

- 通用物理推理引擎
- 真正的"心智模拟器"用于通用 Agent
- 端侧实时世界模型

</details>

<details>
<summary><b>2.3 冷静看待:真实的局限</b></summary>

1. **评估极难** — 什么叫"世界建模得好"?没有公认指标,容易自欺欺人
2. **长时序不稳定** — 目前生成几十秒后就开始漂移、违反物理
3. **算力贵** — 训一个像样的视频 world model 成本 > 训 LLM
4. **LeCun 的 JEPA 路线尚未证明能 scale** — 还是愿景阶段
5. **"World Model" 有被滥用嫌疑** — 很多公司把普通视频生成包装成 world model 炒估值

</details>

<details>
<summary><b>2.4 一句话总结</b></summary>

> **短期价值在机器人和自动驾驶的仿真训练(已经赚到钱);长期价值在于它可能是 LLM 之后的下一代 AI 基础架构 —— 让模型真正"理解"而不是"背诵"世界。**

</details>

---

## 三、三大流派深入对比

<details>
<summary><b>3.1 三大世界模型流派总览</b></summary>

| 流派 | 代表 | 预测对象 | 目标 |
|------|------|---------|------|
| **生成式 World Model** | Sora、Genie、GAIA、DIAMOND | **像素 / 视频帧** | 生成可视化的未来 |
| **Latent Dynamics(RL 派)** | Dreamer v1/v2/v3、PlaNet | **latent state**(但仍带重建损失) | 服务于 model-based RL 规划 |
| **JEPA(预测式表征)** | I-JEPA、V-JEPA、V-JEPA 2 | **抽象 embedding**,不重建像素 | 学习世界的结构化表征 |

</details>

<details>
<summary><b>3.2 JEPA 的核心主张</b></summary>

JEPA 是 LeCun 力推的**第三条路线**,自成一派 —— 「预测式表征学习(Predictive Embedding)」。

LeCun 的观点很鲜明:

> **"不要预测像素,预测表征。"**

**原因**:
- 像素级预测浪费算力在无关细节上(云的形状、树叶抖动)
- 世界本质上不可完全预测,强行重建会学到噪声
- 人脑也不是在"脑内渲染 4K 视频",而是在抽象层面预测

**做法**:
- 用 encoder 把观测映射到 latent
- 用 predictor 在 **latent 空间**预测被遮挡/未来部分的 embedding
- 用 **stop-gradient + EMA target encoder** 防止坍塌(类似 BYOL / DINO)
- **没有 decoder,不做像素重建**

</details>

<details>
<summary><b>3.3 JEPA vs Dreamer 的关键区别(容易混)</b></summary>

两者都在 latent 空间预测,但:

| | Dreamer | JEPA |
|---|---------|------|
| 是否重建像素 | **是**(reconstruction loss 是核心监督) | **否**(纯 embedding 预测) |
| 训练信号 | 重建 + 奖励 + KL | embedding 距离 + 防坍塌 |
| 目标 | model-based RL,会用 world model 做 rollout 规划 | **自监督表征学习**,下游再接任务 |
| 是否能"想象"出画面 | 能(有 decoder) | **不能**(这是有意为之) |

所以严格说:**Dreamer 是"latent 但仍生成式"**,JEPA 才是真正的"非生成式"。

</details>

<details>
<summary><b>3.4 JEPA 现状(2024–2026)</b></summary>

**进展**
- I-JEPA(图像,2023)、V-JEPA(视频,2024)、**V-JEPA 2(2024 末)** — 在动作预测、物理理解 benchmark 上表现不错
- Meta 押注很重,LeCun 本人的旗舰项目

**质疑**
- 尚未展示 Sora / Dreamer 级别的**惊艳 demo**(因为没 decoder,demo 不直观)
- Scaling 到底行不行还没定论
- 社区大部分还是在生成式路线上卷

**一句话定位**:

> **JEPA 是 LeCun 赌的"反 Sora"路线:用抽象表征而非像素来建模世界,理论优雅但工程证据还不够。目前属于「学术声量大、产业落地少」的阶段。**

</details>

---

## 四、必读论文

<details>
<summary><b>4.0 前置概念:Model-Free vs Model-Based RL</b></summary>

理解 World Model 的前提是先理解它在 RL 谱系里的位置。

### 「环境」是什么

环境(Environment)= **把动作变成下一状态和奖励的「黑盒」**。数学上由两个函数定义:

```
状态转移:  P(s_{t+1} | s_t, a_t)     "做了这个动作,下一步会变成什么"
奖励函数:  R(s_t, a_t)                "做了这个动作,得到多少分"
```

### 两种学习范式

**🔴 Model-Free —— 不学习环境**

Agent 把环境当**纯黑盒**:可以试动作、可以收到反馈,但**不去预测**"做 X 会怎样",只学"**这个状态下选哪个动作能拿高分**"。

- 类比:第一次玩马里奥,失败 1000 次,记住 1000 个"成功模式",但不研究跳跃物理
- DQN 的做法:输入画面 → 输出 18 个动作的 Q 值 → argmax,**从不预测下一帧**

**🟢 Model-Based / World Model —— 学习环境**

Agent 主动学一个**环境的副本**(世界模型),然后在脑子里推演。

- 类比:学会"按 A 键 → 跳 4 格"、"碰蘑菇头 → 死",可以在脑子里预演
- Dreamer 的做法:学 RSSM 预测下一个 latent + 奖励,在虚拟环境里"做梦"训 actor-critic

### 关键澄清:模型 ≠ 策略 ≠ 价值

容易混淆这三个词:

| 概念 | 学的是什么 | 谁有 |
|------|----------|------|
| **环境模型** (model) | `P(s' ∣ s,a)` 和 `R(s,a)` —— **物理规律** | 仅 model-based |
| **价值函数** (value) | `V(s)` 或 `Q(s,a)` —— **某状态有多好** | 两者都可有 |
| **策略** (policy) | `π(a ∣ s)` —— **在某状态选什么动作** | 两者都可有 |

→ **Model-free 学「该做什么」(策略/价值),但不学「世界怎么运作」(模型)**
→ **Model-based 学「世界怎么运作」(模型),然后推出「该做什么」**

### 全面对比

| 维度 | Model-Free | Model-Based |
|------|-----------|-------------|
| 是否学环境模型 | ❌ | ✅ |
| 样本效率 | **低**(需要海量交互) | **高**(可以"梦里训练") |
| 推理算力换性能 | ❌ 固定 | ✅ 可线性 scale |
| 跨任务迁移 | ❌ 几乎为零 | ✅ 大部分保留 |
| 工程复杂度 | 相对简单 | 复杂(要训世界模型) |
| 训练稳定性 | 较稳 | 易被模型误差坑(model exploitation) |
| 经典代表 | DQN、PPO、SAC | World Models、Dreamer、MuZero |

### Model-Free 代表算法谱系

```
┌─ Value-based ─────────────────────────┐
│  Q-learning → DQN → Rainbow → R2D2    │
└───────────────────────────────────────┘

┌─ Policy-based ────────────────────────┐
│  REINFORCE → TRPO → PPO ⭐ 最常用     │
└───────────────────────────────────────┘

┌─ Actor-Critic ────────────────────────┐
│  A3C → DDPG → TD3 → SAC ⭐ 连续控制   │
└───────────────────────────────────────┘
```

### 🚀 Model-Based 的真正价值:不是"省数据",是"学规律"

许多人理解 Model-Based 时只盯着「样本效率」一条优势,**但这只是表象**。

**根本差异**:
- Model-Free 学「**这个任务里该做什么**」(任务答案)
- Model-Based 学「**世界如何运作**」(物理规律)

这一个根本差异,带来**三个独立的外在表现**:

```
        Model-Based 学到世界规律
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
    ① 样本效率高   ② 推理算力可 scale   ③ 跨任务迁移
       100-1000×        无上限              几乎完全保留
```

下面逐一展开。

---

#### 优势 ①:样本效率高出 100-1000 倍

| 任务 | Model-Free | Model-Based | 提升 |
|------|-----------|-------------|-----|
| Atari Breakout | DQN/Rainbow **2 亿帧** | DreamerV3 **2000 万帧** | 10× |
| Atari 100k | Rainbow 很差 | EfficientZero 接近人类 | 巨大 |
| Crafter | PPO 几千万步,~10 分 | DreamerV3 **100 万步**,~14 分 SOTA | 30×+ |
| 真机机器人抓取 | PPO 几个月真机数据 | Dreamer 类 **几小时** | 1000× |

**为什么效率这么高?** 五个根本机制的复利效应:

| # | 机制 | 一句话说明 |
|:---:|------|----------|
| **1** | **学规律 vs 学数据点** | 网络权重存的是"物理规律"(可外推),不是"状态价值"(只能插值) |
| **2** | **梦境数据增强** | 1 条真实经验 → 训世界模型 → 梦里 rollout 几百次虚拟经验,policy 训练信号放大几百倍 |
| **3** | **自由起点探索** | 真实环境只能 reset 到初始,梦境可以任意 reset 到任何 latent state(零代价试错) |
| **4** | **解析梯度反传** ⭐ | 整条想象链可微,梯度精确反传(O(1) 样本)vs Monte Carlo 估计的高方差(O(N) 样本) |
| **5** | **长程预演** | GPU 上 15 步 latent rollout 只需 1.5ms,代替真实环境 1000 步的等待 |

💡 **直观类比 —— 学开车**:
- 🔴 Model-Free:想学下雪天开车?**必须等下雪**;想学侧翻救车?**必须真侧翻**
- 🟢 Model-Based:**真开 100 小时学会方向/刹车/摩擦力的规律**,然后**在脑中预演 10000 个 corner case**

→ 各机制的工程细节在 [§4.3 Dreamer](#43-dreamer-v1--v2--v3-2020–2023) 节会进一步展开。

---

#### 优势 ②:推理时算力换性能(Test-Time Compute Scaling)⭐ 最被忽视

**Model-Free** 的算力分配:
```
训练阶段:海量算力训 Q / Policy 网络
推理阶段:网络前向一次 → 出动作 (毫秒级)
```
→ 推理算力**固定**,给 1 秒还是 1 分钟,**输出动作相同**。性能上限就卡死。

**Model-Based** 的算力分配:
```
训练阶段:训世界模型
推理阶段:用世界模型 rollout
  - 给 1 秒  → CEM 跑 10 次迭代,选还行的动作
  - 给 1 分钟 → CEM 跑 600 次迭代,选更优的
  - 给 1 小时 → 几乎找到最优解
```
→ **推理时多花算力,性能直接更好**(只要世界模型够准)。

##### 经典案例:AlphaGo

Silver 2017(PlaNet 段 2 引用的这篇)的核心洞察:
- 训练好神经网络后,**推理时 MCTS 跑多少次直接决定棋力**
- 给 1 秒 → 业余高手
- 给 1 分钟 → 职业棋手
- 给 1 小时 → 超越人类世界冠军

##### 当代意义:o1 / o3 与"推理算力新增长曲线"

这个理念在 2024–2025 在 LLM 圈大爆发:

| 趋势 | 体现 |
|------|------|
| **OpenAI o1 / o3** | 推理时延长 chain-of-thought,性能持续提升 |
| **Q\* / MCTS + LLM** | 把 search 引入 LLM 推理 |
| **Test-time compute scaling** | 已成为 2025+ AGI 路线的关键词 |

→ 训练时 scaling(GPT-3/4)有上限;**推理时 scaling 是下一条增长曲线** —— 而它**必然需要某种 world model + search**。

→ Model-Based 范式**天然支持「算力换性能」**,Model-Free 给不了。

---

#### 优势 ③:跨任务迁移性

**为什么 Model-Free 不能迁移?**

Model-Free 学的是 `Q(s, a)` 或 `π(a|s)` —— Q 函数**和奖励紧密耦合**。换个任务、换个奖励,Q 完全作废,**从头学**。

**为什么 Model-Based 能迁移?**

Model-Based 学的是 `P(s' | s, a)` —— **转移函数只关心物理规律,和奖励无关**。换个任务,**转移函数仍然有效**。

##### 具体例子

| 新任务 | Model-Free | Model-Based |
|--------|-----------|-------------|
| "抓杯子" → "叠衣服" | **从头重训 Q** | **世界模型不变**,只需训新 reward head |
| "平地走" → "上楼梯" | **从头重训 Q** | **世界模型不变**(腿的物理一样) |
| 改 reward 形状(稀疏→密集) | **重训 Q** | **零修改** |

##### 当代意义:机器人基础模型 + LLM Agent

这个特性在 2024–2026 正在被兑现:

| 方向 | 体现 |
|------|------|
| **机器人基础模型**(Octo / OpenVLA / RT-X) | 训一个通用 dynamics → 部署到多任务 |
| **LLM Agent** | LLM 是某种语义级世界模型,同一模型做编程/推理/规划 |
| **LeCun JEPA 路线** | 核心论点正是「学世界规律 → 跨任务迁移」 |

---

#### 三者本质上是同一件事

回到根本差异:

```
                Model-Based 学「世界规律」
                          │
              不是"任务答案",是"物理 / 转移"
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   ① 样本效率高      ② 推理 scale       ③ 跨任务迁移
   一条经验榨出      规律可任意推演,    规律对所有任务有效
   更多监督信号      算力越多越准
```

**核心洞察**:**三个优势不是三件独立的事,而是「学习世界规律 vs 学习任务策略」这一根本差异的三种表现**。理解了这点,就理解了为什么 World Model 是通向 AGI 的关键路线(而不只是"提升样本效率的技巧")。

---

### 代价(没有免费午餐)

| 维度 | Model-Free | Model-Based |
|------|-----------|-------------|
| ✅ 优势 | 简单、稳定、工程门槛低 | 三大优势(见上) |
| ❌ 代价 | 样本贪婪、推理算力固定、不可迁移 | GPU 算力 ↑、工程复杂、易被模型误差坑(model exploitation) |

→ Model-Based **省的是真实数据,花的是 GPU 算力 + 工程复杂度**。

### 当下共识

- **数据廉价**(模拟器、游戏、LLM RLHF) → model-free 仍然主流
- **数据昂贵 / 需要规划 / 需要想象**(真机机器人、自驾、Agent) → world model 是未来
- **AGI 路线**:几乎所有人(Sutton、LeCun、Hassabis)都认为通用智能**必须包含 world model**

### 🎯 一句话总结

> **Model-Free RL 学「这个任务里该做什么」,Model-Based 学「世界如何运作」。这一个根本差异带来三个根本优势:① 样本效率高 100-1000 倍 ② 推理时算力可换性能(test-time scaling)③ 跨任务迁移 —— 三者其实是同一件事的三种表现。简单稳定的 Model-Free 在数据廉价场景仍是主流,但 Model-Based / World Model 是机器人、自驾、AGI 的必经之路。**

</details>

<details>
<summary><b>4.1 World Models (Ha & Schmidhuber, 2018)</b></summary>

> **论文**:[arxiv.org/abs/1803.10122](https://arxiv.org/abs/1803.10122) · **交互式网站**(强烈推荐):<https://worldmodels.github.io/>
>
> **要点**:经典起点,VAE + MDN-RNN + 小 controller,第一次在梦境里训练 agent 并迁移到真实环境。

这篇论文是现代 World Model 研究的**起点和精神图腾**。影响力不在性能多炸裂,而在于第一次清晰展示了:**Agent 可以在自己"做的梦"里学会玩游戏。**

<p align="center">
  <img src="asset/world-models-2018/world_model_comic.jpeg" width="600"/><br/>
  <i>开篇引子:Scott McCloud《Understanding Comics》中的"心智模型"</i>
</p>

### 📖 核心思想

#### 把 Agent 拆成三块

<p align="center">
  <img src="asset/world-models-2018/world_model_overview.png" width="700"/><br/>
  <i>整体架构:V (Vision) → M (Memory) → C (Controller)</i>
</p>

```
   观察 ─►  V (Vision)  ─►  M (Memory)  ─►  C (Controller)  ─►  动作
            压缩当下          预测未来          决策(很小)
```

| 模块 | 角色 | 实现 | 参数量 |
|------|------|------|--------|
| **V** — Vision | 把高维图像压成低维表示 | **VAE**(变分自编码器) | ~4M |
| **M** — Memory | 学习世界的时间动力学,预测下一步 latent | **MDN-RNN**(混合密度网络 + LSTM) | ~400K |
| **C** — Controller | 根据 V 和 M 的信息选动作 | **单层线性网络** | ~1K |

<p align="center">
  <img src="asset/world-models-2018/world_model_schematic.png" width="600"/><br/>
  <i>Agent 内部数据流:观察 → z → action,h 在 M 内部循环</i>
</p>

🔑 **关键洞察**:把"感知"和"记忆"做成大模型,把"决策"做得**极小**。决策器小到可以用**进化算法(CMA-ES)** 而不是反向传播来优化。

#### 各模块拆解

**V:VAE 压缩视觉**

<p align="center">
  <img src="asset/world-models-2018/vae.png" width="600"/><br/>
  <i>VAE 流程:图像 → encoder → latent z → decoder → 重建图像</i>
</p>

- 输入 64×64×3 游戏画面 → 输出 **32 维 latent `z`**
- 用随机策略采集帧,自监督训练(标准 VAE:重建 + KL)

**M:MDN-RNN 学习动力学**

<p align="center">
  <img src="asset/world-models-2018/mdn_rnn_new.png" width="600"/><br/>
  <i>MDN-RNN:LSTM 输出高斯混合分布的参数,采样得到下一步 z</i>
</p>

**M 的一次前向计算**:
```
输入:  (z_t, a_t, h_t)        ← 当前 latent + 动作 + 上一时刻 LSTM 隐藏状态
输出:
  ① (π, μ, σ)                 ← z_{t+1} 的高斯混合分布参数(MDN 部分)
                                 采样后得到下一帧 latent:z_{t+1} ~ Σ π_k · N(μ_k, σ_k²)
  ② h_{t+1}                   ← 新的 LSTM 隐藏状态(下一步用)
  ③ done_logit                ← 是否结束的概率(sigmoid 后)
```

- 为什么是分布?真实世界不可完全预测,用 **MDN(高斯混合)** 捕获多模态不确定性
- **温度 τ** 控制采样随机性:τ 越高梦境越混乱,τ 越低越确定
- 同样的 MDN-RNN 思路也用于 SketchRNN(预测下一笔笔画):

  <img src="asset/world-models-2018/mp4_sketch_rnn_insect.gif" width="500"/>

> 💡 **z 和 h 的关系澄清**:World Models 这里 **z 和 h 是「主从分离」关系** —— z 是 VAE 独立预训练的输出(只学视觉重建),h 只是 MDN-RNN 内部的「工作记忆」,辅助预测下一步 z。Controller 可选择只用 z、或用 [z, h](论文消融:CarRacing 上 [z, h] 提分 40%)。这与后来 PlaNet 的 **RSSM 双路 state**(联合训练、z 同时学视觉+动力学、(h, z) 共同构成统一环境状态)是**不同的设计哲学** —— 详见 §4.2 对比表。

**C:超小 Controller**
```python
a_t = W_c · [z_t, h_t] + b_c    # 就一个线性层
```
- 用 **CMA-ES** 黑盒优化几百个参数,无需反向传播
- 哲学意义:**复杂认知交给世界模型,决策本身可以很简单**(像人开车)

<p align="center">
  <img src="asset/world-models-2018/mccloud_baseball.jpeg" width="600"/><br/>
  <i>类比:棒球击球手凭"内部预测模型"在毫秒内反应,而不是显式规划</i>
</p>

#### 训练流程(三阶段,完全解耦)

World Models 用一个**分阶段、不端到端**的训练流程,每个阶段单独训完才进下一阶段。

**🗺️ 三阶段速览**(含核心公式):

**阶段 1**:随机动作收集 10000 局回放数据

<p align="center"><img src="asset/formulas/f01.png" alt="formula"/></p>

**阶段 2(a)**:训 VAE(只看图像)→ V

<p align="center"><img src="asset/formulas/f02.png" alt="formula"/></p>

**阶段 2(b)**:训 MDN-RNN(看 z 和 a 的序列)→ M

<p align="center"><img src="asset/formulas/f03.png" alt="formula"/></p>

**阶段 3**:冻结 V 和 M,CMA-ES 训 Controller

<p align="center"><img src="asset/formulas/f04.png" alt="formula"/></p>

**阶段 4**(部署 / 推理):把训好的 C 放回真实环境

<p align="center"><img src="asset/formulas/f05.png" alt="formula"/></p>

下面逐阶段详细解释。

##### 阶段 1:用随机策略收集真实数据

**🎯 目的**:让世界模型见过尽可能多样的状态(包括死亡、碰撞等边角情况),所以**用随机策略**而不是强策略。

**核心公式**:
<p align="center"><img src="asset/formulas/f06.png" alt="formula"/></p>

即:在真实环境中按均匀随机策略采样,收集 (观察, 动作) 序列。

**具体代码**:
```python
data = []
for episode in range(10000):
    obs = env.reset()
    done = False
    while not done:
        a = env.action_space.sample()    # 随机动作
        obs_next, reward, done = env.step(a)
        data.append((obs, a))            # 只存观察和动作
        obs = obs_next
```

- **规模**:VizDoom 收集 ~10000 局,每局几百帧 → 总共几百万帧
- **存储**:VAE 训练只需要 `obs`,M 训练需要 `(obs, a)` 序列
- **不需要 reward**:阶段 1 完全不依赖奖励信号(这是 World Models 范式的灵活性)

##### 阶段 2(a):训 VAE → 得到 V

**🎯 目的**:学一个**压缩-重建**模型,把 64×64×3 像素压成 32 维 latent z,作为后续 M 和 C 的输入特征。

**核心公式**(VAE ELBO):
<p align="center"><img src="asset/formulas/f07.png" alt="formula"/></p>

- 编码器:`q(z|o) = N(μ_φ(o), σ_φ(o)²)` —— 把图像编码成高斯分布
- 解码器:`p(o|z)` —— 从 z 重建图像
- **结果**:`encode: o → z`(32 维) + `decode: z → o`

**具体代码**:
```python
for epoch in range(N):
    for batch in shuffle(data):
        obs = batch.obs                  # 64×64×3 像素
        mu, sigma = VAE.encoder(obs)     # 输出 latent 分布参数
        z = mu + sigma * randn()         # reparameterization
        obs_recon = VAE.decoder(z)       # 重建图像

        loss = MSE(obs_recon, obs) + KL(mu, sigma)
        loss.backward()
```

- **单纯无监督** —— 只看 obs,完全不看 action / reward
- **冻结 V** —— 下阶段不再更新

##### 阶段 2(b):训 MDN-RNN → 得到 M

**🎯 目的**:学一个**时序预测**模型,让 M 能根据 `(当前 z, 当前动作, 历史记忆 h)` 预测**下一个 z 的概率分布**以及是否结束。

**核心公式**:
<p align="center"><img src="asset/formulas/f08.png" alt="formula"/></p>

其中 z 的预测分布是 K 个高斯的混合:
<p align="center"><img src="asset/formulas/f09.png" alt="formula"/></p>

- LSTM 输出 `(π, μ, σ)` 作为混合分布参数
- 训练目标:让真实的 `z_{t+1}` 在这个分布下概率最大

**具体代码**:
```python
# 先用 V 把所有 obs 编码成 z 序列
for episode in data:
    z_seq = [VAE.encode(obs) for obs in episode.obs]
    a_seq = episode.actions

for epoch in range(N):
    for (z_seq, a_seq) in episodes:
        h = zeros(256)
        for t in range(len(z_seq) - 1):
            (π, μ, σ), h, done_logit = M(z_seq[t], a_seq[t], h)
            loss_z = -log_mixture_gaussian(z_seq[t+1], π, μ, σ)
            loss_done = BCE(done_logit, real_done[t])
            loss = loss_z + loss_done
            loss.backward()
```

- **冻结 M** —— 下阶段不再更新

##### 阶段 3:用 CMA-ES 在梦境里训 C

**🎯 目的**:让 Controller 学会"在梦里能拿高分"的策略 —— 完全不碰真实环境,只用 V+M 构成的虚拟世界来训。这是 **VizDoom Take Cover** 的做法(CarRacing 用真实环境训,见下文)。

**核心公式**:
<p align="center"><img src="asset/formulas/f10.png" alt="formula"/></p>

- 目标:找到使**梦境累积奖励**最大的 Controller 参数
- `r_t = +1`(每存活一帧,VizDoom 的奖励规则)
- 用 **CMA-ES**(无梯度黑盒优化)而非反向传播

**梦境 rollout 函数**:
```python
def dream_rollout(controller_params):
    """完全在 M 里跑一局,返回 fitness"""
    z = sample_initial_z()           # 从真实数据里抽一个起点 z
    h = rnn.initial_state()
    cumulative_reward = 0
    while True:
        a = C_apply(controller_params, [z, h])         # ← 用候选参数算动作
        (π, μ, σ), h, done_logit = M(z, a, h)           # ← M 当虚拟环境
        z = sample_mdn(π, μ, σ, temperature=1.15)       # ← 温度防作弊
        if sigmoid(done_logit) > random():
            break
        cumulative_reward += 1                          # 活一帧 +1
    return cumulative_reward
```

**CMA-ES 进化优化循环**:
```python
es = CMAES(initial_mean=zeros(C.param_count), sigma=0.1)
for generation in range(800):
    # 1. CMA-ES 生成一批候选参数(population_size=64)
    candidates = es.ask()
    # 2. 每个候选都跑 N 次梦境,平均 fitness
    fitnesses = [
        mean([dream_rollout(c) for _ in range(16)])
        for c in candidates
    ]
    # 3. 把 fitness 反馈给 CMA-ES,它会更新分布
    es.tell(candidates, fitnesses)

best_C = es.best_solution()           # 训好的 Controller
```

- **无梯度**:CMA-ES 是黑盒优化,只看 fitness 不看梯度
- **并行友好**:64 个候选可同时跑梦境(GPU batch)
- **多次评估**:每个候选 rollout 16 次取均值,降低梦境随机性带来的噪声

<details>
<summary><b>📌 概念补充:CMA-ES 详解 + 为什么不用反向传播 / Bellman?</b></summary>

**CMA-ES** = Covariance Matrix Adaptation Evolution Strategy(协方差矩阵自适应进化策略),Nikolaus Hansen 1996 年提出,是**黑盒连续优化**最成功的进化算法之一。

> ⚠️ **符号约定**:标准 CMA-ES 文献用 **C** 表示协方差矩阵,但 World Models 论文里 **C** 已经被用作 **Controller** 的代号。为避免混淆,本节用 **Σ**(标准统计学符号)表示协方差矩阵。所以"Controller C"和"协方差 Σ"是两个完全不同的对象。

---

### Part 1:CMA-ES 是什么 —— 三句话原理

1. **维护一个多元高斯分布** $\mathcal{N}(m, \sigma^2 \Sigma)$ 描述「当前估计的最优解可能位置」
2. **每一代撒 λ 个候选,选最好的 μ 个**(μ ≈ λ/2)
3. **更新均值 m、协方差 Σ、步长 σ**,让分布慢慢"瞄准"最优区域

**比喻 —— 蒙眼找山顶**:撒一群人到当前位置周围 → 让他们汇报海拔 → 看最高的几个人在哪个方向 → 集体往那边移动 → 同时调整撒人的形状(椭球)和范围(步长)。

#### 🖼️ 直观看一眼:CMA-ES 怎么收敛?

<p align="center">
  <img src="asset/cma-es/02_generations_evolution.png" width="900"/><br/>
  <i>CMA-ES 在 2D 目标函数 f(x,y) = −((x−3)² + 5(y+1)²) 上的进化过程。绿色三角是真实最优 (3, −1),红星是当前均值 m,红色椭圆是当前 N(m, σ²C) 的 2σ 范围,白点是采样的候选,黄色圈是选出来的 top-μ。20 代就稳稳收敛到最优。</i>
</p>

注意观察:
- **第 0 代**:m 在 (0, 0),椭圆是圆(C = I),范围大
- **第 3 代**:m 已经被往右下方向"拖"走(top-μ 都在那边),椭圆开始变扁
- **第 8 代**:m 接近真实最优,椭圆继续缩小、变成扁长形(因为 y 方向梯度更陡)
- **第 20 代**:几乎完美收敛

#### 每代 5 步循环

<p align="center">
  <img src="asset/cma-es/03_5step_loop.png" width="900"/><br/>
  <i>CMA-ES 每代的 5 步流程图</i>
</p>

```
① 采样:x_i = m + σ·B·D·z_i,  z_i ~ N(0, I)
② 评估:计算 f(x_i)
③ 排序:按 fitness 排,取前 μ 个
④ 更新均值:m_new = Σ w_i · x_i
⑤ 更新协方差 Σ 和步长 σ(看进化路径)
```

关键超参:**λ** (population) = 16~64,**μ** = λ/2,**σ** 初始 = 0.1,代数 = 几百到几千。

#### 🔍 步骤①里的 B 和 D 是什么?

$B$ 和 $D$ 是协方差矩阵 $\Sigma$ 的**特征分解**:
<p align="center"><img src="asset/formulas/f12.png" alt="formula"/></p>

- **B**:正交矩阵(Σ 的特征向量) —— 几何上是**旋转**,把标准坐标轴转到 Σ 椭球的主轴方向
- **D**:对角矩阵(Σ 特征值的平方根) —— 几何上是**沿坐标轴方向缩放**

**为什么要拆 Σ 成 B·D²·Bᵀ?** 因为计算机只能生成标准正态噪声 $z \sim \mathcal{N}(0, I)$,需要将其变换成符合 $\mathcal{N}(m, \sigma^2 \Sigma)$ 分布的样本。下图把整个过程拆成 4 步直观展示:

<p align="center">
  <img src="asset/cma-es/01_BD_decomposition.png" width="900"/><br/>
  <i>采样公式 x = m + σ·B·D·z 的几何分解:① 从标准球形噪声 z 出发 → ② D 沿坐标轴拉伸成椭球 → ③ B 旋转到 Σ 的主轴方向 → ④ σ 放大并平移到 m 位置。蓝点是 200 个采样,红色椭圆是 2σ 范围。</i>
</p>

**小贴士**:每代只在 Σ 更新后重新算一次 B 和 D(`eigendecompose(Σ)`),然后这一代的 λ 次采样全部复用,计算上很划算。

#### 协方差 Σ 的自适应(CMA 的灵魂)

> ⚠️ **先澄清一个常见混淆**:本小节讲的是「**如何更新 Σ**」,与前面「`Σ = B·D²·Bᵀ` 特征分解」是**两个不同的步骤**:
> - **采样阶段**(每代步骤 ①②):从 Σ 中提取 B、D,用 `x = m + σ·B·D·z` 生成候选
> - **更新阶段**(每代步骤 ⑤,即本节):用本代的反馈信息**修改 Σ 本身**
> - 两步前后衔接:先用旧 Σ 的 B、D 采样 → 评估 → 再更新 Σ → 下一代再分解新 Σ

CMA-ES 不是凭空更新 Σ,而是收集**两种独立证据**,合并后小幅度调整 Σ。

##### 信号 1:Rank-μ Update —— "本代选优集中在哪个方向?"

**直觉**:观察本代选出的 μ 个最优候选,它们集中在哪个方向?Σ 就在那个方向加粗。

**数学**:
<p align="center"><img src="asset/cma-es/06_rank_mu_formula.png" alt="rank-mu" width="450"/></p>

- $x_i$:第 i 个最优候选
- $(x_i - m)(x_i - m)^\top$:**外积**,把方向变成矩阵
- $w_i$:排名权重(top 1 权重最大,递减)

##### 信号 2:Rank-1 Update —— "历代均值在往哪走?"

**直觉**:不只看本代,还要看**历代均值移动的累积方向**(进化路径 $p_c$)。如果连续几代都往同一方向走,这就是个强信号 → 沿这个长期方向加强 Σ。

**数学** —— 先维护进化路径(指数滑动平均):
<p align="center"><img src="asset/cma-es/07_pc_formula.png" alt="pc-update" width="500"/></p>

再取它的外积作为 C 的贡献:
<p align="center"><img src="asset/cma-es/08_rank1_formula.png" alt="rank-1" width="280"/></p>

##### 两个信号互补

| 信号 | 优点 | 缺点 |
|------|------|------|
| **Rank-μ** | 用 μ 个样本,**信息量大、宽度好** | 单代噪声大,容易跟着随机走 |
| **Rank-1** | **历代累积、稳定平滑** | 只用 1 个方向(进化路径),宽度信息少 |

→ **合并起来**:Rank-μ 给"宽度",Rank-1 给"长期方向稳定性",互补。

##### 🖼️ 两个信号的几何含义图

<p align="center">
  <img src="asset/cma-es/04_rank_mu_rank_1.png" width="900"/><br/>
  <i>① 左:Rank-μ 用 top-μ 候选(黄圈)的样本协方差构造一个椭圆(蓝色),把 Σ 朝那个集中方向加粗;② 中:Rank-1 累积历代均值 m₀ → m₅ 的移动方向得到进化路径 p_c(红色粗箭头),其外积给出沿该方向的"杆状"贡献;③ 右:新 Σ(粗绿)= 旧 Σ(虚线) + Rank-μ 蓝色虚线 + Rank-1 红色点划线,三者加权融合。</i>
</p>

##### 合并后的完整 Σ 更新公式

<p align="center"><img src="asset/formulas/f13.png" alt="Σ update formula"/></p>

- 第一项 $(1 - c_1 - c_\mu) \Sigma$:**保留旧 Σ 的大部分**(防止剧烈震荡)
- 第二项 $c_1 \cdot p_c p_c^\top$:Rank-1 贡献
- 第三项 $c_\mu \cdot \sum w_i (x_i - m)(x_i - m)^\top$:Rank-μ 贡献
- $c_1, c_\mu$ 是小权重(典型 0.01 量级),保证三者加和仍是正定矩阵

##### 🖼️ 完整每代 6 步流程图

把"采样 + 更新"两个阶段串起来看,CMA-ES 每代实际有 6 步(前面的 5 步图是简化版,这里给出完整版):

<p align="center">
  <img src="asset/cma-es/05_6step_loop.png" width="950"/><br/>
  <i>每代完整流程:① 特征分解 Σ → 得到 B, D ② 用 B, D 采样 λ 个候选 ③ 评估并排序 ④ 更新均值 m 和进化路径 p_c ⑤ 用 Rank-μ + Rank-1 更新 Σ ⑥ 更新全局步长 σ。下一代回到 ① 用新 Σ 再分解。</i>
</p>

**关键洞察**:**「采样的 B, D」和「更新的 Σ」是同一个矩阵的两面**——更新阶段调整 Σ 本身,下一代的采样阶段再从新 Σ 提取 B、D 给候选生成用。`Σ = B·D²·Bᵀ` 是"翻译工具",`Σ ← ...` 才是"学习行为"。

---

### Part 2:为什么 World Models 选 CMA-ES?(常见误解先澄清)

#### ⚠️ 误解:"梦境不可微"

严格说,**梦境数学上完全可以做成可微的**:

| 组件 | 可微性 |
|------|-------|
| C(线性 Controller) | ✅ 可微 |
| M 的 LSTM 部分 | ✅ 可微 |
| MDN 输出层(MLP) | ✅ 可微 |
| **从 MDN 采样 z** | ⚠️ 默认不可微,**用 reparameterization 可可微**(VAE 已证明) |
| **done 采样** | ⚠️ Bernoulli 默认不可微,**Gumbel-Softmax 可可微** |

**结论**:Ha 2018 选 CMA-ES **不是因为不能可微,而是工程权衡** —— 选择 CMA-ES 自然就不需要让链路可微。

#### ✅ 真实原因:5 个条件完美契合 CMA-ES

| 条件 | World Models 阶段 3 的实际情况 | 这意味着… |
|------|------------------------------|----------|
| **C 的参数量** | 极小(几百到几千) | 100 维以下,黑盒搜索就够,梯度优势不明显 |
| **梦境随机性** | MDN sample + τ=1.15,fitness 噪声大 | 梯度算法被噪声坑,进化算法天然抗噪 |
| **Model exploitation** | C 会找梦境 bug 钻空子 | **梯度会"放大"作弊**(直接告诉 C 怎么钻漏洞最优) |
| **长序列 RNN 梯度** | 一局可能几百帧 | 梯度爆炸/消失,LSTM 也只能缓解 |
| **工程简单度** | 2018 年的目标是"先 demo 可行性" | CMA-ES 几行代码搞定 |

→ **这才是 Ha 2018 选 CMA-ES 的真实动机**,不是技术限制。

---

### Part 3:那能用 Bellman equation 反向求解吗?

这里有个常见混淆需要先澄清:

#### ⚠️ Bellman 方程是 Q-learning 工具,不是 actor 的工具

```
Bellman:Q(s,a) = r + γ · max_{a'} Q(s', a')
```

它用来**学 value 函数 Q**,不是直接学 policy。具体怎么用:

| 算法 | 用 Bellman 做什么 |
|------|------------------|
| **DQN**(model-free) | 用 Bellman 误差当 Q 网络的损失,argmax Q 选动作 |
| **MuZero**(model-based) | 用 Bellman 训 Q,policy 用 MCTS 搜出来 |
| **Dreamer V1/V2/V3** | ⭐ **不用 Bellman**,用 λ-return 直接拟合 critic + 解析梯度反传 actor |

#### 如果硬要在 World Models 用 Bellman 思路会怎样?

**方案 A:把 C 改成 Q 网络**
- 变成 "model-based DQN":学 $Q(z, h, a)$,argmax 选动作
- 但 CarRacing 是**连续动作** → `max Q(s', a')` 难算
- 而且训练目标是 fitting Q,不直接最大化 reward,**多了一层间接性**

**方案 B:让梦境可微 + actor 直接最大化想象 return** ← Dreamer 走的路
- 不用 Bellman,**直接对 actor 求 ∂Return/∂θ_actor 反传**
- 这才是更现代、更高效的做法

→ **方案 B 的思路**(让梦境可微+反传)正是 Dreamer 2020 实现的路径。

---

### Part 4:Dreamer 怎么实现"可微梦境 + 反传"(后续演化)

```
World Models (2018)               Dreamer V1 (2020)
─────────────────────             ──────────────────
V (VAE) + M (MDN-RNN) 分阶段训 →  V + M 合并成 RSSM,端到端
C 极小 + CMA-ES                →  actor + critic(各几十万参数)
梦境不刻意可微                  →  ⭐ 让梦境完全可微 + 反向传播
没有 critic                    →  ⭐ critic 拟合 λ-return,做 actor target
```

**Dreamer V1 的核心训练循环**:
```python
# 在梦里 rollout(H=15 步)
s = sample_initial_state()
returns = 0
for t in range(H):
    a = actor(s)                            # actor 网络出动作
    s_next = world_model.transition(s, a)   # ✅ 可微的转移
    r = world_model.reward(s_next)          # ✅ 可微的奖励
    returns += γ**t * r
returns += γ**H * critic(s_H)               # critic 估计后续残值

# ⭐ 直接对 actor 反传(无 Bellman,无 sampling 估计)
actor_loss = -returns.mean()
actor_loss.backward()
```

关键差异:**没用 Bellman 误差**,而是 **解析梯度 ∂Return/∂θ_actor** 直接最大化想象 return。

---

### Part 5:CMA-ES vs 反向传播(总结对比)

| 维度 | CMA-ES(World Models) | 反向传播(Dreamer) |
|------|---------------------|------------------|
| 是否需要梯度 | ❌ 不需要 | ✅ 必须可微 |
| 适合参数量 | 几百 ~ 几千 | 任意大(亿级) |
| 信息利用率 | 每代 λ × M 次评估 | 一次前向+反传得到全梯度 |
| 收敛速度 | 慢 | 快(梯度信息密集) |
| 鲁棒性(噪声) | 强(选优而非平均) | 弱(噪声直接进梯度) |
| model exploitation 风险 | 中(只看 fitness) | 高(梯度直接钻漏洞) |
| 适合场景 | 小网络黑盒 | 大网络可微 |

**2018 → 2020 的转折点**:Dreamer 把链路做可微 + actor 参数变大 → 反向传播效率远超 CMA-ES → **CMA-ES 在 model-based RL 退出历史舞台**。

---

### Part 6:实践入口

```python
pip install cma
import cma

def rosenbrock(x):
    return sum(100*(x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x)-1))

es = cma.CMAEvolutionStrategy(x0=[0.0]*10, sigma0=0.5, inopts={'popsize': 30})
es.optimize(rosenbrock)
print(es.result.xbest)
```

或用 Ha 自己的 [**estool**](https://github.com/hardmaru/estool) —— World Models 论文的官方进化工具,含 CMA-ES、OpenAI ES、PEPG 等。

**推荐资源**:
- [pycma 官方文档](https://github.com/CMA-ES/pycma) — 含可视化、教程
- [Hansen — CMA-ES Tutorial](https://arxiv.org/abs/1604.00772) — 原作者写,必读
- [David Ha — Visual Guide to Evolution Strategies](https://blog.otoro.net/2017/10/29/visual-evolution-strategies/) ⭐ — 极美的可视化讲解
- [OpenAI ES 论文(Salimans 2017)](https://arxiv.org/abs/1703.03864) — ES 在 Atari 大规模实验

---

### 🎯 整体总结

> **梦境技术上完全可微,但 Ha 2018 选 CMA-ES 是工程权衡:Controller 极小、梦境噪声大、model exploitation 怕被梯度放大、长 RNN 梯度难、demo 优先。Bellman 方程是 Q-learning 工具,不是 actor 优化的最佳选择;真正"可微梦境+反传 actor"的范式由 Dreamer 2020 实现,从此 CMA-ES 在 model-based RL 退场。「用梯度求解」的直觉,正是 Dreamer 系的核心思路 —— 不过用的是 policy gradient 而非 Bellman。**

</details>

##### 阶段 4:部署 / 推理(在真实环境验证)

**🎯 目的**:把训好的 C 拿到真实环境跑,看是否能迁移成功。此阶段**V 和 M 不再更新,但继续在线使用**(V 提供感知压缩,M 提供时序记忆 h)。

**核心公式**:
<p align="center"><img src="asset/formulas/f11.png" alt="formula"/></p>

- 注意:**用真实 $z_t$** 更新 $h$(不是用 M sample 的 $\hat{z}$)
- 这相当于 M 在真实环境里"陪跑",维护对未来的预期

**具体代码**(论文 Algorithm 1):
```python
def rollout(controller):
    """在真实环境跑一局,既用于评估,也用于实际部署"""
    obs = env.reset()                      # ← 真实环境!
    h = rnn.initial_state()
    done = False
    cumulative_reward = 0
    while not done:
        z = vae.encode(obs)                # 真实 obs → z
        a = controller.action([z, h])      # C 决策
        obs, reward, done = env.step(a)    # 真实环境推进
        cumulative_reward += reward
        h = rnn.forward([a, z, h])         # ⭐ 用真实 z 更新 h
                                           # (而不是用 M sample 的 ẑ)
    return cumulative_reward
```

**两个关键细节**:
1. **`obs` 来自真实环境**(`env.step` 而非 `M(...)`)—— Controller 部署时见到的是真实游戏
2. **`h` 仍由 M 维护**,但输入用**真实 z**(不是 sample 的 ẑ)
   - C 接收 `[真实 z, M 陪跑的 h]`,等于既感知当下又有"记忆/预期"

**梦境 rollout vs 真实 rollout 对比**:

| 步骤 | 梦境 rollout(训练 C 时) | 真实 rollout(部署 / CarRacing 训练时) |
|------|------------------------|--------------------------------------|
| obs 从哪来 | 不需要 obs,直接操作 z | `env.reset()` / `env.step()` |
| z 从哪来 | `sample_mdn(M 输出)`(虚拟) | `vae.encode(real_obs)`(真实) |
| h 更新 | M 的 LSTM 内部更新 | `rnn.forward([a, z, h])` 同样的 M |
| reward | done_logit 推出 +1 | `env.step` 返回 |
| 用途 | CMA-ES 进化 fitness | 评估 / 实际玩游戏 |

✨ **关键洞察**:V 和 M 在部署时**继续被使用**,不是仅训练辅助 —— 它们在推理时承担"感知压缩 + 时序记忆"两项工作,让小小的 C 也能做出好决策。

##### CarRacing 的特例:在真实环境训 C

CarRacing 因为奖励复杂,**没在梦里训 Controller**:

```python
# 直接用同一个 rollout() 函数评估 fitness
# 唯一区别:env 是真实 CarRacing 环境
es = CMAES(...)
for gen in range(N):
    candidates = es.ask()
    fitnesses = [rollout(C_apply(c)) for c in candidates]   # 用真实 env!
    es.tell(candidates, fitnesses)
```

- V 和 M 还是在阶段 2 训好(用 random rollout 数据)
- 但 C 直接在真实 CarRacing 里训,只是把 `[z, h]` 当 C 的输入(比只用 z 提分 40%)

##### 三阶段独立训练的优劣

✅ **优点**:
- 简单清晰,每阶段可单独 debug
- V 和 M 用无标签数据训练,大幅降低对真实环境交互的需求
- C 极小(几百参数),CMA-ES 可解,**无需反向传播**

❌ **缺点**(后来被 Dreamer 解决):
- V 学的特征**不一定对决策最优**(只为重建 obs)
- 三阶段独立 → 不能联合优化
- 阶段 1 的 random rollout 数据**覆盖不到关键状态**(论文 Section 5 提到的迭代训练问题)

→ 这些缺陷直接催生了 **PlaNet 的端到端训练** 和 **Dreamer 的 imagination + 反向传播** 路线。

✨ 三个模块独立训练,互不依赖梯度 —— 2018 年的清流。

### 🧪 关键实验

#### 在梦里学会玩 Doom

**CarRacing-v0**:第一个解决该任务的方法(score > 900,此前最佳 ~600)。

🎬 **CarRacing 演示视频**:

<img src="asset/world-models-2018/mp4_carracing_z_only.gif" width="600"/>

**VizDoom: Take Cover —— 论文灵魂**:让 Agent **完全在 M 里训练,不碰真实环境**。

🎬 **Doom 真实环境演示**:

<img src="asset/world-models-2018/mp4_doom_real.gif" width="600"/>

1. 真实环境跑 random policy 收集数据
2. 训 V 和 M
3. 把 M 当"梦境环境",Controller **从未见过真实游戏**
4. 训好的 Controller 直接部署到真实 Doom —— **能玩,通关阈值 750 帧存活**

🤯 **史上第一次清晰展示"Agent 可在自己的世界模型里学习并迁移到真实环境"** —— 这是今天 model-based RL 的核心范式。

> 💡 想看完整可交互 demo(VAE 重建、Doom 梦境实时生成)请访问官方网站:<https://worldmodels.github.io/>

**有趣的"作弊"现象**:Agent 学会利用梦境 bug(让火球凭空消失)。作者**调高 τ 让梦境更难**,逼出鲁棒策略。这预示了后来的核心难题:**model exploitation**(策略钻模型误差的空子)。

### 🔧 实现细节深入

这一节澄清三个**特别容易混淆**的工程细节,理解了它们才算真懂 World Models。

---

##### 细节 ①:World Model vs Model-Free 的真正结构差异

常见误解:"World Model 只是多了个 M 网络,Controller 接收预测的 state"。
**真相**:差异有 **4 层**,而且最关键的不是网络结构。

| 维度 | Model-Free (DQN) | World Models (Ha 2018) |
|------|------------------|----------------------|
| **① 网络模块数** | 1 个(Q 网络) | **3 个**(V + M + C) |
| **② Controller 输入** | 原始观察 $o_t$(或几帧叠加) | $[z_t, h_t]$ —— 压缩观察 + RNN 隐藏状态 |
| **③ Controller 训练数据来源** | **真实环境的 `(s, a, r, s')`** | **梦境里 M 生成的虚拟序列** ⭐ 真正的革命 |
| **④ 优化方式** | 梯度下降 + Bellman 误差 | **CMA-ES**(进化算法) |

**数据流对比**:

先看 **Q-net 的输入输出**(理解 DQN 的基础):

```mermaid
flowchart LR
    obs["obs<br/>(84×84×4 像素)"] --> Qnet["Q Network<br/>(CNN + MLP)"]
    Qnet --> Qvals["Q 值向量<br/>[q₁, q₂, ..., qₙ]"]
    Qvals --> argmax["argmax"]
    argmax --> action["action<br/>(例:FIRE)"]
```

Q-net **只学一件事** —— "在当前 obs 下,每个动作的预期总奖励"。**它从不预测下一帧画面**。

**DQN 完整数据流**:

```mermaid
flowchart TD
    Env["真实环境 Env"] -->|obs| QNet["Q Network"]
    QNet --> Qvals["[Q值 × N动作]"]
    Qvals -->|argmax| action
    action --> step["env.step(a)"]
    step -->|"obs', r, done"| Buffer["Replay Buffer<br/>存 (s, a, r, s')"]
    Buffer -->|采样 batch| Loss["TD Loss (Bellman):<br/>y = r + γ · max Q(s')<br/>L = MSE(Q(s).gather(a), y)"]
    Loss -->|backward| Update["更新 Q net 参数"]
    Update -.->|下一步| QNet
```

**特点**:**1 个网络,所有数据流经真实环境**。

**World Models 完整数据流**(4 个阶段):

```mermaid
flowchart TD
    subgraph S1["阶段 1:收集真实数据(只跑一次)"]
        Env1["真实环境"] -->|obs| Random["Random Policy"]
        Random -->|a| Step1["env.step(a)"]
        Step1 -->|"(obs, a) 序列<br/>10000 局"| Data["回放数据"]
    end

    subgraph S2["阶段 2:训世界模型(V 和 M)"]
        Data --> V["V (VAE)<br/>obs → z (32维)"]
        Data --> M["M (MDN-RNN)<br/>(z_t, a_t, h_t) →<br/>z_{t+1} 分布 + h_{t+1} + done"]
    end

    subgraph S3["阶段 3:梦境里训 Controller(完全不碰真实环境)"]
        Init["initial: z₀, h₀"] --> State["(z_t, h_t)"]
        State --> C["C(线性)<br/>a = W·[z,h] + b"]
        C -->|a_t| MDream["M (虚拟环境)<br/>输出 z', h', done"]
        MDream -->|"if done: break<br/>else: total_reward += 1"| State
        MDream -.->|fitness| CMAES["CMA-ES<br/>(进化算法)<br/>优化 C 的参数"]
    end

    subgraph S4["阶段 4:部署到真实环境验证"]
        Env4["真实环境"] -->|obs| V2["V (encode)"]
        V2 -->|"z_t"| C2["Controller"]
        V2 -->|"z_t"| M2["M (RNN)<br/>更新 h_t → h_{t+1}"]
        C2 -->|"a_t"| Env4
        C2 -->|"a_t"| M2
        M2 -.->|"h_{t+1}<br/>(下一步用)"| C2
    end

    S1 --> S2
    S2 --> S3
    S3 --> S4
```

**核心洞察**:**Controller 在哪里训(梦境 vs 真实环境)** 才是 World Model 范式的灵魂,不是"多一个 M 网络"。

---

##### 细节 ②:z、h、o 三个"状态"概念精确区分

World Models 里有三个相关但角色完全不同的向量,容易混淆:

| 符号 | 名字 | 来源 | 维度(VizDoom) | 角色 |
|------|------|------|---------------|------|
| $o_t$ | **观察**(Observation) | 真实环境给的画面 | 64×64×3 | 真实世界的可见信号 |
| $z_t$ | **Latent**(潜变量) | VAE 把 $o_t$ 压缩 | 64 | **"当前帧的压缩表示"**(空间) |
| $h_t$ | **RNN Hidden State** | M(LSTM)内部维护 | 256 | **"历史 + 未来预期"的总结**(时间) |

**关键区分**:
- $z$ ≈ 看一张照片 —— 只知道场景长什么样
- $h$ ≈ 看一段视频前 5 秒 —— 能预测下 1 秒会发生什么
- **合在一起 $(z, h)$ 才能做正确决策**

**梦境一步的完整转移**:
```
(z_t, h_t, a_t) ──[M]──► (z_{t+1}, h_{t+1})
                          │           │
                     MDN sample     LSTM 更新
```

M **同时输出两个东西**:
1. $z_{t+1}$ 的高斯混合分布(用 MDN 采样得到下一帧的压缩表示)
2. $h_{t+1}$(LSTM 内部自然更新的新记忆向量)

**论文关键消融实验**(CarRacing):

| Controller 输入 | Score |
|-----------------|---:|
| 只用 $z$ | 632 ± 251 |
| **用 $z + h$** | **906 ± 21** ⭐ |

→ 加上 $h$ 大幅提升,证明 $h$ 携带了 $z$ 没有的"动力学信息"。**这条 $(z, h)$ 双路设计直接被 Dreamer 系的 RSSM 继承**。

---

##### 细节 ③:奖励 $\hat{r}_{t+1}$ 在梦里怎么产生?

这是个**特别反直觉的点** —— 直觉上 M 应该会预测 reward,但 **World Models 2018 在 VizDoom 上根本没显式预测连续 reward**。

**VizDoom Take Cover 的实际做法**:
```python
# M 的输出
M(z_t, a_t, h_t) → (π, μ, σ), h_{t+1}, done_logit
                       ↑           ↑          ↑
                  下一个 z 的分布   隐藏状态  是否结束的概率
# 注意:没有 reward head!
```

**奖励完全由 `done` 隐式推出**(因为 Take Cover 规则极简:存活+1):
```python
total_reward = 0
while True:
    a = C([z, h])
    (π, μ, σ), h, done_logit = M(z, a, h)
    z = sample_mdn(π, μ, σ, temperature=1.15)
    if sigmoid(done_logit) > random():
        break              # 死了,停止
    total_reward += 1      # 还活着,reward 隐式 +1
```

**CarRacing 的处理方式更"妥协"**(奖励复杂,梦里训不动):
- **没在梦里训 Controller**
- 而是把 V+M 训完后,**直接在真实环境**用 CMA-ES 训 C(z+h 作为特征)

| 任务 | 在梦里训 C? | reward 怎么来? |
|------|-----------|----------------|
| **VizDoom Take Cover** | ✅ 完全梦里训 | done 推出 +1 |
| **CarRacing** | ❌ 真实环境训 | 真实环境给 |

→ **"在梦里学"这个最炫的范式,Ha 2018 只在奖励规则极简的 VizDoom 上完整 demo 过**。这是论文一个**容易被忽略的局限**。

**Dreamer 系如何升级**:加一个 **reward head**(MLP),显式预测连续 reward:

```python
# Dreamer 的 World Model 输出
RSSM(s_t, a_t) → s_{t+1}, r̂_{t+1}, done
                     ↑          ↑          ↑
                 下一状态  预测奖励   是否结束

# 训练:用真实经验监督 reward head
loss_reward = MSE(reward_head(s_pred), batch.real_reward)

# 梦里 rollout 时累加 r̂
for t in range(H=15):
    a = actor(s)
    s, r_hat, done = world_model.step(s, a)
    total_value += γ**t * r_hat   # 用 r̂ 累积 return
```

→ 这才是 Dreamer 能跑通**通用任务**(DMC、Atari、Minecraft)的关键升级:**reward 不再依赖 done 推出,而是显式建模**。

---

##### 三个细节的相互关系

```
① 结构差异 ─► Controller 在梦里训(灵魂)
                    │
                    ▼
② z + h 双路 ─► 让 Controller 看到"空间 + 时间"完整状态
                    │
                    ▼
③ 奖励处理 ─► 用 done 隐式推(VizDoom)or 显式 reward head(Dreamer)
```

理解这三层细节后,即可:
- 看懂 Dreamer 系论文里 RSSM 为什么做成 `(h, z)` 双路
- 理解为什么 Dreamer 一定要加 reward head 才能扩展到通用任务
- 不会再把"World Model"误解为"只是多个网络的 model-free"

### 💭 理解思考

#### 贡献与历史地位

✅ **贡献**
1. 第一次系统性把 World Model 范式工程化(V+M+C 解耦)
2. 第一次证明纯 latent 梦境训练的 policy 可迁移真实环境
3. 概率性世界模型(MDN)预示了今天的随机生成模型
4. 进化算法 + 神经网络的优雅组合
5. 可视化和叙事极强,让无数研究者入坑

⚠️ **局限**
1. 三阶段独立训练,V 学的特征未必对决策最优(只为重建)
2. CarRacing / Doom 较简单
3. MDN-RNN 容量有限,长程预测会漂移
4. V 一旦训完就冻结,无法在线适应

🌳 **后续影响**
- **PlaNet (2019)**:V 和 M 合并到 RSSM,端到端训练
- **Dreamer v1/v2/v3**:latent 里做 actor-critic,替代进化
- **DreamerV3**:同一套超参解 150+ 任务,Minecraft 钻石
- **DIAMOND / Genie / Sora**:M 换成 diffusion / transformer

Dreamer 系完全是这篇论文的"亲儿子"。

#### 阅读建议

1. **先看交互式网站** <https://worldmodels.github.io/>(demo 都是动的,比论文快)
2. 论文不长(~25 页),但**附录极其详细**,值得细读
3. 重点关注:VAE latent 维度对比、MDN-RNN 温度 τ 作用、"在梦里训练"方法论
4. 代码:[estool](https://github.com/hardmaru/estool) · [WorldModelsExperiments](https://github.com/hardmaru/WorldModelsExperiments)

#### 一句话总结

> **第一次把"Agent 用想象力学习"从哲学变成可复现算法。每个模块都被后人替换了,但「感知—记忆—决策」三件套范式至今统治整个 model-based RL / world model 领域。**

<details>
<summary><b>📚 学习资源(展开)</b></summary>

**🎬 视频讲解**

作者本人:
- [**David Ha — NeurIPS 2018 Talk**](https://youtu.be/HzA8LRqhujk) ⭐ — 一作亲自讲,~30 分钟,信息量最大,**强烈推荐先看**
- David Ha 还有 Stanford / 各种 workshop 的版本,YouTube 搜 "David Ha World Models" 可找到

第三方解读:
- [**Two Minute Papers — "Google's New Dreaming AI"**](https://www.youtube.com/results?search_query=two+minute+papers+world+models) — 5 分钟科普,建立直觉
- [**Arxiv Insights — World Models**](https://www.youtube.com/results?search_query=arxiv+insights+world+models) — 10 分钟左右,讲得清晰
- [**Yannic Kilcher 频道**](https://www.youtube.com/@YannicKilcher) — 搜 "World Models",论文逐句过

**📝 英文图文解读**

- [**官方交互式网站**](https://worldmodels.github.io/) ⭐ — **最佳入门资源**,demo 都是动的,比读 PDF 强 10 倍
- [**Lilian Weng — RL 综述与相关博文**(Lil'Log)](https://lilianweng.github.io/tags/reinforcement-learning/) — RL 标签页,涵盖 policy gradient、exploration、meta-RL 等;Model-Based 部分散见于综述与 [A (Long) Peek into RL](https://lilianweng.github.io/posts/2018-02-19-rl-overview/)
- [**The Gradient**](https://thegradient.pub/) — 把 World Models 放进更大的 AI 叙事

**📝 中文解读**

- **机器之心**:[搜索 "World Models 大梦想家"](https://www.jiqizhixin.com/search?keywords=World%20Models) — 当年发表时有详细中文报道
- **PaperWeekly**:微信号 paperweekly,搜 "World Models" 论文导读
- **知乎**:
  - 搜索 "World Models Ha Schmidhuber" — 多篇高赞解读
  - 搜 "在梦中学习" / "世界模型 综述" 也能找到不错的笔记
- **B 站**:搜 "World Models 论文精读"、"李沐 强化学习" 系列也有相关内容
- **CSDN / 简书**:论文笔记很多,质量参差,挑收藏数 > 100 的看

**💻 代码与复现**

- [**hardmaru/WorldModelsExperiments**](https://github.com/hardmaru/WorldModelsExperiments) — 作者官方实现(TensorFlow,完整但较老)
- [**hardmaru/estool**](https://github.com/hardmaru/estool) — CMA-ES 实现(Controller 训练用)
- [**ctallec/world-models**](https://github.com/ctallec/world-models) ⭐ — **PyTorch 复现**,代码干净,推荐学习用
- [**zacwellmer/WorldModels**](https://github.com/zacwellmer/WorldModels) — 另一个简洁 PyTorch 版本

**🎓 课程**

- [**UC Berkeley CS 285: Deep RL**](https://rail.eecs.berkeley.edu/deeprlcourse/) — Sergey Levine,model-based RL 章节
- [**DeepMind x UCL RL Course**](https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021) — model-based RL 专题
- [**Stanford CS 234: RL**](https://web.stanford.edu/class/cs234/)

**📚 延伸阅读**

前传(Schmidhuber 1990s 的思想源头):
- [Schmidhuber 1990 — *Making the World Differentiable*](http://people.idsia.ch/~juergen/FKI-126-90ocr.pdf)
- [Schmidhuber 1991 — *Curious Model-Building Control Systems*](http://people.idsia.ch/~juergen/curiositysab/curiositysab.html)

后续(读完 World Models 后立刻读):
- [PlaNet](https://arxiv.org/abs/1811.04551) — 端到端版本
- [DreamerV3](https://arxiv.org/abs/2301.04104) — 集大成者

**🎯 推荐学习顺序**

```
1. 先逛 worldmodels.github.io           (1 小时,体感)
2. 看 David Ha NeurIPS 2018 talk        (30 分钟,作者视角)
3. 读 Lil'Log [RL Overview](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) (1 小时,数学梳理)
4. 跑一遍 ctallec/world-models 代码     (半天到一天,动手)
5. 通读论文 + 附录                       (1 天,细节)
6. 跳到 PlaNet / DreamerV3              (理解演化)
```

</details>

> 📁 配套素材已下载到 `asset/world-models-2018/`(架构图、VAE/MDN-RNN 示意图、CarRacing & Doom 演示视频)。图片来源:[worldmodels.github.io](https://worldmodels.github.io/),© Ha & Schmidhuber, 2018,仅作学习参考。


</details>

<details>
<summary><b>4.2 PlaNet (2019)</b></summary>

> **论文**:[arxiv.org/abs/1811.04551](https://arxiv.org/abs/1811.04551)(Hafner et al., ICML 2019)
> **代码**:<https://github.com/google-research/planet> · **项目页**:<https://planetrl.github.io/>
>
> **TL;DR**:**学一个端到端的 latent 世界模型(RSSM),用 CEM 在 latent 空间「想象」未来的 rollouts 来选择动作**。把 World Models 的「分阶段」打通成「端到端」,样本效率比 model-free 高 50 倍。

这篇论文是 Dreamer 系列的**直接前身**,Hafner 第一篇 model-based RL 工作。RSSM 双路 latent 架构在这里诞生,至今(2026)仍是 model-based RL 的标准。

<p align="center">
  <img src="asset/planet-2019/combined.gif" width="500"/><br/>
  <i>PlaNet 在 DeepMind Control Suite 上的实际表现(6 个连续控制任务,从像素输入直接学控制)</i>
</p>

### 📖 核心思想

#### 解决 World Models 的核心痛点

| World Models 的痛点 / 局限 | PlaNet 的回应 |
|--------------------|--------------|
| 形式化模糊,只隐式处理部分可观测性 | 显式建模为 **POMDP**,世界模型即学习该 POMDP 的动力学与观测函数 |
| V 和 M 分阶段独立训 → VAE 学的特征未必对决策有用 | **端到端联合训练**(encoder / transition / decoder / reward 共享一个 ELBO 损失) |
| MDN-RNN 长程不稳,确定性记忆与随机性预测未解耦 | **RSSM**:确定性 GRU(h) + 随机性高斯(z) **双路并存**,区别于纯确定性 RNN 与纯随机性 SSM |
| 仅训单步预测,多步预测误差累积无显式约束 | **Latent overshooting**:在隐空间对所有跨度的多步预测施加 KL 正则,**无需解码回图像** |
| 决策依赖 CMA-ES 进化出的 Controller,换任务需重训 | **无 Policy 网络**,直接用学到的世界模型 + **CEM 在 latent 中在线规划**(MPC) |
| 一次性随机采集数据,无法随模型改善 | **在线数据采集**:边训边用当前模型 + 规划主动探索,数据分布随模型变好而改善 |
| 只在 Doom / CarRacing 这类玩具环境 demo | **DeepMind Control Suite**(6 个连续控制任务,像素输入) |

<details>
<summary>📌 <b>为什么"显式 POMDP 形式化"是 PlaNet 在科学严谨性上的关键进步</b>(点开展开)</summary>

##### 1. 像素 RL 本质就是 POMDP

真实环境的"真实状态"是所有物体的位置、速度、质量、关节角度等;而 agent 拿到的只有 RGB 图像 —— 一帧静态图丢失了**速度、深度、遮挡背后的信息、数值精度**。所以**只要 agent 从像素学控制,问题就一定是 POMDP**,必须在内部维护一个 latent 表示来"补全"观测不到的部分。这件事是物理决定的,不是建模选择。

##### 2. 架构对照 —— World Models 的"隐式" vs PlaNet 的"显式"

| POMDP 组件(理论) | World Models(隐式 / 不完整) | PlaNet(显式 / 1:1 对应) |
|---|---|---|
| **转移 T**: p(s_t ∣ s_{t-1}, a_{t-1}) | MDN-RNN: p(z_{t+1} ∣ z_t, a_t, h_t) —— h 是旁路记忆,**"状态"到底是 z 还是 (z,h),论文从未明确** | RSSM: p(s_t ∣ s_{t-1}, a_{t-1}),其中 s_t = (h_t, z_t) —— **状态定义清晰,转移即 POMDP 的转移** |
| **观测 Z**: p(o_t ∣ s_t) | VAE Decoder: p(o_t ∣ z_t) —— **只是"给图像找压缩码"的副产品,不是 POMDP 的观测函数** | Decoder: p(o_t ∣ s_t) —— **就是 POMDP 的观测函数**,作为 ELBO 的一项被联合训 |
| **奖励 R**: r(s_t) | ❌ **不存在**。reward 由真实环境给出(CarRacing 赛道判定 / Doom 存活判定) | Reward model: r̂(s_t),小 MLP —— 因为 CEM 在脑内 rollout 不接触真环境,**必须由模型自己预测奖励** |
| **Belief**: b(s_t ∣ o_{≤t}, a_{<t}) | VAE encoder q(z ∣ o_t) **只看当前帧**,历史靠 MDN-RNN 的确定性 h 旁路;**[z,h] 从未被合成"对真实状态的概率 belief"** | Encoder/Posterior q(s_t ∣ h_t, o_t),其中 h_t 携带历史 —— **真正的 POMDP belief**:高斯分布,通过 KL 拉向 prior |
| **训练目标**: max ln p(o_{1:T}, r_{1:T} ∣ a_{1:T}) | **VAE 的 ELBO + MDN-RNN 的 NLL**,两段独立、分阶段训练 —— **从未合成"对 POMDP 联合似然的下界"** | **单一 ELBO**(对整段轨迹的对数似然下界),由变分推断从 POMDP 联合似然**自然推导**;重建 / reward / KL 在同一公式里,梯度协同 |

而且训练目标 **ELBO 不是拍脑袋拼出来的**,而是从「POMDP 是一个 latent variable model + 用变分推断学它」**自然推导**出来的(§3 那一坨公式)。每一项 loss 都有明确的数学含义,而不是经验主义的多任务加权。

##### 3. 逐组件深入:为什么是"隐式 vs 显式"

**🔹 组件 1:Transition(转移函数)**

- **World Models 的隐式表现**:MDN-RNN 用 LSTM 维持隐状态 h,转移写成 p(z_{t+1} ∣ z_t, a_t, h_t)。问题是 —— **"POMDP 的状态" 到底是什么? 论文从未给出答案**。如果状态是 z,那 h 凭什么出现在条件里?如果状态是 (z, h),那为什么 h 不参与重建、也不参与 KL?这是个**形式上不闭合**的设计。
- **PlaNet 的显式表现**:明确写下 s_t = (h_t, z_t) 是状态,转移 p(s_t ∣ s_{t-1}, a_{t-1}) 完全符合 POMDP 转移函数的定义。h_t = GRU(h_{t-1}, z_{t-1}, a_{t-1}) 是状态的确定性部分,z_t ~ N(μ(h_t), σ(h_t)) 是状态的随机部分 —— **两部分一起就是 POMDP 的状态**。

**🔹 组件 2:Observation(观测函数)**

- **World Models 的隐式表现**:VAE 解码器是**单独训练**的,目标是「把这一帧的编码 z 还原成图像」—— 这是图像压缩任务,不是 POMDP 观测函数。事实上,如果 z 缺少对动力学有用的信息(比如速度),VAE 完全不在乎,因为这不影响重建。
- **PlaNet 的显式表现**:Decoder p(o_t ∣ s_t) 是 ELBO 的一项,**与转移、reward、KL 联合训练**。如果 s_t 缺了什么信息,重建 loss 就会反向把那部分推回 s_t —— 它被「POMDP 的观测函数」这个角色驱动。

**🔹 组件 3:Reward(奖励函数)**

- **World Models 的隐式表现**:**根本没有这个组件**。reward 全程依赖真环境 —— CMA-ES 训 Controller 时把它放回 CarRacing / Doom 真环境跑、用真环境的 reward 评估。所以 World Models 的"世界模型"严格说**不完整**:只学了动力学,没学奖励。
- **PlaNet 的显式表现**:Reward model r̂(s_t) 是世界模型的一部分,和其他组件一起训。**必要性**:CEM 在 latent 里 rollout 几百条候选动作序列时完全不接触真环境,必须靠模型预测的 reward 来挑选;**附带效果**:reward loss 反向也让 encoder 把"哪些视觉特征与奖励相关"塞进 s_t,这正是 World Models 的 VAE 永远学不到的。

**🔹 组件 4:Belief 更新(后验)**

- **World Models 的隐式表现**:VAE 的 q(z ∣ o_t) **只看当前一帧**,所以它不可能是"对环境状态的 belief"—— 只是"对这一帧的编码"。历史信息走另一条路:MDN-RNN 的 h(确定性、点估计的)。**两条路从未合并成"对真实状态的一个概率分布"**。Controller 拿到的 [z, h] 只是把两条路的最新切片拼起来,既不是分布、也不是 belief。
- **PlaNet 的显式表现**:Encoder 同时吃 (h_t, o_t),输出 q(s_t ∣ h_t, o_t) = N(μ, σ²)。h_t 携带历史、o_t 是当前观测,二者一起决定"对当前隐状态的后验"。这是一个**真正的概率分布**,且通过 KL[q ∥ p] 被拉向"用动力学转移过来的预测",**强制 belief 与动力学一致** —— 这正是 POMDP belief update 的定义。

**🔹 组件 5:Training Objective(训练目标)**

- **World Models 的隐式表现**:loss = VAE 的 ELBO **+** MDN-RNN 的 NLL,**两段独立、分阶段串行训**。两个 loss 没有共同的概率根基 —— VAE 的 ELBO 是对图像 p(o) 的下界,MDN-RNN 的 NLL 是对 z 序列 p(z_{1:T} ∣ a_{1:T}) 的下界,这两个目标**从未被合成"对 POMDP 联合似然的下界"**。结果是:想加新约束就必须再拍个 loss 进来加权,**没有理论依据告诉你该加什么、权重该取多少**。
- **PlaNet 的显式表现**:loss = 对整段轨迹的 ELBO

  <p align="center"><img src="asset/formulas/f18.png" width="780"/></p>

  这**直接就是把 POMDP 当作 latent variable model 做变分推断的结果**。重建、reward、belief 对齐动力学三件事在**同一个公式里**,梯度自动协同 —— encoder 会主动把"对动力学有用"和"对预测 reward 有用"的信息都塞进 s_t。**想加新约束?** 沿着同一个变分推导继续推:**Latent Overshooting 正是这样从"单步 ELBO"自然推广到"多步 ELBO"得到的(§4)**,理论一脉相承,没有任何拍脑袋。

##### 4. 显式形式化的真正价值(不只是用词区别)

- 🎯 **Loss 有源头**:World Models = "VAE loss + MDN-RNN loss"两段独立;PlaNet = ELBO 一步推出。要加新约束(如 latent overshooting)时,可以沿着推导继续加,每一项都还有理论意义。
- 🎯 **职责可诊断**:Decoder 学坏 → 重建 loss 升;Transition 学坏 → KL 升,可定位。World Models 里 z 不好可能是 VAE 也可能是 MDN-RNN,因为职能没按 POMDP 拆开。
- 🎯 **模块松耦合,可只换一个组件**:Dreamer 1/2/3 完全复用 PlaNet 的 RSSM(POMDP 那 4 个组件不动),只把"CEM 规划"换成"Actor-Critic + 解析梯度"。这种"换决策层不换世界模型"的灵活性,没有 POMDP 形式化是做不出来的。
- 🎯 **可苹果对苹果比较**:所有 model-based RL 方法(POMCP / DVRL / SLAC / Dreamer ...)都能放在 POMDP 框架下比较 —— 你的 Z 怎么近似?belief 是什么形式?规划用什么算法?

##### 5. 一句话总结

> **World Models** 把"部分可观测"当成**需要绕过去的工程问题**(堆 VAE + RNN 凑表示)。
> **PlaNet** 把它当成**需要正面建模的科学问题**(写下 POMDP,所有架构和 loss 自然推导出来)。
>
> 同样的网络组件,前者是**工程拼装**,后者是**理论实现**。这正是 Dreamer 1/2/3 全都沿用 PlaNet 的形式化、而没人再回到 World Models 的三阶段范式的根本原因。

</details>

#### 整体架构

```mermaid
flowchart TD
    Env["真实环境"] -->|obs, action, reward| Buffer["Replay Buffer"]
    Buffer -->|训练数据| RSSM["RSSM 世界模型<br/>(Encoder + Transition + Reward + Decoder)<br/>端到端 ELBO 损失"]
    RSSM -.->|"latent rollout"| CEM["CEM 在线规划<br/>采样 1000 个动作序列<br/>选 top-100 elite,迭代 10 次"]
    CEM -->|"a_t"| Env
```

**注意**:**PlaNet 没有 actor / policy 网络** —— 每个动作都是 CEM 实时规划得出的(这是和 Dreamer 最大的区别)。

<p align="center">
  <img src="asset/planet-2019/planet_algorithm.png" width="800"/><br/>
  <i>PlaNet 算法整体流程(来自论文 Figure 2):左侧训练阶段从真实环境采数据训 RSSM(端到端 ELBO),右侧规划阶段从当前 state 出发,用 RSSM 在 latent 空间 rollout 出多个轨迹,CEM 挑选最优首步动作</i>
</p>

#### 关键创新对比

| 维度 | World Models (2018) | **PlaNet (2019)** | Dreamer (2020+) |
|------|--------------------|-----|---|
| 训练方式 | 三阶段独立 | **端到端 ELBO** | 端到端 |
| Latent 结构 | VAE 出 z + MDN-RNN 副产生 h(**分离**,分阶段训) | **(h, z) 作为统一 state**(**双路 RSSM**,联合训) | 同 PlaNet |
| z 学到什么 | 仅视觉重建(VAE 单独训) | **视觉重建 + 动力学预测**(KL 约束) | 同 PlaNet |
| 决策方式 | CMA-ES 训 Controller | **CEM 在线规划** | Actor-Critic + 解析梯度 |
| 主战场 | CarRacing / VizDoom | **DMC(6 任务)** | DMC / Atari / Minecraft |

> 💡 **注意**:World Models 的 M 内部**也有** LSTM 隐藏状态 h,但它只是"工作记忆"的副产品,与 VAE 的 z **分阶段训练、概念上分离**(z 只学重建,h 只辅助预测 z)。PlaNet 的 RSSM 才**第一次把 (h, z) 视为统一的环境状态**,联合训练,让 z 同时学到视觉和动力学信息 —— 这是 RSSM 真正的革命性所在。

### 🧪 关键实验

#### 在 DeepMind Control Suite(像素输入)击败 model-free 50×

| Algorithm | 达到固定性能所需样本数 | 类型 |
|-----------|-----------------------|------|
| A3C | 50 M 帧 | model-free |
| D4PG | 100 M 帧 | model-free SOTA |
| **PlaNet** | **2 M 帧** | **model-based** ⭐ |

→ **样本效率提升 50× 量级**,首次让 model-based RL 在像素任务上**全面碾压 model-free**。

<p align="center">
  <img src="asset/planet-2019/result_table.png" width="800"/><br/>
  <i>论文 Table 1:PlaNet 用 <b>2000 episodes</b> 达到 D4PG <b>100,000 episodes</b> 的性能,各任务样本效率提升 11×~180×</i>
</p>

#### 关键消融

**RSSM 双路的必要性**:
- 只用 deterministic h(纯 RNN)→ 表达不了不确定性,中等性能
- 只用 stochastic z(纯 VAE-RNN)→ **训不动**,长期信息被噪声冲掉
- **h + z 双路** → **最好** ⭐

<p align="center">
  <img src="asset/planet-2019/result_model.png" width="850"/><br/>
  <i>论文 Figure 5:RSSM 消融实验。<b>蓝色 = PlaNet (h+z 双路)</b>,红色 = 纯 deterministic,绿色 = 纯 stochastic。在所有 6 个任务上,纯 RNN 和纯 VAE-RNN 都明显差于双路 RSSM</i>
</p>

**Latent overshooting 的作用**:
- 只用 1 步 KL → 短程预测可以,长程严重漂移
- 加入 D=50 步 overshooting → **长程预测显著稳定**

**规划 horizon H 的影响**:
- H=1 → 退化成贪心,差
- **H=12 → 甜点** ⭐
- H=50 → 模型误差累积,反而变差

→ "**世界模型不能想太远**" 是 model-based RL 的永恒痛点。

### 🔧 实现细节深入

#### 细节 ①:RSSM 状态拆分(PlaNet 最关键贡献)

<p align="center"><img src="asset/formulas/f16.png" alt="RSSM state"/></p>

```
state s_t = (h_t, z_t)
            ↑    ↑
       确定性  随机性
       (GRU)  (高斯)
```

| 变量 | 类型 | 由谁产生 | 角色 |
|------|------|---------|------|
| `h_t` | **确定性** | GRU 的隐藏状态:`h_t = GRU(h_{t-1}, z_{t-1}, a_{t-1})` | **长期记忆**,稳定可靠 |
| `z_t` | **随机性高斯** | Encoder 或 Prior 采样 | **捕捉不确定性 / 多模态未来** |

**为什么要双路?**(关键洞察)

| 单路设计 | 问题 |
|----------|------|
| **纯确定性** | 没法表达噪声、多模态未来 |
| **纯随机** | 训练不稳,长期信息被噪声冲掉 |
| **双路 h + z** | ✅ h 保证稳定记忆,z 表达不确定性 |

→ 这是 RSSM 的**核心数学直觉**:把「过去的稳定记忆」和「未来的不确定性」分到两个变量里独立处理。

<p align="center">
  <img src="asset/planet-2019/rssm.png" width="900"/><br/>
  <i>论文 Figure 1:三种动力学模型的概率图模型对比。<b>(a) RNN</b>:只有确定性 h,没法表达不确定性;<b>(b) SSM</b>:只有随机 s,长期信息易被噪声冲掉;<b>(c) RSSM</b>:h(方块,确定性)+ s(圆圈,随机性)并存,各司其职 —— 这就是 PlaNet 的核心创新</i>
</p>

#### 细节 ②:四个子网络的角色

| 网络 | 形式 | 何时使用 |
|------|------|---------|
| **Encoder**(Posterior) | $q(z_t \mid h_t, o_t)$ | **训练时**:看到真实 obs,出后验 z |
| **Transition**(Prior) | $p(z_t \mid h_t)$ | **规划时 / 想象时**:不看 obs 也能预测 z ⭐ |
| **Reward** | $p(r_t \mid h_t, z_t)$ | 预测奖励(规划时累加 return) |
| **Decoder** | $p(o_t \mid h_t, z_t)$ | 重建 obs(**仅训练辅助**,部署不用) |

🔑 **核心机制**:**训练时用 Encoder 的后验 z(有 obs 监督),规划时用 Transition 的 prior z(没有 obs)** —— 这就是 RSSM 能"在 latent 空间想象未来"的关键。

#### 细节 ③:端到端 ELBO 损失

PlaNet 把 World Models 三阶段独立训练的 V 和 M **合并成一个目标**:

<p align="center"><img src="asset/formulas/f14.png" alt="PlaNet ELBO"/></p>

三个分量同时优化:
- **重建项**:让 decoder 能从 (h, z) 重建 obs(类似 VAE)
- **奖励项**:让 reward head 能预测真实奖励
- **KL 项**:让 posterior `q(z|h, o)` 接近 prior `p(z|h)`(VAE 风格正则)

→ 一个梯度同时优化 4 个子网络,**特征自动对决策有用**(不像 World Models 的 V 只学重建)。

#### 细节 ④:Latent Overshooting(长程稳定性技巧)

标准 ELBO 只看「单步预测」,但 PlaNet 要做 H=12 步规划 → 必须**多步预测都准**。

<p align="center"><img src="asset/formulas/f15.png" alt="latent overshooting"/></p>

直觉:
- 让「从 t 时刻 prior 预测 d 步后的 z」接近「从 t+d 时刻 posterior 编码的 z」
- 不仅单步准,**多步预测的分布也要对齐**
- `α_d` 是各步的权重(通常等权)

→ 这是 PlaNet 长程稳定性的关键。DreamerV1 简化为只用单步 KL + critic 估剩值,效果反而更好。

<p align="center">
  <img src="asset/planet-2019/latent_overshooting.png" width="900"/><br/>
  <i>论文 Figure 3:三种训练目标对比。<b>(a) 标准 ELBO</b>:只在相邻时间步约束(1-step KL);<b>(b) Observation Overshooting</b>:跨多步重建观察(代价大);<b>(c) Latent Overshooting</b> ⭐:在 latent 空间跨多步对齐 prior 和 posterior 的 KL —— 平衡了准确性和计算成本</i>
</p>

#### 细节 ⑤:CEM 在线规划(没有 actor!)

PlaNet **不学 policy 网络**,每个时间步**实时做规划**:

<p align="center"><img src="asset/formulas/f17.png" alt="CEM optimization"/></p>

```python
def plan_action(world_model, current_state):
    # 维护一个动作序列分布:每步独立高斯
    μ = zeros(H, action_dim)        # H = 12 步规划 horizon
    σ = ones(H, action_dim)

    for iteration in range(I):       # I = 10 次 CEM 迭代
        # 1. 采样 J 个候选动作序列(J = 1000)
        action_seqs = sample_normal(μ, σ, J)

        # 2. 用世界模型 rollout 每个序列,累积奖励
        returns = []
        for seq in action_seqs:
            z, h = current_state
            R = 0
            for t in range(H):
                z, h = world_model.transition(z, h, seq[t])  # 用 prior
                R += world_model.reward(z, h)
            returns.append(R)

        # 3. 选 top-K(K = 100)elite
        elite_idx = argsort(returns)[-K:]
        elite_seqs = action_seqs[elite_idx]

        # 4. 用 elite 的均值方差更新分布
        μ = elite_seqs.mean(axis=0)
        σ = elite_seqs.std(axis=0)

    return μ[0]   # 只执行第一个动作,下一步重新规划
```

**关键参数**:

| 参数 | 值 | 含义 |
|------|----|----|
| H(规划 horizon) | 12 | 想象 12 步未来 |
| J(候选序列数) | 1000 | 每代采 1000 个序列 |
| K(elite 数) | 100 | 选 top-100 |
| I(CEM 迭代次数) | 10 | 收敛迭代 10 次 |

**单步计算量**:`10 × 1000 × 12 = 12 万次 transition 前向` —— GPU 上几十毫秒可完成,但**真机机器人实时控制吃力**。这是 PlaNet 被 Dreamer 取代的核心原因之一。

<p align="center">
  <img src="asset/planet-2019/planning_in_latent_space.png" width="700"/><br/>
  <i>论文 Figure 4:CEM 在 latent 空间规划示意。从当前 state 出发,在 latent 里 rollout 多条 trajectory(各代候选动作序列),用 RSSM 预测累积奖励,选 elite 更新动作分布,迭代收敛 —— <b>全程不碰真实环境</b></i>
</p>

#### CEM vs CMA-ES(World Models 用的)

| 维度 | CMA-ES (World Models) | CEM (PlaNet) |
|------|----------------------|--------------|
| 优化对象 | **Controller 的参数 θ** | **动作序列 a_{1:H}** |
| 何时优化 | **训练时**,优化好之后部署 | **每步实时**(在线规划) |
| 协方差自适应 | 是(Σ) | 否(每步独立高斯) |
| 是否需要 actor 网络 | 是(线性 controller) | **否!** |

### 💭 理解思考

#### 贡献与历史地位

✅ **贡献**

1. **RSSM 双路 latent** —— 现代 model-based RL 的标准架构,被 Dreamer V1/V2/V3 全部继承
2. **端到端 ELBO 训世界模型** —— 替代了 World Models 的分阶段,后续无数工作沿用
3. **Latent overshooting** —— 长程稳定性技巧
4. **DMC 上 50× 样本效率** —— 首次让 model-based 在视觉控制上完胜 model-free
5. **代码开源** —— 后续 Dreamer 系的基线

⚠️ **局限**(直接催生 Dreamer)

1. **CEM 在线规划巨慢** —— 每步 12 万次前向,真机机器人实时控制吃力
2. **没法学到隐式的长期策略** —— 规划只能想 12 步,长程任务表现差
3. **只能解连续控制** —— CEM 对离散动作处理不优雅
4. **仍有 model exploitation** —— 比 World Models 用 τ 防御更弱

🌳 **后续影响**

- **DreamerV1 (2020)**:CEM → actor-critic + 解析梯度反传,**推理快几十倍 + 性能更好**
- **DreamerV2 (2021)**:RSSM 的 z 改成离散 categorical,攻克 Atari
- **DreamerV3 (2023)**:同一架构 + symlog 归一化,150+ 任务通用
- **MuZero 系**:借鉴 RSSM 思路 + MCTS 搜索
- **TWM / IRIS / DIAMOND**:RSSM 的 transformer / diffusion 变体

#### 演化脉络

```
World Models (2018)
        │ 三阶段独立 / VAE + MDN-RNN / CMA-ES
        ▼
PlaNet (2019)           ← 我们在这里
        │ 端到端 / RSSM 双路 / CEM 在线规划
        ▼
Dreamer V1 (2020)
        │ 同 RSSM / Actor-Critic 替代 CEM / 解析梯度
        ▼
Dreamer V2/V3 (2021–2023)
        │ 离散 z / symlog / 通用 150+ 任务
```

#### 阅读建议

1. **先看项目页 demo**:<https://planetrl.github.io/>(2 分钟,体感)
2. **读论文 Section 3-4**(RSSM 架构 + ELBO 损失)
3. 跳过实现细节,直接跑官方代码 cartpole-swingup(半天)
4. 想深入再读 Section 5(latent overshooting)
5. **立刻跳到 DreamerV1**(自然演化)

#### 一句话总结

> **PlaNet = 端到端的 RSSM 世界模型 + CEM 在线规划。它把 World Models 的分阶段训练打通成端到端,引入了「确定性 h + 随机性 z」双路 latent 架构(被后续所有 Dreamer 沿用),在 DMC 上首次让 model-based RL 在像素任务上 50× 完胜 model-free。但 CEM 在线规划巨慢,直接催生了 DreamerV1 用 actor-critic + 解析梯度反传取代。**

### 📚 学习资源

**🎬 视频讲解**
- [**Yannic Kilcher — PlaNet paper review**](https://www.youtube.com/results?search_query=yannic+kilcher+planet) — 论文逐句过
- [**Hafner 在 Google AI Blog 的官方介绍**](https://blog.research.google/2019/02/introducing-planet-deep-planning.html)

**💻 代码与复现**
- [**google-research/planet**](https://github.com/google-research/planet) — 官方 TensorFlow 实现
- [**Kaixhin/PlaNet**](https://github.com/Kaixhin/PlaNet) ⭐ — PyTorch 复现,推荐学习用
- [**cross32768/PlaNet_PyTorch**](https://github.com/cross32768/PlaNet_PyTorch) — 另一个 PyTorch 版本

**📝 中文解读**
- 知乎搜索 "PlaNet 解读" / "Hafner RSSM"
- PaperWeekly 微信号搜 "PlaNet"

**📚 延伸阅读**
- 前传:[World Models (2018)](https://arxiv.org/abs/1803.10122) ← 必读前置
- 后续:[DreamerV1 (2020)](https://arxiv.org/abs/1912.01603) ← 必读
- DMC 环境:[dm_control](https://github.com/google-deepmind/dm_control)

</details>

<details>
<summary><b>4.3 Dreamer v1 / v2 / v3 (2020–2023)</b></summary>

> **论文**:[DreamerV1](https://arxiv.org/abs/1912.01603) · [DreamerV2](https://arxiv.org/abs/2010.02193) · [**DreamerV3**](https://arxiv.org/abs/2301.04104)
>
> **要点**:目前 RL 派最强基线。引入「在想象里训 actor-critic + 解析梯度反传」范式。**V3 一定要读** —— 同一组超参跑通 150+ 任务,Minecraft 钻石(从零)。

_📝 详细精读待补充_

</details>

<details>
<summary><b>4.4 GAIA-1 (Wayve, 2023)</b></summary>

> **论文**:[arxiv.org/abs/2309.17080](https://arxiv.org/abs/2309.17080) · **官方 blog**:<https://wayve.ai/thinking/scaling-gaia-1/>
>
> **要点**:自动驾驶 world model。Wayve 用 GAIA 生成驾驶视频,作为 corner case 增强数据。

_📝 详细精读待补充_

</details>

<details>
<summary><b>4.5 Genie / Genie 2 (DeepMind, 2024)</b></summary>

> **论文**:[Genie](https://arxiv.org/abs/2402.15391) · **Genie 2 blog**:<https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/>
>
> **要点**:可交互生成环境。从互联网视频学到 action-conditioned 世界,无需游戏引擎即可生成可交互世界。

_📝 详细精读待补充_

</details>

<details>
<summary><b>4.6 Sora 技术报告 (OpenAI, 2024)</b></summary>

> **技术报告**:<https://openai.com/index/video-generation-models-as-world-simulators/>
>
> **要点**:把视频生成视作 world simulator 的论述。把这个概念推成顶流,资本和媒体快速跟进。

_📝 详细精读待补充_

</details>

<details>
<summary><b>4.7 V-JEPA / V-JEPA 2 (Meta / LeCun)</b></summary>

> **论文**:[V-JEPA](https://arxiv.org/abs/2404.08471) · [V-JEPA 2 官方页](https://ai.meta.com/vjepa/) · [I-JEPA](https://arxiv.org/abs/2301.08243)
>
> **要点**:非生成式、predictive embedding 路线。LeCun 力推的「反 Sora」方案 —— 不预测像素,只预测抽象表征。

_📝 详细精读待补充_

</details>

<details>
<summary><b>4.8 其他值得关注</b></summary>

- [**1X World Model**](https://www.1x.tech/discover/1x-world-model)(人形机器人,1X Technologies)
- [**Oasis**](https://oasis-model.github.io/)(Decart,实时 Minecraft 生成)
- [**DIAMOND**](https://arxiv.org/abs/2405.12399)(NeurIPS 2024,[代码](https://github.com/eloialonso/diamond)) — Atari 视觉效果惊艳,代码干净,适合作为生成式 world model 的入门复现

</details>


---

## 五、参考资料汇总
<details>
<summary><b>5.1 动手实践</b></summary>

最小成本跑通:
```bash
# Dreamer v3 官方实现
pip install dreamerv3
# 或 clone: https://github.com/danijar/dreamerv3
```
- 先在 [`CartPole`](https://gymnasium.farama.org/environments/classic_control/cart_pole/) / [`Crafter`](https://github.com/danijar/crafter) 上跑通 Dreamer v3
- 再试 [`MineRL`](https://github.com/minerllabs/minerl) 或 [Atari 100k](https://github.com/google-research/rliable)
- 生成式方向可以玩 [**Genie 开源复现**](https://github.com/1x-technologies/1xgpt) 或 [**DIAMOND**](https://github.com/eloialonso/diamond)(Atari 视觉效果惊艳,代码干净)

</details>

<details>
<summary><b>5.2 理论基础补齐</b></summary>

- **变分推断 / VAE**(latent 建模)— [Kingma 原论文](https://arxiv.org/abs/1312.6114) · [Lil'Log 教程](https://lilianweng.github.io/posts/2018-08-12-vae/)
- **RNN / Transformer / SSM(Mamba)**(时序动力学)— [Mamba 论文](https://arxiv.org/abs/2312.00752)
- **Diffusion models**(生成派必备)— [DDPM](https://arxiv.org/abs/2006.11239) · [Lil'Log diffusion 综述](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
- **Model-based RL 基础** — [Sutton & Barto《Reinforcement Learning》第 8 章(免费 PDF)](http://incompleteideas.net/book/RLbook2020.pdf)

</details>


<details>
<summary><b>5.3 核心读物</b></summary>

- [**A Path Towards Autonomous Machine Intelligence**](https://openreview.net/pdf?id=BZ5a1r-kVsf) — Yann LeCun 白皮书,JEPA 世界观
- [**Danijar Hafner 个人主页**](https://danijar.com/) — Dreamer 系列作者,代码、论文、讲座齐全
- [Meta AI Blog: V-JEPA](https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/)

</details>

<details>
<summary><b>5.4 综述论文</b></summary>

- [*World Models for Autonomous Driving: A Survey*](https://arxiv.org/abs/2403.02622) (2024)
- [*A Survey of World Models for Autonomous Driving*](https://arxiv.org/abs/2501.11260) (2025)
- [*General World Models: A Survey*](https://arxiv.org/abs/2405.03520) (2024)

</details>

<details>
<summary><b>5.5 Blog & 资源汇总</b></summary>

- [**Lil'Log**](https://lilianweng.github.io/) — Lilian Weng,有 RL/世界模型相关综述
- [**The Gradient**](https://thegradient.pub/)
- [**Awesome-World-Model**](https://github.com/LMD0311/Awesome-World-Model) — GitHub 上持续更新的资源汇总

</details>

---

_最后更新:2026-05-03_
