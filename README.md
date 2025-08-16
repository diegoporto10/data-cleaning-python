# Python Data Cleaning Script

> Reusable **Pandas** pipeline for fast data cleaning: trim strings, coerce types, drop duplicates, standardize column names, and derive bands (e.g., **Age Group**, **Tenure Group**).

## Why
- Gets messy CSVs into analysis shape in minutes.
- Opinionated, readable, and easy to extend.

## Quickstart
```bash
# 1) create a virtual env (optional)
python -m venv .venv && . .venv/Scripts/activate  # on Windows
# . .venv/bin/activate                              # on macOS/Linux

# 2) install
pip install -r requirements.txt

# 3) run
python src/clean.py --input data/raw/sample.csv --output data/processed/clean.csv
# data-cleaning-python
Reusable Pandas pipeline for cleaning tabular data (trim, types, dedupe, banding).
