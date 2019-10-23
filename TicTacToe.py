# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:58:48 2019
Aborted experimental code, tried to learn from pre-generated code. but it was 
bad. 
@author: lennie
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("Tic_tac_initial_results.csv")
encode_win = {'loss':-1, 'win':1, 'draw':0}
State = [0,0,0,0,0,0,0,0,0]
States = []
for row in df.iterrows():
    State = [0,0,0,0,0,0,0,0,0]
    for i in range(0,7):
        if row[1][i] !="?":
            if i%2==0:
                State[int(row[1][i])]= 1
            else:
                State[int(row[1][i])]= -1
    States.append(State)


df["CLASS"] = df["CLASS"].apply(lambda x: encode_win[x])



    #%%
    
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

clf = LinearDiscriminantAnalysis()
transformed = clf.fit_transform(States, df.CLASS)  

plt.figure()
plt.scatter(transformed[:,0],transformed[:,1], c = df.CLASS.values)

#%%
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(States, df["CLASS"], test_size=0.33, random_state=42)

clf = DecisionTreeClassifier(random_state=0)

#cross_val_score(clf, States, df.CLASS.values , cv=10)

clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

np.sum((np.array(predictions) - np.array(y_test))==0)/len(y_test)
