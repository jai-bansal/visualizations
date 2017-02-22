# This script creates a bar graph using (a subset of) 'census_data.csv' using the 'rCharts' library.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (Delaware, Maryland, New Jersey, Pennsylvania, Virginia, 
# and West Virginia) in 2010.

# LOAD LIBRARIES ----------------------------------------------------------
# This section loads the necessary libraries for this script.
library(readr)
library(data.table)
library(dplyr)
library(rCharts)

# IMPORT DATA -------------------------------------------------------------
# This section imports the data for this script.
# Note that the data is in the 'visualizations' folder, NOT the 'rCharts' folder.
census_data = data.table(read_csv('census_data.csv'))

# SUBSET/PROCESS DATA -----------------------------------------------------
# This section prepares the data prior to plotting.

  # Specify states of interest.
  states = c('Delaware', 'Maryland', 'New Jersey', 'Pennsylvania', 
             'Virginia', 'West Virginia')
  
  # Create data subset (specified above).
  census_subset = census_data[Name %in% states, .(Name, `2010`)]
  
  # Divide population values by 1000 for easier graph viewing.
  census_subset$`2010` = census_subset$`2010` / 1000
  
  # Rename columns for plot.
  census_subset = rename(census_subset, 
                         State = Name, 
                         `2010_pop` = `2010`)

#####  
# Plot data.
rPlot(`2010` ~ Name, 
                     data = census_subset, 
                     type = 'bar', 
                     color = 'Name')
  
  
  ggplot(data = census_subset, 
       aes(x = Name, 
           y = `2010`, 
           fill = Name)) + 
  geom_bar(stat = 'identity') + 
  theme(legend.position = 'none') + 
  scale_y_continuous(breaks = seq(0, 12500, 2500)) +
  geom_text(aes(label = round(`2010`, 1)), 
            vjust = 1.5, 
            size = 6) +
  theme(axis.text.x = element_text(color = 'black', 
                                   size = 16), 
        axis.text.y = element_text(color= 'black', 
                                   size = 16),
        axis.title.x = element_text(face = 'bold', 
                                    size = 17, 
                                    vjust = -0.5),
        axis.title.y = element_text(face = 'bold',
                                    size = 17),
        plot.title = element_text(face = 'bold', 
                                  size = 18, 
                                  vjust = 2)) +
  ggtitle('Selected State Populations in 2010 (in thousands)') + 
  xlab('State') + 
  ylab('2010 Population (in thousands)')