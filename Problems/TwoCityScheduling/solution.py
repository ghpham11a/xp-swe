class Solution:
    
    def two_city_sched_cost(self, costs):

        # Initialize a list to store the difference between city B cost and city A cost,
        # along with the individual costs.
        # For each person, store [difference, cost to A, cost to B]
        # The difference (c2 - c1) tells us the extra cost (or saving) of choosing city B over city A.
        diffs  = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])

        # Sort the list of differences in ascending order.
        # Persons with a large negative difference (city B much cheaper than city A)
        # will come first, and persons with a positive difference (city A cheaper) will come later.
        diffs.sort()

        # Initialize output to store the total minimum cost.
        output = 0

        # Iterate over the sorted list.
        # Since we must send exactly n people to each city and there are 2n people total,
        # we choose the first n persons (with lower diff) to go to city B (cheaper option for them)
        # and the remaining n persons to go to city A.
        for i in range(len(diffs)):

            # For the first half of the sorted list, add the cost for city B.
            if i < len(diffs) // 2:
                output += diffs[i][2]
            # For the second half, add the cost for city A.
            else:
                output += diffs[i][1]

        # Return the computed minimum total cost.
        return output

solution = Solution()

assert(solution.two_city_sched_cost([[10,20],[30,200],[400,50],[30,20]]) == 110)

print("PASS")