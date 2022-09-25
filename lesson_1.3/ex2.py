def is_palindrome(str):
    str = str.replace(" ", "")
    return str == str[::-1]

print(is_palindrome("taco cat"))
print(is_palindrome("rotator"))
print(is_palindrome("black cat"))