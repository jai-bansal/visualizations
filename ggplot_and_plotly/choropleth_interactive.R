# This script creates a choropleth map using (a subset of) 'census_data.csv' using the 'plotly' library.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for the year 2010.

# Load packages.
library(data.table)
library(dplyr)
library(plotly)

# Load data.
# Note that the data is located in the 'visualizations' folder, NOT the 'ggplot' folder.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Get abbreviations for states.
  # This is needed for the 'plotly' mapping process.
  state_names = data.table(state = state.name, 
                           initials = state.abb)

  # Add state initials to 'census_data'.
  census_data = merge(census_data, 
                      state_names, 
                      by.x = 'Name', 
                      by.y = 'state', 
                      all.x = T)

  # Restrict 'census_subset' to '2010' observations only.
  census_subset = census_data[, .(Name, initials, `2010`)]

  # Remove aggregate 'United States' population row.
  census_subset = census_subset[Name != 'United States']
  
  # Divide '2010' by 1000 for easier map viewing.
  census_subset$`2010` = round(census_subset$`2010` / 1000000, 2)
  
  # Get US state data.
  states_map = map_data('state')
  
#####  
# Plot data.
  
  # Specify map settings.
  map = list(scope = 'usa', 
             project = list(type = 'albers usa'))
  
  # Create plot.
  # Note: this doesn't always render in the RStudio plot space.
  # You may need to hit the 'Show in new window' to view the plot.
  plot_geo(data = census_subset, 
           locationmode = 'USA-states') %>%
    add_trace(z = ~`2010`, 
              color = ~`2010`, 
              colors = 'Blues', 
              locations = ~initials) %>% 
    colorbar(title = 'Population (millions)') %>%
    layout(title = '2010 US Population (in millions) by State', 
           geo = map)