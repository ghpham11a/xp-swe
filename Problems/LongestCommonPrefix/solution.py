class Solution:
    def longest_common_prefix(self, strs):
        
        output = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return output
                
            output += strs[0][i]

        return output