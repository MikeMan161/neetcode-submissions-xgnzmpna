class Solution:
    def trap(self, height: List[int]) -> int:
        temp = 0
        left = 0
        x = 0
        right = len(height) - 1

        maxEdge = [[] for x in range(len(height))]

        leftedge = 0
        while left < len(height):
            maxEdge[left].append(leftedge)
            leftedge = max(height[left], leftedge)
    
            left += 1 

        rightedge = 0
        while right >= 0:
            maxEdge[right].append(rightedge)
            rightedge = max(height[right], rightedge)

            right -= 1

        while x < len(maxEdge):
            a, b = maxEdge[x]

            if min(a, b) > height[x]:
                temp += (min(a,b) - height[x])

            x += 1


        return temp
