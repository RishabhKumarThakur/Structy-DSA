# ==================== CHAPTER 4 - HASHING ====================
# Hashing.py - 10 questions

# Array - 
# Elements are placed in ordered way 
# Array can have duplicates
# and to lookup an element we need to traverse the whole array which takes O(n) time complexity.

# HashSet - 
# Elements are placed in Unordered way 
# hashset dont have duplicates
# and to lookup an element takes O(1) time complexity on average.
# Lookup, Insertion and Deletion - O(1) time complexity on average.

# HashMap -
# Elements are placed in Unordered way 
# hashset dont have duplicates
# It is a data structure that stores key-value pairs.
# and to lookup an Key takes O(1) time complexity on average.


# sets only store keys, but maps store key-value pairs

# ----------------- Q-1: Anagrams -----------------
# anagrams('restful', 'fluster') # -> True
# we will store count of each character in both strings 
# and match if count same true, else false 
def anagrams(s1, s2):
  return count_char(s1) == count_char(s2)

def count_char(s):
  count = {}

  for char in s:
    if char not in count:
      count[char] = 0

    count[char] += 1
    
  return count

# n = length of string1, m = length of string2
# Time O(n + m) - we need to iterate over both strings
# Space O(n + m) - need to save each character of both strings


# Using python inbuilt counter
# print(Counter("catss")) -> Counter({'s': 2, 'c': 1, 'a': 1, 't': 1})
from collections import Counter
from unittest import result

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)

# n = length of string1, m = length of string2
# Time O(n + m) - we need to iterate over both strings
# Space O(n + m) - need to save each character of both strings

# ----------------- Q-2: Most Frequent Char -----------------
# most_frequent_char('bookeeper') # -> 'e'
# we will store count of each character 
# and find which char has max count, 
# if two char has same count take the first one
def most_frequent_char(s):
  count = {}
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1

  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
    
  return best

# n = length of string
# Time O(n) - we need to iterate over string
# Space O(n) - need to save each character of string

# Using python inbuilt Counter
from collections import Counter 
def most_frequent_char(s):
  count = Counter(s)

  best = None
  for char in s:
    if best is None or count[char] > count[best]:
      best = char
    
  return best

# n = length of string
# Time O(n) - we need to iterate over string
# Space O(n) - need to save each character of string

# ----------------- Q-3: Pair Sum -----------------
# pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
# approach-1 : using 2 loops, Time O(n^2) and space O(1)

def pair_sum(numbers, target_sum):
  for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        return (i,j)
        
# approach-2 : use hashmap to store value:index
# next check target-value in hashmap, if not add
# if found return (found index , current index ) as result

def pair_sum(numbers, target_sum):
  hashmap = {}

  for index, value in enumerate(numbers):
    complement = target_sum - value
    
    if complement in hashmap: # check target-value in hashmap
      return (hashmap[complement], index) # if found return (found index , current index ) as result
    # if not add
    hashmap[value] = index # store value:index

# Time O(n) - we need to iterate over array
# Space O(n) - need to save values in hashmap

# ----------------- Q-4: Pair Product -----------------
# Same as pair sum but instead of sum we will check for product
# pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)

#complement = target_Product / value

# ----------------- Q-5: Intersection -----------------
# intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
# approach-1 : using 2 loops
# n= length of first array, m = length of second array
# Time O(n*m) and space O(min(n+m))
def intersection(a, b):
  result = []

  for item in a:
    if item in b:
      result.append(item)

  return result

# approach-2 : using hashSet
# store values of first array in hashSet 
# and then check if any value of second array is in hashSet, if yes add to result list
# n= length of first array, m = length of second array
# Time O(n + m) iterating both array and space O(n) to store values of first array in hashSet

def intersection(a, b):
  result = []
  items_set = set()

  for item in a:
    items_set.add(item)

  for element in b:
    if element in items_set:
      result.append(element)

  return result
# Time O(n + m) and space O(n)

#Note:
# Array, to add we use array.append(value) - O(1) time complexity
# hashset, to add we use hashset.add(value) - O(1) time complexity on average
# hashmap, to add we use hashmap[key] = value - O(1) time complexity on average

# Using python inbuilt 
def intersection(a, b):
  items_set = set(a) # Directly creating set from list a, time O(n) and space O(n)

  return [ element for element in b if element in items_set]
# Time O(n + m) and space O(n)



# ----------------- Q-6: Exclusive -----------------
# exclusive_items([4,2,1,6], [3,6,9,2,10]) # -> [4,1,3,9,10]

