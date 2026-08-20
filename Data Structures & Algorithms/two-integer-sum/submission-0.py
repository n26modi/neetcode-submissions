""" 
- inputs: array of ints (nums), int (target)
- return the indices(i, j) of the values that add up to target. return the answer with the smaller index first. 

- ex: 
    nums = [3,4,5,6], target = 7

    Output: [0,1]

- brute force: check each combination of values with a nested for loop. this is o(n**2), too slow. 
-  optimization: we can use 2-pointers, but have to sort array first (ascending order). 1 pointer at start, another at end. if the current sum is less then the target, we move the left pointer 1 index right, which would result in a higher target (bc it is sorted). if sum was more, we move the right pointer left. """

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = []  
        for i, num in enumerate(nums):
            indexed.append([num, i])
        indexed = sorted(indexed)

        left, right = 0, len(indexed) - 1
        while left < right: 
            cur = indexed[left][0] + indexed[right][0]
            if cur == target:
                return sorted([indexed[left][1], indexed[right][1]])
            elif cur < target:
                left += 1
            else: 
                right -= 1
            

#if u sort the og list, u cant return the og index of the values that add to the target, so make a new one and sort it. 
# sorted on the index returns it in ascending order, so smaller index first, as required
