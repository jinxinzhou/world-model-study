"""Generate CEM visualisation figures (paired with the CMA-ES ones).

Outputs (mirroring the CMA-ES asset pair):
  - 02_generations_evolution.png : 4 panels showing CEM's diagonal Gaussian
        N(mu, diag(sigma^2)) converging on a 2D reward landscape.
  - 03_4step_loop.png            : 4-box pipeline of one CEM iteration.

Reward landscape is intentionally identical to the CMA-ES figure
(`f(x,y) = -((x-3)^2 + 5*(y+1)^2)`) so the reader can see at a glance
that CEM's diagonal sigma is forced to stay axis-aligned (no rotation),
unlike CMA-ES which adapts a full covariance and can match the
anisotropy.
"""

from __future__ import annotations

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- pick a CJK font that exists on Windows ----
_CJK_CANDIDATES = [
    "Microsoft YaHei", "Microsoft YaHei UI", "SimHei", "SimSun",
    "Noto Sans CJK SC", "PingFang SC", "DejaVu Sans",
]
_AVAILABLE = {f.name for f in fm.fontManager.ttflist}
for _f in _CJK_CANDIDATES:
    if _f in _AVAILABLE:
        plt.rcParams["font.family"] = _f
        break
plt.rcParams["axes.unicode_minus"] = False


# ---------------- shared 2D reward landscape ----------------

def reward(xy: np.ndarray) -> np.ndarray:
    """Same landscape as CMA-ES figure: anisotropic, optimum at (3, -1)."""
    x, y = xy[..., 0], xy[..., 1]
    return -((x - 3.0) ** 2 + 5.0 * (y + 1.0) ** 2)


def _draw_contours(ax):
    xx, yy = np.meshgrid(np.linspace(-2, 6, 220), np.linspace(-4, 3, 220))
    zz = reward(np.stack([xx, yy], axis=-1))
    ax.contourf(xx, yy, zz, levels=18, cmap="viridis", alpha=0.85)
    ax.contour(xx, yy, zz, levels=12, colors="white", alpha=0.18, linewidths=0.6)
    ax.set_xlim(-2, 6)
    ax.set_ylim(-4, 3)
    ax.set_xticks([-2, 0, 2, 4, 6])
    ax.set_yticks([-4, -3, -2, -1, 0, 1, 2, 3])


# ---------------- Figure 02: generations evolution ----------------

def run_cem_history(
    mu0=np.array([0.0, 0.0]),
    sigma0=np.array([3.0, 3.0]),
    J=60,
    K=15,
    iters=10,
    min_sigma=0.18,
    seed=0,
):
    rng = np.random.default_rng(seed)
    history = []
    mu = mu0.astype(float).copy()
    sigma = sigma0.astype(float).copy()
    for _ in range(iters + 1):
        cand = rng.normal(loc=mu, scale=sigma, size=(J, 2))
        scores = reward(cand)
        elite_idx = np.argsort(scores)[-K:]
        elites = cand[elite_idx]
        history.append((mu.copy(), sigma.copy(), cand.copy(), elites.copy()))
        # CEM update: elementwise mean and std (NO covariance). Floor sigma so
        # candidates stay visually distinguishable across the shown iterations.
        mu = elites.mean(axis=0)
        sigma = np.maximum(elites.std(axis=0), min_sigma)
    return history


