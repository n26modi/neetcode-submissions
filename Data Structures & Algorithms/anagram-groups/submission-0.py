""" 
- input: array of strings. ["str", "trs", "make"]
- group all of the anagrams (same count of each characters, meaning same length also) in a subarray. 

- ex:   Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

- brute force/intution: for each str, count the occurances of each char and store in a hashmap. compare it with all other str's

- optmization: have a hashmap with keys == each strings char occurances, and values == list of those strings with the same char occurances (anagrams)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) #map charCount to List of Anagrams

        for i in strs:
                count = [0] * 26
                for j in i:
                        count[ord(j) - ord("a")] += 1
                anagrams[tuple(count)].append(i)
        return list(anagrams.values())

# defaultdict automatically assigns a default value to a key that does not exist yet. "(list)" means any missing key automatically gets initialized as an empty list []. 
# idea: for each str in input, create a counts list to count how many times each letter occurs. 
# "ord" gets the acscii value of each letter, and subtracting the ascii value for "a" maps it to index 0 - 25
# then we use the count for each str as the key for our hash, so everytime another str has the same counts, we add it to the list for that key. (gotta use tuple cuz its hashable)
# finally, return the values of the hash in list form