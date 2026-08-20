""" 
- input = 2 strings (s and t)
- if they are anagrams (each char appears the same num of times, regardless or order), return True
    - If they are not(if each char doesnt appear exactly the same num of times), return False

- ex: 
    Input: s = "racecar", t = "carrace"
    Output: true

- Brute Force: count each char in each string, and compare the counts of each char. requires len(s) + len(t) passes

- optimize: firstly, s and t need to be exact same length for them to be anagrams. if they are, we want to track each char and the amt of times they appear. so use a hashmap to track seen. since there the same length, we can iterate over index, with only 1 pass for each."""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0 ) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT

#  Add each value of s to s's hash, and each value of t to t's hash.
# get() returns value for certain key, but can handle default value with second parameter in case of the first string

# "==" for dict's checks if both have the exact same set of keys, and if the values paired with those keys are identical. Order does not matter: {'a': 1, 'b': 2} == {'b': 2, 'a': 1} returns True.
           
# btw: this does the same thing:
# -->  from collections import Counter

#   class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        return Counter(s) == Counter(t)
