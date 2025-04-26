class Solution:
    def canConstruct(self, ransomNote, magazine):

        seen = {}

        for c in magazine:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1

        for c in ransomNote:
            if c in seen and seen[c] > 0:
                seen[c] -= 1
            else:
                return False

        return True