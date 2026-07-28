# Problems Solved

- Resolved a FileNotFoundError by correcting the dataset path.
- Successfully imported the raw FBref Championship dataset into pandas.
- Promoted the embedded header row to become the DataFrame column names.
- Parsed FBref's hierarchical column headers into SQL-friendly unique feature names while preserving the original statistical categories.
- Standardized column names for easier SQL querying.
- Removed duplicate rows.
- Removed records with missing player names.
- Exported a clean CSV for downstream SQL analysis and Power BI visualization.