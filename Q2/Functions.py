import math
def sphereFunc(x,y):
    return (x ** 2) + (y ** 2)

def rosenbrockFunc(x,y):
    return 100 * (((x ** 2)- y) ** 2) + (1 - x) ** 2

def griewankFunc(x,y):
    return (((x ** 2) + (y ** 2)) / 4000) - math.cos(x) * math.cos(y / math.sqrt(2)) + 1


