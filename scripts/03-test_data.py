#### Preamble ####
# Purpose: Tests the variables in the cleaned dataset.
# Author: Xingjie Yao
# Date: 27 September 2024
# Contact: xingjie.yao@mail.utoronto.ca
# License: MIT
# Pre-requisites: The dataset of interest includes all shooting occurrences from 2014 to 2019 by occurred date aggregated by Division.  
# Any other information needed? Shootings in this data set include both firearm discharges and shooting events. 

#### Workspace setup ####
import pandas as pd

#### Test data ####
clean_data = pd.read_csv("inputs/data/analysis_data/cleaned_shooting_occurrence.csv")

# Check for missing values
print("Any missing values?", clean_data.isna().any().any())

# Check if 'id' is unique
is_id_unique = clean_data['id'].is_unique
print("Is 'id' unique?", is_id_unique)

# Check shooting occurrences by year
print("Occurrences by year:")
print(clean_data['year'].value_counts().sort_index())

# Check shooting occurrences by geographic division
print("Occurrences by division:")
print(clean_data['division'].value_counts().sort_index())

# Summary statistics by year
summary_by_year = clean_data.groupby("year")["count"].agg(
    n="count",
    min="min",
    Q1=lambda x: x.quantile(0.25),
    median=lambda x: x.quantile(0.5),
    Q3=lambda x: x.quantile(0.75),
    max="max",
    mean="mean",
    sd="std"
)
print("Summary by year:")
print(summary_by_year)

# Summary statistics by division
summary_by_division = clean_data.groupby("division")["count"].agg(
    n="count",
    min="min",
    Q1=lambda x: x.quantile(0.25),
    median=lambda x: x.quantile(0.5),
    Q3=lambda x: x.quantile(0.75),
    max="max",
    mean="mean",
    sd="std"
)
print("Summary by division:")
print(summary_by_division)
