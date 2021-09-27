"""
Write a function which takes a input string s and return a string in the following way:
                  C|                          R|
                  |O                          n|
                  D|                          d|
   "CODEWARS" =>  |E       "Rnd Te5T"  =>      |
                  W|                          T|
                  |A                          |e
                  R|                          5|
                  S|                          T|

Notes:

List all the Vowels on the right side of |
List every character except Vowels on the left side of |
Return every character in its original case
Each line is seperated with \n
Invalid input ( undefined / null / integer ) should return an empty string
"""
st = "Rnd TE5T"

def sort_vowels(s):
    new_string = ''
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    if type(s) is str:
        for i in s:
            if i in vowels_list:
                new_string += '|' + i + "\n"
            else:
                new_string += i + '|' + "\n"
        return new_string.strip()
    else:
        return new_string


print(sort_vowels(st))

# def sort_vowels(s):
#     return "" if not isinstance(s, str) else "\n".join("|" + x if x in "aeiouAEIOU" else x + "|" for x in s)

# def sort_vowels(s):
#     q = []
#
#     if type(s) != str:
#         return ''
#
#     for i in s:
#         if i in 'aeiouAEIOU':
#             q.append(f'|{i}')
#         else:
#             q.append(f'{i}|')
#
#     return '\n'.join(q)

# def sort_vowels(s):
#     try:
#         return '\n'.join('|' + i if i.lower() in 'aioue' else i + '|' for i in s)
#     except:
#         return ''



