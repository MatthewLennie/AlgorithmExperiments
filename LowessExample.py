# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:36:36 2019

@author: matt_
"""

import numpy as np
import statsmodels.api as sm
import scipy.pyplot as plt

#%%
import seaborn as sns; sns.set(color_codes=True)
tips = sns.load_dataset("tips")
ax = sns.regplot(x="total_bill", y="tip", data=tips, lowess=True)