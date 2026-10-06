# ==================== CHAPTER 10 - GRAPHS ====================
# Graph.py - 28 questions

# Graph - collection of nodes and edges
# Graph shows relationship - if nodes are cities, then edges are the roads
# A graph can be represented using:
# 1- Adjacency-list (Directed graph)
# 2- Edge-list and array-list   (Undirected graph, we convert edge list to adjacency list)
# 3- Grid

# Directed graph -> node points to another node using arrows
# Directed graph is shown using adjacency list

# Directed graph edges travel in one direction, 
# Undirected graph edges travel in both directions

# SHORTEST PATH - BFS using QUEUE
# LONGEST PATH - DFS using STACK or (RECURSION + DP Memoisation)

# Graph diagram:
#
#     (a) -----> (c)
#      |          |
#      v          v
#     (b) <----- (e)
#      |
#      v
#     (d) <----- (f)

# Adjacency list:
# {
#   a: [b, c],
#   b: [d],
#   c: [e],
#   d: [],
#   e: [b],
#   f: [d]
# }


# --------- Q-1: Graph traversals: -------------
# Graph diagram:
#
#     (a) -----> (c)
#      |          |
#      v          v
#     (b)        (e)
#      |
#      v
#     (d) ----->(f)

# Adjacency list:
# {
#   a: [b, c],
#   b: [d],
#   c: [e],
#   d: [f],
#   e: [],
#   f: []
# }

# Depth First Traversal (DFS):
#   - DFS using STACK or (RECURSION + DP Memoisation)
#  a, b, d, f, c, e

# Breadth First Traversal (BFS):
#   - BFS using QUEUE
#  a, b, c, d, e, f

# --------- Q-2: Graph traversals code -------------
# Graph diagram:
#
#     (a) -----> (c)
#      |          |
#      v          v
#     (b)        (e)
#      |
#      v
#     (d) ----->(f)

graph = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["e"],
  "d": ["f"],
  "e": [],
  "f": []
}

# - Stack based DFS -
def depth_first_traversal(graph, start):
  stack = [ start ]
  while stack:
    current = stack[-1]
    print(current)
    
    stack.pop()
    for neighbor in graph[current]:
      stack.append(neighbor)
# Time O(e) as we iterate over all edges of graph
# Space O(n) as we use stack to store nodes

depth_first_traversal(graph, 'a')
# a, c, e, b, d, f (as we have "a": ["b", "c"])
# will be a, b, d, f, c, e (as we have "a": ["c", "b"])


# - DFS using Iteration -
def depth_first_traversal(graph, current):
  # No base case as ("e": [],  "f": []) are dead ends
  print(current)
  for neighbor in graph[current]:
    depth_first_traversal(graph, neighbor)
# Time O(e) as we iterate over all edges of graph
# Space O(n) as we use recursion stack

depth_first_traversal(graph, 'a')
# will be a, b, d, f, c, e (Normal one, no issue like stack)

# - Queue based DFS -
from collections import deque

def breadth_first_traversal(graph, start):
  queue = deque([ start ])
  while queue:
    current = queue[0]
    print(current)
    
    queue.popleft()
    for neighbor in graph[current]:
      queue.append(neighbor)
# Time O(e) as we iterate over all edges of graph
# Space O(n) as we use queue to store nodes

breadth_first_traversal(graph, 'a')
# will be a, b, c, d, e, f 

# - NO RECURSION DFS -

# ------------- Q-3: DIRECTED Has path -----------------
# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

# Graph diagram:
#
#                 (f)
#                /   \
#               v     v
#             (g) <-- (i) <----- (j)
#              |       |
#              v       v
#             (h)     (k)

# has_path(graph, 'f', 'k') --> True

# Traverse through graph and check if current == dst

# - Stack based DFS -
def has_path(graph, src, dst):
  stack = [src]
  while stack:
    current = stack.pop()
    
    if current == dst:
      return True
      
    for neighbor in graph[current]:
      stack.append(neighbor)

  return False
# Time O(e) as we iterate over all edges of graph
# Space O(n) as we use stack to store nodes

# - Recursion DFS -
def has_path(graph, src, dst):
  if src == dst:
      return True
    
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True

  return False
# Time O(e) as we iterate over all edges of graph
# Space O(n) as we use recursion stack

# - Queue based BFS - (same as stack, instead use deque)
from collections import deque

def has_path(graph, src, dst):
  queue = deque([ src ])
  
  while queue:
    current = queue.popleft()
    
    if current == dst:
      return True
    
    for neighbor in graph[current]:
      queue.append(neighbor)
    
  return False
# Time O(e) as we iterate over all edges of graph
# Space O(n) as we use queue to store nodes

# - NO Recursion BFS -

# ------------- Q-4: UNDIRECTED Has Path -----------------
# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# Graph diagram:
#
# (j) ----- (i) ----- (k) ----- (m)
#                       |
#                       |
#                      (l)
#
# (o) ----- (n)




# undirected_path(edges, 'j', 'm') # -> True

# First Convert edge list -> Adjecency list
# graph = {
#   'i': ['j', 'k'],
#   'j': ['i'],
#   'k': ['i', 'm', 'l'],
#   'm': ['k'],
#   'l': ['k'],
#   'o': ['n'],
#   'n': ['o']
# }

# Mark nodes visited while traversing to prevent cycle

def undirected_path(edges, node_A, node_B):
  graph = build_adjecency_list(edges)
  return has_path(graph, node_A, node_B)
  
def build_adjecency_list(edges):
  graph = {}

  for edge in edges:
    a,b = edge

    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

  return graph

# - Queue based BFS -
# Take visited dictionary visited = {src}
# check before adding in queue, if neighbor not in visited, then add
from collections import deque

def has_path(graph, src, dst):
  visited = set(src)
  queue = deque([src])
  while queue:
    current = queue.popleft()

    if current == dst:
      return True

    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

  return False
  
# - Recursion DFS -
def has_path(graph, src, dst):
  visited = set()
  return _has_path(graph, src, dst, visited)
  
def _has_path(graph, src, dst, visited):
  if src == dst:
    return True

  if src in visited:
    return False

  visited.add(src)
    
  for neighbor in graph[src]:
    if _has_path(graph, neighbor, dst, visited) == True:
      return True

  return False


# Time O(e) and Space O(e)
# Time O(e) as we iterate over all edges of graph
# Space O(e+n) = O(e) as we use  recursion stack/queue and visited set

# ------------- Q-5: Relationship between edges and nodes -----------------
# In a fully connected graph
# e = n * (n - 1) / 2

# e = O(n * (n - 1) / 2) = O(n^2 - n) = O(n^2)
# e = O(n^2)

# NOTE:
# Space O(n) as we use recursion stack/queue 
# Space O(n) as we use visited set
# Space O(n * n) = O(n^2) as we use recursion stack/queue and visited set
# e = O(n^2)
# Space O(e) as we use recursion stack/queue and visited set

