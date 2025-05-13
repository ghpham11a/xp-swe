class Solution:

    def alien_order(self, words):
        graph = {}

        # Step 1: Build the graph (adjacency list of character ordering)
        if not self.build_graph(graph, words):
            # If invalid prefix case is detected, return empty string
            return ""

        seen = {}      # Tracks visited state of each node: True (visited), False (visiting), not in seen (unvisited)
        output = []    # Stores characters in topologically sorted order

        # Step 2: Perform DFS for topological sort
        for node in graph:
            if not self.dfs(graph, seen, output, node):
                # Cycle detected; invalid ordering
                return ""

        # Step 3: Reverse post-order gives correct topological ordering
        return "".join(output[::-1])

    def build_graph(self, graph, words):
        # Initialize graph with all unique characters
        for word in words:
            for c in word:
                graph[c] = []

        # Build edges by comparing adjacent words
        for word, next_word in zip(words, words[1:]):
            for word_char, next_word_char in zip(word, next_word):
                if word_char != next_word_char:
                    # First different character implies an ordering constraint
                    graph[word_char].append(next_word_char)
                    break
            else:
                # Edge case: prefix conflict (e.g., ["abc", "ab"]) is invalid
                if len(next_word) < len(word):
                    return False

        return True

    def dfs(self, graph, seen, output, node):
        if node in seen:
            return seen[node]  # Return False if we are revisiting a node in the current DFS path (cycle)

        seen[node] = False  # Mark node as visiting (gray)
        for next_node in graph[node]:
            result = self.dfs(graph, seen, output, next_node)
            if not result:
                return False  # Cycle detected

        seen[node] = True  # Mark node as visited (black)
        output.append(node)  # Append to output after visiting all descendants
        return True
        

solution = Solution()

assert(solution.alien_order(["wrt","wrf","er","ett","rftt"]) == "wertf")

print("PASS")