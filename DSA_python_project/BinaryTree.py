# ==================== CHAPTER 9 - BINARY TREE ====================
# BinaryTree.py - 31 questions

# =============== BINARY TREE - 1 ===================



# Binary Tree - 
# A tree where every node has atmost 2 children
# Exactly 1 root
# Exactly one path between root and any node

# Note:  Tree with 0 nodes, empty tree is also a binary tree

# ---------------- Q-1: Binary Tree -----------------------
# Good tree for interview with different cases covered
# We first go deeper in the tree and then we go across the tree
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a. right = c
b.left = d
b.right = e
c.right = f

#   a
#  / \  
#  b   c
# / \  \
# d  e  f

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# -------------- Q-2: Depth First Search ------------
#   a
#  / \  
#  b   c
# / \  \
# d  e  f

# depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']

# We use stack for DFS , push and remove from Top
# We add, push right first and then left
# Trace values when it leaves the stack
# Time O(n) we are iterating all nodes of tree
# Space O(n) we are storing nodes on stack
def depth_first_values(root):
  if root is None:
    return []

  values = []
  stack = [ root ]
  
  while stack:
    current = stack.pop()
    values.append(current.val)

    if current.right is not None:
      stack.append(current.right)

    if current.left is not None:
      stack.append(current.left)

  return values
# O(n), O(n)

# - Using Recursion -
def depth_first_values(root):
  if root is None:
    return []

  left_values = depth_first_values(root.left) # [b, d, e]
  right_values = depth_first_values(root.right) # [c, f]
  # return [root.val, *left_values, *right_values]
  return [root.val] + left_values + right_values # [a, b, d, e, c, f]
# O(n), O(n) 
    
 
# -------------- Q-3: Breadth First Search ------------

#   a
#  / \  
#  b   c
# / \  \
# d  e  f

# breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

# We use Queue for BFS , push at back and remove from front
# We push at back left first and then right
# Trace values when it leaves the queue
# Time O(n) we are iterating all nodes of tree
# Space O(n) we are storing nodes on queue
def breadth_first_values(root):
  if root is None:
    return []

  values = []
  queue = [ root ]

  while queue:
    current = queue.pop(0)
    values.append(current.val)

    if current.left is not None:
      queue.append(current.left)

    if current.right is not None:
      queue.append(current.right)

  return values #-> ['a', 'b', 'c', 'd', 'e', 'f']
# Time O(n), Space O(n)   


# Queue Append O(1), but Queue Pop is O(n)
# so to make queue append O(1) and pop O(1), we can use deque
# Changes from queue to deque
from collections import deque
queue = deque([root])
current = queue.popleft()


# - Using Recursion -
# No recursion for BFS as we use queue
# recursion will use stack, counter of queue
  
# -------------- Q-4: Tree Sum ------------
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
#tree_sum(a) # -> 21
# Can use any BFS and DFS iteration and add sum

# Using DFS recursion - recursion call stack
# Time O(n) we are iterating all nodes of tree
# Space O(n) we are storing nodes on queue
def tree_sum(root):
  if root is None: # base case
    return 0

  treesum_left = tree_sum(root.left) # recursion case left tree
  treesum_right = tree_sum(root.right) # recursion case right tree
  return root.val + treesum_left + treesum_right
  # return root.val + tree_sum(root.left) + tree_sum(root.right)
# Time O(n), Space O(n)  

# -------------- Q-5: Tree Includes ------------
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# tree_includes(a, "e") # -> True

# Can use any BFS and DFS iteration, we choose BFS Iteration using deque
# at the time of exiting queue we are checking value is equal to target


from collections import deque

def tree_includes(root, target):
  if root is None:
    return False
    
  queue = deque([root])
  while queue:
    current = queue.popleft()
    
    if current.val == target:
      return True

    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)

  return False
# Time O(n), Space O(n)      

# - Using recursion -
# DFS , there is no recursion in queue based BFS
def tree_includes(root, target):
  if root is None:
    return False

  if root.val == target:
    return True
  
  left_tree = tree_includes(root.left, target)
  right_tree = tree_includes(root.right, target)
  return left_tree or right_tree
