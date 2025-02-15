from collections import defaultdict

class Solution:
    def ladder_length(self, begin_word, end_word, word_list):

        if end_word not in word_list:
            return 0
 
        graph = defaultdict(list)
        word_list.append(begin_word)

        for word in word_list:
            for char_index in range(len(word)):
                node = word[:char_index] + "*" + word[char_index + 1:]
                graph[node].append(word)

        visited = set([begin_word])
        queue = [begin_word]
        output = 1

        while queue:
            for i in range(len(queue)):
                word = queue.pop()
                if word == end_word:
                    return output
                for char_index in range(len(word)):
                    node = word[:char_index] + "*" + word[char_index + 1:]
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.insert(0, neighbor)
            output += 1
        
        return 0

solution = Solution()

assert(solution.ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5)

print("PASS")