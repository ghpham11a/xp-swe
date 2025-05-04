from typing import List

class Solution:

    # Special key used to mark the end of a word in the trie
    WORD_KEY = '$'

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build a trie (prefix tree) from the list of words
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # Traverse down the trie, creating nodes as needed
                node = node.setdefault(letter, {})
            # Mark the end of a word with a special key and store the word itself
            node[self.WORD_KEY] = word

        output = []

        # Iterate through every cell on the board as a potential starting point
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Start backtracking if the letter exists in the root of the trie
                if board[row][col] in trie:
                    self.backtracking(board, row, col, trie, output)

        return output

    def backtracking(self, board, row, col, parent_node, output):
        # Base case: return if the current cell is not valid for exploration
        if not self.is_valid(board, row, col, parent_node):
            return

        letter = board[row][col]
        curr_node = parent_node[letter]  # Move one level down in the trie

        # If a complete word is found, add it to the output
        word_match = curr_node.pop(self.WORD_KEY, False)
        if word_match:
            output.append(word_match)
            # Removing the word prevents duplicates and avoids needing a set

        # Mark the current cell as visited by replacing it with a sentinel
        board[row][col] = '#'

        # Explore all 4 adjacent directions (up, right, down, left)
        self.backtracking(board, row - 1, col, curr_node, output)
        self.backtracking(board, row, col + 1, curr_node, output)
        self.backtracking(board, row + 1, col, curr_node, output)
        self.backtracking(board, row, col - 1, curr_node, output)

        # Restore the original letter after backtracking
        board[row][col] = letter

    def is_valid(self, board, row, col, parent_node):
        # Check if the row is out of bounds
        if row < 0 or row >= len(board):
            return False

        # Check if the column is out of bounds
        if col < 0 or col >= len(board[0]):
            return False

        # Check if the current cell's letter is a valid child in the trie
        if board[row][col] not in parent_node:
            return False

        return True

solution = Solution()

assert(solution.find_words([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]) == ["oath","eat"])

print("PASS")