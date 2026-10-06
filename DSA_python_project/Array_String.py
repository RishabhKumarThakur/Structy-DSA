# ==================== CHAPTER 2 - ARRAYS AND STRINGS ====================
# Array_String.py - 14 questions

# ==========  PREFIX SUM PATTERN =============
# Here we calculate the sum of prefix to the given array element

def prefix_sum(numbers):
  total = 0
  result = []

  for num in numbers:
    total += num
    result.append(total)

  return result
# O(n), O(n)

# NOTE:
# searching for an element in a list - O(n)
# searching for an item in a set - O(1)
# searching for a key in a dictionary hashmap (counter) - O(1)

# ---------- Q-1: prefix product -----------
# For example, the i-th result should be the product of all elements 0 to i:
# result[i] = numbers[0] * numbers[1] * numbers[2] * ... * numbers[i]

# prefix_product([4, 2, 1, 6, 3, 6]) # -> [ 4, 8, 8, 48, 144, 864 ] 

# total = 1
# Iterate over array and multiply each element with total and push total to result array

# Time: O(n); iterate over array
# Space: O(n); store in result

def prefix_product(numbers):
  total = 1
  result = []
  for num in numbers:
    total *= num
    result.append(total)
  return result

# O(n); O(n)


# ------ Q-2: Array, Set, Hashmap (Counter) --------
# array uses append
total = 0
prefix_sum = [0]   
prefix_sum.append(total)

# Set uses add
seen = set()
seen.add(total)

# HASHMAP (COUNTER) - Dictionary with default value of 0
from collections import Counter
nums = [-2, 1, 1, 1, -1, 1, 1, 1, 1]
seen = Counter(nums)
# seen -> Counter({1: 6, -2: 1, -1: 1})
# counts each element: 1 appears 6 times, -2 once, -1 once
seen[2] += 1                # update seen[index 2] with +1 



# ---------- Q-3: PREFIX SUM running sum ---------
# For example, the i-th result should be the sum of all elements 0 to i:
# result[i] = numbers[0] + numbers[1] + numbers[2] + ... + numbers[i]

# running_sum([4, 2, 1, 6, 3, 6]) # -> [ 4, 6, 7, 13, 16, 22 ] 
# running_sum([10, 5, -2, 1, 1]) # -> [ 10, 15, 13, 14, 15 ] 

# Take total of prefix till the current element
# add the total prefix sum and current element value
# save the added value to result array and update prefix sum
# iterate over array until end

# O(n); iterate over elements of array
# O(n); saving final values in result array

def running_sum(numbers):
  total = 0
  result = []

  for num in numbers:
    total += num
    result.append(total)

  return result

# O(n), O(n)

# ----------------- Q-4: Has subarray sum -----------
# The function should return a boolean indicating whether 
# or not there exists a subarray of numbers that sums to the given target.

# has_subarray_sum([1, 3, 1, 4, 3], 8) # -> True
# has_subarray_sum([1, 3, 1, 4, 3], 2) # -> False

# --- Approach - 1: Brute Force Nested Loops ----
# take i at start and j as i+1
# iterate j till end and calculate sum of subarray
# if not found increment i and same j= i+1 
# and iterate till end

# Time Complexity: O(n^3);  i loop, j loop, calculating subarray sum
# Space Complexity: O(1); not saving anything

# O(n^3), O(1)

# --- Approach - 2: Prefix sums ----
# Take prefix sum array and initialise with 0
# Find prefix sum array from original array
# take i at start and j as i+1 on prefix sum array
# iterate j till end 
# and check jth - ith element == target; 
# if yes found target from index i to j in original array
# if not found increment i and make j= i+1 
# and iterate till end on prefix sum array

# Time Complexity: O(n + n^2) = O(n^2)
# n -> calculating prefix sum
# n^2 -> i loop, j loop, calculating difference is O(1)
# n + n^2 -> n^2

# Space Complexity: O(n); prefix array creation but not saving anything

# O(n^2), O(n)

# --- Approach - 3: Prefix sum with SET ----
# Take prefix sum array and initialise with 0
# Find prefix sum array from original array
# Iterate over prefix array
# take complement = i - target
# check complement in set 
# if not add in set
# if found then return True found the target
# else return false at the end

