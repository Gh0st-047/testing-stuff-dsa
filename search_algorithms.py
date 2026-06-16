# ============================================================================
#  search_algorithms.py
# ============================================================================
#  OFFLINE LAB TOOLKIT  -  BFS, DFS, IDFS, UCS, A*
#
#  Matches the exact style used in your lab manuals (Lab 06 UCS, Lab 07 A*):
#     - graph is a dictionary of Node objects
#     - Node(state, parent, actions, totalCost, heuristic)
#     - actions = list of (neighbour, weight) tuples
#     - helper functions: findMin() and actionSequence()
#     - every algorithm returns the PATH as a list, e.g. ['C', 'F', 'D', 'B']
#
#  HOW TO USE IN THE EXAM:
#     1. Find the algorithm you need below.
#     2. Read its  "WHAT TO CHANGE IN THE EXAM"  box.
#     3. Replace ONLY the graph / start / goal (and coordinates for A*).
#     4. Run the file:   python search_algorithms.py
#
#  Standard library only. No installs. Immediately runnable.
# ============================================================================

import math


# ----------------------------------------------------------------------------
#  SHARED BUILDING BLOCKS  (used by every algorithm - do NOT change these)
# ----------------------------------------------------------------------------
class Node:
    """One vertex of the graph (same structure as your lab manual)."""
    def __init__(self, state, parent, actions, totalCost, heuristic=None):
        self.state = state          # name of this node, e.g. 'A'
        self.parent = parent        # who we came from (filled during search)
        self.actions = actions      # list of (neighbour, weight) tuples
        self.totalCost = totalCost  # cost of reaching this node (g)
        self.heuristic = heuristic  # (x, y) coordinate -> only A* uses this


def actionSequence(graph, initialState, goalState):
    """Walk parent pointers backwards from goal to start, then reverse.
       Returns the final path as a list (e.g. ['C', 'F', 'D', 'B'])."""
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution


def findMin(frontier):
    """Return the state in the frontier dict with the LOWEST cost.
       frontier format -> { state : (parent, cost) }.
       This is the 'pop the cheapest' step of UCS and A*."""
    minV = math.inf
    node = ''
    for i in sorted(frontier):      # sorted -> ties are broken ALPHABETICALLY
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node


def euclidean(graph, state, goalState):
    """A* heuristic h: straight-line distance from a node's (x,y)
       coordinate to the goal's (x,y) coordinate."""
    (x1, y1) = graph[state].heuristic
    (x2, y2) = graph[goalState].heuristic
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# ============================================================================
#  1) BREADTH FIRST SEARCH (BFS)
# ============================================================================
#  --------------------------------------------------------------------------
#  WHAT TO CHANGE IN THE EXAM
#  --------------------------------------------------------------------------
#  CHANGE THESE (inside bfs_demo() at the bottom of this section):
#     * graph    -> the new graph the instructor gives you
#     * start    -> the start node
#     * goal     -> the goal node
#  Weights are IGNORED by BFS, so you can just put 1 for every edge.
#  Keep everything else (the BFS function itself) UNCHANGED.
#  --------------------------------------------------------------------------
def BFS(graph, initialState, goalState):
    frontier = [initialState]          # a normal QUEUE -> First In First Out
    explored = []
    while len(frontier) != 0:
        currentNode = frontier.pop(0)  # pop(0) = take from FRONT = BFS
        explored.append(currentNode)
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        for child in graph[currentNode].actions:
            child = child[0]           # child = (neighbour, weight) -> take name
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                frontier.append(child)
    return None                        # goal not reachable


def bfs_demo():
    # 1) SAMPLE GRAPH (weights are 1 because BFS ignores them)
    graph = {
        'A': Node('A', None, [('B', 1), ('C', 1)], 0),
        'B': Node('B', None, [('A', 1), ('D', 1), ('E', 1)], 0),
        'C': Node('C', None, [('A', 1), ('F', 1), ('G', 1)], 0),
        'D': Node('D', None, [('B', 1)], 0),
        'E': Node('E', None, [('B', 1), ('H', 1)], 0),
        'F': Node('F', None, [('C', 1)], 0),
        'G': Node('G', None, [('C', 1)], 0),
        'H': Node('H', None, [('E', 1)], 0),
    }
    start = 'A'        # 2) EXAMPLE START NODE
    goal = 'H'         # 3) EXAMPLE GOAL NODE
    path = BFS(graph, start, goal)   # 4) EXAMPLE FUNCTION CALL
    print("BFS path:", path)
    # 5) EXAMPLE OUTPUT:
    #    BFS path: ['A', 'B', 'E', 'H']


