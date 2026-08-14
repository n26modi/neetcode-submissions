class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
            
            
#to be anagram, both must be same length. Since we want to count how many times each character appears (both strings must have same counts of each char), we use hashmap. 

# since both r same length, we can iterate over indices instead of values, so we only have to loop once. Add each value of s to s's hash, and each value of t to t's hash. 

#get returns value for certain key, but can handle default value with second parameter in case of the first string

# "==" for dict's checks if both have the exact same set of keys, and if the values paired with those keys are identical. Order does not matter: {'a': 1, 'b': 2} == {'b': 2, 'a': 1} returns True.
        