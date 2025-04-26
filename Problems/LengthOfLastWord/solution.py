class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and length == 0:
                continue
            if s[i] == " ":
                break
            else:
                length += 1

        return length