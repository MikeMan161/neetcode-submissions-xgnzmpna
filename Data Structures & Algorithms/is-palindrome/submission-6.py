class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            """if s[i].isalnum():
                pass
            else: 
                i += 1
            if s[j].isalnum():
                pass
            else:
                j += -1"""
            while i < j and s[i].isalnum() == False:
                i += 1
            while j > i and s[j].isalnum() == False:
                j += -1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j += -1
        return True

