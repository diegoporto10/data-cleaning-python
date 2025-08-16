import argparse
from pathlib import Path
import numpy as np
import pandas as pd

def snake_case(name: str) -> str:
    s = name.strip().replace("-", " ").replace("/", " ").replace(".", " ").replace("(", " ").replace(")", " ")
    s = "_".join(s.split())
    return s.lower()

def age_group(v):
    if pd.isna(v): return np.nan
    v = int(v)
    if v < 30: return "18–29"
    if v < 40: return "30–39"
    if v < 50: return "40–49"
    return "50+"

def tenure_group(v):
    if pd.isna(v): return np.nan
    v = float(v)
    if v < 1: return "<1 year"
    if v < 3: return "1–3 years"
    if v < 5: return "3–5 years"
    if v < 10: return "5–10 years"
    return "10+ years"

def clean_df(df: pd.DataFrame, int_cols=None) -> pd.DataFrame:
    df = df.copy()
    df.columns = [snake_case(c) for c in df.columns]
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].astype(str).str.strip().replace({"nan": np.nan, "None": np.nan, "": np.nan})
    df = df.drop_duplicates()
    if int_cols:
        for c in [x.strip() for x in int_cols.split(",")]:
            if c in df.columns:
                df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")
    if "age" in df.columns:
        df["age_group"] = df["age"].apply(age_group)
    if "years_at_company" in df.columns:
        df["tenure_group"] = df["years_at_company"].apply(tenure_group)
    return df

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--int-cols", default="")
    a = p.parse_args()
    inp = Path(a.input)
    out = Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(inp)
    clean = clean_df(df, int_cols=a.int_cols)
    clean.to_csv(out, index=False)
    print(f"✅ Saved {out.resolve()}")

if __name__ == "__main__":
    main()
