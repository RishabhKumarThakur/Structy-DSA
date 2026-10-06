# ==================== CHAPTER 7 - RECURSION AND BACKTRACKING ====================
# Recursion.py - 15 questions

# Recursive - when a function calls itself
# Iteration - When a function uses a loop

# Recursion has a base case and a recursive case
def countdown(n):
  if n == 0:
    return
  print("Entering: " + str(n))
  countdown(n-1)
  print("Exiting: " + str(n))

countdown(3)

# > running script... 
# Entering: 3 
# Entering: 2 
# Entering: 1 
# Exiting: 1 
# Exiting: 2 
# Exiting: 3 
# > finished in 28ms 

# when printed before the recursive case, it prints in decresing order 3,2,1
# when printed after the recursive case, it prints in increasing order 1,2,3

# ----------------- Q-1: Sum Numbers Recursive -----------------
# sum_numbers_recursive([5, 2, 9, 10]); -> 26
def sum_numbers_recursive(numbers):
  if len(numbers) == 0:
    return 0

  return numbers[0] + sum_numbers_recursive(numbers[1:])
    
# n = length of array
# Time O(n^2); O(n) for recursive calls and O(n) for array slicing in each iteration
# Space O(n^2); O(n) for recursive calls and O(n) for array slicing in each iteration

# Recursion uses more time and space, if we would have used for/while loop
# Time and space complexity would be O(n) and O(n)

# ----------------- Q-2: Factorial -----------------
# For example, the factorial of 6 is:
# 6 * 5 * 4 * 3 * 2 * 1 = 720

def factorial(n):
  if n == 0:
    return 1
  
  return n * factorial(n-1)

# n = number
# Time O(n); O(n) for recursive calls stack
# Space O(n); O(n) for recursive calls stack

# ----------------- Q-3: Sum of Lengths -----------------
# sum_of_lengths(['goat', 'cat', 'purple']) # -> 13
def sum_of_lengths(strings):
  if len(strings) == 0:
    return 0
  return len(strings[0]) + sum_of_lengths(strings[1:])
  
# n = length of array
# Time O(n^2); O(n) for recursive calls and O(n) for array slicing in each iteration
# Space O(n^2); O(n) for recursive calls and O(n) for array slicing in each iteration

# ----------------- Q-4: Reverse String Recursive -----------------
# reverse_string("hello") # -> "olleh"
def reverse_string(s):
  if len(s) == 0:
    return ""
  return reverse_string(s[1:]) + s[0] 

# n = length of string
# Time O(n^2); O(n) for recursive calls and O(n) for string slicing in each iteration
# Space O(n^2); O(n) for recursive calls and O(n) for string slicing in each iteration

# NOTE:
# In case of REVERSE we do recursion first and then add first character -> reverse_string(s[1:]) + s[0]
# In case of NORMAL we add first character first and then do recursion -> len(strings[0]) + sum_of_lengths(strings[1:])

# ----------------- Q-5: Palindrome Recursive -----------------
# palindrome("kayak") # -> True
# "" and p -> both are palindrome -> True
def palindrome(s):
  if len(s) == 0 or len(s) == 1: # "" and p -> both are palindrome
    return True
  
#   We can also write like this
#   if len(s) <= 1: # "" and p -> both are palindrome
#     return True
  
  if s[0] != s[-1]: # first and last char of string not same return false
    return False
  return palindrome(s[1:-1]) # Removes 1st and last char of string
  
# n = length of string
# Time O(n^2); O(n) for recursive calls and O(n) for string slicing in each iteration
# Space O(n^2); O(n) for recursive calls and O(n) for string slicing in each iteration

# ----------------- Q-6: Fibonacci Recursive -----------------
# fibonacci(4); # -> 3
# fibonacci(0) -> 0 and fibonacci(1) -> 1
# calculate the sum of previous two numbers
def fibonacci(n):
  if n == 0:
    return 0

  if n == 1:
    return 1

  # We can also write like this
  # if n == 0 or n == 1:
  #   return n

  return fibonacci(n-1) + fibonacci(n-2)

# n = number
# Time O(2^n); will spread like a tree in both sides and exponential time complexity
# Space O(n); for storing distinct n numbers on recursive calls stack
# will push and pop from call stack but overall numbers on stack will always be n
# Space will be the height of tree which is n, so O(n) space complexity






































# =================== EXHAUSTIVE RECURSION ===================
# When we have to explore all possible combinations of a problem, we can use exhaustive recursion.

# NOTE:
# Subsets are unordered, but permutations are ordered.

