class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        right = 0
        q = deque()
        result = []
        for right in (range(len(nums))):
#           pop smaller from back
            while q and nums[q[-1]] < nums[right]:
                q.pop()
#           append current index to the deque
            q.append(right)
#           Evict stale front
            if q[0] < right - k + 1:
                q.popleft()
#           record result
            if right >= k - 1:
                result.append(nums[q[0]])
        return result

#
