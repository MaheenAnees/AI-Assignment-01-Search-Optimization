from search import *


# Reading all the csv files into data structures named cities, connections and heuristics

f = open('CSV\cities.csv', 'r')
cities = list()
connections = dict()
heuristics = dict()

for i in f.readlines():
    cities.append(i[0:-1])
    connections[i[0:-1]] = list()
    heuristics[i[0:-1]] = list()

f.close()

f1 = open('CSV\Connections.csv', 'r')
f2 = open('CSV\heuristics.csv', 'r')
while f1 and f2:
    line1 = f1.readline()[0:-1]
    line2 = f2.readline()[0:-1]
    if line1 == "":
        break   
    if(line1[0] == ','):
        all_cities = line1[1:].split(',')
        continue

    curr_data1 = line1.split(',')
    curr_data2 = line2.split(',')
    curr_city = curr_data1[0]
    for i in range(1, len(curr_data1)):
        connections[curr_city].append((all_cities[i - 1], curr_data1[i]))
        heuristics[curr_city].append((all_cities[i - 1], curr_data2[i]))

f1.close()
f2.close()
    

# The class for the Route planning problem that inherits from the SearchProblem class
 
class RoutePlanning(SearchProblem):
    
    def __init__(self, start, destination, cities, connections, heuristics):
        """
        Initializes the variables needed for the routing problem
        """

        self.start = start
        self.destination = destination
        self.cities = cities
        self.connections = connections
        self.heuristics = heuristics

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """

        return self.start

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        return state == self.destination

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        successors = list()

        for i in range(len(connections[state])):
            if (connections[state][i][1] != '0' and connections[state][i][1] != '-1'):
                successor = connections[state][i][0]
                action = (state, successor)
                stepCost = int(connections[state][i][1])

                successors.append((successor, action, stepCost))

        return successors

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        totalCost = 0

        for i in range(len(actions)):
            start_state = actions[i][0]
            end_state = actions[i][1]
            
            for j in range(len(connections[start_state])):
                if(end_state == connections[start_state][j][0]):
                    totalCost += int(connections[start_state][j][1])

        return totalCost
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """

        return self.heuristics[state][self.cities.index(self.destination)][1]


# For testing the route planning problem

start_city = "Hunza"
end_city = "Naran"
problem = RoutePlanning(start_city, end_city, cities, connections, heuristics)
path, cost = aStarSearch(problem)

print(f"The path taken is: {path}")
print(f"The cost incurred is: {cost}")