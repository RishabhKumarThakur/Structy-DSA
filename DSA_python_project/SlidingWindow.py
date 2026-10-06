# ==================== CHAPTER 3 - TWO POINTERS AND SLIDING WINDOW ====================
# SlidingWindow.py - part 2 of 2 - 13 questions | chapter total 21 across TwoPointer.py, SlidingWindow.py

# ================ Fixed Window ==============
# n = size of array
# k = length of subarray

# Naive sliding window
# n-k = number of subarrays
# k = total work for each subarray
# Time Complexity = O(k * n-k) = O(nk)

# Optimized sliding window algorithm
# we are removing 1st element from the sliding window
# and we are adding element just after of sliding window
# so, total work for each subarray = 2
# n-k = number of subarrays
# 2 = total work for each subarray
# Time Complexity = O(2 * n-k) = O(n - k) = as n>k = O(n)
# Space Complexity = O(1)

def fixed_window_size_k(nums, k):
  current_sum = sum(nums[0:k])

  for i in range(0, len(nums)-k):
    current_sum -= nums[i]
    current_sum += nums[i+k]
    
  return 

# NOTE:
# number of subarray of size K = O(n)
# number of subarray of any size = O(n^2)

# If n >= k, what is O(nk) = O(nk) same as n>k
# If n >= k, what is O(nk - kk) = O(nk)  

# Sliding Window w/ Fixed Size K
# 1.) process first K elements into some "collection" -> current_sum = sum(nums[0:k])
# 2.) move window to the right
#     a.) remove trailing element from "collection" -> current_sum -= nums[i]
#     b.) add leading element to "collection" -> current_sum += nums[i+k]
# 3.) do the business logic (max, min, etc.) 



# --------- Q-9: Max subarray sum size K -----------
# max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3) # -> 15
# # [8,4,3] is the subarray of size 3 with the maximal sum

def max_subarray_sum_size_k(nums, k):
  current_sum = 0
  for i in range(0,k): # sum of sliding window
    current_sum += nums[i]
  
  max_sum = current_sum
  for i in range(0, len(nums) - k):
    current_sum -= nums[i] # removing 1st element from sliding window
    current_sum += nums[i+k] # adding last element to sliding window
    if current_sum > max_sum: # taking max_sum
      max_sum = current_sum
  return max_sum
# Time O(n), Space O(1)

# (1)
# Space O(1)
# current_sum = 0
#   for i in range(0,k): # sum of sliding window
#     current_sum += nums[i]

# instead we can use 
# current_sum = sum(nums[0:k])

# (2)
# if current_sum > max_sum: # taking max_sum
#       max_sum = current_sum

# instead we can use 
# max_sum = max(max_sum, current_sum)

def max_subarray_sum_size_k(nums, k):
  current_sum = sum(nums[0:k]) # sum of sliding window
  max_sum = current_sum

  for i in range(0, len(nums) - k):
    current_sum -= nums[i] # removing 1st element from sliding window
    current_sum += nums[i+k] # adding last element to sliding window
    max_sum = max(max_sum, current_sum)

  return max_sum
# Time O(n), Space O(1)

# --------- Q-10: Max subarray PRODUCT size K -----------
# max_subarray_product_size_k([4, 2, 1, -9, 8, 2, 3], 3) # -> 48
# # [8,2,3] is the subarray of size 3 with the maximal product

# we will use python math to calculate product
import math

def max_subarray_product_size_k(nums, k):
  current_product = math.prod(nums[0:k]) # product of sliding window
  max_product = current_product

  for i in range(0, len(nums) - k):
    current_product /= nums[i] # removing 1st element from sliding window
    current_product *= nums[i+k] # adding last element to sliding window
    max_product = max(max_product, current_product)

  return max_product
# Time O(n), Space O(1)

# --------- Q-11: Count subarray SUM size K -----------
# subarray_target_sum_size_k([2, 3, 2, 2, 3, 1, 3, 8, 5, 0, 2, 4], 7, 3) # -> 5
# The 5 subarrays of size 3 whose sum is 7 are:
#   [2,3,2]
#   [3,2,2]
#   [2,2,3]
#   [3,1,3]
#   [5,0,2]


def subarray_target_sum_size_k(nums, target, k):
  current_sum = sum(nums[0:k])

  count = 0 #Change-1 checking for count instead of max_sum
  if current_sum == target:
    count = 1

  for i in range(0, len(nums)-k):
    current_sum -= nums[i]
    current_sum += nums[i+k]
    
    if current_sum == target: #Change-2 checking for count instead of max_sum
      count += 1

  return count
# Time O(n), Space O(1)

# --------- Q-12: Has substring anagram -----------
# has_substring_anagram("greyhounds", "hoy") # -> True
# the substring "yho" is an anagram of "hoy"

# we use set() to store anagram_set and window_set
# and we use fixed size [len(anagram)] sliding window 

def has_substring_anagram(s, anagram):
  anagram_set = set(anagram)
  window_set = set(s[0:len(anagram)])

  if anagram_set == window_set:
    return True

  for i in range(0, len(s) - len(anagram)):
    window_set.remove(s[i])
    window_set.add(s[i + len(anagram)])

    if anagram_set == window_set:
      return True

  return False  