# Time O(n), Space O(n)   


# -------------- Q-6: Tree Min Value ------------

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
# tree_min_value(a) # -> -2    

# -- Using recursion DFS --
# here base case is infinity if node is None
def tree_min_value(root):
  if root is None: # base case
    return float('inf')

  min_left_tree = tree_min_value(root.left) # recursion case left
  min_right_tree = tree_min_value(root.right) # recursion case right
  return min(root.val, min_left_tree, min_right_tree)
# Time O(n), Space O(n)  

# - Using queue based BFS -
# Taking None node as infinity as want min value
# if any node value while coming out of queue is less then that is new min value
from collections import deque

def tree_min_value(root):
  if root is None:
    return float('inf')

  min_value = float('inf')
  queue = deque([root])
  while queue:
    current = queue.popleft()
    
    if current.val < min_value:
      min_value = current.val

    if current.left is not None:
      queue.append(current.left)
    if current.right is not None:
      queue.append(current.right)

  return min_value
# Time O(n), Space O(n) 

# -------------- Q-7: Max root to leaf path sum ------------
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

# max_path_sum(a) # -> 18

# - Using recursion DFS -
# Taking None node as -infinity as want max value
# if leaf node return node value
# recurse for left and right subtree
# at any node we will take max(leftpart, rightpart) + the node's value
def max_path_sum(root):
  if root is None: # base case
    return float('-inf')

  if root.left is None and root.right is None: # leaf node
    return root.val
  
  left_tree_max = max_path_sum(root.left) # recursion case left
  right_tree_max = max_path_sum(root.right) # recursion case right
  return root.val + max(left_tree_max, right_tree_max)
# Time O(n), Space O(n) 


# -------------- Q-8: tree path finder  ------------
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]

# - Using recursion DFS -
# Taking None node to return None
# if node matches target return result array of that node
# if left path is not None, result array with value add in left path
# if right path is not None, result array with value add in right path
# this will give result array in reverse order node -> head


# in calling function
# if result is None, return None
# if result has array values, reverse it head -> node path (::-1)

def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1] # reversing list [::-1] to get head -> node path

# This method will return list in reverse order, node -> head
def _path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [root.val]

  left_path = _path_finder(root.left, target)
  if left_path is not None:
    # return [ root.val , *left_path] # this will take time, better use append
    left_path.append(root.val)
    return left_path
    
  right_path = _path_finder(root.right, target)
  if right_path is not None:
    # return [ root.val, *right_path] # this will take time, better use append
    right_path.append(root.val)
    return right_path

  return None
  
# Time O(n), Space O(n) 
# Time O(n) + O(n) = O(n); O(n) for finding target node and O(n) for reversing list


# -------------- Q-9: How many nodes match given value ------------

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

# tree_value_count(a,  6) # -> 3

# - using BFS queue based iteration -
# we will check value at the time of exiting queue
# if value matches target then add 1 to count and return count at the end

# - Using recursion DFS -
# we have 2 base case if Node is None return 0
# If node matches the target then add 1 + left_tree_count + right_tree_count
# if not then add 0 + left_tree_count + right_tree_count
def tree_value_count(root, target):
  if root is None:
    return 0

  match = 1 if root.val == target else 0
  
  left_tree_count = tree_value_count(root.left, target)
  right_tree_count = tree_value_count(root.right, target)
  return match + left_tree_count + right_tree_count
# Time O(n), Space O(n) 

# -------------- Q-10: Height of Binary Tree ------------

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# how_high(a) # -> 2

# - Using recursion DFS -
# we will take base case node null as -1
# at each level we will add 1 + maximum of left tree and right tree
def how_high(root):
  if root is None:
    return -1

  left_tree_height = how_high(root.left)
  right_tree_height = how_high(root.right)
  return 1 + max(left_tree_height , right_tree_height)
# Time O(n), Space O(n) 


# -------------- Q-11: Bottom right value ------------
#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1

