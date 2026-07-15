class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        x = 0
        while x < len(nums):
            if not hashmap:
                hashmap[target - nums[x]] = x
            else:
                if nums[x] in hashmap:
                    return [hashmap[nums[x]], x]
                else:
                    hashmap[target - nums[x]] = x
            x += 1
