class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.is_end = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end

    def delete(self, word):
        current = self.root
        # Track the path from the root to the end node.
        path = [current]

        for char in word:
            if char not in current.children:
                # Word not found.
                return False
            current = current.children[char]
            path.append(current)

        # Word found; unmark the end node.
        if not current.is_end:
            # Word was not a complete word in the trie.
            return False
        current.is_end = False

        # Clean up: remove nodes that are no longer needed.
        # We iterate backwards over the word.
        for index in range(len(word) - 1, -1, -1):
            parent = path[index]
            char = word[index]
            child = parent.children[char]
            # Remove the child if it's not the end of another word and has no children.
            if not child.is_end and not child.children:
                del parent.children[char]
            else:
                # If the node is still needed, stop cleaning up.
                break

        return True

# Example usage:
if __name__ == "__main__":
    trie = Trie()

    # Insert words.
    trie.insert("cat")
    trie.insert("cater")
    trie.insert("dog")

    # Search for words.
    print(trie.search("cat"))   # True
    print(trie.search("cater")) # True
    print(trie.search("do"))    # False

    # Delete a word using the iterative method.
    if trie.delete("cater"):
        print("Deleted 'cater' successfully.")
    else:
        print("'cater' not found.")

    # 'cat' should still exist as it is a prefix.
    print(trie.search("cat"))   # True

    # Delete a word using the recursive method.
    if trie.delete_recursive("cat"):
        print("Deleted 'cat' successfully with recursive deletion.")
    else:
        print("'cat' not found during recursive deletion.")

    print(trie.search("cat"))   # False
    print(trie.search("dog"))   # True
