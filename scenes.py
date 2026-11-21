"""Thirteen small illustrated scenes, one per card, drawn in flat shapes.

Each painter takes (draw, x, y, w, h) and fills its own box with a sky
colour first. No text inside scenes: all labels live in the card body.
"""

import math


def _sky(draw, x, y, w, h, colour):
    draw.rectangle([x, y, x + w, y + h], fill=colour)


def _sun(draw, cx, cy, r, colour):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=colour)


def _burst(draw, cx, cy, r, colour, spikes=12):
    for k in range(spikes):
        ang = 2.0 * math.pi * k / spikes
        tip_x = cx + r * math.cos(ang)
        tip_y = cy + r * math.sin(ang)
        mid = ang + math.pi / spikes
        in_x = cx + r * 0.45 * math.cos(mid)
        in_y = cy + r * 0.45 * math.sin(mid)
        draw.polygon([(cx, cy - r * 0.35), (tip_x, tip_y), (in_x, in_y)],
                     fill=colour)


def paint_poland(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (24, 38, 58))
    _sun(draw, x + w - 70, y + 62, 34, (232, 190, 90))
    draw.polygon([(x, y + h), (x + w * 0.42, y + h * 0.55),
                  (x + w * 0.62, y + h), (x, y + h)], fill=(52, 66, 52))
    draw.polygon([(x + w * 0.45, y + h), (x + w * 0.75, y + h * 0.62),
                  (x + w, y + h), (x + w * 0.45, y + h)], fill=(40, 54, 46))
    for k in range(3):
        sx = x + w * (0.22 + 0.24 * k)
        sy = y + h * (0.30 + 0.10 * k)
        draw.line([(sx, sy), (sx + 64, sy + 44)], fill=(240, 120, 60), width=7)
        draw.ellipse([sx - 8, sy - 8, sx + 8, sy + 8], fill=(250, 200, 90))
        draw.ellipse([sx + 56, sy + 36, sx + 72, sy + 52], fill=(250, 120, 60))
    draw.polygon([(x, y + h - 26), (x + w, y + h - 26), (x + w, y + h),
                  (x, y + h)], fill=(220, 60, 40))


def paint_court(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (58, 84, 110))
    _sun(draw, x + w // 2, y + 46, 30, (240, 220, 160))
    draw.polygon([(x + w * 0.14, y + h * 0.34), (x + w * 0.50, y + h * 0.12),
                  (x + w * 0.86, y + h * 0.34)], fill=(232, 224, 200))
    draw.rectangle([x + w * 0.12, y + h * 0.34, x + w * 0.88, y + h * 0.42],
                   fill=(210, 200, 170))
    for k in range(5):
        cx = x + w * (0.20 + 0.15 * k)
        draw.rectangle([cx - 12, y + h * 0.42, cx + 12, y + h * 0.82],
                       fill=(238, 232, 210))
    draw.rectangle([x + w * 0.10, y + h * 0.82, x + w * 0.90, y + h * 0.90],
                   fill=(200, 190, 160))
    draw.rectangle([x + w * 0.44, y + h * 0.55, x + w * 0.56, y + h * 0.82],
                   fill=(60, 70, 80))
    draw.line([(x + w * 0.30, y + h * 0.30), (x + w * 0.30, y + h * 0.52)],
              fill=(240, 220, 160), width=5)
    draw.line([(x + w * 0.70, y + h * 0.30), (x + w * 0.70, y + h * 0.52)],
              fill=(240, 220, 160), width=5)


def paint_market(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (16, 44, 44))
    draw.rectangle([x, y + h - 30, x + w, y + h], fill=(10, 30, 30))
    pts = []
    base_y = y + h * 0.28
    for k in range(9):
        px = x + w * (0.06 + 0.11 * k)
        py = base_y + k * h * 0.055
        pts.append((px, py))
    for a, b in zip(pts, pts[1:]):
        draw.line([a, b], fill=(235, 70, 50), width=9)
    for (px, py) in pts:
        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=(250, 200, 90))
    draw.polygon([(x + w * 0.78, y + h * 0.30), (x + w * 0.92, y + h * 0.30),
                  (x + w * 0.85, y + h * 0.44)], fill=(235, 70, 50))
    for k in range(6):
        bx = x + w * (0.10 + 0.13 * k)
        bh = h * (0.10 + 0.05 * ((k * 7) % 4))
        draw.rectangle([bx, y + h - 30 - bh, bx + 34, y + h - 30],
                       fill=(40, 110, 100))


