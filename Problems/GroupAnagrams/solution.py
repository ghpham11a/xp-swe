from typing import List

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_list = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in map_list:
                map_list[key].append(string)
            else:
                map_list[key] = [string]

        return [map_list[key] for key in map_list]