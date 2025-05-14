class Solution(object):
    
    def num_decodings(self, message):
        
        # If the message starts with '0', it's invalid since '0' can't be mapped
        if message[0] == '0':
            return 0
        
        message_len = len(message)
        
        # DP table: table[i] represents the number of ways to decode the substring message[0:i]
        table = [0 for i in range(message_len + 1)]
        
        # Base case: an empty string has 1 valid decoding (do nothing)
        table[0] = 1
        
        # Base case: the first character has 1 valid decoding (already checked for leading '0')
        table[1] = 1 

        # Start from index 2 and build up the table
        for i in range(2, message_len + 1):  

            # Single digit check: message[i-1] is the current character (1-based)
            # If it's between '1' and '9', we can decode it as a single letter
            if message[i - 1] > '0':  
                table[i] = table[i - 1]  # Extend the count from the previous character

            # Two digit check: message[i-2:i] forms a number between 10 and 26
            if (message[i - 2] == '1' or 
               (message[i - 2] == '2' and message[i - 1] < '7')):  
                table[i] += table[i - 2]  # Add the number of ways from two steps back

        # Return the total number of decoding ways for the full message
        return table[-1]

solution = Solution()

assert(solution.num_decodings("226") == 3)
assert(solution.num_decodings("06") == 0)

print("PASS")