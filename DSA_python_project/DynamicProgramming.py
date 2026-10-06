# ==================== CHAPTER 11 - DYNAMIC PROGRAMMING ====================
# DynamicProgramming.py - 23 questions

# Dynamic Programming using Memoization

# Memoization
# - using recursion
# - uses brute force as base

# Tabulation
# - using iteration
# - No base implementation

# Both Memoization and Tabulation - SAME TIME AND SPACE COMPLEXITY

# ALvin's approach - USING MEMOIZATION
# use recursion to solve the problem, then add a memo to store the results of subproblems.

# NOTE:
# (1) Memoization is a design pattern where we cache return values 
# based on the arguments to a function in order to avoid duplicate computation.

# (2) The memo keys should always contain the arguments that change during the recursion.

# (3) If the recursion tree diagram has duplicate subtrees, then it requires dp.

# (4) Memoization stores value that is returned in the recursive case.

# ----------- Q-1: Fibonacci ------------
# fib(0); # -> 0
# fib(1); # -> 1
# fib(4); # -> 3

# The 0-th number of the sequence is 0.
# The 1-st number of the sequence is 1.
# generate further calculate the sum of previous two numbers

# fib(0) = 0
# fib(1) = 1
# Fib(6) = fib(5) + fib(4)

# Time complexity: O(2^n)
#  level         tree                                    nodes
#  -----   ---------------------------------------       -----
#   1                       (4)                            1
#                          /   \
#   *2                   (3)    3                          *2
#                       /  \   / \
#   *2                (2)   2 2   2                        *2
#                     / \  /\ /\ /\
#   *2              (1) 1 1 1 1 1 1 1                     *2
#
#                         => 2^n  total calls
# each level roughly doubles the number of calls.
# Space complexity: O(n), adding elements to stack

# Using recursion
# O(2^n), O(n)

# Using Memoization
# We will store duplicate nodes
# Time complexity: O(n); as values are stored in memo
# Space complexity: O(n), adding elements to stack
# O(n), O(n)

# -- Using Recursion --
def fib(n):
  if n == 0:
    return 0

  if n == 1:
    return 1

  return fib(n - 1) + fib(n - 2)
# O(2^n), O(n)

# -- Using Memoization --
def fib(n):
  return _fib(n, {})

def _fib(n, memo):
  if n in memo:
    return memo[n]
    
  if n == 0:
    return 0

  if n == 1:
    return 1

  memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
  return memo[n]
# O(n), O(n)

# ----------- Q-2: Tribonacci ------------
# trib(0); # -> 0
# trib(1); # -> 1
# trib(2); # -> 1
# trib(4); # -> 4

# The 0-th and 1-st numbers of the sequence are both 0.
# The 2-nd number of the sequence is 1.
# Generate further numbers of the sequence, calculate the sum of previous three numbers.

# trib(0) = 0
# trib(1) = 0
# trib(2) = 1
# trib(n) = trib(n-1) + trib(n-2) + trib(n-3)

# Time complexity: O(3^n)
#  level              tree                                  nodes
#  -----   ----------------------------------------         -----
#   1                        (5)                              1
#                       /     |     \
#   *3                (4)    (3)     2                        *3
#                   / | \   / | \
#   *3            (3) 2  1  2 1  0                            *3
#                / | \
#   *3         (2) 1  0                                       *3
#
#                         => 3^n  total calls
# each node branches into 3 recursive calls (n-1, n-2, n-3),
# so the call count roughly triples at every level.
# Space complexity: O(n), recursion stack depth is height of tree

# Using Memoization
# We will store duplicate nodes
# Time complexity: O(n); as values are stored in memo
# Space complexity: O(n), adding elements to stack
# O(n), O(n)

# -- Using Recursion --
def tribonacci(n):
  if n == 0:
    return 0

  if n == 1:
    return 0

  if n == 2:
    return 1

  return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
# O(3^n), O(n)

# -- Using Memoization --
def tribonacci(n):
  return _tribonacci(n, {})

def _tribonacci(n, memo):
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0

  if n == 1:
    return 0

  if n == 2:
    return 1

  memo[n] = _tribonacci(n-1, memo) + _tribonacci(n-2, memo) + _tribonacci(n-3, memo)
  return memo[n]
# O(n), O(n)


# --------- Q-3: sum possible --------------
# sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
# sum_possible(15, [6, 2, 10, 19]) # -> False
# sum_possible(13, [6, 2, 1]) # -> True

# amount = 4
# numbers = [1, 2, 3]

#                       (4)
#            /           |           \
#          (3)          (2)          (1)
#        /  |  \        /  \          |
#      (2) (1) (0)    (1)  (0)       (0)
#     /  \   |         |
#   (1)  (0)(0)       (0)
#    |
#   (0)
#
# Each level branches into n children
# so total calls ~ n^a  =>  O(n^a) time.
#   Time : O(n^a)
#   Space: O(a)   (recursion stack depth)

# With Memoization (memo keyed by remaining amount):
#   Time : O(a * n)
#   Space: O(a)

# -- Using Recursion --
def sum_possible(amount, numbers):
  if amount < 0:
    return False

  if amount == 0:
    return True

  for num in numbers:
    if sum_possible(amount - num, numbers) == True:
      return True

  return False
# O(n^a), O(a)

# -- Using Memoization --
def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})
  
def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  
  if amount < 0:            # dont store base case in memo
    return False

  if amount == 0:
    return True

  for num in numbers:
    if _sum_possible(amount - num, numbers, memo) == True:
      memo[amount] = True    # we store in memo at time of returning 
      return True            # we store current "amount" not "amount - num" in memo 

  memo[amount] = False       # we store in memo at time of returning 
  return False
# O(a*n), O(a)


# --------- Q-4: Min change -----------
# min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
# min_change(13, [1, 9, 5, 14, 30]) # -> 5
# min_change(23, [2, 5, 7]) # -> 4

# return the minimum number of coins required to create the amount. 
# You may use each coin as many times as necessary.
# If it is not possible to create the amount, then return -1.

# amount = 4
# coins = [1, 2, 3]

#   Time : O(c^a)
#   Space: O(a)   (recursion stack depth)

# With Memoization 
#   Time : O(a * c)
#   Space: O(a)

# ---- Using Recursion -------
def min_change(amount, coins):
  if amount < 0:
    return float('inf')
  
  if amount == 0:
    return 0

  min_coins = float('inf')
  for coin in coins:
    num_coins = 1 + min_change(amount-coin, coins)
    min_coins = min(num_coins, min_coins)

  return min_coins
