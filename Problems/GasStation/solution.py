class Solution:

    def can_complete_circuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        total = 0
        output = 0

        for i in range(len(gas)):

            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                output = i + 1

        return output
    
solution = Solution()

assert(solution.can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]) == 3)

print("PASS")