"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

string = 'Pig latin is cool !'

def pig_it(text):
    new_string = ''
    for i in text.split():
        if i in '!/.#@$%^&*()_=+-?':
            new_string += i + ' '
        else:
            new_string += i[1:] + i[0] + 'ay' + ' '
    return new_string.strip()

print(pig_it(string))


# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# def pig_it(text):
#     return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

# def pig_it(text):
#     res = []
#
#     for i in text.split():
#         if i.isalpha():
#             res.append(i[1:] + i[0] + 'ay')
#         else:
#             res.append(i)
#
#     return ' '.join(res)