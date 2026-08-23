"""
- input: arrary of ints (nums), int (k)
    - return the k most frequent elements in the arrary 

- ex:       Input: nums = [1,2,2,3,3,3], k = 2
                    Output: [2,3] 
       - asks for the 2 most frequent elemts. 3 is the most frequent,   and 2 is the second most, so return both. 

-brute force: go through array, count the occurances of each char, and return the k top elements. (use hashmap to count)

- optimzation: asks for top k elements -> use min Heap. use frequency hashmap intitially to count how many times each num appears, and then create an empty min heap. For eac num in freq map, push tuple "(freq, num)" to the heap and if heap becomes greater then k, pop once to remove the smallest frequency. After all elements, heap contains k most freq elements!"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        heap = []
        for i in freq.keys():
            heapq.heappush(heap, (freq[i], i))
            if len(heap) > k :
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
# heap.push() takes only 2 args; where ur pushing to and what ur pushing, so push a tuple
#(heap)[1] appends the actual values, which is what we want
            