# bottom_right_value(a) # -> 1
# - Using queue based BFS -
# we keep adding in queue while doing BFS
# we keep removing element on trace
# The last element exiting queue will be bottom right value

from collections import deque

def bottom_right_value(root):
  queue = deque([root])

  current = 0
  while queue:
    current = queue.popleft()

    if current.left is not None:
      queue.append(current.left)

    if current.right is not None:
      queue.append(current.right)

  return current.val

# Time O(n), Space O(n) for using queue

# - NO DFS RECURSION APPROACH -
# def bottom_right_value(root):
#   if root is None:
#     return

#   bottom_right_value(root.left)  
#   bottom_right_value(root.right)


# -------------- Q-12: All Tree paths ------------
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# all_tree_paths(a) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 

# - DFS Recursion -
# helper function
# we will have 2 base cases
# if node is None; return [] array
# if node is leaf; return [[leaf]]
# at each node, add current node to left and right subtree array 
# add both left and right subtree path in final array

# main function
# returns all paths reversed, as we want new node to be at start of list
def all_tree_paths(root):
  final_array = _all_tree_paths(root)
  for path in final_array:
    path.reverse()
  return final_array

def _all_tree_paths(root):
  final_array = []
  
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]

  left_tree_array = _all_tree_paths(root.left)
  for path in left_tree_array:
    path.append(root.val)
    final_array.append(path)
    
  right_tree_array = _all_tree_paths(root.right)
  for path in right_tree_array:
    path.append(root.val)
    final_array.append(path)

  return final_array
    

# time and space complexity will be - leaves * height
# Nodes - n
# height - log(n)
# leaves - n/2
# Time complexity = leaves * height = O(n/2 * log(n)) = O(n*log(n))
# same space complexity = O(n*log(n)), need to store arrays


# -------------- Q-13: All levels of tree ------------
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]

# we will put element along with level on Stack
# we will pop from stack and add to final array list at index of level
# we will add this array list to final array
# when we push left and right child of node, 
# we will add node on stack with level + 1
# and create new array in final list at index level + 1

# - Stack based DFS -
def tree_levels(root):
  if root is None:
    return []

  final_array = []
  stack = [ (root, 0) ]
  
  while stack:
    current, level = stack.pop()

    if len(final_array) == level:
      final_array.append([current.val])
    else:
      final_array[level].append(current.val)

    if current.right is not None:
      stack.append((current.right, level + 1))

    if current.left is not None:
      stack.append((current.left, level + 1))

  return final_array

# Time O(n), Space O(n) for using final array to store all elements

# - Queue based BFS -
from collections import deque

def tree_levels(root):
  if root is None:
    return []

  final_array = []
  queue = deque([ (root, 0) ])
  
  while queue:
    current, level = queue.popleft()

    if len(final_array) == level:
      final_array.append([current.val])
    else:
      final_array[level].append(current.val)

    if current.left is not None:
      queue.append((current.left, level + 1))

    if current.right is not None:
      queue.append((current.right, level + 1))

  return final_array

# Time O(n), Space O(n) for using final array to store all elements

# - Recursion based DFS -
def tree_levels(root):
  final_array = []
  _tree_levels(root, final_array, 0)
  return final_array


def _tree_levels(root, final_array, level):
  if root is None:
    return

  if len(final_array) == level:
    final_array.append([root.val])
  else:
    final_array[level].append(root.val)
  
  _tree_levels(root.left, final_array, level + 1)
  _tree_levels(root.right, final_array, level + 1)

# Time O(n), Space O(n) for using final array to store all elements

# -------------- Q-14: Average value at each level ------------
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

# level_averages(a) # -> [ 3, 7.5, 1 ] 

# Use above -- All levels of tree  -- to get final array with levels
# then we will iterate final array and get average of each level and return array of averages

# use from statistics import mean -- to get mean method

from statistics import mean

def level_averages(root):
  final_array = []
  _tree_levels(root, final_array, 0)

  level_averages = []
  for tree_levels in final_array:
    level_averages.append(mean(tree_levels))
  return level_averages

