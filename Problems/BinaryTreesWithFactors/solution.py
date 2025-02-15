class Solution(object):
    
    def num_factored_binary_trees(self, arr):
        MOD = 10 ** 9 + 7

        arr.sort()
        dp = [1] * len(arr)

        node_to_index = {node: index for index, node in enumerate(arr)}

        for index, node in enumerate(arr):
            for j in range(index):
                if node % arr[j] == 0:
                    right = node / arr[j]
                    if right in node_to_index:
                        dp[index] += dp[j] * dp[node_to_index[right]]
                        dp[index] %= MOD

        return sum(dp) % MOD