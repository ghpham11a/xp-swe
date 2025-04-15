class Solution:
    def kids_with_candies(self, candies, extraCandies):

        max_candy_count = max(candies)
        output = []
        
        for kid_index in range(len(candies)):
            new_count = candies[kid_index] + extraCandies
            output.append(new_count >= max_candy_count)
            
        return output