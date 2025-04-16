class Solution:
    def max_vowels(self, s: str, k: int) -> int:

        vowels = set(["a", "e", "i", "o", "u"])
        cur_count = 0

        for i in range(k):
            if s[i] in vowels:
                cur_count += 1

        max_count = cur_count

        for i in range(len(s) - k):
            if s[i] in vowels:
                cur_count -= 1
            if s[i + k] in vowels:
                cur_count += 1
            max_count = max(max_count, cur_count)

        return max_count
