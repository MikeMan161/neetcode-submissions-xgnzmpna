class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = set()

        for x in nums:
            if x in isDuplicate:
                return True
            else:
                isDuplicate.add(x)
        return False