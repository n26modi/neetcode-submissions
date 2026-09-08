"""
-input: int array (nums)
    - return all triplets that add to 0. 
-output: a array with 3 elements
- contraints: dont return duplicate triplets

brute force: for i in nums, check against all possibilites
optimzation: sort array so you can skip duplicates easily. then loop over each array, for each one (i): do a two pointer with the elements to the right (greater values) but skip over the duplicates. now treat it like two sum with i as the target. if 3sum is higher, then move right pointer inwards one bc its sorted """

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  
                continue    #if duplicate, move on to the next a

            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums [right]])
                    left += 1  #move on to next potential triple
                    right -= 1
                    while nums[left] == nums [left - 1] and left < right:
                        left += 1  # if duplicate move on
        return res

#sorting makes this possible
#rmr to check duplicates both times
