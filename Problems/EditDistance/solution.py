class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[0 for col in range(len(word1) + 1)] for row in range(len(word2) + 1)]
        
        for row in range(len(word2) + 1):
            for col in range(len(word1) + 1):
                if row == 0:
                    cache[row][col] = col
                elif col == 0:
                    cache[row][col] = row
                else:
                    if word1[col-1] == word2[row-1]:
                        cache[row][col] = cache[row-1][col-1]
                    else:
                        cache[row][col] = min(cache[row-1][col-1], cache[row][col-1], cache[row-1][col]) + 1
                        
        return cache[len(word2)][len(word1)]