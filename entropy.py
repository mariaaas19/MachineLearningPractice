# The aim of this script is to understand entropy in machine learning
# and eventually apply this to creating a decision tree.

# Entropy is the measure of uncertainty in data.
# Low entropy --> low levels of uncertainty
# High entropy --> high levels of uncertainty

import math
from decimal import Decimal
from matplotlib import pyplot as plt
import numpy as np

# function to decide what percentage to go up to

p = []
def probability_list(probability,i=0):
    while i <= probability:
        p.append(i)
        i = (i+0.1)
        i = round(i,2)
        print(p)
    return p
#checking function
#hundred_percent =probability_list(1)
#print(hundred_percent)

#entropy function = -plogp, log base 2
e=[0]   #log 0 based 2 is undefined, going to assign it to 0
def entropy_value(p):
    probability=probability_list(p)
    for p in probability:
        if p>0:
            entropy = -p * math.log(p,2)
            e.append(entropy)
            print(3)
            print(e)
    return e,probability    #multiple returns are returned as a tuple

#plots the entropy curve from 0 to the probability entered
#as it is a probability 1 is the highest number it is designed for

def entropy_plot(probability_value):
    axis = entropy_value(probability_value)
    entropy= axis[0]    #accessing values from returned tuple
    probability =axis[1]
    plt.plot(probability,entropy,color='blue')
    plt.title('p v entropy')
    plt.xlabel('p')
    plt.ylabel('entropy')

entropy_plot(1) #displays the whole range of possible probabilities
