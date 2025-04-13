class Solution:
    def min_window(self, s, t):
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        output, output_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < output_len:
                    output = [l, r]
                    output_len = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = output
        return s[l:r + 1] if output_len != float("inf") else ""
    
solution = Solution()

assert(solution.min_window("ADOBECODEBANC", "ABC") == "BANC")
    
print("PASS")