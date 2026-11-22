"""Deterministic front-page image for Sunday 22 November 2026.

Renders one 1024x1024 newspaper-style summary of the day's world news
using only Pillow. Fixed data, fixed fonts, no randomness, no network:
the same bytes come out on every run.
"""
from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024
PAPER = (247, 242, 231)
INK = (17, 24, 39)
MUTED = (92, 99, 112)
RULE = (17, 24, 39)
RED = (185, 28, 28)
TEAL = (15, 118, 110)
GOLD = (180, 83, 9)
BLUE = (30, 64, 175)
CARD = (255, 253, 247)
CARD_LINE = (209, 201, 182)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, xy, text, fnt, fill, max_width, leading):
    x, y = xy
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


DATE_LINE = "SUNDAY  22 NOVEMBER 2026"
MASTHEAD = "THE WORLD TODAY"
TAGLINE = "One day, one page: the stories the world woke up to"

LEAD_KICKER = "CLIMATE  -  ANTALYA, TURKIYE"
LEAD_HEADLINE = "COP31 runs into overtime as fossil-fuel talks deadlock"
LEAD_BODY = (
    "Delegates at the UN climate summit in Antalya pushed past their "
    "deadline with no final deal. The EU said there was still no "
    "agreement on phasing out fossil fuels."
)
LEAD_FACT = "197 countries  -  summit ran 9-20 Nov, extended 22 Nov"

STORIES = [
    {
        "kicker": "MIDDLE EAST  -  BAHRAIN",
        "color": RED,
        "headline": "Iranian attack hits Bahrain industrial site",
        "body": (
            "Bahrain said an Iranian attack struck an industrial "
            "facility while its air defences intercepted other "
            "attacks, raising tension across the Gulf."
        ),
    },
    {
        "kicker": "MEXICO  -  CARTEL ARREST",
        "color": GOLD,
        "headline": "Mexico captures cartel boss 'El Chapo Isidro'",
        "body": (
            "Soldiers captured Fausto Isidro Meza Flores, on the "
            "FBI most-wanted list, in a military raid. Violence "
            "after the arrest left 11 people dead."
        ),
    },
    {
        "kicker": "UKRAINE  -  WAR",
        "color": BLUE,
        "headline": "Russia strikes Kryvyi Rih; ship ablaze in Gulf of Finland",
        "body": (
            "Russian missiles hit Zelenskyy's home town, killing "
            "a child and wounding dozens. A Russia-bound ship "
            "caught fire after a drone hit; crew evacuated."
        ),
    },
    {
        "kicker": "UNITED STATES  -  FBI",
        "color": TEAL,
        "headline": "FBI probes apparent hack of its crime database",
        "body": (
            "The FBI is investigating an apparent hack of the "
            "national crime database used for warrants and "
            "fugitives. The scope is still unclear."
        ),
    },
    {
        "kicker": "PERU  -  EARTHQUAKE",
        "color": GOLD,
        "headline": "Magnitude 6.7 quake shakes Peru's Andes",
        "body": (
            "A strong 6.7 earthquake struck the Peruvian "
            "mountains. Early reports brought no confirmed "
            "deaths or major damage."
        ),
    },
    {
        "kicker": "PORTUGAL  -  PROTESTS",
        "color": RED,
        "headline": "Thousands march in Lisbon over cost of living",
        "body": (
            "Thousands protested in Lisbon against inflation "
            "and rising living costs, joining a weekend of "
            "demonstrations across Europe."
        ),
    },
]


def masthead(draw):
    draw.rectangle([0, 0, W, 10], fill=RED)
    y = 24
    small = font(SANS_BOLD, 20)
    width = draw.textlength(DATE_LINE, font=small)
    draw.text(((W - width) / 2, y), DATE_LINE, font=small, fill=RED)
    y += 30
    big = font(SERIF_BOLD, 68)
    width = draw.textlength(MASTHEAD, font=big)
    draw.text(((W - width) / 2, y), MASTHEAD, font=big, fill=INK)
    y += 82
    tag = font(SERIF, 20)
    width = draw.textlength(TAGLINE, font=tag)
    draw.text(((W - width) / 2, y), TAGLINE, font=tag, fill=MUTED)
    y += 30
    draw.line([48, y, W - 48, y], fill=RULE, width=4)
    draw.line([48, y + 7, W - 48, y + 7], fill=RULE, width=1)
    return y + 16


def lead_block(draw, top):
    left = 48
    right = W - 48
    draw.rectangle([left, top, right, top + 212], fill=CARD, outline=CARD_LINE, width=2)
    draw.rectangle([left, top, left + 10, top + 212], fill=TEAL)
    x = left + 34
    y = top + 16
    draw.text((x, y), LEAD_KICKER, font=font(SANS_BOLD, 19), fill=TEAL)
    y += 30
    y = draw_wrapped(draw, (x, y), LEAD_HEADLINE, font(SERIF_BOLD, 36), INK, right - x - 28, 41)
    y += 6
    y = draw_wrapped(draw, (x, y), LEAD_BODY, font(SANS, 19), INK, right - x - 28, 25)
    y += 8
    draw.text((x, y), LEAD_FACT, font=font(SANS_BOLD, 16), fill=MUTED)
    return top + 212 + 10


def story_card(draw, left, top, width, height, story):
    draw.rectangle([left, top, left + width, top + height], fill=CARD, outline=CARD_LINE, width=2)
    draw.rectangle([left, top, left + width, top + 8], fill=story["color"])
    x = left + 20
    y = top + 22
    draw.text((x, y), story["kicker"], font=font(SANS_BOLD, 15), fill=story["color"])
    y += 26
    y = draw_wrapped(draw, (x, y), story["headline"], font(SERIF_BOLD, 23), INK, width - 40, 26)
    y += 5
    draw_wrapped(draw, (x, y), story["body"], font(SANS, 15), INK, width - 40, 20)


def footer(draw, top):
    draw.line([48, top, W - 48, top], fill=RULE, width=2)
    line1 = "22 NOVEMBER 2026  -  SIX STORIES, FIVE CONTINENTS, ONE PAGE"
    f1 = font(SANS_BOLD, 17)
    w1 = draw.textlength(line1, font=f1)
    draw.text(((W - w1) / 2, top + 12), line1, font=f1, fill=INK)
    line2 = "Sources: Reuters, AP, BBC and Al Jazeera reports of 22 November 2026"
    f2 = font(SANS, 15)
    w2 = draw.textlength(line2, font=f2)
    draw.text(((W - w2) / 2, top + 38), line2, font=f2, fill=MUTED)


def build(path):
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    y = masthead(draw)
    y = lead_block(draw, y)
    col_w = (W - 96 - 20) // 2
    row_h = 166
    for idx, story in enumerate(STORIES):
        col = idx % 2
        row = idx // 2
        left = 48 + col * (col_w + 20)
        top = y + row * (row_h + 12)
        story_card(draw, left, top, col_w, row_h, story)
    footer_top = y + 3 * (row_h + 12) + 2
    footer(draw, footer_top)
    img.save(path, format="PNG", optimize=True)
    return path


if __name__ == "__main__":
    build("entry.png")
