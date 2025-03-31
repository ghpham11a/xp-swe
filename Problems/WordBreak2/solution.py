class Solution:

    def wordBreak(self, s, wordDict):

        # Define a helper function that returns all sentences for a given substring 'target'.
        # 'words' is a set of valid dictionary words for fast membership checking.
        # 'memo' is used to store previously computed results for substrings.
        def recurse(target, words, memo):

            # If we have already computed the result for this target, return it.
            if target in memo:
                return memo[target]

            output = []

            # If the entire target string is a valid word, it forms a valid sentence by itself.
            if target in words:
                output = [target]

            # Try every possible split of the target into a prefix and a suffix.
            # 'i' goes from 1 to len(target)-1 to ensure non-empty prefix and suffix.
            for i in range(1, len(target)):

                # Take the left part of the split.
                prefix = target[:i]

                # If the prefix is a valid word, we proceed to solve for the suffix.
                if prefix in words:
                    # Recursively solve for the suffix (target[i:]).
                    sentences = recurse(target[i:], words, memo)

                    # For each valid sentence from the recursion, combine it with the prefix.
                    for sentence in sentences:
                        # Append the sentence with a space between the prefix and the sentence.
                        output.append(prefix + " " + sentence)

            # Memoize the result for the current target to avoid recomputation.
            memo[target] = output
            
            return output

        return recurse(s, set(wordDict), {})

solution = Solution()

assert(solution.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]) == ["cat sand dog","cats and dog"])

print("PASS")