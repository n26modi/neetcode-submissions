""" solution 1 is not the most optimal, it was o(n log n). we can do o(n), by using a hashmap with only 1 pass. 
- ex: 
    nums = [2,4,5,3], target = 9
    --> if we store all elements in hash as we go, by the time we get to element 2 ( the 5), we can subtract it from the target (9), and check if 4 is in the hash yet. if it is, then return those indices. """

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}   # val --> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i] 
            prevMap[num] = i 

# prevMap's key is value, which maps to the index, so if the difference (which rep a number) has been seen before, return the index of complement (prevMap[diff]) and the current index