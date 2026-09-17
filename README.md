# E-LECTION 2024 🇮🇳

Vanilla HTML/JS election app — no dependencies, no build step. Just open `index.html`.

## Flow

1. **Nomination** — nominate candidates (min 2). Voting stays locked.
2. **Voting** — voters vote with a unique Voter ID (1 vote each, duplicates rejected). No running tallies are shown while voting (secret ballot).
3. **Results** — End Election locks voting and declares winner/runner-up + full tally + distribution chart.

`↺ New Election` reset is hidden during voting to prevent mid-election wipes.

Data persists in `localStorage` (browser-local demo — add a backend + OTP/ID verification for real elections).

## Run

```
python -m http.server 8000
# open http://localhost:8000/index.html
```

Legacy: `Election.py` (original Rich-based simulation) and `app.py` (Streamlit version) are kept for reference.
