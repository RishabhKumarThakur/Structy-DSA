# ==================== CHAPTER 1 - FOUNDATIONS AND BIG-O ====================
# Introduction.py - 11 questions

# Append = O(1) - constant time, example - nums.append(i) 
# Insert at beginning = O(n) - linear time, example - nums.insert(0, i)

# Code one after other in method = Add complexities
#   O(n) + O(n^2) -> O(n + n^2) -> O(n^2)

# code nested in method = Multiply complexities
#   O(n) * O(n) -> O(n*n) -> O(n^2)


# --------------- Q-1: Greetings ---------------------
def greet(s):
  return "hey " + s

# Max Value
# max_value([4, 7, 2, 8, 10, 9]) # -> 10
def max_value(nums):
  max = -float('inf')

  for num in nums:
    if num > max:
      max = num

  return max
# Time O(n) - for loop
# Space O(1) - no extra space to store values

# ----------------- Q-2: Longest word -----------------
# longest_word("what a wonderful world") # -> "wonderful"
def longest_word(sentence):
  words = sentence.split(" ") 
  longest = ""

  for word in words:
    if len(word) >= len(longest):
      longest = word

  return longest
# Time O(n + n) = O(n) -  split + for loop
# Space O(n) - space to store words list

# ----------------- Q-3: All even -----------------
# all_even([4, 90, 68, 6, -2]) # -> True
# check if any is odd, return false, else true
def all_even(nums):
  for num in nums:
    if num % 2 == 1:
      return False
  return True
# Time O(n) - for loop
# Space O(1) - no extra space to store values   

# ----------------- Q-4: Is Prime -----------------
# is_prime(2) -> True, is_prime(9) -> False
# check if any number divisible except 1 and itself, return false, else true
def is_prime(n):
  if n < 2: # incase n =1
    return False
  
  for i in range(2, n): # incase n = 2 to (last-1)
    if n % i == 0:
      return False
  return True
  

# range(2, 5) = 2,3,4 , range is exclusive in python does not include last
# floor from math to round up

# Time O(n) - for loop
# Space O(1) - no extra space to store values   

from math import sqrt, floor
def is_prime(n):
  if n < 2: # incase n =1
    return False
  
  for i in range(2, floor(sqrt(n)) + 1): # incase n = 2 to last
    if n % i == 0:
      return False
  return True
  
# Time Optimised O(sqrt(n)) - until sqrt(n) covers all n scenarios
# Space O(1) - no extra space to store values 

# ----------------- Q-5: Big-O Notation -----------------

# drop constants
#   O(4n) -> O(n)
#   O(999n) -> O(n)
#   O(n/2) -> O(n)

# drop smaller terms in a sum 
#   O(n + n^2) -> O(n^2)
#   O(n + n^4 + n^2) -> O(n^4)
#   O(n^4 - n^3) -> O(n^4)

# example = O(2n^3 + 3n^2 + 4n + 5) -> O(n^3)
# example = O(n^2/2 + 999) -> O(n^2)

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

# example = O(2^n + n^10) -> O(2^n) - exponential dominates polynomial

# example
def function4(n):
    nums = []
    for i in range(1, n):
        nums.append(i) # O(1) to append at the end of the list
    return nums

print(function4(10))
# Time: O(n) - for loop O(n) and append at the end O(1) = O(n*1) = O(n)
# Space: O(n) - we are storing n-1 numbers in the list, so space is proportional to n

def function4(n):
    nums = []
    for i in range(1, n):
        nums.insert(0, i) # O(n) to insert at the beginning of the list
    return nums

print(function4(10))
# Time: O(n^2) - for loop O(n) and insert at the beginning O(n) = O(n*n) = O(n^2)
# Space: O(n) - we are storing n-1 numbers in the list, so space is proportional to n

# Append = O(1) - constant time, example - nums.append(i) 
# Insert at beginning = O(n) - linear time, example - nums.insert(0, i)