# ------------- Q-7: SUBSETS --------------------
# return a 2D list where each sublist represents one of the possible subsets of the list.

# subsets(['a', 'b', 'c']) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]

# Given n items, there are 2^n subsets. 
# For each item we make 2 choices: include it or not.

#  1                                 []
#                                  /    \
#  A  *2                         []      [A]
#                              /    \    /     \
#  B  *2                    []     [B]  [A]    [A,B]
#                          /  \    /  \   /  \    /    \
#  C  *2                 []  [C] [B] [B,C] [A] [A,C] [A,B] [A,B,C]
#
#  n levels, each item doubles the choices  ->  2 * 2 * 2 = 2^n subsets

# Time Complexity : O(2^n)
# Space Complexity : O(2^n), to store all subsets

# subsets -> [ 'a' ]
def subsets(elements):
  if len(elements) == 0:
    return [ [] ] # base case for empty array [ [] ]

  first = elements[0] # a
  sub_without_first = subsets(elements[1:])  # [[]]

  sub_with_first = [] # [ [a] ]
  for sub in sub_without_first:
    sub_with_first.append([ first, *sub ])

  # [ [], [a]]
  return sub_without_first + sub_with_first

# O(2^n), O(2^n)


# ------------- Q-8: PERMUTATIONS --------------------
# return a 2D list where each sublist represents one of the possible permutations of the list.

# permutations(['a', 'b', 'c']) # -> 
# [ 
#   [ 'a', 'b', 'c' ], 
#   [ 'b', 'a', 'c' ], 
#   [ 'b', 'c', 'a' ], 
#   [ 'a', 'c', 'b' ], 
#   [ 'c', 'a', 'b' ], 
#   [ 'c', 'b', 'a' ] 
# ] 

# Given n items, there are n! permutations. At each level we insert the next
# item into every possible position of the existing arrangements.

#                                  []
#                                   | 1
#                                  [A]
#                          *2  /          \
#                          [B,A]          [A,B]
#                      *3 / | \           / | \
#                C,B,A  B,C,A  B,A,C   C,A,B  A,C,B  A,B,C

#  n levels, each item multiplies the choices  ->  1 * 2 * 3 = n! permutations

# Time Complexity : O(n!)
# Space Complexity : O(n!), to store all permutations

# permutations(['a', 'b', 'c']) 
def permutations(items):
  if len(items) == 0:
    return [ [] ]

  first = items[0] # a
  perm_without_first = permutations(items[1:]) # [ [b,c], [c,b]  ]

  full_permutations = []
  for perm in perm_without_first:
    for i in range(len(perm) + 1):
      full_permutations.append( [*perm[:i] , first , *perm[i:]] )

  return full_permutations
  
# O(n!), O(n!)




# -------- Q-9: COMBINATIONS -----------
# return a 2D list representing all of the combinations of the specified length.

# create_combinations(["q", "r", "s", "t"], 2); # ->
# [
#   [ 'q', 'r' ],
#   [ 'q', 's' ],
#   [ 'q', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 't' ],
#   [ 's', 't' ]
# ]

# Inserting an element into every position of an existing permutation:
#
#   [[q,r,s],          ([q,r,s,t], 3)
#    [q,s,t],
#    [q,r,t]]              /        \
#                         /          \
#                ([r,s,t], 2)     ([r,s,t], 3)  <-
#                                  [[r,s,t]]
#
# The pair (perm, i) means: insert the new element at index i of perm.
# We loop i from 0 to len(perm), so each existing permutation spawns
# len(perm)+1 new permutations by placing the item in every slot.

# Function signature: (items, k)
# base cases:
#   1. if k == 0,                then return [[]]
#   2. if k > items.length,      then return []

# Combinations: choose k items out of n (order does NOT matter).
#
#                     [[a]]
#                   ([a], 1)
#                  /         \
#         ([], 0)             ([], 1)
#
# n = length of items
# k = target size
#
#   C(n, k) = n! / ( k! * (n - k)! )  Binomial coefficient = "n choose k"
#
# Time / Space Complexity : O(n choose k)


# ["a", "b", "c"], 2)
def create_combinations(items, k):
  if len(items) < k:
    return []

  if k == 0:
    return [[]]

  first = items[0] # a
  combos_without_first = create_combinations(items[1:], k) # [ [b,c] ]

  combos_with_first = [] # [ [a,b], [a,c] ]
  partial_combos = create_combinations(items[1:], k-1) # [ [b], [c] ]
  for par in partial_combos:
    combos_with_first.append([ first, *par])

  return combos_with_first + combos_without_first
  
