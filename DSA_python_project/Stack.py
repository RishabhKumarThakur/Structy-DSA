# ==================== CHAPTER 5 - STACK AND HEAP ====================
# Stack.py - part 1 of 2 - 7 questions | chapter total 14 across Stack.py, Heap.py


# SET is a DICTIONARY, STACK is an ARRAY

# Converting array into dictionary
chars = ["a", "e", "i", "o", "u"]
print(chars)          # ['a', 'e', 'i', 'o', 'u'] 
char_set = set(chars)
print(char_set)       # {'a', 'e', 'i', 'o', 'u'}

# stack
# append - Add in stack
# pop - remove from stack
# stack[-1] - Top of stack

# Array
# append - add in array
# "".join(array) -> convert array into string

# -------------- Q-1: reverse some chars --------------
# reverse_some_chars("computer", ["a", "e", "i", "o", "u"]) # -> 'cemputor'
# 'o', 'u', and 'e' are target characters in 'computer'
# so their relative order should be reversed to result in 'cemputor'

# reverse_some_chars("skateboard", ["a", "e", "i", "o", "u"]) # -> 'skatobeard'

# First fill the stack
# iterate over char in word, if char in array list, add to stack

# create result
# iterate char in word again, if normal char add to result
# if char in array list, pop from stack and add to result

# n = length of word
# m = length of array
# Time Complexity O(n + m); need to iterate of word and array list
# Space Complexity O(n + m); need to save result and array list on stack

def reverse_some_chars(s, chars):
  char_set = set(chars)
  stack = []

  for char in s:
    if char in char_set:
      stack.append(char)

  result = []
  for char in s:
    if char in char_set:
      result.append(stack.pop())
    else:
      result.append(char)

  return "".join(result)
# O(n + m),  O(n + m)


# ---------- Q-2: paired parentheses -------------
# return a boolean indicating whether or not the string has well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'

# paired_parentheses("(david)((abby))") # -> True
# paired_parentheses("()rose(jeff") # -> False
# paired_parentheses(")(") # -> False

# We will iterate over characters and maintain count
# if open parantheses '(' increment count
# if closed parantheses ')' decrement count
# case: if while decrementing if count = 0
#       return False, means not paired parantheses
# return final count == 0 check, count must be zero for paired parantheses

# Time Complexity O(n); need to iterate over word
# Space Complexity O(1); just maintaining count

def paired_parentheses(string):
  count = 0

  for char in string:
    if char == '(':
      count += 1

    elif char == ')':
      if count == 0:
        return False
      count -= 1

  return count == 0
# O(n), O(1)


# ------------ Q-3: befitting brackets --------
# The function should return a boolean indicating whether or not the string contains correctly matched brackets.
# You may assume the string contains only characters: ( ) [ ] { }

# befitting_brackets('(){}[](())') # -> True
# befitting_brackets('({[]})') # -> True
# befitting_brackets('[][}') # -> False

# We will iterate over characters and maintain stack
# if '( [ {'  -> push on the stack,
#                push closing brackets so later can check for match
# if ') ] }'  -> remove from the stack
# case-1: if while removing from stack there is mismatch (not same type of bracket)
#         return False
# case-2: if while iterating if we reached end 
#         return True
# case-3: if while iterating if we reached end , and still elements on stack
#         return False

# Time Complexity O(n); need to iterate over word
# Space Complexity O(n); maintain stack

def befitting_brackets(string):
  stack = []

  brackets = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
  }

  for char in string:
    if char in brackets:
      stack.append(brackets[char]) # push on the stack,
                                   # push closing brackets so later can check for match
    else:
      if stack and char == stack[-1]: # stack not empty 
                                      # if top of stack same as closing )]} pop
        stack.pop()
      else:
        return False              # not same, mismatch return False

  return len(stack) == 0         # reached end, still elements on stack, return false
# O(n), O(n)


# ---------- Q-4: decompress braces ----------
# decompress_braces("2{q}3{tu}v")
# -> qqtututuv 

# decompress_braces("ch3{ao}")
# -> chaoaoao

# iterate over string and push on stack
# push alphabets, numbers
# Ignore { braces
# when encountered } while iterating,
# create segment - pop char until get number (check order last element first)
#                 segment = pop char * number 
# push segment back on the stack
# when iteration reach end,
# create final decompress string
# by poping from stack last element first
# return the decompressed string

# G = brace groups
# C = regular chars

# Time Complexity: O(9^G * C)
# Space Complexity: O(9^G * C) ; output string will take that much space