# approach-1 : using 2 loops
# n= length of first array, m = length of second array
# Time O(n*m) and space O(n+m)

def exclusive_items(a, b):
  difference = []
  
  for item in a:
    if item not in b:
      difference.append(item)

  for item in b:
    if item not in a:
      difference.append(item)

  return difference

# approach-2 : using hashSet
# store values of first and second array in hashSet 
# and then check if value of second array is in firsthashSet, if yes add to result list
# and then check if value of first array is in secondhashSet, if yes add to result list
# n= length of first array, m = length of second array
# Time O(n + m) iterating both array and space O(n+m) to store values of first and second array in hashSet

def exclusive_items(a, b):
  difference = []
  set_a = set(a)
  set_b = set(b)
  
  for item in a:
    if item not in set_b:
      difference.append(item)

  for item in b:
    if item not in set_a:
      difference.append(item)

  return difference
# Time O(n + m) and space O(n+m)

# ----------------- Q-7: All Unique -----------------
# all_unique(["q", "r", "s", "a"]) # -> True

# approach: using hashSet
# Set contains all unique values
# so we will add all values of array in hashSet 
# and then check if length of hashSet and array is same, if yes return true, else false
# Time O(n) iterating array and space O(n) to store values in hashSet
def all_unique(items):
  hashset = set(items)
  return len(hashset) == len(items)
# Time O(n) and space O(n)

# ----------------- Q-8: Intersection with Duplicates -----------------
# intersection_with_dupes(
#   ["a", "b", "c", "b"], 
#   ["x", "y", "b", "b"]
# ) # -> ["b", "b"]

# approach: using hashMap
# Create hashmap for both the arrays (can use python inbuilt Counter)
# for every element in first hashmap,
# check number of times using range from 0 to min(count in first hashmap, count in second hashmap) 
# and add that element in result list
# Time O(n + m) iterating both array and space O(n+m) to store values in hashMap

from collections import Counter

def intersection_with_dupes(a, b):
  result = []
  count_a = Counter(a)
  count_b = Counter(b)

  for element in count_a:
    for item in range(0, min(count_a[element], count_b[element])):
      result.append(element)
      
  return result
# Time O(n + m) and space O(n+m)

# ----------------- Q-9: Majority Element -----------------
# majority_element([1, 2, 1, 3, 1]) # -> 1
# majority element is the element which appears more than n/2 times in array
# approach: using hashMap
# Create hashmap to store count of each element
# then find which element has count more than n/2, if found return that element
# Time O(n) iterating array and space O(n) to store values in hashMap

def majority_element(items):
  count = {}
  majority_count = len(items) / 2

  for item in items:
    if item not in count:
      count[item] = 0
    count[item] += 1
  
  for item in count:
    if count[item] > majority_count:
      return item
# Time O(n) and space O(n)

# ----------------- Q-10: Group Anagrams -----------------
# group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# # -> [ ["eat", "tea", "ate"], ["tan", "nat"], ["bat"] ]
# anagrams are words made of the SAME letters, just reordered
# so they need a "signature" that is identical for every anagram
# approach: using hashMap where key = signature and value = list of words
# signature = the word sorted alphabetically, "eat" and "tea" both give "aet"
# every word with the same signature lands in the same bucket
# Time O(n * k log k) sorting each word and space O(n * k) to store all words

def group_anagrams(words):
  groups = {}

  for word in words:
    signature = ''.join(sorted(word)) # "eat" -> "aet", "tea" -> "aet"

    if signature not in groups:
      groups[signature] = []
    groups[signature].append(word)

  return list(groups.values())
# Time O(n * k log k) and space O(n * k)
# n = number of words, k = length of the longest word

# - Using character counts as the signature, avoids sorting -
# count the 26 letters instead of sorting
# "eat" and "tea" both give (1,0,0,0,1,0,...,1,...) which is the same tuple
# a list cannot be a dict key because it is mutable, so convert it to a tuple
# Time O(n * k) and space O(n * k)

def group_anagrams(words):
  groups = {}

  for word in words:
    count = [0] * 26  # one slot per lowercase letter

    for char in word:
      count[ord(char) - ord('a')] += 1 # 'a' -> index 0, 'b' -> index 1

    signature = tuple(count) # tuple is hashable, list is not

    if signature not in groups:
      groups[signature] = []
    groups[signature].append(word)

  return list(groups.values())
# Time O(n * k) and space O(n * k)

