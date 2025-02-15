class Solution:

    def alien_order(self, words):

        graph = {}

        if not self.build_graph(graph, words):
            return ""

        seen = {}
        output = []

        for node in graph:
            if not self.dfs(graph, seen, output, node):
                return ""

        return "".join(output[::-1])

    def build_graph(self, graph, words):
        for word in words:
            for c in word:
                graph[c] = []

        for word, next_word in zip(words, words[1:]):
            for word_char, next_word_char in zip(word, next_word):
                if word_char != next_word_char: 
                    graph[word_char].append(next_word_char)
                    break
            else: 
                if len(next_word) < len(word):
                    return False

        return True

    def dfs(self, graph, seen, output, node): 

        if node in seen:
            return seen[node]

        seen[node] = False
        for next_node in graph[node]:
            result = self.dfs(graph, seen, output, next_node)
            if not result: 
                return False

        seen[node] = True
        output.append(node)

        return True
        

solution = Solution()

assert(solution.alien_order(["wrt","wrf","er","ett","rftt"]) == "wertf")

print("PASS")