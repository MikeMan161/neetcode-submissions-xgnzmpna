class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        sNums = sorted(nums)

        for x in range(len(sNums)):
            left = x + 1
            right = len(sNums) - 1
            while left < right:
                if sNums[x] + sNums[left] + sNums[right] == 0:
                    triplet = tuple(sorted([sNums[x],sNums[left],sNums[right]]))
                    if triplet not in triplets:
                        triplets.add(triplet)
                        
                    else:
                        pass
                    left += 1
                elif sNums[x] + sNums[left] + sNums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return list(triplets)


