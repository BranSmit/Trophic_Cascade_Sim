from organism import Organism
import random as rdm
import math


class Elk(Organism):

    food = []

    def reproduce(self):
        if self.fertile == True:
                self.population.append(Elk())

    def eat(self):
        for i in Organism.population:
            if i.alive == True:
                if type(i) == Aspen:
                    food.append(i)
        for i in range(20):
            prey = rdm.choice(food)
            



    def nextMonth(self):
        self.ageM = self.ageM + 1

# Make Id's for every animal that correspond to their index in the list
#Then use a list comprehension to filter out the desired type, pick 20 or so of those
# Store their ID's and use them as an index to flip their alive boolean to false
