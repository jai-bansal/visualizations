# This script creates a bar graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# observations for 6 states (Delaware, Maryland, New Jersey, Pennsylvania, Virginia, 
# and West Virginia) in 2010.

# Load packages.
library(data.table)
library(ggplot2)

# Load data.
census_data = data.table(read.csv('census_data.csv', header = T, stringsAsFactors = F, check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Specify states of interest.
  states = c('Delaware', 'Maryland', 'New Jersey', 'Pennsylvania', 
             'Virginia', 'West Virginia')
  
  # Create data subset (specified above).
  census_subset = census_data[Name %in% states, .(Name, `2010`)]
  
  # Divide population values by 1000 for easier graph viewing.
  census_subset$`2010` = census_subset$`2010` / 1000

#####  
# Plot data.
ggplot(data = census_subset, aes(x = Name, y = `2010`, fill = Name)) + 
  geom_bar(stat = 'identity') + 
  theme(legend.position = 'none') + 
  scale_y_continuous(breaks = seq(0, 12500, 2500)) +
  geom_text(aes(label = round(`2010`, 1)), 
            vjust = 2) +
  theme(axis.text.x = element_text(color = 'black', 
                                   size = 14), 
        axis.text.y = element_text(color= 'black', 
                                   size = 14),
        axis.title.x = element_text(face = 'bold', 
                                    size = 15),
        axis.title.y = element_text(face = 'bold',
                                    size = 15),
        plot.title = element_text(face = 'bold', 
                                  size = 16)) +
  ggtitle('Selected State Populations in 2010 (in thousands)') + 
  xlab('State') + 
  ylab('2010 Population (in thousands)')