# O(c^a), O(a)     

# ------ Using Memoization ------
def min_change(amount, coins):
  ans = _min_change(amount, coins, {})
  if ans == float('inf'):
    return -1
  else:
    return ans

# - Function -  
def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]
  
  if amount < 0:
    return float('inf')
  
  if amount == 0:
    return 0

  min_coins = float('inf') # positive inf as we want min
  for coin in coins: # adding 1 because at each level we take (1 + min of subtrees)
    num_coins = 1 + _min_change(amount-coin, coins, memo) 
    min_coins = min(num_coins, min_coins)

  memo[amount] = min_coins
  return min_coins
# O(a*c), O(a)   

# --------- Q-5: GRID Count paths -------------
# 'X' represents walls and 'O' represents open spaces.
# You may only move down or to the right and cannot pass through walls.
# number of ways possible to travel from the top-left corner of the grid to the bottom-right corner.

# grid = [
#   ["O", "O"],
#   ["O", "O"],
# ]
# count_paths(grid) # -> 2

# grid = [
#   ["O", "O", "X"],
#   ["O", "O", "O"],
#   ["O", "O", "O"],
# ]
# count_paths(grid) # -> 5
                
#   Time : O(2 ^ (r+c))
#   Space: O(r + c)   (recursion stack depth)

# With Memoization 
#   Time : O(r * c)
#   Space: O(r * c) (r*c coming from size of the memo)

# row and col out-of-bounce, return 0
# if reached wall, return 0
# if at last row, last col i.e bottom right , return 1
# down count = move down
# right count = move right
# return down count + right count

# -- Using recursion --
def count_paths(grid):
  return _count_paths(grid, 0, 0)

def _count_paths(grid, row, col):
  if row == len(grid) or col == len(grid[0]) or grid[row][col] == 'X':
    return 0 # row and col out-of-bounce and wall, return 0

  if row == len(grid) - 1 and col == len(grid[0]) - 1:
    return 1 # if at last row, last col i.e bottom right , return 1

  down_count = _count_paths(grid, row + 1, col)
  right_count = _count_paths(grid, row, col + 1)
  return down_count + right_count
# O(2 ^ (row+col)) , O(row + col)


# -- Using Memoization --
def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, row, col, memo):
  pos = (row, col)
  if pos in memo:
    return memo[pos]
  
  if row == len(grid) or col == len(grid[0]) or grid[row][col] == 'X':
    return 0 # row and col out-of-bounce and wall, return 0

  if row == len(grid) - 1 and col == len(grid[0]) - 1:
    return 1 # if at last row, last col i.e bottom right , return 1

  down_count = _count_paths(grid, row + 1, col, memo)
  right_count = _count_paths(grid, row, col + 1, memo)
  memo[pos] = down_count + right_count
  return memo[pos]
# O((row * col)) , O(row * col)


# --------- Q-6: GRID Max path sum ---------
# Same as count paths, below 2 changes
# if at last row, last col i.e bottom right , return grid[row][col]
# max_path_sum = grid[row][col] + max(down_count , right_count)

# Time and space complexity same as count paths

def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, row, col, memo):
  pos = (row, col)
  if pos in memo:
    return memo[pos]
  
  if row == len(grid) or col == len(grid[0]) or grid[row][col] == 'X':
    return 0

  if row == len(grid) - 1 and col == len(grid[0]) - 1:
    return grid[row][col] # CHANGE
    # if at last row, last col i.e bottom right , return grid[row][col]

  down_count = _max_path_sum(grid, row + 1, col, memo)
  right_count = _max_path_sum(grid, row, col + 1, memo)
  # max_path_sum = grid[row][col] + max(down_count , right_count)
  memo[pos] = grid[row][col] + max(down_count , right_count) # CHANGE
  return memo[pos]
# O((row * col)) , O(row * col)


# -------- Q-7: non adjacent sum ---------------
# There is no limit on how many items can be taken into the sum as long as they are not adjacent.

# For example, given:
# [2, 4, 5, 12, 7]
# The maximum non-adjacent sum is 16, because 4 + 12. 
# 4 and 12 are not adjacent in the list.

# nums = [7, 5, 5, 12]
# non_adjacent_sum(nums) # -> 19

# Create a tree by branching into two,
# 1. include the first number and then skip the next number
# 2. skip the first number and move to the next number
# base case: [ ] -> 0
# at each node take edge value and add to the sum of the subtree
# at each level take max of both subtrees and return to parent node

#
# base case: [ ] -> 0
#
#                          2,4,5,12,7
#                  2 /                  \
#               5,12,7                 4,5,12,7
#            5 /        \ 12        4 /          \
#           7          12,7        12,7         5,12,7
#         7 /  \     12 /  \
#       [ ]   [ ]   [ ]    7

# Time complexity: O(2^n)
# Space complexity: O(n) (recursion stack depth)

# With Memoization
# Time complexity: O(n)
# Space complexity: O(n) (recursion stack depth + memo size)

# -- Using recursion ----
def non_adjacent_sum(nums):
  if len(nums) == 0:
    return 0

  include = nums[0] + non_adjacent_sum(nums[2:]) # number + all rest except adjecent
  exclude = non_adjacent_sum(nums[1:]) # without number + all rest include adjecent

  return max(include, exclude)
# # O(2^n), O(n)

# -- Using recursion with index ----
# Slicing using nums[2:] or nums[1:] takes lot of Time 
# So we will be using index approach
def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0)
  
def _non_adjacent_sum(nums, index):
  if index >= len(nums):
    return 0

  include = nums[index] + _non_adjacent_sum(nums, index + 2) 
  exclude = _non_adjacent_sum(nums, index + 1)

  return max(include, exclude)
# O(2^n), O(n)

# -- Using Memoization ----
def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})
  
def _non_adjacent_sum(nums, index, memo):
  if index in memo:
    return memo[index]
  
  if index >=len(nums):
    return 0

  include = nums[index] + _non_adjacent_sum(nums, index + 2, memo) 
  exclude = _non_adjacent_sum(nums, index + 1, memo) 

  memo[index] = max(include, exclude)
  return memo[index]
# O(n), O(n)

# ---------- Q-8: Summing squares -----------
# Given 12:
# summing_squares(12) -> 3
# The minimum squares required for 12 is three, by doing 4 + 4 + 4.
# Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.

# summing_squares(8) # -> 2