# Time Complexity: O(n + n) = O(n)
# n -> calculating prefix sum
# n -> iterating over prefix array
# O(1) -> for set it takes constant time to add and peek

# Space Complexity: O(n + n) = O(n)
# n -> calculating prefix sum
# n -> for set

# O(n), O(n)

# --- Approach - 1: Brute Force Nested Loops ----
def has_subarray_sum(numbers, target_sum):
  for start in range(0, len(numbers)):
    for end in range(start + 1, len(numbers) + 1): # if array has only 1 element; so end +1
      current_sum = 0

      for i in range(start, end):
        current_sum += numbers[i]

      if current_sum == target_sum:
        return True

  return False
# O(n^3), O(1)

# --- Approach - 2: Prefix sums ----
def has_subarray_sum(numbers, target_sum):
  prefix_sum = [0]           # prefix sum array initialise with 0
  total = 0

  for num in numbers:        # creating prefix sum array
    total += num
    prefix_sum.append(total)

  for start in range(0, len(prefix_sum)):
    for end in range(start + 1, len(prefix_sum)):
      if prefix_sum[end] - prefix_sum[start] == target_sum:
        return True

  return False
  
# O(n^2), O(n)


# --- Approach - 3: Prefix sum with SET ----
def has_subarray_sum(numbers, target_sum):
  prefix_sum = [0]           # prefix sum array initialise with 0
  total = 0
  seen = set()               # taking seen set()

  for num in numbers:        # creating prefix sum array
    total += num
    prefix_sum.append(total)

  for start in prefix_sum:    # if (start - target_sum) in seen set, return true or add in set
    complement = start - target_sum
    if complement in seen:
      return True
    seen.add(start)

  return False
  
# O(n), O(n)


# -------- Q-5: subarray sum count -----------
# subarray_sum_count([1, 3, 1, 4, -2, 3], 5) # -> 3
# 📍subarray_sum_count([-2, 1, 1, 1, -1, 1, 1, 1, 1], 3) # -> 8

# --- Approach - 3: Prefix sum with SET ----
# Simply using count +1 instead of return False 
# will not work as array can have negative element 📍

# --- Approach - 4: Prefix sum with HASHMAP (COUNTER)  ----
# Take prefix sum array and initialise with 0
# Find prefix sum array from original array
# Iterate over prefix array
# take complement = start - target_sum
# count += seen[complement]         # add seen[complement] to count
# seen[start] += 1                # update seen[complement] with +1
# return count                      # return count

# Time Complexity: O(n + n) = O(n)
# n -> calculating prefix sum
# n -> iterating over prefix array
# O(1) -> for counter it takes constant time to add and peek

# Space Complexity: O(n + n) = O(n)
# n -> calculating prefix sum
# n -> for counter

# O(n), O(n)

# --- Approach - 4: Prefix sum with HASHMAP (COUNTER) ----
from collections import Counter

def subarray_sum_count(numbers, target_sum):
  prefix_sum = [0]           # prefix sum array initialise with 0
  total = 0
  seen = Counter()           # taking seen Counter()
  count = 0

  for num in numbers:        # creating prefix sum array
    total += num
    prefix_sum.append(total)

  for start in prefix_sum: 
    complement = start - target_sum # complement = start - target_sum
    count += seen[complement]       # add seen[complement] to count
    seen[start] += 1                # update seen[complement] with +1 

  return count                      # return count
# O(n), O(n)




























# ==========  DIVIDE AND CONQUER PATTERN =============

# ------------ Q-6: Merge Sort -----------
# numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
# merge_sort(numbers)
# # -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ] 

# numbers = [7, -30, -4, -1, 12, 0, 20]
# merge_sort(numbers)
# # -> [ -30, -4, -1, 0, 7, 12, 20 ] 

# --- Q-7: Merge 2 sorted array ---
# take merged array
# take 2 pointers. pointer1 for array 1, pointer2 for array 2
# compare pointer1 and pointer2
# if pointer1 < pointer2; add pointer1 element to merged; move pointer 1
# else; add pointer2 element to merged; move pointer 2
# return merged array

