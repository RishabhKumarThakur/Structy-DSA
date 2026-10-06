# ==================== CHAPTER 3 - TWO POINTERS AND SLIDING WINDOW ====================
# TwoPointer.py - part 1 of 2 - 8 questions | chapter total 21 across TwoPointer.py, SlidingWindow.py

# ------------------ Q-1: Is Palindrome ------------
# is_palindrome("stables") # -> False
# is_palindrome("kayak") # -> True

# we will take 2 pointers, one from start, other from end
# we will compare values of start and end pointers
# if values same, increment start and decrement end
# keep doing until start and end meets

def is_palindrome(s):
  i = 0
  j= len(s) - 1

  while i < j:
    if s[i] != s[j]:
      return False

    i += 1
    j -= 1

  return True

# Time O(n/2) = O(n) we are traversing half using 2 pointers
# Space O(1)
# O(n), O(1)

# ------------------ Q-2: Uncompress ------------
# uncompress("2c3a1t") # -> 'ccaaat'
# uncompress("4s2b") # -> 'ssssbb'

# we will take 2 pointers (i & j), both from start
# we will increase j until we found alphanumeric value
# save result = int(s[i:j]) * s[j] and increment j, reset i to jth position
# keep doing until the end
# retuen result

def uncompress(s):
  numbers = '1234567890'
  result = ''
  i = 0
  j = 0

  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result += num * s[j]
      j += 1
      i = j

  return result

      
# Time O(n) we are traversing using 2 pointers ❌
# Space O(1) ❌

# 1000P1000Q here n=10, but output=2000
# 1a1b1c1d1e here n=10, but output=5
# so time and space complexity cannot be calculated based on n

# let say G is number of groups 1000P, 500Q
# ley say M is max number for any group, M=1000
# Time O(G*M), no. og group * max for any group
# Space O(G*M) we are saving lengthy output

# Time O(G*M), Space O(G*M)

# Note: can also use
# result = []
# result.append(num * s[j])
# and return ''.join(result)

def uncompress(s):
  numbers = '1234567890'
  result = []
  i = 0
  j = 0

  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result.append(num * s[j])
      j += 1
      i = j

  return ''.join(result)

# ------------------ Q-3: Compress ------------
# compress('ccaaatsss') # -> '2c3at3s'
# compress('ssssbbz') # -> '4s2bz'

# we will use 2 pointer (i & j) from start
# keeping increasing j until different character in string found
# count = j-i, and result = count + s[i], make reset i = j for next group
# special case -1: 
# if value of count is 1, no need to add count directly add s[i] in result
# special case -2: 
# if j is at end of string, consider outofindex as last place to calculate count 
# count = outofindex position - i, add result = count + s[i]
# return result

def compress(s):
  s += '!' # adding one element at end for special case-2
  result = []
  i = 0
  j = 0

  while j < len(s):
    if s[j] == s[i]:
      j += 1
      
    else:
      count = j - i
      
      if count == 1:
        result.append(s[i])
      else:
        result.append(str(count) + s[i])

      i = j

  return ''.join(result)
    

# Time O(n) we are traversing using 2 pointers
# Space O(n) to store results
# O(n), O(n)

# ------------- Q-4: five sort ------------
# Rearrange elements of the list such that all 5s appear at the end

# five_sort([5, 0])
# -> [0, 5] 

# five_sort([12, 5, 1, 5, 12, 7])
# -> [12, 7, 1, 12, 5, 5] 

# Take 2 pointer (i & j) from start and end
# from end while j is already 5, decrement j until non 5 element
# from start while i find new 5, if found swap i and j element, increment i
# after swap i++ and j--
# continue doing in while loop until i<j

def five_sort(nums):
  i = 0
  j = len(nums) - 1

  while i < j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    else:
      i += 1
      j -= 1

  return nums

# Time O(n) we are traversing half using 2 pointers
# Space O(1)
# O(n), O(1)

# ------------- Q-5: Is Subsequence --------------
# string_1 is a subsequence of string_2
# A subsequence is a string that can be formed by deleting 0 or more characters from another string.
# cant rearrange the order in string_2 to get subsequence

# is_subsequence("bde", "abcdef") # -> True
# is_subsequence("bda", "abcdef") # -> False
# is_subsequence("bda", "abcdef") # -> False

# we will have 2 pointer, 
# i will point start of string_1
# j will point start of string_2
# match value of i & j, if yes increment i & j
#  else increase only j
# if i has traverse entire string_1, return True
# else return false

def is_subsequence(string_1, string_2):
  i = 0
  j = 0

  while i < len(string_1) and j < len(string_2):
    # check values of i & j, if match increase i & j, else increase only j
    if string_1[i] == string_2[j]:
      i += 1
      j += 1
    else:
      j += 1

    # if i reach the end return True
    if i == len(string_1):
      return True

  return False

