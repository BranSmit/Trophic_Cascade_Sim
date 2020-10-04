import numpy as np
import random as rdm


#Defined basic structure of all sub classes
class Organism:

# Master List of all organism objects
    population = []

    
    # Constructor, will pretty much always be modified
    def __init__(self):
        self.ageM = 0
        self.alive = True
        self.fertile = False
        self.id = len(Organism.population)
        print(len(Organism.population))
        Organism.population.append(self)
    # Checks if an organism is fertile, and if true, a given quantity of 
    # Organisms are created, note that fertility does not mean the biological definition,
    # think of it more like a "Will I make babies?" Attribute, this lets us call it every
    # time babies are in season for every organism.
    # THIS MUST BE OVERRIDED IN ALL SUBCLASSES, USE ONLY AS A TEMPLATE FOR COPY & PASTE
    def reproduce(self, quantity):
        if self.fertile == True:
            for offspring in range(quantity):
                self.population.append(self)

    # Kills Organism and makes them infertile
    # Mostly used for getting eaten, but also death by natural causes     
    def die(self):
        self.alive = False
        self.fertile = False
    
    # Increases the age of the animal by an increment of a
    # MONTH, ****not**** a YEAR.<-------IMPORTANT!!!!!!!

    def nextMonth(self):
        pass 

