# World Models Study Notes

**🌐 Language**: [中文](World-Model-学习笔记.md) · **English**

> Compiled from study discussions in April–May 2026, organized by the logic: "What it is → Why it matters → Schools comparison → How to get started"
>
> 💡 Each chapter uses collapsible blocks; click ▶ on the title to expand/collapse.

---

## Table of Contents

- [I. What Is a World Model](#i-what-is-a-world-model)
- [II. Why Are World Models Popular? What Is Their Practical Value?](#ii-why-are-world-models-popular-what-is-their-practical-value)
- [III. In-Depth Comparison of the Three Schools](#iii-in-depth-comparison-of-the-three-schools)
- [IV. Getting Started](#iv-getting-started)
- [V. Reference Materials](#v-reference-materials)

---

## I. What Is a World Model

<details>
<summary><b>Expand / Collapse</b></summary>

World Model is a prominent research direction in AI agent systems. Its central idea is to enable a model to **predict future states of the environment**, thereby supporting planning, decision-making, and imagination-based reasoning.

The field currently consists of three major schools (see [§3](#iii-in-depth-comparison-of-the-three-schools)):

| School | Representatives | Prediction Target |
|------|------|---------|
| **Generative / Video School** | Sora, Genie, GAIA | Pixels / video frames |
| **Latent Dynamics (RL School)** | Dreamer v1/v2/v3, PlaNet | latent state (with pixel reconstruction) |
| **JEPA (Predictive Representation School)** | I-JEPA, V-JEPA, V-JEPA 2 | Abstract embedding (without reconstruction) |

The relevant school should be identified first, because the learning paths differ substantially.

</details>

---

## II. Why Are World Models Popular? What Is Their Practical Value?

<details>
<summary><b>2.1 Why They Suddenly Became Popular</b></summary>

**1. LLMs have encountered bottlenecks and need a new narrative**
Pure language models perform poorly on physical reasoning, long-horizon planning, and embodied tasks. The industry consensus is that **predicting the next token from text alone does not yield genuine physical common sense**. LeCun has strongly argued that "LLMs are a dead end," and JEPA / World Model has become a flagship alternative route.

**2. Sora became a breakout example (early 2024)**
OpenAI positioned Sora as a "world simulator" rather than merely a video generator, which immediately pushed the concept into the mainstream. Capital markets and media attention followed rapidly.

**3. Embodied intelligence / robotics / autonomous driving accelerated**
Tesla FSD, Wayve, 1X, Figure, and Physical Intelligence all require one capability: **large-scale, low-cost simulation of the real world before deployment**. Collecting real-machine data is too expensive and too slow; world model is the only scalable solution.

**4. Technical conditions matured**
- Diffusion + Transformer brought video generation quality beyond a usable threshold
- Dreamer v3 first demonstrated that **one set of hyperparameters** can solve 150+ tasks, including Minecraft diamond collection (pure model-based, the first in the world)
- Compute and data scale became available

**5. Scaling Law needs a new battlefield**
Text data is approaching exhaustion, whereas video and interaction data are the next gold mine. world model is a natural architecture for absorbing such data.

</details>

<details>
<summary><b>2.2 Practical Value (Ordered by Deployment Maturity)</b></summary>

#### ✅ Already Commercially Valuable / Clearly Useful

**1. Autonomous-driving simulation**
- [Wayve GAIA-1](https://wayve.ai/thinking/scaling-gaia-1/) / [GAIA-2](https://wayve.ai/thinking/gaia-2/), [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/), Tesla internal models
- Value: generating massive numbers of corner cases (heavy rain, suddenly emerging pedestrians), **reducing per-mile testing cost from several dollars to a few cents**
- Addresses the fundamental difficulty of collecting **long-tail data** in real road testing

**2. Model-based RL (robot control)**
- The [Dreamer family](https://danijar.com/project/dreamerv3/) has already enabled real robots to **learn new skills from only a few hours of real-machine data** (where traditional model-free methods require days)
- Google DeepMind, [1X](https://www.1x.tech/discover/1x-world-model), and [Physical Intelligence](https://www.physicalintelligence.company/) are all using related approaches
- Value: **1–2 orders of magnitude improvement in sample efficiency**, making real-machine training feasible

**3. Games / content generation**
- [Genie 2](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/), [Oasis](https://oasis-model.github.io/) (real-time Minecraft generation), [DIAMOND](https://github.com/eloialonso/diamond)
- Value: interactive worlds can be generated **without a game engine**, potentially transforming game-development workflows in the long run

#### 🟡 Promising but Not Yet Scaled

**4. Agent planning / reasoning**
- Give an LLM agent a world model so that it can trial-and-error "in its head" before acting
- This is analogous to human "imagination" and is one of the key pieces toward AGI

**5. Scientific simulation**
- Fluids, weather, materials, and protein dynamics
- [GraphCast](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/) and [AlphaFold](https://alphafold.ebi.ac.uk/) can be viewed, in a sense, as domain-specific world model systems
- Value: 1000–10000× faster than traditional numerical simulation

**6. Video generation / film and media**
- [Sora](https://openai.com/sora/), [Kling](https://kling.kuaishou.com/), [Runway](https://runwayml.com/)
- Value: content-productivity tools, although "physical realism" remains below the required standard

#### 🔴 Still Speculative

- A general physical-reasoning engine
- A true "mind simulator" for general Agent systems
- Real-time edge-side world models

</details>

<details>
<summary><b>2.3 A Sober View: Real Limitations</b></summary>

1. **Evaluation is extremely difficult** — What does it mean for a model to "model the world well"? There is no accepted metric, and self-deception is easy.
2. **Long-horizon instability** — Current models begin to drift and violate physics after generating for tens of seconds.
3. **Compute is expensive** — Training a competent video world model costs more than training an LLM.
4. **LeCun's JEPA route has not yet been proven to scale** — It remains largely at the vision stage.
5. **The term "World Model" is susceptible to overuse** — Many companies repackage ordinary video generation as world model to inflate valuation narratives.

</details>

<details>
<summary><b>2.4 TL;DR</b></summary>

> **The short-term value lies in simulation-based training for robotics and autonomous driving (already monetized); the long-term value is that it may become the next-generation AI infrastructure after LLMs — enabling models to truly "understand" rather than merely "memorize" the world.**

</details>

---

## III. In-Depth Comparison of the Three Schools

<details>
<summary><b>3.1 Overview of the Three World Model Schools</b></summary>

| School | Representatives | Prediction Target | Goal |
|------|------|---------|------|
| **Generative World Model** | Sora, Genie, GAIA, DIAMOND | **Pixels / video frames** | Generate a visualizable future |
| **Latent Dynamics (RL School)** | Dreamer v1/v2/v3, PlaNet | **latent state** (still with reconstruction loss) | Serve model-based RL planning |
| **JEPA (Predictive Representation)** | I-JEPA, V-JEPA, V-JEPA 2 | **Abstract embedding**, without pixel reconstruction | Learn structured representations of the world |

</details>

<details>
<summary><b>3.2 Core Claims of JEPA</b></summary>

JEPA is LeCun's strongly advocated **third route**, forming its own school: "Predictive Embedding" representation learning.

LeCun's view is explicit:

> **"Do not predict pixels; predict representations."**

**Rationale**:
- Pixel-level prediction wastes compute on irrelevant details (cloud shapes, leaf motion)
- The world is intrinsically not fully predictable; forcing reconstruction leads to learning noise
- The human brain is not "rendering 4K video internally"; it predicts at an abstract level

**Method**:
- Use an encoder to map observations to latent
- Use a predictor to predict the embedding of masked or future parts in **latent space**
- Use **stop-gradient + EMA target encoder** to prevent collapse (similar to BYOL / DINO)
- **No decoder and no pixel reconstruction**

</details>

<details>
<summary><b>3.3 Key Differences Between JEPA and Dreamer (Easy to Confuse)</b></summary>

Both predict in latent space, but:

| | Dreamer | JEPA |
|---|---------|------|
| Pixel reconstruction? | **Yes** (reconstruction loss is a core supervision signal) | **No** (pure embedding prediction) |
| Training signal | Reconstruction + reward + KL | Embedding distance + collapse prevention |
| Objective | model-based RL, using the world model for rollout planning | **Self-supervised representation learning**, followed by downstream tasks |
| Can it "imagine" images? | Yes (has a decoder) | **No** (intentionally) |

Strictly speaking, therefore, **Dreamer is "latent but still generative," whereas JEPA is truly "non-generative."**

</details>

<details>
<summary><b>3.4 Current Status of JEPA (2024–2026)</b></summary>

**Progress**
- I-JEPA (images, 2023), V-JEPA (video, 2024), and **V-JEPA 2 (late 2024)** — solid performance on action prediction and physical-understanding benchmarks
- Meta has invested heavily; this is LeCun's flagship project

**Concerns**
- It has not yet produced a **striking demo** at the level of Sora / Dreamer (because there is no decoder, the demo is less intuitive)
- Whether it scales remains unresolved
- Most of the community is still competing along the generative route

**In one sentence**:

> **JEPA is LeCun's "anti-Sora" bet: model the world using abstract representations rather than pixels. The theory is elegant, but engineering evidence remains insufficient. At present, it has high academic visibility and limited industrial deployment.**

</details>

---

## IV. Getting Started

<details>
<summary><b>4.0 Background Concept: Model-Free vs Model-Based RL</b></summary>

Understanding World Model first requires understanding its position in the RL taxonomy.

### What Is the "Environment"?

Environment = **a "black-box" that converts actions into next states and rewards**. Mathematically, it is defined by two functions:

```
State transition:  P(s_{t+1} | s_t, a_t)     "Given this action, what will the next step become?"
Reward function:   R(s_t, a_t)                "Given this action, how much reward is obtained?"
```

### "Not Learning the Environment" vs "Learning the Environment"

**🔴 Model-Free — Not Learning the Environment**

The Agent treats the environment as a **pure black-box**: it can try actions and receive feedback, but it **does not predict** "what will happen if X is done"; it only learns "**which action yields high reward in this state**."

- Analogy: playing Mario for the first time, failing 1000 times, and memorizing 1000 "successful patterns" without studying jump physics
- DQN's method: input image → output Q values for 18 actions → argmax, while **never predicting the next frame**

**🟢 Model-Based / World Model — Learning the Environment**

The Agent actively learns a **copy of the environment** (a world model) and then performs rollouts in its mind.

- Analogy: learning that "press A → jump 4 blocks" and "touch Goomba → die," making mental rehearsal possible
- Dreamer's method: learn RSSM to predict the next latent + reward, and train actor-critic in a virtual environment, i.e., "dreaming"

### Key Clarification: Model ≠ Policy ≠ Value

These three terms are easily confused:

| Concept | What Is Learned | Who Has It |
|------|----------|------|
| **Environment model** (model) | $P(s' \mid s, a)$ and $R(s, a)$ — **physical laws** | Only model-based |
| **Value function** (value) | $V(s)$ or $Q(s, a)$ — **how good a state is** | Both can have it |
| **Policy** (policy) | $\pi(a \mid s)$ — **which action to choose in a state** | Both can have it |

→ **Model-free learns "what to do" (Policy/value), but not "how the world works" (model)**
→ **Model-based learns "how the world works" (model), then derives "what to do"**

### Comprehensive Comparison

| Dimension | Model-Free | Model-Based |
|------|-----------|-------------|
| Learns an environment model? | ❌ | ✅ |
| Sample efficiency | **Low** (requires massive interaction) | **High** (can train "inside the dream") |
| Asymptotic performance | Can be very strong in the long run | Limited by model accuracy |
| Engineering complexity | Relatively simple | Complex (must train a world model) |
| Training stability | More stable | Vulnerable to model error (model exploitation) |
| Compute | Fast in training/inference | Slow training (dual burden); inference may be slow (planning) |
| Classic representatives | DQN, PPO, SAC | World Models, Dreamer, MuZero |

### Representative Model-Free Algorithm Families

```
┌─ Value-based ─────────────────────────┐
│  Q-learning → DQN → Rainbow → R2D2    │
└───────────────────────────────────────┘

┌─ Policy-based ────────────────────────┐
│  REINFORCE → TRPO → PPO ⭐ most used   │
└───────────────────────────────────────┘

┌─ Actor-Critic ────────────────────────┐
│  A3C → DDPG → TD3 → SAC ⭐ continuous control │
└───────────────────────────────────────┘
```

### The Fatal Weakness of Model-Free Methods

> **Low sample efficiency** — this is the fundamental reason model-based / world model methods emerged.

- **DQN on Atari**: requires **200 million frames** (equivalent to a human playing continuously for 39 days)
- **DreamerV3 on Crafter / Minecraft**: succeeds in **1 million steps**, a **100–1000× efficiency improvement**

→ In settings where "real data is expensive," such as **real robots, autonomous driving, and medicine**, model-free methods are nearly unusable.

### 🔑 Why Model-Based Methods Have High Sample Efficiency

**Core statement**: Model-Based uses **one real experience to train the world model once, then repeatedly creates unlimited "virtual experiences" inside the world model to train the policy**. Model-Free must use **one real experience for every training signal**, so the gap in real-data consumption is enormous.

The following five fundamental reasons should be understood **in terms of concrete operations**:

#### Reason 1: Learning Laws vs Learning Data Points

| Step | Model-Free (DQN) | Model-Based (Dreamer) |
|------|------------------|----------------------|
| Receives `(s, a, r, s')` | Store in Replay Buffer | Store in Replay Buffer |
| What is done with this experience? | Train the Q network: make $Q(s, a)$ close to $r + \gamma \cdot \max Q(s')$ | **Two steps**: ① train the world model $W(s, a) \to (s', r)$; ② use W to generate many virtual experiences to train the policy |
| Network output space | "What to do" (Q values) | "**How the world works**" (transition + reward) |
| What about unseen states? | Q values are interpolation and **fragile** | The world model can **extrapolate** (it has learned laws) |

**Intuitive analogy**:
- Model-free student: memorizes answers to 1000 mechanics problems → fails on problem 1001
- Model-based student: learns $F = ma$ → can derive answers to any mechanics problem

**Doom fireball example**:
- Model-free has seen "left-side fireball" 1000 times → only learns "left-side fireball → jump right"
- Model-based learns that "fireballs shoot linearly from the monster's mouth" → **knows what to do the first time a monster appears on the right**

**Concrete implementation in Dreamer**:
```python
def world_model(s, a):
    h = GRU(h, [z, a])
    z_next = MLP_prior(h)
    r_next = MLP_reward(h, z_next)
    return z_next, r_next, h
# What is stored in the network weights is "laws" (GRU + MLP parameters), not "data points"
```

#### Reason 2: Training Policy in the Dream = 10,000× Data Augmentation

First introduce a key concept — **Replay Ratio**:

```
Replay Ratio = (number of gradient updates × batch_size) / number of newly collected real experiences
             = average number of times each real experience is "seen" by the network
```

**One Model-Free round**:
```
1. Collect 256 real experiences
2. Use these 256 experiences for 1 gradient update
→ Replay Ratio ≈ 1 (each experience is sampled once on average)
→ Even with repeated sampling from the Replay Buffer, Replay Ratio is at most ~20
   (higher values cause overfitting collapse: Q-network errors self-amplify and the policy distorts)
```

**One Model-Based round**:
```
1. Collect 256 real experiences
2. Train the world model for several steps (Replay Ratio for the world model ~ tens)
3. Imagine inside the world model: 50 starting points × 15 steps = 750 virtual experiences
4. The policy receives 750 gradient signals from virtual experiences
→ Real data is effectively "amplified" by hundreds to thousands of times
→ No overfitting — because virtual experiences are new samples "generated according to laws" by the world model,
   not repeated licking of the same real data
```

**Key comparison**:

| Metric | Model-Free (DQN/PPO) | Model-Based (Dreamer) |
|------|---------------------|---------------------|
| Real experience consumed | 1000 steps | 1000 steps |
| Gradient uses per real step | 1–20 (replay-ratio ceiling) | **World model ~ dozens; policy ~ hundreds to thousands** |
| imagined rollout length H | Not applicable | 15 |
| Number of imagined starting points (parallel) | Not applicable | 50 |
| **Total number of "training states" seen by the policy** | 1000–20,000 | **1000 × 50 × 15 = 750,000** |
| Overfitting risk | ❌ High replay ratio can collapse | ✅ Virtual data varies and is less prone to overfitting |

→ **With the same real-data consumption, the policy receives tens to thousands of times more training signal**.

**Why cannot Model-Free simply raise the replay ratio?**

Experiments in Andrychowicz 2020, D'Oro 2022, and related work show:
```
replay ratio = 1   → normal
replay ratio = 4   → slightly better
replay ratio = 16  → begins to decline
replay ratio = 64  → collapses (Q-value estimates become severely distorted)
```
**In model-free methods, "new data ↔ number of training steps" is fundamentally coupled**, producing a ceiling.

**Why can Model-Based break through?** The key is the **different generation mechanism**:
- Model-free repeatedly samples the same real data → like "licking the same piece of candy repeatedly" → overfitting
- Model-based uses the world model to generate new virtual data → like "using the candy recipe to make 1000 new candies" → every sample differs → no overfitting

**Why is virtual data effective?** As long as the world model is accurate enough, the dreamed `(ŝ, â, r̂, ŝ')` and real experiences have **consistent statistical distributions**; actor-critic cannot distinguish them. Dream data is nearly "free" (pure GPU matrix multiplication, microsecond scale).

#### Reason 3: The Dream Allows Arbitrary Resets and Free-Form Exploration

**First, a fundamental constraint: why can real environments only reset to the initial state?**

| Environment Type | Why Arbitrary Reset Is Impossible |
|---------|---------------------|
| **Real physical world** (robots/autonomous driving) | Physics is irreversible — there is no "undo key"; a shattered cup does not restore itself. One reset = manual human restoration + several seconds of waiting |
| **Games / simulators** (Gym/Doom) | Developers expose only `env.reset()`, which returns to a fixed initial state; internal state is too complex (thousands of variables), and no dump/restore API was designed |
| **Real software systems** (recommendation/search) | Want to reset to "rainy day + pedestrian crossing"? **Actual rain must occur** |

**By contrast, the dream = a collection of neural-network tensors**, which can be **assigned arbitrarily**:
```python
env_dream.z = z_target    # arbitrary starting point, no physical constraint
env_dream.h = h_target
```
There is no timer, no memory dependency, complete reversibility, and complete controllability — this is the **fundamental structural advantage** of a world model over the real environment.

**Several engineering workarounds that "pretend reset is possible"** (shown to clarify the advantage of the dream):
- Multiple parallel workers: can only start from states that are **naturally reached**
- Simulator snapshot (MuJoCo): supported, but restore is 10×+ slower than step, and **real robots do not support it**
- HER (Hindsight Replay): retrospectively relabels goals; it is not a real reset

**Scenario**: training an "edge-of-rollover vehicle recovery" task

| Step | Real Environment | Dream |
|------|---------|------|
| Reach the "edge of rollover" state | **Must actually drive there**, requiring hundreds of full episodes | **Directly select a rollover latent state as the starting point** |
| Try 1000 recovery strategies | Damage the vehicle 1000 times | Completed within 1 second |
| After failure | episode ends and the entire environment resets | **Return directly to the previous frame and retry** |

**Dreamer implementation**:
```python
# Randomly select 50 real states from the Replay Buffer as starting points
real_states = buffer.sample(batch_size=50)
h_0, z_0 = encoder(real_states)
# 50 starting points perform rollout fully in parallel
for t in range(15):
    a_t = actor(h_t, z_t)
    h_{t+1}, z_{t+1} = world_model(h_t, z_t, a_t)
```

**Core gap**:

| Operation | Real Environment | Dream |
|------|---------|------|
| Reset to any state | ❌ Mostly only reset to initial state | ✅ Any z is possible |
| Parallel multiple rollouts | ❌ Requires multiple instances and is expensive | ✅ GPU batch=1024 is still easy |
| "Undo" outcomes | ❌ Physics is irreversible | ✅ Reset latent |
| Start from an unseen "hypothetical state" | ❌ Impossible | ✅ Possible as long as it lies within the world-model distribution |

**Greatest benefit: Counterfactual reasoning**

> "What would have happened if the Agent had gone left?"

Model-free cannot answer (it was not actually tried); Model-based can **try it inside the dream** and obtain an answer within microseconds.

**Concrete analogy**:
- Training a student in the real environment = every attempt must begin with the first lesson of grade one; to practice the final college-entrance problem, **the entire high-school curriculum must be repeated first**
- Training a student in the dream = **jump to any problem at will**, and practice whichever problem is desired

→ The exploration cost in the real environment is mostly spent on **reaching the state of interest**, not on **learning how to handle it**. This is why the dream's "arbitrary reset" can yield an additional 2–10× improvement in sample efficiency.


#### Reason 4: Analytic Gradient Backpropagation (the Dreamer Family's Killer Feature)

**Model-Free Policy gradient (using REINFORCE as an example)**:
```
∇θ J = E[ R · ∇θ log π(a|s) ]
            ↑          ↑
        real reward  random sampling
```
`R` is affected by environmental randomness → the gradient is a **Monte Carlo estimate** with **very high variance** → N must be extremely large (thousands to tens of thousands of episodes) for stability.

**Model-Based + differentiable world model**:
```python
# The entire imagination chain consists of neural networks and is differentiable!
for t in range(H):
    a_t = actor(h_t, z_t)
    h_{t+1}, z_{t+1} = world_model(h_t, z_t, a_t)
    r_t = reward_model(h_t, z_t)
    total_value += γ**t * r_t

loss = -total_value
loss.backward()    # gradients backpropagate through reward → world_model → actor end-to-end
```

**Comparison**:

| Perspective | Model-Free | Model-Based |
|------|-----------|-------------|
| Gradient source | Sampling estimate $\nabla_\theta J \approx R \cdot \nabla \log \pi$ | **Analytic computation** $\nabla_\theta R = \frac{\partial R}{\partial a} \cdot \frac{\partial a}{\partial \theta}$ |
| Information per step | One scalar reward | All tensors (the total derivative of $R$) |
| Sample complexity | $O(1/\epsilon^2)$ | $\mathbf{O(1/\epsilon)}$ |
| Analogy | Guessing the direction of a mountain summit while blindfolded | **Using a compass to know the precise gradient direction** |

**Key technique: Reparameterization Trick (making randomness differentiable)**
```python
# ❌ Not differentiable (gradient is broken)
z = sample(Normal(μ, σ))
# ✅ Differentiable (gradients can backpropagate through μ and σ)
ε = sample(Normal(0, 1))
z = μ + σ * ε
```
This is a core technique shared by VAE, Dreamer, and Diffusion.

#### Reason 5: Long-Horizon Rollout / Imagination Is Possible in the Dream

**Model-Free evaluation of "long-term value"**:
```
1. Run the real environment for 1000 steps
2. Wait for the episode to end
3. Propagate cumulative return backward to each step
```

| Operation | Real Time Required |
|------|---------|
| 1 real step | 1ms ~ 1s |
| Complete a 1000-step episode | 1s ~ several minutes |
| Run 1000 episodes for stable estimation | several hours ~ several days |

**Model-Based evaluation of "long-term value"**:
```
1. rollout 15 steps in latent
2. Critic estimates the remaining residual value
3. λ-return = Σ γ^t · r_t + γ^H · V(s_H)
```

| Operation | Real Time Required |
|------|---------|
| 1 world-model step (GPU batch=50) | 0.1ms |
| Complete H=15 rollout steps | 1.5ms |
| Parallel 50 starting points | **still 1.5ms** |

→ **1.5ms of compute produces 50×15=750 steps of long-term signal**

**Why can "15 steps replace 1000 steps"?**

```
V_λ = γ^0·r_0 + γ^1·r_1 + ... + γ^14·r_14  +  γ^15·V(s_15)
       ↑                                          ↑
     the 15 imagined steps                    critic estimates the later "residual value"
```

As long as the critic's `V(s_15)` is reasonably accurate, **there is no need to actually rollout to 1000 steps** — this is **bootstrapping**.

| Method | rollout length | Why |
|------|--------------|--------|
| Monte Carlo | Full episode (1000) | Does not trust V; relies entirely on real rewards |
| Model-free TD (1-step) | 1 step | Fully trusts V; high bias |
| **Dreamer λ-return** | **15 steps** | **Sweet spot**: moderately trusts V + moderately uses real signal |

#### 📊 Summary Table of the Five Reasons

| # | Reason | Model-Free Method | Model-Based Method | Source of Efficiency Gain |
|:---:|------|----------------|----------------|------------|
| **1** | **Learning laws vs learning data points** | Q network stores "state→value" data points | World model stores the physical laws of "state+action→next state" | **Generalization** — can infer even for unseen states |
| **2** | **Data augmentation** | 1 real experience → 1 policy update | 1 real experience → train world model → hundreds/thousands of dream rollouts → hundreds/thousands of policy updates | **Training signal ×750+** |
| **3** | **Free-form exploration** | Must truly reach a state; failure = episode reset | Arbitrarily reset to any latent; failure = replay latent | **Zero-cost trial and error** |
| **4** | **Analytic gradient** | Policy gradient uses sampling, O(N) samples | The whole imagination chain is differentiable; exact gradient backpropagation, O(1) samples | **Variance elimination → exponential convergence acceleration** |
| **5** | **Long-horizon rollout** | 1000 real steps = actual time for 1000 steps | GPU 15 steps + critic estimates remaining value = 1.5ms | **Time compression** |

#### Rough Estimates of the "Efficiency Multipliers"

| Reason | Sample-efficiency improvement in the best case |
|------|-----------------------|
| 1. Learning laws → generalization | 5× ~ 50× |
| 2. Dream data augmentation | 10× ~ 100× |
| 3. Free-start exploration | 2× ~ 10× |
| 4. **Analytic gradient** | **100× ~ 1000×** (the most important source in the Dreamer family) |
| 5. Long-horizon rollout | 5× ~ 50× |
| **Total multiplier (product)** | **5,000× ~ hundreds of thousands×** in principle |

Empirically, Dreamer improves Atari by **10×~100×** and robotics by **1000×**, matching the estimated order of magnitude.

#### 💡 Intuitive Analogy — Learning to Drive

- 🔴 **Model-Free**: To learn driving in snow, **actual snow must occur**; to learn rollover recovery, **a real rollover must occur**
- 🟢 **Model-Based**: **Drive for 100 real hours to learn the laws of steering/braking/friction**, then **rehearse 10,000 corner cases in the mind**

#### Real Numerical Comparisons

| Task | Model-Free | Model-Based | Improvement |
|------|-----------|-------------|-----|
| Atari Breakout | DQN/Rainbow **200 million frames** | DreamerV3 **20 million frames** | 10× |
| Atari 100k | Rainbow performs poorly | EfficientZero approaches human level | Large |
| Crafter | PPO requires tens of millions of steps, ~10 score | DreamerV3 **1 million steps**, ~14 score SOTA | 30×+ |
| Real-robot grasping | PPO requires months of real-machine data | Dreamer-like methods require **hours** | 1000× |

#### Cost (No Free Lunch)

- ✅ Saves **real samples** (data)
- ❌ Spends **GPU compute** (training the world model + dreaming)
- ❌ **Engineering is more complex** and susceptible to model error (model exploitation)

→ **Real robots / autonomous driving** (expensive data): model-based decisively wins
→ **Atari / simulators / LLM RLHF** (cheap data): model-free is still usable

#### 🎯 In One Sentence

> **The high sample efficiency of Model-Based RL is not "one magic trick," but the compounding effect of five independent mechanisms: law generalization + data augmentation + free-form exploration + analytic gradients + long-horizon rollout. Among them, analytic gradient backpropagation is the Dreamer family's true killer feature — replacing high-variance Monte Carlo estimates with exact backpropagation is a qualitative leap.**

### Current Consensus

- **Cheap data** (simulators, games, LLM RLHF) → model-free remains mainstream
- **Expensive data / need for planning / need for imagination** (robotics, autonomous driving, Agent systems) → world model is the future

**In one sentence**: Model-Free RL does not learn the environment; it learns "what to do" purely by trial and error. It is simple and stable but sample-inefficient, so it is increasingly replaced by model-based / world model methods in real-world scenarios.

</details>

<details>
<summary><b>4.1 Essential Papers (in Order)</b></summary>

**Foundations**
1. [**World Models**](https://arxiv.org/abs/1803.10122) (Ha & Schmidhuber, 2018) — the classic starting point: VAE + MDN-RNN + small controller ([interactive website](https://worldmodels.github.io/))

   This paper is the **starting point and intellectual totem** of modern World Model research. Its influence does not come from overwhelming performance, but from the first clear demonstration that **an Agent can learn to play games inside its own "dream."**

   <p align="center">
     <img src="asset/world-models-2018/world_model_comic.jpeg" width="600"/><br/>
     <i>Opening example: the "mental model" from Scott McCloud's Understanding Comics</i>
   </p>

   ### 📖 Core Ideas

   #### Decomposing the Agent into Three Parts

   <p align="center">
     <img src="asset/world-models-2018/world_model_overview.png" width="700"/><br/>
     <i>Overall architecture: V (Vision) → M (Memory) → C (Controller)</i>
   </p>

   ```
      Observation ─►  V (Vision)  ─►  M (Memory)  ─►  C (Controller)  ─►  Action
                     compresses the present   predicts the future   decides (very small)
   ```

   | Module | Role | Implementation | Parameter Count |
   |------|------|------|--------|
   | **V** — Vision | Compress high-dimensional images into low-dimensional representations | **VAE** (variational autoencoder) | ~4M |
   | **M** — Memory | Learn temporal dynamics of the world and predict the next latent | **MDN-RNN** (mixture density network + LSTM) | ~400K |
   | **C** — Controller | Choose actions based on information from V and M | **Single-layer linear network** | ~1K |

   <p align="center">
     <img src="asset/world-models-2018/world_model_schematic.png" width="600"/><br/>
     <i>Internal Agent data flow: observation → z → action; h loops inside M</i>
   </p>

   🔑 **Key insight**: make "perception" and "memory" large models, and make "decision-making" **extremely small**. The decision-maker is small enough to be optimized by an **evolutionary algorithm (CMA-ES)** rather than backpropagation.

   #### Module Breakdown

   **V: VAE Compresses Vision**

   <p align="center">
     <img src="asset/world-models-2018/vae.png" width="600"/><br/>
     <i>VAE pipeline: image → encoder → latent z → decoder → reconstructed image</i>
   </p>

   - Input 64×64×3 game frames → output **32-dimensional latent `z`**
   - Frames are collected with a random policy, followed by self-supervised training (standard VAE: reconstruction + KL)

   **M: MDN-RNN Learns Dynamics**

   <p align="center">
     <img src="asset/world-models-2018/mdn_rnn_new.png" width="600"/><br/>
     <i>MDN-RNN: LSTM outputs parameters of a Gaussian mixture distribution, and sampling yields the next z</i>
   </p>

   **One forward pass of M**:
   ```
   Input:  (z_t, a_t, h_t)        ← current latent + action + previous LSTM hidden state
   Output:
     ① (π, μ, σ)                 ← Gaussian-mixture parameters of z_{t+1} (MDN component)
                                    after sampling, the next-frame latent is obtained: z_{t+1} ~ Σ π_k · N(μ_k, σ_k²)
     ② h_{t+1}                   ← new LSTM hidden state (used at the next step)
     ③ done_logit                ← probability of termination (after sigmoid)
   ```

   - Why a distribution? The real world is not fully predictable; **MDN (Gaussian mixture)** captures multimodal uncertainty
   - **Temperature τ** controls sampling randomness: higher τ makes the dream more chaotic; lower τ makes it more deterministic
   - The same MDN-RNN idea is also used in SketchRNN (predicting the next pen stroke):

     <img src="asset/world-models-2018/mp4_sketch_rnn_insect.gif" width="500"/>

   **C: Ultra-Small Controller**
   ```python
   a_t = W_c · [z_t, h_t] + b_c    # just one linear layer
   ```
   - **CMA-ES** is used for black-box optimization of a few hundred parameters; no backpropagation is required
   - Philosophical implication: **complex cognition can be delegated to the world model, while decision-making itself can be simple** (as in human driving)

   <p align="center">
     <img src="asset/world-models-2018/mccloud_baseball.jpeg" width="600"/><br/>
     <i>Analogy: a baseball batter reacts within milliseconds using an "internal predictive model," rather than explicit planning</i>
   </p>

   #### Training Pipeline (Three Stages, Fully Decoupled)

   World Models uses a **staged, non-end-to-end** training pipeline. Each stage is completed independently before moving to the next.

   **🗺️ Three-Stage Overview** (with core formulas):

   **Stage 1**: collect replay data from 10,000 episodes with random actions

   <p align="center"><img src="asset/formulas/f01.png" alt="formula"/></p>

   **Stage 2(a)**: train VAE (images only) → V

   <p align="center"><img src="asset/formulas/f02.png" alt="formula"/></p>

   **Stage 2(b)**: train MDN-RNN (sequences of z and a) → M

   <p align="center"><img src="asset/formulas/f03.png" alt="formula"/></p>

   **Stage 3**: freeze V and M; train Controller with CMA-ES

   <p align="center"><img src="asset/formulas/f04.png" alt="formula"/></p>

   **Stage 4** (Deployment / Inference): place the trained C back into the real environment

   <p align="center"><img src="asset/formulas/f05.png" alt="formula"/></p>

   The stages are explained in detail below.

   ##### Stage 1: Collect Real Data with a Random Policy

   **🎯 Objective**: expose the world model to as many diverse states as possible (including death, collision, and other edge cases), so a **random policy** is used rather than a strong policy.

   **Core formula**:
   <p align="center"><img src="asset/formulas/f06.png" alt="formula"/></p>

   That is, sample in the real environment under a uniformly random policy and collect (observation, action) sequences.

   **Concrete code**:
   ```python
   data = []
   for episode in range(10000):
       obs = env.reset()
       done = False
       while not done:
           a = env.action_space.sample()    # random action
           obs_next, reward, done = env.step(a)
           data.append((obs, a))            # store only observations and actions
           obs = obs_next
   ```

   - **Scale**: VizDoom collects ~10,000 episodes; each has several hundred frames → several million frames in total
   - **Storage**: VAE training only needs `obs`; M training needs `(obs, a)` sequences
   - **No reward is required**: Stage 1 is entirely independent of reward signals (a flexibility of the World Models paradigm)

   ##### Stage 2(a): Train VAE → Obtain V

   **🎯 Objective**: learn a **compression-reconstruction** model that compresses 64×64×3 pixels into a 32-dimensional latent z, used as input features for M and C.

   **Core formula** (VAE ELBO):
   <p align="center"><img src="asset/formulas/f07.png" alt="formula"/></p>

   - Encoder: `q(z|o) = N(μ_φ(o), σ_φ(o)²)` — encodes the image into a Gaussian distribution
   - Decoder: `p(o|z)` — reconstructs the image from z
   - **Result**: `encode: o → z` (32 dimensions) + `decode: z → o`

   **Concrete code**:
   ```python
   for epoch in range(N):
       for batch in shuffle(data):
           obs = batch.obs                  # 64×64×3 pixels
           mu, sigma = VAE.encoder(obs)     # output latent distribution parameters
           z = mu + sigma * randn()         # reparameterization
           obs_recon = VAE.decoder(z)       # reconstruct image

           loss = MSE(obs_recon, obs) + KL(mu, sigma)
           loss.backward()
   ```

   - **Purely unsupervised** — uses only obs and never uses action / reward
   - **Freeze V** — it is no longer updated in the next stage

   ##### Stage 2(b): Train MDN-RNN → Obtain M

   **🎯 Objective**: learn a **temporal prediction** model so that M can predict the **probability distribution of the next z** and whether the episode terminates from `(current z, current action, historical memory h)`.

   **Core formula**:
   <p align="center"><img src="asset/formulas/f08.png" alt="formula"/></p>

   The predicted distribution of z is a mixture of K Gaussians:
   <p align="center"><img src="asset/formulas/f09.png" alt="formula"/></p>

   - LSTM outputs `(π, μ, σ)` as mixture-distribution parameters
   - Training objective: maximize the likelihood of the real `z_{t+1}` under this distribution

   **Concrete code**:
   ```python
   # First use V to encode all obs into z sequences
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

   - **Freeze M** — it is no longer updated in the next stage

   ##### Stage 3: Train C with CMA-ES Inside the Dream

   **🎯 Objective**: train the Controller to learn a Policy that achieves high reward "inside the dream" — without touching the real environment, using only the virtual world formed by V+M. This is the method used for **VizDoom Take Cover** (CarRacing trains in the real environment, discussed below).

   **Core formula**:
   <p align="center"><img src="asset/formulas/f10.png" alt="formula"/></p>

   - Objective: find Controller parameters that maximize **cumulative reward in the dream**
   - `r_t = +1` (reward rule in VizDoom: +1 for each surviving frame)
   - Use **CMA-ES** (gradient-free black-box optimization) rather than backpropagation

   **Dream rollout function**:
   ```python
   def dream_rollout(controller_params):
       """Run one episode entirely inside M and return fitness"""
       z = sample_initial_z()           # draw a starting z from real data
       h = rnn.initial_state()
       cumulative_reward = 0
       while True:
           a = C_apply(controller_params, [z, h])         # ← compute action with candidate parameters
           (π, μ, σ), h, done_logit = M(z, a, h)           # ← M acts as the virtual environment
           z = sample_mdn(π, μ, σ, temperature=1.15)       # ← temperature prevents cheating
           if sigmoid(done_logit) > random():
               break
           cumulative_reward += 1                          # surviving one frame gives +1
       return cumulative_reward
   ```

   **CMA-ES evolutionary optimization loop**:
   ```python
   es = CMAES(initial_mean=zeros(C.param_count), sigma=0.1)
   for generation in range(800):
       # 1. CMA-ES generates a batch of candidate parameters (population_size=64)
       candidates = es.ask()
       # 2. Each candidate runs N dream episodes; fitness is averaged
       fitnesses = [
           mean([dream_rollout(c) for _ in range(16)])
           for c in candidates
       ]
       # 3. Feed fitness back to CMA-ES; it updates the distribution
       es.tell(candidates, fitnesses)

   best_C = es.best_solution()           # trained Controller
   ```

   - **Gradient-free**: CMA-ES is black-box optimization; it only observes fitness, not gradients
   - **Parallel-friendly**: 64 candidates can run dream episodes simultaneously (GPU batch)
   - **Repeated evaluation**: each candidate runs 16 rollouts and uses the mean, reducing noise from dream stochasticity

   <details>
   <summary><b>📌 Concept Supplement: CMA-ES Explained + Why Not Backpropagation / Bellman?</b></summary>

   **CMA-ES** = Covariance Matrix Adaptation Evolution Strategy, proposed by Nikolaus Hansen in 1996. It is one of the most successful evolutionary algorithms for **black-box continuous optimization**.

   > ⚠️ **Notation convention**: standard CMA-ES literature uses **C** for the covariance matrix, but in the World Models paper **C** is already taken as the symbol for the **Controller**. To avoid confusion, this section uses **Σ** (the standard symbol from probability/statistics) for the covariance matrix. So "Controller C" and "covariance Σ" are two completely different objects.

   ---

   ### Part 1: What Is CMA-ES? — The Principle in Three Sentences

   1. **Maintain a multivariate Gaussian distribution** $\mathcal{N}(m, \sigma^2 \Sigma)$ describing "where the currently estimated optimum is likely located"
   2. **Sample λ candidates each generation and select the best μ candidates** (μ ≈ λ/2)
   3. **Update mean m, covariance Σ, and step size σ**, so the distribution gradually "aims" at the optimal region

   **Analogy — finding a mountain summit while blindfolded**: scatter a group of people around the current location → have them report altitude → identify the direction of the highest few people → move the group in that direction → meanwhile adjust the scattering shape (ellipsoid) and range (step size).

   #### 🖼️ Intuitive View: How Does CMA-ES Converge?

   <p align="center">
     <img src="asset/cma-es/02_generations_evolution.png" width="900"/><br/>
     <i>Evolution of CMA-ES on the 2D objective function f(x,y) = −((x−3)² + 5(y+1)²). The green triangle is the true optimum (3, −1), the red star is the current mean m, the red ellipse is the current 2σ range of N(m, σ²Σ), white dots are sampled candidates, and yellow circles are the selected top-μ candidates. It converges reliably to the optimum within 20 generations.</i>
   </p>

   Observe:
   - **Generation 0**: m is at (0, 0); the ellipse is a circle (C = I), with a large range
   - **Generation 3**: m has already been "pulled" down and to the right (top-μ are in that direction), and the ellipse begins to flatten
   - **Generation 8**: m is close to the true optimum; the ellipse continues shrinking and becomes elongated (because the y-direction gradient is steeper)
   - **Generation 20**: nearly perfect convergence

   #### Five-Step Loop per Generation

   <p align="center">
     <img src="asset/cma-es/03_5step_loop.png" width="900"/><br/>
     <i>The five-step loop of each CMA-ES generation</i>
   </p>

   ```
   ① Sampling:   x_i = m + σ·B·D·z_i,  z_i ~ N(0, I)
   ② Evaluation: compute f(x_i)
   ③ Sorting:    sort by fitness and select the top μ
   ④ Mean update: m_new = Σ w_i · x_i
   ⑤ Update covariance Σ and step size σ (using evolution paths)
   ```

   Key hyperparameters: **λ** (population) = 16~64, **μ** = λ/2, initial **σ** = 0.1, number of generations = hundreds to thousands.

   #### 🔍 What Are B and D in Step ①?

   $B$ and $D$ are the **eigendecomposition** of covariance matrix $\Sigma$:
   <p align="center"><img src="asset/formulas/f12.png" alt="formula"/></p>

   - **B**: orthogonal matrix (eigenvectors of Σ) — geometrically a **rotation** that turns standard coordinate axes to the principal-axis directions of the Σ ellipsoid
   - **D**: diagonal matrix (square roots of Σ's eigenvalues) — geometrically **scaling along coordinate axes**

   **Why decompose Σ into B·D²·Bᵀ?** Because computers can only generate standard normal noise $z \sim \mathcal{N}(0, I)$; this noise must be transformed into samples following the $\mathcal{N}(m, \sigma^2 \Sigma)$ distribution. The figure below decomposes the full process into four intuitive steps:

   <p align="center">
     <img src="asset/cma-es/01_BD_decomposition.png" width="900"/><br/>
     <i>Geometric decomposition of the sampling formula x = m + σ·B·D·z: ① start from standard spherical noise z → ② D stretches it along coordinate axes into an ellipsoid → ③ B rotates it to the principal-axis direction of Σ → ④ σ scales it and translates it to position m. Blue dots are 200 samples; the red ellipse is the 2σ range.</i>
   </p>

   **Tip**: B and D are recomputed only once per generation after Σ is updated (`eigendecompose(Σ)`), then reused for all λ samples in that generation, which is computationally efficient.

   #### Adaptation of Covariance Σ (the Core of CMA)

   > ⚠️ **Clarifying a common confusion**: this subsection is about **how to update Σ**, which is **a different step** from the earlier "`Σ = B·D²·Bᵀ` eigendecomposition":
   > - **Sampling phase** (per-generation steps ①②): extract B, D from Σ, and use `x = m + σ·B·D·z` to generate candidates
   > - **Update phase** (per-generation step ⑤, this subsection): use the feedback from the current generation to **modify Σ itself**
   > - The two phases connect sequentially: use the old Σ's B, D to sample → evaluate → update Σ → next generation decomposes the new Σ

   CMA-ES does not update Σ arbitrarily. Instead, it collects **two independent pieces of evidence** and combines them to make a small adjustment to Σ.

   ##### Signal 1: Rank-μ Update — "Where are the top-μ candidates of this generation concentrated?"

   **Intuition**: Look at the μ best candidates selected in the current generation. In which direction are they concentrated? Make Σ wider along that direction.

   **Math**:
   <p align="center"><img src="asset/cma-es/06_rank_mu_formula.png" alt="rank-mu" width="450"/></p>

   - $x_i$: the i-th top candidate
   - $(x_i - m)(x_i - m)^\top$: **outer product**, turning a direction into a matrix
   - $w_i$: rank weight (highest for top-1, decreasing)

   ##### Signal 2: Rank-1 Update — "In which direction has the mean been moving historically?"

   **Intuition**: Beyond the current generation, also look at the **accumulated direction of historical mean movement** (evolution path $p_c$). If several consecutive generations move in the same direction, this is a strong signal → reinforce Σ along that long-term direction.

   **Math** — first maintain the evolution path (exponential moving average):
   <p align="center"><img src="asset/cma-es/07_pc_formula.png" alt="pc-update" width="500"/></p>

   Then take its outer product as C's contribution:
   <p align="center"><img src="asset/cma-es/08_rank1_formula.png" alt="rank-1" width="280"/></p>

   ##### The Two Signals Are Complementary

   | Signal | Pros | Cons |
   |--------|------|------|
   | **Rank-μ** | Uses μ samples, **rich information / good for width** | High per-generation noise, can chase randomness |
   | **Rank-1** | **Historical accumulation, smooth and stable** | Uses only 1 direction (the evolution path), limited width info |

   → **Combined**: Rank-μ provides "width", Rank-1 provides "long-term directional stability"; together they complement each other.

   ##### 🖼️ Geometric Meaning of the Two Signals

   <p align="center">
     <img src="asset/cma-es/04_rank_mu_rank_1.png" width="900"/><br/>
     <i>① Left: Rank-μ uses the sample covariance of top-μ candidates (yellow circles) to construct an ellipse (blue), making Σ wider along that concentration direction; ② Middle: Rank-1 accumulates historical mean movements m₀ → m₅ into the evolution path p_c (thick red arrow); its outer product yields a "rod-shaped" contribution along that direction; ③ Right: new Σ (thick green) = old Σ (dashed) + Rank-μ (blue dotted) + Rank-1 (red dash-dotted), weighted fusion of all three.</i>
   </p>

   ##### Full Update Formula for Σ

   <p align="center"><img src="asset/formulas/f13.png" alt="Σ update formula"/></p>

   - First term $(1 - c_1 - c_\mu) \Sigma$: **preserves most of the old Σ** (prevents drastic oscillations)
   - Second term $c_1 \cdot p_c p_c^\top$: Rank-1 contribution
   - Third term $c_\mu \cdot \sum w_i (x_i - m)(x_i - m)^\top$: Rank-μ contribution
   - $c_1, c_\mu$ are small weights (typically on the order of 0.01), ensuring the sum remains positive-definite

   ##### 🖼️ Complete Per-Generation 6-Step Flow

   Connecting the "sampling" and "update" phases, CMA-ES actually has 6 steps per generation (the earlier 5-step diagram was a simplification; here is the complete version):

   <p align="center">
     <img src="asset/cma-es/05_6step_loop.png" width="950"/><br/>
     <i>Full per-generation flow: ① Eigendecompose Σ → obtain B, D ② Use B, D to sample λ candidates ③ Evaluate and rank ④ Update mean m and evolution path p_c ⑤ Use Rank-μ + Rank-1 to update Σ ⑥ Update global step size σ. The next generation returns to ① and decomposes the new Σ.</i>
   </p>

   **Key insight**: **"the B, D for sampling" and "the Σ being updated" are two faces of the same matrix** — the update phase modifies Σ itself, and the next generation's sampling phase extracts B, D from the new Σ for candidate generation. `Σ = B·D²·Bᵀ` is a "translation tool", whereas `Σ ← ...` is the actual "learning behavior".

   ---

   ### Part 2: Why Did World Models Choose CMA-ES? (Clarifying a Common Misunderstanding)

   #### ⚠️ Misunderstanding: "The dream is not differentiable"

   Strictly speaking, **the dream can be made fully differentiable mathematically**:

   | Component | Differentiability |
   |------|-------|
   | C (linear Controller) | ✅ differentiable |
   | LSTM part of M | ✅ differentiable |
   | MDN output layer (MLP) | ✅ differentiable |
   | **Sampling z from MDN** | ⚠️ Not differentiable by default; **reparameterization can make it differentiable** (as shown by VAE) |
   | **done sampling** | ⚠️ Bernoulli is not differentiable by default; **Gumbel-Softmax can make it differentiable** |

   **Conclusion**: Ha 2018 chose CMA-ES **not because differentiability was impossible, but as an engineering trade-off** — choosing CMA-ES naturally removes the need to make the entire chain differentiable.

   #### ✅ Real Reason: Five Conditions Fit CMA-ES Perfectly

   | Condition | Actual Situation in World Models Stage 3 | This Means... |
   |------|------------------------------|----------|
   | **Parameter count of C** | Extremely small (hundreds to thousands) | Under ~100 dimensions, black-box search is sufficient and gradients have limited advantage |
   | **Dream stochasticity** | MDN sample + τ=1.15, high fitness noise | Gradient algorithms suffer from noise; evolutionary algorithms are naturally noise-resistant |
   | **Model exploitation** | C searches for dream bugs to exploit | **Gradients amplify cheating** (they directly reveal how C can exploit loopholes optimally) |
   | **Long-sequence RNN gradients** | One episode may contain hundreds of frames | Exploding/vanishing gradients; LSTM only mitigates the problem |
   | **Engineering simplicity** | The 2018 goal was to "first demonstrate feasibility" | CMA-ES requires only a few lines of code |

   → **This is the true motivation for Ha 2018 choosing CMA-ES**, not a technical limitation.

   ---

   ### Part 3: Can the Bellman Equation Be Used for Backward Solution?

   A common confusion must first be clarified:

   #### ⚠️ The Bellman equation is a Q-learning tool, not an actor tool

   ```
   Bellman: Q(s,a) = r + γ · max_{a'} Q(s', a')
   ```

   It is used to **learn the value function Q**, not to learn the Policy directly. Concretely:

   | Algorithm | What Bellman Is Used For |
   |------|------------------|
   | **DQN** (model-free) | Uses Bellman error as the loss for the Q network; argmax Q selects actions |
   | **MuZero** (model-based) | Uses Bellman to train Q; Policy is obtained through MCTS search |
   | **Dreamer V1/V2/V3** | ⭐ **Does not use Bellman**; it fits the critic with λ-return + uses analytic gradient backpropagation for the actor |

   #### What if Bellman were forced into World Models?

   **Option A: Change C into a Q network**
   - This becomes "model-based DQN": learn $Q(z, h, a)$ and select actions by argmax
   - But CarRacing has **continuous actions**, making `max Q(s', a')` difficult to compute
   - Moreover, the training target is fitting Q rather than directly maximizing reward, adding an indirect layer

   **Option B: Make the dream differentiable + let the actor directly maximize imagined return** ← the path taken by Dreamer
   - No Bellman; **backpropagate directly through ∂Return/∂θ_actor**
   - This is the more modern and more efficient method

   → **The idea of Option B** (differentiable dream + backpropagation) is exactly the path implemented by Dreamer in 2020.

   ---

   ### Part 4: How Dreamer Implements "Differentiable Dream + Backpropagation" (Later Evolution)

   ```
   World Models (2018)               Dreamer V1 (2020)
   ─────────────────────             ──────────────────
   V (VAE) + M (MDN-RNN) trained in stages → V + M merged into RSSM, end-to-end
   Tiny C + CMA-ES                 →  actor + critic (hundreds of thousands of parameters each)
   Dream not intentionally differentiable → ⭐ make the dream fully differentiable + backpropagation
   No critic                       →  ⭐ critic fits λ-return and provides the actor target
   ```

   **Core training loop of Dreamer V1**:
   ```python
   # rollout in the dream (H=15 steps)
   s = sample_initial_state()
   returns = 0
   for t in range(H):
       a = actor(s)                            # actor network outputs action
       s_next = world_model.transition(s, a)   # ✅ differentiable transition
       r = world_model.reward(s_next)          # ✅ differentiable reward
       returns += γ**t * r
   returns += γ**H * critic(s_H)               # critic estimates subsequent residual value

   # ⭐ backpropagate directly to actor (no Bellman, no sampling estimate)
   actor_loss = -returns.mean()
   actor_loss.backward()
   ```

   Key difference: **Bellman error is not used**; instead, **analytic gradient ∂Return/∂θ_actor** directly maximizes imagined return.

   ---

   ### Part 5: CMA-ES vs Backpropagation (Summary Comparison)

   | Dimension | CMA-ES (World Models) | Backpropagation (Dreamer) |
   |------|---------------------|------------------|
   | Requires gradients? | ❌ No | ✅ Must be differentiable |
   | Suitable parameter count | Hundreds ~ thousands | Arbitrarily large (hundreds of millions) |
   | Information utilization | λ × M evaluations per generation | One forward pass + backprop obtains the full gradient |
   | Convergence speed | Slow | Fast (dense gradient information) |
   | Robustness (noise) | Strong (selection rather than averaging) | Weak (noise enters gradients directly) |
   | model exploitation risk | Medium (only sees fitness) | High (gradients directly exploit loopholes) |
   | Suitable setting | Small black-box networks | Large differentiable networks |

   **The 2018 → 2020 turning point**: Dreamer made the chain differentiable and enlarged actor parameters → backpropagation became far more efficient than CMA-ES → **CMA-ES exited the historical stage of model-based RL**.

   ---

   ### Part 6: Practical Entry Point

   ```python
   pip install cma
   import cma

   def rosenbrock(x):
       return sum(100*(x[i+1] - x[i]**2)**2 + (1 - x[i])**2 for i in range(len(x)-1))

   es = cma.CMAEvolutionStrategy(x0=[0.0]*10, sigma0=0.5, inopts={'popsize': 30})
   es.optimize(rosenbrock)
   print(es.result.xbest)
   ```

   Alternatively, use Ha's own [**estool**](https://github.com/hardmaru/estool) — the official evolutionary toolkit for the World Models paper, including CMA-ES, OpenAI ES, PEPG, and others.

   **Recommended resources**:
   - [pycma official documentation](https://github.com/CMA-ES/pycma) — includes visualization and tutorials
   - [Hansen — CMA-ES Tutorial](https://arxiv.org/abs/1604.00772) — written by the original author; essential reading
   - [David Ha — Visual Guide to Evolution Strategies](https://blog.otoro.net/2017/10/29/visual-evolution-strategies/) ⭐ — beautifully visualized explanation
   - [OpenAI ES paper (Salimans 2017)](https://arxiv.org/abs/1703.03864) — large-scale ES experiments on Atari

   ---

   ### 🎯 Overall Summary

   > **The dream is technically fully differentiable, but Ha 2018 chose CMA-ES as an engineering trade-off: the Controller is tiny, the dream is noisy, model exploitation might be amplified by gradients, long RNN gradients are difficult, and demo feasibility was the priority. The Bellman equation is a Q-learning tool, not the best choice for actor optimization; the true paradigm of "differentiable dream + backpropagated actor" was implemented by Dreamer 2020, after which CMA-ES receded from model-based RL. The intuition of "solving with gradients" is exactly the core idea of the Dreamer family — but it uses policy gradient rather than Bellman.**

   </details>

   ##### Stage 4: Deployment / Inference (Validation in the Real Environment)

   **🎯 Objective**: run the trained C in the real environment and test whether transfer succeeds. At this stage, **V and M are no longer updated, but they continue to be used online** (V provides perceptual compression; M provides temporal memory h).

   **Core formula**:
   <p align="center"><img src="asset/formulas/f11.png" alt="formula"/></p>

   - Note: **real $z_t$** is used to update $h$ (not the sampled $\hat{z}$ from M)
   - This is equivalent to M "running alongside" the real environment and maintaining expectations about the future

   **Concrete code** (paper Algorithm 1):
   ```python
   def rollout(controller):
       """Run one episode in the real environment; used both for evaluation and actual deployment"""
       obs = env.reset()                      # ← real environment!
       h = rnn.initial_state()
       done = False
       cumulative_reward = 0
       while not done:
           z = vae.encode(obs)                # real obs → z
           a = controller.action([z, h])      # C decides
           obs, reward, done = env.step(a)    # real environment advances
           cumulative_reward += reward
           h = rnn.forward([a, z, h])         # ⭐ update h with real z
                                              # (rather than the ẑ sampled from M)
       return cumulative_reward
   ```

   **Two key details**:
   1. **`obs` comes from the real environment** (`env.step`, not `M(...)`) — during deployment, the Controller sees the real game
   2. **`h` is still maintained by M**, but its input uses **real z** (not sampled ẑ)
      - C receives `[real z, h maintained by M]`, meaning it perceives the present and has "memory/expectation"

   **Dream rollout vs real rollout**:

   | Step | Dream rollout (when training C) | Real rollout (deployment / CarRacing training) |
   |------|------------------------|--------------------------------------|
   | Where does obs come from? | No obs needed; directly operate on z | `env.reset()` / `env.step()` |
   | Where does z come from? | `sample_mdn(M output)` (virtual) | `vae.encode(real_obs)` (real) |
   | h update | Updated inside M's LSTM | The same M via `rnn.forward([a, z, h])` |
   | reward | Derived from done_logit +1 | Returned by `env.step` |
   | Purpose | CMA-ES evolutionary fitness | Evaluation / actual gameplay |

   ✨ **Key insight**: V and M are **still used during deployment**, not merely as training auxiliaries. At inference time, they perform "perceptual compression + temporal memory," enabling the tiny C to make good decisions.

   ##### CarRacing Special Case: Training C in the Real Environment

   Because CarRacing has complex rewards, the **Controller was not trained inside the dream**:

   ```python
   # Directly use the same rollout() function to evaluate fitness
   # Only difference: env is the real CarRacing environment
   es = CMAES(...)
   for gen in range(N):
       candidates = es.ask()
       fitnesses = [rollout(C_apply(c)) for c in candidates]   # use real env!
       es.tell(candidates, fitnesses)
   ```

   - V and M are still trained in Stage 2 (using random rollout data)
   - But C is trained directly in real CarRacing, using `[z, h]` as C's input (improving score by 40% compared with z alone)

   ##### Advantages and Disadvantages of Three-Stage Independent Training

   ✅ **Advantages**:
   - Simple and clear; each stage can be debugged independently
   - V and M are trained on unlabeled data, substantially reducing the need for real-environment interaction
   - C is extremely small (hundreds of parameters), CMA-ES can solve it, and **no backpropagation is needed**

   ❌ **Disadvantages** (later addressed by Dreamer):
   - Features learned by V are **not necessarily optimal for decision-making** (only for reconstructing obs)
   - Independent three-stage training → no joint optimization
   - Random rollout data in Stage 1 **may not cover critical states** (the iterative training issue mentioned in Section 5 of the paper)

   → These limitations directly led to **PlaNet's end-to-end training** and Dreamer's **imagination + backpropagation** route.

   ✨ Three modules are trained independently and do not rely on shared gradients — a distinctive 2018 design.

   ### 🧪 Key Experiments

   #### Learning to Play Doom Inside the Dream

   **CarRacing-v0**: the first method to solve the task (score > 900; previous best ~600).

   🎬 **CarRacing demo video**:

   <img src="asset/world-models-2018/mp4_carracing_z_only.gif" width="600"/>

   **VizDoom: Take Cover — the soul of the paper**: the Agent is trained **entirely inside M, without touching the real environment**.

   🎬 **Doom real-environment demo**:

   <img src="asset/world-models-2018/mp4_doom_real.gif" width="600"/>

   1. Run a random policy in the real environment to collect data
   2. Train V and M
   3. Treat M as the "dream environment"; the Controller **has never seen the real game**
   4. Deploy the trained Controller directly into real Doom — **it can play, reaching the completion threshold of 750 surviving frames**

   🤯 **This was the first clear historical demonstration that an Agent can learn inside its own world model and transfer to the real environment** — the core paradigm of today's model-based RL.

   > 💡 For full interactive demos (VAE reconstruction, real-time Doom dream generation), visit the official website: <https://worldmodels.github.io/>

   **Interesting "cheating" behavior**: the Agent learned to exploit dream bugs (making fireballs disappear out of nowhere). The authors **increased τ to make the dream harder**, forcing a robust Policy. This foreshadowed a later central challenge: **model exploitation** (Policies exploiting model errors).

   ### 🔧 Implementation Details Deep-Dive

   This section clarifies three engineering details that are **particularly easy to confuse**; understanding them is necessary for a precise understanding of World Models.

   ---

   ##### Detail ①: The Real Structural Difference Between World Model and Model-Free

   Common misunderstanding: "World Model merely adds an M network, and the Controller receives the predicted state."
   **Reality**: the difference has **four layers**, and the most important one is not network structure.

   | Dimension | Model-Free (DQN) | World Models (Ha 2018) |
   |------|------------------|----------------------|
   | **① Number of network modules** | 1 (Q network) | **3** (V + M + C) |
   | **② Controller input** | Raw observation $o_t$ (or stacked frames) | $[z_t, h_t]$ — compressed observation + RNN hidden state |
   | **③ Source of Controller training data** | **Real-environment `(s, a, r, s')`** | **Virtual sequences generated by M inside the dream** ⭐ the real revolution |
   | **④ Optimization method** | Gradient descent + Bellman error | **CMA-ES** (evolutionary algorithm) |

   **Data-flow comparison**:

   First examine the **input and output of Q-net** (the basis for understanding DQN):

   ```mermaid
   flowchart LR
       obs["obs<br/>(84×84×4 pixels)"] --> Qnet["Q Network<br/>(CNN + MLP)"]
       Qnet --> Qvals["Q-value vector<br/>[q₁, q₂, ..., qₙ]"]
       Qvals --> argmax["argmax"]
       argmax --> action["action<br/>(e.g., FIRE)"]
   ```

   Q-net **learns only one thing** — "the expected total reward of each action under the current obs." **It never predicts the next frame.**

   **Complete DQN data flow**:

   ```mermaid
   flowchart TD
       Env["Real environment Env"] -->|obs| QNet["Q Network"]
       QNet --> Qvals["[Q-value × N actions]"]
       Qvals -->|argmax| action
       action --> step["env.step(a)"]
       step -->|"obs', r, done"| Buffer["Replay Buffer<br/>store (s, a, r, s')"]
       Buffer -->|sample batch| Loss["TD Loss (Bellman):<br/>y = r + γ · max Q(s')<br/>L = MSE(Q(s).gather(a), y)"]
       Loss -->|backward| Update["Update Q net parameters"]
       Update -.->|next step| QNet
   ```

   **Characteristic**: **one network; all data flows through the real environment**.

   **Complete World Models data flow** (four stages):

   ```mermaid
   flowchart TD
       subgraph S1["Stage 1: Collect real data (run once)"]
           Env1["Real environment"] -->|obs| Random["Random Policy"]
           Random -->|a| Step1["env.step(a)"]
           Step1 -->|"(obs, a) sequences<br/>10,000 episodes"| Data["Replay data"]
       end

       subgraph S2["Stage 2: Train world model (V and M)"]
           Data --> V["V (VAE)<br/>obs → z (32D)"]
           Data --> M["M (MDN-RNN)<br/>(z_t, a_t, h_t) →<br/>z_{t+1} distribution + h_{t+1} + done"]
       end

       subgraph S3["Stage 3: Train Controller inside the dream (no real environment)"]
           Init["initial: z₀, h₀"] --> State["(z_t, h_t)"]
           State --> C["C (linear)<br/>a = W·[z,h] + b"]
           C -->|a_t| MDream["M (virtual environment)<br/>outputs z', h', done"]
           MDream -->|"if done: break<br/>else: total_reward += 1"| State
           MDream -.->|fitness| CMAES["CMA-ES<br/>(evolutionary algorithm)<br/>optimizes C parameters"]
       end

       subgraph S4["Stage 4: Deploy to the real environment for validation"]
           Env4["Real environment"] -->|obs| V2["V"]
           V2 -->|z| C2["Controller"]
           M2["M (provides h)"] -.->|h| C2
           C2 -->|a| Env4
       end

       S1 --> S2
       S2 --> S3
       S3 --> S4
   ```

   **Core insight**: **where the Controller is trained (dream vs real environment)** is the soul of the World Model paradigm, not "having one additional M network."

   ---

   ##### Detail ②: Precise Distinction Among the Three "State" Concepts z, h, and o

   World Models contains three related vectors with entirely different roles, which are easy to confuse:

   | Symbol | Name | Source | Dimension (VizDoom) | Role |
   |------|------|------|---------------|------|
   | $o_t$ | **Observation** | Image provided by the real environment | 64×64×3 | Visible signal from the real world |
   | $z_t$ | **Latent** (latent variable) | VAE compresses $o_t$ | 64 | **"Compressed representation of the current frame"** (space) |
   | $h_t$ | **RNN Hidden State** | Maintained inside M (LSTM) | 256 | Summary of **"history + future expectation"** (time) |

   **Key distinction**:
   - $z$ ≈ looking at a single photograph — only indicates what the scene looks like
   - $h$ ≈ watching the first 5 seconds of a video — enables prediction of what will happen in the next second
   - **Only the combination $(z, h)$ supports correct decisions**

   **Complete one-step transition in the dream**:
   ```
   (z_t, h_t, a_t) ──[M]──► (z_{t+1}, h_{t+1})
                             │           │
                        MDN sample     LSTM update
   ```

   M **outputs two things simultaneously**:
   1. A Gaussian-mixture distribution over $z_{t+1}$ (the compressed next-frame representation obtained via MDN sampling)
   2. $h_{t+1}$ (the new memory vector naturally updated inside LSTM)

   **Key ablation experiment in the paper** (CarRacing):

   | Controller Input | Score |
   |-----------------|---:|
   | $z$ only | 632 ± 251 |
   | **$z + h$** | **906 ± 21** ⭐ |

   → Adding $h$ substantially improves performance, proving that $h$ carries "dynamical information" absent from $z$. **This two-path $(z, h)$ design was directly inherited by RSSM in the Dreamer family**.

   ---

   ##### Detail ③: How Is Reward $\hat{r}_{t+1}$ Generated Inside the Dream?

   This is a **particularly counterintuitive point** — intuition suggests that M should predict reward, but **World Models 2018 did not explicitly predict continuous reward at all on VizDoom**.

   **Actual method in VizDoom Take Cover**:
   ```python
   # Output of M
   M(z_t, a_t, h_t) → (π, μ, σ), h_{t+1}, done_logit
                          ↑           ↑          ↑
                     distribution of next z   hidden state  probability of termination
   # Note: no reward head!
   ```

   **Reward is entirely derived implicitly from `done`** (because Take Cover has a very simple rule: surviving gives +1):
   ```python
   total_reward = 0
   while True:
       a = C([z, h])
       (π, μ, σ), h, done_logit = M(z, a, h)
       z = sample_mdn(π, μ, σ, temperature=1.15)
       if sigmoid(done_logit) > random():
           break              # dead, stop
       total_reward += 1      # still alive, reward implicitly +1
   ```

   **CarRacing uses a more "compromised" treatment** (complex rewards make dream training ineffective):
   - The **Controller was not trained inside the dream**
   - Instead, after V+M were trained, C was trained **directly in the real environment** with CMA-ES using z+h as features

   | Task | Train C inside the dream? | Where does reward come from? |
   |------|-----------|----------------|
   | **VizDoom Take Cover** | ✅ Entirely trained inside the dream | Derived from done as +1 |
   | **CarRacing** | ❌ Trained in the real environment | Provided by the real environment |

   → **The most spectacular paradigm, "learning inside the dream," was fully demonstrated by Ha 2018 only on VizDoom, whose reward rule is extremely simple**. This is an **easily overlooked limitation** of the paper.

   **How the Dreamer family upgrades this**: add a **reward head** (MLP) to explicitly predict continuous reward:

   ```python
   # Dreamer's World Model output
   RSSM(s_t, a_t) → s_{t+1}, r̂_{t+1}, done
                        ↑          ↑          ↑
                    next state  predicted reward  termination

   # Training: supervise the reward head with real experiences
   loss_reward = MSE(reward_head(s_pred), batch.real_reward)

   # During dream rollout, accumulate r̂
   for t in range(H=15):
       a = actor(s)
       s, r_hat, done = world_model.step(s, a)
       total_value += γ**t * r_hat   # use r̂ to accumulate return
   ```

   → This is the key upgrade that enables Dreamer to handle **general tasks** (DMC, Atari, Minecraft): **reward is no longer derived from done, but explicitly modeled**.

   ---

   ##### Relationship Among the Three Details

   ```
   ① Structural difference ─► Controller trained inside the dream (the soul)
                               │
                               ▼
   ② z + h dual pathway ─► lets the Controller observe the full "space + time" state
                               │
                               ▼
   ③ Reward handling ─► implicit from done (VizDoom) or explicit reward head (Dreamer)
   ```

   After these three layers of detail are understood, it becomes possible to:
   - Understand why RSSM in the Dreamer papers uses a dual `(h, z)` pathway
   - Understand why Dreamer must add a reward head to scale to general tasks
   - Avoid mistaking "World Model" for "just model-free with multiple networks"

   ### 💭 Reflections

   #### Contributions and Historical Status

   ✅ **Contributions**
   1. First systematic engineering of the World Model paradigm (decoupling V+M+C)
   2. First demonstration that a policy trained purely in a latent dream can transfer to the real environment
   3. Probabilistic world model (MDN) foreshadowed today's stochastic generative models
   4. Elegant combination of evolutionary algorithms and neural networks
   5. Strong visualization and narrative, attracting many researchers to the field

   ⚠️ **Limitations**
   1. Three-stage independent training; features learned by V may not be optimal for decision-making (only for reconstruction)
   2. CarRacing / Doom are relatively simple
   3. MDN-RNN has limited capacity, and long-horizon prediction drifts
   4. Once V is trained, it is frozen and cannot adapt online

   🌳 **Subsequent Influence**
   - **PlaNet (2019)**: merges V and M into RSSM and trains end-to-end
   - **Dreamer v1/v2/v3**: performs actor-critic in latent, replacing evolution
   - **DreamerV3**: solves 150+ tasks with one set of hyperparameters, including Minecraft diamond collection
   - **DIAMOND / Genie / Sora**: replace M with diffusion / transformer

   The Dreamer family is a direct descendant of this paper.

   #### Reading Suggestions

   1. **Start with the interactive website** <https://worldmodels.github.io/> (all demos are animated and faster than reading the paper)
   2. The paper is short (~25 pages), but the **appendix is extremely detailed** and worth careful reading
   3. Focus on: VAE latent dimensionality comparisons, the role of MDN-RNN temperature τ, and the methodology of "training inside the dream"
   4. Code: [estool](https://github.com/hardmaru/estool) · [WorldModelsExperiments](https://github.com/hardmaru/WorldModelsExperiments)

   #### In One Sentence

   > **This paper first turned "an Agent learning through imagination" from philosophy into a reproducible algorithm. Every module has since been replaced by later work, but the perception–memory–decision triad still dominates the entire model-based RL / world model field.**

   <details>
   <summary><b>📚 Learning Resources (Expand)</b></summary>

   **🎬 Video Explanations**

   By the author:
   - [**David Ha — NeurIPS 2018 Talk**](https://youtu.be/HzA8LRqhujk) ⭐ — presented by the first author, ~30 minutes, highest information density; **strongly recommended as the first video**
   - David Ha also has Stanford and workshop versions; searching YouTube for "David Ha World Models" will find them

   Third-party explanations:
   - [**Two Minute Papers — "Google's New Dreaming AI"**](https://www.youtube.com/results?search_query=two+minute+papers+world+models) — 5-minute popular explanation for intuition
   - [**Arxiv Insights — World Models**](https://www.youtube.com/results?search_query=arxiv+insights+world+models) — roughly 10 minutes, clear explanation
   - [**Yannic Kilcher channel**](https://www.youtube.com/@YannicKilcher) — search "World Models" for a line-by-line paper walkthrough

   **📝 English Text-and-Figure Explanations**

   - [**Official interactive website**](https://worldmodels.github.io/) ⭐ — **best introductory resource**; all demos are animated and far more intuitive than the PDF
   - [**Lilian Weng — RL surveys and related posts** (Lil'Log)](https://lilianweng.github.io/tags/reinforcement-learning/) — RL tag page covering policy gradient, exploration, meta-RL, etc.; model-based content appears across surveys and [A (Long) Peek into RL](https://lilianweng.github.io/posts/2018-02-19-rl-overview/)
   - [**The Gradient**](https://thegradient.pub/) — situates World Models within a broader AI narrative

   **📝 Chinese Explanations**

   - **Machine Heart**: [search "World Models Great Dreamer"](https://www.jiqizhixin.com/search?keywords=World%20Models) — detailed Chinese coverage was published when the paper appeared
   - **PaperWeekly**: WeChat account paperweekly; search "World Models" for a paper guide
   - **Zhihu**:
     - Search "World Models Ha Schmidhuber" — multiple highly liked explanations
     - Search "learning in dreams" / "world model survey" for additional useful notes
   - **Bilibili**: search "World Models paper close reading" and the "Mu Li reinforcement learning" series for related content
   - **CSDN / Jianshu**: many paper notes exist; quality varies, so prioritize posts with >100 saves

   **💻 Code and Reproduction**

   - [**hardmaru/WorldModelsExperiments**](https://github.com/hardmaru/WorldModelsExperiments) — official implementation by the authors (TensorFlow; complete but older)
   - [**hardmaru/estool**](https://github.com/hardmaru/estool) — CMA-ES implementation (used for Controller training)
   - [**ctallec/world-models**](https://github.com/ctallec/world-models) ⭐ — **PyTorch reproduction** with clean code, recommended for study
   - [**zacwellmer/WorldModels**](https://github.com/zacwellmer/WorldModels) — another concise PyTorch version

   **🎓 Courses**

   - [**UC Berkeley CS 285: Deep RL**](https://rail.eecs.berkeley.edu/deeprlcourse/) — Sergey Levine, model-based RL lectures
   - [**DeepMind x UCL RL Course**](https://www.deepmind.com/learning-resources/reinforcement-learning-lecture-series-2021) — model-based RL module
   - [**Stanford CS 234: RL**](https://web.stanford.edu/class/cs234/)

   **📚 Further Reading**

   Prehistory (intellectual origins in Schmidhuber's 1990s work):
   - [Schmidhuber 1990 — *Making the World Differentiable*](http://people.idsia.ch/~juergen/FKI-126-90ocr.pdf)
   - [Schmidhuber 1991 — *Curious Model-Building Control Systems*](http://people.idsia.ch/~juergen/curiositysab/curiositysab.html)

   Subsequent work (read immediately after World Models):
   - [PlaNet](https://arxiv.org/abs/1811.04551) — end-to-end version
   - [DreamerV3](https://arxiv.org/abs/2301.04104) — synthesis and strongest baseline

   **🎯 Recommended Learning Order**

   ```
   1. Browse worldmodels.github.io first       (1 hour, intuitive experience)
   2. Watch David Ha NeurIPS 2018 talk         (30 minutes, author's perspective)
   3. Read Lil'Log [RL Overview](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) (1 hour, mathematical organization)
   4. Run the ctallec/world-models code once   (half a day to one day, hands-on)
   5. Read the full paper + appendix           (1 day, details)
   6. Move on to PlaNet / DreamerV3            (understand the evolution)
   ```

   </details>

   > 📁 Supporting materials have been downloaded to `asset/world-models-2018/` (architecture diagrams, VAE/MDN-RNN diagrams, CarRacing & Doom demo videos). Image source: [worldmodels.github.io](https://worldmodels.github.io/), © Ha & Schmidhuber, 2018, for study reference only.

2. [**PlaNet**](https://arxiv.org/abs/1811.04551) (2019) — latent dynamics for planning
3. **Dreamer v1/v2/v3** (2020–2023) — currently the strongest baseline in the RL school; **v3 is essential reading**
   - [DreamerV1](https://arxiv.org/abs/1912.01603) · [DreamerV2](https://arxiv.org/abs/2010.02193) · [**DreamerV3**](https://arxiv.org/abs/2301.04104)

**Generative / Video**

4. [**GAIA-1**](https://arxiv.org/abs/2309.17080) (Wayve, 2023) — autonomous-driving world model ([official blog](https://wayve.ai/thinking/scaling-gaia-1/))
5. **Genie / Genie 2** (DeepMind, 2024) — interactive generative environments
   - [Genie paper](https://arxiv.org/abs/2402.15391) · [Genie 2 blog](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/)
6. [**Sora technical report**](https://openai.com/index/video-generation-models-as-world-simulators/) (OpenAI, 2024) — argument for treating video generation as world simulation

**Frontier**

7. **V-JEPA / V-JEPA 2** (Meta / LeCun) — non-generative predictive-embedding route
   - [V-JEPA](https://arxiv.org/abs/2404.08471) · [V-JEPA 2](https://ai.meta.com/vjepa/) · [I-JEPA](https://arxiv.org/abs/2301.08243)
8. Other items worth tracking:
   - [**1X World Model**](https://www.1x.tech/discover/1x-world-model) (humanoid robots)
   - [**Oasis**](https://oasis-model.github.io/) (Decart, real-time Minecraft generation)
   - [**DIAMOND**](https://arxiv.org/abs/2405.12399) (NeurIPS 2024, [code](https://github.com/eloialonso/diamond))

</details>

<details>
<summary><b>4.2 Hands-On Practice</b></summary>

Minimum-cost path to a working run:
```bash
# Official Dreamer v3 implementation
pip install dreamerv3
# or clone: https://github.com/danijar/dreamerv3
```
- First run Dreamer v3 successfully on [`CartPole`](https://gymnasium.farama.org/environments/classic_control/cart_pole/) / [`Crafter`](https://github.com/danijar/crafter)
- Then try [`MineRL`](https://github.com/minerllabs/minerl) or [Atari 100k](https://github.com/google-research/rliable)
- For the generative route, explore the [**open-source Genie reproduction**](https://github.com/1x-technologies/1xgpt) or [**DIAMOND**](https://github.com/eloialonso/diamond) (impressive Atari visuals and clean code)

</details>

<details>
<summary><b>4.3 Filling in the Theoretical Foundations</b></summary>

- **Variational inference / VAE** (latent modeling) — [Kingma's original paper](https://arxiv.org/abs/1312.6114) · [Lil'Log tutorial](https://lilianweng.github.io/posts/2018-08-12-vae/)
- **RNN / Transformer / SSM (Mamba)** (temporal dynamics) — [Mamba paper](https://arxiv.org/abs/2312.00752)
- **Diffusion models** (essential for the generative school) — [DDPM](https://arxiv.org/abs/2006.11239) · [Lil'Log diffusion survey](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
- **Model-based RL fundamentals** — [Sutton & Barto, *Reinforcement Learning*, Chapter 8 (free PDF)](http://incompleteideas.net/book/RLbook2020.pdf)

</details>

---

## V. Reference Materials

<details>
<summary><b>5.1 Core Readings</b></summary>

- [**A Path Towards Autonomous Machine Intelligence**](https://openreview.net/pdf?id=BZ5a1r-kVsf) — Yann LeCun white paper and JEPA worldview
- [**Danijar Hafner's homepage**](https://danijar.com/) — author of the Dreamer series; code, papers, and lectures are all available
- [Meta AI Blog: V-JEPA](https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/)

</details>

<details>
<summary><b>5.2 Survey Papers</b></summary>

- [*World Models for Autonomous Driving: A Survey*](https://arxiv.org/abs/2403.02622) (2024)
- [*A Survey of World Models for Autonomous Driving*](https://arxiv.org/abs/2501.11260) (2025)
- [*General World Models: A Survey*](https://arxiv.org/abs/2405.03520) (2024)

</details>

<details>
<summary><b>5.3 Blog & Resource Collections</b></summary>

- [**Lil'Log**](https://lilianweng.github.io/) — Lilian Weng, with RL/world-model-related surveys
- [**The Gradient**](https://thegradient.pub/)
- [**Awesome-World-Model**](https://github.com/LMD0311/Awesome-World-Model) — continuously updated GitHub resource collection

</details>

---

_Last updated: 2026-05-03_
