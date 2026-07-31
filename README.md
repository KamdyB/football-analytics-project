# ⚽ Football Analytics Project

A Python-based football analytics engineering project focused on building a reproducible data pipeline for analyzing the 2024/25 EFL Championship season. This repository documents my transition from writing standalone Python scripts to developing modular, maintainable software for football data analysis.

Rather than treating analytics as isolated notebooks or one-off scripts, this project is being developed as an engineering codebase where reusable functions, structured workflows, and version control are prioritized from the beginning.

---

# 🎯 Project Objective

The goal of this project is to build a complete football analytics pipeline that follows the same stages used in professional data teams:

* Data acquisition
* Data inspection and validation
* Data cleaning
* Feature engineering
* Exploratory data analysis
* Data visualization
* Analytical reporting

Every stage of development is version-controlled and documented to demonstrate both analytical reasoning and software engineering practices.

---

# 📊 Data Source

This project uses football data from **FBref**, accessed programmatically through the `soccerdata` Python library. During development, datasets may also be stored locally as CSV files for testing and reproducibility.

---

# 🛠️ Technologies

* Python
* Pandas
* NumPy
* soccerdata
* Matplotlib
* Git
* GitHub

---

# 📂 Current Repository Structure

```text
football-analytics-project/
│
├── dashboard/
│   └── scouting_dashboard...
│
├── data/
│   ├── championship_player_stats.csv
│   └── championship_schedule.csv
│
├── downloaded_files/
│   └── (temporary downloaded datasets)
│
├── scripts/
│   ├── analyse_data.py
│   ├── football_utils.py
│   └── scrape_fbref.py
│
├── sql/
│   └── analytical_queries.sql
│
├── README.md
└── requirements.txt
```

This structure will continue evolving as additional modules are introduced for data loading, cleaning, validation, feature engineering, and visualization.

## 📁 Directory Overview

| Folder | Purpose |
|---------|---------|
| **dashboard/** | Stores dashboards and visualizations created during the project. |
| **data/** | Contains Championship datasets used for analysis. |
| **downloaded_files/** | Temporary storage for downloaded data before processing. |
| **scripts/** | Core Python scripts for scraping, utility functions, and analysis workflows. |
| **sql/** | SQL queries used for analytical tasks and database exploration. |

---

# 🚀 Current Progress

### ✅ Project Setup

* Initialized Git repository
* Organized project structure
* Created reusable utility module

### ✅ Reusable Football Functions

Implemented reusable functions including:

* Goal difference calculation
* League points calculation
* Minutes per 90 calculation
* Player age classification
* Column name standardization

### ✅ Dataset Inspection Workflow

Built an inspection workflow for newly imported datasets using:

* `head()`
* `shape`
* `columns`
* `info()`
* `isna().sum()`
* `describe()`

This ensures datasets are validated before analysis begins.

---

# 🧠 Engineering Principles Practiced

This repository emphasizes software engineering concepts alongside data analysis, including:

* Modular programming
* Reusable functions
* Single Responsibility Principle
* Data validation before analysis
* Consistent naming conventions
* Version control with Git
* Incremental project development

---

# 🗺️ Roadmap

## Phase 1 — Project Foundations ✅

* Project setup
* Utility functions
* Dataset inspection

## Phase 2 — Data Engineering

* Import Championship datasets
* Data cleaning
* Missing value handling
* Column standardization
* Validation pipeline

## Phase 3 — Football Analytics

* Player performance metrics
* Team analysis
* Per-90 statistics
* Expected Goals (xG)
* Expected Assists (xA)

## Phase 4 — Visualization

* Performance dashboards
* Team comparisons
* Player comparisons
* Statistical graphics

## Phase 5 — Reporting

* Analytical reports
* Match summaries
* Scouting insights
* Portfolio case studies

---

# ▶️ Getting Started

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dataset inspection workflow:

```bash
python inspect_dataset.py
```

---

# 📚 Learning Journey

This repository serves as a public record of my progression into football analytics engineering. Each commit represents a genuine stage of learning, with an emphasis on writing clean, reusable, and maintainable code rather than simply completing tutorials.

The long-term objective is to develop a production-style analytics pipeline capable of supporting meaningful football analysis while demonstrating professional software engineering practices.

---

# 📌 Future Enhancements

* Automated data ingestion
* Feature engineering modules
* Statistical modelling
* Interactive dashboards
* Match prediction experiments
* Player scouting workflows
* Performance reporting

---

## Author

**Blossom**

Aspiring Football Analytics Engineer | Computer Science Student | Building reusable analytics systems with Python, data engineering principles, and football data.
