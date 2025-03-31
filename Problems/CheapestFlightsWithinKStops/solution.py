class Solution(object):

    def find_cheapest_price(self, n, flights, src, dst, k):
        # Initialize a list to hold the minimum price to reach each city.
        # Set all prices to infinity initially because we haven't computed any routes.
        prices = [float("inf") for _ in range(n)]
        # The cost to reach the source city is 0.
        prices[src] = 0

        # Perform the relaxation process for exactly k+1 iterations.
        # Each iteration allows us to consider one more flight (edge) in the path.
        for _ in range(k + 1):
            # Create a temporary copy of the current prices.
            # This ensures that we only use the prices from the previous iteration
            # while updating new prices for this iteration.
            temp = prices.copy()
            # Iterate over all flights, where each flight is represented as
            # (route_src, route_dst, route_weight).
            for route_src, route_dst, route_weight in flights:
                # Check if the source city for the current flight is reachable.
                # If it is reachable, see if taking this flight results in a cheaper cost to reach the destination city.
                if prices[route_src] + route_weight < temp[route_dst]:
                    # Update the cost for route_dst in the temporary copy.
                    temp[route_dst] = prices[route_src] + route_weight
            # After processing all flights, update the prices list with the new costs.
            prices = temp

        # If the destination city is still unreachable (price remains infinity),
        # return -1. Otherwise, return the computed minimum price.
        return -1 if prices[dst] == float("inf") else prices[dst]


solution = Solution()

assert(solution.find_cheapest_price(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700)

print("PASS")