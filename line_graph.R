# This script creates a line graph using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for Pennsylvania and Illinois.

# Load packages.
library(data.table)
library(reshape2)
library(ggplot2)

# Load data.
census_data = data.table(read.csv('census_data.csv', header = T, stringsAsFactors = F, check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Subset data.
  census_subset = census_data[Name == 'Pennsylvania' | Name == 'Illinois']
  
  # Divide population values by 1000 for easier graph viewing.
  census_subset$`1960` = census_subset$`1960` / 1000
  census_subset$`1970` = census_subset$`1970` / 1000
  census_subset$`1980` = census_subset$`1980` / 1000
  census_subset$`1990` = census_subset$`1990` / 1000
  census_subset$`2000` = census_subset$`2000` / 1000
  census_subset$`2010` = census_subset$`2010` / 1000
  
  # Reshape data for line graph.
    
    # Transpose 'census_subset'.
    census_subset_transpose = data.table(t(census_subset), keep.rownames = T)
    
    # Set column names for 'census_subset_transpose'.
    setnames(census_subset_transpose, names(census_subset_transpose), c('Year', 'Illinois', 'Pennsylvania'))
    
    # Remove old, transposed header row.
    census_subset_transpose = census_subset_transpose[Year != 'Name']
    
    # Melt data into convenient form for line graph.
    census_subset_transpose = melt(census_subset_transpose, id = 'Year')
    
    # Change column names for melted 'census_subset_transpose'.
    setnames(census_subset_transpose, names(census_subset_transpose), c('Year', 'State', 'Population'))
    
    # Change 'census_subset_transpose$Population' to 'numeric'.
    census_subset_transpose$Population = as.numeric(census_subset_transpose$Population)

#####  
# Plot data.
ggplot(data = census_subset_transpose, aes(x = Year, y = Population, group = State, color = State)) + 
  geom_line() + 
  geom_point() + 
  ylim(c(10000, 13000)) + 
  theme_economist() +
  theme(axis.text.x = element_text(color = 'black'), 
        axis.text.y = element_text(color = 'black'), 
        axis.title.x = element_text(face = 'bold', 
                                    size = 12),
        axis.title.y = element_text(face = 'bold',
                                    size = 12),
        plot.title = element_text(face = 'bold', 
                                  size = 14, 
                                  hjust = 0.35)) +
  annotate('text', 
           x = 1, 
           y = 10000, 
           label = census_subset_transpose[State == 'Illinois' & Year == '1960']$Population, 
           size = 4) +
  annotate('text',
           x = 1, 
           y = 11250, 
           label = census_subset_transpose[State == 'Pennsylvania' & Year == '1960']$Population, 
           size = 4) + 
  annotate('text', 
           x = 6.2, 
           y = 12600, 
           label = census_subset_transpose[State == 'Pennsylvania' & Year == '2010']$Population, 
           size = 4) +
  annotate('text', 
           x = 6, 
           y = 12950, 
           label = census_subset_transpose[State == 'Illinois' & Year == '2010']$Population, 
           size = 4) +
  ggtitle('Population (in thousands) Over Time for Selected States') +
  xlab('Year') +
  ylab('Population (in thousands)')