# n = length of string_1
# m = length of string_2
# Time O(m), as length of string_2 is bigger and will take more Time
# Space O(1)



# --------- Q-6: Token replace -----------

# tokens = {
#   '$LOCATION$': 'park',
#   '$ANIMAL$': 'dog',
# }
# token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# -> 'Walk the dog in the park!'

# keep output array
# use 2 pointer i and j; i = start and j = i + 1
# loop until end of string
# until $ first found in string s, add s[i] to output; keep incrementing i and j; i = i + 1; j = i +1
# after first # found, keep incrementing j = j + 1 until found another $
# now we have word between 2$, represented by key = s[ i: j+1 ]; j+1 as end is exclusive
# add tokens[key] in output; increment i = j + 1 and j = i + 1 as new start for search
# return the output joined by ''


# Time O(n); iterate over string
# Space O(n); saving in result array

def token_replace(s, tokens):
  output = []
  i = 0
  j = i + 1

  while i < len(s):
    if s[i] != '$':
      output.append(s[i])
      i = i + 1
      j = i + 1
    elif s[j] != '$':
      j = j + 1
    else:
      key = s[i: j+1]
      value = tokens[key]
      output.append(value)
      i = j + 1
      j = i + 1

  return ''.join(output)


# Time O(n); iterate over string
# Space O(n); saving in result array


# ---------- Q-7: Token Transform -----------

# tokens = {
#   '$LOCATION$': '$ANIMAL$ park',
#   '$ANIMAL$': 'dog',
# }
# token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# -> 'Walk the dog in the dog park!'

# -- similar to token replace,
#  but we need to call token_transform recursively until no more token found in output

# after getting key = s[i: j+1] instead of directly adding to output output.append(tokens[key])
# we will recursively call method with value and token (instead of string s in first time) to get evaluated_value
# replace tokens[key] with evaluated_value, so that if same token found again in string, 
#     we will get evaluated value instead of original value
# use evaluated_value to add in output 

      # key = s[i:j + 1]
      # value = tokens[key]
      # evaluated_value = token_transform(value, tokens)
      # tokens[key] = evaluated_value
      # output.append(evaluated_value)

# n = length of string s
# m = number of unique tokens 
# Time: ~O(n^m) ; n for iterating and m for each token we are calling recursively
# Space: ~O(n^m); we will have m recursive calls and each call will save result in output array of length n

def token_transform(s, tokens):
  output = []
  i = 0
  j = i + 1

  while i < len(s):
    if s[i] != '$':
      output.append(s[i])
      i = i + 1
      j = i + 1
    elif s[j] != '$':
      j = j + 1
    else:
      key = s[i:j + 1] # get the key between 2 $; j+1 as end is exclusive
      value = tokens[key] # get value for key from tokens
      evaluated_value = token_transform(value, tokens) # recursively call to get evaluated_value
      tokens[key] = evaluated_value # replace tokens[key] to avoid repeated calculation for same token
      output.append(evaluated_value) # use evaluated_value to add in output
      i = j + 1
      j = i + 1
  
  return ''.join(output)

# Time: ~O(n^m) ; n for iterating and m for each token we are calling recursively
# Space: ~O(n^m); we will have m recursive calls and each call will save result in output array of length n


# -------------- Q-8: trapping rain water  -----------
# heights are bars of a histogram, find how much rain water gets trapped between them.

# trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) # -> 6
# trapping_rain_water([4,2,0,3,2,5]) # -> 9
# trapping_rain_water([3,2,1]) # -> 0   water always spills off the side

#          #
#      #~~~##~#
#    #~##~#####
#    0102101321      ~ = trapped water

# KEY IDEA: water sitting on ONE bar = min(tallest on left, tallest on right) - own height
# so every bar needs to know the tallest bar on BOTH sides

# --- Approach - 1: Two pointers ---
# walk in from both ends instead of precomputing both maxes
# the SHORTER side is the one that limits the water level,
# so we can safely settle that side and move it inward,
# because a taller bar is guaranteed to exist on the other side

# n = number of bars
# Time Complexity O(n); one pass with two pointers
# Space Complexity O(1); only counters

def trapping_rain_water(heights):
  if not heights:
    return 0

  left = 0
  right = len(heights) - 1

  left_max = heights[left]
  right_max = heights[right]

  water = 0

  while left < right:
    if left_max < right_max:    # left side is shorter -> left_max limits the water
      left += 1
      left_max = max(left_max, heights[left])
      water += left_max - heights[left]     # fill this bar up to left_max
    else:                       # right side is shorter -> right_max limits the water
      right -= 1
      right_max = max(right_max, heights[right])
      water += right_max - heights[right]

  return water

# O(n), O(1)
