class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_duplicate = {}
        for x in nums:
            if x in check_duplicate:
                return True
            check_duplicate[x] = True 
        return False
        
        
