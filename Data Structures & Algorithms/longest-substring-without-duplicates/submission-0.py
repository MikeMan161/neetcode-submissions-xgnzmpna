class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        left, right = 0, 0
        frequency = {}

        while (right < len(s)):
            if s[right] in frequency:
                frequency[s[right]] += 1
            else:
                frequency[s[right]] = 1
            right += 1
            while frequency[s[right - 1]] > 1:
                frequency[s[left]] -= 1
                left += 1
            if right - left > maxlength:
                maxlength = right - left
        return maxlength

            