# input: 10
# At each node, subtract a perfect square (1, 4, 9, ...) that fits.
# At each node take the minimum of the subtree and add 1 (for the current node) and return to parent node.
# base case: if n == 0, then return 0
#
#                                  10
#                      1 /          4 |          9 \
#                      9             6             1
#                 1 / 4 | 9 \     1 / 4 \        1 |
#                 8   5   0      5     2          0
#                 :   :       1 / 4 \   | 1
#                             4    1    1
#                          1 / 4 \  | 1  | 1
#                          3    0   0    0
#                        1 |
#                          2
#                        1 |
#                          1
#                        1 |
#                          0

# Time Complexity = O( sqrt(n) ^ n) ; 
# not 2^n as base is not 2, abse is sqrt(n)
# Space Complexity = O(n)

# -- Using memoization --
# Time Complexity = O( n * sqrt(n)) 
# Space Complexity = O(n)

# Using recursion
import math
def summing_squares(n):
  if n == 0:
    return 0

  min_squares = float('inf')
  for i in range(1, math.floor(math.sqrt(n)) + 1):
    square = i * i
    num_squares = 1 + summing_squares(n - square)
    min_squares = min(min_squares, num_squares)

  return min_squares
# O( sqrt(n) ^ n) , O(n)


# Using memoization
import math
def summing_squares(n):
  return _summing_squares(n, {})

def _summing_squares(n, memo):
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0

  min_squares = float('inf')
  for i in range(1, math.floor(math.sqrt(n)) + 1):
    square = i * i
    num_squares = 1 + _summing_squares(n - square, memo)
    min_squares = min(min_squares, num_squares)

  memo[n] = min_squares
  return memo[n]
# O( n * sqrt(n)) , O(n)


# ----------- Q-9: counting change -----------
# For example,
# counting_change(4, [1,2,3]) -> 4
# There are four different ways to make an amount of 4:
# 1. 1 + 1 + 1 + 1
# 2. 1 + 1 + 2
# 3. 1 + 3
# 4. 2 + 2

# counting_change(8, [1, 2, 3]) # -> 10

# Count the number of different ways to make a given amount using the coins.
# You may use each coin as many times as necessary.

# amount = 4
# coins = [1, 2, 3]
# -> 4 different ways

# At each level we pick the next coin and branch on how many of it to use
# (x0, x1, x2, ...) until the amount is exceeded.
# base case: amount == 0 -> count this as 1 valid way (checkmark)
#
#                                4
#         coin=1  x0 /      x1 |     x2 \     x4 \
#                  4           3         2        0  (way)
#       coin=2  x0/ x1| x2\  x0/  x1\  x0/ x1\
#               4   2   0   3    1    2    0  (way)
#                          (way)          (way)
#     coin=3  x0/ x1\ x0|  x0/ x1\   x0|
#             4    1   2  3    0    2
#                              (way)

# Using recursion
# Time complexity: O(amount ^ coins)  
# Space complexity: O(amount + coins)  (recursion stack depth)

# With Memoization
# Time complexity: O(amount * coins)
# Space complexity: O(amount * coins) (recursion stack depth + memo dictionary size)

# NOTE: -- Min change ---
# amount = 4
# coins = [1, 2, 3]

#   Time : O(c^a)
#   Space: O(a)   (recursion stack depth)

# With Memoization 
#   Time : O(a * c)
#   Space: O(a)

# using recursion
def counting_change(amount, coins):
  return _counting_change(amount, coins, 0)

def _counting_change(amount, coins, index):
  if amount == 0:
    return 1

  if index == len(coins):
    return 0

  total_ways = 0
  coin = coins[index]
  for qty in range(0, (amount // coin) + 1): # '//' to roundup, + 1 for range 
    remainder = amount - (qty * coin)
    total_ways += _counting_change(remainder, coins, index + 1)

  return total_ways
# O(a ^ c), O(a + c)


# using Memoization
def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, index, memo):
  key = (amount, index)
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1

  if index == len(coins):
    return 0

  total_ways = 0
  coin = coins[index]
  for qty in range(0, (amount // coin) + 1): # '//' to roundup, + 1 for range 
    remainder = amount - (qty * coin)
    total_ways += _counting_change(remainder, coins, index + 1, memo)

  memo[key] = total_ways
  return memo[key]
# O(a * c), O(a * c)


# ---------- Q-10: array stepper ------------
# For example, given:
#    idx =  0  1  2  3  4  5
# numbers = [2, 4, 2, 0, 0, 1]

# The answer is True.
# We start at idx 0, we could take 1 step or 2 steps forward.
# The correct choice is to take 1 step to idx 1.
# Then take 4 steps forward to the end at idx 5.

# array_stepper([2, 3, 2, 0, 0, 1]) # -> False
# array_stepper([4, 1, 5, 1, 1, 1, 0, 4]) # -> True

# Given an array of non-negative numbers.
# Each element represents the maximum number of steps you can take forward
# from that index. Return True if you can reach the last index, else False.

# nums = [2, 4, 2, 0, 0, 1]
#  idx =  0  1  2  3  4  5   <- goal is to reach the last index (5)
# array_stepper(nums) # -> True

# At each index, branch into (1..nums[index]) forward steps.
# base case: if index >= last index -> reached the goal, return True
#
#                                  0
#                      /                      \
#                     1                        2
#         /      |      |     \             /     \
#        2       3      4      5(true)     3       4
#      /   \   false  false              false   false
#     3     4
#   false  false

# Using recursion
# Time complexity: O(n ^ 2)  
# Space complexity: O(n)     (recursion stack depth)
#
# With Memoization (memo keyed by index):
# Time complexity: O(n)
# Space complexity: O(n)

# Using recursion
def array_stepper(numbers):
  return _array_stepper(numbers, 0)

def _array_stepper(numbers, index):
  if index >= len(numbers) - 1:
    return True

  max_step = numbers[index]
  for step in range(1, max_step + 1):
    if _array_stepper(numbers, index + step):
      return True

  return False
# Time complexity: O(n ^ 2)  
# Space complexity: O(n)     (recursion stack depth)

# Using Memoization
def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, index, memo):
  if index in memo:
    return memo[index]
  
  if index >= len(numbers) - 1:
    return True

  max_step = numbers[index]
  for step in range(1, max_step + 1):
    if _array_stepper(numbers, index + step, memo):
      memo[index] = True
      return memo[index]

  memo[index] = False
  return memo[index]
# Time complexity: O(n)  
# Space complexity: O(n)     (recursion stack depth)



# --------- Q-11: max palin subsequence -----------
# The function should return the length of the longest subsequence that is also a palindrome.
# A subsequence of a string can be created by deleting any characters of the string,
# while maintaining the relative order of characters.

# max_palin_subsequence("luwxult") # -> 5
# max_palin_subsequence("xyzaxxzy") # -> 6

# A subsequence is formed by deleting 0 or more characters without
# reordering. Return the length of the longest subsequence that is a palindrome.

# max_palin_subsequence("lxuul") # -> 4  (because "luul")

# At each node look at the first and last characters of the string:
# 1. if first == last -> 2 + inner string (drop both ends)  [edge label = 2]
# 2. if first != last -> branch into two:                   [edge label = 0]
#       a. drop the first character
#       b. drop the last character
#    then take the max of both subtrees.
#
# Base Cases:
#   if str.length == 0, then return 0
#   if str.length == 1, then return 1
#
#                            lxuul
#                              | 2
#                            xuu
#                       0 /        \ 0
#                       uu          xu
#                       | 2      0 /    \ 0
#                      [ ]        u      x

# Using recursion
# Time complexity: O(2^n)   
# Space complexity: O(n)    (recursion stack depth)

# With Memoization (memo keyed by (i, j) substring bounds):
# Time complexity: O(n) ❌
# Space complexity: O(n) ❌

# In the earlier problems (fib, array_stepper, summing_squares),
# the memo key was a single value (one index or one number).
# Time complexity: O(n^2)  The memo stores (i, j) pair → O(n^2)
# Space complexity: O(n^2) The memo stores one entry per (i, j) pair → O(n^2)

# Using recursion
def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1)

def _max_palin_subsequence(string, i, j):
  if i == j:
    return 1

  if i > j:
    return 0

  if string[i] == string[j]:
    return 2 + _max_palin_subsequence(string, i + 1, j - 1)
  else:
    return max(
      _max_palin_subsequence(string, i + 1, j),
      _max_palin_subsequence(string, i, j - 1)
    )
# O(2^n), O(n) 


# Using Memoization
def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, i, j, memo):
  key = (i,j)
  if key in memo:
    return memo[key]
  
  if i == j:
    return 1

  if i > j:
    return 0

  if string[i] == string[j]:
    memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
  else:
    memo[key]= max(
      _max_palin_subsequence(string, i + 1, j, memo),
      _max_palin_subsequence(string, i, j - 1, memo)
    )

  return memo[key]
