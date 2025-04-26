class Solution:
    def romanToInt(self, s):
        # largest to smallest: add them up
        # smaller before larger: subtract smaller
        
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        output = 0

        for i in range(len(s)):
            if i + 1 < len(s) and dictionary[s[i]] < dictionary[s[i + 1]]:
                output -= dictionary[s[i]]
            else:
                output += dictionary[s[i]]

        return output