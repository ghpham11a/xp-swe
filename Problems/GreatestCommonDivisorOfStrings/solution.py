class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Get the lengths of both input strings
        len1, len2 = len(str1), len(str2)

        # This inner function checks if the prefix of str1 with given length `l`
        # can be used as a divisor for both str1 and str2.
        def is_divisor(l):
            # If either string's length is not a multiple of l, then the prefix of length l
            # cannot be concatenated to form that string.
            if len1 % l or len2 % l:
                return False
            # Calculate the number of repetitions needed for each string
            f1, f2 = len1 // l, len2 // l
            # Check if repeating the substring str1[:l] the required number of times 
            # yields exactly str1 and str2 respectively.
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # Try every possible length l from the minimum string length down to 1.
        # Since we iterate in decreasing order, the first valid divisor is the largest.
        for l in range(min(len1, len2), 0, -1):
            if is_divisor(l):
                # Return the substring of length l that divides both strings.
                return str1[:l]

        # If no common divisor is found, return an empty string.
        return ""