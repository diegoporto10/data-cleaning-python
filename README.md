# Python Data Cleaning Script

Reusable **Pandas** pipeline for fast data cleaning: standardize column names, trim strings, handle nulls, drop duplicates, coerce numeric types, and derive **Age** / **Tenure** bands.

## Quickstart
```bash
python -m venv .venv && . .venv/Scripts/activate   # Windows
# . .venv/bin/activate                              # macOS / Linux
pip install -r requirements.txt
python src/clean.py --input data/raw/sample.csv --output data/processed/clean.csv --int-cols age,years_at_company
