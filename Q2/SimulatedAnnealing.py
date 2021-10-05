import random
import math
import random
from matplotlib import pyplot as plt

class SimulatedAnnealing:
    def __init__(self, function, limits, minTemp, factor, iterations, stepSize):
        self.function = function
        self.xLower = limits[0]
        self.yLower = limits[1]
        self.xUpper = limits[2]
        self.yUpper = limits[3]
        self.minTemp = minTemp
        self.coolingFactor = factor
        self.iterations = iterations
        self.xcoordLst = []
        self.ycoordLst = []
        self.coordLst = []
        self.stepSize = stepSize

    def returnNeighbour(self, x, y):
        neighbourhood = [(x + self.stepSize, y), (x - self.stepSize, y), (x, y + self.stepSize), (x, y - self.stepSize),
                 (x - self.stepSize, y - self.stepSize), (x + self.stepSize, y + self.stepSize), (x - self.stepSize, y + self.stepSize), (x + self.stepSize, y - self.stepSize)]
    
    def algorithm(self):
        #choose initial position randomly within given limits  
        x = random.randint(self.xLower, self.xUpper)
        y = random.randint(self.yLower, self.yUpper)
        temp = self.function(x, y) * 0.2

        #add the initial x,y coords in the plot list for visualization
        self.xcoordLst.append(x)
        self.ycoordLst.append(y)

        while(temp > self.minTemp):
            for i in range(self.iterations):
                #choose a random neighbour
                newX, newY = self.returnNeighbour()
                delta = self.function(newX, newY) - self.function(x, y)
                if delta > 0:
                    x, y = newX, newY
                else:
                    m = math.exp((delta/temp))
                    p = random.uniform(0,1)
                    if p < m:
                        x, y = newX, newY
            #decrease the temp by given factor
            temp = self.coolingFactor * temp
            #add the updated/new x,y in plot lists for visualization
            self.xcoordLst.append(x)
            self.ycoordLst.append(y)
            self.coordLst.append(self.function(x,y))






    def visualize(self):
        f, (ax1, ax2) = plt.subplots(2, 1)
        ax1.plot(self.coordLst, marker=".", color="red", label="objective")
        ax2.plot(self.xcoordLst, marker=".", label="x1", color="blue")
        ax2.plot(self.ycoordLst, linestyle="dashed", color="green",  label="x2")
        ax1.legend(), ax2.legend()
        plt.show()


#functions provided
def sphereFunc(x,y):
    return (x ** 2) + (y ** 2)

def rosenbrockFunc(x,y):
    return 100 * (((x ** 2)- y) ** 2) + (1 - x) ** 2

def griewankFunc(x,y):
    return (((x ** 2) + (y ** 2)) / 4000) - math.cos(x) * math.cos(y / math.sqrt(2)) + 1




