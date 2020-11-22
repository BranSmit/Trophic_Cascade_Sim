# import matplotlib.pyplot as plt
#import pandas as ps
import numpy as np
import random
import csv
import statistics as sts
# from numba import jit, cuda
from timeit import default_timer as timer
from organisms import* # Imports all classes

# This script will be the master script


# All the treatments, being the total number of wolves re introduced
totalTreatments = [31, 11,  21, 41, 51]   
firstEvent  = [14,  5,  10, 18, 23]                # Numbers of wolves introduced on month 1 
secondEvent = [17,  6,  11, 23, 28]                # Numbers of wolves intoduced in the coming years 

# First thing we need to do is initialize the ecosystem to imitate the 1995 Greater Yellowstone ecosystem
# FIXME: Update function to fix where the things are pointing
def setInitState(fEvent):
    # First step in that, is creating all of the Aspen trees and Elk
    # The problem with that, is that as far as I can tell, no one counted all the aspen trees in yellowstone in 1995
    # That means I have to guess, and tune by parameters to make it acurate to real life
    # 190000 Aspen 
    # 19000 elk    742659 
    for _ in range(95000):
        Aspen()
    for _ in range(19000):
        Elk() 
    release(fEvent)
    # This whole block of code is for setting up the Aspen stats 
    for a in Aspen.aPopulation:
        height = round(np.random.normal(35, 10))
        while height < 0:                               # If the value is a negative, it's re rolled until positive
            height = round(np.random.normal(35, 10))
        a.height = height 

    # This block of code sets up the stats for the elk
    for a in Elk.ePopulation:
        age = round(np.random.normal(78, 40))
        while age < 0:                                  # If the value is negative, it's re rolled until positive
            age = round(np.random.normal(78, 40))
        a.ageM = age
        # The ages of the elk is a normal distribution, with a guesstimate standard deviation.
        
def release(q):
    j = len(Wolf.packs) 
    packQ = round(q / 7)
    n = packQ + j 
    # print(j, packQ, n)
    while len(Wolf.packs) < n:
        Wolf.packs.append([])
    print(q, "Wolves are being released")
    newpacks = range(packQ)
    i = 0
    for wolfN in range(q):
        g = newpacks[i]
        h = j + g
        i += 1
        if i == len(newpacks):
            i = 0
        if len(Wolf.packs[h]) < 1: 
            Wolf(h, 36, True, True)
        else:
            age = rdm.randint(9, 60)
            if age > 24:
                fertile = True
            else: 
                fertile = False
            Wolf(h, age, fertile, False)
        
def runMonth():
    for i in Aspen.aPopulation:
        i.nextMonth()
    print("ASPEN DONE")
    for i in Elk.ePopulation:
        i.nextMonth()
    print("Elk DONE")
    for pack in Wolf.packs:
        for w in pack:
            w.nextMonth()
    print("WOLVES DONE")

# Resets the populations
def popsClear():
    Aspen.aPopulation.clear()
    Elk.ePopulation.clear()
    Wolf.packs.clear()


# FIXME: use the real numbers to pix totals of initial and trickle wolves
# Also, pretend it took 13 months
# https://bit.ly/3kBDagl
print("""
TROPHIC CASCADE SIMULATOR

Made by Brandon Smith in 2020 for his IB BIO IA


Welcome to TCS, a small computational model of Yellowstone National Park's Wolf Reintroduction effort. TCS is specifically
made to model the effects of Wolf Reintroduction on Mean Aspen height 10 years down the line. This is achieved by simulating proportional amounts
of the most relevant organisms, and modeling their interactions with eachother using basic statistics.

TCS is designed to run on only 1 CPU thread, using under 2 gigs of ram per instance.
It's reccomended to run multiple instances of TCS at once, as long as you leave 1 thread free for your OS/other apps to use.

You must tell TCS which reintroduction preset to simulate. Custom wolf quantities are not stable at the moment.
Population data is logged at the end of every month, and is written into a .csv file in this format:

        | Month | Wolf Pop | Elk Pop | Aspen Pop | Mean Aspen Height |
        |-------|----------|---------|-----------|-------------------|
        |  int  |   int    |   int   |    int    | float (3 Sig Fig) |
        |  int  |   int    |   int   |    int    | float (3 Sig Fig) |
        etc.

You must also indicate what trial is being computed at the moment, so the .csv file can be named accordingly.
        
Wolf Quantity........""",totalTreatments,"""
Index................   0   1   2   3   4

Index 0 is used for the experiment control.  All other Indexes are used for theoretical Wolf quantities.

""")
while True:  
    nIndex = int(input("What is the Index of the Wolf Quantity you would like to simulate?: "))
    if nIndex >= 0 and nIndex <= 4:
        break
    else:
        print(nIndex,"is not a valid input! Try again")
trialNumber = int(input("What trial is this?: "))
fileName = "trtmnt" + str(nIndex) + "_trial" + str(trialNumber)
fileNameCSV = fileName + ".csv"
print("The file name will be :", fileNameCSV)
print("\n########################################################################\n")

# This version seems to give stable Elk numbers
# TODO: Start logging data and produce graphs for quick tweaking, 
# or at lease start writing to a file so I can graph as the program is running

popsClear()
with open(fileNameCSV, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    columns = ["month", "wPop", "ePop", "aPop", "mAHeight"]
    csv_writer.writerow(columns)

fQ = firstEvent[nIndex]
setInitState(fQ)
# try:
for years in range(10):                         # Controls duration of years in experiment
    if years == 1:
    # if Organism.elapsedM == 6:
        # nIndex = firstEvent.index(treatment)
        sQ = secondEvent[nIndex]
        release(sQ)
    for months in range(12):                    # Makes it so theres 12 months in the year
        Organism.elapsedM += 1
        print ("Month", Organism.elapsedM)
        start = timer()
        runMonth()
        print("There are currently ",len(Aspen.aPopulation), " Aspen")
        print("There are currently ", len(Elk.ePopulation), " Elk")
        count = 0
        for e in Wolf.packs:
            # print(e)
            for p in e:
                if p.alive == True:
                    count += 1
        print("There are currently ", count, " Wolves in ", len(Wolf.packs), " Packs!")
        heights = []
        for tree in Aspen.aPopulation:
           heights.append(tree.height)
        mAHeights = round(sts.mean(heights), ndigits=3)
        newRow = [Organism.elapsedM, count, len(Elk.ePopulation), len(Aspen.aPopulation), mAHeights]
        with open(fileNameCSV, "a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(newRow)
        print('SUCCESS')
        print("Month time:",round(timer()-start), "seconds\n")
# except:
    # print("""
    ################################################################################################################################################
    ################################################################################################################################################
    
    
                                                #             THIS SHOULD NEVER HAPPEN.
                                                # THERE HAS BEEN A CRITICAL FAILURE, GOOD LUCK FIXING IT.
    

    ################################################################################################################################################
    ################################################################################################################################################
    # """)     


# There are currently  221842  Aspen
# There are currently  31040  Elk
# 226
# SUCESS
# month 20



# for i in Organism.population:
#     i.reproduce()

# # # mu, sigma = 35, 10
# s = np.random.normal(78, 40, 1000)

# count, bins, ignored = plt.hist(s, 30, density=True)
# # # # plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
# # # #                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
# # # #          linewidth=2, color='r')
# # # plt.plot(count)
# plt.show()
