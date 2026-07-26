class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        y = list(t)
        d1 = {}
        d2 = {}
        value = 1

        for char in x:  
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = value
        for char in y:
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = value

        if len(d1) != len(d2):
            return False
        else:
            for key in d1:
                if key not in d2 or d1[key] != d2[key]:
                    return False
            else:
                return True