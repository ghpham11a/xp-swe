class Solution(object):
    
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
        
        results = []
        
        if digits:
            self.recur(results, "", digits)
        
        return results
        
    def recur(self, results, progress, remaining_digits):
        
        if len(remaining_digits) == 0:
            results.append(progress)
        else:
            for letter in self.PHONE[remaining_digits[0]]:
                self.recur(results, progress + letter, remaining_digits[1:])