# O(n choose k), O(n choose k)


# --------------- Q-10: Grocery budget COMBINATION APPROACH -------------
# return all possible ways to purchase items without spending more than the given budget.

# grocery_budget([  
#   ('eggs', 5),
#   ('milk', 3),
#   ('butter', 3)
# ], 7) # ->
# [ 
#   [ 'eggs' ], 
#   [ 'butter', 'milk' ], 
#   [ 'milk' ], 
#   [ 'butter' ], 
#   [] 
# ] 


# n = # items
# b = budget

# Base Case:
#   1.) if no items and budget >= 0:   return [ [ ] ]
#   2.) if budget < 0:                 return [ ]
#
# Recursive Step:
#                        ( [E, M, B, G], 7 )
#                        /                   \
#                include E                 exclude E
#                   /                           \
#         ( [M, B, G], 2 )               ( [M, B, G], 7 )

# include E -> subtract E's cost from the budget and move to the next item
# exclude E -> keep the same budget and move to the next item

# Time:  ~O(2^n)
# Space: ~O(2^n)


def grocery_budget(grocery_list, budget):
  if budget < 0:
    return []

  if not grocery_list:
    return [ [] ]

  combos_without_first = grocery_budget(grocery_list[1:], budget)

  combos_with_first = []
  first_item_name, first_item_price = grocery_list[0]
  partial_combos = grocery_budget(grocery_list[1:], budget - first_item_price)
  for par in partial_combos:
    combos_with_first.append([first_item_name , *par])

  return combos_with_first + combos_without_first


# n = # of groceries
# Time: ~O(2^n)
# Space: ~O(2^n)


# ---------- Q-11: Lining up COMBINATION APPROACH with Permutations on combos_with_first -------------
# We need to add people to the waitlist for a popular restaurant, but space is limited.
# The function should return a 2D list containing all the possible orders
# by which the people can line up. A valid line must be filled up exactly to the capacity.

# lining_up(["jason", "jen", "cody", "vicky"], 3) # ->
# [ 
#   [ 'jason', 'jen', 'cody' ], 
#   [ 'jen', 'jason', 'cody' ], 
#   [ 'jen', 'cody', 'jason' ], 
#   [ 'jason', 'cody', 'jen' ], 
#   [ 'cody', 'jason', 'jen' ], 
#   [ 'cody', 'jen', 'jason' ], 
#   [ 'jason', 'jen', 'vicky' ], 
#   [ 'jen', 'jason', 'vicky' ], 
#   [ 'jen', 'vicky', 'jason' ], 
#   [ 'jason', 'vicky', 'jen' ], 
#   [ 'vicky', 'jason', 'jen' ], 
#   [ 'vicky', 'jen', 'jason' ], 
#   [ 'jason', 'cody', 'vicky' ], 
#   [ 'cody', 'jason', 'vicky' ], 
#   [ 'cody', 'vicky', 'jason' ], 
#   [ 'jason', 'vicky', 'cody' ], 
#   [ 'vicky', 'jason', 'cody' ], 
#   [ 'vicky', 'cody', 'jason' ], 
#   [ 'jen', 'cody', 'vicky' ], 
#   [ 'cody', 'jen', 'vicky' ], 
#   [ 'cody', 'vicky', 'jen' ], 
#   [ 'jen', 'vicky', 'cody' ], 
#   [ 'vicky', 'jen', 'cody' ], 
#   [ 'vicky', 'cody', 'jen' ] 
# ] 

# n = # of people
# k = capacity
# Time: ~O(n! / (n - k)!)
# Space: ~O(n! / (n - k)!)

# used combination approach but used permutation with combos_with_first

def lining_up(people, capacity):
  if len(people) < capacity:
    return []

  if capacity == 0:
    return [ [] ]

  first = people[0]

  partial_combos = lining_up(people[1:], capacity - 1)
  combos_with_first = []
  for par in partial_combos:
    for i in range(0, len(par) + 1):
      combos_with_first.append([ *par[:i], first, *par[i:] ])

  combos_without_first = lining_up(people[1:], capacity)

  return combos_with_first + combos_without_first

# n = # of people
# k = capacity
# Time: ~O(n! / (n - k)!)
# Space: ~O(n! / (n - k)!)


# --------------- Q-12: GRAPH All Paths (Source to Destination) SUBSETS ---------------
# return a list containing all possible paths that travel between the source and destination.

