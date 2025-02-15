class Node:
    
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node()
            curr_node = curr_node.children[char]
        curr_node.is_end = True

    def delete(self, word):

        curr_node = self.root
        parents = [curr_node]
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
            parents.append(curr_node)

        curr_node.is_end = False

        parents.pop()

        for parent_and_word_index in range(len(parents) - 1, 0, -1):
            parent = parents[parent_and_word_index]
            char = word[parent_and_word_index]
            if parent.children[char].is_end == False and len(parent.children[char].children) == 0:
                del parent.children[char]

        return True
        
    def search(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_end
