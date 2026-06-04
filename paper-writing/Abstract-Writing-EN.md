# Abstract Writing Pattern with Annotated Example

**🌐 Language**: [🇨🇳 中文](Abstract-Writing-ZH.md) · 🇬🇧 **English**

> This note extracts a general **"5-step" writing template** from the PlaNet abstract (Hafner et al., ICML 2019), along with a line-by-line breakdown of the original text.

---

## I. Why the Abstract Matters

- **80% of a reviewer's first impression comes from the abstract.** Most reviewers skim abstract + figures before deciding whether to read in depth
- **arXiv readers** read only the abstract before deciding to open the PDF
- **Search engines and Google Scholar** index the abstract — it determines discoverability
- **Future readers** (including yourself a year later) see the abstract first

→ **The abstract is not a "summary" — it is the 8 most important sentences of the entire paper.**

---

## II. The 5-Step Structure (Generalized from PlaNet)

| Step | Role | # Sentences | Key Question |
|:----:|------|:----------:|--------------|
| **① Problem framing** | Hook — establish context | 2–3 | "What is the long-standing challenge? Why are old methods insufficient?" |
| **② Method introduction** | Name + one-sentence positioning | 1 | "What did we do? Say it in one sentence." |
| **③ Technical contribution** | List 1–2 key innovations | 1–2 | "Why does our approach work? What is the core trick?" |
| **④ Experimental setting** | Emphasize task difficulty | 1 | "On what challenging scenarios is it validated?" |
| **⑤ Results comparison** | Numbers + comparison to SOTA | 1 | "How much better than the baseline? How much data/compute?" |

**Total length**: 8–10 sentences is ideal (≈ 150–250 words).

---

## III. Generic Template (Plug-and-Play)

```
[1] [Field] has been very successful under [known condition].
[2] To extend [capability] to [unknown condition], we need to solve [core difficulty].
[3] However, [more specific challenge] has been a long-standing problem,
    especially under [extreme condition].

[4] We propose [Method] (abbreviation), a [positioning] [method type]
    that [core mechanism] to address [goal].

[5] To achieve [key performance metric], we must solve [sub-problem].
[6] We address this with [Technique 1] and [Technique 2].

[7] Using only [input constraint], our method solves tasks with [challenges a, b, c],
    exceeding the difficulty of [what prior work could solve].

[8] [Method] uses [N× less resource] to achieve performance [close to / exceeding]
    the strong baseline [SOTA name].
```

---

## IV. Case Study: PlaNet Abstract, Sentence by Sentence

### Original

> [1] Planning has been very successful for control tasks with known environment dynamics.
> [2] To leverage planning in unknown environments, the agent needs to learn the dynamics from interactions with the world.
> [3] However, learning dynamics models that are accurate enough for planning has been a long-standing challenge, especially in image-based domains.
> [4] We propose the Deep Planning Network (PlaNet), a purely model-based agent that learns the environment dynamics from images and chooses actions through fast online planning in latent space.
> [5] To achieve high performance, the dynamics model must accurately predict the rewards ahead for multiple time steps.
> [6] We approach this using a latent dynamics model with both deterministic and stochastic transition components.
> [7] Moreover, we propose a multi-step variational inference objective that we name latent overshooting.
> [8] Using only pixel observations, our agent solves continuous control tasks with contact dynamics, partial observability, and sparse rewards, which exceed the difficulty of tasks that were previously solved by planning with learned models.
> [9] PlaNet uses substantially fewer episodes and reaches final performance close to and sometimes higher than strong model-free algorithms.

### Per-Sentence Mapping to Template

| Sentence | Template Step | Function |
|:--------:|:-------------:|----------|
| [1] | ① Hook starting point | Establish consensus: "planning works on known dynamics" |
| [2] | ① Pain-point transition | Introduce the gap: "unknown dynamics" |
| [3] | ① Specification | Narrow pain to "image domain, insufficient precision" |
| [4] | ② **Method + naming** | Give name (PlaNet) + one-sentence positioning: **pure model-based + pixel input + latent planning** |
| [5] | ③ Technical challenge | Key issue: accurate multi-step prediction |
| [6] | ③ **Technical contribution 1** | Dual-path latent (deterministic + stochastic) |
| [7] | ③ **Technical contribution 2** | Latent overshooting (named and briefly described) |
| [8] | ④ **Experimental difficulty** | Emphasize three challenges (contact / partial obs / sparse rewards) |
| [9] | ⑤ **Results comparison** | No specific numbers but explicit: "fewer episodes + ≥ model-free SOTA" |

---

## V. Key Writing Techniques (Lessons from PlaNet)

### 1. The First Sentence Should Establish "Known vs Unknown" Tension

