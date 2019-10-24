# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:12:14 2019
built up an classifier for the DOTA system 
The hacker rank scoring system has been comprimised. 
Without resorting to NN, 60% on the validation set seems to the be the best

@author: lennie
"""
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis,QuadraticDiscriminantAnalysis
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
df = pd.read_csv("https://s3.amazonaws.com/hr-testcases/368/assets/trainingdata.txt",header=None)
#%% Create encoded features. 

names = np.unique(df.iloc[:,:10].values.flatten())
from sklearn.preprocessing import label_binarize

for_against = [1,1,1,1,1,-1,-1,-1,-1,-1,]
encoded = []

for row in df.iterrows():
        encoded.append(np.array(sum(label_binarize(row[1][:5], classes=names))-sum(label_binarize(row[1][5:10], classes=names))))

encoded_df = pd.DataFrame(encoded)
encoded_df['win'] = df[10]-1

#%% Test train split. 

X_train, X_test, y_train, y_test = train_test_split(
    encoded_df.iloc[:,:96], encoded_df['win'], test_size=0.33, random_state=42)
#%% Trid out LDA and QDA to split or to generate better features. Wasn't succesful. 

QDA = QuadraticDiscriminantAnalysis()
QDA.fit(X_train,y_train) 
#clf.transform(encoded_df.iloc[:2,:96].values)

print("QDA")
QDA.fit(X_train,y_train)
print(QDA.score(X_train,y_train))
print(QDA.score(X_test,y_test))

#%%
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier(n_estimators=100, random_state=0)
ada.fit(X_train, y_train)  

print("ada")
ada.fit(X_train,y_train)
print(ada.score(X_train,y_train))
print(ada.score(X_test,y_test))
#%%
from sklearn.ensemble import RandomForestClassifier

Forest = RandomForestClassifier(n_estimators=100, max_depth=10,
                             random_state=0)
print("Random Forest")
Forest.fit(X_train,y_train)
print(Forest.score(X_train,y_train))
print(Forest.score(X_test,y_test))
#%%

from sklearn.ensemble import GradientBoostingClassifier
GBC = GradientBoostingClassifier(n_estimators=100, learning_rate=0.4,
    max_depth=2, random_state=0)
print("Gradient Boosting")
GBC.fit(X_train,y_train)
print(GBC.score(X_train,y_train))
print(GBC.score(X_test,y_test))
#%%

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state=0, solver='lbfgs')

clf.fit(X_train, y_train)

print("Logistic")
print(clf.score(X_train,y_train))
print(clf.score(X_test,y_test))
#%%
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=50)
neigh.fit(X_train,y_train) 
#neigh.score(encoded_df.iloc[:,:96], encoded_df['win'])
print(neigh.score(X_train,y_train))
print(neigh.score(X_test,y_test))
#%% Try an ensemble classfier


eclf = VotingClassifier(estimators=[('log', clf),('ada',ada)], voting='hard')

eclf.fit(X_train, y_train)

print(eclf.score(X_train,y_train))
print(eclf.score(X_test,y_test))
#%%
