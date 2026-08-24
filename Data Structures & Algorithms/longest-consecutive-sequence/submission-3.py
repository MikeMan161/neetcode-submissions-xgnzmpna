class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        length = 0
        maxLen = 0
        temp = 0
        for x in num:
            if x-1 not in num:
                temp = x
                length = 1
                while temp + 1 in num:
                    length += 1
                    temp += 1
                if length > maxLen:
                    maxLen = length
        return maxLen
                
                    