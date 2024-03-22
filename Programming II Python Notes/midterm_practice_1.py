def is_palindrome(word):
    # To handle numbers, if the input isn't a string, convert it to one.
    str_word = str(word)
    # Check that the word equals the reverse of itself.
    if str_word == str_word[::-1]:
        return True
    else:
        return False

# Example usage with a number
print(is_palindrome(9847255590886266818998186626880955527489))  #Should the number be a palindrome, the result ought to be True.
print(is_palindrome(1414884937242655719669145562427394884141))  #Return False if the situation is not a palindrome.
print(is_palindrome(6892149109325320763773670235239019412986))
print(is_palindrome(6800923757255865070000705685527573290086))

import random

# Initiate an empty list
random_numbers = [1,2,98,56,48,28]

