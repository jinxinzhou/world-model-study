# Introduction Writing Pattern with Annotated Example

**🌐 Language**: [🇨🇳 中文](Introduction-Writing-ZH.md) · 🇬🇧 **English**

> This note distills a generic **"5–6 paragraph narrative arc"** template from the PlaNet (Hafner et al., ICML 2019) Introduction section.

---

## I. The Core Job of an Introduction

If the Abstract is an "advertisement", the Introduction is a "persuasion document" — it has 1–2 pages to convince the reviewer of four things:

1. **The problem exists** (and matters)
2. **Solving it has value**
3. **Prior work hasn't solved it well** (but cannot be dismissed)
4. **Our method deserves a look**

→ A weak Introduction leaves reviewers skeptical no matter how strong the experimental results are.

---

## II. Standard 5–6 Paragraph Narrative Arc

| Para | Role | Length | Key Question |
|:----:|------|--------|--------------|
| **① What's the problem** | Foundation + list pain points | Longer | What is the long-standing challenge in this field? |
| **② Why it matters** | Value proposition | Medium | What benefits does solving this bring? |
| **③ What others did** | Narrow the gap | Medium | What have prior works achieved? What remains? |
| **④ What we propose** | Introduce the method | Short | What is our method? One-sentence positioning |
| **⑤ Concrete contributions** | Bullet list | Medium | 1–3 specific technical contributions (mirroring abstract) |
| **⑥ Figure / Table reference** (optional) | Visual anchor | Very short | Direct reader to a key figure for intuition |

---

## III. Sentence-Level Templates per Paragraph

### ① What's the problem

```
[Field] is a natural / powerful / important approach for [scope where it works well].
To extend this to [unknown / harder condition], the agent needs to [necessary capability].
However, [specific challenge] has been a long-standing challenge.
Key difficulties include [pain 1], [pain 2], [pain 3], and [pain 4].
```

🔑 **Key technique**: **List 3–4 concrete pain points** (not vague "it's hard"); shows reviewers you understand the domain.

### ② Why it matters

```
[Our approach class] offers several benefits over [alternative class]:

First, [benefit 1 with reason] — [optional citation].
Moreover, [benefit 2 with future implication] — as shown by [citation].
Finally, [benefit 3, often transferability / generality].
```

🔑 **Key technique**:
- **3 independent selling points** (First / Moreover / Finally)
- Each backed by a citation, looks grounded
- Do not exceed 3 (4+ feels verbose)

### ③ What others did (give credit, then narrow gap)

```
Recent work has shown promise in [narrow setting] ([citations]).
However, these approaches typically assume [strong assumption] / are limited to [narrow scope].
In [our setting], we would like to [extension goal].
The success of such methods has previously been limited to [explicit limitation],
e.g., [concrete example].
```

🔑 **Key technique**:
- **Acknowledge prior work first, then point out the gap** — never dismiss prior work outright (the reviewer may be one of them)
- Make "they did X, we will do X+1" concrete — 100× stronger than vague "prior work is limited"

### ④ What we propose

```
In this paper, we propose [Method Name] ([abbreviation]),
a [positioning] that [core mechanism] to [accomplish goal].
To achieve [key property], we use [Technique 1] and propose [Technique 2 — your own].
[Method] solves [hard setting] that [exceeds prior work's scope].
```

🔑 **Key technique**:
- Method name + full name + abbreviation **given all at once on first mention**
- **Directly respond to the gap from ③** — forming a clean "problem → method" mapping
- End with a "difficulty commitment" (harder setting than prior work)

### ⑤ Concrete contributions (bullet list)

```
Key contributions of this work are summarized as follows:

• [Contribution 1 name]:  [1–2 sentences with concrete number or claim]
• [Contribution 2 name]:  [1–2 sentences]
• [Contribution 3 name]:  [1–2 sentences with claim of generality]
```

