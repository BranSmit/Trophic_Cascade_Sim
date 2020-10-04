from organism import Organism
import random as rdm
import math


class Aspen(Organism):
    
    # Tunable rate of reproduction
    # height * reproductionFactor = amount of new trees
    rf = 0.3

    # Overwriting base organisim constructor
    def __init__(self):
        self.ageM = 0
        self.alive = True
        # Initializing all Aspen trees with a height of 1 cm
        self.height = 1
        # Making all Aspens capable of flowering, keep in mind this is
        # Averaging out among thousands of trees
        self.fertile = True

    def reproduce(self):
        n = self.height * Aspen.rf # Base new tree quantity
        floor = math.floor(n-(n/4)) # Minimum new tree quantity
        ceiling = math.ceil(n+(n/4)) # Max new tree quantity
        #print(n, floor, ceiling)
        # Loops depending on a random int betwixed the floor and celing
        for _ in range(rdm.randint(floor, ceiling)): 
            Organism.population.append(Aspen()) # Appends baby object in master pop list

    def nextMonth(self):
        self.ageM = self.ageM + 1
        self.height = self.height + 4.6

