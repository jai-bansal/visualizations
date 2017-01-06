# This script plots ROC curves and and a lift chart using 'census_data.csv'.

# LOAD LIBRARIES ----------------------------------------------------------
# This section loads necessary libraries for this script.
library(readr)
library(data.table)
library(dplyr)
library(randomForest)
library(kknn)
library(pROC)
library(ROCR)

# IMPORT DATA -------------------------------------------------------------
# This section imports the data to be used in the script.
census_data = data.table(read_csv('census_data.csv'))

# CLEAN AND PROCESS DATA --------------------------------------------------------------
# This section cleans and processes 'census_data' so predictive models can be built smoothly.

  # Rename columns of 'census_data'.
  census_data = rename(census_data, 
                       sixty = `1960`, 
                       seventy = `1970`, 
                       eighty = `1980`, 
                       ninety = `1990`, 
                       hundred = `2000`, 
                       ten = `2010`)
  
  # Remove null values from 'census_data'.
  census_data = census_data[is.na(`Area (sq. miles)`) == F]
  
  # Create a variable so that classification models can be built.
  # To generate an ROC curve, I need a classification model.
  # For a classification model, I generate a binary variable.
  census_data$size = as.factor(ifelse(census_data$`Area (sq. miles)` > median(census_data$`Area (sq. miles)`), 1, 0))

# CREATE PREDICTIVE MODELS ----------------------------------------------
# This section creates random forest and k nearest neighbor models.
# Since I'm only interested in ROC curves, I do not split the data into training and test sets.
# I also do not scale the data before applying k nearest neighbor for the same reason.
  
  # Create random forest model.
  set.seed(666)
  rf = randomForest(size ~ sixty + seventy + eighty + ninety + hundred + ten, 
                    data = census_data, 
                    ntree = 1001)
  
  # Create k nearest neighbor model.
  set.seed(666)
  knn = kknn(formula = size ~ sixty + seventy + eighty + ninety + hundred + ten, 
             train = census_data, 
             test = census_data)
  
  # Generate predictions for random forest model.
  census_data$rf_pred = data.table(predict(rf, 
                                           newdata = census_data, 
                                           type = 'prob'))$`1`
  
  # Generate predictions for k nearest neighbor model.
  census_data$knn_pred = data.table(knn$prob)$`1`
  

# PLOT ROC CURVES ---------------------------------------------------------
# This section plots ROC curves for the predictive models above.
  
  # Add random forest model ROC curve.
  plot(roc(census_data$size, 
           census_data$rf_pred), 
       col = 'red', 
       print.auc = T, 
       print.auc.x = 0.9, 
       print.auc.y = 1.1)
  
  # Add k nearest neighbor ROC curve.
  plot(roc(census_data$size, 
           census_data$knn_pred), 
       col = 'blue', 
       print.auc = T, 
       print.auc.x = 0.9,
       print.auc.y = 0.85, 
       add = T)
  
  # Add legend to plot.
  legend('bottomright', 
         legend = c('RF', 'KNN'), 
         col = c('red', 'blue'), 
         lwd = 2)
  

# PLOT LIFT CHART ---------------------------------------------------------
# This section plots a lift chart for the predictive models above.
  
  # Add lift chart for random forest model.
  plot(performance(prediction(census_data$rf_pred, 
                              census_data$size), 
                   'lift', 'rpp'), 
       col = 'blue')
  
  # Add lift chart for KNN model.
  plot(performance(prediction(census_data$knn_pred, 
                              census_data$size), 
                   'lift', 'rpp'), 
       col = 'red', 
       add = T)
  
  # Add legend.
  legend('bottomleft', 
         legend = c('RF', 'KNN'), 
         col = c('red', 'blue'), 
         lwd = 2)
