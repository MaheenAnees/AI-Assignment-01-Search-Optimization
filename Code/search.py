# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from util import *

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
       
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

        util.raiseNotDefined()
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        util.raiseNotDefined()


def aStarSearch(problem: SearchProblem):
    """Search the node that has the lowest combined cost and heuristic first.
    
    Reference used for inspiration: 
    https://www.redblobgames.com/pathfinding/a-star/implementation.html
    
    """

    # Initialization of the frontier of the queue and the dictionaries to maintain for the 
    # algorithm. 

    frontier = PriorityQueue() 
    start = problem.getStartState()
    frontier.push(start, 0)

    came_from = dict()
    cost_so_far = dict()
    came_from[str(start)] = None
    cost_so_far[str(start)] = 0

    while not frontier.isEmpty():
        current = frontier.pop()

        # Reaching the goal state
        if (problem.isGoalState(current)):
            break

        # Traversing the neighbors/successors of the current state
        for successor, action, stepCost in problem.getSuccessors(current):
            new_cost = cost_so_far[str(current)] + stepCost

            # Updating costs according to the new information received, if applicable
            if str(successor) not in cost_so_far or new_cost < cost_so_far[str(successor)]:
                cost_so_far[str(successor)] = new_cost
                priority = new_cost + int(problem.getHeuristic(successor))
                frontier.push(successor, priority)
                came_from[str(successor)] = current

    # Using the path travelled to get the states taken at each stage
    path = list()
    node = current
    path.insert(0, (came_from[str(node)], node))

    while came_from[str(node)] != start:
        node = came_from[str(node)] 
        path.insert(0, (came_from[str(node)], node))    

    # Returning the path and the cost of taking that path
    return path, problem.getCostOfActions(path)


    