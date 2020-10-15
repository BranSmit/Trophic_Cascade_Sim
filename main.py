import matplotlib.pyplot as plt
#import pandas as ps
import numpy as np
import random
from organisms import* # Imports all classes


# This script will be the master script

# First thing we need to do is initialize the ecosystem to imitate the 1995 Greater Yellowstone ecosystem

# First step in that, is creating all of the Aspen trees and Elk
# The problem with that, is that as far as I can tell, no one counted all the aspen trees in yellowstone in 1995
# That means I have to guess, and tune by parameters to make it acurate to real life
# 190000 Aspen  (10x elk)
# 19000 elk
for _ in range(190000):
    Aspen()
for _ in range(19000):
    Elk()

for a in [i for i in Organism.population if type(i) == Aspen]:
    index = a.id
    height = round(np.random.normal(35, 10))
    while height < 0:
        height = round(np.random.normal(35, 10))
    age = round(height / 3.45)
    Organism.population[index].height = height
    Organism.population[index].ageM = age

for a in [i for i in Organism.population if type(i) == Elk]:
    index = a.id
    age = round(np.random.normal(78, 40))
    while age < 0:
        age = round(np.random.normal(78, 40))
    Organism.population[index].ageM = age


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




for years in range(10):
    for months in range(12):
        pass