# ============================================================================
#  2) DEPTH FIRST SEARCH (DFS)
# ============================================================================
#  --------------------------------------------------------------------------
#  WHAT TO CHANGE IN THE EXAM
#  --------------------------------------------------------------------------
#  CHANGE THESE (inside dfs_demo() at the bottom of this section):
#     * graph    -> the new graph
#     * start    -> the start node
#     * goal     -> the goal node
#  Weights are IGNORED by DFS (put 1 for every edge).
#  Keep the DFS function itself UNCHANGED.
#  (Only difference from BFS: pop(-1) instead of pop(0) -> goes DEEP first.)
#  --------------------------------------------------------------------------
def DFS(graph, initialState, goalState):
    frontier = [initialState]           # used as a STACK -> Last In First Out
    explored = []
    while len(frontier) != 0:
        currentNode = frontier.pop(-1)  # pop(-1) = take from BACK = DFS
        explored.append(currentNode)
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        for child in graph[currentNode].actions:
            child = child[0]
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                frontier.append(child)
    return None


def dfs_demo():
    # 1) SAMPLE GRAPH
    graph = {
        'A': Node('A', None, [('B', 1), ('C', 1)], 0),
        'B': Node('B', None, [('A', 1), ('D', 1), ('E', 1)], 0),
        'C': Node('C', None, [('A', 1), ('F', 1), ('G', 1)], 0),
        'D': Node('D', None, [('B', 1)], 0),
        'E': Node('E', None, [('B', 1), ('H', 1)], 0),
        'F': Node('F', None, [('C', 1)], 0),
        'G': Node('G', None, [('C', 1)], 0),
        'H': Node('H', None, [('E', 1)], 0),
    }
    start = 'A'        # 2) EXAMPLE START NODE
    goal = 'G'         # 3) EXAMPLE GOAL NODE
    path = DFS(graph, start, goal)   # 4) EXAMPLE FUNCTION CALL
    print("DFS path:", path)
    # 5) EXAMPLE OUTPUT:
    #    DFS path: ['A', 'C', 'G']


# ============================================================================
#  3) ITERATIVE DEEPENING DEPTH FIRST SEARCH (IDFS)
# ============================================================================
#  --------------------------------------------------------------------------
#  WHAT TO CHANGE IN THE EXAM
#  --------------------------------------------------------------------------
#  CHANGE THESE (inside idfs_demo() at the bottom of this section):
#     * graph    -> the new graph
#     * start    -> the start node
#     * goal     -> the goal node
#     * maxDepth -> only raise it if the graph is very deep (default 50 is fine)
#  Weights are IGNORED (put 1 for every edge).
#  Keep the DLS and IDFS functions UNCHANGED.
#  --------------------------------------------------------------------------
def DLS(graph, currentNode, goalState, limit, explored):
    """Depth Limited Search: a DFS that is not allowed to go deeper than 'limit'."""
    explored.append(currentNode)
    if currentNode == goalState:
        return True
    if limit <= 0:
        return False                 # hit the depth wall -> stop going deeper
    for child in graph[currentNode].actions:
        child = child[0]
        if child not in explored:
            graph[child].parent = currentNode
            if DLS(graph, child, goalState, limit - 1, explored):
                return True
    return False


def IDFS(graph, initialState, goalState, maxDepth=50):
    """Run DLS with limit = 0, 1, 2, ... until the goal is found."""
    for limit in range(maxDepth):
        for s in graph:              # reset parents before each new round
            graph[s].parent = None
        explored = []
        if DLS(graph, initialState, goalState, limit, explored):
            return actionSequence(graph, initialState, goalState)
    return None


