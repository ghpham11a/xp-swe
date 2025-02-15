class Solution:

    WORD_KEY = '$'

    def find_words(self, board, words):
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[self.WORD_KEY] = word
        
        output = []
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie:
                    self.backtracking(board, row, col, trie, output)

        return output

    def backtracking(self, board, row, col, parent_node, output):

        if not self.is_valid(board, row, col, parent_node):
            return

        letter = board[row][col]
        curr_node = parent_node[letter]  
        
        word_match = curr_node.pop(self.WORD_KEY, False)
        if word_match:
            output.append(word_match)
        
        board[row][col] = '#'

        self.backtracking(board, row - 1, col, curr_node, output)
        self.backtracking(board, row, col + 1, curr_node, output)
        self.backtracking(board, row + 1, col, curr_node, output)
        self.backtracking(board, row, col - 1, curr_node, output)

        board[row][col] = letter

    def is_valid(self, board, row, col, parent_node):
        if row < 0 or row >= len(board):
            return False
            
        if col < 0 or col >= len(board[0]):
            return False

        if not board[row][col] in parent_node:
            return False

solution = Solution()

assert(solution.find_words([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]) == ["oath","eat"])

print("PASS")