# ------------- Q-6: UNDIRECTED Connected component count -----------------
# connected_components_count({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# }) # -> 2

# calls has_path for each node in graph
# Increments count if has_path is true
def connected_components_count(graph):
  visited = set() 
  count = 0

  for node in graph:
    if has_path(graph, node, visited) == True:
      count += 1

  return count


# - Queue based BFS -
# Instead of taking visited = set(src)
# Here we have defined visited = set() and passed as parameter
# then first we check if src in visited, if not then add
from collections import deque

def has_path(graph, src, visited):
  if src in visited:
    return False

  visited.add(src)

  queue = deque([src])

  while queue:
    current = queue.popleft()

    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

  return True

# - Recursion based DFS -
def has_path(graph, src, visited):
  if src in visited:
    return False

  visited.add(src)

  for neighbor in graph[src]:
    has_path(graph, neighbor, visited)

  return True
# Time O(e) as we iterate over all edges of graph
# Space O(e) as we use recursion stack/queue and visited set


# ------------- Q-7: UNDIRECTED Largest Connected component count -----------------
# largest_component({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# }) # -> 4

# Same as Connected component count
# Just instead of connected component true/false
# We are taking current_count and max_count
# Calculate current_count for each connected component
# update max_count is current connected component is Largest
def largest_component(graph):
  visited = set() 
  max_count = 0

  for node in graph:
    current_count = has_path(graph, node, visited)    
    if current_count > max_count:
      max_count = current_count

  return max_count

# - Queue based BFS -
# Calculate current_count for each connected component
from collections import deque

def has_path(graph, src, visited):
  if src in visited:
    return 0

  visited.add(src)

  queue = deque([src])

  current_count = 0
  while queue:
    current = queue.popleft()
    current_count += 1

    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

  return current_count

# - Recursion based DFS -
# Calculate current_count for each connected component
# initially here connected count is 1
# and then increments with each iteration in loop
def has_path(graph, src, visited):
  if src in visited:
    return 0

  visited.add(src)

  current_count = 1
  for neighbor in graph[src]:
    current_count += has_path(graph, neighbor, visited)

  return current_count
# Time O(e) as we iterate over all edges of graph
# Space O(e) as we use recursion stack/queue and visited set

# ------------- Q-8: UNDIRECTED Shortest path distance -----------------
# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]

# Graph diagram (undirected):
#               2  
#         (x) ----- (y)
#       1 /             \3
#      (w)             (z)
#       1 \             /
#         (v) --------'
#               2
     
# shortest_path(edges, 'w', 'z') # -> 2

# DFS is not good for shortest path as it goes deep and then backtracks
# BFS is good for shortest path as it goes level by level and finds the target node at the earliest level

# We will use queue based BFS for path finding
# first build graph from edges
# then using queue based BFS use (node, distance)
# if matches target node return distance
# else with each neighbor increase distance + 1
# if nothing no path return -1
def shortest_path(edges, node_A, node_B):
  graph = build_adjecency_list(edges)
  shortest_path = has_path(graph, node_A, node_B)
  return shortest_path

  
# build graph from edges 
def build_adjecency_list(edges):
  graph = {}

  for edge in edges:
    a,b = edge

    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

  return graph

  
# - queue based BFS -
from collections import deque

def has_path(graph, src, dst):
  visited = set(src)
  queue = deque([(src, 0)])
  while queue:
    current, current_distance = queue.popleft()

    if current == dst:
      return current_distance

    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, current_distance + 1))

  return -1 #asked in question to return -1 (not 0/False)
  
# Time O(e) as we iterate over all edges of graph
# Space O(e) as we use recursion stack/queue and visited set

# SHORTEST PATH - BFS using QUEUE
# LONGEST PATH - DFS using STACK or (RECURSION + DP Memoisation)

# ------------- Q-9: GRID Number of Island -----------------
# grid = [
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'W', 'W', 'L', 'W'],
#   ['W', 'W', 'L', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['L', 'L', 'W', 'W', 'W'],
# ]

# island_count(grid) # -> 3

# DFS
# we will take (row,col) of grid as node for undirected graph
# at any node we can do up (r-1,c), down (r+1,c), left (r,c-1), right (r,c+1)
# we will start from top corner and loop over each node
# if node is water skip, if node is island then explore using DFS
# we can mark visited when exloring and take count 
# finally when loop ends at bottom right, we will return count

# keep mark of visited and keeps count if explore returns true
def island_count(grid):
  visited = set()
  count = 0
  
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if explore(grid, row, col, visited) == True:
        count += 1

  return count

# 3 base cases: not row_inbound or col_inbound, is water, already visited - return False
# explore up, down, left, right and return True
def explore(grid, row, col, visited):
  row_inbound = 0 <= row < len(grid)
  col_inbound = 0 <= col < len(grid[0])

  if not row_inbound or not col_inbound:
    return False

  if grid[row][col] == 'W':
    return False

  pos = (row, col)
  if pos in visited:
    return False
  visited.add(pos)

  explore(grid, row - 1, col, visited)
  explore(grid, row + 1, col, visited)
  explore(grid, row, col - 1, visited)
  explore(grid, row, col + 1, visited)

  return True

# Time: O(row * col), 2 loop for itering over grid nodes and visiting every node once in explore
# Space: O(row * col), we are marking visited and adding to stack

# ------------- Q-10: GRID Minimum size of Island -----------------
# grid = [
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'W', 'W', 'L', 'W'],
#   ['W', 'W', 'L', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['L', 'L', 'W', 'W', 'W'],
# ]

# minimum_island(grid) # -> 2

# DFS
# Same as number of islands, DFS
# just instead of False we will return 0
# and instead of True we will take size count from initial 1 and then increament with up, down, left, right

# for driver function instead of count we will take min_size as infinity 
# and update min_size : if size > 0 and size < min_size
# return min_size at end of loop

# driver method 
def minimum_island(grid):
  visited = set()
  min_size = float('inf')
  
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      size = explore(grid, row, col, visited)
      if size > 0 and size < min_size:
        min_size = size

  return min_size

# explore method
def explore(grid, row, col, visited):
  row_inbound = 0 <= row < len(grid)
  col_inbound = 0 <= col < len(grid[0])

  if not row_inbound or not col_inbound:
    return 0

  if grid[row][col] == 'W':
    return 0

  pos = (row, col)
  if pos in visited:
    return 0
  visited.add(pos)

  size = 1
  size += explore(grid, row - 1, col, visited)
  size += explore(grid, row + 1, col, visited)
  size += explore(grid, row, col - 1, visited)
  size += explore(grid, row, col + 1, visited)

  return size

# Time: O(row * col), 2 loop for itering over grid nodes and visiting every node once in explore
# Space: O(row * col), we are marking visited and adding to stack