# a = length of array 1
# b = length of array 2
# Time O(a + b), iterate over array1 and array2
# Space O(a + b), save array1 + array2 in merge array
# O(a + b), O(a + b)

# here (a + b) = n
# so, O(n), O(n)

# ---- Q-6: Merge Sort ------
# Idea (3 steps):
# 1. DIVIDE  : split the array into two halves at the middle
# 2. CONQUER : recursively merge_sort each half until length <= 1 (already sorted)
# 3. COMBINE : merge the two sorted halves back into one sorted array

# How the array is split (length n, log n levels of splitting):
# [4, 6, 7, 3, 1, 2, 5, 8]
# [4, 6, 7, 3]      [1, 2, 5, 8]
# [4, 6] [7, 3]     [1, 2] [5, 8]
# [4][6] [7][3]     [1][2] [5][8]
# then merged back up in sorted order

# Time Complexity: O(n log n)
# log n -> number of levels (array halved each time)
# n     -> merging all elements at each level (Merge 2 sorted array )
# Space Complexity: O(n); temporary arrays used while merging

# ---- Q-6: Merge Sort ------
def merge_sort(nums):
  if len(nums) <= 1:          # base case: 0 or 1 element is already sorted
    return nums

  mid = len(nums) // 2            # DIVIDE: find the middle index
  left = merge_sort(nums[:mid])   # CONQUER: sort left half
  right = merge_sort(nums[mid:])  # CONQUER: sort right half

  return merge(left, right)      # COMBINE: merge the two sorted halves
# O(n log n), O(n)


# --- Q-7: Merge 2 sorted array ---
def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):  # pick the smaller front element
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])        # add any leftover elements
  result.extend(right[j:])
  return result
# O(n), O(n)



# ------- Q-8: combine intervals ----------

# Given two intervals:
# (1, 4) and (3, 7)
# The intervals overlap and
# should be combined into:
# (1, 7)

# intervals = [
#   (1, 4),
#   (12, 15),
#   (3, 7),
#   (8, 13),
# ]
# combine_intervals(intervals)
# -> [ (1, 7), (8, 15) ]

# we can combine (1, 4) and (3, 7) into (1, 7)
# we can combine (12, 15) and (8, 13) into (8, 15)

# sort the given intervals based on start of interval pair
# Take combine_intervals array and assign initial first interval pair
# now check for next interval pair in intervals, sorted_intervals[1:]
# if next interval pair overlaps, combine with last interval
# if next does not overlaps, add into combine_intervals array and increment last interval
# keep iterating over intervals until end
# return combine_intervals

# Time Complexity
# n = array length
# sort -> n * log(n)
# iterate over intervals - > n
# Time Complexity = (n * log(n)) + n = O(n * log(n))

# Space Complexity
# O(n) = to store intervals in combine interval array


def combine_intervals(intervals):
  sorted_intervals = sorted(intervals, key = lambda interval:interval[0] )
  # print(sorted_intervals) -> [(1, 4), (3, 7), (8, 13), (12, 15)] 

  combined = [sorted_intervals[0] ] # initialize with first pair from sorted_intervals

  for current_interval in sorted_intervals[1:]:
    last_start, last_end = combined[-1] # Take first and last interval pair
    current_start, current_end = current_interval 
    # last interval combined[-1] (1, 4) and current_interval (3, 7)

    if last_end >= current_start: 
      if last_end < current_end: # overlaps, then merge interval
        combined[-1] = (last_start, current_end)
    else:
      combined.append(current_interval) # does not overlaps, add into combine_intervals array
      
  return combined
  
# O(n * log(n)), O(n)


# ------- Q-9: minimum meeting rooms ----------
# Given meeting intervals, find the MINIMUM number of rooms needed
# so that no two overlapping meetings are put in the same room.

# meetings = [
#   (0, 30),
#   (5, 10),
#   (15, 20)
# ]
# min_meeting_rooms(meetings) # -> 2
# (0,30) overlaps both others, but (5,10) and (15,20) do not overlap
# so they can share the second room

