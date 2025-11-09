"""
data_cleaning.py
----------------
Handles loading, merging, and cleaning World Happiness datasets.
"""

import pandas as pd
import os

def load_and_clean_data(data_dir="../data"):
    """Load multiple CSVs, combine and clean them."""
    all_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]
    df_list = []

    for file in all_files:
        temp = pd.read_csv(os.path.join(data_dir, file))
        temp["year"] = int(file.replace(".csv", ""))
        df_list.append(temp)

    df = pd.concat(df_list, ignore_index=True)

    # Standardize columns
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    # Select important columns
    cols_to_keep = [
        "country", "year", "happiness_score", "gdp_per_capita", "social_support",
        "healthy_life_expectancy", "freedom_to_make_life_choices", "generosity",
        "perceptions_of_corruption"
    ]
    df = df[[col for col in cols_to_keep if col in df.columns]]

    # Drop duplicates and fill missing
    df.drop_duplicates(inplace=True)
    df.fillna(df.median(numeric_only=True), inplace=True)
    df.fillna("Unknown", inplace=True)

    return df