# _tree_levels - same as above to get tree levels
# Time O(n), Space O(n) for using final array to store all elements and average array 


# -------------- Q-15: Leaf list ------------
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# leaf_list(a) # -> [ 'd', 'e', 'f' ] 

# - Queue based BFS - will not work because not all leaves are at last level -

# - Stack based DFS -
def leaf_list(root):
  if root is None:
    return []

  values = []
  stack = [ root ]
  while stack:
    current = stack.pop()
    
    if current.left is None and current.right is None:
      values.append(current.val)

    if current.right is not None: # right part goes first in stack approach
      stack.append(current.right)
      
    if current.left is not None: # then left
      stack.append(current.left)
      
  return values
# Time O(n), Space O(n) for leaf values array

# - Recursion DFS -
def leaf_list(root):
  values = []
  _leaf_list(root, values)
  return values

def _leaf_list(root, leaf_list):
  if root is None:
    return []

  if root.left is None and root.right is None:
      leaf_list.append(root.val)

  _leaf_list(root.left, leaf_list)
  _leaf_list(root.right, leaf_list)
# Time O(n), Space O(n) for leaf values array






















# =============== BINARY TREE - 2 ===================

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

# NOTE:
# (1)
# Preorder - [self, left, right]
# Inorder - [left, self, right]
# Postorder - [left, right, self]

# (2)
# Height -> distance of the root to the farthest leaf.
# Depth -> distance of the root to the node.

# (3)
# balanced tree -> height of left and right subtree of every node differ at most by 1

# Worst case height of tree -> n; when tree is skewed like linked list
# Best case height of balanced tree -> log(n); when tree is balanced

#   Best-Case (balanced)             Worst-Case (skewed / linked-list like)
#   height ~ log(n)                  height ~ n
#
#   Best-Case (6 nodes)              Worst-Case (6 nodes)
#                                       O
#          O                            \
#         / \                            O
#        O   O      height 2              \
#       / \   \                            O          height 5
#      O   O   O                            \
#                                            O
#                                             \
#                                              O
#                                               \
#                                                O

# Balanced tree -> height ~ log(n)  => DFS recursion uses log(n) stack space
# Skewed tree   -> height ~ n       => DFS recursion uses n stack space




# ---------- Q-16: lowest common ancestor LCA --------------
# return the value of the lowest common ancestor of the two values in the tree.

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

# lowest_common_ancestor(a, 'd', 'h') # b
# lowest_common_ancestor(a, 'b', 'h') # b

# Ancestor - all nodes from root to that nodes
# Decendent - all nodes below give node till leaf

# Lowest common ancestor of 2 nodes
# find common ancestors of node1
# find common ancestors of node2
# the lowest where both path meets, LCA

# Path G : [G, E, B, A]
# Path D : [D, B, A]
# LCA -> first one matching -> B

# n = number of nodes
# Time complexity: O(n) + O(n) = O(n); DFS for both node and finding common in both array
# Space complexity: O(n); storing paths on array


def lowest_common_ancestor(root, val1, val2):
  path1 = get_path(root, val1)
  path2 = get_path(root, val2)

  set2 = set(path2)

  for val in path1:
    if val in set2:
      return val
# O(n), O(n)



# -- get root to target value path --
# This method returns path in reverse array (from target to root) 
# Path G : [G, E, B, A]
def get_path(root, target_val): 
  if root is None:
    return None

  if root.val == target_val:
    return [ root.val ]


  left_path = get_path(root.left, target_val)
  if left_path is not None:
    left_path.append(root.val)
    return left_path

  right_path = get_path(root.right, target_val)
  if right_path is not None:
    right_path.append(root.val)
    return right_path

  return None
# Time O(n); DFS on tree
# Space O(n); storing values in array



# --------- Q-17: Flip Tree ---------

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

# flip_tree(a) 

#       a
#    /    \
#   c      b
#  /     /   \
# f     e    d
#     /  \
#    h    g


