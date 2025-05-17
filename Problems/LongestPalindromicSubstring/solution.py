class Solution(object):
    def longestPalindrome(self, s):
        str_len = len(s)
        
        # Initialize a 2D cache to keep track of whether s[i:j+1] is a palindrome
        cache = [[0 for col in range(str_len)] for row in range(str_len)]
        
        max_length = 1  # Minimum palindrome length is 1 (a single character)

        # Every single character is a palindrome of length 1
        for i in range(str_len):
            cache[i][i] = True
            
        start = 0  # Start index of the longest palindromic substring found so far

        # Check for palindromes of length 2
        for i in range(str_len - 1):
            if s[i] == s[i + 1]:
                cache[i][i + 1] = True
                start = i
                max_length = 2  # Update max length to 2 for this case
                
        # Check for palindromes of length 3 and above
        for sub_len in range(3, str_len + 1):
            # i is the starting index of the current substring
            for i in range(str_len - sub_len + 1):
                sub_end_index = i + sub_len - 1  # Ending index of the substring
                
                # A substring is a palindrome if:
                # - The ends match (s[i] == s[j])
                # - The inner substring s[i+1:j-1] is also a palindrome
                if cache[i + 1][sub_end_index - 1] and s[i] == s[sub_end_index]:
                    cache[i][sub_end_index] = True
                    
                    # If we found a longer palindrome, update the max length and starting index
                    if sub_len > max_length:
                        start = i
                        max_length = sub_len
                        
        # Return the longest palindromic substring found
        return s[start:start + max_length]