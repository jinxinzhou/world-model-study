# World Model 学习笔记

> 整理自 2026 年 4–5 月的学习讨论。按「是什么 → 为什么重要 → 流派对比 → 怎么入门」的逻辑组织。
>
> 💡 每章使用可折叠区块,点击 ▶ 标题即可展开/收起。

---

## 目录

- [一、World Model 是什么](#一world-model-是什么)
- [二、为什么 World Model 火?实际价值在哪?](#二为什么-world-model-火实际价值在哪)
- [三、三大流派深入对比](#三三大流派深入对比)
- [四、入门路径](#四入门路径)
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

先明确你关心哪一支,学习路径差别很大。

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

## 四、入门路径

<details>
<summary><b>4.0 前置概念:Model-Free vs Model-Based RL</b></summary>

理解 World Model 的前提是先理解它在 RL 谱系里的位置。

### 「环境」是什么

环境(Environment)= **把动作变成下一状态和奖励的「黑盒」**。数学上由两个函数定义:

```
状态转移:  P(s_{t+1} | s_t, a_t)     "做了这个动作,下一步会变成什么"
奖励函数:  R(s_t, a_t)                "做了这个动作,得到多少分"
```

### 「不学习环境」 vs 「学习环境」

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
| **环境模型** (model) | $P(s' \mid s, a)$ 和 $R(s, a)$ —— **物理规律** | 仅 model-based |
| **价值函数** (value) | $V(s)$ 或 $Q(s, a)$ —— **某状态有多好** | 两者都可有 |
| **策略** (policy) | $\pi(a \mid s)$ —— **在某状态选什么动作** | 两者都可有 |

→ **Model-free 学「该做什么」(策略/价值),但不学「世界怎么运作」(模型)**
→ **Model-based 学「世界怎么运作」(模型),然后推出「该做什么」**

### 全面对比

| 维度 | Model-Free | Model-Based |
|------|-----------|-------------|
| 是否学环境模型 | ❌ | ✅ |
| 样本效率 | **低**(需要海量交互) | **高**(可以"梦里训练") |
| 最终性能 | 长期看可以很强 | 受限于模型精度 |
| 工程复杂度 | 相对简单 | 复杂(要训世界模型) |
| 训练稳定性 | 较稳 | 易被模型误差坑(model exploitation) |
| 计算量 | 训练/推理都快 | 训练慢(双重),推理可能慢(规划) |
| 经典代表 | DQN、PPO、SAC | World Models、Dreamer、MuZero |

### Model-Free 的代表算法谱系

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

### Model-Free 的致命弱点

> **样本效率低** —— 这是 model-based / world model 兴起的根本原因。

- **DQN 玩 Atari**:需要 **2 亿帧**(人类玩 39 天不停)
- **DreamerV3 玩 Crafter / Minecraft**:**100 万步**搞定,**100~1000 倍效率提升**

→ 在**真机机器人、自驾、医疗**等"真实数据贵"场景,model-free 几乎不可用。

### 🔑 为什么 Model-Based 样本效率高

**核心一句话**:Model-Based 用**一次真实经验,训一遍世界模型,然后在世界模型里无限复制出"虚拟经验"反复训 policy**。Model-Free 则必须**每一次训练都用一条真实经验**,所以真实数据消耗量天差地别。

下面五个根本原因,**结合具体操作**来理解:

#### 原因 1:学「规律」 vs 学「数据点」

| 步骤 | Model-Free(DQN) | Model-Based(Dreamer) |
|------|------------------|----------------------|
| 收到 `(s, a, r, s')` | 存入 Replay Buffer | 存入 Replay Buffer |
| 用这条经验做什么 | 训 Q 网络:让 $Q(s, a)$ 接近 $r + \gamma \cdot \max Q(s')$ | **两步**:① 训世界模型 $W(s, a) \to (s', r)$;② 用 W 生成无数虚拟经验训 policy |
| 网络输出空间 | "该做什么"(Q 值) | "**世界如何运作**"(转移+奖励) |
| 未见过状态怎么办 | Q 值是插值,**脆弱** | 世界模型可以**外推**(学到了规律) |

**直观类比**:
- Model-free 学生:背 1000 道力学题答案 → 第 1001 题翻车
- Model-based 学生:学会 $F = ma$ → 任何力学题都能推

**Doom 火球例子**:
- Model-free 见过 1000 次"左侧火球" → 只学到"左侧火球 → 向右跳"
- Model-based 学到"火球从怪嘴里直线射出" → **第一次见右侧怪物也知道怎么办**

**Dreamer 里的具体实现**:
```python
def world_model(s, a):
    h = GRU(h, [z, a])
    z_next = MLP_prior(h)
    r_next = MLP_reward(h, z_next)
    return z_next, r_next, h
# 网络权重里存的是"规律"(GRU + MLP 参数),不是"数据点"
```

#### 原因 2:梦里训 policy = 数据增强 10000 倍

先引入一个关键概念 —— **Replay Ratio(回放比例)**:

```
Replay Ratio = (梯度更新次数 × batch_size) / 收集的新真实经验数
            = 每条真实经验平均被网络"看到"的次数
```

**Model-Free 一轮**:
```
1. 收集 256 条真实经验
2. 用这 256 条算 1 次梯度更新
→ Replay Ratio ≈ 1(每条经验平均被采样 1 次)
→ 即便有 Replay Buffer 反复采样,Replay Ratio 最多 ~20
   (再高就过拟合崩塌:Q 网络误差自我放大,policy 失真)
```

**Model-Based 一轮**:
```
1. 收集 256 条真实经验
2. 训世界模型几步(对世界模型的 Replay Ratio ~ 几十)
3. 在世界模型里想象:50 起点 × 15 步 = 750 条虚拟经验
4. policy 从虚拟经验拿到 750 次梯度信号
→ 真实数据被有效"放大"几百~几千倍
→ 不会过拟合 —— 因为虚拟经验是世界模型"按规律生成"的新样本,
   不是反复舔同一批真实数据
```

**关键对比**:

| 指标 | Model-Free(DQN/PPO) | Model-Based(Dreamer) |
|------|---------------------|---------------------|
| 真实经验消耗 | 1000 步 | 1000 步 |
| 每步真实经验做几次梯度 | 1~20 次(replay ratio 天花板) | **世界模型 ~几十次,policy ~几百到几千次** |
| 想象 rollout 长度 H | 不适用 | 15 |
| 想象起点数(并行) | 不适用 | 50 |
| **policy 见到的"训练状态"总数** | 1000~20,000 | **1000 × 50 × 15 = 750,000** |
| 是否会过拟合 | ❌ 高 replay ratio 会崩 | ✅ 虚拟数据有变化,不易过拟合 |

→ **真实消耗相同,policy 训练信号多几十到几千倍**。

**为什么 Model-Free 不能也调高 replay ratio?**

Andrychowicz 2020、D'Oro 2022 等论文实验显示:
```
replay ratio = 1   → 正常
replay ratio = 4   → 略好
replay ratio = 16  → 开始下降
replay ratio = 64  → 崩塌(Q 值估计严重失真)
```
**Model-free 本质上 "新数据 ↔ 训练步数" 是耦合的**,有天花板。

**为什么 Model-Based 能突破?** 关键是**生成机制不同**:
- Model-free 反复采样同一批真实数据 → 像"反复舔同一块糖" → 过拟合
- Model-based 用世界模型生成新的虚拟数据 → 像"用糖的配方做 1000 块新糖" → 每条样本都不同 → 不过拟合

**为什么虚拟数据有效?** 只要世界模型够准,梦里 `(ŝ, â, r̂, ŝ')` 与真实经验**统计分布一致**,actor-critic 分不出真假;但梦里数据近乎"免费"(纯 GPU 矩阵乘法,微秒级)。

#### 原因 3:梦里可以"重置"任意起点,自由探索

**先理解一个根本约束:为什么真实环境只能 reset 到初始状态?**

| 环境类型 | 为什么不能任意 reset |
|---------|---------------------|
| **真实物理世界**(机器人/自驾) | 物理不可逆 —— 没有"撤销键",打碎的杯子不会自己回来;reset 一次 = 人类手动复位 + 等几秒 |
| **游戏 / 模拟器**(Gym/Doom) | 开发者只暴露了 `env.reset()` 一个入口,固定回初始;内部状态太复杂(上千变量),没设计 dump/restore API |
| **真实软件系统**(推荐/搜索) | 想 reset 到"下雨天+行人横穿"?**得真等下雨** |

**而梦境 = 一堆神经网络张量**,可以**任意赋值**:
```python
env_dream.z = z_target    # 任意起点,无物理约束
env_dream.h = h_target
```
没有计时器、没有内存依赖、完全可逆、完全可控 —— 这是世界模型相对真实环境的**根本结构性优势**。

**工程上"假装能 reset"的几种 workaround**(对比说明梦境的优势):
- 多并行 worker:只能从**自然到达**的状态起跑
- 模拟器 snapshot(MuJoCo):支持,但 restore 比 step 慢 10×+,**真机器人不支持**
- HER(Hindsight Replay):事后假装目标,不是真 reset

**情境**:你想训"侧翻边缘怎么救车"

| 步骤 | 真实环境 | 梦境 |
|------|---------|------|
| 到达"侧翻边缘"状态 | **必须真开到那里**,几百次完整 episode | **直接从 latent 挑一个侧翻状态作为起点** |
| 试 1000 种救车策略 | 损毁 1000 次 | 1 秒内完成 |
| 失败后 | episode 结束,reset 整环境 | **直接退回上一帧重试** |

**Dreamer 的实现**:
```python
# 从 Replay Buffer 随机选 50 个真实状态做起点
real_states = buffer.sample(batch_size=50)
h_0, z_0 = encoder(real_states)
# 50 个起点完全并行 rollout
for t in range(15):
    a_t = actor(h_t, z_t)
    h_{t+1}, z_{t+1} = world_model(h_t, z_t, a_t)
```

**核心差距**:

| 操作 | 真实环境 | 梦境 |
|------|---------|------|
| Reset 到任意状态 | ❌ 大多只能 reset 到初始 | ✅ 任意 z 都行 |
| 并行多个 rollout | ❌ 需多实例,贵 | ✅ GPU batch=1024 也轻松 |
| 让结果"撤销" | ❌ 物理不可撤销 | ✅ 重置 latent |
| 从未到过的"假想状态"起跑 | ❌ 不可能 | ✅ 只要在世界模型分布内 |

**最大好处:Counterfactual reasoning(反事实推理)**

> "如果刚才向左走会怎样?"

Model-free 没法回答(没真试过);Model-based **梦里真试一下**,微秒内得答案。

**形象比喻**:
- 真实环境训学生 = 每次只能从一年级第一课开始,想练高考压轴题?**先把整个高中重读一遍**
- 梦境训学生 = **任意一题随手就能跳到**,想练哪道就练哪道

→ 真实环境的探索成本主要花在**到达感兴趣的状态**上,而不是**学怎么应对它** —— 这就是为什么梦境的"任意 reset"能带来 2-10× 的额外样本效率提升。


#### 原因 4:解析梯度反传(Dreamer 系的杀手锏)

**Model-Free 的 policy gradient(以 REINFORCE 为例)**:
```
∇θ J = E[ R · ∇θ log π(a|s) ]
            ↑          ↑
        真实奖励    随机采样
```
`R` 受环境随机性影响 → 梯度是 **Monte Carlo 估计**,**方差极高** → 需要 N 极大(几千-几万 episode)才能稳定。

**Model-Based + 可微世界模型**:
```python
# 整条想象链都是神经网络,可微!
for t in range(H):
    a_t = actor(h_t, z_t)
    h_{t+1}, z_{t+1} = world_model(h_t, z_t, a_t)
    r_t = reward_model(h_t, z_t)
    total_value += γ**t * r_t

loss = -total_value
loss.backward()    # 梯度通过 reward → world_model → actor 全程反传
```

**对比**:

| 角度 | Model-Free | Model-Based |
|------|-----------|-------------|
| 梯度来源 | 采样估计 $\nabla_\theta J \approx R \cdot \nabla \log \pi$ | **解析计算** $\nabla_\theta R = \frac{\partial R}{\partial a} \cdot \frac{\partial a}{\partial \theta}$ |
| 单步信息量 | 1 个 scalar reward | 全部张量($R$ 的全导数) |
| 样本复杂度 | $O(1/\epsilon^2)$ | $\mathbf{O(1/\epsilon)}$ |
| 类比 | 蒙眼朝山顶猜方向 | **拿指南针知道精确梯度方向** |

**关键技巧:Reparameterization Trick(让随机也可微)**
```python
# ❌ 不可微(梯度断了)
z = sample(Normal(μ, σ))
# ✅ 可微(梯度能通过 μ 和 σ 反传)
ε = sample(Normal(0, 1))
z = μ + σ * ε
```
这是 VAE、Dreamer、Diffusion 共享的核心技巧。

#### 原因 5:梦里可以长程预演

**Model-Free 评估"长期价值"**:
```
1. 真实环境跑 1000 步
2. 等 episode 结束
3. 累积 return 反推每一步
```

| 操作 | 真实耗时 |
|------|---------|
| 真实 1 步 | 1ms ~ 1s |
| 跑完 1000 步 episode | 1s ~ 几分钟 |
| 跑 1000 episode 才能稳定估计 | 几小时 ~ 几天 |

**Model-Based 评估"长期价值"**:
```
1. 在 latent 里 rollout 15 步
2. critic 估计后续残值
3. λ-return = Σ γ^t · r_t + γ^H · V(s_H)
```

| 操作 | 真实耗时 |
|------|---------|
| 世界模型 1 步 (GPU batch=50) | 0.1ms |
| 跑完 H=15 步 rollout | 1.5ms |
| 并行 50 个起点 | **仍然 1.5ms** |

→ **1.5ms 算力产出 50×15=750 步长期信号**

**为什么能"用 15 步代替 1000 步"?**

```
V_λ = γ^0·r_0 + γ^1·r_1 + ... + γ^14·r_14  +  γ^15·V(s_15)
       ↑                                          ↑
     真实想象的 15 步                       critic 估计后面的"残值"
```

只要 critic 估的 `V(s_15)` 还算准,**不需要真 rollout 到 1000 步** —— 这就是 **bootstrapping**(自举)。

| 方法 | rollout 长度 | 为什么 |
|------|--------------|--------|
| Monte Carlo | 整 episode(1000) | 不信任 V,全靠真实奖励 |
| Model-free TD(1-step) | 1 步 | 完全信任 V,偏差大 |
| **Dreamer λ-return** | **15 步** | **甜点**:适度信任 V + 适度真实信号 |

#### 📊 五个原因总结对比表

| # | 原因 | Model-Free 做法 | Model-Based 做法 | 效率提升来源 |
|:---:|------|----------------|----------------|------------|
| **1** | **学规律 vs 学数据** | Q 网络存"状态→价值"数据点 | 世界模型存"状态+动作→下一状态"的物理规律 | **泛化能力** —— 没见过的状态也能推 |
| **2** | **数据增强** | 1 条真实经验 → 1 次 policy 更新 | 1 条真实经验 → 训世界模型 → 梦里千百次 rollout → 千百次 policy 更新 | **训练信号 ×750+** |
| **3** | **自由探索** | 必须真去到某状态;失败 = episode 重置 | 任意 reset 到任何 latent;失败 = 重玩 latent | **零代价试错** |
| **4** | **解析梯度** | Policy gradient 用 sampling,O(N) 样本 | 整条想象链可微,梯度精确反传,O(1) 样本 | **方差消除 → 收敛指数级加速** |
| **5** | **长程预演** | 真实 1000 步 = 实际 1000 步时间 | GPU 15 步 + critic 估剩余 = 1.5ms | **时间被压缩** |

#### 各原因的"效率倍数"粗估

| 原因 | 最佳情况下的样本效率提升 |
|------|-----------------------|
| 1. 学规律 → 泛化 | 5× ~ 50× |
| 2. 梦里数据增强 | 10× ~ 100× |
| 3. 自由起点探索 | 2× ~ 10× |
| 4. **解析梯度** | **100× ~ 1000×**(Dreamer 系最关键来源) |
| 5. 长程预演 | 5× ~ 50× |
| **总倍数(乘积)** | **5,000× ~ 几十万×** 量级(理论上) |

实测:Dreamer 在 Atari 提升 **10×~100×**,在机器人提升 **1000×**,跟估算量级吻合。

#### 💡 直观类比 —— 学开车

- 🔴 **Model-Free**:想学下雪天开车?**必须等下雪**;想学侧翻救车?**必须真侧翻**
- 🟢 **Model-Based**:**真开 100 小时学会方向/刹车/摩擦力的规律**,然后**在脑中预演 10000 个 corner case**

#### 真实数字对比

| 任务 | Model-Free | Model-Based | 提升 |
|------|-----------|-------------|-----|
| Atari Breakout | DQN/Rainbow **2 亿帧** | DreamerV3 **2000 万帧** | 10× |
| Atari 100k | Rainbow 很差 | EfficientZero 接近人类 | 巨大 |
| Crafter | PPO 几千万步,~10 分 | DreamerV3 **100 万步**,~14 分 SOTA | 30×+ |
| 真机机器人抓取 | PPO 几个月真机数据 | Dreamer 类 **几小时** | 1000× |

#### 代价(没有免费午餐)

- ✅ 省的是**真实样本**(数据)
- ❌ 花的是 **GPU 算力**(要训世界模型 + 做梦)
- ❌ **工程更复杂**,容易被模型误差坑(model exploitation)

→ **真机机器人 / 自驾**(数据贵):model-based 完胜
→ **Atari / 模拟器 / LLM RLHF**(数据便宜):model-free 也能用

#### 🎯 一句话总结

> **Model-Based RL 的高样本效率不是"一个魔法",而是「规律泛化 + 数据增强 + 自由探索 + 解析梯度 + 长程预演」五个独立机制的复利效应。其中「解析梯度反传」是 Dreamer 系真正区别于一切前辈的杀手锏 —— 把方差极高的 Monte Carlo 估计替换成精确的反向传播,这是质的飞跃。**

### 当下共识

- **数据廉价**(模拟器、游戏、LLM RLHF) → model-free 仍然主流
- **数据昂贵 / 需要规划 / 需要想象**(机器人、自驾、Agent) → world model 是未来

**一句话**:Model-Free RL 不学环境,纯靠试错学"该怎么做"。简单稳定但样本效率低,所以在现实世界场景被 model-based / world model 越来越多地替代。

</details>

<details>
<summary><b>4.1 必读论文(按顺序)</b></summary>

**奠基**
1. [**World Models**](https://arxiv.org/abs/1803.10122) (Ha & Schmidhuber, 2018) — 经典起点,VAE + MDN-RNN + 小 controller([交互式网站](https://worldmodels.github.io/))

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

   ```math
   \mathcal{D} = \{(o_t, a_t)\}_{t=1}^{T}, \quad a_t \sim \text{Uniform}(\mathcal{A})
   ```

   **阶段 2(a)**:训 VAE(只看图像)→ V

   ```math
   \mathcal{L}_{\text{VAE}} = \mathbb{E}_{q(z|o)}\big[\|o - \hat{o}\|^2\big] + \beta \cdot \text{KL}\big(q(z|o) \,\|\, \mathcal{N}(0, I)\big)
   ```

   **阶段 2(b)**:训 MDN-RNN(看 z 和 a 的序列)→ M

   ```math
   \mathcal{L}_{M} = -\sum_t \log P(z_{t+1} \mid z_t, a_t, h_t) + \sum_t \text{BCE}(\text{done}_t^{\text{pred}}, \text{done}_t^{\text{real}})
   ```

   **阶段 3**:冻结 V 和 M,CMA-ES 训 Controller

   ```math
   \theta_C^* = \arg\max_{\theta_C} \; \mathbb{E}_{\text{dream rollout}}\Big[\sum_{t=0}^{T} r_t\Big] \quad \text{(无梯度黑盒优化)}
   ```

   **阶段 4**(部署 / 推理):把训好的 C 放回真实环境

   ```math
   a_t = C\big([z_t,\, h_t]\big), \quad z_t = V_{\text{encode}}(o_t), \quad h_{t+1} = M_{\text{RNN}}(a_t, z_t, h_t)
   ```

   下面逐阶段详细解释。

   ##### 阶段 1:用随机策略收集真实数据

   **🎯 目的**:让世界模型见过尽可能多样的状态(包括死亡、碰撞等边角情况),所以**用随机策略**而不是强策略。

   **核心公式**:
   ```math
   \mathcal{D} = \{(o_t, a_t)\}_{t=1}^{T}, \quad a_t \sim \text{Uniform}(\mathcal{A})
   ```

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
   ```math
   \mathcal{L}_{\text{VAE}} = \underbrace{\mathbb{E}_{q(z|o)}[\|o - \hat{o}\|^2]}_{\text{重建损失}} + \underbrace{\beta \cdot \text{KL}\big(q(z|o) \,\|\, \mathcal{N}(0, I)\big)}_{\text{KL 正则,逼近标准高斯先验}}
   ```

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
   ```math
   \mathcal{L}_{\text{M}} = \underbrace{-\sum_t \log P(z_{t+1} \mid z_t, a_t, h_t)}_{\text{MDN 负对数似然(高斯混合)}} \;+\; \underbrace{\sum_t \text{BCE}(\text{done}_t^{\text{pred}}, \text{done}_t^{\text{real}})}_{\text{结束概率二元交叉熵}}
   ```

   其中 z 的预测分布是 K 个高斯的混合:
   ```math
   P(z_{t+1} \mid \cdot) = \sum_{k=1}^{K} \pi_k \cdot \mathcal{N}(z_{t+1}; \mu_k, \sigma_k^2)
   ```

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
   ```math
   \theta_C^* = \arg\max_{\theta_C} \; \mathbb{E}_{\text{dream rollout}} \Big[\sum_{t=0}^{T} r_t\Big]
   ```

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

   ---

   ### Part 1:CMA-ES 是什么 —— 三句话原理

   1. **维护一个多元高斯分布** $\mathcal{N}(m, \sigma^2 C)$ 描述"我觉得最优解大概在哪"
   2. **每一代撒 λ 个候选,选最好的 μ 个**(μ ≈ λ/2)
   3. **更新均值 m、协方差 C、步长 σ**,让分布慢慢"瞄准"最优区域

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
   ⑤ 更新协方差 C 和步长 σ(看进化路径)
   ```

   关键超参:**λ** (population) = 16~64,**μ** = λ/2,**σ** 初始 = 0.1,代数 = 几百到几千。

   #### 🔍 步骤①里的 B 和 D 是什么?

   $B$ 和 $D$ 是协方差矩阵 $C$ 的**特征分解**:
   ```math
   C = B \cdot D^2 \cdot B^\top
   ```

   - **B**:正交矩阵(C 的特征向量) —— 几何上是**旋转**,把标准坐标轴转到 C 椭球的主轴方向
   - **D**:对角矩阵(C 特征值的平方根) —— 几何上是**沿坐标轴方向缩放**

   **为什么要拆 C 成 B·D²·Bᵀ?** 因为计算机只会生成标准正态噪声 $z \sim \mathcal{N}(0, I)$,我们需要把它变换成符合 $\mathcal{N}(m, \sigma^2 C)$ 的样本。下图把整个过程拆成 4 步直观展示:

   <p align="center">
     <img src="asset/cma-es/01_BD_decomposition.png" width="900"/><br/>
     <i>采样公式 x = m + σ·B·D·z 的几何分解:① 从标准球形噪声 z 出发 → ② D 沿坐标轴拉伸成椭球 → ③ B 旋转到 C 的主轴方向 → ④ σ 放大并平移到 m 位置。蓝点是 200 个采样,红色椭圆是 2σ 范围。</i>
   </p>

   **小贴士**:每代只在 C 更新后重新算一次 B 和 D(`eigendecompose(C)`),然后这一代的 λ 次采样全部复用,计算上很划算。

   #### 协方差 C 的自适应(CMA 的灵魂)

   两个信号告诉 C 该怎么变:
   - **Rank-μ Update**:本代选优的样本协方差 → 最优解集中在哪个方向,C 在那个方向变粗
   - **Rank-1 Update**:历代均值移动方向的累积(进化路径) → 连续几代往同方向走就加强它

   ```math
   C \leftarrow (1 - c_1 - c_\mu) C + c_1 \cdot p_c p_c^\top + c_\mu \cdot \sum w_i (x_i - m)(x_i - m)^\top
   ```

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

   → **你的直觉其实更接近"方案 B"**(让梦境可微+反传),Dreamer 2020 实现的正是这条路。

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

   ### Part 6:动手玩玩

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

   > **梦境技术上完全可微,但 Ha 2018 选 CMA-ES 是工程权衡:Controller 极小、梦境噪声大、model exploitation 怕被梯度放大、长 RNN 梯度难、demo 优先。Bellman 方程是 Q-learning 工具,不是 actor 优化的最佳选择;真正"可微梦境+反传 actor"的范式由 Dreamer 2020 实现,从此 CMA-ES 在 model-based RL 退场。你直觉里"用梯度求解"的想法,正是 Dreamer 系的核心思路 —— 不过用的是 policy gradient 而非 Bellman。**

   </details>

   ##### 阶段 4:部署 / 推理(在真实环境验证)

   **🎯 目的**:把训好的 C 拿到真实环境跑,看是否能迁移成功。此阶段**V 和 M 不再更新,但继续在线使用**(V 提供感知压缩,M 提供时序记忆 h)。

   **核心公式**:
   ```math
   a_t = C\big([\,z_t,\; h_t\,]\big), \quad z_t = V_{\text{encode}}(o_t), \quad h_{t+1} = M_{\text{RNN}}(a_t, z_t, h_t)
   ```

   - 注意:**用真实 $z_t$** 更新 $h$(不是用 M sample 的 $\hat{z}$)
   - 这相当于 M 在真实环境里"陪跑",维护对未来的预期

   **具体代码**(你给的图就是这段,论文 Algorithm 1):
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
           Env4["真实环境"] -->|obs| V2["V"]
           V2 -->|z| C2["Controller"]
           M2["M (提供 h)"] -.->|h| C2
           C2 -->|a| Env4
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

   这是个**特别反直觉的点** —— 你以为 M 会预测 reward,但 **World Models 2018 在 VizDoom 上根本没显式预测连续 reward**。

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

   理解这三层细节,你就能:
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

2. [**PlaNet**](https://arxiv.org/abs/1811.04551) (2019) — latent dynamics 用于规划
3. **Dreamer v1/v2/v3** (2020–2023) — 目前 RL 派最强基线,**v3 一定要读**
   - [DreamerV1](https://arxiv.org/abs/1912.01603) · [DreamerV2](https://arxiv.org/abs/2010.02193) · [**DreamerV3**](https://arxiv.org/abs/2301.04104)

**生成式 / 视频**

4. [**GAIA-1**](https://arxiv.org/abs/2309.17080) (Wayve, 2023) — 自动驾驶 world model([官方 blog](https://wayve.ai/thinking/scaling-gaia-1/))
5. **Genie / Genie 2** (DeepMind, 2024) — 可交互生成环境
   - [Genie 论文](https://arxiv.org/abs/2402.15391) · [Genie 2 blog](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/)
6. [**Sora 技术报告**](https://openai.com/index/video-generation-models-as-world-simulators/) (OpenAI, 2024) — 把视频生成视作 world simulator 的论述

**前沿**

7. **V-JEPA / V-JEPA 2** (Meta / LeCun) — 非生成式、predictive embedding 路线
   - [V-JEPA](https://arxiv.org/abs/2404.08471) · [V-JEPA 2](https://ai.meta.com/vjepa/) · [I-JEPA](https://arxiv.org/abs/2301.08243)
8. 其他值得关注:
   - [**1X World Model**](https://www.1x.tech/discover/1x-world-model)(人形机器人)
   - [**Oasis**](https://oasis-model.github.io/)(Decart,实时 Minecraft 生成)
   - [**DIAMOND**](https://arxiv.org/abs/2405.12399)(NeurIPS 2024,[代码](https://github.com/eloialonso/diamond))

</details>

<details>
<summary><b>4.2 动手实践</b></summary>

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
<summary><b>4.3 理论基础补齐</b></summary>

- **变分推断 / VAE**(latent 建模)— [Kingma 原论文](https://arxiv.org/abs/1312.6114) · [Lil'Log 教程](https://lilianweng.github.io/posts/2018-08-12-vae/)
- **RNN / Transformer / SSM(Mamba)**(时序动力学)— [Mamba 论文](https://arxiv.org/abs/2312.00752)
- **Diffusion models**(生成派必备)— [DDPM](https://arxiv.org/abs/2006.11239) · [Lil'Log diffusion 综述](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
- **Model-based RL 基础** — [Sutton & Barto《Reinforcement Learning》第 8 章(免费 PDF)](http://incompleteideas.net/book/RLbook2020.pdf)

</details>

---

## 五、参考资料汇总

<details>
<summary><b>5.1 核心读物</b></summary>

- [**A Path Towards Autonomous Machine Intelligence**](https://openreview.net/pdf?id=BZ5a1r-kVsf) — Yann LeCun 白皮书,JEPA 世界观
- [**Danijar Hafner 个人主页**](https://danijar.com/) — Dreamer 系列作者,代码、论文、讲座齐全
- [Meta AI Blog: V-JEPA](https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/)

</details>

<details>
<summary><b>5.2 综述论文</b></summary>

- [*World Models for Autonomous Driving: A Survey*](https://arxiv.org/abs/2403.02622) (2024)
- [*A Survey of World Models for Autonomous Driving*](https://arxiv.org/abs/2501.11260) (2025)
- [*General World Models: A Survey*](https://arxiv.org/abs/2405.03520) (2024)

</details>

<details>
<summary><b>5.3 Blog & 资源汇总</b></summary>

- [**Lil'Log**](https://lilianweng.github.io/) — Lilian Weng,有 RL/世界模型相关综述
- [**The Gradient**](https://thegradient.pub/)
- [**Awesome-World-Model**](https://github.com/LMD0311/Awesome-World-Model) — GitHub 上持续更新的资源汇总

</details>

---

_最后更新:2026-05-03_
