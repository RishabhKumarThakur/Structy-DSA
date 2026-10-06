# ==================== CHAPTER 6 - BINARY SEARCH ====================
# BinarySearch.py - 10 questions

# Binary Search follows logarithmic time complexity

# 2^4 = 16
# Log(16) = 4
# meaning how many times divide by 2 to get 1
# 16 -> 8 -> 4 -> 2 -> 1 ; 4 times divide by 2 to get 1

# Log(128)
# 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1 ; 7 times divide by 2 to get 1
# Log(128) = 7

# Log represents repeated half path
# In binary search we keep dividing into half based on mid
# so, binary search is O(log(n)) - logarithmic time complexity

# Big-O Complexity Order (Worst to Best):
#
#   Worse
#     |  factorial    -> O(n!)
#     |  exponential  -> O(c^n) : O(2^n), O(3^n), ...
#     |  polynomial   -> O(n^c) : O(n^2), O(n^3), ...
#     |  linear       -> O(n)
#     |  logarithmic  -> O(log(n))
#     |  constant     -> O(1)  <- performance does not scale with input size
#   Better

# Linear search O(n) takes more time than binary search O(log(n)) 

# ------------ Q-1: Binary Search -----------
# binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) # -> 6
# binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> -1

# we take 2 pointer low at start and high at end of array
# low = 0
# high = len(numbers) - 1
# loop until low <= high
# take mid = (low + high) // 2   -> '/' gives decimal and '//' gives integer 
# if target < num[mid] ; high = mid - 1
# if target > num[mid]; low = mid + 1
# else return mid
# if nothing return -1

def binary_search(numbers, target):
  low = 0
  high = len(numbers) - 1

  while low <= high:
    mid = (low + high) // 2 # '/' gives decimal and '//' gives integer 

    if target < numbers[mid]: # left half
      high = mid - 1
    elif target > numbers[mid]: # right half
      low = mid + 1
    else:                      # target equal to mid
      return mid

  return -1                    # never found target

# Time O(log(n)), Space O(1)

# ------------ Q-2: Binary Search Index -----------
# return the index where the target can be found within the list. 
# If the target is not found in the list,
# then return the index where it should appear in the sorted order.

# binary_search_index([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) # -> 6
# binary_search_index([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> 8
# binary_search_index([0, 6, 8, 12, 16, 19, 20, 28], 8) # -> 2

# Same binary Search
# instead of returning -1 if nothing found
# return place it could have appeared if array is sorted
# means return low instead of -1,
# to show place it should have appeared if array is sorted

def binary_search_index(nums, target):
  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = (low + high) // 2

    if target < nums[mid]:
      high = mid - 1
    elif target > nums[mid]:
      low = mid + 1
    else:
      return mid

  return low # If the target is not found in the list,
             # then return the index where it should appear in the sorted order.

# Time O(log(n)), Space O(1)

# ----------- Q-3: Square root -----------
# square_root(16) # -> 4
# square_root(15) # -> 3.87 -> 3
# square_root(81) # -> 9

# Math.sqrt(n) ❌
# Math.pow(n, 0.5) ❌
# we are not going to use these

# square_root(15) # -> 3.87 -> 3
# we can code this by returning high pointer if nothing finds
# if we do not find number directly giving root
# returning high instead of -1

def square_root(n):
  low = 0
  high = n

  while low <= high:
    mid = (low + high) // 2
    if n < mid * mid:
      high = mid - 1
    elif n > mid * mid:
      low = mid + 1
    else:
      return mid

  return high
  
# Time O(log(n)), Space O(1)

# ---- Q-4: Left most index where target can be found ----------
# find_leftmost_index([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 3) # -> 2
# find_leftmost_index([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 4) # -> 5

# return the leftmost index where the target can be found in the list. 
# If the target does not exist in the list, then return -1.

# Iterate through array and take first occurence -> O(n)
# Binary search -> O(log(n))
# keep searching leftward even if target is found

# Instead of returning mid on else, go left and update leftmost
# high = mid -1
# leftmost = mid

