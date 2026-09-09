"""
input: array of ints(heights), where each index is the height of ith bar
    - trying to return max amt of water, so highest lxw
output: int 

* width is the difference between the two indices 

brute force: u can go through each i with a for loop, and compare against each other index by taking the min height as the lentgh and the diff btwn indices as the width. but this is o(n^2)

optimization: if we want to do this in one pass, we can use two pointers to track. track and update the max.  """

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            area = min(heights[l], heights[r]) * width 
            res = max(area, res) #update res if this pair is higher

            if heights[l] >= heights[r]: 
                r -= 1
            else:
                l += 1

        return res

#height is limited by shorter bar, so to potentially increase area, increase the shorter bar. by always moving the shorter side, we explore all meaningful possibilities
