class Solution(object):

    def word_break(self, s, word_dict):
        
        def recurse(target, words, memo):

            if target in memo:
                return memo[target]

            if target == "":
                return True

            for word in words:
                if target.find(word) == 0:
                    suffix = target[len(word):]
                    if recurse(suffix, words, memo) == True:
                        memo[target] = True
                        return memo[target]

            memo[target] = False
            return memo[target]

        return recurse(s, word_dict, {})

solution = Solution()

assert(solution.word_break("leetcode", ["leet","code"]) == True)

print("PASS")