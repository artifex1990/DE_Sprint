def translete_to_roman(number):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):

        result += number // arabic * roman
        number %= arabic

    return result

print(translete_to_roman(1945))