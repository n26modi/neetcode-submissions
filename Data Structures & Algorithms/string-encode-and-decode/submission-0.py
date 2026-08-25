"""
- input: list of strings (strs)
    - write encode() to encode the list of strings into a strings
        - decode() decode's it back to og list of strings

 - ex: strs = ["hey", "im", "nishant"]
        - encode(strs) --> "hey im nishant"
        - decode(strs) --> ["hey", "im", "nishant"]

-brute force/intution: encode the list of strings using .join(,), and decode them (idk how)
- optimization: encode them by appending them to a result list then joining using .join(), but also append the int length of each string follwed by a delimiter(a special char to seperate strings), so when i decode, I can seperate strings after the int length of each string """

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res) # empty qoutes = nothing, so elements from  res are glued directly together(seperator is nothing)
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0    #what position in the input string r we currently on
        
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #len of element is string from i to j
            i = j + 1
            j = i + length
            res.append(s[i:j]) #add string as an element in result
            i = j
        return res
            
           
# kinda hard



