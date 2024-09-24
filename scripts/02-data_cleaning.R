#### Preamble ####
# Purpose: Cleans the raw data (titled "Shooting Occurrences") from OpenDataToronto.
# Author: Xingjie Yao
# Date: 27 September 2024
# Contact: xingjie.yao@mail.utoronto.ca
# License: MIT
# Pre-requisites: The dataset of interest includes all shooting occurrences from 2014 to 2019 by occurred date aggregated by Division.  
# Any other information needed? Shootings in this data set include both firearm discharges and shooting events. 


#### Workspace setup ####
library(opendatatoronto)
library(tidyverse)
library(dplyr)

#### Clean data ####
raw_data <- read_csv("inputs/data/raw_data/shooting_occurrence.csv")
# clean the dataset accordingly and save the dataset
clean <- data.frame(id=raw_data$Index_, year=raw_data$OccurredYear, division=raw_data$GeoDivision, count=raw_data$Count_)
glimpse(clean)
any(is.na(clean)) # check for missing values

#### Save data ####
write_csv(clean, "inputs/data/analysis_data/cleaned_shooting_occurrence.csv") 
