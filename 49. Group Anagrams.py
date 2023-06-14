from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

# # Create a dictionary with default value as an empty dictionary
# char_count_dict = defaultdict(dict)

# # Iterate through each element in strs
# for word in strs:
#     # Count the occurrence of each character in the word
#     char_count = {}
#     for char in word:
#         char_count[char] = char_count.get(char, 0) + 1

#     # Assign the character count dictionary to the corresponding element in the main dictionary
#     char_count_dict[word] = char_count

# # Sort the value list for each key in the main dictionary
# sorted_dict = {key: sorted(value.items()) for key, value in char_count_dict.items()}


# new_dict = {}

# # Iterate over the original dictionary
# for key, value in sorted_dict.items():
#     # Convert the value tuple/list to a tuple of tuples
#     value = tuple(value)
    
#     # Check if the value already exists in the new dictionary
#     if value in new_dict:
#         new_dict[value].append(key)  # Append the key to the existing list
#     else:
#         new_dict[value] = [key]  # Create a new list with the key as the value

# # # Print the resulting dictionary
# # for key, value in new_dict.items():
# #     print(key, value)

# print(new_dict.values())

final_dict = defaultdict(list)
for s in strs:
    count = [0] * 26
    
    for char in s:
        count[ord(char) - ord("a")] += 1
    final_dict[tuple(count)].append(s)
    
print(final_dict.values())