# need to flip every left and right pointer
# recusion using DFS 
# return root of Tree

# Time O(n); DFS on tree
# Space O(n); stack space to perform DFS recusion


def flip_tree(root):
  if root is None:
    return None

  left = flip_tree(root.left)
  right = flip_tree(root.right)

  root.left = right
  root.right = left

  return root
# O(n), O(n)


# ---------- Q-18: Left Nodes -----------

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

# lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]

# we will do DFS (left to right) and place 1st element of every level in array
# every index on array will hold 1st left element on that level
# if we already have item at index ignore, move and 
# when new level encountered place that element in array index

# Depth-first, left-to-right
#
#         0:  A
#            / \
#         1: B   C  :1
#          /  \    \
#       2: D   E    F :2
#            /  \
#         3: G   H :3
#           /
#        4: I       <-- left-most node at each level
#
#            0  1  2  3  4
#          [ A, B, D, G, I ]
#
# The left-most node at every level (0..4) -> [A, B, D, G, I]

# Time O(n); DFS on tree
# Space O(n); stack space to perform DFS recusion


def lefty_nodes(root):
  values = []
  traverse(root, 0, values)
  return values

# --- left to right; DFS --------
def traverse(root, level, values):
  if root is None:
    return 

  # if there is no value stored at index level in array, add value
  if len(values) == level:
    values.append(root.val)

  traverse(root.left, level + 1, values)
  traverse(root.right, level + 1, values)

# O(n), O(n)





















# ------- Q-19: BST binary search tree includes ------------
#  return a boolean indicating whether or not the target is found within the tree.

# A Binary Search Tree is a binary tree where 
# all values within a node's left subtree are smaller than the node's value 
# and all values in a node's right subtree are greater than or equal to the node's value.

#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19

# binary_search_tree_includes(a, 9) # -> True
# binary_search_tree_includes(a, 15) # -> False
# binary_search_tree_includes(a, 1) # -> False

# BST has smaller element in left, larger in right
# we dont have to traverse whole tree
# if our target is less than node, go left, else go right
# if target found return true, else False

# n = number of nodes
# height of tree -> log(n)
# Time complexity : log(n); we will traverse downward till height
# space complexity : log(n); recursion call stack on height of BST


# -- Tree Height: Best-Case vs Worst-Case Complexity --
#
#   n = # nodes
#
#   Best-Case (balanced)        Worst-Case (skewed / linked-list like)
#   Time:  log(n)               Time:  n
#   Space: log(n)               Space: n
#
#
#   Best-Case (6 nodes)              Worst-Case (6 nodes)
#                                       O
#          O                            \
#         / \                            O
#        O   O      height 2              \
#       / \   \                            O          height 5
#      O   O   O                            \
#                                            O
#                                             \
#                                              O
#                                               \
#                                                O
#
# Balanced tree -> height ~ log(n)  => DFS recursion uses log(n) stack space
# Skewed tree   -> height ~ n       => DFS recursion uses n stack space

# -- recursion using DFS but split left if target < root.val; else right --- 
def binary_search_tree_includes(root, target):
  if root is None:
    return False

  if root.val == target:
    return True

  if target < root.val:
    return binary_search_tree_includes(root.left, target)
  else:
    return binary_search_tree_includes(root.right, target)
    
# Best Case -> log(n); log(n)
# Worst Case ->  n    ;  n



# ---------- Q-20: is binary search tree --------------
# return a boolean indicating whether or not the tree satisfies the binary search tree property.

#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19

# is_binary_search_tree(a) # -> True

# all values in left subtree is less than value, right subtree greater
# inorder traversal [left, self, right] and add values to array
# values of array should be in increasing order -> BST
# take 2 pointer, i and j = i+1
# value of j should always be greater than i, increasing order, return true; else false

# Time complexity: O(n) + O(n = O(n); traverse and sort array
# Space complexity: O(n) + O(n = O(n); recursion stack and store array


def is_binary_search_tree(root):
  values = []
  in_order_traversal(root, values)
  return is_sorted(values)
# O(n), O(n)

