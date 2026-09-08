"""
- input: string (s)
    - if string first letter from left, and first from right are the same, and same for all chars. 
- output: return true or false
-constraints: case-insensitive(.lower)

ex: Input: s = "Was it a car or a cat I saw?"
    Output: true
    Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

brute force: check every characters
optimization: first .lower everything. use two pointers, if left == right, move inwards, until it doesnt, then return false (while loop)

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

# left < right inside each inner loop makes it so u dont walk left straight past right if the string were all punctuation
#   str.isalnum() — returns True if a character is a letter or digit, False for punctuation, spaces, colons, etc. 
# before you compare s[left] and s[right] on each iteration, you first need to nudge each pointer forward/backward past any non-alphanumeric characters. That means an inner while loop for each pointer, guarded so it doesn't run past the other pointer: