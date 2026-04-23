from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1920, 1080
img = Image.new("RGB", (W, H), "#0f0808")
draw = ImageDraw.Draw(img)

try:
    font_big = ImageFont.truetype("arialbd.ttf", 88)
    font_small = ImageFont.truetype("arial.ttf", 42)
except:
    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()

cream = "#F5F0DC"
coral = "#FF6B47"

lines_big = [
    ("AMERICA'S FATE EQUALS YOUR CALL.", cream),
    ("DO NOTHING — CHINA WINS.", cream),
    ("FORWARD THIS — AMERICA LIVES.", cream, "FORWARD"),
]
lines_small = [
    "YouTube: Nir Strulovitz  |  github.com/strulovitz",
    "Everything is explained in my FREE book:",
    "github.com/strulovitz/MadHoney/blob/main/README.md",
]

total_big_h = 3 * 88 * 1.2 + 2 * 20
divider_h = 20
total_small_h = 3 * 42 * 1.4 + 2 * 10
gap = 40
total_h = total_big_h + divider_h + total_small_h + gap * 2
y = (H - total_h) / 2

for item in lines_big:
    text = item[0]
    color = item[1]
    special = item[2] if len(item) > 2 else None

    if special:
        before = special + " "
        rest = text[len(before):]
        w_before = draw.textlength(before, font=font_big)
        w_rest = draw.textlength(rest, font=font_big)
        total_w = w_before + w_rest
        x = (W - total_w) / 2
        draw.text((x, y), before, font=font_big, fill=coral)
        draw.text((x + w_before, y), rest, font=font_big, fill=cream)
    else:
        w = draw.textlength(text, font=font_big)
        draw.text(((W - w) / 2, y), text, font=font_big, fill=cream)

    y += 88 * 1.2 + 20

y += gap
draw.line([(W//2 - 300, y), (W//2 + 300, y)], fill="#4a3a3a", width=3)
y += divider_h + gap

for line in lines_small:
    w = draw.textlength(line, font=font_small)
    draw.text(((W - w) / 2, y), line, font=font_small, fill="#BDB89A")
    y += 42 * 1.4 + 10

out = os.path.join(os.path.expanduser("~"), "Downloads", "E01S77-final-screen.png")
img.save(out)
print("Saved:", out)