# min_meeting_rooms([ (7, 10), (2, 4) ]) # -> 1   nothing overlaps
# min_meeting_rooms([]) # -> 0

# natural follow-up to combine_intervals, and it starts the same way: sort by start
# the difference is we do NOT merge them, we count how many run at the same time

# use a MIN-HEAP holding the END time of every meeting currently in a room
# the heap root is therefore the room that frees up SOONEST
# for each meeting, taken in start order:
#   if the earliest ending meeting is already finished, reuse that room -> pop
#   push this meeting's end time -> it now occupies a room
# the heap only shrinks right before it grows again, so it never gets smaller
# that means its final size IS the peak number of rooms

# n = number of meetings
# Time Complexity O(n log n); sorting, plus a push and maybe a pop per meeting
# Space Complexity O(n); every meeting could overlap and sit in the heap

import heapq

def min_meeting_rooms(meetings):
  if not meetings:
    return 0

  sorted_meetings = sorted(meetings, key = lambda meeting: meeting[0]) # sort by start
  in_use = []   # min-heap of END times of meetings currently in a room

  for start, end in sorted_meetings:
    if in_use and in_use[0] <= start:  # earliest room frees up before this starts
      heapq.heappop(in_use)            # reuse that room instead of opening a new one

    heapq.heappush(in_use, end)        # this meeting now occupies a room

  return len(in_use)  # heap never shrank below its peak -> rooms needed

# O(n * log(n)), O(n)




















# ==========  LEXICAL ORDER PATTERN =============


# --------------- Q-10: Lexical order ------------
#  Lexical Order is like "dictionary" order

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lexical_order("apple", "dock", alphabet) # -> True
# lexical_order("apple", "ample", alphabet) # -> False
# lexical_order("app", "application", alphabet) # -> True

# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# lexical_order("zoo", "dinner", alphabet) # -> True
# lexical_order("backs", "backdoor", alphabet) # -> True
# lexical_order("leaper", "leap", alphabet) # -> False

# n = length of shorter character
# Time Complexity = O(n)
# Space Complexity = O(1)

# given word_1 and word_2 and alphabet
# take max_length as length of longer string
# iterate through max_length
# find location of char_1 on alphabet
# find location of char_2 on alphabet
# if value_1 comes first, then True
# if value_2 comes first, then False
# in case both words are same and equal length
# O(n), O(1)

def lexical_order(word_1, word_2, alphabet):
  
  max_length = max( len(word_1), len(word_2) ) # length of longer string

  for i in range(0, max_length):
    
    # location of char_1 on alphabet
    value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf') 
    # location of char_2 on alphabet
    value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')

    if value_1 < value_2: # if value_1 comes first, then True
      return True
    elif value_2 < value_1: # if value_2 comes first, then False
      return False

  return True # in case both words are same and equal length
  
# O(n), O(1)


# --------- Q-11: detect dictionary ----------

# alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# detect_dictionary(dictionary, alphabet)

# dictionary = ["zoo", "tick", "tack", "door"]  # -> True
# dictionary = ["zoo", "tack", "tick", "door"]  # -> False

# Traverse through dictionary
# take current and next element of dictionary as word_1 and word_2
# check for lexical order on word_1 and word_2
# if any othe lexical order fails for words, return False
# finally return true all passed

# n -> max of length of word_1 and word_2
# k -> length of dictionary
# check lexical order of 2 words word_1 and word_2 -> # O(n), O(1)
# trace entire dictionary -> O(k)
# Time complexity -> O(n * k)

# Space complexity -> O(1)

def detect_dictionary(dictionary, alphabet):
  
  for i in range(0, len(dictionary) - 1):
    word_1 = dictionary[i] # current and next element of dictionary as word_1 and word_2
    word_2 = dictionary[i + 1] 

    if lexical_order(word_1, word_2, alphabet) == False:
      return False # if any othe lexical order fails for words, return False

  return True # finally return true all passed
# O(n * k), O(1)


# ---- Q-10: Lexical order -----
def lexical_order(word_1, word_2, alphabet):
  
  max_length = max( len(word_1), len(word_2) ) # length of longer string

  for i in range(0, max_length):
    
    # location of char_1 on alphabet
    value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf') 
    # location of char_2 on alphabet
    value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')

    if value_1 < value_2: # if value_1 comes first, then True
      return True
    elif value_2 < value_1: # if value_2 comes first, then False
      return False

  return True # in case both words are same and equal length
  
