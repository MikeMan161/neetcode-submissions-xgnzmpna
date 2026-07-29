class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #we use a binary search
        #nums[left] is greater than nums[right]
        #we are checking to see if the range is correct
        # this is an exact binary search, not a boundary search

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            #first check if nums[mid] is equal to target. if true, return index
            #then check if nums[mid] is greater than nums[left]. if it is, we know it's a valid range,
            #check if target is in there too. something like nums[left] < target < nums[mid]
            #if true, shrink the right. if false, we know that it's on the right, so shrink left.

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1     
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1