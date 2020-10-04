from organism import Organism
from aspen import Aspen
import random as rdm
import math


class Elk(Organism):


    def reproduce(self):
        if self.fertile == True:
                self.population.append(Elk())

    def eat(self):
        prePrey = [i for i in Organism.population if type(i) == Aspen]
        prey = [j for j in prePrey if j.alive == True]
        targets = rdm.sample(prey, 20)
        for i in targets:
            Organism.population[i.id].alive = False
        for e in Organism.population:
            print (e.alive)

        
    def nextMonth(self):
        self.ageM = self.ageM + 1


j = Aspen()
for i in range(40):
    j.reproduce()

k = Elk()
k.eat()



# Make Id's for every animal that correspond to their index in the list
# Then use a list comprehension to filter out the desired type, pick 20 or so of those
# Store their ID's and use them as an index to flip their alive boolean to false
