from collections import defaultdict

nums = [4,1,-1,2,-1,2,3]
k = 2

num_dict = defaultdict(int)

for n in nums:
    if n in num_dict:
        num_dict[n] += 1
    else:
        num_dict[n] = 1

sorted_dict = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)
print(list(sorted_dict.keys())[:k])