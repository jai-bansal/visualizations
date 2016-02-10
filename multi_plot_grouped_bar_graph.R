# This script creates a figure consisting of two subplots using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv'.

# The first subplot will be a grouped bar graph that uses all observations for 3 states: Vermont, Delaware, and Ohio
# It will show the percentage growth between decades for each state.
# The second subplot will be a bar graph that uses the aggregate United States observations
# and shows the percentage growth between decades for the entire United States.

# Population percentage growth in a decade 't' will be computed as:
# 100 * (population(t + 1) - population(t)) / population(t)

# For example, the population growth between 1960 and 1970 is:
# 100 * (population(1970) - population(1960)) / population(1960)

# Load packages.
library(data.table)
library(ggplot2)
library(reshape2)
library(grid)

# Load data.
census_data = data.table(read.csv('census_data.csv', header = T, stringsAsFactors = F, check.names = F))

#####
# SUBSET/PROCESS DATA.

  # Specify rows of interest (states specified above and aggregate 'United States').
  interest = c('Vermont', 'Delaware', 'Ohio', 'United States')

  # Subset data.
  census_subset = census_data[Name %in% interest]
  
  # Compute percentage growth during 1960s decade (between 1960 and 1970):
  census_subset$`1960s_growth` = 100 * (census_subset$`1970` - census_subset$`1960`) / census_subset$`1960`
  
  # Compute percentage growth during 1970s decade (between 1970 and 1980):
  census_subset$`1970s_growth` = 100 * (census_subset$`1980` - census_subset$`1970`) / census_subset$`1970`

  # Compute percentage growth during 1980s decade (between 1980 and 1990):
  census_subset$`1980s_growth` = 100 * (census_subset$`1990` - census_subset$`1980`) / census_subset$`1980`

  # Compute percentage growth during 1990s decade (between 1990 and 2000):
  census_subset$`1990s_growth` = 100 * (census_subset$`2000` - census_subset$`1990`) / census_subset$`1990`

  # Compute percentage growth during 2000s decade (between 2000 and 2010):
  census_subset$`2000s_growth` = 100 * (census_subset$`2010` - census_subset$`2000`) / census_subset$`2000`
  
  # Remove unneeded columns (all actual population measurements):
  census_subset = census_subset[, .(Name, `1960s_growth`, `1970s_growth`, `1980s_growth`, `1990s_growth`, `2000s_growth`)]
  
  # Melt data to allow plotting.
  census_subset = melt(census_subset, id = 'Name')

#####
# PLOT DATA.
  
  # Create state data plot.
  plot_1 = ggplot(data = census_subset[Name != 'United States'], aes(x = variable, y = value)) +
            geom_bar(aes(fill = Name), 
                     position = 'dodge', 
                     stat = 'identity', 
                     width = 0.9) +
            scale_y_continuous(breaks = seq(0, 25, by = 5), limits = c(0, 25)) +
            theme(axis.text.x =  element_text(color = 'black', 
                                      size = 14), 
                  axis.text.y = element_text(color = 'black', 
                                     size = 14), 
                  axis.title.x = element_text(face = 'bold', 
                                    size = 14), 
                  axis.title.y = element_text(face = 'bold', 
                                    size = 14), 
                  plot.title = element_text(face = 'bold',
                                  size = 16), 
                  legend.title = element_text(size = 16), 
                  legend.text = element_text(size = 15)) +
                  guides(fill = guide_legend(title = 'State')) +
                  scale_x_discrete(labels = c('1960s', '1970s', '1980s', '1990s', '2000s')) +
            ggtitle('Percentage Growth By Decade For Selected States') +
            xlab('Decade') +
            ylab('Percentage Growth')

  # Create aggregate United States plot.
  plot_2 = ggplot(data = census_subset[Name == 'United States'], aes(x = variable, y = value)) +
            geom_bar(aes(fill = Name), 
                     position = 'dodge', 
                     stat = 'identity',  
                     width = 0.3) +
            scale_y_continuous(breaks = seq(0, 25, by = 5), limits = c(0, 25)) +
            scale_fill_manual(values = 'orange') +
            theme(axis.text.x =  element_text(color = 'black', 
                                      size = 14), 
                  axis.text.y = element_text(color = 'black', 
                                     size = 14), 
                  axis.title.x = element_text(face = 'bold', 
                                    size = 14), 
                  axis.title.y = element_text(face = 'bold', 
                                    size = 14), 
                  plot.title = element_text(face = 'bold',
                                  size = 16), 
                  legend.title = element_text(size = 16), 
                  legend.text = element_text(size = 15)) +
                  scale_x_discrete(labels = c('1960s', '1970s', '1980s', '1990s', '2000s')) +
                  guides(fill = guide_legend(title = 'Country')) +
            ggtitle('Percentage Growth by Decade for United States') +
            xlab('Decade') +
            ylab('Percentage Growth')
  
  # Plot both subplots.
  grid.newpage()
  grid.draw(rbind(ggplotGrob(plot_1), ggplotGrob(plot_2), size = 'last'))