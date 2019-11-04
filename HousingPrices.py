# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:55:00 2019
Here is a nice example of how to inspect the quality of a linear regression. 

In the example below. There are two data points with moderate leverage but very
large studentized residuals. 

The example comes from the hacker rank challenge. 
https://www.hackerrank.com/challenges/predicting-house-prices/submissions/code/128834191

This code is laid out in my discovery process order rather than a clean pipeline. 

Principles:
    1. In small datasets, be very critical of residual distributions, normality 
    is rare in very small datasets. KFold is important here. 
    2. Think whether more complicated features i.e. polynomial features are required
    or whether it would be better to fit a simple but robust model. 
    3. Stats models has a nice built in function to get an influence plot. 
    4. Huber regressor from Sklearn works pretty well. 
    
Result: full marks on hackerrank with a simple but robust model 
@author: lennie
"""
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy.stats import zscore 
from statsmodels.graphics.regressionplots import influence_plot
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import OLSInfluence
import statsmodels.api as sm

from sklearn.linear_model import HuberRegressor


data = np.array([[0.18, 0.89, 109.85],
[1.0, 0.26, 155.72],
[0.92, 0.11, 137.66],
[0.07, 0.37, 76.17],
[0.85, 0.16, 139.75],
[0.99, 0.41, 162.6],
[0.87, 0.47, 151.77]])

#%% First think I did was a k-fold split of the data to maximize the quality of 
# of my model design given the tiny amount of data. 

kf = KFold(n_splits=3)

# first try with a vanilla Linear regression. 

for train_index, test_index in kf.split(data[:,0]):
   print("TRAIN:", train_index, "TEST:", test_index)
   X_train, X_test = data[train_index,:2], data[test_index,:2]
   y_train, y_test = data[train_index,2], data[test_index,2]
   reg = LinearRegression().fit(X_train, y_train)
#   reg_huber = HuberRegressor().fit(X_train, y_train)
#   model = sm.OLS(y_train,sm.add_constant(X_train)).fit()
   print(reg.score(X_test, y_test))
   print(mean_squared_error(y_test, reg.predict(X_test)))
   residuals = y_test-reg.predict(X_test)
   plt.hist(zscore(residuals))
"""   
while running this the mean squared error was way higher for one of the three 
folds. Normally this indicates bad generalization. 
This could be that the model is too complex and is over fitting. 
However, Given it is only linear model I suspect that an outlier is more likely
the culprit. Of course I can see in the data straight up that this is likely. 
Howver, I wanted to show it systematically. 
"""
#%% Influence plot. 
"""   
A good way of finding outliers of a linear model is to use an influence plot. 
especialy with data < 50 where single outliers are critical. I am just going 
to pump in all of the data to inspect what is going on. I am not doing any model
model training at this point. 
"""

model = sm.OLS(a[:,2],sm.add_constant(a[:,:2])).fit()
fig = sm.graphics.influence_plot(model, alpha  = 0.05, criterion="cooks")
# two of the data points are nasty!
#%% Final Model Approach. 
"""
I am not faced with two choices, remove outliers based on a metric, 
or choose a robust model. 
The Huber loss metric is more robust to outliers than MSE because of the linear
relationship away from the inner std deviations. 
The final model I ended up using was the Huber Regressor. 
I checked in the k fold loop above, it is still not great with the huge outliers,
but I had squeezed enough value out of this excercise and moved on. Also trying
to fit a more complicated approach with 7 data points would be silly

This model got full points on the hacker rank challenge. 
"""

plt.figure()
reg_huber = HuberRegressor().fit(data[:,:2], data[:,2])
residuals = a[:,2] - reg_huber.predict(a[:,:2])
plt.hist(residuals )