def idfs_demo():
    # 1) SAMPLE GRAPH
    graph = {
        'A': Node('A', None, [('B', 1), ('C', 1)], 0),
        'B': Node('B', None, [('A', 1), ('D', 1), ('E', 1)], 0),
        'C': Node('C', None, [('A', 1), ('F', 1), ('G', 1)], 0),
        'D': Node('D', None, [('B', 1)], 0),
        'E': Node('E', None, [('B', 1), ('H', 1)], 0),
        'F': Node('F', None, [('C', 1)], 0),
        'G': Node('G', None, [('C', 1)], 0),
        'H': Node('H', None, [('E', 1)], 0),
    }
    start = 'A'        # 2) EXAMPLE START NODE
    goal = 'H'         # 3) EXAMPLE GOAL NODE
    path = IDFS(graph, start, goal)  # 4) EXAMPLE FUNCTION CALL
    print("IDFS path:", path)
    # 5) EXAMPLE OUTPUT:
    #    IDFS path: ['A', 'B', 'E', 'H']


# ============================================================================
#  4) UNIFORM COST SEARCH (UCS)
# ============================================================================
#  --------------------------------------------------------------------------
#  WHAT TO CHANGE IN THE EXAM
#  --------------------------------------------------------------------------
#  CHANGE THESE (inside ucs_demo() at the bottom of this section):
#     * graph    -> the new WEIGHTED graph (the weights MATTER now!)
#     * start    -> the start node
#     * goal     -> the goal node
#  Each edge MUST have its real cost:  ('neighbour', cost).
#  For a 2-way road put the edge on BOTH nodes (see how B<->A appears twice).
#  Keep the UCS function itself UNCHANGED.
#
#  >>> This is the SAME graph as Lab 06 (going from C to B). <<<
#  --------------------------------------------------------------------------
def UCS(graph, initialState, goalState):
    frontier = dict()                  # { state : (parent, cost-so-far) }
    frontier[initialState] = (None, 0)
    explored = []
    while len(frontier) != 0:
        currentNode = findMin(frontier)     # pop the CHEAPEST node
        currentCostSoFar = frontier[currentNode][1]
        graph[currentNode].totalCost = currentCostSoFar
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            newCost = child[1] + currentCostSoFar     # add edge weight
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                frontier[child[0]] = (currentNode, newCost)
            elif child[0] in frontier:
                # found a cheaper (or equal, to match the manual's tie-break)
                # way to a node we already have -> update it
                if frontier[child[0]][1] >= newCost:
                    graph[child[0]].parent = currentNode
                    frontier[child[0]] = (currentNode, newCost)
    return None


def ucs_demo():
    # 1) SAMPLE GRAPH (the weighted graph from Lab 06, Activity 1)
    graph = {
        'A': Node('A', None, [('B', 6), ('C', 9), ('E', 1)], 0),
        'B': Node('B', None, [('A', 6), ('D', 3), ('E', 4)], 0),
        'C': Node('C', None, [('A', 9), ('F', 2), ('G', 3)], 0),
        'D': Node('D', None, [('B', 3), ('E', 5), ('F', 7)], 0),
        'E': Node('E', None, [('A', 1), ('B', 4), ('D', 5), ('F', 6)], 0),
        'F': Node('F', None, [('C', 2), ('E', 6), ('D', 7)], 0),
        'G': Node('G', None, [('C', 3)], 0),
    }
    start = 'C'        # 2) EXAMPLE START NODE
    goal = 'B'         # 3) EXAMPLE GOAL NODE
    path = UCS(graph, start, goal)   # 4) EXAMPLE FUNCTION CALL
    print("UCS path:", path, " total cost:", graph[goal].totalCost)
    # 5) EXAMPLE OUTPUT:
    #    UCS path: ['C', 'F', 'D', 'B']  total cost: 12