# Code one after other in method = Add complexities
#   O(n) + O(n^2) -> O(n + n^2) -> O(n^2)

# code nested in method = Multiply complexities
#   O(n) * O(n) -> O(n*n) -> O(n^2)

# ------------- Q-6: FIZZ BUZZ -----------------
# FIZZ BUZZ - divisible by 3 fizz, divisible by 5 buzz, divisible by 3 and 5 fizzbuzz
# fizz_buzz(11) # -> [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11]
def fizz_buzz(n):
  result = []

  for i in range(1, n+1):
    #( first check for 3 and 5, then check for 3 and then 5, else it will never reach to 3 and 5 condition)
    if i % 3 == 0 and i % 5 == 0: 
      result.append("fizzbuzz")
    elif i % 3 == 0:
      result.append("fizz")
    elif i % 5 == 0:
      result.append("buzz")
    else:
      result.append(i)

  return result
# Time O(n) - for loop
# Space O(n) - to store all elements in result

# ------------- Q-7: PAIRS -----------------
#pairs(["a", "b", "c", "d"]) # ->
# [
#    ["a", "b"],
#    ["a", "c"],
#    ["a", "d"],
#    ["b", "c"],
#    ["b", "d"],
#    ["c", "d"]
# ]
def pairs(elements):
  result = []

  for i in range(0, len(elements)):
    for j in range(i+1, len(elements)):
      pair = [elements[i], elements[j]]
      result.append(pair)

  return result
# Time O(n^2) - 2 nested for loop
# Space O(n^2) - to store result O(n) and pair O(n)



# ------------ Q-8: Large Big-O examples ------------

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


# --- Q-9: Exponential O(2^n) example ---
# Time:  O(2^n)
# Space: O(n)   (recursion stack depth)

# def foo(n):
#   if n == 1:
#     return
#   foo(n - 1)
#   foo(n - 1)

# Each call branches into 2 recursive calls, so the number of
# calls roughly doubles at every level -> O(2^n).
#
#                          (4)
#                  /                 \
#               (3)                  (3)
#             /      \             /      \
#           (2)      (2)        (2)       (2)         *2
#          /   \    /   \      /   \     /   \
#        (1)  (1) (1)  (1)   (1)  (1)  (1)  (1)       *2
#                                                     :
#                         => 2^n  total calls


# --- Q-10: Exponential O(3^n) example ---
# Time:  O(3^n)
# Space: O(n)   (recursion stack depth)

# def bar(n):
#   if n == 1:
#     return
#   bar(n - 1)
#   bar(n - 1)
#   bar(n - 1)

# Each call branches into 3 recursive calls, so the number of
# calls roughly triples at every level -> O(3^n).
#
#                                  (4)
#                  /                |                \
#               (3)               (3)               (3)            *3
#            /   |   \         /    |   \         /    |   \
#         (2) (2) (2)      (2)  (2)  (2)     (2)  (2)  (2)         *3
#        /|\  /|\  /|\     /|\  /|\  /|\     /|\  /|\  /|\
#       111 111 111      111 111 111       111 111 111            *3
#                                                                 :
#                         => 3^n  total calls


# --- Q-11: Factorial O(n!) example ---
# Time:  O(n!)
# Space: O(n)   (recursion stack depth)

# def baz(n):
#   if n == 1:
#     return
#   for i in range(0, n):
#     baz(n - 1)

# The number of children shrinks by one at each level
# (n, then n-1, then n-2, ...), so the total calls grow like
# n * (n-1) * (n-2) * ... * 1  ->  O(n!).
#
#                                  (4)                            *4
#              /            |             |            \
#           (3)           (3)           (3)           (3)         *3
#         / | \         / | \         / | \         / | \
#       (2)(2)(2)     (2)(2)(2)     (2)(2)(2)     (2)(2)(2)       *2
#       /\ /\ /\      /\ /\ /\      /\ /\ /\      /\ /\ /\
#      11 11 11      11 11 11      11 11 11      11 11 11
#                         => n!  total calls





