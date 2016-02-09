# This script creates the data file used for all visualizations.
# Specifically, it scrapes the data from the web and processes it.

# The data consists of the population of each US state for 1960, 1970, 1980, 1990, 2000, and 2010.
# This data comes from the United States Census and can be viewed at the url below.
# https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population

# Added to this is the area of each state in square miles.
# This data comes from Wikipedia and can be viewed at the url below.
# https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_area

# IMPORT MODULES.
import pandas as pd

# SCRAPE DATA.
# 'pandas read_html' will search for all tables on the provided url as long as they match the 'match' parameter.
# For 'census_data', I've provided a 'match' parameter of '2010' as the table I want turns out to be the only table with this value.
# For 'area_data', I've provided a 'match' parameter of 'Alaska' as the table I want turns out to be the only table with this value.
# I personally think this is a silly way of scraping and that I should be able to pass in the xpath. Anyway, this works.
census_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population', match = '2010')
area_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_area', match = 'Alaska')

# CLEAN/PROCESS DATA.

# Convert data to 'DataFrame'.
# 'pandas read_html' returns a list, so I extract the first element.
census_data = census_data[0]
area_data = area_data[0]

# Remove unneeded columns of 'area_data'.
area_data = area_data[[0, 2]]

# Rename columns (header row was not recognized).
census_data.columns = ['Name', '1960', '1970', '1980', '1990', '2000', '2010']
area_data.columns = ['Name', 'Area (sq. miles)']

# Drop duplicate header rows.
census_data = census_data[census_data['Name'] != 'Name']
area_data = area_data[area_data['Name'].isnull() == False]
area_data = area_data[area_data['Name'] != 'State/territory']

# Join 'census_data' and 'area_data'.
# The result is still called 'census_data' and so is technically is misnomer.
census_data = census_data.merge(area_data, how = 'left', on = 'Name')

# Sort 'census_data' by 'Name'.
census_data.sort_values( by = 'Name', inplace = True)

# CREATE CSV FILE.
census_data.to_csv('census_data.csv', index = False)
