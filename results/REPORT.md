# TP2 — Answers

## Part 1: feature engineering and outliers

Loaded 10,000 rows. TotalPrice = Quantity × UnitPrice.
Transactions strictly above 3,000,000: **2,094**.
Rows in df_cleaned_outliers: **7,906**.
Difference from original: **2,094**.

## Part 2A: wrangling

Whole-row duplicates: **0**; keep='last' leaves
**10,000** rows. A temporary dropna loses
**0** rows. Missing-value counts and bin frequencies are printed.
CustomerID values filled with ANON: **0**.
This real file has no missing values or duplicate rows; the required operations
are still performed, rather than injecting fabricated problems into the data.
Part 2 starts from df_sales, as requested, not the outlier-filtered subset.

**Dataset mismatch:** the assignment's URL supplies Account and SKU instead of
CustomerID and Description. CustomerID is an explicit Account alias; Description
is an explicit SKU product-label alias, not a claimed full textual description.
The original columns are retained. No invented customer IDs or descriptions are used.

## Part 2B: variable classification

| Variable | Statistical type | Subtype |
|---|---|---|
| UnitPrice | Quantitative | Continuous |
| Quantity | Quantitative | Discrete |
| Description (SKU alias) | Categorical | Nominal |
| Country | Categorical | Nominal |
| TotalPrice | Quantitative | Continuous |
| Quantity_Bin | Categorical | Ordinal |

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