def paint_summit(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (120, 40, 44))
    _sun(draw, x + w // 2, y + 52, 44, (245, 200, 110))
    for k in range(3):
        cx = x + w * (0.22 + 0.28 * k)
        draw.rectangle([cx - 52, y + h * 0.52, cx + 52, y + h * 0.78],
                       fill=(250, 244, 228))
        draw.ellipse([cx - 26, y + h * 0.34, cx + 26, y + h * 0.52],
                     fill=(232, 196, 160))
        draw.rectangle([cx - 30, y + h * 0.78, cx + 30, y + h * 0.86],
                       fill=(40, 60, 80))
    draw.rectangle([x + w * 0.08, y + h * 0.86, x + w * 0.92, y + h * 0.92],
                   fill=(90, 30, 34))
    draw.line([(x + w * 0.22, y + h * 0.52), (x + w * 0.50, y + h * 0.52)],
              fill=(240, 220, 160), width=6)
    draw.line([(x + w * 0.50, y + h * 0.52), (x + w * 0.78, y + h * 0.52)],
              fill=(240, 220, 160), width=6)


def paint_deal(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (30, 70, 110))
    _sun(draw, x + 70, y + 54, 30, (245, 210, 120))
    draw.rectangle([x + w * 0.10, y + h * 0.55, x + w * 0.90, y + h * 0.62],
                   fill=(245, 240, 220))
    for k in range(4):
        fx = x + w * (0.16 + 0.20 * k)
        draw.line([(fx, y + h * 0.30), (fx, y + h * 0.55)], fill=(230, 225, 200),
                  width=5)
        draw.rectangle([fx, y + h * 0.30, fx + 56, y + h * 0.46],
                       fill=(250, 244, 228))
        draw.rectangle([fx + 8, y + h * 0.35, fx + 48, y + h * 0.41],
                       fill=(40, 110, 90))
    draw.ellipse([x + w * 0.42, y + h * 0.66, x + w * 0.58, y + h * 0.86],
                 fill=(240, 200, 90))
    draw.rectangle([x + w * 0.44, y + h * 0.70, x + w * 0.56, y + h * 0.82],
                   fill=(40, 70, 110))


def paint_bridge(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (46, 62, 84))
    _sun(draw, x + w - 66, y + 56, 28, (240, 200, 120))
    draw.rectangle([x, y + h * 0.66, x + w, y + h * 0.72], fill=(60, 58, 54))
    draw.rectangle([x + w * 0.12, y + h * 0.66, x + w * 0.16, y + h],
                   fill=(70, 66, 60))
    draw.rectangle([x + w * 0.46, y + h * 0.66, x + w * 0.50, y + h],
                   fill=(70, 66, 60))
    draw.rectangle([x + w * 0.80, y + h * 0.66, x + w * 0.84, y + h],
                   fill=(70, 66, 60))
    for k in range(5):
        ax = x + w * (0.16 + 0.16 * k)
        draw.arc([ax - 60, y + h * 0.30, ax + 60, y + h * 0.72],
                 start=180, end=360, fill=(210, 205, 190), width=6)
    draw.polygon([(x + w * 0.30, y + h * 0.72), (x + w * 0.46, y + h * 0.72),
                  (x + w * 0.38, y + h * 0.86)], fill=(220, 60, 40))
    _burst(draw, x + w * 0.38, y + h * 0.52, 34, (250, 160, 60))
    draw.rectangle([x, y + h - 18, x + w, y + h], fill=(36, 60, 80))


def paint_blast(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (52, 44, 52))
    _burst(draw, x + w * 0.50, y + h * 0.46, 74, (250, 130, 50))
    _burst(draw, x + w * 0.50, y + h * 0.46, 46, (250, 200, 90))
    _burst(draw, x + w * 0.50, y + h * 0.46, 24, (255, 240, 200))
    draw.rectangle([x, y + h - 34, x + w, y + h], fill=(30, 28, 34))
    for k in range(4):
        bx = x + w * (0.10 + 0.22 * k)
        draw.rectangle([bx, y + h - 70, bx + 46, y + h - 34], fill=(60, 56, 62))
    draw.ellipse([x + w * 0.16, y + h * 0.18, x + w * 0.30, y + h * 0.30],
                 fill=(120, 110, 118))


def paint_shield(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (20, 52, 74))
    for k in range(3):
        sx = x + w * (0.24 + 0.26 * k)
        sy = y + h * (0.22 + 0.08 * k)
        draw.line([(sx, sy), (sx + 52, sy + 40)], fill=(250, 120, 60), width=6)
        draw.ellipse([sx - 7, sy - 7, sx + 7, sy + 7], fill=(250, 200, 90))
    draw.arc([x + w * 0.22, y + h * 0.34, x + w * 0.78, y + h * 0.90],
             start=180, end=360, fill=(120, 200, 220), width=10)
    draw.line([(x + w * 0.22, y + h * 0.62), (x + w * 0.22, y + h * 0.34)],
              fill=(120, 200, 220), width=10)
    draw.line([(x + w * 0.78, y + h * 0.62), (x + w * 0.78, y + h * 0.34)],
              fill=(120, 200, 220), width=10)
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=(16, 40, 58))


