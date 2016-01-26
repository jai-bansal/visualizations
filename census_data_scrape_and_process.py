# This script creates the data file used for all visualizations.
# Specifically, it scrapes the data from the web and processes it.

# The data consists of the population of each US state for 1960, 1970, 1980, 1990, 2000, and 2010.
# This data comes from the United States Census and can be viewed at the url below.
# https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population

# Import modules.
import pandas as pd

# Scrape data.
# 'pandas read_html' will search for all tables on the provided url as long as they match the 'match' parameter.
# I've provided a 'match' parameter of '2010' as the table I want turns out to be the only table with this value.
# I personally think this is a silly way of scraping and that I should be able to pass in the xpath. Anyway, this works.
census_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population', match = '2010')

# CLEAN/PROCESS DATA:

# Convert census_data to 'DataFrame'.
# 'pandas read_html' returns a list, so I extract the first element.
census_data = census_data[0]