def figure_generations_evolution(out_path: str):
    history = run_cem_history()
    to_show = [0, 2, 5, 10]
    fig, axes = plt.subplots(1, 4, figsize=(20, 4.6))
    title = "CEM 在 2D 目标函数上的优化过程(10 次迭代收敛到最优 (3, -1),σ 始终轴对齐 = 对角高斯)"
    fig.suptitle(title, fontsize=15, fontweight="bold", y=1.02)

    for ax, gen in zip(axes, to_show):
        mu, sigma, cand, elites = history[gen]
        _draw_contours(ax)
        # all candidates
        ax.scatter(cand[:, 0], cand[:, 1], s=18, facecolors="none",
                   edgecolors="white", linewidths=0.8, label="候选")
        # elites
        ax.scatter(elites[:, 0], elites[:, 1], s=42, facecolors="none",
                   edgecolors="orange", linewidths=1.6, label="top-K elite")
        # current mu
        ax.scatter([mu[0]], [mu[1]], marker="*", s=220, color="red",
                   edgecolors="black", linewidths=0.6, label="均值 μ", zorder=5)
        # 2-sigma diagonal ellipse (NO rotation -> shows it stays axis-aligned)
        ax.add_patch(Ellipse(xy=mu, width=4 * sigma[0], height=4 * sigma[1],
                             angle=0, fill=False, edgecolor="red", linewidth=2,
                             label="2σ 椭圆 N(μ, diag σ²)"))
        # true optimum
        ax.scatter([3.0], [-1.0], marker="^", s=200, color="#2e7d32",
                   edgecolors="black", linewidths=0.6, label="真实最优", zorder=5)
        ax.set_title(f"第 {gen} 次迭代", fontsize=13)
        ax.set_aspect("equal")

    # single legend below
    handles, labels = axes[1].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=5,
               bbox_to_anchor=(0.5, -0.14), fontsize=11, frameon=False)
    fig.tight_layout(rect=[0, 0.04, 1, 1])
    fig.savefig(out_path, dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {out_path}")


# ---------------- Figure 03: 4-step loop ----------------

def figure_4step_loop(out_path: str):
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 5)
    ax.set_axis_off()

    fig.suptitle("CEM 每次迭代 4 步循环(单步决策内重复 I 次)",
                 fontsize=16, fontweight="bold", y=0.99)

    boxes = [
        {"x": 0.4,  "color": "#bbdefb", "title": "① 采样",
         "sub": r"$a_i \sim \mathcal{N}(\mu, \mathrm{diag}\,\sigma^2)$" + "\n(J = 1000 条序列)"},
        {"x": 4.0,  "color": "#c8e6c9", "title": "② Rollout 评估",
         "sub": r"$R_i = \sum_t \hat r(\hat s_t)$" + "\n(用 RSSM 在 latent 里展开)"},
        {"x": 7.6,  "color": "#fff9c4", "title": "③ 选 top-K elite",
         "sub": "elite_idx = argsort(R)[-K:]\n(K = 100)"},
        {"x": 11.2, "color": "#f8bbd0", "title": "④ 更新 μ, σ",
         "sub": "μ ← elite.mean(0)\nσ ← elite.std(0)  (对角)"},
    ]

    W, H = 3.2, 2.6
    centers = []
    for b in boxes:
        x, y = b["x"], 1.3
        box = FancyBboxPatch(
            (x, y), W, H, boxstyle="round,pad=0.05,rounding_size=0.18",
            edgecolor="#333", facecolor=b["color"], linewidth=1.6,
        )
        ax.add_patch(box)
        ax.text(x + W / 2, y + H * 0.72, b["title"], ha="center", va="center",
                fontsize=15, fontweight="bold")
        ax.text(x + W / 2, y + H * 0.32, b["sub"], ha="center", va="center",
                fontsize=11)
        centers.append((x + W / 2, y + H / 2))

    # forward arrows between boxes
    for i in range(len(boxes) - 1):
        x0 = boxes[i]["x"] + W + 0.05
        x1 = boxes[i + 1]["x"] - 0.05
        ax.add_patch(FancyArrowPatch(
            (x0, 2.6), (x1, 2.6),
            arrowstyle="->,head_length=10,head_width=8",
            color="#333", linewidth=2.0, shrinkA=0, shrinkB=0,
        ))

    # input / output labels
    ax.text(boxes[0]["x"] + W / 2, 4.4, "输入:当前 μ, σ",
            ha="center", va="center", fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff3e0",
                      edgecolor="#bf6f00"))
    ax.text(boxes[-1]["x"] + W / 2, 4.4, "输出:新 μ, σ → 下一次迭代",
            ha="center", va="center", fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff3e0",
                      edgecolor="#bf6f00"))

    # back-edge: from 4th box bottom curving back to 1st box bottom (arc downward, below boxes)
    start = (boxes[-1]["x"] + W / 2, 1.3)
    end = (boxes[0]["x"] + W / 2, 1.3)
    ax.add_patch(FancyArrowPatch(
        start, end,
        connectionstyle="arc3,rad=-0.35",
        arrowstyle="->,head_length=12,head_width=9",
        color="#666", linewidth=1.6,
    ))
    ax.text((start[0] + end[0]) / 2, 0.05,
            "↑ 下一次 CEM 迭代(I 次 / 每次决策)↑",
            ha="center", va="center", fontsize=12, color="#444", style="italic")

    # final action callout (only first action of mu is executed)
    ax.text((boxes[0]["x"] + boxes[-1]["x"] + W) / 2, -0.55,
            "迭代 I 次后 → 取 μ[0] 作为本时刻 a_t(只执行第一个动作)",
            ha="center", va="center", fontsize=12, color="#c62828",
            fontweight="bold")

    ax.set_ylim(-1.0, 5)

    fig.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    figure_generations_evolution(os.path.join(HERE, "02_generations_evolution.png"))
    figure_4step_loop(os.path.join(HERE, "03_4step_loop.png"))
