""" 
- input = array of ints
- if any value is appears twice, return true
    - if no value appears twice, return false

- ex: 
    Input: nums = [1, 2, 3, 3]
    Output: true

- brute force: check each index's value and compare it to all other indexes. O(n**2), not optimal. 

- optimize: since were tracking how often we seen a number, we can use a set for o(n) """

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

# checking for uniqueness, so use a set. 

#init it before loop, and add each value to it. in the loop, before adding the value, check to see if its in the set already. if it is return True, without having to even go through entire array. If True is not returned after loop exits, return False. 
# O(N), only need 1 pass max