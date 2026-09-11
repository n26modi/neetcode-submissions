""" solution 1 is not the most optimal, it was o(n log n). we can do o(n), by using a hashmap with only 1 pass. 
- ex: 
    nums = [2,4,5,3], target = 9
    --> if we store all (val -> index) in hash as we go, by the time we get to element 2 ( the 5), we can subtract it from the target (9), and check if 4 is in the hash yet. if it is, then return the indices of 4 (as the complement and 5 as the current index). """

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # key -> value

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i #add current val:index to hash

# prevMap's key is value, which maps to the index, so if the difference (which rep a number) has been seen before, return the index of complement (prevMap[diff]) and the current index