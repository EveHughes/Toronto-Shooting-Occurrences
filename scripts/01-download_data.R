#### Preamble ####
# Purpose: Downloads and saves the data (titled "Shooting Occurrences") from OpenDataToronto.
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

#### Download data ####
package <- show_package("f29feb49-ceb1-44bf-a2b6-5fc6a0e6147a") # get package
# get all resources for this package
resources <- list_package_resources("f29feb49-ceb1-44bf-a2b6-5fc6a0e6147a")
# identify datastore resources
datastore_resources <- filter(resources, tolower(format) %in% c('csv', 'geojson'))
# load the first datastore resource which is in 'csv'
data <- filter(datastore_resources, row_number()==1) %>% get_resource()
glimpse(data)

#### Save data ####
write_csv(data, "inputs/data/raw_data/shooting_occurrence.csv") 
