"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a
hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that
fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r, g, b):
    values = [r, g, b]
    res = ''
    for i in values:
        if i > 255:
            i = 255
        if i <= 0:
            i = 0
            res += "0"
        if 0 < i < 16:
            res += "0"
        res += hex(i)[2:4]
    return res.upper()


print(rgb(255, 255, 255))
print(rgb(148, 0, 211))
print(rgb(-148, 0, 400))
print(rgb(15, 5, 3))
