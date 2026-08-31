"""
- input: array of ints (nums)
    - return another array (output), where each corresponding index is the product of all other indexes in nums

- ex: Input: nums = [1,2,4,6]
        Output: [48,24,12,8]

-brute force/intiution: create a list of zeros big as len(nums), for each position, go through all other values in nums and multiply. o(n^2) bc were traversing through entire array for each i

- optimization: for each i in nums, calculate the prefix(multiply all the values before i), store at output[i]. then, calculate the postfix(multiply all values AFTER i), and multiply that number with the value already at output[i]. this does the job in 0(n), we can compute all indexes in two passes: 1 for prefix and 1 for postfix"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]  #multiply i to prefix to get new prefix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #start, stop, step
            output[i] *= postfix
            postfix *= nums[i]
        return output

# postfix range: start at last index, stop at first (-1 means last index), step by -1, which is why -1 means first index in this case