# O(n^2), O(n^2) 

# -------------- Q-12: overlap subsequence --------------
# The function should return the length of the longest overlapping subsequence.
# A subsequence of a string can be created by deleting any characters of the string,
# while maintaining the relative order of characters.

# overlap_subsequence("dogs", "daogt") # -> 3
# overlap_subsequence("xcyats", "criaotsi") # -> 4

#  Given two strings, return the length of the longest common subsequence
# between them. A subsequence is formed by deleting 0 or more characters
# without reordering the remaining characters.

# overlap_subsequence("dogs", "normantizes") # -> ? 
# overlap_subsequence("cat", "aot") # -> 1  (because "t")

# Compare the first character of each string:
# 1. if a[i] == b[j] -> 1 + overlap of (rest of a, rest of b)   [edge = 1]
#                       (move both pointers forward)
# 2. if a[i] != b[j] -> branch into two:                        [edge = 0]
#       a. move forward in the first string  (i + 1, j)
#       b. move forward in the second string (i, j + 1)
#    then take the max of both subtrees.
#
# base case: if either string is empty -> return 0
#
#                              cat
#                              aot
#                           0 /     \ 0
#                         at          cat
#                         aot         ot
#                       1 |        0 /     \ 0
#                        t          at       cat
#                        ot         t         t
#                     0 / \ 0    0 / \ 0    0 /  \ 0
#                      ot   t    t     at   at    cat
#                      t         t                (empty branches)
#
# Using recursion
# Time complexity: O(2 ^ (n + m))
# Space complexity: O(n + m)   (recursion stack depth)
#
# With Memoization (memo keyed by (i, j) positions in the two strings):
# Time complexity: O(n * m) The memo stores (i, j) pair → O(n * m)
# Space complexity: O(n * m) The memo stores one entry per (i, j) pair → O(n * m)

# Using recursion 
def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0)

def _overlap_subsequence(string_1, string_2, i, j):
  if i == len(string_1) or j == len(string_2):
    return 0

  if string_1[i] == string_2[j]:
    return 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1)
  else:
    return max(
      _overlap_subsequence(string_1, string_2, i + 1, j),
      _overlap_subsequence(string_1, string_2, i, j + 1)
    )
# O(2 ^ (n + m)), O(n + m) 

# Using Memoization
def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, i, j, memo):
  key = (i, j)
  if key in memo:
    return memo[key]
  
  if i == len(string_1) or j == len(string_2):
    return 0

  if string_1[i] == string_2[j]:
    memo[key] = 1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
  else:
    memo[key] = max(
      _overlap_subsequence(string_1, string_2, i + 1, j, memo),
      _overlap_subsequence(string_1, string_2, i, j + 1, memo)
    )

  return memo[key]
# O(n * m), O(n * m) 


# ------------------ Q-13: can concat -------------------
# return boolean indicating whether or not it is possible 
# to concatenate words of the list together to form the string.
# You may reuse words of the list as many times as needed.
  
# can_concat("oneisnone", ["one", "none", "is"]) #  -> True
# can_concat("oneisnone", ["on", "e", "is"]) #  -> False
# can_concat("oneisnone", ["on", "e", "is", "n"]) #  -> True

# foodisgood
# ["foo", "f", "ood", "is", "g", "good", "disgood"]
# At each node, try every word that is a prefix of the remaining target.
# For each matching prefix, strip it off and recurse on the suffix.
# The edge label is the prefix (word) being removed.
# base case: if str.length == 0, then return True (whole target consumed)
#
#                          foodisgood
#                     f /              \ foo
#                  oodisgood          disgood
#                  ood |
#                   isgood
#                   is |
#                    good
#                    g |
#                     ood
#                   ood |
#                     [ ]  -> True

# s = length of string
# n = number of words

# Using recursion
# Time complexity: O(n ^ s)   
# Space complexity: O(s) for Using recursion stack

# With Memoization (memo keyed by remaining suffix):
# Time complexity: O(s * n) 
# Space complexity: O(s) for Using recursion stack

# Using recursion
def can_concat(s, words):
  if s == '':
    return True

  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      if can_concat(suffix, words) ==  True:
        return True

  return False    
