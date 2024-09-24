#### Preamble ####
# Purpose: Replicated graphs from the paper. 
# Author: Xingjie Yao
# Date: 27 September 2024
# Contact: xingjie.yao@mail.utoronto.ca
# License: MIT
# Pre-requisites: The dataset of interest includes all shooting occurrences from 2014 to 2019 by occurred date aggregated by Division.  
# Any other information needed? Shootings in this data set include both firearm discharges and shooting events. 


#### Workspace setup ####
library(dplyr)
library(ggplot2)
library(tidyverse)
library(opendatatoronto)

#### Load data ####
clean_data <- read_csv("inputs/data/analysis_data/cleaned_shooting_occurrence.csv")

#### Graphs ####
# Distribution of GeoDivision Shooting Occurrences by Year (2014-2019)
ggplot(clean_data) + 
  geom_boxplot(aes(x=as.factor(year), y=count)) + 
  labs(x = "Year", y = "Shooting Occurance") + 
  scale_x_discrete(breaks = c("2014", "2015", "2016", "2017", "2018", "2019"), labels = c("2014", "2015", "2016", "2017", "2018", "2019")) + 
  theme_minimal() 
# Shooting Occurrences by Year (2014-2019) Across Toronto GeoDivisions
ggplot(clean_data, aes(x = year, y = count, fill = factor(year))) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~ division) +  # subplot for each GeoDivision
  labs(x = "Year", y = "Shooting Occurrences", fill = "Year") +
  scale_x_continuous(breaks = seq(2014, 2019, by = 1)) + 
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 50, hjust = 1))