# -- inorder traversal [left, self, right] --
def in_order_traversal(root, values):
  if root is None:
    return

  in_order_traversal(root.left, values)
  values.append(root.val)
  in_order_traversal(root.right, values)
# --

# -- Is sorted --
def is_sorted(numbers):
  for i in range(0, len(numbers) - 1):
    current = numbers[i]
    next = numbers[i + 1]

    if current > next: # increasing order, next should be greater than current
      return False

  return True
# --



# -------- Q-21: Post Order Traversal [left, right, self] --------

#       a
#    /    \
#   b      c

# pre_order(x)
# # ['a', 'b', 'c']

# in_order(x)
# # ['b', 'a', 'c']

# post_order(x)
# # ['b', 'c', 'a']


# n = number of nodes
# Time complexity = O(n); traversing entire nodes of tree
# Space complexity = O(n); using recursion call stack

# --- post order [left, right, self] ---
def post_order(root):
  values = []
  post_order_traversal(root, values)
  return values
# O(n), O(n)

# --- post order [left, right, self] ---
def post_order_traversal(root, values):
  if root is None:
    return

  post_order_traversal(root.left, values)
  post_order_traversal(root.right, values)

  values.append(root.val)
# -- 
  


# ----- Q-22: Build tree inorder Postorder ------
# The function should build a binary tree 
# that has the given in-order and post-order traversal structure. 
# The function should return the root of this tree.

# build_tree_in_post(
#   [ 'd', 'b', 'e', 'a', 'f', 'c', 'g' ],
#   [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
# )
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g

# last element in postorder will be current root
# find that element in inorder, left to element will go leftsubtree, right to element in rightsubtree
# left post order = post_order[: len(left_in_order)] -> 0 till len(left_in_order) from post_order
# right post order = post_order[len(left_in_order) : -1] 
# -> after left post order till n-1; as last in postorder is current root
# repeat the same logic for all subtree
# will stop as base case empty array, None node, return None

# n = length of array
# Time complexity: O(n^2); n for recursive call * n for copies of array
# Space complexity: O(n^2); n for recursive call * n for copies of array

# -- Tree Node --
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
# --

def build_tree_in_post(in_order, post_order):
  if len(in_order) == 0:
    return None

  # last element in postorder will be current root
  val = post_order[-1]
  root = Node(val)

  # find that element in inorder, left to element will go leftsubtree, right in rightsubtree
  mid = in_order.index(val)
  left_in_order = in_order[:mid] #0 -> mid-1 as mid is covered above
  right_in_order = in_order[mid + 1:] #mid+1 -> n as mid is covered above

  left_size = len(left_in_order)
  left_post_order = post_order[: left_size] # left postorder -> 0 till left_size from post_order
  right_post_order = post_order[left_size : -1]  # right postorder -> left_size till -1 from post_order;
                                                  # as last (n) in postorder is current root

  root.left = build_tree_in_post(left_in_order, left_post_order) # repeat logic for leftsubtree
  root.right = build_tree_in_post(right_in_order, right_post_order) # repeat logic for rightsubtree
                     
  return root

# O(n^2); O(n^2)



# ----- Q-23: Build tree inorder Preorder ------
# The function should build a binary tree 
# that has the given in-order and pre-order traversal structure. 
# The function should return the root of this tree.

# build_tree_in_pre(
#   [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
#   [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
# )
#       a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

# FIRST element in preorder will be current root
# find that element in inorder, left to element will go leftsubtree, right to element in rightsubtree
# left_size = len(left_in_order)
# left pre order = pre_order[1: 1 + left_size] ; 1 -> 1 + leftsize; as first element in preorder is root
# right pre order = pre_order[1 + left_size :]; 1 + leftsize -> end in preorder
# repeat the same logic for all subtree
# will stop as base case empty array, None node, return None

# n = length of array
# Time complexity: O(n^2); n for recursive call * n for copies of array
# Space complexity: O(n^2); n for recursive call * n for copies of array

