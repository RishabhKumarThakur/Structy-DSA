# ==================== CHAPTER 13 - BIT MANIPULATION ====================
# BitManipulation.py - 2 questions

# ==================== BIT MANIPULATION ====================


# Every integer is stored as binary, and we can operate on those bits directly.

#   decimal 5  ->  binary 101
#   decimal 6  ->  binary 110

# The operators:
#   &   AND    1 only if BOTH bits are 1        5 & 6  = 101 & 110 = 100 = 4
#   |   OR     1 if EITHER bit is 1             5 | 6  = 101 | 110 = 111 = 7
#   ^   XOR    1 only if the bits DIFFER        5 ^ 6  = 101 ^ 110 = 011 = 3
#   ~   NOT    flips every bit
#   <<  shift left,  x << 1 doubles x           5 << 1 = 1010 = 10
#   >>  shift right, x >> 1 halves x            5 >> 1 = 10   = 2

# Three XOR facts that solve most bit interview questions:
#   x ^ x = 0     a number cancels itself out
#   x ^ 0 = x     zero changes nothing
#   order does not matter, so a ^ b ^ a = b


# ---------------- Q-1: Single Number ----------------
# Every number appears TWICE except one. Find the one that appears once.

# single_number([2, 2, 1]) # -> 1
# single_number([4, 1, 2, 1, 2]) # -> 4
# single_number([7]) # -> 7

# a hashmap of counts works, but it costs O(n) space
# the real question is asking for O(1) space, so count-based answers do not qualify

# XOR everything together and let the pairs destroy themselves:
#   4 ^ 1 ^ 2 ^ 1 ^ 2
# = 4 ^ (1 ^ 1) ^ (2 ^ 2)     order does not matter, so regroup the pairs
# = 4 ^ 0 ^ 0                 each pair cancels to 0
# = 4                         only the lonely number survives

# n = length of nums
# Time Complexity O(n); a single pass
# Space Complexity O(1); one running value, no extra structure

def single_number(nums):
  result = 0

  for num in nums:
    result ^= num   # pairs cancel each other, the lonely number survives

  return result

# O(n), O(1)


# ---------------- Q-2: Number of 1 Bits ----------------
# Count how many bits are set to 1 (also called popcount or Hamming weight).

# number_of_1_bits(11)  # -> 3   11 is 1011
# number_of_1_bits(128) # -> 1   128 is 10000000
# number_of_1_bits(0)   # -> 0

# --- Approach - 1: Check the last bit, then shift ---
# n & 1 is 1 exactly when the LAST bit is set
# n >> 1 throws that bit away and slides everything right
# repeat until nothing is left

# Time Complexity O(number of bits); 32 steps for a 32-bit number
# Space Complexity O(1)

def number_of_1_bits(n):
  count = 0

  while n:
    count += n & 1  # add 1 when the last bit is set
    n >>= 1         # drop the last bit

  return count

# O(bits), O(1)


# --- Approach - 2: Brian Kernighan trick ---
# n & (n - 1) clears the RIGHTMOST 1 bit and leaves everything else alone
#   n     = 1011
#   n - 1 = 1010    subtracting 1 flips the rightmost 1 and everything to its right
#   n & (n - 1) = 1010     the rightmost 1 is gone
# so the loop runs once per SET bit rather than once per bit

# Time Complexity O(number of set bits); much faster when the number is mostly zeros
# Space Complexity O(1)

def number_of_1_bits(n):
  count = 0

  while n:
    n &= n - 1    # knock out the rightmost 1 bit
    count += 1    # count how many times we had to do it

  return count

# O(set bits), O(1)
