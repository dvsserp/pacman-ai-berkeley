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

import util

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print("start", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's Successors", problem.getSuccessors(problem.getStartState()))
    stack = util.Stack()
    visited = set()
    path = []
    visited.add(problem.getStartState())
    rDFS(problem, visited, path, problem.getStartState(), stack)
    return path

# problem.getStartState() =(5, 5)

def rDFS(problem, visited, path, state, stack):
    if (problem.isGoalState(state)==True):
        temp = state 

        while(stack.isEmpty()!= True):
            successor = stack.pop()
            parent = stack.pop()
            if (temp == successor[0]):
                path.insert(0, successor[1])
                temp = parent


        return True
    for successor in problem.getSuccessors(state):
        if (successor[0] not in visited):
            visited.add(successor[0])
            stack.push(state)
            stack.push(successor)
        
            if (rDFS(problem, visited, path, successor[0], stack)):
                return True

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    stack = util.Stack()
    queue.push(problem.getStartState())
    visited = set()
    visited.add(problem.getStartState())
    path = []
    while (queue.isEmpty() != True):
       state = queue.pop()
       if (problem.isGoalState(state) == True):
            temp = state
            while (stack.isEmpty()!= True): 
                successor = stack.pop()  
                parent = stack.pop()
                if (temp == successor[0]):
                    path.insert(0, successor[1])
                    temp = parent
            return path
       for successor in problem.getSuccessors(state):
            if (successor[0] not in visited):
                visited.add(successor[0])
                stack.push(state)
                stack.push(successor)
                queue.push(successor[0])
            

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    stack = util.Stack()
    visited = set()
    path = []
    start = [problem.getStartState(),0]
    pq.push(start, start[1])
    visited.add(problem.getStartState())
    # [[(5,5), 0], 0]
    # if we have a successor: [((5, 4),'South','1'), 1]

    while pq.isEmpty()is not True:
        node = pq.pop()

        if (node[0]== problem.getStartState()):
            state = node[0]
        else:
            state = node[0][0]

        if(problem.isGoalState(state)==True):
            temp = state
            while (stack.isEmpty()!= True):
                successor = stack.pop()
                parent = stack.pop()
                if (temp == successor[0]):
                    path.insert(0,successor[1])
                    temp = parent
            return path

        for successor in problem.getSuccessors(state):
            if (successor[0] not in visited or problem.isGoalState(successor[0] == True)):
                temp = [successor, node[1] + successor[2]]
                visited.add(successor[0])
                stack.push(state)
                stack.push(successor)
                pq.push(temp, temp[1])
             

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    path = []
    visited = set()
    visited.add(problem.getStartState())
    pq = util.PriorityQueue()

    start = [problem.getStartState(), 0, 0]

    pq.push(start, start[2])
    
    while pq.isEmpty() is False:
        node = pq.pop()
        #[(5,5), 0]
        #[((5,4), 'South', '1'), 1]
        if (node[0] == problem.getStartState()):
            state = node[0]
        else:
            state = node[0][0]

        if problem.isGoalState(state) is True:
            temp = state
            while stack.isEmpty() is False:
                succ = stack.pop()
                parent = stack.pop()

                if (temp == succ[0]):
                    path.insert(0, succ[1])
                    temp = parent
            return path
        for successor in problem.getSuccessors(state):
            if (successor[0] not in visited or problem.isGoalState(successor[0]) is True):
                visited.add(successor[0])
                stack.push(state)
                stack.push(successor)
                temp = [successor, node[1] + successor[2], node[1] + successor[2] + heuristic(successor[0],problem)]

            # heuristic(state, problem)
                pq.push(temp, temp[2])



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
