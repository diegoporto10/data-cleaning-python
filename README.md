# Python Data Cleaning Script

Reusable **Pandas** pipeline for fast data cleaning:
- Standardizes column names to `snake_case`
- Trims strings and converts `"nan"`, `""` to missing
- Drops duplicate rows
- Coerces numeric types (smart: `Int64` only if all values are whole numbers, else `Float64`)
- Adds `age_group` and `tenure_group` helper bands

## Quickstart

### Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1   # if blocked: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
python -m pip install -r requirements.txt

python src\clean.py --input data\raw\sample.csv --output data\processed\clean.csv --int-cols age
start data\processed\clean.csv
