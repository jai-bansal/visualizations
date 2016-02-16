# This script creates a histogram using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for 2010.

# Load packages.
library(data.table)
library(ggplot2)
library(grid)

# Load data.
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
  
  # Divide population values by 1000 for easier graph viewing.
  census_subset$`2010` = census_subset$`2010` / 1000
  
#####
# Plot data.
ggplot(data = census_subset, 
       aes(x = `2010`)) +
  geom_histogram(binwidth = 1500, 
                 fill = I('darkgreen'), 
                 col = I('black')) +
  theme_bw() +
  scale_y_continuous(breaks = seq(0, 14, by = 1)) + 
  scale_x_discrete(breaks = seq(0, 40000, by = 5000)) +
  theme(axis.text.x = element_text(color = 'black', 
                                   size = 15), 
        axis.text.y = element_text(color = 'black', 
                                   size = 15),
        axis.title.x = element_text(face = 'bold', 
                                    size = 16, 
                                    vjust = -0.5),
        axis.title.y = element_text(face = 'bold',
                                    size = 16),
        plot.title = element_text(face = 'bold', 
                                  size = 17, 
                                  vjust = 2), 
        panel.grid.minor = element_blank()) +
  geom_segment(aes(x = 26000, 
                   y = 2, 
                   xend = 25000, 
                   yend = 1.1), 
               arrow = arrow(length = unit(0.5, 'cm')), 
               size = 1) +
  geom_segment(aes(x = 35000, 
                   y = 2, 
                   xend = 36000, 
                   yend = 1.1), 
               arrow = arrow(length = unit(0.5, 'cm')), 
               size = 1) +
  annotate('text', 
           x = 26000, 
           y = 2.8,
           label = census_subset[`2010` > 20000 & `2010` < 30000]$Name,
           size = 6) +
  annotate('text', 
           x = 26000, 
           y = 2.3, 
           label = paste0('(', 
                          round(census_subset[Name == 'Texas']$`2010`, 2), 
                          ')'), 
           size = 6) +
  annotate('text', 
           x = 35000, 
           y = 2.8, 
           label = census_subset[`2010` > 30000]$Name, 
           size = 6) +
  annotate('text', 
           x = 35000, 
           y = 2.3, 
           label = paste0('(', 
                          round(census_subset[Name == 'California']$`2010`, 2), 
                          ')'), 
           size = 6) +
  ggtitle('Histogram of 2010 US State Populations (in thousands)') +
  xlab('2010 Populations (in thousands)') +
  ylab('Number of States')