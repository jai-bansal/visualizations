# This script creates a line graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for Pennsylvania and Illinois.

# Load packages.
library(data.table)
library(reshape2)
library(ggplot2)
library(ggthemes)

# Load data.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Remove unneeded column.
  census_data$`Area (sq. miles)` = NULL

  # Subset data.
  census_subset = census_data[Name == 'Pennsylvania' | Name == 'Illinois']
  
  # Divide population values by 1000000 for easier graph viewing.
  census_subset$`1960` = census_subset$`1960` / 1000000
  census_subset$`1970` = census_subset$`1970` / 1000000
  census_subset$`1980` = census_subset$`1980` / 1000000
  census_subset$`1990` = census_subset$`1990` / 1000000
  census_subset$`2000` = census_subset$`2000` / 1000000
  census_subset$`2010` = census_subset$`2010` / 1000000
  
  # Reshape data for line graph.
    
    # Transpose 'census_subset'.
    census_subset_transpose = data.table(t(census_subset), 
                                         keep.rownames = T)
    
    # Set column names for 'census_subset_transpose'.
    setnames(census_subset_transpose, 
             names(census_subset_transpose), 
             c('Year', 'Illinois', 'Pennsylvania'))
    
    # Remove old, transposed header row.
    census_subset_transpose = census_subset_transpose[Year != 'Name']
    
    # Melt data into convenient form for line graph.
    census_subset_transpose = melt(census_subset_transpose, 
                                   id = 'Year')
    
    # Change column names for melted 'census_subset_transpose'.
    setnames(census_subset_transpose, 
             names(census_subset_transpose), 
             c('Year', 'State', 'Population'))
    
    # Change 'census_subset_transpose$Population' to 'numeric'.
    census_subset_transpose$Population = as.numeric(census_subset_transpose$Population)

#####  
# Plot data.
ggplot(data = census_subset_transpose, 
       aes(x = Year, 
           y = Population, 
           group = State, 
           color = State)) + 
  geom_line() + 
  geom_point() + 
  ylim(c(10, 13.05)) + 
  theme_economist() +
  theme(axis.text.x = element_text(color = 'black', 
                                   size = 16), 
        axis.text.y = element_text(color = 'black', 
                                   size = 16), 
        axis.title.x = element_text(face = 'bold', 
                                    size = 16),
        axis.title.y = element_text(face = 'bold',
                                    size = 16, 
                                    vjust = 1),
        axis.ticks = element_blank(),
        plot.title = element_text(face = 'bold', 
                                  size = 17, 
                                  hjust = 0.35), 
        legend.title = element_text(size = 17),
        legend.text = element_text(size = 16)) +
  annotate('text', 
           x = 0.91, 
           y = 10.3, 
           label = round(census_subset_transpose[State == 'Illinois' & Year == '1960']$Population, 2), 
           size = 5.5) +
  annotate('text',
           x = 1, 
           y = 11.55, 
           label = round(census_subset_transpose[State == 'Pennsylvania' & Year == '1960']$Population, 2), 
           size = 5.5) + 
  annotate('text', 
           x = 6, 
           y = 12.55, 
           label = round(census_subset_transpose[State == 'Pennsylvania' & Year == '2010']$Population, 2), 
           size = 5.5) +
  annotate('text', 
           x = 6, 
           y = 13.02, 
           label = round(census_subset_transpose[State == 'Illinois' & Year == '2010']$Population, 2), 
           size = 5.5) +
  ggtitle('Population (in milions) Over Time for Selected States') +
  xlab('Year') +
  ylab('Population (in millions)')