# O(n), O(1)


# ==========  MATRIX PATTERN =============


# ---------- Q-12: Spiral matrix ----------
# Return every element of a 2D matrix in spiral (clockwise) order.

# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# spiral_order(matrix) # -> [1, 2, 3, 6, 9, 8, 7, 4, 5]

# matrix = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8]
# ]
# spiral_order(matrix) # -> [1, 2, 3, 4, 8, 7, 6, 5]

# nothing clever here, it is pure boundary bookkeeping
# hold 4 boundaries: top, bottom, left, right
# walk ONE edge at a time, then shrink that boundary inward
#   left -> right along the top row,      then top moves down
#   top -> bottom along the right column, then right moves left
#   right -> left along the bottom row,   then bottom moves up
#   bottom -> top along the left column,  then left moves right
# the two extra if checks matter for non-square matrices:
# without them a single leftover row or column gets walked twice

# r = rows, c = columns
# Time Complexity O(r * c); every cell is visited exactly once
# Space Complexity O(1); not counting the output list

def spiral_order(matrix):
  if not matrix:
    return []

  result = []
  top, bottom = 0, len(matrix) - 1
  left, right = 0, len(matrix[0]) - 1

  while top <= bottom and left <= right:
    for col in range(left, right + 1):        # top row, left -> right
      result.append(matrix[top][col])
    top += 1

    for row in range(top, bottom + 1):        # right column, top -> bottom
      result.append(matrix[row][right])
    right -= 1

    if top <= bottom:                         # guard a single leftover row
      for col in range(right, left - 1, -1):  # bottom row, right -> left
        result.append(matrix[bottom][col])
      bottom -= 1

    if left <= right:                         # guard a single leftover column
      for row in range(bottom, top - 1, -1):  # left column, bottom -> top
        result.append(matrix[row][left])
      left += 1

  return result

# O(r * c), O(1)


# ---------- Q-13: Rotate image ----------
# Rotate an n x n matrix by 90 degrees CLOCKWISE, in place (no second matrix).

# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# rotate_image(matrix)
# # matrix -> [
# #   [7, 4, 1],
# #   [8, 5, 2],
# #   [9, 6, 3]
# # ]

# the trick: clockwise rotation = TRANSPOSE then REVERSE each row

# transpose = flip over the main diagonal, swap matrix[row][col] with matrix[col][row]
#   [1,2,3]      [1,4,7]
#   [4,5,6]  ->  [2,5,8]
#   [7,8,9]      [3,6,9]

# then reverse every row left to right
#   [1,4,7]      [7,4,1]
#   [2,5,8]  ->  [8,5,2]
#   [3,6,9]      [9,6,3]

# the inner loop starts at row + 1, not 0
# otherwise every pair is swapped twice and the transpose undoes itself

# n = side length of the square matrix
# Time Complexity O(n^2); we touch every cell
# Space Complexity O(1); all swaps happen in place

def rotate_image(matrix):
  n = len(matrix)

  for row in range(n):              # transpose over the main diagonal
    for col in range(row + 1, n):   # row + 1 so each pair is swapped only once
      matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

  for row in matrix:                # then reverse each row
    row.reverse()

  return matrix

# O(n^2), O(1)


# ------------- Q-14: Two Sum -----------------
# [2, 11, 7, 15], Target 9 -> [0,2]

# Brute Force - 2 for loops
# Time O(n^2), Space O(1)

# Optimised - Hash Map
# Store element : index in hash map
# if target - element in hashmap,
# return [index of element, hash_map[target - element]]
# Time O(n), Space O(n)

def Two_sum(elements, target):
  hash_map = {}

  for index, element in enumerate(elements):
    if target - element in hash_map: # if target - element is in hash map, we found the pair
      return [index, hash_map[target - element]]

    hash_map[element] = index # store element : index in hash map

  return
# Time O(n) for iterating through list
# Space O(n) for storing elements in hashmap
