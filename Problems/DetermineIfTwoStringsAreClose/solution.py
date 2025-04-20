from collections import Counter

class Solution:

    def close_strings(self, word1, word2):
        
        if len(word1) != len(word2):
            return False

        counts1 = Counter(word1)
        counts2 = Counter(word2)
        if counts1.keys() != counts2.keys():
            return False
        
        if sorted(counts1.values()) != sorted(counts2.values()):
            return False

        return True