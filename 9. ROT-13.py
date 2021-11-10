"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
after it in the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there
are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13
"implementation".

Please note that using encode is considered cheating.
"""

# from string import ascii_letters


def rot13(string):

    alf_one = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alf_two = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    new_string = ''

    for letter in string:
        if letter.isalpha():
            new_string += alf_two[alf_one.index(letter)]
        else:
            new_string += letter
    return new_string


print('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(rot13('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
