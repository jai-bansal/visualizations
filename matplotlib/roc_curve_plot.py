# This script plots ROC curves and and a lift chart using 'census_data.csv'.

################
# IMPORT MODULES
################
# This section imports necessary modules for this script.
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from matplotlib import style

#############
# IMPORT DATA
#############

# Set working directory.
# This obviously needs to be changed depending on the computer being used.
os.chdir('D:\\Users\\JBansal\\Documents\\GitHub\\visualizations')

# This section imports the data to be used in the script.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

########################
# CLEAN AND PROCESS DATA
########################
# This section cleans and processes 'census_data' so predictive models can be built smoothly.

# Remove null values from 'census_data'.
census_data.dropna(inplace = True)

# Create a variable so that classification models can be built.
# To generate an ROC curve, I need a classification model.
# For a classification model, I generate a binary variable.
census_data['size'] = census_data['Area (sq. miles)'] > census_data['Area (sq. miles)'].median()

##########################
# CREATE PREDICTIVE MODELS
##########################
# This section creates random forest and k nearest neighbor models.
# Since I'm only interested in ROC curves, I do not split the data into training and test sets.
# I also do not scale the data before applying k nearest neighbor for the same reason.

# Create random forest model.
rf = RandomForestClassifier(n_estimators = 1001,
                            oob_score = True,
                            random_state = 666)

# Fit 'rf' on 'census_data'.
rf.fit(census_data[['1960', '1970', '1980', '1990', '2000', '2010']],
       census_data['size'])

# Create k nearest neighbor model.
knn = KNeighborsClassifier()

# Fit 'knn' on 'census_data'.
knn.fit(census_data[['1960', '1970', '1980', '1990', '2000', '2010']],
       census_data['size'])

# Generate predictions for random forest model.
census_data['rf_pred'] = rf.predict_proba(census_data[['1960', '1970', '1980', '1990', '2000', '2010']])[:,1]

# Generate predictions for k nearest neighbor model.
census_data['knn_pred'] = knn.predict_proba(census_data[['1960', '1970', '1980', '1990', '2000', '2010']])[:,1]

#################
# PLOT ROC CURVES
#################
# This section plots ROC curves for the predictive models above.

# Get ROC curve values for random forest and k nearest neighbor models.
rf_roc = roc_curve(census_data['size'],
                   census_data['rf_pred'])
knn_roc = roc_curve(census_data['size'],
                    census_data['knn_pred'])

# Set plot style.
style.use('ggplot')

# Create figure.
fig = plt.figure()

# Add random forest ROC curve.
plt.plot(rf_roc[0],
         rf_roc[1],
         color = 'red',
         label = 'RF')

# Add k nearest neighbor ROC curve.
plt.plot(knn_roc[0],
         knn_roc[1],
         color = 'blue',
         label = 'KNN')

# Add null model reference line.
plt.plot([0, 1],
         [0, 1],
         color = 'black',
         linestyle = '--')

# Add AUC score annotations.
plt.annotate(roc_auc_score(census_data['size'],
                           census_data['rf_pred']),
             color = 'red',
             xy = (0.2, 1.03),
             fontsize = 14)
plt.annotate(round(roc_auc_score(census_data['size'],
                           census_data['knn_pred']),
                   2),
             color = 'blue',
             xy = (0.2, 0.6),
             fontsize = 14)

# Set plot x and y limits.
plt.xlim([-0.1, 1.1])
plt.ylim([-0.1, 1.1])

# Set plot labels.
plt.title('Model ROC Curves')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

# Add legend.
plt.legend(loc = 'lower right')

# Show plot.
plt.show()
