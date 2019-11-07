# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:54:31 2019
String Manip and regex practice. 
@author: matt_
"""

import string
# Get a list of punctuation 

punch = string.punctuation
#%%
sample = "aSd. fGsdfsadf,,Asdf.asdf'asdf, asdf"

print(sample.lower())

print(sample.upper())
print(sample.capitalize())

#%% Split function works pretty well. 
import re
names = 'Aaliyah 91 Aaron 57 Abagail 895 Abbey 695 Abbie 650'

re.findall('[a-zA-Z]{1,}',names)

names2 = "grep 'Trinity ' *.summary grep 'Nick ' *.summary grep 'Miguel ' *.summary grep 'Emily ' *.summary"

re.findall("(?<=')\w{1,}(?= ')",names2)

# recipe 
re.split("[!#$%&\()*+,-./:;<=>?@[\\]^_`{|}~]+",sample.lower())


#%% Join Function 
string_list = ['a', 'b','c','d']
print(' '.join(string_list))
print(names.join(string_list))