🔑 **Key technique**:
- **3 bullets is ideal** (not 5+, readers will forget)
- Each bullet gets a **"keyword" name** (for cross-referencing throughout the paper), in bold
- At least one bullet should contain a **concrete number** (N×, +M points)
- At least one bullet should imply **generality / transferability** (signals it's not a hack)
- **Should map one-to-one** with the abstract's 3 contributions, but with more detail here

---

## IV. The "Logical Gears" of the 6-Paragraph Arc

```
Para ① pain ── leads to ────► Para ② value
     │                            │
     └─── big problem, worth solving ────┘
                                  │
Para ③ prior ◄─── but didn't solve it ──┘
     │
     └──── leaves explicit gap ──► Para ④ proposed method
                                          │
                                          └── maps to gap ──► Para ⑤ contributions
                                                                   │
                                                                   └──► Para ⑥ see figure
```

**Key check**: the gap in para ③ must **map one-to-one** with the method in para ④. If para ③ lists 3 gaps, para ④ must show how the method addresses all 3.

---

## V. 8-Question Self-Review Checklist

After writing the Introduction, run through:

- [ ] Does the first paragraph list **3–4 concrete pain points**, not vague "it's hard"?
- [ ] Is there a **"Why it matters"** paragraph with 2–3 **independent** value claims?
- [ ] Does it **give prior work credit + citations**, rather than dismissing them?
- [ ] Is the **prior-work gap specific** (concrete enough to "point at and say: they didn't do this")?
- [ ] Does the method **directly respond** to that gap (each gap → one contribution)?
- [ ] Are **method name + abbreviation** introduced by paragraph 4?
- [ ] Are **contribution bullets** ≤3, each with a keyword name?
- [ ] Does at least one bullet contain a **concrete number**?

Pass all 8 → it's a solid Introduction.

---

## VI. Case Study: PlaNet's Introduction Follows the Template Exactly

PlaNet's Section 1 strictly follows the 6-paragraph template:

| Para | PlaNet instance | Technique distilled |
|:----:|----------------|---------------------|
| ① | Lists 4 pain points: model accuracy / multi-step error / multi-modality / overconfidence | Immediately establishes domain expertise |
| ② | First (sample efficiency) / Moreover (more compute → better) / Finally (task transfer) | Three-part value proposition |
| ③ | Credits Deisenroth 2011 etc.; but they assume known state; high-dim only solved cartpole | Give credit + concretize the gap |
| ④ | "We propose PlaNet, a model-based agent that..." — one-sentence positioning | Name + full + abbreviation + positioning all-in-one |
| ⑤ | **3 bullets**: Latent planning / RSSM / Latent overshooting | Maps 1:1 to abstract, each with a concrete number (200× / both crucial / compatible) |
| ⑥ | Figure 1 showing 6 DMC tasks | Lets the reader see "what kind of tasks we're solving" |

Full original + Chinese translation: [World Models Study Notes §4.2 PlaNet](../World-Model-Study-Notes.md#42-planet-2019).

---

## VII. Other Classic Introductions Worth Studying

| Paper | Distinctive feature of its Introduction |
|-------|----------------------------------------|
| **AlphaGo** (Nature 2016) | First paragraph delivers a shocking number: beating a professional player |
| **Transformer** (2017) | Extreme conciseness: 5 paragraphs, quickly arrives at "attention is all you need" |
| **GPT-3** (2020) | Heavily cites scaling laws; "why go big" is the throughline of the entire paper |
| **Sora Technical Report** (2024) | Breaks standard ML format with a "vision-first" narrative |

---

## VIII. One-Sentence Summary

> **An Introduction is a 6-paragraph narrative: «problem → value → prior gap → our method → contribution list». Every paragraph has a specific job, and the gap in para ③ must align one-to-one with the method in para ④ — this is the logical gear reviewers scrutinize most.** PlaNet's Section 1 is a textbook example.

---

_Distilled from: [PlaNet (Hafner et al., 2019)](https://arxiv.org/abs/1811.04551) Section 1 · Last updated: 2026-06_
