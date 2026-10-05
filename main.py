"""CSV converter demo — clean a prospects CSV and write a normalized output file."""
from pathlib import Path
import re
import pandas as pd

INPUT_FILE = Path("sample_input.csv")
OUTPUT_FILE = Path("prospects_clean_sample.csv")

df = pd.read_csv(INPUT_FILE)

# Basic cleanup demos
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()
    df[col] = df[col].str.replace(r"\s{2,}", " ", regex=True)

# Drop clearly empty rows
df = df.dropna(how="all")
df.to_csv(OUTPUT_FILE, index=False)
print(f"Saved cleaned CSV to: {OUTPUT_FILE.resolve()}")
print(f"Rows: {len(df)}  Columns: {len(df.columns)}")
print(df.head())
