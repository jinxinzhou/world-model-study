# World Model 学习笔记

个人学习 **World Model / Model-Based RL** 方向的系统性笔记。

> 📖 主笔记入口:**[World-Model-学习笔记.md](World-Model-学习笔记.md)**

## 内容概览

按「**是什么 → 为什么重要 → 流派对比 → 怎么入门**」的逻辑组织,涵盖:

| 章节 | 内容 |
|------|------|
| **一** | World Model 是什么 + 三大流派速览 |
| **二** | 为什么火 / 实际价值 / 局限 |
| **三** | 三大流派深入对比(生成式 / Latent Dynamics / JEPA) |
| **四** | 入门路径,含 **Model-Free vs Model-Based** 前置概念详解 |
| **五** | 参考资料汇总 |

## 重点论文精读

- **[World Models (Ha & Schmidhuber, 2018)](https://arxiv.org/abs/1803.10122)** — 含核心思想、关键实验、🔧 实现细节深入、CMA-ES 详解(含 4 张配套图)、Bellman 讨论等
- PlaNet / Dreamer V1-V3(规划中)
- JEPA / Sora / Genie(规划中)

## 配套素材

```
asset/
├── world-models-2018/         # 架构图、VAE/MDN 示意、CarRacing/Doom 演示 GIF
└── cma-es/                    # CMA-ES 进化过程、5 步流程、B/D 分解图
```

## 渲染要求

- **GitHub Web**:全部原生支持(Mermaid / LaTeX / GIF / `<details>`)
- **VSCode** 预览需装两个插件:
  - `Markdown Preview Mermaid Support` (bierner)
  - `Markdown All in One` (yzhang,LaTeX 公式渲染)

## 友情提示

部分图片素材引用自原论文交互式网站 [worldmodels.github.io](https://worldmodels.github.io/),© Ha & Schmidhuber 2018,仅作学习参考使用。

---

_最后更新:2026 年_
