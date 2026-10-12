# DataVisualisation-TP2025 — TP2

Simple solution of the [teacher's TP2](https://github.com/ahmed3991/DataVisualisation-TP2025/blob/main/TP2/TP2.md), covering the required tasks only.

- **TP2.ipynb**: executed notebook, with real outputs and the written answers.
- **tp2.py**: equivalent Python entry point.
- **EXPLICATION_AR.md**: Arabic explanation of each step and the results.
- **data/**: the actual source data used.
- **results/**: generated results and **REPORT.md** with the required answers.

## Run

Download `TP2.ipynb` from this private repository, upload it to [Google Colab](https://colab.research.google.com/), and choose **Runtime → Run all**. The first cell installs missing libraries. Private GitHub links can require authentication; uploading the downloaded notebook avoids that issue.

Alternatively, from this repository folder:

```sh
python -m pip install -r requirements.txt
python tp2.py
```

Verified: all notebook cells executed successfully on the supplied 10,000-row CSV; 2,094 rows exceed the specified threshold. The missing CustomerID/Description names are transparently mapped to Account/SKU, as explained in the answers.
