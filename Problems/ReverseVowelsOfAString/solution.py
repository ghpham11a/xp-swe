class Solution:
    def reverse_vowels(self, s):
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        output = list(s)
        vowels_seen = []

        for letter in output:
            if letter in vowels:
                vowels_seen.append(letter)

        for index, letter in enumerate(output):
            if letter in vowels:
                vowel = vowels_seen.pop()
                output[index] = vowel

        return "".join(output)