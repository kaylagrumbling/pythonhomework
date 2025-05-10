#  1. Even or odd Creates a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

# 2. Convert a Number to a String this is a  function that can transform a number (integer) into a string.
def number_to_string(num):
    return str(num)

# 3. Remove String Spaces this is a function that removes the spaces from the string, then return the resultant string.
def no_space(x):
    return x.replace(" ", "")

# 4.Vowel Count this Returns the number (count) of vowels in the given string.
def getCount(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