# decompress_braces("ch3{ao}")
def decompress_braces(string):
  number_chars = '123456789'
  stack = []

  for char in string:
    if char in number_chars:
      stack.append(int(char)) # number_char is char '2', 
                              #int(char) 2 convert into number and push on stack
    else:
      if char == '}':          # popping logic
        
        # Build segment
        # keep poping and adding to segment until top of stack is number (int)
        segment = ''
        while not isinstance(stack[-1], int):
          popped = stack.pop()
          segment = popped + segment # popped + segment -> to check order last element first

        # multiply segment with number and push to stack
        num = stack.pop()
        stack.append(segment * num)
        
      elif char != '{':
        stack.append(char) # not number and } segment, push char to stack
        
  # After the end of for, stack has all element and segment
  # now return in order, last element first
  # print(stack) -> ['c', 'h', 'aoaoao'] 
  return ''.join(stack) # chaoaoao
  
# O(9^G * C), O(9^G * C)


# -------------- Q-5: nesting score -----------
# [] is worth 1 point
# XY is worth X + Y 
# [S] is worth S * 2 

# For example:
# [[][][]] is equivalent to (1 + 1 + 1) * 2 = 6

# nesting_score("[]") # -> 1
# nesting_score("[][][]") # -> 3
# nesting_score("[ [][][] ]") # -> 3 * 2 -> 6
# nesting_score("[ [][][] ] []") # -> 3 * 2 + 1 -> 7

# start with initial stack with 0; stack[0]
# when you see [, push 0 to stack
# when you see ], pop from stack 
#   if poped value is 0, add +1 to next top of stack
#   if poped value is non-0, multiply *2 to popped and add to next top of stack
# now stack will be remained with exactly 1 element, return that stack[0]

# n = length of string
# Time Complexity O(n); need to iterate over string input
# Space Complexity O(n); maintain stack

def nesting_score(string):
  stack = [0]             # start with initial stack with 0
  
  for char in string:
    if char == '[':       # when you see [, push 0 to stack
      stack.append(0)     
    else:
      popped = stack.pop() # when you see ], pop from stack 
      if popped == 0:      # if poped value is 0, add +1 to next top of stack
        stack[-1] += 1
      else:   # if poped value is non-0, multiply *2 to popped and add to next top of stack
        stack[-1] += popped * 2

  return stack[0]          # return only element in stack stack[0]

# O(n), O(n)












# ----------- MONOTONIC STACK -----------

# -------------- Q-6: next greater element (MONOTONIC STACK) -----------
# For each number, find the first number to its RIGHT that is bigger than it.
# If there is no bigger number, use -1.

# next_greater_element([2, 1, 2, 4, 3]) # -> [4, 2, 4, -1, -1]
# next_greater_element([1, 2, 3]) # -> [2, 3, -1]
# next_greater_element([3, 2, 1]) # -> [-1, -1, -1]

# MONOTONIC STACK = a stack we deliberately keep sorted (here: decreasing)
# we push INDEXES whose answer is still unknown, and they wait on the stack

# for each new number:
#   while the value at the stack top is SMALLER than current
#     -> current IS its next greater number, pop it and fill the answer
#   push current index, now it waits for its own answer
# whatever is still on the stack at the end never found a bigger number -> stays -1

# brute force is O(n^2), scanning right for every element
# here each index is pushed once and popped at most once -> O(n) total

# n = length of nums
# Time Complexity O(n); each index is pushed and popped at most once
# Space Complexity O(n); stack holds indexes waiting for an answer

def next_greater_element(nums):
  result = [-1] * len(nums)   # default answer is -1
  stack = []                  # holds INDEXES waiting for a bigger number

  for index, current in enumerate(nums):
    # current num is bigger than the value sitting at the top index
    while stack and nums[stack[-1]] < current:
      waiting = stack.pop()   # this index finally found its answer
      result[waiting] = current

    stack.append(index)           # current index now waits for its own answer

  return result               # indexes left on the stack keep -1

# O(n), O(n)


# -------------- Q-7: daily temperatures  (MONOTONIC STACK)  -----------
# How many days must you wait until a WARMER temperature?
# 0 if it never gets warmer.

# daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) # -> [1, 1, 4, 2, 1, 1, 0, 0]
# daily_temperatures([30, 40, 50, 60]) # -> [1, 1, 1, 0]
# daily_temperatures([30, 20, 10]) # -> [0, 0, 0]

# exactly the same monotonic stack as next_greater_element
# the ONLY difference is what we store when we pop:
#   next greater  -> result[waiting] = num          (the value)
#   days to wait  -> result[waiting] = i - waiting  (the distance)
# that is why the default is 0 here instead of -1

# n = length of temps
# Time Complexity O(n); each index is pushed and popped at most once
# Space Complexity O(n); stack holds indexes waiting for a warmer day

def daily_temperatures(temps):
  result = [0] * len(temps)   # default 0 = it never gets warmer
  stack = []                  # indexes waiting for a warmer day

  for index, current in enumerate(temps):
    while stack and temps[stack[-1]] < current:
      waiting = stack.pop()
      result[waiting] = index - waiting   # store the DISTANCE, not the value

    stack.append(index)

  return result

# O(n), O(n)