# O(n ^ s), O(s)

# Using Memoization
def can_concat(s, words):
  return _can_concat(s, words, {})

def _can_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if s == '':
    return True

  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      if _can_concat(suffix, words, memo) ==  True:
        memo[s] = True
        return memo[s]

  memo[s] = False    
  return memo[s]
# O(n * s), O(s)

# ------------- Q-14: Quickest concat -----------
# The function should return the minimum number of words
# needed to build the string by concatenating words of the list.
# If it is not possible to build the string, then return -1.
  
# quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) # -> 2
# quickest_concat('caution', ['ion', 'caut', 'caution']) # -> 1

# At each node, 1 + the minimum of the subtrees, and return to parent node.
# base condition: if str.length == 0, then return 0 (whole target consumed)

#                          caution
#                     ca /          \ caut
#                    ution            ion
#                  ut |             ion |
#                    ion              [ ]  -> 0
#                  ion |
#                   [ ]  -> 0

# s = length of string
# n = number of words

# Using recursion
# Time complexity: O(n ^ s)
# Space complexity: O(s)   (recursion stack depth)

# With Memoization (memo keyed by remaining suffix):
# Time complexity: O(s * n)
# Space complexity: O(s)


# Using recursion
def quickest_concat(s, words):
  result = _quickest_concat(s, words)

  if result == float('inf'):
    return -1
  else:
    return result

def _quickest_concat(s, words):
  if s == '':
    return 0

  min_value = float('inf')
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      current_value = 1 + _quickest_concat(suffix, words)
      min_value = min(min_value, current_value)

  return min_value
# O(n ^ s), O(s)       

# Using Memoization
def quickest_concat(s, words):
  result = _quickest_concat(s, words, {})

  if result == float('inf'):
    return -1
  else:
    return result

def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if s == '':
    return 0

  min_value = float('inf')
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      current_value = 1 + _quickest_concat(suffix, words, memo)
      min_value = min(min_value, current_value)

  memo[s] = min_value
  return memo[s]
# O(n * s), O(s)  


# ----------- Q-15: valid compound -----------
# The function should return a boolean indicating whether
# or not the compound can be created from the given elements.
# A compound is made by concatenating one or more elements together.
# You may reuse elements of the list as many times as needed to make a compound.

# valid_compound("neco", [
#   "Ne",
#   "O",
#   "Be",
#   "I",
#   "N",
#   "Os",
#   "Si",
#   "S",
#   "Co",
#   "C",
#   "Ir",
# ]) # -> True

# s = length of string
# n = number of words

# Using recursion
# Time complexity: O(n ^ s)
# Space complexity: O(s)   (recursion stack depth)

# With Memoization (memo keyed by remaining suffix):
# Time complexity: O(s * n)
# Space complexity: O(s)

# SAME AS CAN CONCAT
# Here words are in capital letters
# so, in if block we will have .lower() check
# if s.startswith(word.lower()):

def valid_compound(compound, elements):
  return _can_concat(compound, elements, {})

def _can_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if s == '':
    return True

  for word in words:
    if s.startswith(word.lower()):
      suffix = s[len(word):]
      if _can_concat(suffix, words, memo) ==  True:
        memo[s] = True
        return memo[s]

  memo[s] = False    
  return memo[s]
# O(s * n), O(s)


# -------- Q-16: count compounds -----------
# Here words are in capital letters
# so, in if block we will have .lower() check
# if s.startswith(word.lower()):

# Instead of True/ False here we will return number
# add to count and save in memo before return

# With Memoization (memo keyed by remaining suffix):
def count_compounds(compound, elements):
  return _can_concat(compound, elements, {})

def _can_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if s == '':
    return 1

  count = 0
  for word in words:
    if s.startswith(word.lower()):
      suffix = s[len(word):]
      count += _can_concat(suffix, words, memo)

  memo[s] = count    
  return memo[s]
# O(s * n), O(s)


# ----------- Q-17: DIRECTED GRAPH longest path -----------
# takes in an adjacency list for a directed acyclic graph.
# return the length of the longest path within the graph. 
# A path may start and end at any two nodes. 
# The length of a path is considered the number of edges in the path,
#   not the number of nodes.

# graph = {
#   'a': ['c', 'b'],
#   'b': ['c'],
#   'c': []
# }

# longest_path(graph) # -> 2


# Nodes: a, b, c, d, e, f, g
#
#                                   ( D )2
#                                  /     \
#                                 v       v
#       3        2        1      /         \
#   ( F ) --> ( G ) --> ( C ) <-           ( E )0
#                          \                 ^
#                           \_______________/
#                                  1 -> 0
#
#   ( A ) --> ( B )
#     1         0
#
# Edges:
#   F -> G
#   G -> C
#   C -> E
#   D -> C
#   D -> E
#   A -> B
#
# Longest path starting from each node:
#   E = 0   (no outgoing edges, leaf)
#   B = 0   (no outgoing edges, leaf)
#   C = 1   (C -> E)
#   G = 2   (G -> C -> E)
#   F = 3   (F -> G -> C -> E)   <- overall longest path = 3
#   D = 2   (D -> C -> E = 2, D -> E = 1, take max = 2)
#   A = 1   (A -> B)
#
# At each node, longest path = 1 + max(longest path of its neighbors).
# base case: a node with no neighbors -> 0

# e = number of edges
# n = number of nodes
# With Memoization (memo keyed by node):
# Time O(e) as we iterate over all edges of graph
# Space O(e) as we use recursion stack / (stack/queue in case of BFS and DFS) and visited set

def longest_path(graph):
  memo = {}

  # a node with no neighbors -> 0
  for node in graph:
    if graph[node] == []:
      memo[node] = 0

  for node in graph:
    _longest_path(graph, node, memo)
    
  return max(memo.values())


# DFS on graph - recursion and memoization
def _longest_path(graph, node, memo):
  if node in memo:
    return memo[node]

  max_length = 0
  for neighbor in graph[node]:
    current_path_length = 1 + _longest_path(graph, neighbor, memo)
    max_length = max(max_length, current_path_length)
      
  memo[node] = max_length
  return memo[node]
# O(e), O(n)


# --------- Q-18: UNDIRECTED GRAPH semesters required -------------
# takes in a number of courses (n) and a list of prerequisites as arguments.
# A single prerequisite of (A, B) means that course A must be taken before course B. 
# Return the minimum number of semesters required to complete all n courses. 
# There is no limit on how many courses you can take in a single semester, 
# as long as the prerequisites of a course are satisfied before taking it

