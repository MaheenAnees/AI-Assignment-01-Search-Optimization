from search import *
import pprint

# The class for the Jumping frogs problem that inherits from the SearchProblem class

class JumpingFrogs(SearchProblem):
    
    def __init__(self):
        """
        Initializes the variables needed for the jumping frogs problem

        'G' refers to a green frog
        'B' refers to a brown frog
        '_' refers to an empty spot
        """

        self.curr_state = ['G', 'G', 'G', '_', 'B', 'B', 'B']
        self.start_state = ['G', 'G', 'G', '_', 'B', 'B', 'B']
        self.end_state = ['B', 'B', 'B', '_', 'G', 'G', 'G']

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """

        return self.start_state


    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        return state == self.end_state

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """

        successors = list()
        
        for i in range(len(state)):
            successor = list(state)

            if (state[i] == 'G'):
                try:
                    if (state[i+1] == '_'):
                        successor[i], successor[i+1] = successor[i+1], successor[i]
                        stepCost = 1
                        successors.append((successor, (state, successor), stepCost))


                    elif (state[i+1] == 'B' and state[i+2] == '_'):
                        successor[i], successor[i+2] = successor[i+2], successor[i]
                        stepCost = 2
                        successors.append((successor, (state, successor), stepCost))
                except:
                    continue

            elif (state[i] == 'B'):
                try:
                    if (state[i-1] == '_'):
                        successor[i], successor[i-1] = successor[i-1], successor[i]
                        stepCost = 1
                        successors.append((successor, (state, successor), stepCost))

                    elif (state[i-1] == 'G' and state[i-2] == '_'):
                        successor[i], successor[i-2] = successor[i-2], successor[i]
                        stepCost = 2
                        successors.append((successor, (state, successor), stepCost))
                except:
                    continue

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

            successors = self.getSuccessors(start_state)
            
            for j in range(len(successors)):
                if (successors[j][0] == end_state):
                    totalCost += successors[j][2]

        return totalCost
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.

         In this case, each out of place frog is used to calculate the steps to be taken
         and add to the heuristic. It gives a fairly good approximation that is maximum
         at the start state and decreases to become 0 at the end state. 
        """

        heuristic = 0

        for i in range(len(state)):

            # Out of place Brown frog
            if state[i] != "B" and i < 3:
                for j in range(i, len(state)):
                    if(state[i] == "G"):
                        heuristic += 1

            # Out of place Green frog
            if state[i] != "G" and i > 3:
                for j in range(i):
                    if(state[i] == "B"):
                        heuristic += 1

        return heuristic


        
# For testing the jumping frogs problem
 
problem = JumpingFrogs()

path, cost = aStarSearch(problem)
pp = pprint.PrettyPrinter()

# The output of the path is such that there is a list of tuples with each tuple having a pair
# of states, where the first is the "from" state and the second is the "to" state.

print("The path taken comprises the following steps: ")
pp.pprint(path)
print(f"The cost incurred is: {cost}")