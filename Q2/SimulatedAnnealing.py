import random
import math
import random
from matplotlib import pyplot as plt

class SimulatedAnnealing:
    def __init__(self, function, limits, minTemp, factor, iterations, stepSize, opType):
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
        self.funcLst = []
        self.stepSize = stepSize
        self.opType = opType    #the operation type: either max or min

    #check whether the coordinates are within the given limits or not
    def checkBoundary(self, x, y):
        if  x >= self.xLower and x <= self.xUpper and y >= self.yLower and y <= self.yUpper:
            return True

    def returnNeighbour(self, x, y):
        #defined neighbourhood with all possible moves
        neighbourhood = [(x + self.stepSize, y), (x - self.stepSize, y), (x, y + self.stepSize), (x, y - self.stepSize),
                 (x - self.stepSize, y - self.stepSize), (x + self.stepSize, y + self.stepSize), (x - self.stepSize, y + self.stepSize), (x + self.stepSize, y - self.stepSize)]
        validMoves = []
        #for every neighbour check whether its in the boundary to consider it as valid move
        for i in range(len(neighbourhood)):
            if self.checkBoundary(neighbourhood[i][0], neighbourhood[i][1]) == True:
                validMoves.append((round(neighbourhood[i][0], 2), round(neighbourhood[i][1], 2)))
        #return a random move from valid moves        
        return validMoves
    
    def algorithm(self):
        #choose initial position randomly within given limits  
        x = random.randint(self.xLower, self.xUpper)
        y = random.randint(self.yLower, self.yUpper)
        temp = self.function(x, y) * 0.2
        #add the x,y, f coords in the plot list for visualization
        self.xcoordLst.append(x)
        self.ycoordLst.append(y)
        self.funcLst.append(self.function(x,y))

        while(temp > self.minTemp):
            for i in range(self.iterations):
                #choose a random neighbour
                newX, newY = random.choice(self.returnNeighbour(x,y))
                delta = self.function(newX, newY) - self.function(x, y)
                if delta > 0 and self.opType == 'max': #for maximum, f(xNew, yNew) should be more than f(x,y)
                    x, y = newX, newY
                elif delta < 0 and self.opType == 'min': #for minimum, f(xNew, yNew) should be less than f(x,y)
                    x, y = newX, newY 
                else:
                    m = math.exp(-(abs(delta)/temp))
                    p = random.uniform(0,1)
                    if p < m:
                        x, y = newX, newY
            #decrease the temp by given factor
            temp = self.coolingFactor * temp
            #add the x,y, f coords in the plot list for visualization
            self.xcoordLst.append(x)
            self.ycoordLst.append(y)
            self.funcLst.append(self.function(x,y))
        


    def visualize(self):
        f, (ax1, ax2) = plt.subplots(2, 1)
        ax1.plot(self.funcLst, marker=".", color="red", label="objective")
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

# limits = [xLower, yLower, xUpper, yUpper] 
func1 = SimulatedAnnealing(function=sphereFunc, limits=[-5,-5,5,5], minTemp = 0.0000001, factor=0.9, iterations=100, stepSize=0.1, opType='max')
func1.algorithm()
func1.visualize()


