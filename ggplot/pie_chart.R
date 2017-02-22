# This script creates a pie chart using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (North Carolina, Maryland, New Jersey, Pennsylvania, Virginia, 
# and New York) in 2010.

# Load packages.
library(data.table)
library(ggplot2)
library(ggthemes)

# Load data.
# Note that the data is located in the 'visualizations' folder, NOT the 'ggplot' folder.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Specify states of interest.
  states = c('North Carolina', 'Maryland', 'New Jersey', 'Pennsylvania', 
             'Virginia', 'New York')
  
  # Create data subset (specified above).
  census_subset = census_data[Name %in% states, .(Name, `2010`)]
  
  # Divide population values by 1000000 for easier graph viewing.
  census_subset$`2010` = census_subset$`2010` / 1000000
  
  # Compute percentage of total population accounted for by each state.
  
    # Compute percentage.
    census_subset$percent = round(100 * (census_subset$`2010` / sum(census_subset$`2010`)), 2)
  
    # Change to 'character' vector with form 'percent + %'.
    census_subset$percent = as.character(census_subset$percent)
    census_subset$percent = paste0(census_subset$percent, '%')
    
    # Change 'census_subset$Name' from state name to state abbreviation so labels fit on pie chart.
    census_subset$Name = ifelse(census_subset$Name == 'North Carolina', 'North\nCarolina', 
                                ifelse(census_subset$Name == 'Maryland', 'Maryland', 
                                       ifelse(census_subset$Name == 'New Jersey', 'New\nJers.', 
                                              ifelse(census_subset$Name == 'Pennsylvania', 'Penn.', 
                                                     ifelse(census_subset$Name == 'Virginia', 'Virginia', 'New\nYork')))))
  
  # Specify locations for pie chart labels.
  
    # Count cumulative population.
    # This has no statistical or data significance, it's only to help with chart labels.
    census_subset$sum = cumsum(census_subset$`2010`)
    
    # Create 'offset_sum' column that will help with chart labels.
    census_subset$offset_sum = c(0, census_subset$sum[1:(nrow(census_subset) - 1)])
    
    # Create 'label_locations' column that specifies label locations on pie chart.
    census_subset$label_locations = (census_subset$sum + census_subset$offset_sum) / 2

#####  
# Plot data.
ggplot(data = census_subset, 
       aes(x = '', 
           y = `2010`, 
           fill = as.character(round(`2010`, 2)))) + 
geom_bar(stat = 'identity', 
         color = 'black') +
geom_text(aes(y = label_locations, 
              label = census_subset$percent), 
          size = 6) +
coord_polar('y', 
            start = 5.55) +
guides(fill = guide_legend(title = 'Population\n(millions)')) +
theme_few() +
theme(axis.ticks = element_blank(), 
      axis.text.x = element_text(color = 'black', 
                                 size = 17, 
                                 vjust = 10), 
      plot.title = element_text(face = 'bold', 
                                size = 18, 
                                vjust = 2),
      panel.background = element_rect(fill = 'lightgrey', 
                                      colour = 'lightgrey'), 
      legend.text = element_text(size = 17), 
      legend.title = element_text(size = 17)) +
scale_y_continuous(breaks = census_subset$label_locations, 
                   labels = census_subset$Name) +
scale_fill_brewer(palette = 'Set1') +
ggtitle('Selected State 2010 Population (millions) and Percentage') +
xlab('') +
ylab('')