# num_courses = 6
# prereqs = [
#   (1, 2),
#   (2, 4),
#   (3, 5),
#   (0, 5),
# ]
# semesters_required(num_courses, prereqs) # -> 3

# Directed graph:
# {
#   0: [5],
#   1: [2],
#   2: [4],
#   3: [5],
#   4: [],
#   5: [],
# }

# (1) --> (2) --> (4)        (3) --> (5) <-- (0)

# e = number of edges
# n = number of nodes
# With Memoization (memo keyed by node):
# Time O(e) as we iterate over all edges of graph
# Space O(e) as we use recursion stack / (stack/queue in case of BFS and DFS) and visited set

# STEP 1: Convert list into Directed graph
# STEP 2: Use DFS Recursion + memoisation to find _longest_path
# Base case : a node with no neighbors -> 1 (instead of 0)

def semesters_required(num_courses, prereqs):
  # STEP 1: Convert list into Directed graph
  graph = build_graph(num_courses, prereqs)
  
  memo = {}

  # Base case : a node with no neighbors -> 1 (instead of 0)
  for node in graph:
    if graph[node] == []:
      memo[node] = 1

  # STEP 2: Use DFS Recursion + memoisation to find _longest_path
  for node in graph:
    _longest_path(graph, node, memo)
    
  return max(memo.values())


# DFS on graph - recursion and memoization
def _longest_path(graph, node, memo):
  if node in memo:
    return memo[node]

  max_length = 0
  for neighbor in graph[node]:
    current_path_length = 1 + _longest_path(graph, neighbor, memo)
    max_length = max(max_length, current_path_length)
      
  memo[node] = max_length
  return memo[node]

# Build Directed graph from list
def build_graph(num_courses, prereqs):
  graph = {}
  
  for course in range(num_courses):
    graph[course] = []
    
  for prereq in prereqs:
    a, b = prereq
    graph[a].append(b)
  
  return graph
# O(e), O(n)


# -------- Q-19: max increasing subseq ------------
# return the length of the longest subsequence of strictly increasing numbers.

# A subsequence of a list can be created by deleting any items of the list, 
# while maintaining the relative order of items.

# numbers = [4, 18, 20, 10, 12, 15, 19]
# max_increasing_subseq(numbers) # -> 5

# numbers = [12, 9, 2, 5, 4, 32, 90, 20]
# max_increasing_subseq(numbers) # -> 4

# nums = [6, 9, 7, 8]
# At each node decide to SKIP or TAKE the first number:
#   - Left branch  -> skip current number (prev stays the same)
#   - Right branch -> take current number (only if current > prev),
#                     prev becomes current (edge label = number taken)
# The blue label is the "prev" value (starts at -inf).
#
#                        -inf [6,9,7,8]
#                       /                \ 6
#               -inf [9,7,8]            6 [9,7,8]
#              /            \ 9        /          \ 9
#      -inf [7,8]        9 [7,8]   6 [7,8]      9 [7,8]
#       /      \ 7         | 9     /     \ 7       | 9
# -inf [8]   7 [8]      9 [8]  6 [8]   7 [8]    9 [8]
#  /   \ 8    | 8        | 8   /  \ 8   | 8       | 8
# [ ] [ ]    [ ]       [ ]  [ ] [ ]   [ ]       [ ]


# split into tree by taking not taking current and taking current
# intially previous = -infy
# when taking current, split number should be greater than previous taken, as we are finding max increasing subsequence
# for longest path - look for path with most number of numbers along edges

# n = number of items
# Time: O(2 ^ n); exponential for each item we split into 2 left and right tree
# Space: O(n); storing items

# -- using memoisation -- key = prev, index
# Time: O(n * n); we will store previous and index of array items; so n * n
# Space: O(n * n); space consumed by memo weight and index of array items; so n * n


# -- using brute force ------
def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, float('-inf'), 0)

def _max_increasing_subseq(numbers, prev, i):
  if i == len(numbers):    # index at end, index = len of numbers, return 0
    return 0

  current = numbers[i]
  dont_take_current = _max_increasing_subseq(numbers, prev, i + 1) # not taking current, previous does not change, increment index

  take_current = 0
  if current > prev:
    take_current = 1 + _max_increasing_subseq(numbers, current, i + 1) # taking current, previous replaced with current, increment index and add 1 for path

  return max(dont_take_current, take_current)

# n = number of items
# Time: O(2 ^ n); exponential for each item we split into 2 left and right tree
# Space: O(n); storing items


# -- using Memoization ------
def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, float('-inf'), 0, {})

def _max_increasing_subseq(numbers, prev, i, memo):
  key = (prev, i)  # key is the things that changes in method
  if key in memo:
    return memo[key]
  
  if i == len(numbers):    # index at end, index = len of numbers, return 0
    return 0

  current = numbers[i]
  dont_take_current = _max_increasing_subseq(numbers, prev, i + 1, memo) # not taking current, previous does not change, increment index

  take_current = 0
  if current > prev:
    take_current = 1 + _max_increasing_subseq(numbers, current, i + 1, memo) # taking current, previous replaced with current, increment index and add 1 for path

  memo[key] = max(dont_take_current, take_current)
  return memo[key]

# n = number of items
# Time: O(2 ^ n); exponential for each item we split into 2 left and right tree
# Space: O(n); storing items



# ------------- Q-20: knapsack --------------
# knapsack that takes in a list of item values, a list of item weights, and a weight limit.
# Your job is to pick items to pack into your knapsack 
# so that its total weight does not exceed the limit and the value of the items is maximized. 
# You may either take an item once or not at all. 
# You cannot take the same item multiple times. 
# Return the maximum total value of items you can pack into the knapsack.

# knapsack([5, 4, 9], [6, 1, 15], 20) # -> 13
# knapsack([5, 1, 6], [4, 1, 5], 20) # -> 12

# wl = 8  (weight limit)
# w = [4, 1, 5, 2]   (weights)
# v = [5, 1, 7, 3]   (values)
# i =  0  1  2  3    (index)

# Each node holds the REMAINING weight limit.
# At each item branch into two:
#   - Left  -> skip the item (weight limit unchanged, edge label = none)
#   - Right -> take the item (weight limit - weights[i], edge label = value[i])
# A node going negative means that path is invalid.
#
#                                  8
#                       /                       \ 5
#                      8                          4
#                /          \ 1            /            \ 1
#               8            7            4              3
#            /     \ 7    /     \ 7    /     \ 7      /     \ 7
#           8       3    7       2    4      -1     3       -2
#          / \ 3   / \ 3 / \ 3  / \ 3 / \ 3        / \ 3
#         8   6   3   1 7   5  2   0 4   2        3   1

