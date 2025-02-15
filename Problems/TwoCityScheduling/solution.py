class Solution:
    
    def two_city_sched_cost(self, costs):

        diffs  = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
        diffs.sort()

        output = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                output += diffs[i][2]
            else:
                output += diffs[i][1]

        return output

solution = Solution()

assert(solution.two_city_sched_cost([[10,20],[30,200],[400,50],[30,20]]) == 110)

print("PASS")