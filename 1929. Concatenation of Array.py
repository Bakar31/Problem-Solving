"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
"""

def getConcatenation(nums):
    nums2 = [0] * (2 * len(nums))
    
    for i, j in enumerate(nums):
        nums2[i] = j
        nums2[i + len(nums)] = j
    return nums2

nums = [1,2,1]
num2 = getConcatenation(nums)
print(num2)