class Solution:

    def merge_alternately(self, word1, word2):

        word1_index = 0
        word2_index = 0

        output = ""

        target_len = len(word1) + len(word2)

        while len(output) != target_len:

            if word1_index < len(word1):
                output += word1[word1_index]
                word1_index += 1

            if word2_index < len(word2):
                output += word2[word2_index]
                word2_index += 1

        return output