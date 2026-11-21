"""Compose the Saturday 21 November 2026 digest at 2048px, export 1024px.

Top to bottom: kicker and masthead, region and field tally bars, the
day in numbers, three hero cards, ten mid cards in two rows, the pinned
world map beside twenty-two numbered briefs, and a date-check footer.
Every text block is capped to its measured line budget, so nothing
overflows its card. Deterministic: fixed text, fixed geometry, no
clock, no network, no randomness, so two runs write byte-identical PNGs.
"""

import os

from PIL import Image, ImageDraw

import data
from draw import (centered_text, draw_map_pin, draw_world_map,
                  draw_wrapped, load_font, rule, shrink_to_fit, wrap_lines)
from scenes import PAINTERS

PAGE_W = 2048
PAGE_H = 2048
MARGIN = 64
CONTENT_W = PAGE_W - 2 * MARGIN
PAPER = (247, 241, 222)
CARD_BG = (253, 250, 242)
INK = (26, 25, 22)
MUTED = (96, 89, 74)
ACCENT_RED = (176, 32, 26)
RULE = (58, 54, 46)
SEA_FILL = (206, 220, 222)
LAND_FILL = (122, 142, 108)
PIN_FILL = (190, 44, 34)
CARD_LINE = (216, 207, 184)


def _tally_line(parts):
    joined = "   ·   ".join(parts)
    return joined


