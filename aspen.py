from organism import Organism

class Aspen(Organism):

    # Overriding base organisim constructor
    def __init__(self):
        #Extending, but keeping attributes
        super().__init__()
        # Initializing all Aspen trees with a height of 1 cm
        self.height = 1
        # Making all Aspens capable of flowering, keep in mind this is
        # Averaging out among thousands of trees
        self.fertile = True

    def reproduce(self, quantity):
        super().reproduce(quantity)











# test = Aspen()
# print(test.fertile)
# print(test.ageM)
# test.ageup(2)
# print(test.ageM)
# print (len(Organism.population))
# print (len(Aspen.population))
