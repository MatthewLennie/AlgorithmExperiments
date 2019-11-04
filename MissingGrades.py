import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
marks = pd.read_json('./Data/training.json',orient = 'records',lines=True)


#%%
x_keys = [x for x in marks.keys() if x!='Mathematics' and x!='serial']

X_train, X_test, y_train, y_test = train_test_split(marks[x_keys],marks['Mathematics'], test_size=0.33, random_state=42)
parameters = {'reg_lambda':[0.1,0.3,1],'reg_alpha':[0.1,0.3,1],'n_estimators':[100,1000],'gamma':[0.1,0.2,0.9],'max_depth':[1,2,3,4],'learning_rate':[0.01,0.1,0.3,0.5]}

clf = xgb.XGBRegressor(base_score = 2,n_jobs=3)
search = GridSearchCV(clf,parameters,cv=3)
search.fit(X_train,y_train)
#clf.fit(X_train,y_train)
#%%

search.get_params()
#%%

plt.hist(abs(search.predict(X_test)-y_test),density=True,bins=range(8),alpha=0.5)
plt.hist( abs(marks['Mathematics'].sample(30000).values-marks['Mathematics'].sample(30000).values),density=True,bins=range(8),alpha=0.5)
