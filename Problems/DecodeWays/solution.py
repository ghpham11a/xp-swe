class Solution(object):
    
    def num_decodings(self, message):
        
        if message[0] == '0':
            return 0
        
        message_len = len(message)
        
        table = [0 for i in range(message_len + 1)]
        
        table[0] = 1
        table[1] = 1 

        for i in range(2, message_len + 1):  

            if (message[i - 1] > '0'):  
                table[i] = table[i - 1] 

            if (message[i - 2] == '1' or (message[i - 2] == '2' and message[i - 1] < '7')):  
                table[i] += table[i - 2]

        return table[-1]

solution = Solution()

assert(solution.num_decodings("226") == 3)
assert(solution.num_decodings("06") == 0)

print("PASS")