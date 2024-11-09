num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(x, y):

    if x < 10 or y < 10:
        return x * y

    x, y =  str(x), str(y)
    n = max(len(x), len(y))
    # n = max(len(str(x)), len(str(y)))
    m = n //2

    a, b = int(x[:-m]), int(x[-m:])
    c, d = int(y[:-m]), int(y[-m:])
    # print(a,b,c,d)

    # a, b = divmod(x, 10**m)
    # c, d = divmod(y, 10**m)
    # print(a,b,c,d)

    # Recursively calculate the three multiplications
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd
    

    # Combine the results using the Karatsuba formula
    result = (ac * 10**(2*m)) + (ad_bc * 10**m) + bd

    return result

result = karatsuba(num1, num2)
print(f"Result obtained: {result}")