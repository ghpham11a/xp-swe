from collections import defaultdict

class Solution:

    def wordBreak(self, s, wordDict):

        def recurse(target, words, memo):

            if target in memo:
                return memo[target]

            output = []

            if target in words:
                output = [target]

            for i in range(1, len(target)):
                prefix = target[:i]
                if prefix in words:
                    sentences = recurse(target[i:], words, memo)
                    for sentence in sentences:
                        output.append(prefix + " " + sentence)

            memo[target] = output
            return output

        return recurse(s, set(wordDict), {})

solution = Solution()

assert(solution.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]) == ["cat sand dog","cats and dog"])

print("PASS")