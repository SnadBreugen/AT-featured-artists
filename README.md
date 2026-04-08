# Audiotool Featured Artists Archive

A static archive of all Gen II Featured Artists (2021–2026) from the Audiotool message board.

## Files

- `index.html` — Grid overview of all artists
- `artist.html` — Individual artist page (loads via `?id=ArtistName`)
- `data.json` — Complete database of all 66 artists

## Usage

Works as a static site — no build step needed. Just open `index.html` in a browser, or host on GitHub Pages.

### GitHub Pages

1. Push to a repo
2. Settings → Pages → Source: `main` branch, `/ (root)`
3. Done — available at `https://username.github.io/repo-name/`

## Data Structure

Each artist in `data.json`:

```json
{
  "artist": "Artist Name",
  "real_name": "Real Name",
  "date": "YYYY-MM-DD",
  "board_url": "https://audiotool.com/board/...",
  "album_url": "https://audiotool.com/album/...",
  "at_profile": "https://audiotool.com/user/...",
  "soundcloud": "https://soundcloud.com/...",
  "intro": "Moderator intro text",
  "about": "Artist self-description",
  "tracks": [
    { "url": "https://audiotool.com/track/...", "desc": "Artist comment" }
  ]
}
```
