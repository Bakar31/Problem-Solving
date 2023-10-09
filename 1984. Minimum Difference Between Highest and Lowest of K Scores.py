"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. 
You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and 
the lowest of the k scores is minimized.

Return the minimum possible difference.

Input: nums = [90], k = 1
Output: 0

Input: nums = [9,4,1,7], k = 2
Output: 2
    """

def minimumDifference(nums, k):
    nums.sort()
    l, r = 0, k-1
    res = float('inf')

    while r < len(nums):
        res = min(res, nums[r] - nums[l])
        l, r = l+1, r+1
    return res

nums = [9,4,1,7]
k = 2
print(minimumDifference(nums, k))