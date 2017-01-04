# This script plots ROC curves using 'census_data.csv'.

# LOAD LIBRARIES ----------------------------------------------------------
# This section loads necessary libraries for this script.
library(readr)
library(data.table)
library(dplyr)
library(randomForest)
library(kknn)


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

  
  
   plot(performance(prediction(pred_test$rrf_term_prob, 
                              pred_test$outcome), 
                   'tpr', 'fpr'))
   
   
   
     plot(roc(pred_test$outcome, 
           pred_test$rrf_term_prob), 
       col = 'red', 
       print.auc = T, 
       print.auc.y = 0.5)
  plot(roc(pred_test$outcome, 
           pred_test$adaboost_prob), 
       col = 'blue', 
       print.auc = T, 
       add = T, 
       print.auc.y = 0.75)
    


