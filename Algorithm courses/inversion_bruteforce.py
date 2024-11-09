"""
This Python code calculates the number of inversions in a given array. 
An inversion in an array occurs when a pair of elements at different 
positions have the left element greater than the right element. 
The code iterates through the array and checks each element against all the subsequent elements to count the inversions.

# Main Logic:

Initialize count to 0 for tracking the number of inversions.
Iterate through the array elements using index i.
For each element at index i, create a subarray array2 containing elements that come after it.
Compare the element at index i with each element in array2.
If the element at index i is greater than an element in array2, increment count.
Print the pair of elements forming the inversion.
After both loops, the total count of inversions is stored in count.

Runtime O(n^2)
"""


array = [1, 3, 5, 2, 4, 6]

count = 0
for i in range(len(array)):
    # Create a new subarray array2 starting from the current index i to the end of the original array. This subarray contains all elements that come after the element at index i.
    array2 = array[i:]
    for j in range(len(array2)):
        if array[i] == array2[j]:
            continue
        else:
            if array[i] > array2[j]:
                count += 1
                print(array[i], array2[j])

print(count) 