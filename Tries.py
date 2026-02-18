# 1. The "Global Autocomplete" System (Tries)
# ○ Problem: Build a Trie-based system that stores 1 million strings. Implement a
# function that returns the top 5 most frequent suggestions for a given prefix.
# ○ Complexity Requirement: The prefix search must be O(L), where L is the length of
# the prefix, regardless of the dictionary size.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.top = []


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.freq = {}

    def insert(self, word):
        self.freq[word] = self.freq.get(word, 0) + 1

        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

            if word not in node.top:
                node.top.append(word)

            node.top.sort(key=lambda x: self.freq[x], reverse=True)

            if len(node.top) > 5:
                node.top.pop()

    def autocomplete(self, prefix):
        node = self.root

        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        return node.top


t = Trie()

words = [
    "hello","hello","hello",
    "help","help",
    "hell",
    "helping",
    "helps",
    "hel",
    "dog","dog",
    "cat"
]

for w in words:
    t.insert(w)

print(t.autocomplete("he"))
print(t.autocomplete("hel"))
print(t.autocomplete("h"))
