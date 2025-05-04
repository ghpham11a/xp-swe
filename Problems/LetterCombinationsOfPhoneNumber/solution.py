class Solution(object):
    
    # Mapping of digits to letters, just like on a telephone keypad.
    PHONE = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
    }
    
    def letterCombinations(self, digits):
        # This list will store all the possible letter combinations.
        results = []
        
        # Start the recursion only if the input is non-empty.
        if digits:
            self.recur(results, "", digits)
        
        return results
        
    def recur(self, results, progress, remaining_digits):
        # Base case: If no more digits are left, add the formed combination to results.
        if len(remaining_digits) == 0:
            results.append(progress)
        else:
            # Recursive case: process the first digit in remaining_digits
            # and explore each corresponding letter.
            for letter in self.PHONE[remaining_digits[0]]:
                # Append the current letter to the in-progress string,
                # and recurse on the rest of the digits.
                self.recur(results, progress + letter, remaining_digits[1:])