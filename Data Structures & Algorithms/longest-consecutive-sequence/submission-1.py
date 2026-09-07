""" 
-input: array of ints (nums)
    - return length of longest consective sequence (exactly 1 greater)  that can be formed (doesnt have to be two elements ina row)
- output: int length
constraint: o(n) time

ex: Input: nums = [2,20,4,10,3,4,5]
    Output: 4
    Explanation: The longest consecutive sequence is [2, 3, 4, 5].

brute force: for each value, check against all values. start at 0, if one is greater by 1, add it to the count and keep going 
optimization: create a set if input array (nums), than loop over initial array. A number is the start of a sequence if num - 1 is not in the set. 
we only want to start counting when we find the beginning of a consecutive sequence.

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0 

        for num in numsSet:
            if (num - 1) not in numsSet: #if num is start of conseq seq
                length = 1
                while (num + length) in numsSet:
                    length += 1
                longest = max(length, longest) #max of all conseq seq's
        return longest 
        
#Convert the list into a set numSet for O(1) lookups.
# Initialize longest to track the length of the longest consecutive sequence.
#For each number num in numSet:
#   - Check if num - 1 is not in the set:
#       - If true, num is the start of a sequence.
#       - Initialize length = 1.
#       - While num + length exists in the set, increase length.
#   -Update longest with the maximum length found.
#Return longest after scanning all numbers.
