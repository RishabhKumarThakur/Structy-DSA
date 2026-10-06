# ==================== CHAPTER 8 - LINKED LIST ====================
# LinkedList.py - 20 questions

# ==================== LINKEDLIST - 1  ====================


# Array - list of continious memory locations to store values of same type
# If we want to insert value in middle, we have to move next elements and causing O(n) time complexity

# Linked List - collection of nodes where each node has a value and a pointer to the next node
# we can insert value in middle by just changing previous and next pointer, causing O(1) time complexity

# ---------------- Q-1: LinkedList Traversal -----------------------
# Start with Head of the linked list
# take current pointing to head and keeping going next until end of list is reached (current is None) 

from curses.ascii import SO


class Node:
  def __init__(self,val):
    self.val = val
    self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> None

def print_list(head):
  current = head
  while current is not None:
    print(current.val)
    current = current.next

# Time O(n) iterate over entire list and space O(1)
print_list(a)

# > running script... 
# A 
# B 
# C 
# D 
# > finished in 26ms 

# Using Recursion
def print_list(head):
  if head is None: # base case
    return
  print(head.val) # print statement here will print in normal order
  print_list(head.next) # recursion case
  # print statement here will print in reverse order

# Time O(n) iterate over entire list and space O(1)
print_list(a)


# -------------- Q-2: Store linked list values ---------------------
# a -> b -> c -> d
# [ 'a', 'b', 'c', 'd' ]
# If we store values of list in array Space complexity will be O(n) to store values
# Time O(n) iterate over entire list and space O(n) to store values in array

# Iterative approach
def linked_list_values(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values

# Using Recursion
def linked_list_values(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None: 
    return
  values.append(head.val)
  _linked_list_values(head.next, values)
# Time O(n) iterate over entire list and space O(n) to store values in array

# -------------- Q-3: Sum linked list values ---------------------
# 2 -> 8 -> 3 -> -1 -> 7 = 19
def sum_list(head):
  sum = 0
  current = head # classic iteration of linkedlist
  while current is not None:
    sum += current.val
    current = current.next
  return sum
# O(n), O(1)
# O(n) to iterate over linked list
  
def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)
# O(n), O(n)
#  O(n) to iterate over linked list, O(n) for recursion call stack


# -------------- Q-4: Find in linked list ---------------------
# a -> b -> c -> d
# 'c' in linkedlist -> True
def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False
# O(n), O(1)
# O(n) to iterate over linked list

def linked_list_find(head, target):
  if head is None:
    return False

  if head.val == target:
    return True

  return linked_list_find(head.next, target)
# O(n), O(n)
#  O(n) to iterate over linked list, O(n) for recursion call stack

# -------------- Q-5: Get node value at given index in linked list ---------------------
# a -> b -> c -> d
# index is 2 : 'c'
def get_node_value(head, index):
  count = 0
  current = head
  while current is not None:
    if index == count:
      return current.val
    count += 1
    current = current.next
  return None
# O(n), O(1)
# O(n) to iterate over linked list

def get_node_value(head, index):
  if head is None:
    return None

  if index == 0:
    return head.val

  return get_node_value(head.next, index-1)
# O(n), O(n)
# O(n) to iterate over linked list, O(n) for recursion call stack

# -------------- Q-6: Reverse linked list ---------------------
# a -> b -> c -> d -> e -> f
# f -> e -> d -> c -> b -> a
# we take 3 pointers prev, current, next
# we make current.next point to prev
# keep incementing next, current, prev until current point to null, means end of linked list
# when we reach the end where current points null prev is the last element 
# and we return prev as new head

# - Using Iterative approach -
# STEP-1 Normal iteration of linked list
def reverse_list(head):
  current = head
  
  while current is not None:
    current = current.next
    
  return current

# STEP-2 change current.next to prev and assign prev
def reverse_list(head):
  prev = None
  current = head
  
  while current is not None:
    current = current.next
    current.next = prev
    
  return current

# STEP-3 store current.next in next
def reverse_list(head):
  prev = None
  current = head
  
  while current is not None:
    next = current.next
    current.next = prev
    
  return current

# STEP-4 incement prev and current
def reverse_list(head):
  prev = None
  current = head
  
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
    
  return current

# STEP-5 return prev as new head instead of current
def reverse_list(head):
  prev = None
  current = head
  
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
    
  return prev
# O(n), O(1)
# O(n) to iterate over linked list 

# - Using Recursive approach -
# STEP-1 Normal recursive traversal
def reverse_list(head):
  if head is None:
    return
  return reverse_list(head.next)
  
# STEP-2 Add prev to base and recursion case
def reverse_list(head, prev = None):
  if head is None:
    return prev
  return reverse_list(head.next, head) # if head.next is next, then head is prev

# STEP-3 Store head,next in next and update recursive case
def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  return reverse_list(next, head)

# STEP-4 Do the actual reversing by making head.next point to prev
def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)