# At every node we split into leave item or take the item
# if take the item, then substract value of item from weight
# after making tree, at leaf nodes we can have 
#    -ve <0 means path invalid
#    +ve >0 means space left
#    0 means totally used space of knapsack
# base case, 
#     taking leaf nodes as 0, 
#     left subtree - go left without taking vales, but increment
#     Right subtree - go right taking values, adding values at the edges while going up
#     taking max of left-subtree and right sub-tree

# n = number of items
# w = weight limit
# Time: O(2 ^ n); exponential for each item we split into 2 left and right tree
# Space: O(n); storing items

# -- using memoisation --
# Time: O(n * w); we will store weight and index of array items; so n * w
# Space: O(n * w); space consumed by memo weight and index of array items; so n * w

# -- using brute force ---
def knapsack(values, weights, weight_limit):
  return _knapsack(values, weights, weight_limit, 0)


def _knapsack(values, weights, weight_limit, i):
  if weight_limit < 0:    # if weight limit is negative return  -infinity
    return float("-inf")

  if i == len(values):    # if done choosing all items, index at end, index = len of values or items, return 0
    return 0

  # dont take current item, but increment level
  left_subtree = _knapsack(values, weights, weight_limit, i + 1) 
  # take current item, increment level, and add value along the edge while going up
  right_subtree = values[i] + _knapsack(values, weights, weight_limit - weights[i], i + 1) 

  return max(left_subtree, right_subtree)

# n = number of items
# w = weight limit
# Time: O(2 ^ n); exponential for each item we split into 2 left and right tree
# Space: O(n); storing items

# -- using Memoisation ---
def knapsack(values, weights, weight_limit):
  return _knapsack(values, weights, weight_limit, 0, {})


def _knapsack(values, weights, weight_limit, i, memo):
  key = (weight_limit, i)  # key is the things that changes in method
  if key in memo:
    return memo[key]
  
  if weight_limit < 0:    # if weight limit is negative return  -infinity
    return float("-inf")

  if i == len(values):    # if done choosing all items index = len of vales or item
    return 0

  # dont take current item, but increment level
  left_subtree = _knapsack(values, weights, weight_limit, i + 1, memo) 
  # take current item, increment level, and add value along the edge while going up
  right_subtree = values[i] + _knapsack(values, weights, weight_limit - weights[i], i + 1, memo) 

  memo[key] = max(left_subtree, right_subtree)
  return memo[key]

# -- using memoisation --
# Time: O(n * w); we will store weight and index of array items; so n * w
# Space: O(n * w); space consumed by memo weight and index of array items; so n * w


# ------- Q-21: positioning plants -------------

# Given these costs,
# costs = [
#   [4, 3, 7],
#   [6, 1, 9],
#   [2, 5, 3]
# ]

# The costs of plants at position 1 are $6, $1, and $9.
# The cost of planting flower type 0 at position 1 is $6.
# The cost of planting flower type 2 at position 1 is $9.

# The function should return the minimum cost of planting flowers without placing the same flower type in adjacent positions.
  
# plants = [
#   [4, 3, 7],
#   [6, 1, 9],
#   [2, 5, 3],
# ]
# positioning_plants(plants) # -> 7
# (plant 0 at pos 0 = 4) + (plant 1 at pos 1 = 1) + (plant 0 at pos 2 = 2) = 7

#         plant
#          0 1 2
#   pos 0 [4,3,7]
#   pos 1 [6,1,9]
#   pos 2 [2,5,3]
#
# Each node is (position, previous_plant).
# Root (0, NULL) -> nothing placed yet, every plant is allowed.
# The edge label is the cost of placing that plant at the current position.
# At each position branch into every plant whose index != previous_plant.
#
#                                 (0,NULL)
#                   4 /              3 |              7 \
#                 (1,0)            (1,1)            (1,2)
#               1 /   \ 9        6 /   \ 9        6 /   \ 1
#           (2,1)    (2,2)   (2,0)    (2,2)   (2,0)    (2,1)
#          2 / \ 3  2 / \ 5  5 / \ 3 2 / \ 5  5 / \ 3 2 / \ 3
#       (3,0)(3,2)(3,0)(3,1)(3,1)(3,2)(3,0)(3,1)(3,1)(3,2)(3,0)(3,2)
#
# base case: pos == len(plants) -> 0 (all positions filled)
# At each node take the cost on the edge + min (left subtree + right subtree).
 
# every row represents position of garden
# every col represents plant type within a garden
# 2 same flower type cannot be together
# minimum cost of planting every flower in garden

# n = number of positions
# m = number of plant types
# Time: O(m ^ n); height of tree = n; branching factor = m; branching factor becomes base
# Space: O(n); stack space of using recursion

# -- using memoisation - key = (pos, last_plant)
# Time: O(n * m); these many unique recursion function calls to make
# Space: O(n * m)); store all the unique recursion result in memo object


# -- Using recursion --
def positioning_plants(costs):
  return _positioning_plants(costs, 0, None)

def _positioning_plants(costs, pos, last_plant):
  if pos == len(costs): # pos at end of tree; leaf node; return 0
    return 0

  min_cost = float('inf')
  for plant_type, plant_cost in enumerate(costs[pos]): # costs[pos] will give all rows; enumerate will give pair ( plant_type, plant_cost)
    if plant_type != last_plant: # same plants should not be together
      candidate = plant_cost + _positioning_plants(costs, pos + 1, plant_type) # increamenting pos for next level
      min_cost = min(min_cost, candidate)

  return min_cost

# n = number of positions
# m = number of plant types
# Time: O(m ^ n); height of tree = n; branching factor = m; branching factor becomes base
# Space: O(n); stack space of using recursion

 # -- Using memoisation -- key = (pos, last_plant)
def positioning_plants(costs):
  return _positioning_plants(costs, 0, None, {})

def _positioning_plants(costs, pos, last_plant, memo):
  key = (pos, last_plant)
  if key in memo:
    return memo[key]
  
  if pos == len(costs): # pos at end of tree; leaf node; return 0
    return 0

  min_cost = float('inf')
  for plant_type, plant_cost in enumerate(costs[pos]): # costs[pos] will give all rows; enumerate will give pair ( plant_type, plant_cost)
    if plant_type != last_plant: # same plants should not be together
      candidate = plant_cost + _positioning_plants(costs, pos + 1, plant_type, memo) # increamenting pos for next level
      min_cost = min(min_cost, candidate)

  memo[key] = min_cost
  return memo[key] 

