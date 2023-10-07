"""
Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.
"""

class DynamicArray():
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int):
        return self.arr[i]
    
    def set(self, i: int, n: int):
        self.arr[i] = n

    def pushback(self, n: int):
        self.arr[self.length] = n
        self.length += 1

    def popback(self):
        self.length -= 1

        return self.arr[self.length]
    
    def resize(self):
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getsize(self):
        return self.length
    
    def getcapacity(self):
        return self.capacity

    
