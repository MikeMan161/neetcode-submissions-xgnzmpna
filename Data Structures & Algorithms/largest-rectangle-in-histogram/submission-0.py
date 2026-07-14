class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        i = 0
        while i < int(len(heights)):
            if not stack:
                stack.append(i)
            else:
                if heights[i] < heights[stack[-1]]:
                    while stack and heights[i] < heights[stack[-1]]:
                        j = stack.pop()
                        if not stack:
                            width = i
                        else:
                            width = i - stack[-1] - 1
                        area = heights[j] * width
                        if area > maxArea:
                            maxArea = area
                    stack.append(i)
                else:
                    stack.append(i)
            i += 1
        while stack:
            l = stack.pop()
            if not stack:
                width = len(heights)
            else:
                width = int(len(heights)) - stack[-1] - 1
            area = heights[l] * width
            if area > maxArea:
                maxArea = area
        return maxArea
        