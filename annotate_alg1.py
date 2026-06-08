"""Annotate the PlaNet Algorithm 1 paper image with overlay callouts.

Adds:
- Right-side braces for Block A (Model fitting) and Block B (Data collection)
- Inner small bracket for "Action repeat" sub-loop
- Side callouts pointing to key lines (loss / belief / planner) with
  cross-references to other chapters
- Back-arrow showing the outer while-loop alternation
"""
from PIL import Image, ImageDraw, ImageFont

SRC = r"C:\Users\jinxinzhou\world_model\asset\planet-2019\planet_algorithm.png"
DST = r"C:\Users\jinxinzhou\world_model\asset\planet-2019\planet_algorithm_annotated.png"

src = Image.open(SRC).convert("RGBA")
W, H = src.size  # 1016 x 1567

RIGHT_PAD = 900
canvas = Image.new("RGBA", (W + RIGHT_PAD, H), "white")
canvas.paste(src, (0, 0))
draw = ImageDraw.Draw(canvas, "RGBA")

# ---- Fonts ----
def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()

CN_REG = r"C:\Windows\Fonts\msyh.ttc"
CN_BD = r"C:\Windows\Fonts\msyhbd.ttc"
f_big = load_font(CN_BD, 34)
f_med = load_font(CN_REG, 26)
f_small = load_font(CN_REG, 22)
f_tiny = load_font(CN_REG, 20)

# ---- Colors ----
BLUE = (25, 118, 210, 255)
GREEN = (56, 142, 60, 255)
ORANGE = (230, 81, 0, 255)
RED = (198, 40, 40, 255)
GRAY = (97, 97, 97, 255)

# ---- Block A: Model fitting (lines 4-7) ----
A_TOP, A_BOT = 750, 1020
BX = W + 25
BW = 18
TX = BX + BW + 25

draw.line([(BX + BW, A_TOP), (BX, A_TOP), (BX, A_BOT), (BX + BW, A_BOT)],
          fill=BLUE, width=5)
draw.line([(BX, (A_TOP + A_BOT) // 2), (BX - 12, (A_TOP + A_BOT) // 2)],
          fill=BLUE, width=5)

draw.text((TX, A_TOP - 5), "A · Model fitting", font=f_big, fill=BLUE)
draw.text((TX, A_TOP + 38), "模型更新 × C 次", font=f_med, fill=BLUE)
draw.text((TX, A_TOP + 78), "(C ≈ 100, B ≈ 50, L ≈ 50)", font=f_small, fill=GRAY)

# Callout for line 6 (Compute loss)
L6_Y = 945
draw.line([(W - 50, L6_Y), (TX - 10, A_TOP + 140)], fill=RED, width=2)
draw.text((TX, A_TOP + 130), "L(θ) = Latent Overshooting ELBO", font=f_small, fill=RED)
draw.text((TX, A_TOP + 158), "(= §Overshooting 章, 论文 Equation 8)", font=f_tiny, fill=RED)

# ---- Block B: Data collection (lines 8-16) ----
B_TOP, B_BOT = 1025, 1560
draw.line([(BX + BW, B_TOP), (BX, B_TOP), (BX, B_BOT), (BX + BW, B_BOT)],
          fill=GREEN, width=5)
draw.line([(BX, (B_TOP + B_BOT) // 2), (BX - 12, (B_TOP + B_BOT) // 2)],
          fill=GREEN, width=5)

draw.text((TX, B_TOP + 5), "B · Data collection", font=f_big, fill=GREEN)
draw.text((TX, B_TOP + 48), "用当前模型跑 1 条新 episode", font=f_med, fill=GREEN)
draw.text((TX, B_TOP + 85), "→ 攒进 buffer 喂下一轮 A", font=f_small, fill=GRAY)

# Callout for line 10 (Infer belief)
L10_Y = 1200
draw.line([(W - 50, L10_Y), (TX - 10, B_TOP + 135)], fill=RED, width=2)
draw.text((TX, B_TOP + 125), "belief = §RSSM 双路:", font=f_small, fill=RED)
draw.text((TX + 14, B_TOP + 152), "h_t = GRU(h_{t-1}, s_{t-1}, a_{t-1})", font=f_tiny, fill=RED)
draw.text((TX + 14, B_TOP + 178), "s_t ~ q_φ(s_t | h_t, o_t)", font=f_tiny, fill=RED)

# Callout for line 11 (planner)
L11_Y = 1300
draw.line([(W - 50, L11_Y), (TX - 10, B_TOP + 220)], fill=RED, width=2)
draw.text((TX, B_TOP + 210), "planner = §Deploy 章 CEM (见论文 Algorithm 2)", font=f_small, fill=RED)

# Inner sub-bracket for action repeat (lines 13-15)
SUB_TOP, SUB_BOT = 1420, 1530
SX = BX + BW + 6
SW = 12
draw.line([(SX + SW, SUB_TOP), (SX, SUB_TOP), (SX, SUB_BOT), (SX + SW, SUB_BOT)],
          fill=ORANGE, width=4)
draw.text((SX + SW + 8, SUB_TOP - 5), "Action repeat × R", font=f_small, fill=ORANGE)
draw.text((SX + SW + 8, SUB_TOP + 22), "(R = 2~4, 把规划长度压缩 R 倍)", font=f_tiny, fill=ORANGE)

# ---- Outer while loop back-arrow ----
WHILE_Y = 545  # y of "3 while not converged do"
ARC_X = W + RIGHT_PAD - 80
# Bottom horizontal: from inside the image margin to ARC_X
draw.line([(BX - 8, B_BOT - 5), (ARC_X, B_BOT - 5)], fill=BLUE, width=3)
# Right vertical: from B_BOT up to WHILE_Y
draw.line([(ARC_X, B_BOT - 5), (ARC_X, WHILE_Y)], fill=BLUE, width=3)
# Top horizontal: from ARC_X back to image
draw.line([(ARC_X, WHILE_Y), (BX - 8, WHILE_Y)], fill=BLUE, width=3)
# Arrow head pointing to "while"
draw.polygon([(BX - 8, WHILE_Y), (BX + 10, WHILE_Y - 10), (BX + 10, WHILE_Y + 10)], fill=BLUE)
# 3-line label alongside the right vertical
label_cx = ARC_X - 270
label_y = (WHILE_Y + B_BOT) // 2 - 50
draw.text((label_cx, label_y),       "回到 while", font=f_big, fill=BLUE)
draw.text((label_cx, label_y + 44),  "A 与 B 交替", font=f_med, fill=BLUE)
draw.text((label_cx, label_y + 78),  "直到 converged", font=f_med, fill=BLUE)

# Save
canvas.convert("RGB").save(DST, quality=95)
print(f"Saved: {DST}")
print(f"Size: {canvas.size}")

