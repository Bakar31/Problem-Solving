from collections import defaultdict

nums = [-1,1,0,-3,3]
mul_dict = []

for i in nums:
    new_nums = nums.copy()
    new_nums.remove(i)
    print(new_nums)

    mul = 1
    for j in new_nums:
        mul = mul*j
    print(mul)
    # mul_dict[i] = mul
    mul_dict.append(mul)

print(mul_dict)
# print(list(mul_dict.values()))