# Lunar New Year 2026 — Year of the Horse Scavenger Hunt (Option C)

This is a **single-page static site**. Each QR code should open:

- https://YOUR-SITE-URL/?step=1
- https://YOUR-SITE-URL/?step=2
- ...
- https://YOUR-SITE-URL/?step=12

## Host it anywhere that serves static files

### GitHub Pages (fast + free)
1) Create a GitHub repo (public or private per policy)
2) Upload: index.html + clues.json
3) Repo Settings → Pages → Deploy from branch
4) Your URL will look like: https://<org>.github.io/<repo>/

### SharePoint / Internal hosting
Serve both files from the same folder. The page fetches `./clues.json`.

## After you have your base URL
Regenerate QR codes so each encodes the URL with `?step=N`.
(Ask ChatGPT to regenerate, or use the included `generate_qr.py`.)
