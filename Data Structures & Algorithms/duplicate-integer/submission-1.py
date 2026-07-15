class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_duplicates = {}
        for x in nums:
            if x in check_duplicates:
                return True
            check_duplicates[x] = True
        return False