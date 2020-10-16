import random as rdm
import math
# from numba import jit, cuda
#Defined basic structure of all sub classes
class Organism:

# Master List of all organism objects
    population = []
    elapsedM = 0

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
    rf = 0.03

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

    eatQ = 3 # Quantity of trees eaten a month
    killThresh = 50 # Height of tree before elk starts to slow growth instead of kill
    birthRate = 0.5

    def reproduce(self):
        if Organism.elapsedM % 12 == 5:
            if rdm.random() <= Elk.birthRate:  # If this random number is under within the birth rate, the elk will reproduce
                Elk()
    # @jit(target ="cuda") GPU Acceleration test
    def eat(self):
        # TODO: Replace this filter then random check approach with a random check then confirm approach
        # Re writing this segment of code will very likey speed up the program several times over
        a=0
        while a != Elk.eatQ:
            prey = rdm.choice(Organism.population)
            if prey.alive == True:
                if type(prey) == Aspen:
                    if prey.height > Elk.killThresh:
                        prey.gr = prey.gr * 0.6
                    else:
                        prey.die()
                        prey.height = 0
                    a += 1





        # prePrey = [i for i in Organism.population if type(i) == Aspen]
        # prey = [j for j in prePrey if j.alive == True] # returns living aspens
        # # print(len(prey))
        # targets = rdm.sample(prey, Elk.eatQ) # Randomly returns a sample of all living aspens
        # for i in targets:
        #     if Organism.population[i.id].height >= Elk.killThresh: # Checks if tree will survive an elk attack
        #         Organism.population[i.id].gr = Organism.population[i.id].gr * 0.6 # Slows elk growth
        #     else:
        #         Organism.population[i.id].die() # Kills aspen if under threshold
        #         Organism.population[i.id].height = 0 # Set's height to 0

    
    def nextMonth(self):
        if self.alive == True:
            self.ageM = self.ageM + 1 # Increment age
            self.eat()
            #rdmDeath = rdm.randint(1, 100) # picks random number between 0 and 100
            if self.ageM >= 24: # Fertile at 2 years
                self.reproduce()
            if rdm.random() <= 0.01: # checks if the random death occurs
                self.die()

##########################################################################################
##########################################################################################

# Defining the wolf class



class Wolf(Organism):

    # 2d array, the first index is the pack, and the second is the actual wolf itself
    packs = [[]]

    # Chance that wolf will form a new pack instead of joining a new one
    loneWolfChance = 0.3
    # Tweak this as well as the random death chance to get an average pack size of like 9.8

    # Couldnt figure out to use super() so I just copied and pasted :/ 
    # Sorry John OOP
    def __init__(self, pack):
        # pack is an argument for the constructor. This is used for pack inheritence.
        self.ageM = 0 
        self.alive = True
        self.id = len(Organism.population)
        self.fertile = False 
        # Standard atributes^^^^
        self.alpha = False # All wolves are born as non breeding ("alpha" is an innacurate term, but it's short and clear)
        # There will only be one alpha per pack, for simplicity there will only be the "Alpha Female"
        self.pack = pack   # Pup inherits mother's pack identity
        self.packId = len(Wolf.packs[pack]) 
        # Much like the global id attribute, the packId attribute is the Index of the wolf inside it's pack
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
                litterSize = range(rdm.choice(range(3,7))) 
                # Wolves will have litters of 3 to 6 pups //This looks like a dumb way to do this, but who *really* cares ¯\_(ツ)_/¯
                for pup in litterSize: # Iterates through litterSize list
                    Wolf(self.pack) # Constructs a new Wolf of the same Pack
    
    def eat(self):
        # TODO: Confirm Wolf eating habits and implement 
        # IIRC the wolves eat about 1 elk per wolf per month
        prePrey = [i for i in Organism.population if type(i) == Elk]
        prey = [j for j in prePrey if j.alive == True] # returns living Elk
        rdmEat = rdm.random()
        if rdmEat < 0.665:  # This should create the right number of elk killed on average (18-22 per wolf per year)
            preyQ = 2
        else:
            preyQ = 1
        targets = rdm.sample(prey, preyQ)   # Returns 2 living elk at random
        for i in targets:
            Organism.population[i.id].die() # Kills number of elk based off target list
        

    def die(self):
        # Organism.population[self.id].alive = False 
        # Organism.population[self.id].fertile
        self.alive = False                          # Kills Wolf in global population list
        self.fertile = False
        Wolf.packs[self.pack][self.packId].alive = False     # Kills Wolf in Pack List
        Wolf.packs[self.pack][self.packId].fertile = False 

    def migrate(self):
        if self.ageM == 24:
            self.fertile = True
            if rdm.random() < 0.64:
                oldPackId = self.packId                          # Stores old packId
                oldPack = self.pack                              # Stores old pack
                if rdm.random() < Wolf.loneWolfChance:
                    newPack = rdm.choice(range(len(Wolf.packs))) # Returns the index of a random pack 
                    while newPack == self.pack:                  # Verifies that newPack doesnt equal current pack
                        newPack = rdm.choice(range(len(Wolf.packs)))
                else:
                    newPack = len(Wolf.packs)                    # Uses length before new pack as index of new pack
                    Wolf.packs.append([])                        # Appends blank list with index that matched newPack
                    self.aplha = True
                self.packId = len(Wolf.packs[newPack])           # Reassigns PackId to the index of the new pack
                self.pack = newPack                              # Reassigns Pack to the index of the Wolf.packs list
                Wolf.packs[newPack].append(self)                 # Appends self to new pack
                Wolf.packs[oldPack][oldPackId].alive = False     # Kills old wolf
                Wolf.packs[oldPack][oldPackId].fertile = False   # Makes old wolf infertile (So they can't be re assigned as the new alpha if alpha dies)


    def nextMonth(self):
        # TODO: Implement Pack Migration using PackId's and Age. Do research about this part
        if self.alive == True:
            self.ageM = self.ageM + 1
            self.migrate()
            self.eat()
            if Organism.elapsedM % 12 == 4: # Only reproduce in april
                self.reproduce()
            if rdm.random() <= 0.03: # Chance of dying every year ~3%  Consider proportional random death
                self.die()
                if self.aplha == True:
                    Wolf.packs[pack][packId].alpha = False     # Makes sure dead wolves arent alphas
                    self.alpha = False                         # Makes sure dead wolves arent alphas
                    living = [j for j in Wolf.packs[self.pack] if j.alive == True] # Returns a list of living wolves in this pack
                    nextAlpha = [j for j in living if j.fertile == True] # Returns a list of fertile living wolves (Look, I know this is a bit redundant and inefficient)
                    # WORKING SLOW CODE IS BETTER THAN OPTIMISED CODE THAT DOESNT RUN
                    nextAlphaId = nextAlpha[0].packId
                    Wolf.packs[self.pack][nextAlphaId].alpha = True  # Makes the next living fertile wolf the Alpha
    

# Initializing the first packs can be done later, you need to figure out how to make a new wolf inherit it's mothers pack
# Then once that's figured out, try creating a method that moves the wolves around between packs. Either use a numpy 2d array
# Or a basic 2D array as a list of lists. Possibly will need another atribute that can store it's multi dimensional index 
# use an attribute in the constructor as an argument for pack inheritence (self.pack)
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