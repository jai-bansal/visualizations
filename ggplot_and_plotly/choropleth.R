# This script creates a choropleth map using (a subset of) 'census_data.csv' using the 'ggplot2' library.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

# Load packages.
library(data.table)
library(ggplot2)
library(maps)

# Load data.
# Note that the data is located in the 'visualizations' folder, NOT the 'ggplot' folder.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Restrict 'census_subset' to '2010' observations only.
  census_subset = census_data[, .(Name, `2010`)]

  # Remove aggregate 'United States' population row.
  census_subset = census_subset[Name != 'United States']
  
  # Make 'Name' lower case.
  # This is necessary for the choropleth to work.
  census_subset$Name = tolower(census_subset$Name)
  
  # Divide '2010' by 1000 for easier map viewing.
  census_subset$`2010` = census_subset$`2010` / 1000000
  
  # Get US state data.
  states_map = map_data('state')
  
#####  
# Plot data.
ggplotly(ggplot(data = census_subset, 
       aes(map_id = census_subset$Name)) + 
    geom_map(aes(fill = `2010`), 
             map = states_map) + 
    expand_limits(x = states_map$long, 
                  y = states_map$lat) +
    scale_fill_continuous(name = 'Population\n(millions)', 
                          low = 'lightblue', 
                          high = 'darkblue') + 
    borders(database = 'state', 
            colour = 'white') +
    theme_classic() +
    theme(panel.background = element_rect(fill = 'white', 
                                          colour = 'white'),
          line = element_blank(), 
          axis.ticks.x = element_blank(), 
          axis.ticks.y = element_blank(),
          axis.text.x = element_blank(), 
          axis.text.y = element_blank(), 
          plot.title = element_text(face = 'bold', 
                                    size = 18), 
          legend.title = element_text(size = 18), 
          legend.text = element_text(size = 17)) +
    ggtitle('2010 United States Population (millions) by State') +
    xlab('') +
    ylab(''))
