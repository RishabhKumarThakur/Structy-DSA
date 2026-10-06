# ==================== CHAPTER 12 - TRIE ====================
# Trie.py - 2 questions

# ==================== TRIE (PREFIX TREE) ====================


# Trie - a tree where each EDGE is a character, so every PATH from the root spells a prefix.
# Used for autocomplete, spell check, prefix search, and word dictionaries.

# Why not just a HashMap?
# a hashmap answers "is this EXACT word in my set?" in O(1),
# but it cannot answer "how many words start with 'app'?" without scanning everything.
# a trie shares prefixes, so every word starting with 'app' lives under one branch.

# Storing ["cat", "car", "do"]:
#
#         root
#         /   \
#        c     d
#        |     |
#        a     o*
#       / \
#      t*  r*
#
# * marks a node where a real word ENDS
# "ca" is a valid path in the tree but is NOT a stored word,
# which is exactly why every node needs the is_word flag

# n = length of the word being inserted or searched
# insert / search / starts_with are all O(n)
# note this does NOT depend on how many words are already stored


# ---------------- Q-1: Implement Trie ----------------
# trie = Trie()
# trie.insert("cat")
# trie.insert("car")
# trie.search("cat")        # -> True
# trie.search("ca")         # -> False, the path exists but no word ends there
# trie.starts_with("ca")    # -> True, some word does start with "ca"
# trie.search("dog")        # -> False

# each node holds:
#   children -> dict mapping a character to the next TrieNode
#   is_word  -> True only when a word ENDS at this node

# insert      : walk down, create nodes for missing characters, flag the final node
# search      : walk down, fail if a character is missing, then check the flag
# starts_with : identical walk, but do NOT check the flag

class TrieNode:
  def __init__(self):
    self.children = {}    # character -> TrieNode
    self.is_word = False  # True if some word ends exactly here

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    current = self.root

    for char in word:
      if char not in current.children:
        current.children[char] = TrieNode()  # build the branch as we go
      current = current.children[char]

    current.is_word = True   # flag the last node, "cat" is a real word
  # O(n), O(n)

  def _walk(self, prefix):   # shared helper, follow the path or return None if it breaks
    current = self.root

    for char in prefix:
      if char not in current.children:
        return None
      current = current.children[char]

    return current

  def search(self, word):
    node = self._walk(word)
    return node is not None and node.is_word  # path exists AND a word ends there
  # O(n), O(1)

  def starts_with(self, prefix):
    return self._walk(prefix) is not None     # path exists, word or not
  # O(n), O(1)


# ---------------- Q-2: Words with a given prefix (autocomplete) ----------------
# this is the payoff, the thing a hashmap simply cannot do efficiently

# trie = Trie()
# trie.insert("cat")
# trie.insert("car")
# trie.insert("do")
# words_with_prefix(trie, "ca") # -> ['cat', 'car']
# words_with_prefix(trie, "d")  # -> ['do']
# words_with_prefix(trie, "z")  # -> []

# walk to the node at the end of the prefix, then DFS everything underneath it
# each node flagged is_word completes a word,
# and we rebuild that word from the characters used to walk down

# p = length of the prefix, k = words under it, L = their average length
# Time Complexity O(p + k * L); walk the prefix, then collect the whole subtree
# Space Complexity O(k * L); the collected words

def words_with_prefix(trie, prefix):
  node = trie._walk(prefix)
  if node is None:          # prefix is not in the trie at all
    return []

  words = []

  def collect(current, path):
    if current.is_word:
      words.append(path)    # path spells a complete word

    for char in current.children:
      collect(current.children[char], path + char)  # extend the path downward

  collect(node, prefix)
  return words

# O(p + k * L), O(k * L)
