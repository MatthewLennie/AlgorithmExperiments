# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:41:25 2019

Just a bit of experimenting with the Iris data set to playing around with 
decision trees and LDA

Principles Learnt: 
    1. LDA seems effective for this vanilla test case
    2. Random Forest helps with validation error. 
    3. Controlling the depth and number of features helps with over fitting
    4. More trees > More features. 
    5. Both ridiculously fast
    6. 
@author: matt_
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.datasets import load_iris
from sklearn.ensemble import (RandomForestClassifier, ExtraTreesClassifier,
                              AdaBoostClassifier)
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
#%%
# Parameters
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # fine step width for decision surface contours
plot_step_coarser = 0.5  # step widths for coarse classifier guesses
RANDOM_SEED = 13  # fix the seed on each iteration

# Load data
iris = load_iris()

plot_idx = 1

models = [DecisionTreeClassifier(max_depth=None),
          RandomForestClassifier(n_estimators=n_estimators),
          ExtraTreesClassifier(n_estimators=n_estimators),
          AdaBoostClassifier(DecisionTreeClassifier(max_depth=3),
                             n_estimators=n_estimators)]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.33)

scaler = StandardScaler()
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_valid_scaled = scaler.transform(X_test)
#%% RAndom Forest

model = RandomForestClassifier(max_features=3,max_depth=4,n_estimators=6)

model.fit(X_train_scaled, y_train)

scores = model.score(X_train_scaled, y_train)
print(scores)
# Create a title for each column and the console by using str() and
# slicing away useless parts of the string
scores = model.score(X_valid_scaled, y_test)
print(scores)


#%% LDA + Random Forest. 

# Train
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

clf = LinearDiscriminantAnalysis()
x_LDA_train= clf.fit_transform(X_train_scaled, y_train)  
x_LDA_test = clf.transform(X_valid_scaled)

#%%
model = RandomForestClassifier(max_features=2,max_depth=6,n_estimators=1)

model.fit(x_LDA_train, y_train)

scores = model.score(x_LDA_train, y_train)
print(scores)
# Create a title for each column and the console by using str() and
# slicing away useless parts of the string
scores = model.score(x_LDA_test, y_test)
print(scores)
# Seems like the classifier just doesn't need to be as fancy to get good results. 
# less depth and estimators were nessescary. 
# Even with 1 estimator already good. 

#%% Boost 

modelBoost = AdaBoostClassifier(n_estimators=100)

model.fit(x_LDA_train,y_train)

scores = model.score(x_LDA_train, y_train)

print(scores)

scores = model.score(x_LDA_test, y_test)
print(scores)
