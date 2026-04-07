class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in hashmap:
                return ([hashmap[remainder], index])
            hashmap[value] = index