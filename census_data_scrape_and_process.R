# This script creates the data file used for all visualizations.
# Specifically, it scrapes the data from the web and processes it.

# The data consists of the population of each US state for 1960, 1970, 1980, 1990, 2000, and 2010.
# This data comes from the United States Census and can be viewed at the url below:
# https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population

# Added to this is the area of each state in square miles.
# This data comes from Wikipedia and can be viewed at the url below.
# https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_area

# Load packages.
library(rvest)
library(data.table)

#####
# SCRAPE DATA.

  # Specify webpages.
  population_page = html('https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population')
  area_page = html('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_area')
  
  # Get xpaths.
  population_xpath = html_nodes(population_page, 
                                xpath = '//*[@id="mw-content-text"]/table[3]')
  area_xpath = html_nodes(area_page, 
                          xpath = '//*[@id="mw-content-text"]/table[1]')
  
  # Get data.
  # 'html_table' returns a list containing a data frame, so the data frame is extracted.
  census_data = html_table(population_xpath, 
                           fill = T)[[1]]
  area_data = html_table(area_xpath, 
                         fill = T)[[1]]
  census_data = data.table(census_data)
  area_data = data.table(area_data)
  
#####
# PROCESS DATA.
  
  # Process 'census_data'.
  
    # Columns are 'character' vectors and have commas.
    # These must be removed.
    census_data$`1960` = gsub(',', 
                              '', 
                              census_data$`1960`)
    census_data$`1970` = gsub(',', 
                              '', 
                              census_data$`1970`)
    census_data$`1980` = gsub(',', 
                              '', 
                              census_data$`1980`)
    census_data$`1990` = gsub(',', 
                              '', 
                              census_data$`1990`)
    census_data$`2000` = gsub(',', 
                              '', 
                              census_data$`2000`)
    census_data$`2010` = gsub(',', 
                              '', 
                              census_data$`2010`)
    
    # Convert columns to numeric.
    census_data$`1960` = as.numeric(census_data$`1960`)
    census_data$`1970` = as.numeric(census_data$`1970`)
    census_data$`1980` = as.numeric(census_data$`1980`)
    census_data$`1990` = as.numeric(census_data$`1990`)
    census_data$`2000` = as.numeric(census_data$`2000`)
    census_data$`2010` = as.numeric(census_data$`2010`)
    
    # Sort data by 'Name'.
    census_data = census_data[order(Name)]
    
  # Process 'area_data'.
  
      # Remove unneeded columns and rename columns.
      area_data = area_data[, .(V1, V3)]
      setnames(area_data, 
               names(area_data), 
               c('Name', 'Area (sq. miles)'))
      
      # Remove old header row
      area_data = area_data[Name != 'State/territory']
      
      # Columns are 'character' vectors and have commas.
      # These must be removed.
      area_data$`Area (sq. miles)` = gsub(',', 
                                          '', 
                                          area_data$`Area (sq. miles)`)
      
      # Convert columns to numeric.
      area_data$`Area (sq. miles)` = as.numeric(area_data$`Area (sq. miles)`)
  
  # Add 'area_data' to 'census_data'.    
  # The result is still called 'census_data' and so is technically is misnomer.
  census_data = merge(census_data, 
                      area_data, 
                      by = 'Name', 
                      all.x = T)

# Write data to '.csv' file.
write.csv(census_data, 
          'census_data.csv', 
          row.names = F)