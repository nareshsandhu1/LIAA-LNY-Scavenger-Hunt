from pathlib import Path
import qrcode

BASE_URL = "https://YOUR-SITE-URL/"  # e.g. https://org.github.io/repo/
OUT_DIR = Path("qr_out")
OUT_DIR.mkdir(exist_ok=True)

for i in range(1, 13):
    url = f"{BASE_URL}?step={i}"
    img = qrcode.make(url)
    img.save(OUT_DIR / f"QR_{i:02d}.png")

print("Done. Check qr_out/")
