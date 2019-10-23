# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:17:07 2019
A very very basic bot for playing tic tac toe. 

Actor is based on a greedy action search based on the state-action value function 
estimated from simulated random games. 

This off policy learning, there is no updating of the state-value function in
context of the policy. 

Just uses a single look ahead for planning. 

I use MC traces for the value function i.e. I play out a game, then sweep back the
value using the discounting factor. This simple implementation was fairly resilient
to the discounting factor because of the large data vs entropy. 

X are represented as 1 
0 is represented as -1

as are their victory conditions. 

Improvements would switch to epsilon - greedy exploration and would begin to 
update the state-value function. 

TODO: Without randomization, the actor reaches a game theory optimal point 

@author: lennie
"""
from random import choice
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#Checks if the state contains a win
def CheckWin(state):
    win_conditions = np.array([[1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0],\
                               [0,0,1,0,0,1,0,0,1],[1,1,1,0,0,0,0,0,0],\
                               [0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,1,1,1],\
                               [1,0,0,0,1,0,0,0,1],[0,0,1,0,1,0,1,0,0]])
    for win_state in win_conditions:
        state_sum = sum(win_state*state)
        if state_sum ==3:
            return 1
        elif state_sum ==-3:
            return -1     
    return 0
    
#creates a random move from availiable positions. 
def MakeRandomMove(state,turn):
    if 0 in state:
        state[choice(np.where(np.array(state) == [0])[0])]=turn
              
    win_cond = CheckWin(state)
    terminal = False
    if 0 not in state:
        terminal = True
        
    return state, win_cond ,terminal 
        
#Just to plot the state nicely for debugging. 
def showGame(state):
    print(state.reshape(3,3))

# Returns a one step look head of states. 
def ReturnPossibles(state,turn):
    opens = np.where(np.array(state) == [0])[0]
    new_state = []
    for i in opens:
        temp = state.copy()
        temp[i] = turn
        new_state.append(temp.copy())
    return new_state
#%% takes the one step look ahead and plans. 
# Chooses optimal step or returns random when no infomation is present. 
def Plan(state,turn,savFunc):
    possible_turns = ReturnPossibles(state,turn)
    if turn ==-1:
        best_score = 10
    else:
        best_score = -10
        
    for single_action in possible_turns:
#        print(single_action)
        score = savFunc.predict([single_action])[0]
#        print(score)
#        print(best_score)
        
        if turn==1 and score>best_score:
            best_score = score
            
            final_choice = single_action
        elif turn==-1 and score<best_score:
            best_score = score
            
            final_choice = single_action
    
    if abs(best_score)==10:
        print("unable to get best score")
        state,b,terminal = MakeRandomMove(state,turn)
        return state 
    else: 
       return final_choice

#%% Collect random exploration data.       
       
dfGames = []

value_decay = 0.8
for i in range(20000):
    state = np.array([0,0,0,0,0,0,0,0,0])
    terminal= False
    turn = 1
    state_action_values = []
    turn_count = 0 
    state_store = [state.copy()]
    while not terminal:
        
        state, win_cond, terminal = MakeRandomMove(state,turn)
        turn*=-1 #flips between O and X
        turn_count +=1
        state_store.append(state.copy())
        
    #reward*decay**steps
    for i in range(turn_count+1):
        state_action_values.append(win_cond*value_decay**(i))    
    state_action_values=state_action_values[::-1]
    #Throw everything into dataframes.     
    state_store = np.array(state_store)
    cols = [0,1,2,3,4,5,6,7,8]
    df = pd.DataFrame(state_store)
    df['sav'] = state_action_values
    dfGames.append(df)

dfGames = pd.concat(dfGames)


#%% Just used a Decision tree because I wasn't looking to do any online training
# in the first round. 

X_train, X_test, y_train, y_test = train_test_split(dfGames.iloc[:,0:9], \
                                                    dfGames['sav'], \
                                                    test_size=0.33, \
                                                    random_state=42)
clf = DecisionTreeRegressor(random_state=0)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

#%% First up run gave 5% error on validation set. 
# so cheap to generate data, relatively low entropy regression
# overfitting wasn't a real issue for this hacky experiment. 
# I would look into regularizing the tree through pruning, setting maximum depth
# or using an ensemble. Just wasn't nessescary. 
print(mean_squared_error(predictions,y_test))


#%% Play gaames with greedy actor. 
result = []
turn = 1
watch = True

for i in range(1):
    state = np.array([0,0,0,0,0,0,0,0,0])
    terminal= False
    while not terminal:
        state = Plan(np.array(state),turn,clf)

        win_cond = CheckWin(state)
        if 0 not in state:
            terminal = True
        turn*=-1
        if watch:
            showGame(state)
            
    result.append(win_cond)
    
print(result)

