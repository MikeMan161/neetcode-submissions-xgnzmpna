class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        left = 0
        right = 0
        maxLen = 0

        while right < len(s):
            dictionary[s[right]] = dictionary.get(s[right],0) + 1
            if ((sum(dictionary.values()) - max(dictionary.values()) <= k)):
                if (right - left + 1) > maxLen:
                    maxLen = right - left + 1                
            else:
                while sum(dictionary.values()) - max(dictionary.values()) > k:
                    dictionary[s[left]] -= 1
                    left += 1
                if (right - left + 1) > maxLen:
                    maxLen = right - left + 1
            right += 1
        return maxLen
