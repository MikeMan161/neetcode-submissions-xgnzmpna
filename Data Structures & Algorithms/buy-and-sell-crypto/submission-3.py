class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        left, right = 0, 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
                continue
            elif (prices[right] - prices[left]) > maxValue:
                maxValue = prices[right] - prices[left]
            right += 1
        return maxValue

    