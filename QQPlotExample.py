# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:01:33 2019
Just taken from the stats_models .. 
@author: matt_
"""
from scipy.stats import norm, t, poisson
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
import statsmodels as stats
import numpy as np
dist = norm(2,10)
Samples = np.array([x for x in  dist.rvs(100000)])

qqplot(Samples,norm, fit=True,line='r')


sampleA = np.mean([160+40*x**2 for x in poisson(0.88).rvs(1000000)])
qqplot(Samples,poisson, fit=True,line='r')



#statsmodels.graphics.gofplots.qqplot

from scipy.optimize import curve_fit
parameters, cov_matrix = curve_fit(poisson, bin_middles, entries)