# Time O(n), Space O(1)

# --------- Q-13: Count substring anagram -----------
# count_substring_anagrams("tacoctacabcatt", "cat") # -> 4
# the 4 substrings that are an anagram of "cat" are:
#  - tac
#  - cta
#  - tac
#  - cat

# we cannot use set() to store anagram_set as string s can have duplicates 
# and set cannot store duplicate values (same value twice)
# We use Counter instead of set(), counter is a map
# Counter('gat') = {g:1, a:1, t:1}
# and we use fixed size [len(anagram)] sliding window 
from collections import Counter

def count_substring_anagrams(s, anagram):
  anagram_counter = Counter(anagram)
  window_counter = Counter(s[0:len(anagram)])

  count = 0
  if anagram_counter == window_counter:
    count = 1

  for i in range(0, len(s) - len(anagram)):
    window_counter[s[i]] -= 1 #Change-1 substract or add direct on map
    window_counter[s[i + len(anagram)]] += 1

    if anagram_counter == window_counter:
      count += 1

  return count  

# Time O(n), Space O(1) ❌
# Time O(n*k) = n as sliding window and k as need to compare 2 maps
# Space O(k) = k for space consumed by map
# Time O(n*k), Space O(k) ✅ 




















# ================ Variable Window ==============
# Here we if window sum is less than our target, increase window to right
# if window sum is more than our target, decrease window from left
# Time O(n), Space O(1)

# Sliding Window with Variable Size
# 1.) initialize start pointer to 0
# 2.) initialize window "collection"
# 3.) iterate end pointer through array
#     a.) (+) add leading element to collection
#     b.) (-) remove trailing elements from collection while constraint is violated
# 4.) do the business logic (count, max, min, find, etc...)


# --------- Q-14: Find subarray sum -----------
# find_subarray_sum([1, 2, 3, 7, 5], 12) # -> (1,3)
# the subarray that spans indices 1 to 3 is [2,3,7] and its sum is 12

# Need to return [start_index,end_index] of subarray
def find_subarray_sum(nums, target_sum):
  start = 0
  window_sum = 0
  
  for end in range(0, len(nums)):
    window_sum += nums[end] # keep increasing to right
    
    while window_sum > target_sum: # if greater than target, decrease window from left
      window_sum -= nums[start] 
      start += 1

    if window_sum == target_sum: # if matched target return
      return (start,end) 
  
# Time O(n), Space O(1)

# --------- Q-15: Longest subarray sum -----------
# longest_subarray_sum([1, 2, 1, 5, 2, 3, 10, 1, 9, 4, 3, 3, 7], 10) # -> 4
# the longest subarray with a sum of 10 is [2, 1, 5, 2] and its length is 4

# Need to return longest length of subarray
# at the matched target return max of current (end-start+1) and longest (initial -1)
def longest_subarray_sum(nums, target_sum):
  start = 0
  window_sum = 0
  
  longest_subarray_length = -1 # one of base case expects -1 instead of -inf
  # longest_subarray_length = float('-inf')
  
  for end in range(0, len(nums)):
    window_sum += nums[end] # keep increasing to right
    
    while window_sum > target_sum: # if greater than target, decrease window from left
      window_sum -= nums[start] 
      start += 1

    if window_sum == target_sum: # if matched target return
      current_subarray_length = end - start + 1
      longest_subarray_length = max(longest_subarray_length, current_subarray_length)
    
  return longest_subarray_length
# Time O(n), Space O(1)

# --------- Q-16: Longest unique substring -----------
# longest_unique_substring("abcabcqbb") # -> 4
# 'abcq' is the longest substring with unique characters and its length is 4

# Here we will take a hashmap, and add char : frequency
# keeping adding characters until frequency is 1 (i.e unique)
# If frequency is more that one decrease the window size
# keep track of longest substring
# return longest
from collections import Counter

def longest_unique_substring(s):
  start = 0
  window_counter = Counter() # window is counter here
  
  longest = 0

  for end in range(0, len(s)):
    leading_char = s[end]
    window_counter[leading_char] += 1 

    while window_counter[leading_char] > 1: # while check freq of each char is 1, if more decrese window size
      trailing_char = s[start]
      window_counter[trailing_char] -= 1 
      start += 1

    longest = max(end - start + 1, longest) 
    
  return longest

# Time O(n) for loop to iterate over entire string
# Space O(n) using hash map to store char:frequency
# Time O(n), Space O(n)

# --------- Q-17: Longest two char substring -----------
# longest_two_char_substring("xyzyyx") # -> 4
# 'yzyy' is the longest substring of 2 distinct characters and its length is 4

# Here we will take a hashmap, and add char : frequency
# keeping adding characters until length of map(counter) is 2 (i.e 2 distinct characters)
# If length of map(counter) is more than 2, decrease the window size
# Remove the char:freq from map(counter) if frequency is 0
# keep track of longest substring if length of map(counter) is 2 
# return longest
from collections import Counter

