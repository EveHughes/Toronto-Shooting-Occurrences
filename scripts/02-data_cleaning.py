#### Preamble ####
# Purpose: Cleans the raw data (titled "Shooting Occurrences") from OpenDataToronto.
# Author: Xingjie Yao
# Date: 27 September 2024
# Contact: xingjie.yao@mail.utoronto.ca
# License: MIT
# Pre-requisites: The dataset of interest includes all shooting occurrences from 2014 to 2019 by occurred date aggregated by Division.  
# Any other information needed? Shootings in this data set include both firearm discharges and shooting events. 

#### Workspace setup ####
import pandas as pd

#### Clean data ####
# Read raw data
raw_data = pd.read_csv("data/raw_data/shooting_occurrence.csv")

# Select and rename relevant columns
clean = raw_data.rename(columns={
    "Index_": "id",
    "OccurredYear": "year",
    "GeoDivision": "division",
    "Count_": "count"
})[["id", "year", "division", "count"]]

# Display structure and check for missing values
print(clean.info())
print("Any missing values?", clean.isna().any().any())

#### Save data ####
clean.to_csv("data/analysis_data/cleaned_shooting_occurrence.csv", index=False)
