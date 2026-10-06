# ==================== CHAPTER 5 - STACK AND HEAP ====================
# Heap.py - part 2 of 2 - 7 questions | chapter total 14 across Stack.py, Heap.py

# Heap:
# Heap is binary tree data structure
# store items
# maintains order between items
# similar to binary search tree

# Binary Search Tree:
# - all values to the left of a parent must be less than the parent
# - all values to the right of a parent must be greater than or equal to the parent

# Min Heap:
# - parent nodes must be less than or equal to their children

# Max Heap:
# - parent nodes must be greater than or equal to their children

# Example:
# Binary Search Tree              Min Heap
#
#          12                         2
#         /  \                       / \
#        5    19                    5   12
#       / \   / \                  / \  / \
#      2   5 14  25               5  25 19 14
#
# - BST: left child < parent, right child >= parent (sorted left-to-right)
# - Min Heap: parent <= children, but no left/right ordering between siblings


# ---------------- Q-8: Heap stored as an array ----------------
# A heap is a complete binary tree, so we can store it in a simple array.
# For a node at index i:
#   parent      = (i - 1) // 2
#   left child  = 2 * i + 1
#   right child = 2 * i + 2
#
# Min Heap as tree            Same heap as array
#
#          2                  index : 0  1  2  3  4
#         / \                 value : 2  5  12 5  25
#        5   12
#       / \
#      5   25

# heap = []                 # start empty

# heap_insert(heap, 12)     # heap -> [12]
# heap_insert(heap, 5)      # heap -> [5, 12]
# heap_insert(heap, 2)      # heap -> [2, 12, 5]

# heap_pop(heap)            # returns 2, heap -> [5, 12]

# ---------------- Q-9: Insert into Min Heap (sift-up) ----------------
# - Add the new value at the END of the array (keeps the tree complete).
# - Then "bubble it up": while it is smaller than its parent, swap them.
# - Stop when it reaches the root or its parent is smaller/equal.
# Time O(log n) - at most the height of the tree, Space O(1)

def heap_insert(heap, value):
  heap.append(value)        # add at the end
  i = len(heap) - 1         # index of new value

  while i > 0:
    parent = (i - 1) // 2
    if heap[i] < heap[parent]:   # smaller than parent -> swap up
      heap[i], heap[parent] = heap[parent], heap[i]
      i = parent
    else:
      break
# O(log n), O(1)


# ---------------- Q-10: Delete (pop) min from Min Heap (sift-down) ----------------
# - The min is always the root (index 0). We want to remove and return it.
# - Move the LAST element to the root (keeps the tree complete).
# - Then "bubble it down": swap with its smaller child while it is bigger.
# - Stop when both children are larger/equal or we reach a leaf.
# Time O(log n) - at most the height of the tree, Space O(1)

def heap_pop(heap):
  if not heap:
    return None

  root = heap[0]
  last = heap.pop()         # remove last element
  if heap:                  # if list not empty, put last at root
    heap[0] = last
    i = 0
    n = len(heap)

    while True:
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = i

      if left < n and heap[left] < heap[smallest]:
        smallest = left
      if right < n and heap[right] < heap[smallest]:
        smallest = right

      if smallest == i:     # already in correct spot
        break

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest

  return root
# O(log n), O(1)


# ---------------- Q-11: Kth largest element ----------------
# nums = [3, 2, 1, 5, 6, 4], k = 2  ->  5  (2nd largest)
#
# Trick: to find the Kth LARGEST, use a MIN-heap of size k.
# - Keep only the k biggest values seen so far in the heap.
# - The root (smallest of those k) is exactly the Kth largest.
# - For each number: push it, and if heap grows past k, pop the smallest.
# Time O(n log k), Space O(k)

import heapq

def kth_largest(nums, k):
  heap = []
  for n in nums:
    heapq.heappush(heap, n)
    if len(heap) > k:
      heapq.heappop(heap)   # drop the smallest, keep k biggest
  return heap[0]            # root = Kth largest
