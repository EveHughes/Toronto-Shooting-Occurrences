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
library(opendatatoronto)
library(tidyverse)
library(dplyr)

#### Simulate data ####
set.seed(123456)
n <- 96 # the sample size
id <- 1:n # unique random identifiers
Index_ <- 1:n # unique random identifiers
# generate random years between 2014 and 2019
OccurredYear <- sample(2014:2019, n, replace = TRUE)
# generate random geographic division
GeoDivision <- sample(c("D11", "D12", "D13", "D14", "D22", "D23", "D31", "D32", "D33", "D41", "D42", "D43", "D51", "D52", "D53", "D54/D55"), n, replace = TRUE)
# all categories are "Shooting Occurrence"
Category <- sample(c("Shooting Occurrence"), n, replace = TRUE)
# generate random discrete annual shooting numbers between 0 and 70
Count_ <- sample(0:70, n, replace = TRUE)
shooting_data <- data.frame(`_id` = id, Index_ = Index_, OccurredYear = OccurredYear, GeoDivision = GeoDivision, Category = Category, Count_ = Count_)
glimpse(shooting_data)

#### Develop some tests ####
any(is.na(shooting_data)) # check for missing values
length(unique(shooting_data$X_id)) == nrow(shooting_data) # check if _id is unique
length(unique(shooting_data$Index_)) == nrow(shooting_data) # check if Index_ is unique
# check shooting occurrences by year
table(shooting_data$OccurredYear)
# check shooting occurrences by geographic division
table(shooting_data$GeoDivision)
