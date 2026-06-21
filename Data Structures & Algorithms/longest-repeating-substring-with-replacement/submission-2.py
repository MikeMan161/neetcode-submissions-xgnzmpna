class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left, right = 0, 0
        frequency = {}

        while right < len(s):
            if s[right] in frequency:
                frequency[s[right]] += 1
            else:
                frequency[s[right]] = 1
            while (right - left + 1) - max(frequency.values()) > k:
                frequency[s[left]] -= 1
                left += 1
            if (right - left) + 1 > maxLength:
                maxLength = (right - left) + 1
            right += 1
        return maxLength