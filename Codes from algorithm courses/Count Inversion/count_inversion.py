with open('G:/Python/LeetCode/Codes from algorithm courses/Count Inversion/IntegerArray.txt') as f:
    a = [int(x) for x in f]

def CountSplitInv(B, C):
    i = 0
    j = 0
    count = 0
    D = []
    while i < len(B) and j < len(C):
        D.extend([min(B[i], C[j])])
        if B[i] < C[j]:
            i = i + 1
        else:
            count += len(B[i:])
            j += 1
    D.extend(B[i:])
    D.extend(C[j:])
    Z = count
    return D, Z

def Sort_Count(A):
    n = len(A)
    if n > 1:
        splitposition = int(n / 2)  # Convert splitposition to an integer
        B, X = Sort_Count(A[:splitposition])  # Corrected slice
        C, Y = Sort_Count(A[splitposition:])  # Corrected slice
        D, Z = CountSplitInv(B, C)
        return D, X + Y + Z
    else:
        return A, 0

_, c = Sort_Count(a)
print(c)
