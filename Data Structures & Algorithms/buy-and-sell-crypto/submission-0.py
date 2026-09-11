"""
- this is a comparing pairs problem: two pointers
    -  we can have a left starting at prices[0] and right at prices[1]. while in range, if r > l (profitable), calc the profit and then compare with the current max. if l < r: not profitable so move l to right (bc r is cheaper so better profit). in any case, update r by 1, so pointers dont overlap.
    - this is one pass, so O(n) 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices [r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP
        