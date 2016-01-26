# This script creates the data file used for all visualizations.
# Specifically, it scrapes the data from the web and processes it.

# The data consists of the population of each US state for 1960, 1970, 1980, 1990, 2000, and 2010.
# This data comes from the United States Census and can be viewed at the url below:
# https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population

# Load packages.
library(rvest)
library(data.table)

#####
# SCRAPE DATA.

  # Specify webpage.
  page = html('https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population')
  
  # Get xpath.
  xpath = html_nodes(page, xpath = '//*[@id="mw-content-text"]/table[3]')
  
  # Get data.
  # 'html_table' returns a list containing a data frame, so the data frame is extracted.
  census_data = html_table(xpath, fill = T)[[1]]
  census_data = data.table(census_data)
  
#####
# PROCESS DATA.
  
  # Columns are 'character' vectors and have commas.
  # These must be removed.
  census_data$`1960` = gsub(',', '', census_data$`1960`)
  census_data$`1970` = gsub(',', '', census_data$`1970`)
  census_data$`1980` = gsub(',', '', census_data$`1980`)
  census_data$`1990` = gsub(',', '', census_data$`1990`)
  census_data$`2000` = gsub(',', '', census_data$`2000`)
  census_data$`2010` = gsub(',', '', census_data$`2010`)
  
  # Convert columns to numeric.
  census_data$`1960` = as.numeric(census_data$`1960`)
  census_data$`1970` = as.numeric(census_data$`1970`)
  census_data$`1980` = as.numeric(census_data$`1980`)
  census_data$`1990` = as.numeric(census_data$`1990`)
  census_data$`2000` = as.numeric(census_data$`2000`)
  census_data$`2010` = as.numeric(census_data$`2010`)
  
  # Sort data by 'Name'.
  census_data = census_data[order(Name)]
  
# Write data to '.csv' file.
write.csv(census_data, 'census_data.csv', row.names = F)
