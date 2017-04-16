# This script creates a correlation plot using (a subset of) 'census_data.csv' with the 'ggplot' and 'plotly'.
# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.

# LOAD LIBRARIES ----------------------------------------------------------
# This section loads relevant libraries.
library(readr)
library(data.table)
library(dplyr)
library(ggplot2)
library(plotly)

# IMPORT DATA -------------------------------------------------------------
# This section imports the data to be used in the correlation plot.
# Note that the data is located in the 'visualizations' folder, NOT the 'ggplot' folder.
census_data = data.table(read_csv('census_data.csv'))

# CLEAN DATA --------------------------------------------------------------
# This section cleans the data so the correlation plot shows up properly.

  # Remove 'Name' from 'census_data'.
  # All correlation plot data must be numeric.
  census_data = select(census_data, 
                       -c(Name))

  # Remove null values from 'Area (sq. miles)'.
  correlation_plot_data = census_data[is.na(`Area (sq. miles)`) == F]

# ADD FEATURE -------------------------------------------------------------
# This section adds features to 'correlation_plot_data' that are negatively correlated with each other.
# This results in the correlation plot showing an example of how negative correlations look.
  
  # Add population growth in percentage terms between 1960 and 1970.
  correlation_plot_data$`60_70_growth` = (correlation_plot_data$`1970` - correlation_plot_data$`1960`) / correlation_plot_data$`1960`

  # Add population growth in percentage terms between 1970 and 1980.
  correlation_plot_data$`70_80_growth` = (correlation_plot_data$`1980` - correlation_plot_data$`1970`) / correlation_plot_data$`1970`
  
# CREATE CORRELATION PLOT -------------------------------------------------
# This section creates a correlation plot (using only numeric columns).
  
  # Get correlations between variables.
  correlations = cor(correlation_plot_data)
  
  # Get 'correlations' into a form to be plotted.
  melted_correlations = melt(correlations)
  
  # Plot correlation plot.
  ggplotly(ggplot(data = melted_correlations, 
         aes(x = Var1, 
             y = Var2, 
             fill = value)) + 
    geom_raster() + 
    scale_fill_gradient(low = 'red', 
                        high = 'blue') +
    labs(fill = 'Correlation', 
         x = '', 
         y = '', 
         title = 'Correlation Plot for State Population Variables'))
