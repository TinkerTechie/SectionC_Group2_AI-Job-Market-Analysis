# AI Job Market Analysis

## Project Overview

This project analyzes the impact of Artificial Intelligence on employment trends across industries. The focus is on understanding how AI influences job growth, salary patterns, automation risk, and workforce structure, and then preparing those insights for dashboard-based decision-making.

The workflow follows a structured analytics pipeline:

- Data extraction
- Data cleaning
- Exploratory data analysis
- Statistical analysis
- Final data preparation for dashboard visualization

## Objectives

- Identify high-growth industries and job roles influenced by AI
- Analyze salary patterns across industries and experience levels
- Evaluate automation risk and its impact on job stability
- Understand workforce trends including education, experience, and remote work
- Prepare structured datasets for interactive dashboard visualization

## Dataset Description

- Dataset: AI Job Trends Dataset
- Records: approximately 30,000 job entries
- Format: structured tabular data

### Key Features

- Job Title
- Industry
- Job Openings (2024, 2030)
- Median Salary (USD)
- AI Impact Level
- Automation Risk (%)
- Required Education
- Required Experience (Years)
- Remote Work Ratio (%)

## Project Structure

```text
SectionC_Group2_AI-Job-Market-Analysis/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── notebook/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
├── scripts/
│   └── etl_pipeline.py
├── tableau/
│   ├── screenshots/
│   └── dashboard_links.md
├── report/
├── docs/
└── src/
```

## Methodology

### 1. Data Extraction

- Dataset loaded using Python and Pandas
- Initial inspection of structure, data types, and missing values

### 2. Data Cleaning and Transformation

- Standardization of column names
- Handling missing values
- Data type corrections
- Feature engineering for:
  - Growth rate
  - Risk categories
  - Growth categories

### 3. Exploratory Data Analysis

EDA is organized into four business-focused sections:

- Job Growth and Demand
- Salary Analysis
- Automation Risk
- Workforce Structure

### 4. Statistical Analysis

- Correlation analysis between key variables
- Hypothesis testing for selected business questions
- Regression models for salary and growth-related patterns

### 5. Final Data Preparation

- Column standardization
- Feature engineering
- KPI creation
- Aggregated datasets for Tableau
- Export of dashboard-ready CSV files

## Tableau Dashboards

The project includes four dashboard themes:

- Job Growth and Future Demand
- Salary Drivers and AI Impact
- Automation Risk and Job Vulnerability
- Workforce Trends and Hiring Strategy

Each dashboard is aligned with business questions derived from EDA and supported by statistical analysis.

## Key Insights

- AI-driven roles show significantly higher growth rates
- High AI impact roles command higher salaries
- Jobs with high automation risk are more likely to decline
- Mid-level experience roles dominate job demand
- Remote work is increasingly associated with competitive salaries

## Tools and Technologies

- Python
- Pandas, NumPy, Matplotlib, Seaborn
- Jupyter Notebook / Google Colab
- Tableau Public
- Git and GitHub

## How to Run

1. Clone the repository.
2. Open the notebooks in Jupyter Notebook or Google Colab.
3. Run the notebooks in order:
   `01_extraction.ipynb` -> `02_cleaning.ipynb` -> `03_eda.ipynb` -> `04_statistical_analysis.ipynb` -> `05_final_load_prep.ipynb`
4. Use the generated CSV files for Tableau dashboard creation.

## Current Status

- Data extraction and cleaning: Completed
- Exploratory data analysis: Completed
- Statistical analysis: Completed
- Final data preparation: Completed
- Dashboard development: In progress
