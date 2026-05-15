class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxWater = 0
        while i < j:
            temp = (j - i) * min(heights[i], heights[j])
            if temp > maxWater:
                maxWater = temp
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            elif heights[i] == heights[j]:
                i += 1
        return maxWater