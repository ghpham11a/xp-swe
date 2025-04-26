class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False

        word_to_char = {}
        char_to_word = {}

        for i in range(len(words)):

            if pattern[i] in char_to_word and char_to_word[pattern[i]] != words[i]:
                return False

            if words[i] in word_to_char and word_to_char[words[i]] != pattern[i]:
                return False

            word_to_char[words[i]] = pattern[i]
            char_to_word[pattern[i]] = words[i]

        return True