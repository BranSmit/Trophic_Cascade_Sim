import numpy as np
import random as rdm

class Organism:

    population = []
    
    iden = 0

    def __init__(self, species, alive, fertile):
        self.species = species
        self.alive = alive
        self.fertile = fertile


        #Trying to make a method to reproduce, but having
        #Trouble with making the population list.
        #Perhaps it should be a dictionary instead, with the identification number as the key
        #Or maybe I can store the object name as a string?
    def reproduce(self, quantity, species, alive, fertile):
        if self.fertile == True:
            for offspring in range(quantity):
                instace = self.iden
                instace = Organism(species, alive, fertile)
                self.iden = self.iden + 1
                self.population.append(instace) #bad


test = Organism('wolf', True, True)
test.reproduce(6, 'wolf', True, False)
print(test.population)

