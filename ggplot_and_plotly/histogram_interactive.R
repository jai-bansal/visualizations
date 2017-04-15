# This script creates a histogram using (a subset of) 'census_data.csv' using the 'ggplot2' and 'plotly' libraries

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for 2010.

# Load packages.
library(data.table)
library(ggplot2)
library(grid)
library(plotly)

# Load data.
# Note that the data is located in the 'visualizations' folder, NOT the 'ggplot' folder.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

#####
# SUBSET/PROCESS DATA.
  
  # Create data subset consisting of all 2010 observations.
  census_subset = census_data[, .(Name, `2010`)]
  
  # Remove row containing total population of United States.
  census_subset = census_subset[Name != 'United States']
  
  # Divide population values by 1000000 for easier graph viewing.
  census_subset$`2010` = census_subset$`2010` / 1000000
  
#####
# Plot data.
ggplotly(ggplot(data = census_subset, 
       aes(x = `2010`)) +
  geom_histogram(binwidth = 1.5, 
                 fill = I('darkgreen'), 
                 col = I('black')) +
  theme_bw() +
  scale_y_continuous(breaks = seq(0, 14, by = 1)) + 
  scale_x_discrete(breaks = seq(0, 40, by = 5)) +
  theme(axis.text.x = element_text(color = 'black', 
                                   size = 17), 
        axis.text.y = element_text(color = 'black', 
                                   size = 17),
        axis.title.x = element_text(face = 'bold', 
                                    size = 18, 
                                    vjust = -0.5),
        axis.title.y = element_text(face = 'bold',
                                    size = 18),
        plot.title = element_text(face = 'bold', 
                                  size = 19, 
                                  vjust = 2), 
        panel.grid.minor = element_blank()) +
  ggtitle('Histogram of 2010 US State Populations (in millions)') +
  xlab('2010 Populations (in millions)') +
  ylab('Number of States'))