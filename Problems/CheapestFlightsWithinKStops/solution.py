class Solution(object):

    def find_cheapest_price(self, n, flights, src, dst, k):
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp_prices = prices.copy()

            for flight_src, flight_dst, flight_price in flights:
                if prices[flight_src] == float("inf"):
                    continue

                agg_price = prices[flight_src] + flight_price
                if agg_price < tmp_prices[flight_dst]:
                    tmp_prices[flight_dst] = agg_price

            prices = tmp_prices

        return -1 if prices[dst] == float("inf") else prices[dst]  

solution = Solution()

assert(solution.find_cheapest_price(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700)

print("PASS")