x = -121

def isPlaindrom(x):
    x = str(x)
    x_reversed = ''.join(list(reversed(x)))
    if x == x_reversed:
        print('True')
    else:
        print('False')

isPlaindrom(x)