# graph = {
#   "a": ["b", "c", "d"],
#   "b": ["d"],
#   "c": ["d"],
#   "d": []
# }
# possible_paths(graph, "a", "d") # ->
# [
#   ["a", "b", "d"],
#   ["a", "c", "d"],
#   ["a", "d"]
# ]


#                           F []
#                          ^
#                        /
# [[ABD], [AD], [ACD]]  /       [ [BD] ]
#         A ----------------> B
#         |  \                |
#         |    \              |
#         v      \            v
#         C ------->--------> D
         # [ [CD] ]            [ [D] ]


# DFS 
# we are finding from A to D
# Base case: 
  # 1. when src:D and dst:D -> return [ [D] ]
  # 2. when src:F and dst:D -> return [ ] 
# node c -> [ [CD] ]
# node b -> [ [BD] ]
# node a -> [[ABD], [AD], [ACD]]

# n = # of nodes
# e = # of edges
# Time:  O(2^n) in the worst case (exponential number of paths)
# Space: O(2^n), to store all paths

def possible_paths(graph, src, dst):
  if src == dst:
    return [ [dst] ]

  paths = []
  for neighbor in graph[src]:
    neighbor_paths = possible_paths(graph, neighbor, dst) # node b -> [ [BD] ]
    for neighbor_path in neighbor_paths:
      paths.append([ src, *neighbor_path ]) # add to final list, # node b -> add a ->  [ [ABD] ]
      
  return paths

# O(2^n), O(2^n) 


# --------------- Q-13: Parenthetical Possibilities ---------------
# return a list containing all of the strings that could be generated by
# expanding all the parentheses of the string into its possibilities.

# parenthetical_possibilities("x(mn)yz") # ->
# [
#   "xmyz",
#   "xnyz"
# ]

# Each set of parentheses represents a choice of one character. For every
# choice inside the parentheses we recurse on the rest of the string.

#                  "x(mn)yz"
#                 /          \
#          x + "(m)..."   x + "(n)..."
#                |              |
#             "xmyz"         "xnyz"

# Base Case:
#   if string is empty -> return [ "" ]
#
# Recursive Step:
#   - If the string starts with '(', take every character inside the
#     parentheses as a choice, then prepend it to every possibility of the
#     remaining string (after the closing ')').
#   - Otherwise, take the first character and prepend it to every
#     possibility of the rest of the string.


# x(mn)yz -> xmyz, xnyz
def parenthetical_possibilities(s):
  if len(s) == 0:
    return ['']                          # -> ['']

  remaining, chars = get_options(s)      # get_options("x(mn)yz") -> ("(mn)yz", "x")  | get_options("(mn)yz") -> ("yz", "mn")
  suffixes = parenthetical_possibilities(remaining)  # recurse on remaining -> e.g. ("yz") -> ['yz']
  # chars = "mn", suffixes = ['yz']
  possibilities = []
  for char in chars:                     # char loops over each choice: 'm' then 'n'
    possibilities += [ char + suffix for suffix in suffixes]  # 'm'+'yz'->'myz', 'n'+'yz'->'nyz'

  return possibilities                   # -> ['myz', 'nyz']  ... finally -> ['xmyz', 'xnyz']


def get_options(s):
  if s[0] == '(':             # if the first element is (
    idx = s.index(')')        # find the index of )      -> "(mn)yz" gives idx = 4
    chars = s[1:idx]          # char = 1 till idx         -> "mn"
    remaining = s[idx + 1:]   # remaining idx + 1 to end  -> "yz"
    return ( remaining, chars )           # -> ("yz", "mn")
  else:
    chars = s[0]              # char = first element       -> "x"
    remaining = s[1:]         # remaining = next element after first -> "(mn)yz"
    return ( remaining, chars )           # -> ("(mn)yz", "x")


# n = length of string
# Time:  O(c^n), where c is the max number of choices in a parentheses group
# Space: O(c^n), to store all possibilities


# --------------- Q-14: Substituting Synonyms ---------------
# return a list containing all possible sentences that can be formed by
# substituting words of the sentence with their synonyms.

# sentence = "follow the yellow brick road"
# synonyms = {
#   "follow": ["chase", "pursue"],
#   "yellow": ["gold", "amber", "lemon"],
# }
# substitute_synonyms(sentence, synonyms) # ->
# [
#   'chase the gold brick road',
#   'chase the amber brick road',
#   'chase the lemon brick road',
#   'pursue the gold brick road',
#   'pursue the amber brick road',
#   'pursue the lemon brick road'
# ]

# Each word is a choice: if it has synonyms, every synonym is an option,
# otherwise the only option is the word itself. We recurse on the rest of
# the words and prepend every option to every sub-sentence.