def paint_climate(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (150, 200, 205))
    _sun(draw, x + w - 64, y + 54, 36, (250, 190, 80))
    draw.ellipse([x + w * 0.30, y + h * 0.30, x + w * 0.70, y + h * 0.70],
                 fill=(40, 120, 80))
    draw.arc([x + w * 0.36, y + h * 0.36, x + w * 0.64, y + h * 0.64],
             start=200, end=340, fill=(240, 240, 220), width=7)
    draw.rectangle([x + w * 0.16, y + h * 0.72, x + w * 0.84, y + h * 0.78],
                   fill=(90, 140, 100))
    for k in range(3):
        lx = x + w * (0.22 + 0.26 * k)
        draw.rectangle([lx - 6, y + h * 0.78, lx + 6, y + h * 0.94],
                       fill=(70, 110, 80))
    draw.polygon([(x + w * 0.50, y + h * 0.18), (x + w * 0.56, y + h * 0.30),
                  (x + w * 0.44, y + h * 0.30)], fill=(40, 120, 80))


def paint_flame(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (60, 32, 30))
    draw.rectangle([x, y + h - 30, x + w, y + h], fill=(34, 22, 20))
    cx = x + w * 0.50
    cy = y + h * 0.52
    draw.polygon([(cx - 52, cy + 40), (cx - 30, cy - 30), (cx - 6, cy + 6),
                  (cx + 12, cy - 56), (cx + 34, cy - 6), (cx + 52, cy + 40)],
                 fill=(250, 120, 40))
    draw.polygon([(cx - 30, cy + 40), (cx - 14, cy - 6), (cx + 4, cy + 16),
                  (cx + 16, cy - 22), (cx + 30, cy + 40)], fill=(250, 200, 80))
    draw.ellipse([cx - 14, cy + 18, cx + 14, cy + 44], fill=(255, 240, 180))
    for k in range(3):
        tx = x + w * (0.18 + 0.32 * k)
        draw.rectangle([tx, y + h - 64, tx + 40, y + h - 30], fill=(80, 60, 50))


def paint_pill(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (210, 235, 235))
    draw.rounded_rectangle([x + w * 0.18, y + h * 0.36, x + w * 0.82,
                            y + h * 0.64], radius=40, fill=(255, 255, 255),
                           outline=(30, 120, 110), width=6)
    draw.rectangle([x + w * 0.18, y + h * 0.36, x + w * 0.50, y + h * 0.64],
                   fill=(30, 120, 110))
    draw.rounded_rectangle([x + w * 0.18, y + h * 0.36, x + w * 0.82,
                            y + h * 0.64], radius=40, outline=(20, 90, 85),
                           width=6)
    for k in range(3):
        px = x + w * (0.24 + 0.20 * k)
        py = y + h * (0.20 + 0.06 * k)
        draw.ellipse([px - 12, py - 12, px + 12, py + 12],
                     fill=(240, 90, 70))
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=(30, 120, 110))


def paint_bridgehit(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (30, 48, 66))
    _sun(draw, x + 64, y + 52, 28, (240, 200, 120))
    draw.rectangle([x, y + h * 0.58, x + w * 0.42, y + h * 0.64],
                   fill=(200, 195, 180))
    draw.rectangle([x + w * 0.58, y + h * 0.58, x + w, y + h * 0.64],
                   fill=(200, 195, 180))
    draw.polygon([(x + w * 0.42, y + h * 0.58), (x + w * 0.50, y + h * 0.44),
                  (x + w * 0.58, y + h * 0.58)], fill=(90, 84, 76))
    _burst(draw, x + w * 0.50, y + h * 0.42, 44, (250, 150, 60))
    _burst(draw, x + w * 0.50, y + h * 0.42, 24, (255, 220, 120))
    draw.rectangle([x, y + h - 22, x + w, y + h], fill=(28, 52, 70))
    for k in range(3):
        wx = x + w * (0.16 + 0.30 * k)
        draw.ellipse([wx, y + h - 44, wx + 26, y + h - 18], fill=(90, 130, 150))


def paint_cuffs(draw, x, y, w, h):
    _sky(draw, x, y, w, h, (44, 56, 66))
    draw.ellipse([x + w * 0.16, y + h * 0.30, x + w * 0.44, y + h * 0.70],
                 outline=(220, 200, 140), width=12)
    draw.ellipse([x + w * 0.56, y + h * 0.30, x + w * 0.84, y + h * 0.70],
                 outline=(220, 200, 140), width=12)
    draw.line([(x + w * 0.44, y + h * 0.50), (x + w * 0.56, y + h * 0.50)],
              fill=(220, 200, 140), width=10)
    draw.rectangle([x + w * 0.26, y + h * 0.44, x + w * 0.34, y + h * 0.56],
                   fill=(240, 220, 160))
    draw.rectangle([x + w * 0.66, y + h * 0.44, x + w * 0.74, y + h * 0.56],
                   fill=(240, 220, 160))
    draw.rectangle([x, y + h - 26, x + w, y + h], fill=(30, 40, 48))


PAINTERS = {
    "poland": paint_poland,
    "court": paint_court,
    "market": paint_market,
    "summit": paint_summit,
    "deal": paint_deal,
    "bridge": paint_bridge,
    "blast": paint_blast,
    "shield": paint_shield,
    "climate": paint_climate,
    "flame": paint_flame,
    "pill": paint_pill,
    "bridgehit": paint_bridgehit,
    "cuffs": paint_cuffs,
}
