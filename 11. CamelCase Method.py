"""
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings.
All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
"""


def camel_case(string):
    return ''.join(i.capitalize() for i in string.split())

print(camel_case('ddd ddd dddsd a'))


# def camel_case(string):
#     return string.title().replace(" ", "")
