class Solution:

    def get_length_of_optimal_compression(self, s, k):

        cache = {}
        
        def count(i, k, prev, prev_count):

            key = "{}_{}_{}_{}".format(i, k, prev, prev_count)

            if key in cache:
                return cache[key]

            if k < 0:
                return float("inf")

            if i == len(s):
                return 0

            if s[i] == prev:
                increment = 1 if prev_count in [1, 9, 99] else 0
                result = increment + count(i + 1, k, prev, prev_count + 1)
            else:
                delete_result = count(i + 1, k - 1, prev, prev_count)
                no_delete_result = 1 + count(i + 1, k, s[i], 1)
                result = min(delete_result, no_delete_result)
            
            cache[key] = result
            return cache[key]
                
        return count(0, k, "", 0)