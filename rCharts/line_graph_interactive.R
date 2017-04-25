# This script creates a line graph using (a subset of) 'census_data.csv' using the 'rCharts' library.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for Pennsylvania and Illinois.


# LOAD LIBRARIES ----------------------------------------------------------
# This section loads the necessary libraries for this script.
library(data.table)
library(rCharts)


# IMPORT DATA -------------------------------------------------------------
# This section imports the data for this script.
# Note that the data is in the 'visualizations' folder, NOT the 'rCharts' folder.
census_data = data.table(read.csv('census_data.csv', 
                                  header = T, 
                                  stringsAsFactors = F, 
                                  check.names = F))

# SUBSET/PROCESS DATA -----------------------------------------------------
# This section prepares the data prior to plotting.

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
    

# PLOT DATA ---------------------------------------------------------------
# This section plots the data.
    
  # Create plot.
  line_graph = nPlot(Population ~ Year, 
                     data = census_subset_transpose, 
                     type = 'lineChart', 
                     group = 'State')
    
  # Label axes.
  line_graph$xAxis(axisLabel = 'Year')
  
  # View plot.
  line_graph


    