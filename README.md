# World Model Study Notes / 世界模型学习笔记

**🌐 Choose language / 选择语言**:
- 🇨🇳 **[中文版 World-Model-学习笔记.md](World-Model-学习笔记.md)**
- 🇬🇧 **[English Version: World-Model-Study-Notes.md](World-Model-Study-Notes.md)**

---

A systematic study notebook on **World Models / Model-Based RL**.

## Contents Overview

Organized by the logic: **What it is → Why it matters → School comparison → How to get started**, covering:

| Chapter | Content |
|------|------|
| **I** | What is a World Model + Three Schools at a glance |
| **II** | Why it's hot / Practical value / Limitations |
| **III** | Deep comparison of three schools (Generative / Latent Dynamics / JEPA) |
| **IV** | Getting started, including **Model-Free vs Model-Based** prerequisites |
| **V** | Reference resources |

## Featured Paper Deep-Dives

- **[World Models (Ha & Schmidhuber, 2018)](https://arxiv.org/abs/1803.10122)** — Core ideas, key experiments, 🔧 implementation deep-dive, CMA-ES detailed walkthrough (with 4 figures), Bellman discussion, etc.
- PlaNet / Dreamer V1-V3 (planned)
- JEPA / Sora / Genie (planned)

## Asset Layout

```
asset/
├── world-models-2018/      # Architecture diagrams, VAE/MDN illustrations, CarRacing/Doom demos (GIF)
├── cma-es/                 # CMA-ES evolution process, 5-step loop, B/D decomposition
└── formulas/               # Pre-rendered LaTeX formulas (PNG)
```

## Rendering Requirements

- **GitHub Web**: All elements supported natively (Mermaid / LaTeX images / GIF / `<details>`)
- **VSCode Preview** requires two extensions:
  - `Markdown Preview Mermaid Support` (bierner)
  - `Markdown All in One` (yzhang, for LaTeX inline math)

## Attribution

Some figures are referenced from the original paper's interactive site [worldmodels.github.io](https://worldmodels.github.io/), © Ha & Schmidhuber 2018, used for educational purposes only.

---

_Last updated: 2026_
