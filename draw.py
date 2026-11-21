"""Small drawing helpers for the 21 November digest page.

All helpers work on a Pillow ImageDraw at the 2048px master scale.
Fonts resolve from the system DejaVu and Liberation families; the
fallback chain never raises, it lands on Pillow's built-in bitmap font.
"""

from PIL import ImageFont

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_XBOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

FONT_PATHS = {
    "serif-bold": SERIF_BOLD,
    "serif": SERIF,
    "sans-bold": SANS_BOLD,
    "sans": SANS,
    "sans-xbold": SANS_XBOLD,
}

_cache = {}


def load_font(kind, size):
    key = (kind, size)
    found = _cache.get(key)
    if found is not None:
        return found
    path = FONT_PATHS.get(kind, SANS)
    picked = None
    try:
        picked = ImageFont.truetype(path, size)
    except OSError as caught:
        _ = caught
        picked = ImageFont.load_default()
    _cache[key] = picked
    return picked


def shrink_to_fit(draw, text, kind, start_size, max_width, floor_size=18):
    size = start_size
    font = load_font(kind, size)
    width = draw.textlength(text, font=font)
    while width > max_width and size > floor_size:
        size = size - 2
        font = load_font(kind, size)
        width = draw.textlength(text, font=font)
    return font


def wrap_lines(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if current == "" else current + " " + word
        trial_width = draw.textlength(trial, font=font)
        if trial_width <= max_width:
            current = trial
        if trial_width > max_width and current != "":
            lines.append(current)
            current = word
        if trial_width > max_width and current == "":
            current = word
    if current != "":
        lines.append(current)
    return lines


def draw_wrapped(draw, text, font, x, y, max_width, fill, leading=6):
    lines = wrap_lines(draw, text, font, max_width)
    cursor_y = y
    for line in lines:
        draw.text((x, cursor_y), line, font=font, fill=fill)
        cursor_y = cursor_y + font.size + leading
    return cursor_y


def centered_text(draw, text, font, cx, y, fill):
    width = draw.textlength(text, font=font)
    draw.text((cx - width / 2, y), text, font=font, fill=fill)
    return y + font.size


def chip(draw, x, y, text, font, bg, fg):
    pad_x = 14
    pad_y = 7
    width = draw.textlength(text, font=font)
    box_w = int(width + pad_x * 2)
    box_h = font.size + pad_y * 2
    draw.rounded_rectangle([x, y, x + box_w, y + box_h], radius=8, fill=bg)
    draw.text((x + pad_x, y + pad_y), text, font=font, fill=fg)
    return box_w


def rule(draw, x, y, w, fill, weight=3):
    draw.rectangle([x, y, x + w, y + weight], fill=fill)


def map_point(lon, lat, x0, y0, w, h):
    fx = (lon + 170.0) / 360.0
    fy = (75.0 - lat) / 130.0
    px = x0 + fx * w
    py = y0 + fy * h
    return (px, py)


def draw_world_map(draw, x0, y0, w, h, sea, land, pin, pin_edge):
    draw.rectangle([x0, y0, x0 + w, y0 + h], fill=sea)
    for poly in LAND_POLYS:
        pts = [map_point(lon, lat, x0, y0, w, h) for (lon, lat) in poly]
        draw.polygon(pts, fill=land)
    return None


def draw_map_pin(draw, x0, y0, w, h, lon, lat, num, pin, pin_edge, num_fill):
    px, py = map_point(lon, lat, x0, y0, w, h)
    big = num <= 13
    radius = 17 if big else 9
    draw.ellipse([px - radius, py - radius, px + radius, py + radius],
                 fill=pin, outline=pin_edge, width=3)
    if big:
        font = load_font("sans-bold", 22)
        text = str(num)
        tw = draw.textlength(text, font=font)
        draw.text((px - tw / 2, py - 11), text, font=font, fill=num_fill)
    return None


LAND_POLYS = [
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73), (-65, 62),
     (-55, 52), (-60, 47), (-70, 42), (-75, 35), (-80, 32), (-85, 30),
     (-90, 21), (-97, 16), (-105, 20), (-115, 28), (-125, 40), (-125, 49),
     (-145, 60), (-168, 66)],
    [(-80, 10), (-60, 8), (-50, 0), (-35, -8), (-40, -20), (-48, -28),
     (-58, -35), (-65, -41), (-70, -52), (-73, -40), (-75, -20), (-80, -5),
     (-80, 10)],
    [(-10, 36), (-9, 43), (-2, 48), (-5, 50), (0, 51), (5, 53), (8, 57),
     (10, 59), (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (32, 70),
     (40, 68), (44, 66), (40, 60), (35, 55), (30, 50), (28, 46), (23, 40),
     (19, 42), (12, 44), (8, 44), (3, 42), (0, 38), (-6, 36), (-10, 36)],
    [(-6, 35), (0, 36), (10, 37), (20, 32), (30, 31), (35, 28), (37, 22),
     (40, 15), (43, 11), (48, 11), (51, 10), (44, 0), (40, -10), (35, -18),
     (32, -26), (28, -33), (20, -35), (16, -29), (12, -18), (9, -1), (9, 4),
     (4, 6), (-8, 5), (-13, 8), (-17, 15), (-16, 20), (-15, 25), (-10, 30),
     (-6, 35)],
    [(30, 62), (40, 68), (50, 69), (60, 70), (70, 72), (80, 73), (90, 75),
     (100, 76), (110, 74), (120, 73), (130, 72), (140, 72), (150, 70),
     (158, 66), (162, 60), (158, 55), (150, 59), (142, 55), (140, 50),
     (135, 45), (130, 42), (127, 38), (122, 38), (120, 32), (115, 25),
     (110, 20), (108, 15), (105, 10), (100, 8), (97, 10), (92, 16), (90, 22),
     (85, 20), (80, 15), (77, 8), (75, 12), (70, 20), (66, 25), (62, 25),
     (58, 26), (55, 26), (52, 28), (50, 30), (48, 30), (44, 29), (40, 30),
     (38, 32), (36, 36), (33, 40), (30, 42), (28, 45), (30, 50), (30, 55),
     (30, 62)],
    [(113, -22), (114, -30), (115, -35), (120, -34), (125, -32), (130, -32),
     (135, -35), (140, -38), (145, -38), (150, -37), (153, -32), (153, -27),
     (150, -22), (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
     (132, -12), (130, -13), (126, -14), (122, -17), (118, -20), (113, -22)],
]
