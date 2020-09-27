import numpy as np
import random as rdm


#Defined basic structure of all classes
class Organism:

    population = []
    

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
                offspring = Organism(species, alive, fertile)
                self.population.append(offspring) #bad
    
    def die(self):
        self.alive = False
        self.fertile = False

class Aspen(Organism):
    null
