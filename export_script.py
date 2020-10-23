

# This is temporarily a testing ground for experiments


class Aspen():
    
    population = []

    # Tunable rate of reproduction
    # height * reproductionFactor = amount of new trees
    rf = 0.1

    # Overwriting base organisim constructor
    def __init__(self):
        # self.ageM = 0
        self.alive = True
        # Initializing all Aspen trees with a height of 1 cm
        self.height = 1
        # Making all Aspens capable of flowering, keep in mind this is
        # Averaging out among thousands of trees
        # self.fertile = True
        # self.id = len(Organism.population)
        self.gr = 4.6
        # Organism.population.append(self)
        Aspen.population.append(self)

    def reproduce(self):
        n = self.height * Aspen.rf                      # Base new tree quantity
        floor = math.floor(n-(n/4))                     # Minimum new tree quantity
        ceiling = math.ceil(n+(n/4))                    # Max new tree quantity  
        for _ in range(rdm.randint(floor, ceiling)):    # Loops depending on a random int betwixed the floor and celing
            Aspen()                                     # Appends baby tree in tree list

    def nextMonth(self):
        # if self.alive == True: # Check if alive
        # self.ageM = self.ageM + 1 # Increase Age
        self.height = self.height + self.gr             # Increase height depending on growth factor
        if Organism.elapsedM % 12 == 4:                 # Checks if it's the 4th month of the year
            self.reproduce()                            # calls reproduce
        if rdm.random() <= 0.1 :                        # checks if the random death occurs
            Aspen.population.remove(self)               # Kills tree by removing from list

print(range(0))
for i in range(0):
    print('bruh')