def longest_two_char_substring(s):
  start = 0
  window_counter = Counter()

  longest = 0

  for end in range(0, len(s)):
    leading_char = s[end]
    window_counter[leading_char] += 1

    while len(window_counter) > 2: # while length of map(counter) is more than 2, decrease window size
      trailing_char = s[start]
      window_counter[trailing_char] -= 1
      start += 1

      if window_counter[trailing_char] == 0: # if frequency of char is 0, remove it from map(counter)
        del window_counter[trailing_char]

    if len(window_counter) == 2: # if length of map(counter) is 2, then we can check for longest
      longest = max(end - start + 1, longest)

  return longest

# Time O(n) for loop to iterate over entire string
# Space O(1) using hash map to store char:frequency, 
             # but hasmap will never grow more than 2
             #  if it grows we decrease size
# Time O(n), Space O(1)

# --------- Q-18: Max ones with single flip -----------
# max_ones_with_single_flip("10110110") # -> 5
# flipping the second 0 will give us the longest streak of 1s

# Basically longest subtring problem 
# with no more than 1 zero in longest window
# we keep incereasing our window and keep incereasing zero_count
# If zero_count > 1, we decrease the window and keep decreasing zero_count
# keep track of longest substring
# return longest

from collections import Counter

def max_ones_with_single_flip(s):
  start = 0
  zero_count = 0
  
  longest = 0
  
  for end in range(0, len(s)):
    leading_char = s[end]
    if leading_char == '0':
      zero_count += 1

    while zero_count > 1: # while check freq of each char is 1, if more decrese window size
      trailing_char = s[start]
      if trailing_char == '0':
        zero_count -= 1
      start += 1

    longest = max(end - start + 1, longest) 
    
  return longest

# Time O(n) for loop to iterate over entire string
# Space O(1) just zero_count variable
# Time O(n), Space O(1)

# --------- Q-19: Count subarray product -----------
# count_subarray_product([2, 4, 3, 10], 31) # -> 8
# the 8 subarrays that have a product less than 31 are:
# [2] 
# [4] 
# [2, 4] 
# [3]
# [4, 3]
# [2, 4, 3]
# [3, 10]
# [10]


# Here we will use variable sliding window
# keep increaing window (multiply *) and getting window_product
# and if window_product > target_product and start <= end (for single element case)
# we will decrease window (divide /)
# keep track of count
# count += 1 ❌
      # for every end we can have many subarray with product <= target
      # so we use count += end - start + 1 ✅
# return count


def count_subarray_product(nums, target_product):
  start = 0
  window_product = 1

  count = 0

  for end in range(0, len(nums)):
    window_product *= nums[end]

    while window_product >= target_product and start <= end:
      # The start <= end; handles case single element >= target_product
      window_product /= nums[start]
      start += 1

    count += end - start + 1
    # count += 1 ❌
    # for every end we can have many subarray with product <= target
    # so we use count += end - start + 1 ✅
    
  return count
   
# Time O(n) for loop to iterate over entire string
# Space O(1) just zero_count variable
# Time O(n), Space O(1)

# --------- Q-20: Count substring at most k distinct -----------
# count_substring_at_most_k_distinct("gattc", 3) # -> 14
# there are 14 substrings that consist of at most 3 distinct chars:
#   gatt
#   attc
#   gat
#   att
#   ttc
#   ga
#   at
#   tt
#   tc
#   g
#   a
#   t
#   t
#   c

# variable sliding window
# same as longest substring of length k
# but instead of count of substring i.e count += 1 ❌
# we want substring  upto length (atmost) k i.e count = end - start + 1 ✅

from collections import Counter

def count_substring_at_most_k_distinct(s, k):
  start = 0
  window_counter = Counter()

  num_substrings = 0

  for end in range(0, len(s)):
    leading_char = s[end]
    window_counter[leading_char] += 1

    while len(window_counter) > k: # while length of counter is more than k, decrease window size
      trailing_char = s[start]
      window_counter[trailing_char] -= 1
      start += 1

      if window_counter[trailing_char] == 0: # if frequency of char is 0, remove it from map(counter)
        del window_counter[trailing_char]

    num_substrings += end - start + 1

  return num_substrings

# Time O(n) for loop to iterate over entire string
# Space O(k) hashmap will have atmost k character
# Time O(n), Space O(k)

# --------- Q-21: Count substring exactly k distinct -----------
# count_substring_exactly_k_distinct("gattc", 3) # -> 3
# there are 3 substrings that consist of 3 distinct chars:
#  gat
#  gatt
#  attc   

# variable sliding window 
# variable sliding window with len(counter) == k
# but == k is not possible to implement because of sliding nature of counter
# we can implement >k and <k, not == k
# so we will use different approach

# count substring ATMOST distinct  k -> <=k
# count substring EXACTLY distinct k -> <=k
# exactly(K) -> atmost(K) - atmost(k-1)

def count_substring_exactly_k_distinct(s, k):
  exactly_k = count_substring_at_most_k_distinct(s, k) - count_substring_at_most_k_distinct(s, k-1)
  return exactly_k

# Time O(n) for loop to iterate over entire string
# Space O(k) hashmap will have atmost k character
# Time O(n), Space O(k)