# Time: O(n * m); these many unique recursion function calls to make
# Space: O(n * m)); store all the unique recursion result in memo object


# ------- Q-22: counting paths out of grid (out of boundary paths) -------------
# Given a grid of m rows and n columns, a ball starts at position (r, c).
# In each move the ball can go up, down, left, or right by one cell.
# You may make at most k moves.
# Return the number of ways to move the ball OUT of the grid boundary.

# m, n, k, r, c = 3, 4, 2, 0, 0
# count_paths(m, n, k, r, c) # -> 6

#   m, n, k, r, c
#   3, 4, 2, 0, 0
#
# Each node is (k, r, c) -> (moves left, row, col).
# At each node branch into 4 directions, each costs 1 move (k - 1):
#   up    -> (k-1, r-1, c)
#   down  -> (k-1, r+1, c)
#   left  -> (k-1, r, c-1)
#   right -> (k-1, r, c+1)
#
#                                  2,0,0
#               up /        down |        left |        right \
#            1,-1,0           1,1,0          1,0,-1          1,0,1
#             OUT          /   |   |   \      OUT        /   |   |   \
#                      0,0,0 0,2,0 0,1,-1 0,1,1     0,-1,1 0,1,1 0,0,0 0,0,2
#                                   OUT                OUT
#
# base case 1: if r or c is out of bounds -> return 1 (one way out)
# base case 2: if k == 0 (no moves left) and still in bounds -> return 0
# At each node sum the counts of all 4 subtrees.

# Using recursion
# Time complexity: O(4 ^ k)   (each node branches into 4 directions)
# Space complexity: O(k)      (recursion stack depth)

# With Memoization (memo keyed by (k, r, c)):
# Time complexity: O(k * m * n)   (k*m*n unique states)
# Space complexity: O(k * m * n)  (one memo entry per state)

# -- using recursion --
def breaking_boundaries(m, n, k, r, c):
  return _breaking_boundaries(m, n, k, r, c)

def _breaking_boundaries(m, n, k, r, c):

  row_inbounds = 0 <= r < m
  col_inbounds = 0 <= c < n
  if not row_inbounds or not col_inbounds:
    return 1
  
  if k == 0:
    return 0
  
  count = 0
  
  deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for delta in deltas:
    d_row, d_col = delta
    count += _breaking_boundaries(m, n, k - 1, r + d_row, c + d_col)
    
  return count
# O(4 ^ k), O(k)

# -- using Memoization --

def breaking_boundaries(m, n, k, r, c):
  return _breaking_boundaries(m, n, k, r, c, {})

def _breaking_boundaries(m, n, k, r, c, memo):
  key = (k, r, c)
  if key in memo:
    return memo[key]
  
  row_inbounds = 0 <= r < m
  col_inbounds = 0 <= c < n
  if not row_inbounds or not col_inbounds:
    return 1
  
  if k == 0:
    return 0
  
  count = 0
  
  deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for delta in deltas:
    d_row, d_col = delta
    count += _breaking_boundaries(m, n, k - 1, r + d_row, c + d_col, memo)
    
  memo[key] = count
  return memo[key]
# O(k * m * n), O(k * m * n)


# ------- Q-23: knightly number -------------
# A knight is on a chess board.
# Return the total number of ways the knight can move to a target position
# in exactly m moves. On a single move, the knight moves in an "L" shape;
# two spaces in any direction, then one space in a perpendicular direction.
# This gives 8 possible positions on a single move.
# The knight cannot move out-of-bounds of the board.

# n  = the length of the chess board
# m  = the number of moves that must be used
# kr = the starting row of the knight
# kc = the starting column of the knight
# pr = the target row
# pc = the target column

# knightly_number(8, 2, 4, 4, 5, 5) # -> 2
# knightly_number(8, 2, 7, 1, 7, 1) # -> 3

# Each node is (m, kr, kc) -> (moves left, knight row, knight col).
# At each node branch into the 8 "L" shaped knight moves, each costs 1 move (m - 1):
#   (kr + 2, kc + 1)   (kr + 2, kc - 1)
#   (kr - 2, kc + 1)   (kr - 2, kc - 1)
#   (kr + 1, kc + 2)   (kr + 1, kc - 2)
#   (kr - 1, kc + 2)   (kr - 1, kc - 2)
#
# base case 1: if kr or kc is out of bounds -> return 0 (invalid path)
# base case 2: if m == 0 (no moves left):
#                 return 1 if knight is on the target (kr == pr and kc == pc)
#                 else return 0
# At each node sum the counts of all 8 subtrees.


# Using recursion
# n = length of the board
# m = number of moves
# Time complexity: O(8 ^ m)   (each node branches into 8 directions)
# Space complexity: O(m)      (recursion stack depth)

# With Memoization (memo keyed by (m, kr, kc)):
# n = length of the board
# m = number of moves
# Time complexity: O(m * n * n)   (m*n*n unique states)
# Space complexity: O(m * n * n)  (one memo entry per state)

# -- using recursion --
def knightly_number(n, m, kr, kc, pr, pc):
  row_inbounds = 0 <= kr < n
  col_inbounds = 0 <= kc < n
  if not row_inbounds or not col_inbounds:
    return 0

  if m == 0:
    if kr == pr and kc == pc:
      return 1
    else:
      return 0

  count = 0

  deltas = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2),
  ]
  for delta in deltas:
    d_row, d_col = delta
    count += knightly_number(n, m - 1, kr + d_row, kc + d_col, pr, pc)

  return count
# O(8 ^ m), O(m)

# -- using Memoization --
def knightly_number(n, m, kr, kc, pr, pc):
  return _knightly_number(n, m, kr, kc, pr, pc, {})

def _knightly_number(n, m, kr, kc, pr, pc, memo):
  key = (m, kr, kc)
  if key in memo:
    return memo[key]

  row_inbounds = 0 <= kr < n
  col_inbounds = 0 <= kc < n
  if not row_inbounds or not col_inbounds:
    return 0

  if m == 0:
    if kr == pr and kc == pc:
      return 1
    else:
      return 0

  count = 0

  deltas = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2),
  ]
  for delta in deltas:
    d_row, d_col = delta
    count += _knightly_number(n, m - 1, kr + d_row, kc + d_col, pr, pc, memo)

  memo[key] = count
  return memo[key]
# O(m * n * n), O(m * n * n)