# O(n), O(n)
# O(n) to iterate over linked list, O(n) for recursion call stack

# ------------ Q-7: zipper lists --------------
# a -> b -> c
# x -> y -> z
# a -> x -> b -> y -> c -> z
# we will take 3 pointers and a counter
# current_1 -> linkedlist 1, current_2 -> linkedlist 2, tail to trace
# we will increment count on each add to result linkedlist
# if count is even we will take from linkedlist-1 and odd from linkedlist-2
# if any linkedlist ends first we will add the remaining to result
# Time O(min(n+m)), as we will add remaining if one list ends so min of both linkedlist
# Space O(1) as the tail will trace without storing

# tail points -> head_1
# current_1 points -> head_1.next
# current_2 points -> head_2.next
# remember return the head_1 (not the tail)
def zipper_lists(head_1, head_2):
  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0

  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
       tail.next = current_2
       current_2 = current_2.next
    else:
      tail.next = current_1
      current_1 = current_1.next
    tail = tail.next
    count += 1

  if current_1 is not None:
    tail.next = current_1

  if current_2 is not None:
    tail.next = current_2
    
  return head_1
# Time O(min(n+m)), Space O(1)
# Time O(min(n+m)), as we will add remaining if one list ends so min of both linkedlist
# Space O(1) as the tail will trace without storing

# Using recursion
def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2

  if head_2 is None:
    return head_1

  next1 = head_1.next
  next2 = head_2.next

  head_1.next = head_2
  head_2.next = zipper_lists(next1, next2)

  return head_1
# Time O(min(n+m)), Space O(min(n+m))
# Time O(min(n+m)), as we will add remaining if one list ends so min of both linkedlist
# Space O(min(n+m)) for the recursion stack of the minimum list

# ----------- Q-8: Merge 2 sorted linkedlists -----------
# 5 -> 7 -> 10 -> 12 -> 20 -> 28
# 6 -> 8 -> 9 -> 25
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# we will take current_1 to trace linkedlist1
# we will take current_2 to trace linkedlist2
# We wil take dummy_head and tail to trace dummy_head
# if current_1 < current_2, add to tail.next increment tail and current_1
# else add to tail.next increment tail and current_2
# return dummy_head.next 
def merge_lists(head_1, head_2):
  dummy_head = Node(0)
  current_1 = head_1
  current_2 = head_2
  tail = dummy_head

  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1
      current_1 = current_1.next
    else:
      tail.next = current_2
      current_2 = current_2.next
    tail = tail.next
    
  if current_1 is not None:
    tail.next = current_1

  if current_2 is not None:
    tail.next = current_2

  return dummy_head.next
# Time O(min(n+m)), Space O(1)
# Time O(min(n+m)), as we will add remaining if one list ends so min of both linkedlist
# Space O(1) as the tail will trace without storing

# - Using Recursion -
def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2

  if head_2 is None:
    return head_1

  if head_1.val < head_2.val:
    current_1 = head_1.next
    head_1.next = merge_lists(current_1, head_2)
    return head_1
  else:
    current_2 = head_2.next
    head_2.next = merge_lists(head_1, current_2)
    return head_2
# Time O(min(n+m)), Space O(min(n+m))
# Time O(min(n+m)), as we will add remaining if one list ends so min of both linkedlist
# Space O(min(n+m)) for the recursion stack of the minimum list

# ----------- Q-9: UniValue List - All node values are same -----------
# 7 -> 7 -> 7 (True)
def is_univalue_list(head):
  head_value = head.val
  current = head

  while current is not None:
    if current.val != head_value:
      return False
    current = current.next

  return True
# O(n), O(1)
# O(n) to iterate over linked list

