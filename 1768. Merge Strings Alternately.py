"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

"""

def mergeAlternately(word1, word2):
    merged_list = []
    r = max(len(word1), len(word2))

    for i in range(r):
        try:
            merged_list.append(word1[i])
        except:
            pass
        try:
            merged_list.append(word2[i])
        except:
            pass
    return ''.join(merged_list)

word1 = "ab"
word2 = "pqr"
print(mergeAlternately(word1, word2))