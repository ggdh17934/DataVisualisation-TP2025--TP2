"""TP2: the requested sales wrangling and variable-classification exercises."""
# %% 1. Load the specified CSV and inspect it
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
DATA = ROOT / "data" / "sales.csv"
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)
URL = "https://raw.githubusercontent.com/PacktPublishing/Hands-on-Exploratory-Data-Analysis-with-Python/refs/heads/master/Chapter%204/sales.csv"
df_sales = pd.read_csv(DATA if DATA.exists() else URL)
print(df_sales.head().to_string(index=False))
df_sales.info()

# %% 2. TotalPrice and the exact 3,000,000 outlier threshold
df_sales["TotalPrice"] = df_sales["Quantity"] * df_sales["UnitPrice"]
print(df_sales.head().to_string(index=False))
outlier_count = df_sales.loc[df_sales["TotalPrice"] > 3_000_000].shape[0]
df_cleaned_outliers = df_sales.loc[df_sales["TotalPrice"] <= 3_000_000].copy()
row_difference = len(df_sales) - len(df_cleaned_outliers)
print("TotalPrice > 3,000,000:", outlier_count)
print("Rows removed:", row_difference)

# %% 3. Duplicates: retain the last occurrence
duplicate_count = int(df_sales.duplicated().sum())
df_no_duplicates = df_sales.drop_duplicates(keep="last").copy()
print("Duplicate rows:", duplicate_count)
print("Rows after keep='last':", len(df_no_duplicates))

# %% 4. Missing values and the field-name mismatch in the linked dataset
print("Missing values by column:\n", df_no_duplicates.isna().sum())
temporary_dropped = df_no_duplicates.dropna()
rows_lost_dropna = len(df_no_duplicates) - len(temporary_dropped)
print("Rows lost by temporary dropna:", rows_lost_dropna)

# The actual linked CSV has Account and SKU, not CustomerID and Description.
# Use transparent aliases of existing data to perform the named exercises.
df_no_duplicates["CustomerID"] = df_no_duplicates["Account"].astype("string")
df_no_duplicates["Description"] = df_no_duplicates["SKU"]
customer_missing = int(df_no_duplicates["CustomerID"].isna().sum())
df_no_duplicates["CustomerID"] = df_no_duplicates["CustomerID"].fillna("ANON")
print("CustomerID missing values filled with ANON:", customer_missing)

# %% 5. Three equal-interval Quantity bins and Country indicators
df_no_duplicates["Quantity_Bin"] = pd.cut(
    df_no_duplicates["Quantity"], bins=3,
    labels=["Low Quantity", "Medium Quantity", "High Quantity"],
)
print("Quantity_Bin counts:\n", df_no_duplicates["Quantity_Bin"].value_counts())
country_dummies = pd.get_dummies(df_no_duplicates["Country"], dtype=int)
print("Country indicators:\n", country_dummies.head())

# %% 6. Required variable classification, roles, and reliability conclusion
classification = pd.DataFrame([
    ["UnitPrice", "Quantitative", "Continuous"],
    ["Quantity", "Quantitative", "Discrete"],
    ["Description (SKU alias)", "Categorical", "Nominal"],
    ["Country", "Categorical", "Nominal"],
    ["TotalPrice", "Quantitative", "Continuous"],
    ["Quantity_Bin", "Categorical", "Ordinal"],
], columns=["Variable", "Statistical type", "Subtype"])
print(classification.to_string(index=False))
table = "| Variable | Statistical type | Subtype |\n|---|---|---|\n"
for row in classification.itertuples(index=False):
    table += f"| {row[0]} | {row[1]} | {row[2]} |\n"
report = f"""# TP2 — Answers

## Part 1: feature engineering and outliers

Loaded {len(df_sales):,} rows. TotalPrice = Quantity × UnitPrice.
Transactions strictly above 3,000,000: **{outlier_count:,}**.
Rows in df_cleaned_outliers: **{len(df_cleaned_outliers):,}**.
Difference from original: **{row_difference:,}**.

## Part 2A: wrangling

Whole-row duplicates: **{duplicate_count}**; keep='last' leaves
**{len(df_no_duplicates):,}** rows. A temporary dropna loses
**{rows_lost_dropna}** rows. Missing-value counts and bin frequencies are printed.
CustomerID values filled with ANON: **{customer_missing}**.
This real file has no missing values or duplicate rows; the required operations
are still performed, rather than injecting fabricated problems into the data.
Part 2 starts from df_sales, as requested, not the outlier-filtered subset.

**Dataset mismatch:** the assignment's URL supplies Account and SKU instead of
CustomerID and Description. CustomerID is an explicit Account alias; Description
is an explicit SKU product-label alias, not a claimed full textual description.
The original columns are retained. No invented customer IDs or descriptions are used.

## Part 2B: variable classification

{table}
Outcome: **TotalPrice**. Three proposed explanatory variables:
**Quantity**, because it directly determines the purchased amount;
**UnitPrice**, because it directly determines the price per unit;
**Country**, because product/price/quantity distributions may differ by market.
Quantity and UnitPrice already define TotalPrice exactly through multiplication;
this is an exercise in variable roles, not a claim that a regression model is needed.
The dummy dataframe contains only Country indicators: 1 means the row belongs
to that country, and 0 means it does not. Quantity_Bin is ordered Low < Medium < High.

## Part 2C: reliability — four sentences

Removing duplicates prevents repeated records from artificially weighting the analysis.
Checking missing values reveals where measurements or identifiers are incomplete.
Replacing missing customer identifiers with ANON preserves an explicit unknown category instead of claiming a known identity.
These steps improve consistency and reproducibility, but do not guarantee that every recorded value is factually correct.

Assignment: https://github.com/ahmed3991/DataVisualisation-TP2025/blob/main/TP2/TP2.md
"""
(OUT / "REPORT.md").write_text(report, encoding="utf-8")
print("Saved required answers in", OUT / "REPORT.md")