# - Using Recursion -
def is_univalue_list(head):
  head_value = head.val
  return _is_univalue_list(head, head_value)

def _is_univalue_list(head, head_value):
  if head is None:
    return True

  if head_value != head.val:
    return False

  return _is_univalue_list(head.next, head_value)
# O(n), O(n)
# O(n) to iterate over linked list, O(n) for recursion call stack

# ---- Q-10: longest streak: length of the longest consecutive streak of the same value ----------
# 5 -> 5 -> 7 -> 7 -> 7 -> 6
# longest streak of 7, number is 3
def longest_streak(head):
    
  longest_streak = 0
  current_streak = 0
  prev_value = None
  current = head
  
  while current is not None:
    if current.val == prev_value:
      current_streak += 1
    else:
      current_streak = 1
      prev_value =  current.val
      
    if current_streak > longest_streak:
      longest_streak = current_streak
    
    current = current.next

  return longest_streak
# O(n), O(1)
# O(n) to iterate over linked list

# ----------- Q-11: Remove Node from LinkedList -----------
# a -> b -> c 
# Remove b; a -> c
# return head of the list
def remove_node(head, target_val):
  if head.val == target_val: # Special case in remove node, if target is head itself
    return head.next         # Then, just move head next
    
  prev = None
  current = head

  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break # there can be multiple values matching target,
            # we just want to remove 1st matching value and then break
    prev = current # Moving previous ahead
    current = current.next  # Moving current ahead

  return head
# O(n), O(1)
# O(n) to iterate over linked list

