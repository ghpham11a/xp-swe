class Solution:
    def unhappy_friends(self, n, preferences, pairs):
        d = {}

        # Step 1: Build a dictionary 'd' that maps each person to the set of friends
        # they prefer *more* than their current pair.
        for x, y in pairs:
            # For x, get the set of people more preferred than y
            d[x] = set(preferences[x][:preferences[x].index(y)])
            # For y, get the set of people more preferred than x
            d[y] = set(preferences[y][:preferences[y].index(x)])

        output = 0

        # Step 2: For each person x, iterate over all people y they prefer over their partner
        for x in d:
            for y in d[x]:
                # If y also prefers x over their current partner,
                # then both x and y are unhappy with their current pairs.
                if x in d[y]:
                    output += 1
                    break  # Only count each unhappy person once

        return output
    
solution = Solution()

assert(solution.unhappy_friends(4, [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], [[0,1],[2,3]]) == 2)

print("PASS")