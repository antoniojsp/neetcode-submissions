from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapa = defaultdict(list)
        for i in strs:
            mapa["".join(sorted(i))].append(i)
        return list(mapa.values())