def build_tree_in_pre(in_order, pre_order):
  if len(in_order) == 0:
    return None

  # FIRST element in preorder will be current root
  val = pre_order[0]
  root = Node(val)

  # find that element in inorder, left to element will go leftsubtree, right in rightsubtree
  mid = in_order.index(val)
  left_in_order = in_order[:mid] #0 -> mid-1 as mid is covered above
  right_in_order = in_order[mid + 1:] #mid+1 -> n as mid is covered above

  left_size = len(left_in_order)
  left_pre_order = pre_order[1 : 1 + left_size] # 1 -> 1 + leftsize; as first element in preorder is rootfrom pre_order
  right_pre_order = pre_order[1 + left_size :] # 1 + leftsize -> end; in preorder

  root.left = build_tree_in_pre(left_in_order, left_pre_order) # repeat logic for leftsubtree
  root.right = build_tree_in_pre(right_in_order, right_pre_order) # repeat logic for rightsubtree
                     
  return root

# O(n^2); O(n^2)


# ------------ Q-24: BALANCED BINARY TREE --------------

# height -> distance of the root to the farthest leaf.
# balanced tree -> height of left and right subtree of every node differ at most by 1

# As in BST includes Question, balanced tree is the best case

#   Best-Case (6 nodes)              Worst-Case (6 nodes)
#                                       O
#          O                            \
#         / \                            O
#        O   O      height 2              \
#       / \   \                            O          height 5
#      O   O   O                            \
#                                            O
#                                             \
#                                              O
#                                               \
#                                                O

# Balanced tree -> height ~ log(n)  => DFS recursion uses log(n) stack space

# height -> distance of the root to the farthest leaf.
# balanced tree -> height of left and right subtree of every node differ at most by 1


# ------ Is tree balanced --------

# height of None node is 0
# for every node, we take max(height_left, height_right) and add 1
# and for tree to be balanced 1 + max(height_left, height_right) should not be more than 1
# if it is more than 1 (atmost 1 condition) return -1 (-1 represents unbalanced)
# if any node is unbalanced -1, then whole tree is unbalanced

# Time complexity: O(n) traversing whole tree
# Space complexity: O(n) recursion stack


def is_tree_balanced(root):
  return check_height_balance(root) != -1  # atmost 1 height difference; (-1 represents unbalanced)
#--

# -- return -1 if tree is not balanced 
def check_height_balance(root):
  if root is None:
      return 0

  left_height = check_height_balance(root.left)
  if left_height == -1:
    return -1  # (-1 represents unbalanced)

  height_right = check_height_balance(root.right)
  if height_right == -1:
    return -1  # (-1 represents unbalanced)

  if abs(left_height - height_right) > 1:
    return -1  # (-1 represents unbalanced)
  else:
    return 1 + max(left_height, height_right) 
# O(n) traversing whole tree
# O(n) recursion stack




# --------- Q-25: leaf layers of tree ---------
# To get a leaf layer, take all leaf nodes in tree. 
# Then, conceptually "remove" them from the tree. 
# This will create new "leaves". 
# Repeat this process until the tree is empty.

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b;
# a.right = c;
# b.left = d;
# b.right = e;
# c.right = f;

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# leaf_layers(a) # ->
# [
#   ['d', 'e', 'f'],
#   ['b', 'c'],
#   ['a']
# ]


# Find height of each node: distance from farthest leaf
# Base case: for null node, height = -1
# height = 1 + max(height left subtree, height right subtree)
# return array where each subarray represents nodes at a particular height

# Time: O(n); counting height of binary tree
# Space: O(n); adding to array


def leaf_layers(root):
  layers = []
  traverse(root, layers)
  return layers
  

# find height of node and add to array
def traverse(root, layers):
  if root is None:
    return -1

  left_height = traverse(root.left, layers)
  right_height = traverse(root.right, layers)
  
  height = 1 + max(left_height, right_height)

  if len(layers) == height: # if new height level, add empty subarray
    layers.append([])
  # else:                    # height subarray exist, add current root.val to subarray
  layers[height].append(root.val)
  
  return height # we will return height, only add to array during traversal
  
