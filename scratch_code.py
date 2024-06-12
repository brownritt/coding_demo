#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A collection of small code snippets that demonstrate
some basic ideas in Python, mostly generalizable to 
other languages

Created on Wed Jun 12 10:27:50 2024

@author: jritt
"""

#%% Bytes and bits

# A bit is one switch
# A byte is 8 bits
#    has 256 possible values

import numpy as np

#%% Data types

# int

a = 3
type(a)

# float 

b = 3.7
type(b)

# Demonstration of round-off error

np.sqrt(16)
np.sqrt(16)**2

np.sqrt(3)**2

np.sqrt(3)**2 == 3

np.sqrt(3)**2 - 3

np.isclose( np.sqrt(3)**2, 3)

float(4)
int(10.7)
np.round(10.7)

# Strings

message = "Hi there"
message2 = "I don't know"

1 + 4
"1" + "4"

# Lists

number_list = [3, 4, 5]
general_list = ['a', 34.5, 9, 'hello']
general_list[0]
general_list[3]
general_list[4]
general_list[-1]

number_list +1
number_list*2
number_list + general_list

number_list.append(78)

# Dictionary 

subjects = {'name':'Jason','department':'Carney'}
subjects
subjects['name']

# Numpy array

number_array = np.array([3,4,5])
number_array + 1

np.array(['a',2,3])
np.array(['a',2,3]) + 1

number_list.sum()

# Pandas DataFrames

# See code from Mon


#%% Flow control



#%% Functions






