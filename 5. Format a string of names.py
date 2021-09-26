"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for
the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""


names_list = [{'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Homer'}, {'name': 'Marge'}]


def namelist(names):
    string = ''
    for i in range(len(names)):
        string += names[i]['name']
        if i < len(names) - 2:
            string += ", "
        if i == len(names) - 2:
            string += " & "

    return string


# def namelist(names):
#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
#                                 names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''

# def namelist(names):
#     if len(names)==0: return ''
#     if len(names)==1: return names[0]['name']
#     return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']

# def namelist(names):
#   return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]