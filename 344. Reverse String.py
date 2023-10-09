"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        s_rev = [s[i] for i in range((len(s)-1), -1, -1)]
        for i in range(len(s_rev)):
            s[i] = s_rev[i]

s = ["h","e","l","l","o"]
reverseString(s)