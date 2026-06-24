class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#       What is an Anagram? Order does not matter
#       We just have to check if each string has an equal num of each character
        sfrequency = {}
        tfrequency = {}

        for i in range(len(s)):
            if s[i] in sfrequency:
                sfrequency[s[i]] += 1
            else:
                sfrequency[s[i]] = 1
        for j in range(len(t)):
            if t[j] in tfrequency:
                tfrequency[t[j]] += 1
            else:
                tfrequency[t[j]] = 1
        
        if sfrequency == tfrequency:
            return True
        else:
            return False