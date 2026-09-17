# E-LECTION 2024 🇮🇳

Two frontends, same streamlined flow: **Nomination → Voting → Results**.

| File | What |
|---|---|
| `Election.py` | Python CLI (stdlib only, no deps): nominate → vote with Voter IDs → end → results |
| `index.html` | Vanilla HTML/JS web UI (no deps): same flow + secret ballot + tricolor theme |

## Flow

1. **Nomination** — nominate candidates (min 2). Voting stays locked.
2. **Voting** — voters vote with a unique Voter ID (1 vote each, duplicates rejected). No running tallies shown while voting (secret ballot).
3. **Results** — End Election locks voting and declares winner/runner-up + full tally + distribution chart.

`↺ New Election` reset is hidden during voting to prevent mid-election wipes.

Web data persists in `localStorage`; the CLI is in-memory (browser-local/in-memory demo — add a backend + OTP/ID verification for real elections).

## Run

```
python Election.py
python -m http.server 8000
# open http://localhost:8000/index.html
```
