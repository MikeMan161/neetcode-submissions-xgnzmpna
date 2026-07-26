class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #frequency map approach
        #count the frequencies of string s, and subtract when iterating through t
        #if final total is 0, that means that they are anagrams
        #also if the length of s and t are not equal, return false early

        frequency = {}

        if len(s) != len(t):
            return False

        for x in s:
            if x not in frequency:
                frequency[x] = 1
            else:
                frequency[x] += 1
        
        for i in t:
            if i in frequency:
                frequency[i] -= 1
            else:
                return False
        if all(value == 0 for value in frequency.values()):
            return True
        else:
            return False
        