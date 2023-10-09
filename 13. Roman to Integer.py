romantointdict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def romantoint(roman):
    if len(roman) == 1:
        print(romantointdict[roman])
    
    else:
        number = 0
        for i in roman:
            print(romantointdict[i])
            number += romantointdict[i]
        
        print(number)

romantoint('MCMXCIV')