# ------------- Q-11: GRID Closest carrot to rabbit -----------------
# grid = [
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'X', 'O', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['O', 'X', 'C', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['C', 'O', 'O', 'O', 'O'],
# ]

# closest_carrot(grid, 1, 2) # -> 4

# Queue based BFS using distance
# earlier for island we just had water 'W' and land 'X'
# Here we have path 'O', wall 'X' and carrot 'C' on grid
# at any node grid[row][col] we have rabbit placed
# and need to find shortest path to carrot from rabbit
# we will use Queue based BFS with distance, same as shortest path
# and increment distance + 1 with extra horizontal distance

# STEP-1 Queue based BFS using distance, return if carrot found
# STEP-2 Add in_bound and outbound check, using delta and for loop
# STEP-3 Mark Visited
# STEP-4 simplify 3 base conditions: row_inbound and col_inbound and not 'X' and not visited
from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  visited = set([(starting_row, starting_col)]) 
  queue = deque([(starting_row, starting_col, 0)])
  while queue:
    row, col, distance = queue.popleft()

    if grid[row][col] == 'C':
      return distance

    deltas = [(1,0),(-1,0),(0,1),(0,-1)]

    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col
      row_inbound = 0 <= neighbor_row < len(grid)
      col_inbound = 0 <= neighbor_col < len(grid[0])
      pos = (neighbor_row, neighbor_col)
      
      if row_inbound and col_inbound and pos not in visited and grid[neighbor_row][neighbor_col] != 'X':
        visited.add(pos)
        queue.append((neighbor_row, neighbor_col, distance + 1))
        
  return -1

# Time: O(row * col), 2 loop for itering over grid nodes and visiting every node once in explore
# Space: O(row * col), we are marking visited and adding to stack


# ------------- Q-12: GRID Shortest Path between 2 Islands -----------------
# grid = [
#   ["W", "W", "W", "L", "L"],
#   ["L", "L", "W", "W", "L"],
#   ["L", "L", "L", "W", "L"],
#   ["W", "L", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
# ]
# best_bridge(grid) # -> 1

# STEP-1: Find a Island (DFS)
# Iterate through each node and when found Island explore

# STEP-2: Find path to next Island (Queue based BFS using distance)
# keep count of paths, return shortest path
def best_bridge(grid):
  # STEP-1: Find a Island (DFS)
  main_island = find_island(grid)
  distance = find_next_island(grid, main_island)
  return distance

  
# STEP-2: Find path to next Island (Queue based BFS using distance)
from collections import deque

def find_next_island(grid, main_island):
  visited = set(main_island)
  queue = deque([])
  
  # marking distance 0 to found island
  for pos in main_island:
    r,c = pos
    queue.append((r,c,0))

  while queue:
    row, col, distance = queue.popleft()

    if grid[row][col] == 'L' and (row,col) not in main_island:
      return distance - 1

    deltas = [(1,0),(-1,0),(0,1),(0,-1)]

    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col
      row_inbound = 0 <= neighbor_row < len(grid)
      col_inbound = 0 <= neighbor_col < len(grid[0])
      neighbor_pos = (neighbor_row, neighbor_col)
      
      if row_inbound and col_inbound and neighbor_pos not in visited:
        visited.add(neighbor_pos)
        queue.append((neighbor_row, neighbor_col, distance + 1))
  
 

# STEP-1: Find a Island (DFS)
# Iterate through each node and when found Island explore
# driver method 
def find_island(grid):
  visited = set()
  
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      island_found = explore(grid, row, col, visited)
      if len(island_found) > 0:
        return island_found

  return set()

# explore method
def explore(grid, row, col, visited):
  row_inbound = 0 <= row < len(grid)
  col_inbound = 0 <= col < len(grid[0])

  if not row_inbound or not col_inbound:
    return visited

  if grid[row][col] == 'W':
    return visited

  pos = (row, col)
  if pos in visited:
    return visited
  visited.add(pos)
  
  explore(grid, row - 1, col, visited)
  explore(grid, row + 1, col, visited)
  explore(grid, row, col - 1, visited)
  explore(grid, row, col + 1, visited)

  return visited
  
# Time: O(row * col), 2 loop for itering over grid nodes and visiting every node once in explore
# Space: O(row * col), we are marking visited and adding to stack

# ------------- Q-13: DIRECTED GRAPH Has cycle-----------------
# has_cycle({
#   "a": ["b"],
#   "b": ["c"],
#   "c": ["a"],
# }) # -> True

# DFS
# WHITE-GREY-BLACK Algorithm
# White - unexplored
# Grey - visiting
# black - visited
# Initially all nodes are white
# When we traverse through graph we mark them as Grey
# And once we reach dead-end no further we mark it as black
# if at any point in traversing if we reach grey again -> cycle

def has_cycle(graph):
  grey = set()
  black = set()

  for node in graph:
    if detect_cycle(graph, node, grey, black) == True:
      return True
  return False

# DFS with grey and black
def detect_cycle(graph, node, grey, black):
  if node in black:
    return False

  if node in grey:
    return True
    
  grey.add(node)

  for neighbor in graph[node]:
    if detect_cycle(graph, neighbor, grey, black) == True:
      return True

  grey.remove(node)
  black.add(node)

  return False
# Time O(e) as we iterate over all edges of graph
# Space O(n) as we use stack to store nodes/recursion stack

# can also use names like visiting and visited instead of grey and black

# ------------- Q-14: UNDIRECTED(ARRAY) Prerequisites to courses -----------------
# numCourses = 6
# prereqs = [
#   (0, 1),
#   (2, 3),
#   (0, 2),
#   (1, 3),
#   (4, 5),
# ]
# prereqs_possible(numCourses, prereqs) # -> True

# Adjecency List
# {
#   0: [1, 2],
#   1: [0, 3],
#   2: [3, 0],
#   3: [2, 1],
#   4: [5],
#   5: [4],
# }

# Directed Graph
# (0) ─── (1)
#  │       │
# (2) ─── (3)

# (4) ─── (5)

# Create Directed Graph from Undirected ARRAY
# now once we have graph we can do detect_cycle
# if we have cycle we cannot do all prerequisites, return False
def prereqs_possible(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  cycle = has_cycle(graph)

  if cycle:
    return False
    
  return True


# build graph (adjecency list) from prereqs array
def build_graph(num_courses, prereqs):
  graph = {}
  for i in range(0, num_courses):
    graph[i] = []

  for pair in prereqs:
    course_a, course_b = pair
    graph[course_a].append(course_b)

  return graph

# build graph
# n = num_courses, p = prereqs
# Time O(n+p) for loop on num_courses and for loop on prereqs
# Space O(n+p) adding in graph - for loop on num_courses and for loop on prereqs

# has_cycle has O(n), O(n) as we iterate over all nodes of graph

#so final Time O(n+p + n) = O(n+p)
#so final Space O(n+p + n) = O(n+p)
# Time O(n+p) and Space O(n+p)






























# =================== GRAPH - 2 ===================




# ------------- Q-15: Knight Attack ------------

# A knight and a pawn are on a chess board. 
# return a number representing the minimum number of moves required for the knight to land ontop of the pawn.
# If it is not possible for the knight to attack the pawn, then return None.
# On a single move, the knight can move in an "L" shape; 
# two spaces in any direction, then one space in a perpendicular direction. 
# This means that on a single move, a knight has eight possible positions it can move to.

# Write a function, knight_attack, that takes in 5 arguments:

# n, kr, kc, pr, pc

# n = the length of the chess board
# kr = the starting row of the knight
# kc = the starting column of the knight
# pr = the row of the pawn
# pc = the column of the pawn

# knight_attack(8, 1, 1, 2, 2) # -> 2
# knight_attack(8, 1, 1, 2, 3) # -> 1

# For shortest path use BFS
# for first move by knight mark level as 1
# next moves, increase levels + 1
# do this until knight meets pawn

# n = no. of rows, cols
# Time: O(n^2), need to visit each cell on grid
# Space: O(n^2), need to mark each cell on grid as visited level by level

from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  visited = set()            # add (kr,kc) to visited set
  visited.add((kr, kc))

  queue = deque([ (kr, kc, 0) ])   # pop first element from queue with level 0
  while len(queue) > 0:
    r, c, step = queue.popleft()
    if (r, c) == (pr, pc):        # if matches, return the step
      return step

    valid_positions = get_valid_positions(n, r, c)

    for neighbor in valid_positions:       # for all neighbors in valid_positions, increment step by + 1, for next level
      neighbor_row, neighbor_col = neighbor
      if neighbor not in visited:         # check and add to visited set
        visited.add(neighbor)
        queue.append((neighbor_row, neighbor_col, step + 1))

  return None                            # if not possible way, return None
  
# - get valid moves from 8 'L' moves
def get_valid_positions(n, r, c):
  positions = [                   # 8 possible 'L' moves
    (r + 2, c + 1),
    (r - 2, c + 1),
    (r + 2, c - 1),
    (r - 2, c - 1),
    (r + 1, c + 2),
    (r - 1, c + 2),
    (r + 1, c - 2),
    (r - 1, c - 2),
  ]

  valid_positions = []           # from 8 moves remove the outbounds
  for pos in positions:
    new_row, new_col = pos
    if 0 <= new_row < n and 0 <= new_col < n:
      valid_positions.append(pos)

  return valid_positions        # add rest to valid positions and return valid positions

# n = no. of rows, cols
# Time: O(n^2), need to visit each cell on grid
# Space: O(n^2), need to mark each cell on grid as visited level by level



# -------- Q-16: can color --------
# Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph.
# The function should return a boolean indicating whether or not it is possible to color 
# nodes of the graph using two colors in such a way that adjacent nodes are always different colors.

# For example, given this graph:

# x-y-z

# It is possible to color the nodes by using red for x and z, 
# then use blue for y. So the answer is True.

# For example, given this graph:

#     q
#    / \
#   s - r

# It is not possible to color the nodes without making two 
# adjacent nodes the same color. So the answer is False.

# can_color({
#   "x": ["y"],
#   "y": ["x","z"],
#   "z": ["y"]
# }) # -> True

# can_color({
#   "q": ["r", "s"],
#   "r": ["q", "s"],
#   "s": ["r", "q"]
# }) # -> False


# every single node node will have different colors than its immediate neighbors
# use DFS and while marking visited add color to node
# while moving next in DFS add different color to node (can be done using bool switch)
#   so, while traversing and marking color on visited,
#   if we encounter different color than we are tring to paint, return False

# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n); stack for recursion and set for visited storing


def can_color(graph):
  coloring = {}
  
  for node in graph: # for every node in graph
    if node not in coloring: # node should not be already colored
      if validate(graph, node, coloring, False) == False:
        return False  # if any one color mismatches during coloring, return False

  return True # else, return True


# --- validate by coloring neighbors and check if already colored --
def validate(graph, node, coloring, current_color):
  if node in coloring:                      # if node already colored, check it is same color as we want to color
    return current_color == coloring[node]   

  coloring[node] = current_color       # else color the node with current color

  for neighbor in graph[node]:     # traverse rest neighbors by switching color (not current_color)
    if validate(graph, neighbor, coloring, not current_color) == False:
      return False       # if any one color mismatches during coloring, return False

  return True # else, return True

# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n); stack for recursion and set for visited storing


# ----------- Q-17: tolerant teams -----------

# Write a function, tolerant_teams, that takes in a list of rivalries as an argument. 
# A rivalry is a pair of people who should not be placed on the same team. 
# The function should return a boolean indicating whether or not it is possible 
# to separate people into two teams, without rivals being on the same team. 
# The two teams formed do not have to be the same size.

# tolerant_teams([
#   ('philip', 'seb'),
#   ('raj', 'nader')
# ]) # -> True

# tolerant_teams([
#   ('philip', 'seb'),
#   ('raj', 'nader'),
#   ('raj', 'philip'),
#   ('seb', 'raj')
# ]) # -> False

# SAME AS CAN COLOR
# Build graph from given list
# use CAN COLOR on the graph

# CAN COLOR
# every single node node will have different colors than its immediate neighbors
# use DFS and while marking visited add color to node
# while moving next in DFS add different color to node (can be done using bool switch)
#   so, while traversing and marking color on visited,
#   if we encounter different color than we are tring to paint, return False

# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n); stack for recursion and set for visited storing

def tolerant_teams(rivalries):
  graph = build_graph(rivalries)
  coloring = {}
  
  for node in graph: # for every node in graph
    if node not in coloring: # node should not be already colored
      if validate(graph, node, coloring, False) == False:
        return False  # if any one color mismatches during coloring, return False

  return True # else, return True


# --- validate by coloring neighbors and check if already colored --
def validate(graph, node, coloring, current_color):
  if node in coloring:                      # if node already colored, check it is same color as we want to color
    return current_color == coloring[node]   

  coloring[node] = current_color       # else color the node with current color

  for neighbor in graph[node]:     # traverse rest neighbors by switching color (not current_color)
    if validate(graph, neighbor, coloring, not current_color) == False:
      return False       # if any one color mismatches during coloring, return False

  return True # else, return True

# -- build graph from list --
def build_graph(edges):
  graph = {}
  
  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []   
    graph[a].append(b)
    graph[b].append(a)    
    
  return graph

# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n); stack for recursion and set for visited storing




# -------------- Q-18: rare routing ------------
# takes in a number of cities (n) and a list of tuples where each tuple represents a direct road that connects a pair of cities.
# return a boolean indicating whether or not there exists a unique route for every pair of cities. 
# A route is a sequence of roads that does not visit a city more than once.
# Cities will be numbered 0 to n - 1.
# You can assume that all roads are two-way roads. 

# For example, given these roads:

# 0 --- 1
# | \
# |  \
# |   \
# 2    3

# There is a unique route for between every pair of cities.
# So the answer is True.


# For example, given these roads:

# 0 --- 1
# | \
# |  \
# |   \
# 2 -- 3

# There are two routes that can be used to travel from city 1 to city 2:
# - first route:  1, 0, 2
# - second route: 1, 0, 3, 2 
# The answer is False, because routes should be unique.

# rare_routing(4, [
#   (0, 1),
#   (0, 2),
#   (0, 3)
# ]) # -> True

#   rare_routing(4, [
#   (0, 1),
#   (0, 2),
#   (0, 3),
#   (3, 2)
# ]) # -> False

# Convert edge list into adjecency list
# for every pair of cities there should be only one unique path
# DFS using track of visited node
# if you visit every node in a graph and did not retraverse visited node -> True
# double visited node -> False

# Case: if 2 components of graph is disconnected
# so, if you start DFS from one node and never visited all nodes -> False

# Case: no need to back track and visited last node
# so pass lastnode in recursion as one, and every pass node
# check neighbor != last node

# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n + n^2) = O(n^2) 
# n = stack for recursion and set for visited storing
# n^2 = convert edge lost into adjecency list 

# -- DFS using visited --
def rare_routing(n, roads):
  graph =  make_graph(n, roads)
  
  visited = set()
  valid = validate(graph, 0, visited, None) # starting from 1st node 0, last_node as None

  if valid and len(visited) == n: # all visited and no separate components len(visited) == n; True
    return True

  return False
  
# -- check for node visited twice --
def validate(graph, node, visited, last_node):
  if node in visited: # if already visited return false
    return False

  visited.add(node)  # add to visited set

  for neighbor in graph[node]: # check for others, if already visited, False
    if neighbor != last_node and validate(graph, neighbor, visited, node) == False:
      return False # no need to back track and visited last node

  return True # else, return True


# -- build graph from list --
def make_graph(n, roads):
  graph = {}
  
  for city in range(n):
    graph[city] = []
    
  for road in roads:
    a, b = road
    graph[a].append(b)
    graph[b].append(a)
    
  return graph

# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n + n^2) = O(n^2) 
# n = stack for recursion and set for visited storing
# n^2 = convert edge lost into adjecency list 
  


# -------- Q-19: topological order -----------
# Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph. The function should return a list containing the topological-order of the graph.

# The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence.

# topological_order({
#   "a": ["f"],
#   "b": ["d"],
#   "c": ["a", "f"],
#   "d": ["e"],
#   "e": [],
#   "f": ["b", "e"],
# }) # -> ['c', 'a', 'f', 'b', 'd', 'e']

# topological_order({
#   "h": ["l", "m"],
#   "i": ["k"],
#   "j": ["k", "i"],
#   "k": ["h", "m"],
#   "l": ["m"],
#   "m": [],
# }) # -> ['j', 'i', 'k', 'h', 'l', 'm']

# Take 4 things: number_of_parents, ready, order, visited
# number_of_parents dictionary = generate dictionary of node : number of parents it have
# ready list : 
      # start with node with 0 parent
      # put its parents in ready list
      # decrease parent count for that node in number_of_parents
      # add node in order list
      # while decreasing parent count if parent count becomes zero, add that into ready list
# order list : takes node from ready list
# visited set: if the node is in order list, mark it as visited


# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n); order and ready list


def topological_order(graph):
  
  # number_of_parents = generate dictionary of node : number of parents it have
  number_of_parents = {}
  for node in graph: # make initial node : 0 parents
    number_of_parents[node] = 0

  for node in graph: # node -> "c": ["a", "f"] and graph[node] -> ["a", "f"]
    for child in graph[node]: # child in graph[node] -> "a": ["f"] and "f": ["b", "e"]
      number_of_parents[child] += 1

  # ready list = start with node with 0 parent
  ready = [node for node in number_of_parents if number_of_parents[node] == 0] 
  order = []

  while ready:
    node = ready.pop() # pop a node from ready list
    order.append(node) # as parent count is 0, put it into order list
    for child in graph[node]: # decrease parent count for that node in number_of_parents
      number_of_parents[child] -= 1 
      if number_of_parents[child] == 0: # while decreasing parent count if parent count becomes zero
        ready.append(child) # add that into ready list
    
  return order

# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n); order and ready list


# --------- Q-20: safe cracking -------------
# Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine the correct combination. Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

# The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit can occur zero or one time in the answer.

# Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination that will unlock the safe. The function should return a string representing the combination.

# safe_cracking([
#   (7, 1),
#   (1, 8),
#   (7, 8),
# ]) # -> '718'

# safe_cracking([
#   (3, 1),
#   (4, 7),
#   (5, 9),
#   (4, 3),
#   (7, 3),
#   (3, 5),
#   (9, 1),
# ]) # -> '473591'


# Convert list into graph [build unidirectional graph, comment # graph[b].append(a) ]
# Find topological order on graph [enter digit 'x' before 'y' ]


# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n + n^2) = O(n^2) 
# n = order and ready list
# n^2 = build graph from list

def safe_cracking(hints):
  graph = build_graph(hints)
  order = topological_order(graph)
  return ''.join(str(digit) for digit in order)

# -- Topological order -----
def topological_order(graph):
  
  # number_of_parents = generate dictionary of node : number of parents it have
  number_of_parents = {}
  for node in graph: # make initial node : 0 parents
    number_of_parents[node] = 0

  for node in graph: # node -> "c": ["a", "f"] and graph[node] -> ["a", "f"]
    for child in graph[node]: # child in graph[node] -> "a": ["f"] and "f": ["b", "e"]
      number_of_parents[child] += 1

  # ready list = start with node with 0 parent
  ready = [node for node in number_of_parents if number_of_parents[node] == 0] 
  order = []

  while ready:
    node = ready.pop() # pop a node from ready list
    order.append(node) # as parent count is 0, put it into order list
    for child in graph[node]: # decrease parent count for that node in number_of_parents
      number_of_parents[child] -= 1 
      if number_of_parents[child] == 0: # while decreasing parent count if parent count becomes zero
        ready.append(child) # add that into ready list
    
  return order

# -- build graph from list --
def build_graph(edges):
  graph = {}
  
  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []   
    graph[a].append(b)
    # graph[b].append(a)    
    
  return graph


# n = number of nodes on graph
# Time: O(n^2); traversing through the graph
# Time: O(n + n^2) = O(n^2) 
# n = order and ready list
# n^2 = build graph from list



# ------------- Q-21: weighted graph min path -----------------
# Write a function that takes in the adjacency list for a weighted graph and two nodes, src and dst. 
# The function should return the minimum cost path that travels from src to dst.
# The cost of a path is the sum of the weights of edges traveled.
# You can assume that the weights are non-negative numbers and there is at least one path between src and dst.

# graph = {
#   "a": { "b": 2, "d": 9, "c": 5 },
#   "b": { "a": 2, "d": 4, "e": 6 },
#   "c": { "a": 5, "e": 4 },
#   "d": { "a": 9, "b": 4, "e": 1 },
#   "e": { "b": 6, "c": 4, "d": 1 },   
# }
# weighted_graph_min_path(graph, "a", "e") # -> 7

# graph = {
#   "a": { "b": 1, "c": 1 },
#   "b": { "c": 3, "a": 1 },
#   "c": { "b": 3, "d": 1, "a": 1 },
#   "d": { "c": 1, "b": 2 },
# }
# weighted_graph_min_path(graph, "a", "d") # -> 2

# Weighted Graph - each edge has an associated weight/cost
# Represented using a nested dictionary { node: { neighbor: weight } }

# {
#   A: { B:2, D:9, C:5 },
#   B: { A:2, D:4, E:6 },
#   C: { A:5, E:4 },
#   D: { A:9, B:4, E:1 },
#   E: { B:6, C:4, D:1 }
# }

# Weighted Graph diagram (undirected):

#          2
#     (A)------(B)
#     | \      / \
#    5|  \9   /4  \6
#     |   \  /     \
#     |   (D)--1--(E)
#     |          /
#    (C)--------'
#          4

#   Edges (with weights):
#     A - B : 2
#     A - D : 9
#     A - C : 5
#     B - D : 4
#     B - E : 6
#     D - E : 1
#     C - E : 4

# Min path from A to E
# BFS for shortest path will not work here, 
    # ADE and ABE are shortest - but actual min path is ABDE
# so, we will use DFS Recursive
# we will start from dst as 0
# and keep going level up adding along edges
# until we find source and the min value path

# visited set difference - here we will allow visited, except in same path

# n = number of nodes on graph
# Time: O(n!); n! paths between src and dst - Factorial
# Space: O(n); For visited set

def weighted_graph_min_path(graph, src, dst):
  return min_path(graph, src, dst, set())

def min_path(graph, src, dst, visited):
  if src == dst: # if reached dst return 0
    return 0

  if src in visited: # if already visited avoid taking that path, inf will never win in min path
    return float('inf')
  visited.add(src)  # if not visited add in set

  min_weight = float('inf')
  for neighbor in graph[src]: # graph[src]: { "b": 1, "c": 1 }
    weight = graph[src][neighbor] # graph[src][neighbor] : 2 and 1
    total_weight = weight + min_path(graph, neighbor, dst, visited) # add current edge weight and recurse for neighbor to dst
    min_weight = min(min_weight, total_weight) # min of total and current weight

  visited.remove(src) # allow visited, except in same path
  return min_weight

# n = number of nodes on graph
# Time: O(n!); n! paths between src and dst - Factorial
# Space: O(n); For visited set




# --------- Q-22: lowest toll ------------
# You are given the tolls for different highways. 
# Each highway connects a pair of cities and has a particular cost that must be paid to use it.
# Each highway toll is a triplet (cityA, cityB, cost). 
# Every highway can be traveled in either direction.
# Write a function that takes in highway tolls and two cities. 
# The function should return the lowest cost required to travel between the two cities. 
# You can assume that there exists at least one way to travel between the two cities.

# highway_tolls = [
#   ("Hampton", "Fairfax", 7.50),
#   ("Roanoake", "Alexandria", 4.20),
#   ("Alexandria", "Hampton", 14.50),
#   ("Hampton", "Roanoake", 8.90),
#   ("Alexandria", "Fairfax", 5.90),
#   ("Hampton", "Manassas", 3.50),
#   ("Fairfax", "Manassas", 2.20),
# ]
# lowest_toll(highway_tolls, "Alexandria", "Hampton") # -> 11.60

# highway_tolls = [
#   ("Hampton", "Fairfax", 7.50),
#   ("Roanoake", "Alexandria", 4.20),
#   ("Alexandria", "Hampton", 14.50),
#   ("Hampton", "Roanoake", 8.90),
#   ("Alexandria", "Fairfax", 5.90),
#   ("Hampton", "Manassas", 3.50),
#   ("Fairfax", "Manassas", 2.20),
# ]
# lowest_toll(highway_tolls, "Alexandria", "Fairfax") # -> 5.90

# we need to find start: Alexandria and dst: Hampton
# Convert Weighted edge list to Weighted Adjecency list
# then use, min path in weighted graph

# Weighted Edge List:
# [
#   [ Hampton,    Fairfax,    7.50 ],
#   [ Roanoake,   Alexandria, 4.20 ],
#   [ Alexandria, Hampton,    14.50 ],
#   [ Hampton,    Roanoake,   8.90 ],
#   [ Alexandria, Fairfax,    5.90 ],
#   [ Hampton,    Manassas,   3.50 ],
#   [ Fairfax,    Manassas,   2.20 ],
# ]

# Weighted Adjacency List:
# {
#   H: { F: 7.50,  A: 14.50, R: 8.90, M: 3.50 },
#   A: { H: 14.50, R: 4.20,  F: 5.90 },
#   R: { H: 8.90,  A: 4.20 },
#   F: { H: 7.50,  A: 5.90,  M: 2.20 },
#   M: { F: 2.20,  H: 3.50 },
# }

# weighted_graph_min_path(graph, "Alexandria", "Hampton") # -> 11.60
# (Alexandria -> Fairfax -> Manassas -> Hampton = 5.90 + 2.20 + 3.50 = 11.60)

# n = number of nodes on graph
# Time: O(n!); n! paths between src and dst - Factorial
# Space: O(n + n^2) = O(n^2)
  # n = For visited set 
  # n^2 for Convert Weighted edge list to Weighted Adjecency list


def lowest_toll(highway_tolls, start_city, end_city):
  weighted_graph = build_weighted_graph(highway_tolls)
  return weighted_graph_min_path(weighted_graph, start_city, end_city)


# -- build weighted adjacency list from weighted edge list --
def build_weighted_graph(edges):
  graph = {}
  for edge in edges:
    a, b, weight = edge

    if a not in graph:
      graph[a] = {}
    if b not in graph:
      graph[b] = {}

    graph[a][b] = weight
    graph[b][a] = weight # undirected: add weight both ways

  return graph

# --- Q-21: weighted graph min path ---
def weighted_graph_min_path(graph, src, dst):
  return min_path(graph, src, dst, set())

def min_path(graph, src, dst, visited):
  if src == dst: # if reached dst return 0
    return 0

  if src in visited: # if already visited avoid taking that path, inf will never win in min path
    return float('inf')
  visited.add(src)  # if not visited add in set

  min_weight = float('inf')
  for neighbor in graph[src]: # graph[src]: { "b": 1, "c": 1 }
    weight = graph[src][neighbor] # graph[src][neighbor] : 2 and 1
    total_weight = weight + min_path(graph, neighbor, dst, visited) # add current edge weight and recurse for neighbor to dst
    min_weight = min(min_weight, total_weight) # min of total and current weight

  visited.remove(src) # allow visited, except in same path
  return min_weight


# n = number of nodes on graph
# Time: O(n!); n! paths between src and dst - Factorial
# Space: O(n + n^2) = O(n^2)
  # n = For visited set 
  # n^2 for Convert Weighted edge list to Weighted Adjecency list























  
# ---------- Q-23: UNION FIND ALGORITHM -----------

# union find
# - graph algorithm
# - very performant when optimized
# - deals with connected-components or "islands"
# - consists of two steps: union and find

# Union Find takes an edge list and builds a "unified structure"
# where every connected-component becomes a tree pointing to a single root.

# original graph:            edges:          unified structure:
#                                            (each node points to a parent,
#    (7)                     [ 3, 2 ]         roots point to themselves)
#     |                      [ 5, 4 ]
#    (8) --- (9)             [ 4, 3 ]            (7) <-- self root
#                            [ 2, 1 ]             ^
#    (0)   (5)               [ 0, 1 ]            (8) <--- (9)
#     |   /   \              [ 3, 1 ]
#    (1)-(3)  (4)            [ 8, 9 ]            (0) <-- self root
#       \ |   / \            [ 4, 6 ]             ^
#        (2) (6) ...         [ 7, 8 ]            (5) <--- (1)(3)(4)
#                                                 ^         |
#                                                (0)       (2)
#                                                (6)

# Component-1 { 7, 8, 9 } -> root 7
# Component-2 { 0, 1, 2, 3, 4, 5, 6 } -> root 0
# NUMBER OF COMPONENTS = 2

# NOTE:
# 1. Node first points to itself (3,2); 3 points itself and 2 points itself
# 2. Then Union happens; 2nd points 1st ; 2 points to 3 (3,2) -> 3 points itself and 2 points to 3
# 3. the one points itself is root of the tree; all other nodes point to the root here 3,2 -> 3 is the root



# ---------------- Q-24: UNION-FIND (FIND COUNT OF COMPONENTS)-----------
#  The function should return the number of connected components in the given graph.

# count_components(7, [
#   (0, 2),
#   (1, 0),
#   (4, 3),
#   (2, 5),
#   (3, 6)
# ]) # -> 2


# we will inplement union find using array
# length of array - numbers in union find
# index of array - all the numbers in edges
# values of array - root of number (root of index as index represents number)
# we iterate over edges and keep updating array values based edge number/index points which root
# to find root, do DFS from number to node where it points itself (root)

# the end we will have indexes(number of edges) and array values (index/edge point which root)
# iterate over array; if array value == index; that is an root
# number of connected components == number of roots

#        (1) <-- self root          (4) <-- self root
#         ^                          ^
#    (5) (0)                    (3) (6)
#         ^
#        (2)

#   array:   [ 1, 1, 0, 4, 4, 1, 4 ]
#   idx:       0  1  2  3  4  5  6

# root -> index 1 and value 1 ; index 4 and value 4
# number of connected components => 2

# Time: O(n) -> iterate over all elements of edges
# Space: O(n) -> array to store all edges values

# -- Count components method --
def count_components(n, edges):
  roots = [ i for i in range(0,n) ] # intialises array same index and same number [0,1,2...]

  for edge in edges: # take edge from edges and send for union (3,2)
    node_a, node_b = edge
    union(roots, node_a, node_b)

  # now we have roots array completed,
  # we can find number of roots; array index and value as same
  # connected components as number of roots
  count = 0
  for i in range(0, n):
    if roots[i] == i:
      count += 1
      
  return count

# -- Union method --
def union(roots, node_a, node_b): #(3,2)
  root_a = find(roots, node_a) # find root of 3
  root_b = find(roots, node_b) # find root of 2

  if root_a == root_b: # if both roots are same, no need to union
    return
  
  roots[root_b] = root_a       # 2 points 3


# -- Finds root for given node --
def find(roots, node):
  if roots[node] == node: # if index and value is same; means points itself; return as root
    return node

  return find(roots, roots[node]) # if not root then go look value stored at index root[node] in roots array 
                          # and find root on that recursively



# Time: O(n) -> iterate over all elements of edges
# Space: O(n) -> array to store all edges values




# ------ Q-25: province sizes [ UNION-FIND WITH SIZES ] ------
# Write a function, provinceSizes, that takes in a number of cities n and a list of roads which connect cities. 
# Roads can be traveled in both directions. 
# Cities are named from 0 to n.

# A "province" is a group of 1 or more cities that are connected by roads. 
# The "size" of a province is the number of cities that make up that province.

# Your function should return a list containing the sizes of the provinces. 
# You may return the result in any order.
# Solve this using Union-Find.

# province_sizes(6, [
#   (4, 5),
#   (1, 0),
#   (2, 3),
#   (0, 5),
#   (5, 1),
#   (4, 0)
# ]) # -> [4, 2]


# SOLUTION:
# same as count components, but instead of counting number of roots, we will count size of each root
# we will have size dictionary, where key is root and value is size of that root
# iterate over roots array, find root for each index and save in size dictionary as value
# sizes[root] = sizes.get(root, 0) + 1
# return list of size dictionary values
  
def province_sizes(n, roads):
  return count_components(n, roads)

# -- Count components method --
def count_components(n, edges):
  roots = [ i for i in range(0,n) ] # intialises array same index and same number [0,1,2...]

  for edge in edges: # take edge from edges and send for union (3,2)
    node_a, node_b = edge
    union(roots, node_a, node_b)

  # now we have roots array completed,
  # take size dixtionary
  # find root for each index and save in size dictionary as value 
  # sizes[root] = sizes.get(root, 0) + 1
  # return list of size dictionary values
  sizes = {}
  for i in range(0, n):
    root = find(roots, i)              # save in size dictionary
    sizes[root] = sizes.get(root, 0) + 1
  
  return list(sizes.values())          # # return list of size dictionary values -> [4, 2]

  
# -- Union method --
def union(roots, node_a, node_b): #(3,2)
  root_a = find(roots, node_a) # find root of 3
  root_b = find(roots, node_b) # find root of 2
  roots[root_b] = root_a       # 2 points 3


# -- Finds root for given node --
def find(roots, node):
  if roots[node] == node: # if index and value is same; means points itself; return as root
    return node

  return find(roots, roots[node]) # if not root then go look value stored at index root[node] in roots array 
                          # and find root on that recursively

# Time: O(n) -> iterate over all elements of edges
# Space: O(n) -> array to store all edges values



# ------ Q-26: extra cable [ UNION-FIND; FIND EDGE(pair) CAUSING DISCONNECTED COMPONENTS ] ------
# You are given a network of computers connected by cables. 
# A cable connects two computers and can transmit data in both directions.

# A fully-connected network is a network where all computers can communicate with each other by transmitting data through cables. 
  
# For example:
# 1. the following network is fully-connected:
#     3
#     |
# 0---1---2---4


# 2. the following network is not fully-connected:
#     3
#     |
# 0---1     2---4

# Example 2 is not fully-connected because computers 2 and 0 cannot communicate.
# There are other such pairs of computers that cannot communicate like 4 and 1, etc..

# You are given a computer network that started out as fully-connected and minimal,
#  but someone added exactly one extra cable. 
# Your job is to find a cable that can be safely removed, ensuring network is fully-connected and minimal.

# Write a function that takes in number num_computers and a list of cables that connect the computers. 
# Computers have ids from 0 to num_computers - 1. 
# The function should return a cable that can be safely removed. 
# There will be multiple possible cables that can be chosen; you may return any of them.


# SOLUTION:
# Need to find cable that can be removed to make components connected
# Use UNION-FIND 
# when roots of both node is same, that means dis-connected there
# return false if roots of 2 nodes are same
# and return the cable pair having (node_a, node_b)

def extra_cable(num_computers, cables):
  roots = [ i for i in range(0, num_computers) ]  # init: every node is its own root

  for cable in cables:
    computer_a, computer_b = cable
    if union(roots, computer_a, computer_b) == False:  # already connected -> cycle
      return cable                                     # ...so this cable is safe to remove


# -- Union method --
def union(roots, node_a, node_b): #(3,2)
  root_a = find(roots, node_a) # find root of 3
  root_b = find(roots, node_b) # find root of 2

  if root_a == root_b: # if both roots are same, no need to union
    return False
  
  roots[root_b] = root_a       # 2 points 3
  return True



# -- Finds root for given node --
def find(roots, node):
  if roots[node] == node: # if index and value is same; means points itself; return as root
    return node

  return find(roots, roots[node]) # if not root then go look value stored at index root[node] in roots array 
                          # and find root on that recursively

# Time: O(n) -> iterate over all elements of edges
# Space: O(n) -> array to store all edges values





















# ------------ Q-27: All Trips ----------------

# routes = [
#   ('brookdale', 'denton junction'),
#   ('astor place', 'brookdale'),
#   ('astor place', 'cony island'),
#   ('astor place', 'denton junction'),
#   ('cony island', 'denton junction')
# ]
# all_trips(routes, 'astor place', 'denton junction') # ->
# [
#   ['astor place', 'brookdale', 'denton junction'],
#   ['astor place', 'cony island', 'denton junction'],
#   ['astor place', 'denton junction']
# ]

# You are given a list of bus routes, a starting station, and an ending station. 
# returns a list containing all possible trips we can make that travel from the starting station to the ending station. 

# start: A
# end:   D
#
#                              (F)
#                            /
#         [ A B D ]        /
#         [ A C D ]      /
#         [ A D ]      /
#              \     /
#               (A) ---------> (B)
#              /  |  \           \   [ B D ]
#             /   |   \           \
#            /    |    \           v
#          (C) <--     ----------> (D)   [ D ]
#           |  [ C D ]            ^
#           |                    /
#            \__________________/
#
# Edges:
#   A -> F
#   A -> B
#   A -> C
#   A -> D
#   B -> D
#   C -> D
#
# All paths collected at each node (to reach target D):
#   D = [ [D] ]                          (target itself)
#   B = [ [B D] ]                        (B -> D)
#   C = [ [C D] ]                        (C -> D)
#   F = [ ]                              (no path from F to D)
#   A = [ [A B D], [A C D], [A D] ]      (overall answer from source A)

# convert edge list to adjecency list
# now use Graph possible path problem to find paths from A to D

# n = number of nodes
# Time O((2 ^ n) * n); for every node we split into 2 include path or exclude path and n nodes each
# Space O((2 ^ n) * n); need to store all the path information


def all_trips(routes, start_station, end_station):
  graph = build_graph(routes)
  all_paths = get_paths(graph, start_station, end_station)
  return [path[::-1] for path in all_paths] # reverse the all paths array

# -- get paths A to D --
def get_paths(graph, src, dst):
  if src == dst:
    return [ [src] ]

  all_paths = []
  for neighbor in graph[src]:
    neighbor_paths = get_paths(graph, neighbor, dst)
    for path in neighbor_paths:
      path.append(src) # add current src to neighbors and return by adding in all_paths
      all_paths.append(path)
  return all_paths
# --
  

# -- build graph --
def build_graph(edges):
  graph = {}
  for edge in edges:
    a,b = edge

    if a not in graph:
      graph[a] = []

    if b not in graph:
      graph[b] = []

    graph[a].append(b)

  return graph
# --

# n = number of nodes
# Time O((2 ^ n) * n); for every node we split into 2 include path or exclude path and n nodes each
# Space O((2 ^ n) * n); need to store all the path information 




# ------------ Q-28: virus spread ------------
# n the grid, 0's are empty spaces, 1's are clean computers, and 2's are infected computers. 
# Every hour, the virus spreads from infected computers to immediately adjacent clean computers.
# The virus can only spread to adjacent computers that are up, down, left, or right.
#  If it is impossible for all computers to become infected, then return -1.

# grid = [
#   [1,1,1],
#   [0,1,0],
#   [0,1,2]
# ]
# virus_spread(grid) # -> 4

# BFS using queue and visited
# Iterate through grid 
    # get count of clean computers 
    # add infected computer in queue and mark infected as visited
# Now run BFS, 
   # take infected computers as 0
   # and make adjecent healthy ones as +1 means infected, and reduce clean computer count
   # for every level of BFS add +1 and infect adjecent and reduce clean computer count until 0
   # finally queue will be empty, then returm max level it vel to make clean computer as 0
   # after queue empty, if clean computer remains, return -1, impossible to infect all computers

# r = number of rows
# c = number of colums
# O(r * c) iterating through grid in 2 nested loops
# O(r * c) doing BFS using queue
# Time: O(rc + rc) = O(rc)
# Space: O(rc) using queue and visited set to store every positions

from collections import deque

def virus_spread(grid):
  queue = deque([])               # BFS using queue and visited
  visited = set()
  
  num_clean_computers = 0
  
  for r in range(0, len(grid)):   # Iterate through grid 
    for c in range(0, len(grid[0])):
      if grid[r][c] == 1:
        num_clean_computers += 1  # get count of clean computers 
      elif grid[r][c] == 2:
        queue.append((r,c,0))     # add infected computer in queue and mark infected as visited
        visited.add((r,c))

  max_t = 0
  deltas = [(0,1), (0,-1), (1,0), (-1,0)]
  
  while queue:                    # Now run BFS, 
    r,c,t = queue.popleft()
    max_t = t
    
    for delta in deltas:
      delta_row, delta_col = delta
      new_row = r + delta_row
      new_col = c + delta_col
      new_pos = (new_row, new_col)
      row_inbounds = 0 <= new_row < len(grid)
      col_inbounds = 0 <= new_col < len(grid[0])

      # and make adjecent healthy ones as +1 means infected, and reduce clean computer count
      if row_inbounds and col_inbounds and new_pos not in visited and grid[new_row][new_col] == 1:
        num_clean_computers -= 1 
        queue.append((new_row, new_col, t + 1))
        visited.add(new_pos)

        
  # after queue empty, if clean computer remains, return -1, impossible to infect all computers
  if num_clean_computers > 0:
    return -1
  else:
    return max_t
    
# r = number of rows
# c = number of colums
# O(r * c) iterating through grid in 2 nested loops
# O(r * c) doing BFS using queue
# Time: O(rc + rc) = O(rc)
# Space: O(rc) using queue and visited set to store every positions