# O(n); O(n)



# --------- Q-26: Has path sum ---------
# return a boolean indicating whether or not there is a path through the tree that sums to the target.
# A path must begin at the root and end at a leaf.

# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

# has_path_sum(a, 8) # -> True


# root to leaf path sum == target
# subtract target - node and check for new target in left and right subtree
# if leaf == target; return true
# if node == null return false

# Time: O(n); traversing through tree
# Space: O(n); recursion call stack

def has_path_sum(root, target):
  if root is None: # null node return false
    return False

  if root.left is None and root.right is None and root.val == target:
    return True # leaf node and value == target; return True

  # subtract target - node and check for new target in left and right subtree
  return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)

# O(n); O(n)


# -------------- Q-27: Flatten Binary tree to Linked-List -----------
# function should return the root/head of the list.
# For example, this tree:
 
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# flatten_tree(a) # ->
#      a
#       \
#        b
#         \
#          d
#           \
#            e
#            \
#             c
#              \
#               f

# Stack based DFS - Preorder traversal
# here after poping current from stack 
# we are going to store current as previous, and make previous.right = current
# after putting current on stack disconnect current left and right

# Time: O(n); traversing through tree
# Space: O(n); store on stack

def flatten_tree(root):
  stack = [root]
  prev = None

  while stack:
    current = stack.pop()

    if prev: # make previous.right = current
      prev.right = current

    prev = current # store current as previous

    if current.right is not None: # Right first in Stack DFS, then left
      stack.append(current.right)
    
    if current.left is not None:
      stack.append(current.left)

    current.left = None # after putting current on stack disconnect current left and right
    current.right = None
      
  return root
      
# O(n); O(n)


# -------------- Q-28: Serialize and Deserialize Binary tree ------------
# Turn a tree into a string, then rebuild the exact same tree back from that string.

#   a
#  / \
#  b   c
# / \  \
# d  e  f

# serialize(a) # -> "a,b,d,#,#,e,#,#,c,#,f,#,#"
# deserialize("a,b,d,#,#,e,#,#,c,#,f,#,#") # -> rebuilds the tree, returns root 'a'
# serialize(None) # -> "#"

# a plain preorder list is NOT enough to rebuild a tree, which is exactly why
# build_tree_in_pre above also needed the inorder list to know where to split

# the fix: write a marker '#' for every None child
# with those markers, preorder ALONE is enough, because the Nones tell us
# precisely where each subtree ends, so the shape is fully encoded

# serialize   = preorder DFS, append the value, or '#' when the node is None
# deserialize = read the tokens left to right in that SAME preorder order
#   pull one token: '#' -> return None
#   otherwise make the node, then build its left, then build its right

# using an iterator matters, next() consumes a token and never rewinds,
# so each recursive call automatically picks up where the last one stopped

# Time: O(n); every node is written once and read once
# Space: O(n); the string plus the recursion stack

def serialize(root): # serialize(a) # -> "a,b,d,#,#,e,#,#,c,#,f,#,#"
  values = []
  _serialize(root, values)
  return ','.join(values)

# -- preorder DFS; write the value, or '#' when the node is missing --
def _serialize(root, values):
  if root is None:
    values.append('#') # marker for a missing child
    return

  values.append(str(root.val))
  _serialize(root.left, values)  # preorder: self, then left, then right
  _serialize(root.right, values)
# --

# O(n); O(n)


def deserialize(data): # deserialize("a,b,d,#,#,e,#,#,c,#,f,#,#") # -> rebuilds the tree, returns root 'a'
  values = iter(data.split(',')) # iterator, so next() pulls one token at a time
  return _deserialize(values)

# -- read the tokens in the SAME preorder order that serialize wrote them --
def _deserialize(values):
  value = next(values)
  if value == '#': # marker -> there is no node here
    return None

  root = Node(value)
  root.left = _deserialize(values)  # same preorder order as serialize: self, left, right
  root.right = _deserialize(values)
  return root
# --

# O(n); O(n)


