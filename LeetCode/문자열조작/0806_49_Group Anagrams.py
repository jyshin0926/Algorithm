from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