def find_leftmost_index(nums, target):
  low = 0
  high = len(nums) - 1
  leftmost = -1 # initially assigned -1 if nothing returns -1

  while low <= high:
    mid = (low + high) // 2
    if target < nums[mid]:
      high = mid - 1 # keep going left
    elif target > nums[mid]:
      low = mid + 1 # keep going right
    else:
      high = mid - 1 # keep going left (Leftmost)
      leftmost = mid

  return leftmost
  
# Time O(log(n)), Space O(1)

# ---- Q-5: Right most index where target can be found ----------
# find_rightmost_index([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 3) # -> 4

# else:
#       low = mid + 1 # keep going right
#       rightmost = mid

def find_rightmost_index(nums, target):
  low = 0
  high = len(nums) - 1
  rightmost = -1 # initially assigned -1 if nothing returns -1

  while low <= high:
    mid = (low + high) // 2
    if target < nums[mid]:
      high = mid - 1 # keep going left
    elif target > nums[mid]:
      low = mid + 1 # keep going right
    else:
      low = mid + 1 # keep going right (Rightmost)
      rightmost = mid

  return rightmost
# Time O(log(n)), Space O(1)

# ---- Q-6: Count in sorted array ----------
# count_in_sorted_array([1,2,3,3,3,3,3,4,5,6,6,7,8,8,8,9], 3) # -> 5
# count_in_sorted_array([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 4) # -> 1

# return the number of times the target element appears in the list.

# left_most = find_leftmost_index(nums, target)
# right_most = find_rightmost_index(nums, target)
# count = right_most - left_most + 1

def count_in_sorted_array(nums, target):
  righ_most = find_rightmost_index(nums, target)
  left_most = find_leftmost_index(nums, target)

  if righ_most == -1 or left_most == -1:
    return 0
  else:
    return righ_most - left_most + 1

# Time O( log(n) + log(n) ) = O(log(n)) ,
# 2 log(n) for doing binary search twice for leftmost and rightmost

# Time O(log(n)), Space O(1)

# ------ Q-7: min in rotated sorted array -------
# min_in_rotated_sorted_array([6,7,9,10,2,3,4,5]) # -> 2
# the original array was [2,3,4,5,6,7,9,10] and was rotated 4 times

# min_in_rotated_sorted_array([24,25,30,12,15,16,20,21,23]) # -> 12

# Iterating through array to find min value -> O(n)
# Binary search  -> log(n)

# Try to find point of inflection, from where array is rotated
# if mid < high:
#   hi = mid (search left inclusive of mid)
# else: (mid > high)
#   low = mid + 1 (search right exclusive of mid)

# stop searching when low == high (that is minimum in sorted array)
# so our while loop of binary search (while low < high:)
# not regular (while low <= high:) because we want to stop when low == high

# as low == high at stopping condition
# return nums[low] (or return nums[high] same thing)

def min_in_rotated_sorted_array(nums):
  low = 0
  high = len(nums) - 1

  while low < high: # not <= as low == high is stoping condition
    mid = (low + high) // 2
    
    if nums[mid] < nums[high]:
      high = mid # search left inclusive of mid
    else:
      low = mid + 1 # search right exclusive of mid

  return nums[low] # stopped when low == high,
                   # can return nums[low] or nums[high]

# Time O(log(n)), Space O(1)

# ------ IMP Q-8: find in rotated sorted array -------
# find_in_rotated_sorted_array([5,6,7,9,2,3,4], 7) # -> 2
# the original array was [2,3,4,5,6,7,9] and was rotated 4 times

# find_in_rotated_sorted_array([24,25,30,12,15,16,20,21,22,23], 16) # -> 5

# If the target is not found in the list, then return -1

# find min_index in min_in_rotated_sorted_array
# do binary search using min_in_rotated_sorted_array to get min_index
# left_search = 0 to (min_index-1)
# right_search = min_index to [len(arr) - 1]
# if left_search == -1, return right_search (as -1 means not found)
# else return right_search


