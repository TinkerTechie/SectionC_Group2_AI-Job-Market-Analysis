"""ETL Pipeline for the AI Job Trends Analysis project.

This script extracts the raw AI Job Trends dataset, standardizes column formats,
cleans inconsistent categorical and numerical data, and exports a finalized
dataset optimized for exploratory data analysis and visualization.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to a clean snake_case format."""
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    result = df.copy()
    result.columns = cleaned
    return result


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply safe default cleaning steps."""
    result = normalize_columns(df)
    result = result.drop_duplicates().reset_index(drop=True)

    for column in result.select_dtypes(include="object").columns:
        result[column] = result[column].astype("string").str.strip()

    return result


def apply_domain_transformations(df: pd.DataFrame) -> pd.DataFrame:
    """Apply dataset-specific cleaning for the AI Job Trends dataset."""
    result = df.copy()

    # 1. Handle missing values in location.
    if "location" in result.columns:
        mode_location = result["location"].mode(dropna=True)
        if not mode_location.empty:
            result["location"] = result["location"].fillna(mode_location.iloc[0])

    # 2. Standardize categorical values.
    if "required_education" in result.columns:
        result["required_education"] = (
            result["required_education"]
            .astype("string")
            .str.strip()
            .str.lower()
            .replace(
                {
                    "bachelors": "Bachelor's Degree",
                    "bachelor's": "Bachelor's Degree",
                    "masters": "Master's Degree",
                    "master's": "Master's Degree",
                }
            )
        )

    # 3. Clean numerical columns.
    if "median_salary_usd" in result.columns:
        salary_series = (
            result["median_salary_usd"]
            .astype("string")
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
        )
        result["median_salary_usd"] = pd.to_numeric(salary_series, errors="coerce")

    if "experience_required_years" in result.columns:
        experience_series = (
            result["experience_required_years"]
            .astype("string")
            .str.replace(" yrs", "", regex=False)
            .str.replace(" years", "", regex=False)
            .str.strip()
        )
        result["experience_required_years"] = pd.to_numeric(
            experience_series, errors="coerce"
        ).astype("Int64")

    return result


def build_clean_dataset(input_path: Path) -> pd.DataFrame:
    """Read a raw CSV file and return a cleaned dataframe."""
    df = pd.read_csv(input_path)
    df_basic = basic_clean(df)
    df_final = apply_domain_transformations(df_basic)
    return df_final


def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    """Write the cleaned dataframe to disk, creating the parent folder if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run the AI Job Trends ETL pipeline.")
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to the raw CSV file in data/raw/.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to the cleaned CSV file in data/processed/.",
    )
    return parser.parse_args()


def main() -> None:
    """Execute the ETL pipeline end-to-end."""
    args = parse_args()
    cleaned_df = build_clean_dataset(args.input)
    save_processed(cleaned_df, args.output)
    print(f"Processed dataset saved to: {args.output}")
    print(f"Rows: {len(cleaned_df)} | Columns: {len(cleaned_df.columns)}")


if __name__ == "__main__":
    main()
