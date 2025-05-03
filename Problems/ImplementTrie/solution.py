# A node in the Trie
class Node:
    def __init__(self):
        # Each node contains a dictionary of children nodes
        self.children = {}
        # Flag to indicate if the node represents the end of a complete word
        self.is_end = False

class Trie:

    def __init__(self):
        # Initialize the root of the Trie (empty node)
        self.root = Node()

    def insert(self, word: str) -> None:
        # Start from the root node
        current = self.root
        # Iterate through each character in the word
        for char in word:
            # If the character is not already a child, add a new node
            if char not in current.children:
                current.children[char] = Node()
            # Move to the child node
            current = current.children[char]
        # After inserting all characters, mark the end of the word
        current.is_end = True

    def search(self, word: str) -> bool:
        # Start from the root node
        current = self.root
        # Traverse the Trie for each character in the word
        for char in word:
            if char not in current.children:
                # If a character is missing, the word doesn't exist
                return False
            current = current.children[char]
        # Return True only if current node marks the end of a complete word
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        # Start from the root node
        current = self.root
        # Traverse the Trie for each character in the prefix
        for char in prefix:
            if char not in current.children:
                # If a character is missing, no word starts with this prefix
                return False
            current = current.children[char]
        # All characters of the prefix matched, so return True
        return True