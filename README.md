# ⚽ Football Analytics — EFL Championship 2024–25

A Python data pipeline pulling FBref match and player data via `soccerdata`,
with reusable, validated football-metric functions and a dataset-inspection
workflow. Built as a portfolio project documenting real progress, including
the parts that needed rework rather than a polished-from-day-one repo.

## What's actually here right now

- **`scripts/scrape_fbref.py`** — configures `soccerdata`'s league mapping
  and pulls match schedule + player season stats from FBref, saved to CSV.
- **`scripts/football_utils.py`** — reusable functions for football-specific
  calculations: per-90 stats, goal contribution, points, age classification,
  and a header-flattening function that handles FBref's messy multi-row
  column headers. Every calculation validates its inputs (zero-division
  guards, missing-column checks, length checks) before returning a result.
- **`scripts/analyse_data.py`** — dataset inspection workflow (`head`,
  `shape`, `info`, `isna().sum()`, `describe()`) used to validate a dataset
  before analysis begins.
- **`sql/analytical_queries.sql`** — scouting-style SQL queries at varying
  complexity levels.

## Why this looks like scripts, not a finished notebook

This started as modular scripts, following a standard engineering
instinct: split code into reusable pieces. Working through it surfaced a
more useful lesson — **for a football analytics portfolio, the football
reasoning needs to be visible, not buried behind function calls.** 

That's driving the next stage of this project: consolidating the analysis
into a single notebook structured around football questions
(`championship_analysis.py`), while keeping the ETL scripts here as
the data-acquisition layer feeding it.

## Data reliability — what I assumed, and what I checked

| Failure point | What could go wrong | How it's handled | Why |
|---|---|---|---|
| Any per-90 / per-match calculation | Denominator is 0 (unused player, no matches played) | Raises `ValueError` before returning a result | An `inf` or `NaN` stat would silently corrupt a scouting comparison — better to stop and flag it |
| Adding a calculated column to a DataFrame | Expected source column (`gls`, `90s`, etc.) is missing or renamed upstream | `_require_columns()` raises a clear `KeyError` naming the missing column | A missing column should fail immediately at the source, not surface as a confusing error three functions later |
| `team_report()` | Input lists (`players`, `goals`, `assists`, `passes`) are different lengths, or empty | Raises `ValueError` before any calculation runs | A silent length mismatch would `zip()` correctly but attribute goals/assists to the wrong player |
| FBref multi-row headers | A column has no usable header at any of the three header rows | Falls back to a generated `column_N` name instead of crashing | Keeps the pipeline running on partial header data, since this is a labeling gap, not a data-integrity one |

This mirrors a broader rule I try to follow: **decide on purpose whether a
given failure should stop the program or degrade gracefully; don't let
that decision happen by accident.**

## Recently fixed (previously flagged, now resolved)

- Removed duplicate calculation logic — `add_*(df)` functions now call the
  underlying scalar functions instead of re-implementing the same math.
- Fixed `add_goal_involvement_percentage` asilently missing a `return`
  statement.
- `team_report()` rewritten to return a properly formatted string instead
  of a malformed mixed list of strings and numbers.

## Tech

Python • Pandas • `soccerdata` • SQL • Git

## Data source

FBref, accessed via the `soccerdata` library. CSVs stored locally in
`data/` during development for reproducibility.

## Running it

```bash
pip install -r requirements.txt
python scripts/scrape_fbref.py     # pulls fresh data from FBref
python scripts/analyse_data.py     # inspects the pulled dataset
```

## Roadmap

- [ ] Consolidate scripts into `championship_analysis.py`, structured
      as Football Question → Python → Insight per section
- [ ] Expand SQL scouting queries
- [ ] Publish first full write-up (LinkedIn/Substack)
- [ ] Passing-network graph module (players as nodes, pass frequency as
      edges) as a natural extension once the core notebook is done

## Author

**Blossom** — CS student building a football analytics portfolio in
public, documenting real progress including the parts that need rework.