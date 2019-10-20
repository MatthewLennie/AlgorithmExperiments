# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:43:28 2019

Solution to the Stock Trading Hacker Rank Problem. 

There was only 500 data points availiable so it seemed to me that anything other
than the most simple algorithm would be over fitting. Initial analysis of the data
showed a pretty complex structure. 

The final tactic is to simply take a rolling median and compare to the price move. 
Sell high, buy low with no looking at trends. 

If there was more data, would be a nice RL problem. 
@author: matt_
"""

import numpy as np
import math
import pandas as pd
import os
import time 

def printTransactions(m, k, d, names, owned, prices): 
    verbose = False
    State = {key:owned for key,owned in zip(names,owned)}
    State['Bank'] = [m]
    State = pd.DataFrame.from_dict(State)
    
    train = pd.read_csv("train")[names]   
    step = train.tail(1)
    window = 10
    transaction_buffer = []
    if train.shape[0]>window:
       value = (train.tail(window).quantile(0.5)-step).iloc[0]
       
       #Sell Phase iStreet SELL 10
       for key in train.keys():
           #processed_values = value.copy()
           #processed_values[key] = processed_values[key]*State[key].values[0]*k[key]
           if value[key] <0 and State[key].values[0]>0: #if better to sell and has inventory
               Sale = State[key].values[0]*step[key]
               transaction_buffer.append("{1} SELL {0:d}".format(int(State[key].values[0]),key,Sale))
               State[key] = 0 
               #State['Bank'] +=  Sale
               time.sleep(1)
               if verbose:
                   print(value)
                   print(step)
                   print(State)
              
       
               
        #Buy Phase
       for key in value.sort_values(ascending=False).keys():     
            possible_buy = np.floor(State['Bank'].values[0]/step[key])
            
            if possible_buy.values[0] >0 and value[key]>0:
                
                cost = possible_buy*step[key]
                State['Bank'] -= cost
                
                transaction_buffer.append("{1} BUY {0:d}".format(int(possible_buy),key,cost))
                State[key] += possible_buy
                if verbose:     
                    print(value)
                    print(step)
                    print(State)
        

    print(len(transaction_buffer))
    if transaction_buffer:
        [print(x) for x in transaction_buffer]
    return None



if __name__ == '__main__':
    m, k, d = [float(i) for i in input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])
    prices = np.array(prices)
    if os.path.exists("train"):
        train = pd.read_csv("train") 
        newRow = pd.DataFrame(prices[:,-1].transpose()).T
        newRow.columns = names
        
        pd.concat([train[names],newRow]).to_csv("train")
        #train.to_csv("train")   
    else:
        train = pd.DataFrame(prices.transpose(),columns=names)[names].to_csv("train")    
    
    printTransactions(m, k, d, names, owned, prices)  
    
    