#         ["follow", "the", "yellow", "brick", "road"]
#          choices: chase/pursue        gold/amber/lemon
#
#                  follow -> [chase, pursue]
#                       |  prepend to each sub-result
#                  the    -> [the]
#                       |
#                  yellow -> [gold, amber, lemon]
#                       |
#                  brick  -> [brick]
#                       |
#                  road   -> [road]

# Base Case:
#   if no words left -> return [ [] ]   (one empty sentence)
#
# Recursive Step:
#   - find all options for the first word (synonyms or the word itself)
#   - recurse on the remaining words
#   - prepend each option to every sub-sentence


# sentence = "follow the yellow brick road"
# synonyms = {
#   "follow": ["chase", "pursue"],
#   "yellow": ["gold", "amber", "lemon"],
# }

def substitute_synonyms(sentence, synonyms):
  words = sentence.split(' ')                             # ['follow','the','yellow','brick','road']
  subarrays = generate(words, synonyms)                   # [['chase','the','gold','brick','road'], ...]
  return [ ' '.join(subarray) for subarray in subarrays ] # join each back into a sentence

def generate(words, synonyms):
  if len(words) == 0:                             # base case -> [[]]
    return [[]]

  first_word = words[0]                                # 'follow'
  remaining_words = words[1:]                           # ['the','yellow','brick','road']
  
  subarrays = generate(remaining_words, synonyms)    # all combos of the rest
  # for 'follow' call, subsentences =
  # [ ['the','gold','brick','road'], ['the','amber','brick','road'], ['the','lemon','brick','road'] ]

  if first_word in synonyms: # word has synonyms -> each is a choice
    result = [] # 'chase' then 'pursue'
    for synonym in synonyms[first_word]:
      # chase -> ['chase','the','gold','brick','road'], ['chase','the','amber','brick','road'], ...
        # pursue -> ['pursue','the','gold','brick','road'], ['pursue','the','amber','brick','road'], ...
      result += [ [synonym, *subarray] for subarray in subarrays ]
    return result
  else:  # no synonyms -> only one choice (the word itself)
    return [ [first_word, *subarray] for subarray in subarrays]
    # e.g. 'the'  -> ['the','gold','brick','road'], ['the','amber','brick','road'], ...
      # e.g. 'road' -> ['road']   (base sub was [], so result is just [['road']])
  
# n = # of words in the sentence
# c = max # of synonyms for a word
# Time:  O(c^n), to build every combination
# Space: O(c^n), to store all sentences


# ------------- Q-15: WORD SEARCH --------------------
# Given a grid of letters, can we spell out the word by moving
# up / down / left / right between neighbouring cells?
# The same cell may NOT be used twice within one path.

# grid = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word_search(grid, "ABCCED") # -> True
# word_search(grid, "SEE")    # -> True
# word_search(grid, "ABCB")   # -> False, that would reuse the first B

# this is BACKTRACKING on a grid, which is DFS plus an UNDO step

# the island_count style of DFS marks a cell visited and never looks back,
# because it only cares whether a cell was reached at all.
# here a cell blocked on one path may be REQUIRED by a different path,
# so after exploring we must unmark it. that unmark is the backtrack.

# try every cell as a starting point, then at each step:
#   - off the grid, or wrong letter -> dead end, return False
#   - matched the last letter       -> success, return True
#   - otherwise mark the cell, try all 4 directions, then UNMARK it

# r = rows, c = columns, L = length of the word
# Time Complexity O(r * c * 4^L); every cell can start a search that branches 4 ways
# Space Complexity O(L); recursion depth is at most the length of the word

def word_search(grid, word):
  if not grid or not word:
    return False

  rows, cols = len(grid), len(grid[0])

  def explore(row, col, index):
    if index == len(word):    # matched every letter already
      return True

    if row < 0 or row >= rows or col < 0 or col >= cols: # walked off the grid
      return False

    if grid[row][col] != word[index]: # wrong letter, dead end
      return False

    original = grid[row][col]
    grid[row][col] = '#'      # mark visited so this path cannot reuse the cell

    found = (explore(row + 1, col, index + 1) or   # down
             explore(row - 1, col, index + 1) or   # up
             explore(row, col + 1, index + 1) or   # right
             explore(row, col - 1, index + 1))     # left

    grid[row][col] = original # BACKTRACK, put the letter back for other paths

    return found

  for row in range(rows):
    for col in range(cols):
      if explore(row, col, 0):  # try starting the word at every cell
        return True

  return False

# O(r * c * 4^L), O(L)
