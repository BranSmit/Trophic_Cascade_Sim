# import matplotlib.pyplot as plt
#import pandas as ps
import numpy as np
import random
# from numba import jit, cuda
from timeit import default_timer as timer
from organisms import* # Imports all classes

# This script will be the master script

# First thing we need to do is initialize the ecosystem to imitate the 1995 Greater Yellowstone ecosystem

def setInitState():
    # First step in that, is creating all of the Aspen trees and Elk
    # The problem with that, is that as far as I can tell, no one counted all the aspen trees in yellowstone in 1995
    # That means I have to guess, and tune by parameters to make it acurate to real life
    # 190000 Aspen 
    # 19000 elk    742659 
    for _ in range(190000):
        Aspen()
    for _ in range(19000):
        Elk()

    # This whole block of code is for setting up the Aspen stats
    for a in [i for i in Organism.population if type(i) == Aspen]:
        index = a.id
        height = round(np.random.normal(35, 10))
        while height < 0:                               # If the value is a negative, it's re rolled until positive
            height = round(np.random.normal(35, 10))
        age = round(height / 3.45)
        Organism.population[index].height = height 
        Organism.population[index].ageM = age 

    # This block of code sets up the stats for the elk
    for a in [i for i in Organism.population if type(i) == Elk]:
        index = a.id
        age = round(np.random.normal(78, 40))
        while age < 0:                                  # If the value is negative, it's re rolled until positive
            age = round(np.random.normal(78, 40))
        Organism.population[index].ageM = age           
        # The ages of the elk is a normal distribution, with a guesstimate standard deviation.
        # This is mostly a way to make the elk

a = 0
for trials in range(5):                             # Number of trials per initial conditions
    Organism.population.clear()
    setInitState()
    for years in range(10):                         # Controls duration of years in experiment
        for months in range(12):                    # Makes it so theres 12 months in the year
            print('SUCESS')
            Organism.elapsedM = Organism.elapsedM + 1
            quop = [i for i in Organism.population if type(i) == Aspen]
            jack = [j for j in quop if j.alive == True] # returns living aspens
            print(len(jack))
            print ("month", Organism.elapsedM)
            start = timer()
            for instance in Organism.population:
                instance.nextMonth()
            print(timer()-start)












# for i in Organism.population:
#     i.reproduce()

# # # mu, sigma = 35, 10
# s = np.random.normal(78, 40, 1000)

# count, bins, ignored = plt.hist(s, 30, density=True)
# # # # plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
# # # #                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
# # # #          linewidth=2, color='r')
# # # plt.plot(count)
# plt.show()