# O(n log k), O(k)
# Time O(n log k): we loop over all n numbers, and each push/pop on a heap
#   of size k costs O(log k) (height of a heap with k elements).
# Space O(k): the heap never holds more than k elements at a time.


# ---------------- Q-12: Kth smallest element ----------------
# nums = [3, 2, 1, 5, 6, 4], k = 2  ->  2  (2nd smallest)
#
# Trick: to find the Kth SMALLEST, use a MAX-heap of size k.
# - Python's heapq is a min-heap, so negate values to fake a max-heap.
# - Keep only the k smallest values seen so far in the heap.
# - The root (largest of those k) is exactly the Kth smallest.
# Time O(n log k), Space O(k)

import heapq

def kth_smallest(nums, k):
  heap = []
  for n in nums:
    heapq.heappush(heap, -n)  # negate -> max-heap behaviour
    if len(heap) > k:
      heapq.heappop(heap)     # drop the largest, keep k smallest
  return -heap[0]             # root = Kth smallest
# O(n log k), O(k)
# Time O(n log k): we loop over all n numbers, and each push/pop on a heap
#   of size k costs O(log k) (height of a heap with k elements).
# Space O(k): the heap never holds more than k elements at a time.


# ---------------- Q-13: Top K frequent elements ----------------
# nums = [1, 1, 1, 2, 2, 3], k = 2  ->  [1, 2]  (the two most common values)
# nums = [1], k = 1  ->  [1]
#
# Two steps:
# - count how many times each number appears (hashmap)
# - we now want the k LARGEST counts, which is the kth_largest trick again:
#   a MIN-heap of size k holding (count, number) pairs.
# - heapq compares tuples by the FIRST item, so it orders by count for free.
# - if the heap grows past k, pop the smallest count (it cannot be a winner).
# Time O(n log k), Space O(n)

import heapq

def top_k_frequent(nums, k):
  count = {}
  for num in nums:            # count each number
    if num not in count:
      count[num] = 0
    count[num] += 1

  heap = []
  for num in count:
    heapq.heappush(heap, (count[num], num))  # tuple -> ordered by count
    if len(heap) > k:
      heapq.heappop(heap)     # drop the least frequent seen so far

  return [ num for count, num in heap ]      # the k most frequent numbers
# O(n log k), O(n)
# Time O(n log k): count all n numbers, then each push/pop costs O(log k)
#   on a heap that is capped at k elements.
# Space O(n): the hashmap can hold up to n distinct numbers.


# ---------------- Q-14: Merge K sorted linked lists ----------------
# lists = [ 1->4->5, 1->3->4, 2->6 ]  ->  1->1->2->3->4->4->5->6
#
# Merging two at a time re-walks the same nodes over and over -> O(n * k).
# Better: hold ONE candidate from each list in a min-heap of size k.
# - the heap root is always the smallest unused node across every list
# - pop it, attach it to the answer, then push that node's NEXT value
# - the heap never holds more than k nodes, so each step costs O(log k)
# - we push the list index as a tie-breaker, because when two values are
#   equal Python would try to compare the Node objects and crash
# Time O(n log k), Space O(k)

import heapq

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_k_sorted_lists(lists):
  heap = []

  for i, head in enumerate(lists):    # seed the heap with each list's head
    if head is not None:
      heapq.heappush(heap, (head.val, i, head))  # i breaks ties on equal val

  dummy = Node(None)                  # dummy avoids a special case for the head
  tail = dummy

  while heap:
    val, i, node = heapq.heappop(heap)  # smallest value across all lists
    tail.next = node
    tail = tail.next

    if node.next is not None:         # refill the heap from the SAME list
      heapq.heappush(heap, (node.next.val, i, node.next))

  return dummy.next
# O(n log k), O(k)
# Time O(n log k): each of the n nodes is pushed and popped exactly once,
#   and the heap is never bigger than k.
# Space O(k): at most one node per list sits in the heap at a time.