# - Using Recursion -
def remove_node(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  head.next = remove_node(head.next, target_val)
  
  return head
# O(n), O(n)
# Time O(n) to iterate over linked list
# Space O(n) for recursion stack

# ----------- Q-12: Insert Node at a given index LinkedList -----------
# a -> b -> c -> d
# insert_node(a, 'x', 2)
# a -> b -> x -> c -> d
# return head of the list
# Keep iterating prev and current till one before index (index - 1)
# make prev point new Node and new node point next
def insert_node(head, value, index):
  if index == 0:           # Special case in remove node, if target is head itself
    new_head = Node(value) # Then, create a new node and make it new head and return
    new_head.next = head
    return new_head
  
  current = head
  count = 0

  while current is not None:
    if count == index - 1: # till one before index (index - 1)
      next = current.next  # we have current and next, create a new node,
      new_node = Node(value) # assign it between current and next
      current.next = new_node
      new_node.next = next

    count += 1
    current = current.next

  return head # return head
# O(n), O(1)
# O(n) to iterate over linked list

# - Using Recursion -
def insert_node(head, value, index, count = 0):
  if index == 0:             # Special case in remove node, if target is head itself
      new_head = Node(value) # Then, create a new node and make it new head and return
      new_head.next = head
      return new_head
  
  if head is None:
    return None

  if count == index - 1:
    next = head.next  # we have current and next, create a new node,
    new_node = Node(value) # assign it between current and next
    head.next = new_node
    new_node.next = next
    return

  insert_node(head.next, value, index, count + 1)
  return head

# O(n), O(n)
# Time O(n) to iterate over linked list
# Space O(n) for recursion stack




































# ==================== LINKEDLIST - 2  ====================

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

    

# ---------- Q-13: Linkedlist is palindrome ----------
# return a boolean indicating whether or not the linked list is a palindrome.

# a = Node(3)
# b = Node(2)
# c = Node(7)
# d = Node(7)
# e = Node(2)
# f = Node(3)

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

# 3 -> 2 -> 7 -> 7 -> 2 -> 3
# linked_palindrome(a) # True

# Traverse linkedlist and add all values to an array
# reverse the values array
# if values array == reverse values array , palindrome 

# values = ['a', 'b', 'c', 'd']
# values[::-1] = ['d', 'c', 'b', 'a']

# Time O(n) to iterate over linked list
# Space O(n) storing values in array

def linked_palindrome(head):
  values = []
  
  current = head
  while current:
    values.append(current.val)

    current = current.next

  return values == values[::-1]

# O(n), O(n)



# ---------- Q-14: middle value -----------
# return the value of the middle node in the linked list.

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# # a -> b -> c -> d -> e
# middle_value(a) # c

# If linked list is odd -> middle element
# If linked list is even -> 2nd middle element

# Approach - 1: Traverse linkedlist and save in array
# works for both even and odd linkedlist
# Traverse through linked list and save element in array
# round(middle point) in array is middle of linkedlist
# Time O(n) to iterate over linked list
# Space O(n) storing values in array

# Approach - 2: Use Slow/Fast pointer
# slow moves 1, fast moves 2
# when fast reaches end , slow id the middle of linkedlist
# works for odd linkedlist
# for even linkedlist when fast reaches null slow shows middle
# so slow shows end when fast either reaches end or null in linkedlist
# Time O(n) to iterate over linked list
# Space O(1) fast/slow pointer, no array

# Approach - 1: Traverse linkedlist and save in array
# works for both even and odd linkedlist
def middle_value(head):
  values = []

  current = head
  while current:
    values.append(current.val)

    current = current.next

  mid = len(values) // 2
  return values[mid]
# O(n), O(n)


# Approach - 2: Use Slow/Fast pointer
def middle_value(head):
  slow = head
  fast = head

  while not (fast is None or fast.next is None): 
    # order of condition is important, if fast is null then fast.next will give error
    slow = slow.next
    fast = fast.next.next

  return slow.val
# O(n), O(1)




# --------- Q-15: linkedlist cycle ------------
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')

# a.next = b
# b.next = c
# c.next = d
# d.next = b # cycle

# #         _______
# #       /        \
# # a -> b -> c -> d 

# linked_list_cycle(a)  # True

# Approach - 1: Traverse linkedlist and save in set
# keep doing next on nodes of linkedlist
# add values to set
# check before adding, if already next of node in set, cycle
# Time O(n) to iterate over linked list
# Space O(n) storing values in set


# Approach - 2: Use Slow/Fast pointer
# slow moves 1, fast moves 2
# if cycle exits, at somepoint fast pointer will overlap slow pointer
# Time O(n) to iterate over linked list
# Space O(1) fast/slow pointer, no array

# Approach - 1: Traverse linkedlist and save in set
def linked_list_cycle(head):
  nodes_set = set()
  current = head

  while current is not None:
    if current in nodes_set:
      return True
    nodes_set.add(current)
    
    current = current.next

  return False
# O(n), O(n)


# Approach - 2: Use Slow/Fast pointer
def linked_list_cycle(head):
  slow = head
  fast = head

  while not (fast is None or fast.next is None):
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True

  return False
# O(n), O(1)


# -------- Q-16: unduplicate sorted linked list --------

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# return a new linked list containing the original values, with duplicates removed.

# a = Node(4)
# b = Node(4)
# c = Node(6)
# d = Node(6)
# e = Node(6)
# f = Node(7)
# g = Node(7)

# a.next = b;
# b.next = c;
# c.next = d;
# d.next = e;
# e.next = f;
# f.next = g;

# # 4 -> 4 -> 6 -> 6 -> 6 -> 7 -> 7

# undupe_sorted_linked_list(a) # 4 -> 6 -> 7

# Approach: using dummy Node
#  dummy                 (tail builds the unique list)
#    ^
#   tail

# Take dummy node and tail pointing dummy node
# iterate through original undupe_sorted_linked_list
# if dummy node value != tail value , add in dummy node and increment tail
# else iterate next on undupe_sorted_linked_list
# finally we will have dummy node pointing unique linked list
# finally return node after dummy 

#  4 -> 4 -> 6 -> 6 -> 6 -> 7 -> 7  (current walks every node, X = skipped dup)
#                                ^
#                             current

#  dummy -> 4 -> 6 -> 7                 (tail builds the unique list)
#                    ^
#                  tail

# Time O(n) to iterate over linked list
# Space O(n) result dummy linkedlist need to generate

# Approach: using dummy node
def undupe_sorted_linked_list(head):
  current = head
  
  dummy = Node(None) # Take dummy node
  tail = dummy        # Tail pointing dummy node
  
  while current:
    # if dummy node value != tail value , add in dummy node and increment tail
    if current.val != tail.val:
      node = Node(current.val)
      tail.next = node
      tail = tail.next
      
    current = current.next

  return dummy.next # finally return node after dummy 
# O(n), O(n)  



# ------ Q-17: create linked list from array -------
# create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.

# create_linked_list(["h", "e", "y"])
# # h -> e -> y

# create_linked_list([1, 7, 1, 8])
# # 1 -> 7 -> 1 -> 8

# create_linked_list(["a"])
# # a

# create_linked_list([])
# # null

# Approach: using dummy Node
#  dummy                 (tail builds the unique list)
#    ^
#   tail


# Take dummy node and tail pointing dummy node
# iterate through original array
# for each element in array, create new node in dummy, move tail to next
# finally we will have dummy node pointing linked list
# finally return node after dummy 

# Time O(n) to iterate over array
# Space O(n) result dummy linkedlist need to generate

# Approach: using dummy node
def create_linked_list(values):
  dummy = Node(None)
  tail = dummy

  for val in values:
    node = Node(val)
    tail.next = node
    tail = tail.next

  return dummy.next
# O(n), O(n)   




# ------- Q-18: build a queue -----------
# Implement the enqueue and dequeue methods for the existing class. 
# The enqueue method should add a given value into the queue. 
# The dequeue should return and remove an item from the queue 
# following first-in, first-out order.


# queue = Queue()
# queue.enqueue("a")
# queue.size # -> 1
# queue.dequeue() # -> a
# queue.enqueue("b")
# queue.enqueue("c")
# queue.size # -> 2
# queue.dequeue() # -> b
# queue.dequeue() # -> c
# queue.size # -> 0


# enqueue O(1)
# dequeue O(1)

# Approach: Using head,tail 
# Initially we take head,tail and point to NULL
# when first enqueue point head,tail to 1st element
# when more enqueue, create node, tail points node, increment tail
# when dequeue comes, take head.val, remove by incrementing head
# when one element remain, after dequeue make head,tail reset point to NULL


# Time O(1)
# enqueue O(1)
# dequeue O(1)

# Space O(n) for every element we create new node

# Approach: Using head,tail 
# Node
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    

class Queue:
  # queue
  def __init__(self): 
    self.head = None # Initially we take head,tail and point to NULL
    self.tail = None # Initially we take head,tail and point to NULL
    self.size = 0

  
  # enqueue
  # when first enqueue point head,tail to 1st element
  # when more enqueue, create node, tail points node, increment tail
  # increment size of queue
  def enqueue(self, val):
    if self.size == 0: # when first enqueue point head,tail to 1st element
      self.head = Node(val)
      self.tail = self.head
    else: # when more enqueue, create node, tail points node, increment tail
      node = Node(val)
      self.tail.next = node
      self.tail = self.tail.next

    self.size += 1


    
  # dequeue  
  # If size is 0, nothing to dequeue
  # when dequeue comes, take head.val, remove by incrementing head
  # when one element remain, after dequeue make head,tail reset point to NULL
  def dequeue(self):
   # If size is 0, nothing to dequeue
    if self.size == 0:
      return None
    
   # when dequeue comes, take head.val, remove by incrementing head
    value = self.head.val

    # when one element remain, after dequeue make head,tail reset point to NULL
    if self.size == 1: 
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next

    self.size -= 1
    return value

# Time O(1)
# size O(1)
# enqueue O(1)
# dequeue O(1)

# Space O(n) for every element we create new node
  


# -------- Q-19: Add 2 linked list ---------

# Say we wanted to compute 621 + 354 normally. The sum is 975:

#    621
#  + 354
#  -----
#    975

# Then, the reversed linked list format of this problem would appear as:

#     1 -> 2 -> 6
#  +  4 -> 5 -> 3
#  --------------
#     5 -> 7 -> 9

#   621
# + 354
# -----
#   975

# a1 = Node(1)
# a2 = Node(2)
# a3 = Node(6)
# a1.next = a2
# a2.next = a3
# # 1 -> 2 -> 6

# b1 = Node(4)
# b2 = Node(5)
# b3 = Node(3)
# b1.next = b2
# b2.next = b3
# # 4 -> 5 -> 3

# add_lists(a1, b1)
# # 5 -> 7 -> 9

# Approach: Using dummy
# Take dummy node and tail pointing dummy node
# take current_1 pointing head_1, current_2 pointing head_2
# iterate while current_1 is not none / current_2 is not none / carry == 1
#    val_1 = 0, if current_1 is none else current_1.val
#    val_2 = 0, if current_2 is none else current_2.val
#    sum = val_1 + val_2 + carry
#    carry = 1 if sum > 9 else 0 
#    digit = sum % 10
#    new node = node(digit), tail points new node and increment tail
#    if current_1 not none, increment current_1
#    if current_2 not none, increment current_2
# return dummy.next

# n = length of list 1
# m = length of list 2
# Time: O(max(n, m)) as we iterate over both linkedlist which ever is longer
# Space: O(max(n, m)) as we need to generate new node for digit


# Approach: Using dummy
def add_lists(head_1, head_2):
  dummy = Node(None)
  tail = dummy

  current_1 = head_1
  current_2 = head_2

  carry = 0
  while (current_1 is not None) or (current_2 is not None) or (carry == 1):
    val_1 = 0 if current_1 is None else current_1.val
    val_2 = 0 if current_2 is None else current_2.val
    sum = val_1 + val_2 + carry
    carry = 1 if sum > 9 else 0 # this wont work; carry = 0 if sum < 9 or 1
    digit = sum % 10

    node = Node(digit)
    tail.next = node
    tail = tail.next

    if current_1 is not None:
      current_1 = current_1.next

    if current_2 is not None:
      current_2 = current_2.next

  return dummy.next
  
# O(max(n, m)), O(max(n, m)) 
























# ==================== LINKEDLIST - 3  ====================


# ---------------- Q-20: LRU Cache -----------------------
# LRU = Least Recently Used. A cache with a fixed capacity.
# When it is full and something new arrives, throw away whatever was used longest ago.

# cache = LRUCache(2)      # capacity 2
# cache.put(1, 1)          # {1=1}
# cache.put(2, 2)          # {1=1, 2=2}
# cache.get(1)             # -> 1, and 1 is now the most recently used {2=2, 1=1}
# cache.put(3, 3)          # full -> evict key 2, it was least recently used, and add 3, {1=1, 3=3}
# cache.get(2)             # -> -1, it was evicted
# cache.get(3)             # -> 3

# so, INSERT AT TAIL AND REMOVE FROM HEAD

# both get and put must run in O(1), so we need two structures together:
#   HASHMAP            -> jump straight to any node by key in O(1)
#   DOUBLY LINKED LIST -> unlink and re-insert a node in O(1)

# why DOUBLY and not the singly linked list used everywhere above:
# to unlink a node you must fix the node BEFORE it, and in a singly linked
# list finding the previous node costs O(n), which breaks the whole point

# the list order IS the recency order:
#   head side = least recently used   -> evict from here
#   tail side = most recently used    -> insert here

# use a dummy head and dummy tail so the list is never empty
# and we never write special cases for "first node" or "last node"

# Time Complexity O(1) for get and for put; hashmap lookup plus pointer surgery
# Space Complexity O(capacity); one node per cached key

class DoubleNode:
  def __init__(self, key, val):
    self.key = key    # store the key too, needed to delete from the map on evict
    self.val = val
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.nodes = {}                     # key -> DoubleNode

    self.head = DoubleNode(None, None)  # dummy head, least recently used side
    self.tail = DoubleNode(None, None)  # dummy tail, most recently used side
    self.head.next = self.tail
    self.tail.prev = self.head

  def _remove_from_head(self, node):              # unlink a node from wherever it sits
    node.prev.next = node.next
    node.next.prev = node.prev

  def _add_to_tail(self, node):         # insert just before the dummy tail
    last = self.tail.prev
    last.next = node
    node.prev = last
    node.next = self.tail
    self.tail.prev = node

  def get(self, key):
    if key not in self.nodes:
      return -1

    node = self.nodes[key]
    self._remove_from_head(node)                  # it was just used, so
    self._add_to_tail(node)             # move it to the most recent side
    return node.val

  def put(self, key, val):
    if key in self.nodes:               # already cached -> drop the old node
      self._remove_from_head(self.nodes[key])
      del self.nodes[key]

    node = DoubleNode(key, val)
    self.nodes[key] = node
    self._add_to_tail(node)             # newest goes to the tail side

    if len(self.nodes) > self.capacity: # over capacity -> evict from the head side
      lru = self.head.next
      self._remove_from_head(lru)
      del self.nodes[lru.key]           # this is exactly why the node stores its key

# O(1) per operation, O(capacity)

