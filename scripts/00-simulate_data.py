#### Preamble ####
# Purpose: Simulates Toronto shooting occurrences data with 6 columns:
#          _id (Unique row identifier for Open Data database),
#          Index_ (Unique identifier),
#          OccurredYear (Year shooting occurred),
#          GeoDivision (Geographic division crime took place),
#          Category (Shooting category),
#          Count_ (Total number of shooting occurrences).
# Author: Xingjie Yao
# Date: 27 September 2024
# Contact: xingjie.yao@mail.utoronto.ca
# License: MIT
# Pre-requisites: The dataset of interest includes all shooting occurrences from 2014 to 2019 by occurred date aggregated by Division.  
# Any other information needed? Shootings in this data set include both firearm discharges and shooting events. 

#### Workspace setup ####
import pandas as pd
import numpy as np

#### Simulate data ####
np.random.seed(123456)
n = 96  # the sample size
_id = np.arange(1, n + 1)  # unique random identifiers
Index_ = np.arange(1, n + 1)  # unique random identifiers
OccurredYear = np.random.choice(np.arange(2014, 2020), size=n, replace=True)  # years 2014–2019
GeoDivision = np.random.choice(
    ["D11", "D12", "D13", "D14", "D22", "D23", "D31", "D32", "D33", "D41", "D42", "D43", "D51", "D52", "D53", "D54/D55"],
    size=n, replace=True
)
Category = ["Shooting Occurrence"] * n  # fixed value
Count_ = np.random.choice(np.arange(0, 71), size=n, replace=True)  # shooting count 0–70

shooting_data = pd.DataFrame({
    "_id": _id,
    "Index_": Index_,
    "OccurredYear": OccurredYear,
    "GeoDivision": GeoDivision,
    "Category": Category,
    "Count_": Count_
})

print(shooting_data.info())  # equivalent to glimpse in R

#### Develop some tests ####
# Check for missing values
print(any(shooting_data.isna().any()))

# Check if _id is unique
print(len(shooting_data["_id"].unique()) == len(shooting_data))

# Check if Index_ is unique
print(len(shooting_data["Index_"].unique()) == len(shooting_data))

# Check shooting occurrences by year
print(shooting_data["OccurredYear"].value_counts().sort_index())

# Check shooting occurrences by geographic division
print(shooting_data["GeoDivision"].value_counts())