def _draw_header(page_draw):
    kicker_font = load_font("sans-xbold", 30)
    page_draw.text((MARGIN, 40), data.PAGE_KICKER_LEFT, font=kicker_font,
                   fill=ACCENT_RED)
    right_font = load_font("sans-bold", 24)
    right_width = page_draw.textlength(data.PAGE_KICKER_RIGHT, font=right_font)
    page_draw.text((PAGE_W - MARGIN - right_width, 44),
                   data.PAGE_KICKER_RIGHT, font=right_font, fill=MUTED)
    rule(page_draw, MARGIN, 84, CONTENT_W, RULE, 4)
    mast_font = load_font("serif-bold", 108)
    fitted = shrink_to_fit(page_draw, data.DAY_LABEL, "serif-bold", 108,
                           CONTENT_W)
    centered_text(page_draw, data.DAY_LABEL, fitted, PAGE_W // 2, 100, INK)
    sub_font = load_font("serif", 40)
    sub_fitted = shrink_to_fit(page_draw, data.PAGE_SUBTITLE, "serif", 40,
                               CONTENT_W)
    centered_text(page_draw, data.PAGE_SUBTITLE, sub_fitted, PAGE_W // 2, 224,
                  MUTED)
    rule(page_draw, MARGIN, 282, CONTENT_W, RULE, 4)


def _draw_tally(page_draw):
    region_parts = []
    for (name, count) in data.REGION_COUNTS:
        region_parts.append(name.upper() + " " + str(count))
    region_line = "REGIONS   " + _tally_line(region_parts)
    region_fitted = shrink_to_fit(page_draw, region_line, "sans-bold", 27,
                                  CONTENT_W)
    page_draw.text((MARGIN, 296), region_line, font=region_fitted, fill=INK)
    field_parts = []
    for (name, count) in data.FIELD_COUNTS:
        field_parts.append(name.upper() + " " + str(count))
    field_line = "FIELDS   " + _tally_line(field_parts)
    field_fitted = shrink_to_fit(page_draw, field_line, "sans", 25,
                                 CONTENT_W)
    page_draw.text((MARGIN, 330), field_line, font=field_fitted, fill=MUTED)
    rule(page_draw, MARGIN, 366, CONTENT_W, RULE, 3)


def _draw_numbers(page_draw):
    label_font = load_font("sans-xbold", 24)
    page_draw.text((MARGIN, 384), "THE DAY IN NUMBERS", font=label_font,
                   fill=ACCENT_RED)
    cell_w = CONTENT_W // 8
    for idx, (big, small) in enumerate(data.NUMBERS_STRIP):
        cx = MARGIN + idx * cell_w
        big_font = shrink_to_fit(page_draw, big, "sans-xbold", 46,
                                 cell_w - 16)
        centered_text(page_draw, big, big_font, cx + cell_w // 2, 414, INK)
        small_font = load_font("sans", 21)
        lines = wrap_lines(page_draw, small, small_font, cell_w - 16)
        ly = 470
        for line in lines[:2]:
            centered_text(page_draw, line, small_font, cx + cell_w // 2, ly,
                          MUTED)
            ly = ly + 24
    rule(page_draw, MARGIN, 528, CONTENT_W, RULE, 3)


def _draw_card(page_draw, story, x, y, w, h, hero):
    page_draw.rectangle([x, y, x + w, y + h], fill=CARD_BG,
                        outline=CARD_LINE, width=2)
    painter = PAINTERS[story["scene"]]
    scene_h = 168
    if hero is False:
        scene_h = 88
    painter(page_draw, x + 2, y + 2, w - 4, scene_h)
    num_size = 30
    if hero is False:
        num_size = 24
    num_font = load_font("sans-xbold", num_size)
    num_text = str(story["num"])
    badge_r = 23
    if hero is False:
        badge_r = 19
    badge_cx = x + 40
    badge_cy = y + scene_h - 24
    page_draw.ellipse([badge_cx - badge_r, badge_cy - badge_r,
                       badge_cx + badge_r, badge_cy + badge_r],
                      fill=PIN_FILL)
    tw = page_draw.textlength(num_text, font=num_font)
    page_draw.text((badge_cx - tw / 2, badge_cy - num_font.size // 2 - 2),
                   num_text, font=num_font, fill=(255, 255, 255))
    tag_size = 24
    if hero is False:
        tag_size = 20
    tag_font = load_font("sans-bold", tag_size)
    tag_fitted = shrink_to_fit(page_draw, story["tag"], "sans-bold",
                               tag_size, w - 28)
    page_draw.text((x + 14, y + scene_h + 12), story["tag"],
                   font=tag_fitted, fill=ACCENT_RED)
    head_size = 40
    if hero is False:
        head_size = 28
    head_font = load_font("serif-bold", head_size)
    head_lines = wrap_lines(page_draw, story["headline"], head_font, w - 28)
    hy = y + scene_h + 48
    if hero is False:
        hy = y + scene_h + 40
    for line in head_lines[:2]:
        page_draw.text((x + 14, hy), line, font=head_font, fill=INK)
        hy = hy + head_size + 4
    sum_size = 24
    if hero is False:
        sum_size = 22
    sum_lead = 4
    if hero is False:
        sum_lead = 2
    sum_cap = 3
    if hero is False:
        sum_cap = 2
    sum_font = load_font("sans", sum_size)
    sum_lines = wrap_lines(page_draw, story["summary"], sum_font, w - 28)
    sy = hy + 4
    for line in sum_lines[:sum_cap]:
        page_draw.text((x + 14, sy), line, font=sum_font, fill=MUTED)
        sy = sy + sum_size + sum_lead
    return sy


def _draw_heroes(page_draw):
    gap = 24
    card_w = (CONTENT_W - 2 * gap) // 3
    card_h = 400
    top = 544
    for idx, story in enumerate(data.HEROES):
        x = MARGIN + idx * (card_w + gap)
        _draw_card(page_draw, story, x, top, card_w, card_h, True)


def _draw_mids(page_draw):
    gap = 20
    card_w = (CONTENT_W - 4 * gap) // 5
    card_h = 248
    tops = [956, 1212]
    for row in range(2):
        for col in range(5):
            story = data.MIDS[row * 5 + col]
            x = MARGIN + col * (card_w + gap)
            _draw_card(page_draw, story, x, tops[row], card_w, card_h, False)


def _draw_map_and_briefs(page_draw):
    top = 1476
    band_h = 504
    map_x = MARGIN
    map_w = 880
    map_y = top + 44
    map_h = band_h - 44
    label_font = load_font("sans-xbold", 26)
    page_draw.text((map_x, top + 4), "WHERE IT HAPPENED",
                   font=label_font, fill=ACCENT_RED)
    draw_world_map(page_draw, map_x, map_y, map_w, map_h, SEA_FILL,
                   LAND_FILL, PIN_FILL, INK)
    for (num, lon, lat) in data.PIN_SPOTS:
        draw_map_pin(page_draw, map_x, map_y, map_w, map_h, lon, lat, num,
                     PIN_FILL, INK, (255, 255, 255))
    brief_x = MARGIN + map_w + 32
    brief_w = CONTENT_W - map_w - 32
    page_draw.text((brief_x, top + 4), "THE REST OF THE DAY",
                   font=label_font, fill=ACCENT_RED)
    col_w = (brief_w - 24) // 2
    brief_font = load_font("sans", 20)
    num_font = load_font("sans-bold", 20)
    row_h = 44
    for idx, (num, text, _lon, _lat) in enumerate(data.BRIEFS):
        col = idx // 11
        row = idx % 11
        bx = brief_x + col * (col_w + 24)
        by = top + 44 + row * row_h
        num_text = str(num) + "."
        page_draw.text((bx, by), num_text, font=num_font, fill=ACCENT_RED)
        lines = wrap_lines(page_draw, text, brief_font, col_w - 48)
        ly = by
        for line in lines[:2]:
            page_draw.text((bx + 48, ly), line, font=brief_font, fill=INK)
            ly = ly + 21


def _draw_footer(page_draw):
    rule(page_draw, MARGIN, 2012, CONTENT_W, RULE, 3)
    foot_font = load_font("sans", 21)
    lines = wrap_lines(page_draw, data.FOOTER_CHECK, foot_font, CONTENT_W)
    fy = 2022
    for line in lines[:1]:
        page_draw.text((MARGIN, fy), line, font=foot_font, fill=MUTED)
        fy = fy + 24


def build_page():
    page = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    page_draw = ImageDraw.Draw(page)
    _draw_header(page_draw)
    _draw_tally(page_draw)
    _draw_numbers(page_draw)
    _draw_heroes(page_draw)
    _draw_mids(page_draw)
    _draw_map_and_briefs(page_draw)
    _draw_footer(page_draw)
    return page


def main():
    out_dir = os.environ.get("MAKEFUN_OUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    page = build_page()
    small = page.resize((1024, 1024), Image.LANCZOS)
    small.save(os.path.join(out_dir, "entry.png"), optimize=True)
    page.save(os.path.join(out_dir, "master-2048.png"))
    saved = os.path.join(out_dir, "entry.png")
    return saved


if __name__ == "__main__":
    main()
