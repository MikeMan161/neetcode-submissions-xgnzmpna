class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for x in strs:
            word = sorted(x)
            z = ''.join(word)
            if z in anagrams:
                anagrams[z].append(x)
            else:
                anagrams[z] = [x]
        return list(anagrams.values())