```
✅ "Planning has been very successful for control tasks with known environment dynamics."
   → Immediately tells the reader: this paper pushes planning from "known" to "unknown"
```

**Anti-pattern**:
```
❌ "Reinforcement learning is an important field with many applications."
   → Vague, establishes no gap
```

### 2. The Method Name Should Be "Memorable"

PlaNet did this well:
- **PlaNet** = **Pla**nning **Net**work → also a pun on "planet" (Earth/celestial)
- Short (2 syllables), easy to remember, directly tied to function

**Common anti-patterns**:
- ❌ `DLLDMRL` (Deep Latent-Logic Dynamics Model with RL) → no one remembers
- ✅ Dreamer / GATO / Sora / PaLM → simple English words spread the best

### 3. Place "Name + Brief" in the Same Sentence

```
✅ "We propose the Deep Planning Network (PlaNet), a purely model-based agent that ..."
```

- Full name + abbreviation given **at once**
- Followed by an **«a ...» appositive** for one-sentence positioning
- More compact than "We propose X. X is ..."

### 4. Use "Numbers + Comparison" Instead of "Improvement / Enhancement"

PlaNet's abstract doesn't have concrete numbers, but the paper's Table 1 shows:
- PlaNet uses **2,000 episodes** to reach the performance of D4PG with **100,000 episodes**

**Pulled into the abstract this becomes**:
```
✅ "PlaNet uses 50× fewer episodes than D4PG to reach competitive performance."
```

**Anti-pattern**:
```
❌ "PlaNet significantly improves sample efficiency."
   → «significantly improves» is empty phrasing — reviewers hate it
```

### 5. Stack Experimental Difficulty (Reinforce the Contribution)

```
✅ "...solves continuous control tasks with contact dynamics, partial observability, and sparse rewards"
   → Lists 3 difficulties in one breath, demonstrating robustness
```

**Anti-pattern**:
```
❌ "...solves several control tasks"
   → Vague; reviewers will suspect cherry-picked easy tasks
```

### 6. Do Not Discuss Limitations or Future Work in the Abstract

The abstract is an **"advertisement"** that makes people want to read the full paper, not a "complete summary." Save limitations for the discussion section.

---

## VI. Anti-Patterns to Avoid

| ❌ Anti-pattern | Why it's bad | ✅ Improvement |
|----------------|--------------|----------------|
| "We propose a novel framework that..." | "novel" is empty; reviewers hate it most | Directly state what was done: "We propose X, which does Y" |
| "Extensive experiments show..." | Boilerplate, zero information | List concrete numbers + benchmark names |
| Abbreviation overload (VAE, MDN, RSSM, ELBO in one line) | High reading barrier | Spell out on first use; abbreviate only after |
| Sentences > 30 words | Hard to read | Split into two |
| Buzzwords ("paradigm-shift", "revolutionary") | Sounds unconfident | Let numbers and experiments speak |
| No baseline mentioned | Readers can't judge value | Must have an explicit «vs SOTA» comparison |

---

## VII. 6-Question Checklist (Self-Review After Writing)

- [ ] Does the first sentence let a layperson grasp "what problem this field has" in 30 seconds?
- [ ] Is the method name short, memorable, and distinctive?
- [ ] Is the method name introduced in the first 4 sentences?
- [ ] Are technical contributions **1–2 items**, not 5–6 piled together?
- [ ] Are there **concrete numbers** (N× / N M frames / +X points)?
- [ ] Is the **baseline name explicit** (not a vague "prior work")?

Pass all 6 → it's a solid abstract.

---

## VIII. Other Classic Abstracts Worth Studying

| Paper | What its abstract teaches |
|-------|--------------------------|
| **AlphaGo** (Nature 2016) | First sentence delivers a shocking number (beating a professional player) |
| **Transformer** (Vaswani 2017) | Extreme conciseness: "based solely on attention mechanisms" |
| **BERT** (2018) | Results sentence directly lists improvements on 11 tasks |
| **GPT-3** (Brown 2020) | Uses "175B parameters" as the hook |
| **DreamerV3** (2023) | Emphasizes "single set of hyperparameters" as the core selling point |

→ When reading these papers later, study their abstracts specifically to expand this template.

---

## IX. One-Sentence Summary

> **A good abstract = 8–10 sentences that clearly convey «problem → method → technical contribution → experimental difficulty → results comparison», where every sentence carries information, has no boilerplate, and contains concrete numbers and explicit baseline names.** PlaNet's abstract is a textbook example worth re-reading and dissecting line by line.

---

_Distilled from: [PlaNet (Hafner et al., 2019)](https://arxiv.org/abs/1811.04551) · Last updated: 2026-06_
