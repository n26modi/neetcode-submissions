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
            
        