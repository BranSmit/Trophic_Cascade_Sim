import random as rdm
import math


#Defined basic structure of all sub classes
class Organism:

# Master List of all organism objects
    population = []
    elapsedM = 1

    # Constructor, will pretty much always be modified
    def __init__(self):
        self.ageM = 0
        self.alive = True
        self.fertile = False
        self.id = len(Organism.population)
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


##########################################################################################
##########################################################################################

# Defining the Aspen Class

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
        self.id = len(Organism.population)
        self.gr = 4.6
        Organism.population.append(self)

    def reproduce(self):
        n = self.height * Aspen.rf # Base new tree quantity
        floor = math.floor(n-(n/4)) # Minimum new tree quantity
        ceiling = math.ceil(n+(n/4)) # Max new tree quantity
        #print(n, floor, ceiling)
        # Loops depending on a random int betwixed the floor and celing
        for _ in range(rdm.randint(floor, ceiling)): 
            Aspen() # Appends baby object in master pop list

    def nextMonth(self):
        
        if self.alive == True: # Check if alive
            self.ageM = self.ageM + 1 # Increase Age
            self.height = self.height + self.gr # Increase height depending on growth factor
            if Organism.elapsedM % 12 == 4: # Checks if it's the 4th month of the year
                self.reproduce() # calls reproduce
            if rdm.random() <= 0.1 : # checks if the random death occurs
                self.die()  # Kills tree and sets height to zero
                self.height = 0

##########################################################################################
##########################################################################################

# Defining the Elk Class

class Elk(Organism):

    # ELK USES DEFAULT CONSTRUCTOR

    eatQ = 60 # Quantity of trees eaten a month
    killThresh = 120 # Height of tree before elk starts to slow growth instead of kill
    birthRate = 0.5

    def reproduce(self):
        if self.fertile == True: 
            if rdm.random() <= birthRate:  # If this random number is under within the birth rate, the elk will reproduce
                Elk()

    def eat(self):
        prePrey = [i for i in Organism.population if type(i) == Aspen]
        prey = [j for j in prePrey if j.alive == True] # returns living aspens
        targets = rdm.sample(prey, eatQ) # Randomly returns a sample of all living aspens
        for i in targets:
            if Organism.population[i.id].height >= killThresh: # Checks if tree will survive an elk attack
                Organism.population[i.id].gr = Organism.population[i.id].gr * 0.6 # Slows elk growth
            else:
                Organism.population[i.id].alive = False # Kills aspen if under threshold

    def nextMonth(self):
        if self.alive == True:
            self.ageM = self.ageM + 1 # Increment age
            self.eat()
            rdmDeath = rdm.randint(1, 100) # picks random number between 0 and 100
            if self.ageM >= 24: # Fertile at 2 years
                self.fertile = True
                self.reproduce()
            if rdmDeath == 1: # checks if the random death occurs
                self.die()

##########################################################################################
##########################################################################################

# Defining the wolf class


# Wolf figures to model off of

 
# use greater yellowstone ecosystem numbers
# average pack size = 9.8
# dont go above 37 a pack ever
# 2-5% lone wolf
# 4-5 years average lifespan
# 50:50 sex ratio 
# usually monogamous, but about 25% of packs have multiple breeding pairs under polygymous matings
# Birth period: mid-April
# Average litter size in Yellowstone: 4.4 at den emergence, 3.2 survive until late December
class Wolf(Organism):

    # 2d array, the first index is the pack, and the second is the actual wolf itself
    packs = [[]]



    # Couldnt figure out to use super() so I just copied and pasted :/ 
    # Sorry John OOP

    def __init__(self, pack):
        # pack is an argument for the constructor. This is used for pack inheritence.
        self.ageM = 0 
        self.alive = True
        self.id = len(Organism.population)
        # Standard atributes minus fertility since only "alpha's" breed ^^^^
        self.alpha = False # All wolves are born as non breeding ("alpha" is an innacurate term, but it's short and clear)
        # There will only be one alpha per pack, for simplicity they will be the "Alpha Female"
        self.pack = pack   # Pup inherits mother's pack identity
        self.packId = len(Wolf.packs[pack]) # Much like the global id attribute, the packId attribute is the Index of the wolf inside it's pack
        # Add this code back if you decide that Wolves need a sex attribute
        #######################################################
        # sex = rdm.random()
        # if sex > 0.5:
        #     self.male = True
        # else:
        #     self.male = False
        #######################################################
        Wolf.packs[pack].append(self) # Appending self to pack list based on pack of mother
        Organism.population.append(self) # Appending self to global population list


    def reproduce(self):
        if self.alpha == True: # Checks if wolf is an alpha
            if len(Wolf.packs[pack]) > 1: # Checks if alpha has a partner. For simplicity we will disregard sex of partner
                litterSize = range(rdm.choice(range(3,7))) # Wolves will have litters of 3 to 6 pups //This looks like a dumb way to do this, but who *really* cares ¯\_(ツ)_/¯
                for pup in litterSize: # Iterates through litterSize list
                    Wolf(self.pack) # Constructs a new Wolf of the same Pack
    
    def eat(self):
        # TODO: Confirm Wolf eating habits and implement 
        # IIRC the wolves eat about 1 elk per wolf per month
        pass

    def die(self):
        #TODO: REMEBER TO KILL BOTH THE .population AND .packs CLONES. Also remember there is no fertile attribute, only alpha.
        pass
        

    def nextMonth(self):
        # TODO: Implement random death scaling with age. REMEBER TO KILL BOTH THE .population AND .packs CLONES
        # TODO: Implement Pack Migration using PackId's and Age. Do research about this part
        self.reproduce()

# Initializing the first packs can be done later, you need to figure out how to make a new wolf inherit it's mothers pack
# Then once that's figured out, try creating a method that moves the wolves around between packs. Either use a numpy 2d array
# Or a basic 2D array as a list of lists. Possibly will need another atribute that can store it's multi dimensional index 
# use an attribute in the constructor as an argument for pack inheritence (self.pack)
