from typing import List

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a dictionary to map sorted strings to lists of anagrams
        map_list = {}

        # Iterate over each word in the input list
        for string in strs:
            # Sort the characters of the string and use it as a key
            # All anagrams will result in the same sorted string
            key = "".join(sorted(string))

            # If the key already exists in the dictionary, append the string to its list
            if key in map_list:
                map_list[key].append(string)
            else:
                # Otherwise, create a new list for this key
                map_list[key] = [string]

        # Return all the grouped anagram lists as the final result
        return [map_list[key] for key in map_list]