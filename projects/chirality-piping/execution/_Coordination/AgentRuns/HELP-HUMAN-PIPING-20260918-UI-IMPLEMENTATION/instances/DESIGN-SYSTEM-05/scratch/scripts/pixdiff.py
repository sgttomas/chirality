# Pixel-level comparison of two renderings, section by section.  python3 pixdiff.py <base dir> <new dir> <prefix e.g. 1440->
import sys, os
from PIL import Image, ImageChops
base, new, prefix = sys.argv[1:4]
names = sorted(f for f in os.listdir(new) if f.startswith(prefix) and f.endswith(".png"))
for f in names:
    a = Image.open(os.path.join(base, f)).convert("RGB"); b = Image.open(os.path.join(new, f)).convert("RGB")
    if a.size != b.size:
        print(f"{f}: size {a.size} -> {b.size}"); 
        w = min(a.size[0], b.size[0]); h = min(a.size[1], b.size[1]); a2 = a.crop((0, 0, w, h)); b2 = b.crop((0, 0, w, h))
    else:
        a2, b2 = a, b
    d = ImageChops.difference(a2, b2); bbox = d.getbbox()
    if not bbox:
        print(f"{f}: identical pixels" + ("" if a.size == b.size else " in the common area")); continue
    g = d.convert("L"); hist = g.histogram(); n = sum(hist[1:]); big = sum(hist[17:]); mx = max(i for i, c in enumerate(hist) if c)
    print(f"{f}: {n} px differ ({big} by more than 16/255, max {mx}), bbox {bbox}, image {a2.size}")
