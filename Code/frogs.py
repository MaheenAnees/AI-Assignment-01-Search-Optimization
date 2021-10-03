from search import *
import pprint


class JumpingFrogs(SearchProblem):
    
    def __init__(self):
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
                if (state[i+1] == '_'):
                    successor[i], successor[i+1] = successor[i+1], successor[i]
                    stepCost = 1
                    successors.append((successor, (state, successor), stepCost))


                elif (state[i+1] == 'B' and state[i+2] == '_'):
                    successor[i], successor[i+2] = successor[i+2], successor[i]
                    stepCost = 2
                    successors.append((successor, (state, successor), stepCost))

            elif (state[i] == 'B'):
                if (state[i-1] == '_'):
                    successor[i], successor[i-1] = successor[i-1], successor[i]
                    stepCost = 1
                    successors.append((successor, (state, successor), stepCost))

                elif (state[i-1] == 'G' and state[i-2] == '_'):
                    successor[i], successor[i-2] = successor[i-2], successor[i]
                    stepCost = 2
                    successors.append((successor, (state, successor), stepCost))

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
        """

        num_different

        for i in range(len(state)):
            if (state[i] != self.end_state[i]):
                num_different += 1

        return num_different

        


j = JumpingFrogs()
#j.getSuccessors(['G', 'G', 'G', '_', 'B', 'B', 'B'])
# j.getCostOfActions([(['G', 'G', 'G', '_', 'B', 'B', 'B'], ['G', 'G', '_', 'G', 'B', 'B', 'B']),
# (['G', 'G', '_', 'G', 'B', 'B', 'B'], ['G', 'G', 'B', 'G', '_', 'B', 'B'])])