def find_in_rotated_sorted_array(nums, target):
  min_index = min_in_rotated_sorted_array(nums)
  
  left_search = binary_search(nums, target, 0, min_index - 1)
  right_search = binary_search(nums, target, min_index, len(nums) - 1)

  if left_search == -1:
    return right_search
  else:
    return left_search

# Time O(log(n)), Space O(1)

# -- Perform binary search --
def binary_search(nums, target, low, high):

  while low <= high:
    mid = (low + high) // 2

    if target < nums[mid]:
      high = mid - 1
    elif target > nums[mid]:
      low = mid + 1
    else:
      return mid

  return -1
  
# -- Minimum in rotated array --
def min_in_rotated_sorted_array(nums):
  low = 0
  high = len(nums) - 1

  while low < high:
    mid = (low + high) // 2
    
    if nums[mid] < nums[high]:
      high = mid
    else:
      low = mid + 1
      
  return low # returning low as index, not nums[low] value

# ---------- Q-9: Find peak ------------
# find_peak([4,5,6,3,1]) # -> 2
# 6 is a peak b/c it is greater than both of its neighbors 

# find_peak([2,5,7,10,12]) # -> 4
# 12 is a peak b/c it is greater than its single neighbor

# A "peak" is an element that is greater than both of its adjacent neighbors.
# If there are multiple peaks, you may return the index of any one of them.
# first and last element only need to be greater than their single neighbor.
# return index of peak

# To find peak, we look at slope
# If slope is to the right; go right
# else go left

# if nums[mid] < nums[mid + 1]
#     search right exclusive (low = mid + 1)
# else:  ( nums[mid] > nums[mid + 1] )
#     search left inclusive (high = mid)

# when low == high; we found the peak

def find_peak(nums):
  low = 0
  high = len(nums) - 1

  while low < high:                # not <= as low == high is stopping condition
    mid = (low + high) // 2

    if nums[mid] < nums[mid + 1]: # slope right 
      low = mid + 1               # search right exclusive
    else:
      high = mid                  # search left inclusive

  return low                      # return low or high as both low == high
                                  # we are returning index low/high, not element nums[low]

# Time O(log(n)), Space O(1)

# -------------- Q-10: Search sorted grid --------------------

# grid = [
#   [2, 3, 4,  5],
#   [11,12,12,15],
#   [17,20,23,25],
#   [30,31,32,50],
# ]
# search_sorted_grid(grid, 12) # -> True

# grid = [
#   [2, 3, 4,  5],
#   [11,12,12,15],
#   [17,20,23,25],
#   [30,31,32,50],
# ]
# search_sorted_grid(grid, 21) # -> False

# 1. search for row
# use low = first row; high = last row
# take mid row
# the target should be between first and last elemnt of mid row
# if not continue binary search on rows
# if no row found return false, target does not exixt
# O(log(n)); n = number of rows

# 2. search for target within row
# use low = first col; high = last col
# take mid col
# do ninary search on col to find target
# O(log(m)); m = number of col

# Time = O(log(n)) + O(log(m)) = O(log(n * m))


def search_sorted_grid(grid, target):
  row = search_for_row(grid, target)

  if row == -1:
    return False
  else:
    return search_target_within_row(grid, target, row)

#  -- 1. search for row --
def search_for_row(grid, target):
  low = 0
  high = len(grid) - 1

  while low <= high:
    mid = (low + high) // 2

    if target < grid[mid][0]:
      high = mid - 1
    elif target > grid[mid][-1]:
      low = mid + 1
    else:
      return mid
    
  return -1

# 2. -- search for target within row -- 
def search_target_within_row(grid, target, row):
  low = 0
  high = len(grid[0]) - 1

  while low <= high:
    mid = (low + high) // 2

    if target < grid[row][mid]:
      high = mid - 1
    elif target > grid[row][mid]:
      low = mid + 1
    else:
      return True

  return False

  
# O(log(m*n)) ; n = number f rows, m = number of columns
# O(log(m*n)), O(1)

