#### Preamble ####
# Purpose: Tests the variables in the cleaned dataset.
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

#### Test data ####
clean_data <- read_csv("inputs/data/analysis_data/cleaned_shooting_occurrence.csv")
any(is.na(clean_data)) # check for missing values
length(unique(clean_data$id)) == nrow(clean_data) # check if id is unique
# check shooting occurrences by year
table(clean_data$year)
# check shooting occurrences by geographic division
table(clean_data$division)
# get the numerical summarial by year
clean %>% group_by(year) %>% 
  summarize(n=n(), min=min(count), Q1=quantile(count,probs=0.25), median=quantile(count,probs=0.5), Q3=quantile(count,probs=0.75), max=max(count), mean=mean(count), sd=sd(count))
# get the numerical summarial by division
clean %>% group_by(division) %>% 
  summarize(n=n(), min=min(count), Q1=quantile(count,probs=0.25), median=quantile(count,probs=0.5), Q3=quantile(count,probs=0.75), max=max(count), mean=mean(count), sd=sd(count))
