---
name: get-gif
description: "Search GIF providers with CLI/TUI, download results, and extract stills/sheets."
description_zh: "搜索和下载 GIF 动图"
description_en: "Search and download GIFs"
version: 1.0.2
display_name: "get-gif"
display_name_en: "get-gif"
visibility: "public"
---

# get-gif

Use `get-gif` to search GIF providers (Tenor/Giphy), browse in a TUI, download results, and extract stills or sheets.

GIF-Grab (get-gif workflow)

- Search > preview > download > extract (still/sheet) for fast review and sharing.

Quick start

- `get-gif cats` - 搜索一个 GIF（默认）
- `get-gif cats --max 5` - 搜索多个 GIF
- `get-gif cats --format url` - 只输出 URL
- `get-gif search --json cats | jq '.[0].url'`
- `get-gif tui "office handshake"`
- `get-gif cats --download --format url`

TUI + previews

- TUI: `get-gif tui "query"`
- CLI still previews: `--thumbs` (Kitty/Ghostty only; still frame)

Download + reveal

- `--download` saves to `~/Downloads`
- `--reveal` shows the last download in Finder

Stills + sheets

- `get-gif still ./clip.gif --at 1.5s -o still.png`
- `get-gif sheet ./clip.gif --frames 9 --cols 3 -o sheet.png`
- Sheets = single PNG grid of sampled frames (great for quick review, docs, PRs, chat).
- Tune: `--frames` (count), `--cols` (grid width), `--padding` (spacing).

Providers

- `--source auto|tenor|giphy`
- `GIPHY_API_KEY` required for `--source giphy`
- `TENOR_API_KEY` optional (Tenor demo key used if unset)

Output

- `--json` prints an array of results (`id`, `title`, `url`, `preview_url`, `tags`, `width`, `height`)
- `--format` for pipe-friendly fields (e.g., `url`)

Environment tweaks

- `GET_GIF_SOFTWARE_ANIM=1` to force software animation
- `GET_GIF_CELL_ASPECT=0.5` to tweak preview geometry
