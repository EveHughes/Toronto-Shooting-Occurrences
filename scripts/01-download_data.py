#### Preamble ####
# Purpose: Downloads and saves the data (titled "Shooting Occurrences") from OpenDataToronto.
# Author: Xingjie Yao
# Date: 27 September 2024
# Contact: xingjie.yao@mail.utoronto.ca
# License: MIT
# Pre-requisites: The dataset of interest includes all shooting occurrences from 2014 to 2019 by occurred date aggregated by Division.  
# Any other information needed? Shootings in this data set include both firearm discharges and shooting events. 


import requests
import pandas as pd
from io import StringIO

# Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# https://docs.ckan.org/en/latest/api/

# To hit our API, you'll be making requests to:
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# Datasets are called "packages". Each package can contain many "resources"
# To retrieve the metadata for this package and its resources, use the package name in this page's URL:
url = base_url + "/api/3/action/package_show"
params = { "id": "police-annual-statistical-report-shooting-occurrences"}
package = requests.get(url, params = params).json()

# To get resource data:
for idx, resource in enumerate(package["result"]["resources"]):

       # for datastore_active resources:
       if resource["datastore_active"]:

           # To get all records in CSV format:
           url = base_url + "/datastore/dump/" + resource["id"]
           resource_dump_data = requests.get(url)
           data = pd.read_csv(StringIO(resource_dump_data.text))
           data.to_csv("data/raw_data/shooting_occurrence.csv", index = False) 