# ============================================================================
#  5) A* SEARCH
# ============================================================================
#  --------------------------------------------------------------------------
#  WHAT TO CHANGE IN THE EXAM
#  --------------------------------------------------------------------------
#  CHANGE THESE (inside astar_demo() at the bottom of this section):
#     * graph    -> the new graph. EVERY node needs TWO extra things:
#                     - real edge weights:           ('neighbour', cost)
#                     - its (x, y) coordinate:        the 5th argument
#     * start    -> the start node
#     * goal     -> the goal node
#  The heuristic is the Euclidean distance to the goal's coordinate, computed
#  automatically by euclidean(). For a GRID/MAZE the coordinate is just the
#  cell's (column, row). You normally do NOT need to change the heuristic code.
#
#  >>> This is the SAME maze as Lab 07 (going from A to Y). <<<
#  --------------------------------------------------------------------------
def AStar(graph, initialState, goalState):
    frontier = dict()                  # { state : (parent, f = g + h) }
    frontier[initialState] = (None, euclidean(graph, initialState, goalState))
    explored = []
    while len(frontier) != 0:
        currentNode = findMin(frontier)        # pop the lowest f
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        explored.append(currentNode)
        g_current = graph[currentNode].totalCost
        for child in graph[currentNode].actions:
            g = child[1] + g_current                       # g = path cost
            h = euclidean(graph, child[0], goalState)      # h = guess to goal
            f = g + h                                       # f = g + h
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = g
                frontier[child[0]] = (currentNode, f)
            elif child[0] in frontier:
                if frontier[child[0]][1] > f:              # cheaper f -> update
                    graph[child[0]].parent = currentNode
                    graph[child[0]].totalCost = g
                    frontier[child[0]] = (currentNode, f)
    return None


def astar_demo():
    # 1) SAMPLE GRAPH (the 5x5 maze from Lab 07; 5th value = (x, y) coordinate)
    graph = {
        'A': Node('A', None, [('F', 1)], 0, (0, 0)),
        'B': Node('B', None, [('G', 1), ('C', 1)], 0, (2, 0)),
        'C': Node('C', None, [('B', 1), ('D', 1)], 0, (3, 0)),
        'D': Node('D', None, [('C', 1), ('E', 1)], 0, (4, 0)),
        'E': Node('E', None, [('D', 1)], 0, (5, 0)),
        'F': Node('F', None, [('A', 1), ('H', 1)], 0, (0, 1)),
        'G': Node('G', None, [('B', 1), ('J', 1)], 0, (2, 1)),
        'H': Node('H', None, [('F', 1), ('I', 1), ('M', 1)], 0, (0, 2)),
        'I': Node('I', None, [('H', 1), ('J', 1), ('N', 1)], 0, (1, 2)),
        'J': Node('J', None, [('G', 1), ('I', 1)], 0, (2, 2)),
        'K': Node('K', None, [('L', 1), ('P', 1)], 0, (4, 2)),
        'L': Node('L', None, [('K', 1), ('Q', 1)], 0, (5, 2)),
        'M': Node('M', None, [('H', 1), ('N', 1), ('R', 1)], 0, (0, 3)),
        'N': Node('N', None, [('I', 1), ('M', 1), ('S', 1)], 0, (1, 3)),
        'O': Node('O', None, [('P', 1), ('U', 1)], 0, (3, 3)),
        'P': Node('P', None, [('O', 1), ('Q', 1)], 0, (4, 3)),
        'Q': Node('Q', None, [('L', 1), ('P', 1), ('V', 1)], 0, (5, 3)),
        'R': Node('R', None, [('M', 1), ('S', 1)], 0, (0, 4)),
        'S': Node('S', None, [('N', 1), ('R', 1), ('T', 1)], 0, (1, 4)),
        'T': Node('T', None, [('S', 1), ('U', 1), ('W', 1)], 0, (2, 4)),
        'U': Node('U', None, [('O', 1), ('T', 1)], 0, (3, 4)),
        'V': Node('V', None, [('Q', 1), ('Y', 1)], 0, (5, 4)),
        'W': Node('W', None, [('T', 1)], 0, (2, 5)),
        'X': Node('X', None, [('Y', 1)], 0, (4, 5)),
        'Y': Node('Y', None, [('V', 1), ('X', 1)], 0, (5, 5)),
    }
    start = 'A'        # 2) EXAMPLE START NODE
    goal = 'Y'         # 3) EXAMPLE GOAL NODE
    path = AStar(graph, start, goal)   # 4) EXAMPLE FUNCTION CALL
    print("A* path:", path, " total cost:", graph[goal].totalCost)
    # 5) EXAMPLE OUTPUT:
    #    A* path: ['A', 'F', 'H', 'I', 'N', 'S', 'T', 'U', 'O', 'P', 'Q', 'V', 'Y']
    #    total cost: 12


# ============================================================================
#  RUN EVERY EXAMPLE
# ============================================================================
if __name__ == "__main__":
    print("=" * 50)
    bfs_demo()
    dfs_demo()
    idfs_demo()
    ucs_demo()
    astar_demo()
    print("=" * 50)
