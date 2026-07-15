class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best_rate = 0
        left = 1
        right = max(piles)
        mid = 0
        def canFinish(k):
            hours = 0
            x = 0
            while x < len(piles):
                hours += -(-piles[x] // k)
                x += 1
            return hours <= h
            
        while left <= right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                best_rate = mid
                right = mid - 1
            else:
                left = mid + 1

        return best_rate
