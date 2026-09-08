class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxContainer = 0
        while i < j:
            height = min(heights[i],heights[j])
            width = j - i 
            if (height * width) > maxContainer:
                maxContainer = (width * height)
            if heights[i] == heights[j]:
                i += 1
            elif heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
        return maxContainer