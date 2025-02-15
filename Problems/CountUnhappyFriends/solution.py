class Solution:
    def unhappy_friends(self, n, preferences, pairs):
        d = {}

        for x, y in pairs:
            d[x] = set(preferences[x][:preferences[x].index(y)])
            d[y] = set(preferences[y][:preferences[y].index(x)])

        output = 0

        for x in d:
            for y in d[x]:
                if x in d[y]:
                    output += 1
                    break

        return output
    
solution = Solution()

assert(solution.unhappy_friends(4, [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], [[0,1],[2,3]]) == 2)

print("PASS")