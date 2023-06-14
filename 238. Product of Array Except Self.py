# conditions: You must write an algorithm that runs in O(n) time and without using the division operation.

""" 
case 1: Input: nums = [1,2,3,4], Output: [24,12,8,6]
case 2: Input [0,0], expected output: [0,0]

"""

# 1st try failed (Time Limit Exceeded)

from collections import defaultdict
import numpy

nums = [1,2,3,4]

mul_list = [1]*len(nums)
prefix_list = [1]*len(nums)
postfix_list = [1]*len(nums)

# for i, j in enumerate(nums):
#     new_nums = nums.copy()
#     new_nums.remove(j)
#     mul_list[i] = numpy.prod(new_nums)

# print(mul_list)

# 2nd try:

prefix = 1
postfix = 1

for i in range(len(nums)):
    prefix_list[i] = prefix * nums[i]
    prefix = prefix_list[i]

prefix_list.insert(0, 1)
print(prefix_list)

for i in range(len(nums) -1, -1, -1):
    postfix_list[i] = postfix * nums[i]
    postfix = postfix_list[i]

postfix_list.append(1)
print(postfix_list)

for i in range(len(nums)):
    mul_list[i] = prefix_list[i] * postfix_list[i+1]

print(mul_list)