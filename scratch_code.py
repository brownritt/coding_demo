#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A collection of small code snippets that demonstrate
some basic ideas in Python, mostly generalizable to 
other languages.

It is unlikely this code will run straight through, as
it is intended to demonstrate some common types of
programming errors.

Created on Wed Jun 12 10:27:50 2024

@author: jritt
"""

#%% Import block

# In general it is best to put all imports at the top
# of your code so it's easy to see all the dependencies

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#%% Bytes and bits

# A bit is one switch
# A byte is 8 bits
#    has 256 possible values


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

# For loops

for k in range(10):
    print(k)
    
for k in range(10):
    print("I'm here")
    print(k)
    print("Now I'm here")

for name in ['Jason','Alexa','Amaris']:
    print(f'My name is {name}')
    
for name in ['Jason','Alexa','Amaris']:
    print(r'My name is {name}')

# while loops (look them up)

# if elif else branching

name = 'Jason'
if name == 'Jason':
    print('I am at the lecturn')
elif name == 'Alexa':
    print('I am in the back')
else:
    print('I do not know my name')

# match-case lookup 

# About vectorization
# Try to get packages to do their own looping

np.array([3,4,5]) + 10


#%% Functions


def z_score(x):
    '''
    Return the z-scored version of array x.
    
    Input: x is a 1D numpy array
    
    Returns array x with its mean subtracted
    and divided by the standard deviation.
    '''
    return ( x - x.mean() ) / x.std()

print("I'm running a mean unit test")
x = np.array([-6,1,3,0,2,0,4.6])
assert np.isclose( z_score(x).mean(), 0 )
print("I passed the unit test")

print("I'm running a std unit test")
x = np.array([-6,1,3,0,2,0,4.6])
assert np.isclose( z_score(x).std(), 1 )
print("I passed the unit test")











