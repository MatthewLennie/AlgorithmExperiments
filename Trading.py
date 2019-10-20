# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:10:16 2019
Early version fo the stock trading algorithm with volume restrictions 
@author: matt_
"""

import pandas as pd
import sklearn 
from statsmodels.distributions.empirical_distribution import ECDF

df = pd.read_csv('http://s3.amazonaws.com/hr-testcases-us-east-1/329/assets/bigger_data_set.txt',header=None,delimiter=' ')
df.set_index(0,inplace=True)

df = df.T


df.drop('UCSC',axis=1,inplace=True)

train, test = sklearn.model_selection.train_test_split(df,shuffle=False)

scaler = sklearn.preprocessing.RobustScaler().fit(train.values)

train_scaled = pd.DataFrame(scaler.transform(train))
test_scaled = pd.DataFrame(scaler.transform(test))

ecfd = ECDF(train['CAL'], side='right')


Spare = 0
Sell = 80
Buy = 20
window = 100

#%% Trading Engine 
#rules cross threshold 
import time
reduced_keys = df.keys()
State = {key:[0] for key in df.keys()}
State['Bank'] = [100]

val

verbose = False
for i,step in enumerate(train.iterrows()):
    k = {key:np.random.randint(-100,100) for i in range(len(df.keys())) for key in df.keys()}
    
def printTransactions(m, k, d, name, owned, prices):
    State = {key:owned for key,owned in zip(name,owned)}
    State['Bank'] = [m]
    train = pd.from_feather("train")  
    step = train.trail(1)
    window = 100
    if train.shape[0]>window:
       value = train.iloc[i-window:i].quantile(0.5)-step[1]
       #Sell Phase iStreet SELL 10
       for key in train.keys():
           processed_values = value.copy()
           processed_values[key] = processed_values[key]*State[key].values[0]*k[key]
           if processed_values[key] <0 and State[key].values[0]>0 and k[key]<0:
               Sale = np.min([-k[key],State[key].values[0]])*step[1][key]
               print("{1} SELL {0:d}".\
                     format(int(np.min([-k[key],State[key].values[0]])),key,Sale))
               State[key] = State[key] - np.min([-k[key],State[key].values[0]])
               #State['Bank'] +=  Sale
               if verbose:
                   print(value)
                   print(step)
                   print(State)
                   time.sleep(1)
               
        #Buy Phase
        
       for key in processed_values.sort_values(ascending=False).keys():     
            possible_buy = np.floor(State['Bank'].values[0]/step[1][key])
            if k[key] >0 and possible_buy >0 and processed_values[key]>0:
                
                cost = np.min([k[key],possible_buy])*step[1][key]
                #State['Bank'] -= cost
                
                print("{1} BUY {0:d}".\
                      format(int(np.min([k[key],possible_buy])),key,cost))
                State[key] = State[key] + np.min([k[key],possible_buy])
                if verbose:     
                    print(value)
                    print(step)
                    print(State)
                    time.sleep(1)
    



                    time.sleep(1)


#%%
            
            
import numpy as np
import math
def printTransactions(m, k, d, name, owned, prices):
    slope_list=[]
    for i in range(k):
        x=np.array([1.0,2.0,3.0,4.0,5.0])
        y= np.array(prices[i])
        A = np.vstack([x, np.ones(len(x))]).T
        slope, constat = np.linalg.lstsq(A, y)[0]
        slope_list.append(slope)
        
    sort_slope = sorted(slope_list)
    amount_remaining= m
    trans={}
    for j in reversed(range(k)):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]<=0 and amount_remaining>=prices[index_slope][-1]:
            #print prices[index_slope][-1]
            num_stock =math.floor(amount_remaining/prices[index_slope][-1])
            amount_remaining = amount_remaining - prices[index_slope][-1]*num_stock
            trans[name[index_slope]] = names[index_slope]+' BUY ' + str(int(num_stock))
            
        
    for j in range(k):
        index_slope = slope_list.index(sort_slope[j])
        if sort_slope[j]>0 and owned[index_slope]>0:
            trans[name[index_slope]] = names[index_slope]+' SELL ' + str(owned[index_slope]) 
            
    print len(trans.keys())
    for x in trans:
        print trans[x]
        
if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)            